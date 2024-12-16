# This bash script uses git to sync changes between a local and remote GitHub repository.
# It assumes that the remote repository is already set up and that the local repository is already cloned.

# pull changes from remote repository, stage all changes, commit changes with message 'Updated', push changes to remote repository on branch 'main'.

# pull changes from remote repository
git pull origin main

# stage all changes
git stage .

# commit changes with message 'Updated'
git commit -m "Synced changes"

# push changes to remote repository on branch 'main'
git push origin main

# Echo a message to the console indicating that the sync is complete
echo "Sync complete"





