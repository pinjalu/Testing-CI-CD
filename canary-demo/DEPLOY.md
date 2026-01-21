# 🚀 Quick Deployment Guide

Choose your deployment platform:

## 🟢 Railway (Recommended for Beginners)

### Why Railway?
- ✅ $5/month free credit (enough for small projects)
- ✅ Super simple deployment
- ✅ Auto-deploys from GitHub
- ✅ Modern dashboard
- ✅ Fast deployment

### Deploy in 3 Steps:

**Step 1: Create Account**
- Go to [railway.app](https://railway.app)
- Sign up with GitHub

**Step 2: Deploy**
```bash
# Option A: From GitHub (easiest)
1. Push your code to GitHub
2. In Railway: New Project → Deploy from GitHub
3. Select your repo
4. Done! Railway auto-detects Python

# Option B: Using CLI
npm i -g @railway/cli
railway login
railway init
railway up
```

**Step 3: Configure**
```bash
# Set environment variables
railway variables set SHOW_NEW_FEATURE=true
railway variables set CANARY_PERCENTAGE=10

# Generate public URL
# Go to dashboard → Settings → Generate Domain

# View your app
railway open
```

### Railway Commands Cheat Sheet

```bash
railway login              # Login to Railway
railway init               # Initialize project
railway up                 # Deploy current code
railway logs               # View logs
railway open               # Open app in browser
railway variables          # List environment variables
railway variables set KEY=value  # Set variable
railway status             # Check deployment status
railway link               # Link local project to Railway
```

---

## 🟣 Heroku (Industry Standard)

### Why Heroku?
- ✅ Battle-tested and reliable
- ✅ Extensive documentation
- ✅ Great for production apps
- ⚠️ No free tier (paid plans only)

### Deploy in 5 Steps:

**Step 1: Install CLI**
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Login**
```bash
heroku login
```

**Step 3: Create App**
```bash
heroku create your-app-name
```

**Step 4: Deploy**
```bash
git init
git add .
git commit -m "Deploy canary demo"
git push heroku main
```

**Step 5: Configure**
```bash
heroku config:set SHOW_NEW_FEATURE=true
heroku config:set CANARY_PERCENTAGE=10
heroku open
```

### Heroku Commands Cheat Sheet

```bash
heroku login               # Login to Heroku
heroku create [name]       # Create new app
heroku apps                # List your apps
heroku logs --tail         # View real-time logs
heroku open                # Open app in browser
heroku config              # List environment variables
heroku config:set KEY=val  # Set variable
heroku config:get KEY      # Get variable value
heroku ps                  # Check dyno status
heroku restart             # Restart app
heroku releases            # View release history
heroku rollback            # Rollback to previous release
heroku maintenance:on      # Enable maintenance mode
heroku maintenance:off     # Disable maintenance mode
```

---

## 🎛️ Managing Feature Flags

### Railway

```bash
# Canary release (10%)
railway variables set CANARY_PERCENTAGE=10

# Expand to 50%
railway variables set CANARY_PERCENTAGE=50

# Full rollout
railway variables set CANARY_PERCENTAGE=100

# Disable feature
railway variables set SHOW_NEW_FEATURE=false

# View all variables
railway variables
```

### Heroku

```bash
# Canary release (10%)
heroku config:set CANARY_PERCENTAGE=10

# Expand to 50%
heroku config:set CANARY_PERCENTAGE=50

# Full rollout
heroku config:set CANARY_PERCENTAGE=100

# Disable feature
heroku config:set SHOW_NEW_FEATURE=false

# View all config
heroku config
```

---

## 🔄 Quick Rollback

### Railway

**Method 1: Feature Flag**
```bash
railway variables set SHOW_NEW_FEATURE=false
```

**Method 2: Dashboard**
- Go to Deployments tab
- Click "Rollback" on previous successful deployment

### Heroku

**Method 1: Feature Flag**
```bash
heroku config:set SHOW_NEW_FEATURE=false
```

**Method 2: Release Rollback**
```bash
heroku releases          # See history
heroku rollback v42      # Rollback to specific version
heroku rollback          # Rollback to previous
```

---

## 📊 Monitoring

### Railway

```bash
railway logs             # View logs
railway status           # Check status

# Or use the dashboard
# Visit: railway.app/dashboard
```

### Heroku

```bash
heroku logs --tail       # Real-time logs
heroku ps                # Check dyno status

# Or use the dashboard
# Visit: dashboard.heroku.com
```

### Health Endpoint

Both platforms can access:
- `https://your-app-url/health` - Health check
- `https://your-app-url/config` - Current configuration

---

## 💰 Pricing Comparison

| Feature | Railway | Heroku |
|---------|---------|--------|
| **Free Tier** | $5/month credit | None |
| **Starter** | $5/month | $7/dyno/month |
| **Hobby Project** | ~$5/month | ~$7-25/month |
| **Small Production** | ~$20/month | ~$25-50/month |
| **Auto-sleep** | No | No (hobby tier) |

**Recommendation**: 
- **Learning/Hobby**: Railway (better free tier)
- **Production**: Either works (Heroku more established, Railway more modern)

---

## 🆘 Troubleshooting

### Railway Issues

**App not deploying?**
```bash
railway logs             # Check for errors
railway status
```

**Environment variables not working?**
```bash
railway variables        # Verify they're set
# Or check dashboard → Variables tab
```

**Need to restart?**
```bash
# Redeploy
railway up
# Or trigger redeploy from dashboard
```

### Heroku Issues

**App not starting?**
```bash
heroku logs --tail       # Check for errors
heroku ps                # Check dyno status
heroku restart           # Restart if needed
```

**Config vars not working?**
```bash
heroku config            # Verify they're set
heroku config:get SHOW_NEW_FEATURE
```

**Slug size too large?**
```bash
# Check .slugignore file
# Remove unnecessary files
```

---

## 🎯 Quick Reference: Deploy New Changes

### Railway

```bash
# If using GitHub auto-deploy
git add .
git commit -m "Update feature"
git push origin main
# Railway auto-deploys!

# If using CLI
railway up
```

### Heroku

```bash
git add .
git commit -m "Update feature"
git push heroku main
```

---

## 📞 Getting Help

**Railway:**
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway
- Twitter: @railway

**Heroku:**
- Docs: https://devcenter.heroku.com
- Support: help.heroku.com
- Status: status.heroku.com

---

**Happy Deploying! 🚀**

Choose Railway for simplicity, choose Heroku for enterprise-grade reliability!
