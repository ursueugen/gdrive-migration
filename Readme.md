# GDrive migration

## Setup and explore the API
Follow steps from the [Python Quickstart for Google Drive API](https://developers.google.com/drive/api/quickstart/python).
- Authorization and credentials
    - Create a new project in the [Google Developers Console](https://console.developers.google.com/).
    - Enable the Drive API for that project.
    - Create credentials to access Application Data.
    - Download the credentials and save them as `credentials.json` in the same directory as this file.
- Install the Google Drive API client library for Python:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
- Create a sample `quickstart.py` and explore.