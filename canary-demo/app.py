"""
Canary Release Demo Flask App

This app demonstrates a canary release pattern where a new feature
is gradually rolled out to a percentage of users.

DEPLOYMENT INSTRUCTIONS:
========================

LOCAL SETUP:
-----------
1. Install dependencies:
   pip install -r requirements.txt

2. Create a .env file with:
   SHOW_NEW_FEATURE=true
   CANARY_PERCENTAGE=10

3. Run locally:
   python app.py
   OR
   gunicorn app:app

RAILWAY DEPLOYMENT (RECOMMENDED):
---------------------------------
1. Install Railway CLI:
   npm i -g @railway/cli

2. Login to Railway:
   railway login

3. Initialize and deploy:
   railway init
   railway up

4. Set environment variables:
   railway variables set SHOW_NEW_FEATURE=true
   railway variables set CANARY_PERCENTAGE=10

5. Generate domain:
   Go to dashboard → Settings → Networking → Generate Domain

6. View logs:
   railway logs

HEROKU DEPLOYMENT:
-----------------
1. Install Heroku CLI and login:
   heroku login

2. Create a new Heroku app:
   heroku create your-app-name

3. Deploy to Heroku:
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main

4. Set environment variables (config vars):
   heroku config:set SHOW_NEW_FEATURE=true
   heroku config:set CANARY_PERCENTAGE=10

5. View your app:
   heroku open

6. View logs:
   heroku logs --tail

FEATURE FLAG CONTROL:
--------------------
Railway:
- Enable feature for all users:
  railway variables set SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=100
- Enable feature for 10% (canary):
  railway variables set SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=10
- Disable feature completely:
  railway variables set SHOW_NEW_FEATURE=false

Heroku:
- Enable feature for all users:
  heroku config:set SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=100
- Enable feature for 10% (canary):
  heroku config:set SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=10
- Disable feature completely:
  heroku config:set SHOW_NEW_FEATURE=false

ROLLBACK STRATEGIES:
-------------------
Railway:
1. Quick rollback - disable feature flag:
   railway variables set SHOW_NEW_FEATURE=false
2. Rollback to previous deployment:
   Go to dashboard → Deployments → Click rollback

Heroku:
1. Quick rollback - disable feature flag:
   heroku config:set SHOW_NEW_FEATURE=false
2. Rollback to previous deployment:
   heroku releases
   heroku rollback v[VERSION_NUMBER]
3. Emergency rollback:
   heroku maintenance:on
   heroku rollback
   heroku maintenance:off

"""

import os
import random
from flask import Flask, request
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

app = Flask(__name__)

# Configuration
SHOW_NEW_FEATURE = os.getenv('SHOW_NEW_FEATURE', 'false').lower() == 'true'

_raw_canary = os.getenv("CANARY_PERCENTAGE", "10")
try:
    CANARY_PERCENTAGE = int(str(_raw_canary).strip().lstrip("="))
except ValueError:
    CANARY_PERCENTAGE = 10

CANARY_PERCENTAGE = max(0, min(100, CANARY_PERCENTAGE))

# Store user session to maintain consistency
# In production, you'd use Redis or a proper session store
user_feature_map = {}


def should_show_new_feature(user_id):
    """
    Determine if a user should see the new feature based on canary percentage.
    
    This function ensures the same user consistently sees (or doesn't see)
    the new feature by caching the decision per user session.
    
    Args:
        user_id: Unique identifier for the user (IP address or session ID)
    
    Returns:
        bool: True if user should see new feature, False otherwise
    """
    if not SHOW_NEW_FEATURE:
        return False
    
    # Check if we've already decided for this user
    if user_id in user_feature_map:
        return user_feature_map[user_id]
    
    # Determine if user is in the canary group (based on percentage)
    in_canary_group = random.randint(1, 100) <= CANARY_PERCENTAGE
    user_feature_map[user_id] = in_canary_group
    
    return in_canary_group


@app.route('/')
def home():
    """
    Main route that shows either the old or new feature based on canary settings.
    """
    # Use IP address as user identifier (in production, use session ID or user ID)
    user_id = request.remote_addr or 'default'
    
    if should_show_new_feature(user_id):
        return f"""
        <html>
            <head>
                <title>Canary Demo - New Feature</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                    }}
                    .content {{
                        text-align: center;
                        font-size: 3em;
                        animation: fadeIn 1s;
                    }}
                    @keyframes fadeIn {{
                        from {{ opacity: 0; transform: translateY(-20px); }}
                        to {{ opacity: 1; transform: translateY(0); }}
                    }}
                    .badge {{
                        font-size: 0.3em;
                        background: rgba(255, 255, 255, 0.2);
                        padding: 5px 10px;
                        border-radius: 5px;
                        margin-top: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="content">
                    🎉 New Feature Active!
                    <div class="badge">Canary Release - {CANARY_PERCENTAGE}% rollout</div>
                </div>
            </body>
        </html>
        """
    else:
        return f"""
        <html>
            <head>
                <title>Canary Demo - Classic</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background: #f0f0f0;
                        color: #333;
                    }}
                    .content {{
                        text-align: center;
                        font-size: 3em;
                    }}
                    .badge {{
                        font-size: 0.3em;
                        background: #ddd;
                        padding: 5px 10px;
                        border-radius: 5px;
                        margin-top: 20px;
                        color: #666;
                    }}
                </style>
            </head>
            <body>
                <div class="content">
                    Hello, World!
                    <div class="badge">Classic Version</div>
                </div>
            </body>
        </html>
        """


@app.route('/health')
def health():
    """Health check endpoint for monitoring."""
    return {
        'status': 'healthy',
        'feature_flag_enabled': SHOW_NEW_FEATURE,
        'canary_percentage': CANARY_PERCENTAGE
    }


@app.route('/config')
def config():
    """Display current configuration (for debugging)."""
    return {
        'SHOW_NEW_FEATURE': SHOW_NEW_FEATURE,
        'CANARY_PERCENTAGE': CANARY_PERCENTAGE,
        'active_users': len(user_feature_map),
        'users_with_new_feature': sum(1 for v in user_feature_map.values() if v)
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
