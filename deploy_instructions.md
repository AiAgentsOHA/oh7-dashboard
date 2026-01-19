# OH7 Dashboard Deployment to Streamlit Cloud

## Files Required
Make sure these files are in `/Users/mikaeel/Downloads/oh7-dashboard/`:
- `app.py`
- `oh7_executive_dashboard_v7.html`
- `requirements.txt`

## Step 1: Initialize Git Repository

```bash
cd /Users/mikaeel/Downloads/oh7-dashboard

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "OH7 Executive Dashboard v7"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `oh7-dashboard`
3. Keep it public (or private if you have Streamlit Teams)
4. Don't initialize with README

## Step 3: Push to GitHub

```bash
cd /Users/mikaeel/Downloads/oh7-dashboard

git remote add origin https://github.com/YOUR_USERNAME/oh7-dashboard.git
git branch -M main
git push -u origin main
```

## Step 4: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click "New app"
3. Connect your GitHub account if not already
4. Select:
   - Repository: `YOUR_USERNAME/oh7-dashboard`
   - Branch: `main`
   - Main file path: `app.py`
5. Click "Deploy"

## Step 5: Wait for Deployment
- Takes 1-3 minutes
- You'll get a URL like: `https://oh7-dashboard.streamlit.app`

## Quick Terminal Commands (Copy/Paste)

```bash
cd /Users/mikaeel/Downloads/oh7-dashboard
git init
git add .
git commit -m "OH7 Executive Dashboard v7"
```

Then after creating GitHub repo:
```bash
git remote add origin https://github.com/YOUR_USERNAME/oh7-dashboard.git
git branch -M main
git push -u origin main
```

