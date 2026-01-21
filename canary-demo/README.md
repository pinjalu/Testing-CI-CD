# 🎯 Canary Release Demo - Flask App

A demonstration of canary release patterns using Python Flask. This app shows how to gradually roll out new features to a percentage of users using feature flags and randomization.

**✨ Now supports both Railway and Heroku deployment!**

## 📋 Features

- **Feature Flag System**: Control features via environment variables
- **Canary Release**: Gradually roll out features to a percentage of users (default: 10%)
- **Consistent User Experience**: Same user always sees the same version during their session
- **Health Check Endpoint**: Monitor app status and configuration
- **Beautiful UI**: Different designs for old and new features
- **Production Ready**: Configured for Railway and Heroku deployment with gunicorn
- **Easy Deploy**: Works with Railway, Heroku, or any platform supporting Python

## 🚀 Quick Start - Local Development

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Environment File

Create a `.env` file in the project root:

```env
SHOW_NEW_FEATURE=true
CANARY_PERCENTAGE=10
PORT=5000
```

### 3. Run the App

```bash
# Option 1: Development server
python app.py

# Option 2: Production server (gunicorn)
gunicorn app:app
```

Visit `http://localhost:5000` in your browser. Refresh multiple times to see the canary release in action!

## 🌐 Deployment Options

### Option 1: Railway Deployment (Recommended - Easier!)

Railway is a modern platform with a generous free tier and simpler deployment process.

#### Quick Deploy with Railway

1. **Visit Railway**: Go to [railway.app](https://railway.app)

2. **Sign up/Login**: Use GitHub, Discord, or email

3. **Deploy from GitHub**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect it's a Python app!

4. **Or Deploy via CLI**:
   ```bash
   # Install Railway CLI
   npm i -g @railway/cli
   
   # Login
   railway login
   
   # Initialize project
   railway init
   
   # Deploy
   railway up
   ```

5. **Set Environment Variables**:
   - Go to your project dashboard
   - Click "Variables" tab
   - Add:
     - `SHOW_NEW_FEATURE` = `true`
     - `CANARY_PERCENTAGE` = `10`

6. **Generate Domain**:
   - Go to "Settings" → "Networking"
   - Click "Generate Domain"
   - Your app is live! 🎉

#### Railway Commands

```bash
# View logs
railway logs

# Open app in browser
railway open

# View environment variables
railway variables

# Set environment variable
railway variables set SHOW_NEW_FEATURE=true
railway variables set CANARY_PERCENTAGE=10
```

### Option 2: Heroku Deployment

#### Initial Setup

1. **Install Heroku CLI** (if not already installed):
   ```bash
   # Visit: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**:
   ```bash
   heroku create your-app-name
   ```

#### Deploy the App

```bash
# Initialize git repository (if not done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial canary demo deployment"

# Deploy to Heroku
git push heroku main
```

#### Configure Environment Variables

```bash
# Enable feature flag with 10% rollout (canary)
heroku config:set SHOW_NEW_FEATURE=true
heroku config:set CANARY_PERCENTAGE=10

# View current config
heroku config
```

#### Open and Monitor

```bash
# Open the app in browser
heroku open

# View logs in real-time
heroku logs --tail
```

## 🎛️ Feature Flag Control

### Gradual Rollout Strategy

**Railway:**
```bash
# Phase 1: Canary (10% of users)
railway variables set SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=10

# Phase 2: Expand (25% of users)
railway variables set CANARY_PERCENTAGE=25

# Phase 3: Half rollout (50% of users)
railway variables set CANARY_PERCENTAGE=50

# Phase 4: Majority (75% of users)
railway variables set CANARY_PERCENTAGE=75

# Phase 5: Full rollout (100% of users)
railway variables set CANARY_PERCENTAGE=100

# Emergency: Disable feature completely
railway variables set SHOW_NEW_FEATURE=false
```

**Heroku:**
```bash
# Phase 1: Canary (10% of users)
heroku config:set SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=10

# Phase 2: Expand (25% of users)
heroku config:set CANARY_PERCENTAGE=25

# Phase 3: Half rollout (50% of users)
heroku config:set CANARY_PERCENTAGE=50

# Phase 4: Majority (75% of users)
heroku config:set CANARY_PERCENTAGE=75

# Phase 5: Full rollout (100% of users)
heroku config:set CANARY_PERCENTAGE=100

# Emergency: Disable feature completely
heroku config:set SHOW_NEW_FEATURE=false
```

## 🔄 Rollback Strategies

### Strategy 1: Quick Rollback (Feature Flag) ⚡

**Fastest method** - Disable the feature flag:

**Railway:**
```bash
railway variables set SHOW_NEW_FEATURE=false
```

**Heroku:**
```bash
heroku config:set SHOW_NEW_FEATURE=false
```

**Pros**: Instant, no code deployment needed  
**Use when**: Feature has bugs but code is stable

### Strategy 2: Reduce Rollout Percentage

Reduce exposure while investigating:

**Railway:**
```bash
# Reduce to 5% while investigating
railway variables set CANARY_PERCENTAGE=5

# Or 1% for minimal exposure
railway variables set CANARY_PERCENTAGE=1
```

**Heroku:**
```bash
# Reduce to 5% while investigating
heroku config:set CANARY_PERCENTAGE=5

# Or 1% for minimal exposure
heroku config:set CANARY_PERCENTAGE=1
```

### Strategy 3: Full Deployment Rollback

Rollback to a previous release:

**Railway:**
```bash
# Railway automatically keeps deployment history
# Go to dashboard → Deployments → Click "Rollback" on previous deployment
# Or redeploy a specific commit:
railway up --service your-service-name
```

**Heroku:**
```bash
# View release history
heroku releases

# Rollback to specific version
heroku rollback v42

# Or rollback to previous version
heroku rollback
```

**Use when**: Code itself has issues

### Strategy 4: Emergency Actions

For critical issues:

**Railway:**
```bash
# Railway doesn't have maintenance mode, but you can:
# 1. Pause the service in the dashboard
# 2. Or set feature flag to false immediately
railway variables set SHOW_NEW_FEATURE=false
```

**Heroku:**
```bash
# Enable maintenance mode
heroku maintenance:on

# Rollback
heroku rollback

# Disable maintenance mode
heroku maintenance:off
```

## 📊 Monitoring Endpoints

### Health Check
```
GET /health
```

Returns app status and configuration:
```json
{
  "status": "healthy",
  "feature_flag_enabled": true,
  "canary_percentage": 10
}
```

### Configuration Info
```
GET /config
```

Returns detailed configuration:
```json
{
  "SHOW_NEW_FEATURE": true,
  "CANARY_PERCENTAGE": 10,
  "active_users": 42,
  "users_with_new_feature": 4
}
```

## 🧪 Testing the Canary Release

### Local Testing

1. Start the app with `CANARY_PERCENTAGE=50`
2. Open the app in multiple browser windows (or incognito tabs)
3. You should see approximately 50% showing the new feature

### Testing Different Scenarios

```bash
# Test 100% rollout
SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=100 python app.py

# Test feature disabled
SHOW_NEW_FEATURE=false python app.py

# Test 10% canary
SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=10 python app.py
```

## 📁 Project Structure

```
canary-demo/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku/Railway process configuration
├── railway.json       # Railway-specific configuration
├── runtime.txt        # Python version specification
├── env.sample         # Example environment variables
├── .gitignore         # Git ignore rules
├── run_local.sh       # Quick start script (Mac/Linux)
├── run_local.bat      # Quick start script (Windows)
└── README.md          # This file
```

## 🛠️ Technical Details

### How Canary Release Works

1. **User Identification**: Each user is identified by their IP address
2. **Random Selection**: On first visit, user is randomly assigned to canary group based on percentage
3. **Consistency**: User's assignment is cached for consistent experience during session
4. **Feature Flag**: Master switch to enable/disable feature entirely

### Production Considerations

For production use, consider:

- **Persistent Storage**: Use Redis or database instead of in-memory dictionary
- **User Authentication**: Use actual user IDs instead of IP addresses
- **Analytics**: Add logging/metrics to track feature adoption and errors
- **A/B Testing**: Extend to support multiple variants
- **Gradual Rollout Schedule**: Automate percentage increases over time

## 🔧 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SHOW_NEW_FEATURE` | No | `false` | Master switch for new feature |
| `CANARY_PERCENTAGE` | No | `10` | Percentage of users seeing new feature (1-100) |
| `PORT` | No | `5000` | Port number for the application |

## 📝 Common Commands

```bash
# Local development
python app.py                    # Run development server
gunicorn app:app                # Run production server locally

# Railway management
railway logs                    # View real-time logs
railway variables               # View all environment variables
railway status                  # Check deployment status
railway open                    # Open app in browser
railway up                      # Deploy current code

# Heroku management
heroku logs --tail              # View real-time logs
heroku config                   # View all config vars
heroku releases                 # View deployment history
heroku ps                       # Check dyno status
heroku restart                  # Restart the app

# Git operations
git status                      # Check changes
git add .                       # Stage all changes
git commit -m "message"         # Commit changes
git push heroku main            # Deploy to Heroku (if using Heroku)
git push origin main            # Deploy to Railway (if connected to GitHub)
```

## 🐛 Troubleshooting

### App not starting?

**Railway:**
```bash
railway logs
railway status
# Check dashboard for build errors
```

**Heroku:**
```bash
heroku logs --tail
heroku ps
heroku restart
```

### Feature flag not working?

**Railway:**
```bash
# Check current configuration
railway variables

# Or check in the Railway dashboard under Variables tab
```

**Heroku:**
```bash
# Check current configuration
heroku config

# Verify the values are set correctly
heroku config:get SHOW_NEW_FEATURE
heroku config:get CANARY_PERCENTAGE
```

### Want to test locally with different settings?

```bash
# Override environment variables for single run
SHOW_NEW_FEATURE=true CANARY_PERCENTAGE=50 python app.py
```

### Railway vs Heroku: Which to choose?

| Feature | Railway | Heroku |
|---------|---------|--------|
| **Free Tier** | ✅ $5/month credit | ❌ No free tier |
| **Ease of Use** | ⭐⭐⭐⭐⭐ Very easy | ⭐⭐⭐⭐ Easy |
| **Auto-deploy** | ✅ GitHub integration | ✅ GitHub integration |
| **CLI** | ✅ Modern CLI | ✅ Mature CLI |
| **Best For** | New projects, hobbyists | Production apps |

**Recommendation**: Start with Railway for its simplicity and free tier!

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Railway Documentation](https://docs.railway.app/)
- [Railway Python Guide](https://docs.railway.app/guides/python)
- [Heroku Python Guide](https://devcenter.heroku.com/categories/python-support)
- [Feature Flags Best Practices](https://www.martinfowler.com/articles/feature-toggles.html)
- [Canary Deployments](https://martinfowler.com/bliki/CanaryRelease.html)

## 📄 License

This is a demo project for educational purposes. Feel free to use and modify as needed!

---

**Happy Deploying! 🚀**
