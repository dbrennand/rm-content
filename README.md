# rm-content
A Python 3.7 script to remove a specific string from all files and repos (owned by the user).

## Usage
* Provide a Github account [access token](https://github.com/settings/tokens)

* Edit `COMMIT_MSG` if you so desire.

* **Important** `STR_TO_REMOVE`. REQUIRED: The string to search for removal/replace.

* **Important** `REPLACE_WITH`. The string to replace `STR_TO_REMOVE`. Can be left blank.

```
ACCESS_TOKEN = "*"
COMMIT_MSG = "rm-content."
# Fill with the string the user wants to search for and remove/replace.
STR_TO_REMOVE = "*"
# Can be left blank or change to something of users choice.
REPLACE_WITH = ""
```

## Dependencies

* [PyGithub](https://github.com/PyGithub/PyGithub/)

Install dependencies using Pipfile:
```
pipenv install
```
Or
```
pip install -r requirements.txt
```

## Authors -- Contributors

* **dbrennand** - *Author* - [dbrennand](https://github.com/dbrennand)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
