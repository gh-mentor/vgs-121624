# This bash script uses git to sync changes between a local and remote GitHub repository.
# It assumes that the remote repository is already set up and that the local repository is already cloned.

# pull changes from remote repository, stage all changes, commit changes with message 'Updated', push changes to remote repository on branch 'main'.

git pull origin main

git add .

git commit -m "Update"

git push origin main

echo "Changes synced successfully!"


