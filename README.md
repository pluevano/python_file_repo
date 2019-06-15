

#Python script project

repo ssh string (from github) for pull/push:

git@github.com:pluevano/python_file_repo.git

# create new remote repo from pre-existing local repo

$ git remote add origin -m python_file_repo git@github.com:pluevano/python_file_repo.git

# show the URL/s that Git has stored for the shortname to be used when reading and writing to the remote repo

$ git remote -v
origin  git@github.com:pluevano/python_file_repo.git (fetch)
origin  git@github.com:pluevano/python_file_repo.git (push)

$ git push origin master


