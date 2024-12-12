import os
from git import Repo

def get_commits_with_file(repo_path, target_file):
    if not os.path.exists(repo_path):
        raise FileNotFoundError(f"Repository path '{repo_path}' does not exist.")
    
    repo = Repo(repo_path)
    if repo.bare:
        raise ValueError(f"The directory '{repo_path}' is not a valid git repository.")
    
    commits_with_file = []
    for commit in repo.iter_commits():
        for file in commit.stats.files.keys():
            if target_file in file:
                commits_with_file.append({
                    "commit": commit.hexsha,
                    "author": commit.author.name,
                    "date": commit.committed_datetime,
                    "message": commit.message.strip()
                })
                break
    
    return commits_with_file

if __name__ == "__main__":
    # Пример использования
    repo_path = "/path/to/repo"
    target_file = "example.py"

    commits = get_commits_with_file(repo_path, target_file)
    if not commits:
        print(f"No commits found with changes to '{target_file}'.")
    else:
        print(f"Commits involving '{target_file}':")
        for commit in commits:
            print(f"- {commit['commit']}: {commit['message']} by {commit['author']} on {commit['date']}")
