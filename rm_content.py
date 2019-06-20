"""
A Python 3.7 script to remove a specific string from all files and repos (owned by the user).
"""
import github

ACCESS_TOKEN = "*"
COMMIT_MSG = "rm-content."
# Fill with the string the user wants to search for and remove/replace.
STR_TO_REMOVE = "*"
# Can be left blank or change to something of users choice.
REPLACE_WITH = ""

g = github.Github(ACCESS_TOKEN)
for repo in g.get_user().get_repos(type="owner"):
    print(f"Repository Name: {repo.name}")
    # Fetch all content from the repo.
    repo_contents = repo.get_contents("")
    # Set a counter of how many files STR_TO_REMOVE was found in.
    counter = 0
    for file in repo_contents:
        if file.type == "dir":
            # Add files within a directory to the repo_contents.
            repo_contents.extend(repo.get_contents(file.path))
            # Show all repo contents.
            print(f"Full Repository Contents: {repo_contents}")
        # Get the file data of every file.
        try:
            # Decode the bytes file data.
            file_data = file.decoded_content.decode("utf-8")
            if STR_TO_REMOVE in file_data:
                print(f"{STR_TO_REMOVE} found in {file.name}")
                counter += 1
                # Remove STR_TO_REMOVE from file_data; replace with nothing.
                new_file_data = file_data.replace(STR_TO_REMOVE, REPLACE_WITH)
                print("Replace/Remove Successful.")
                # Send changes to Github.
                resp = repo.update_file(
                    path=file.path,
                    message=COMMIT_MSG,
                    content=new_file_data,
                    sha=file.sha,
                )
                print(resp)
            else:
                print(f"{STR_TO_REMOVE} NOT found in {file.name}")
        except AssertionError:
            print(f"{file.name} has unsupported encoding.")
        except UnicodeDecodeError as err:
            print(f"{file.name} errored: {err}")
        # Catches blob size API error.
        except github.GithubException as err:
            print(f"{file.name} threw the following error: {err}")
    print(f"{repo.name} finished with {STR_TO_REMOVE} found in {counter} file(s).")
