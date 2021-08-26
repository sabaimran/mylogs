from datetime import datetime
from git import Repo

class GitProxy:

    def __init__(self, repopath):
        self.repopath = repopath

    ### Pull latest changes from the repo.
    def pull(self):
        repo = Repo(self.repopath)
        repo.git.pull()

    ### Commit and push local changes to the remote repo.
    def commit_and_push(self):
        repo = Repo(self.repopath)
        repo.git.add("--all")
        repo.git.commit(m=str.format("Updated logs on {0} ", datetime.now().isoformat()))
        repo.git.push()