# Navigate to your project directory
cd "c:\Users\t5mis\Desktop\Project-300"

# Check git status to see what files have changed
git status

# Revert all changes to tracked files
git checkout .

# Remove any new untracked files that were created
git clean -fd

# This will remove the new files we created:
# - vercel.json
# - build_files.sh  
# - DEPLOYMENT_GUIDE.md
# - setup_production.py
# - .env.example
# - lost_and_found_portal_MU/static/.gitkeep