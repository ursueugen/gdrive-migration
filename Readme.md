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

Documentation:
- [Google Drive API Python](https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/index%2Ehtml)
- [Google Drive API REST Reference](https://developers.google.com/drive/api/v3/reference)
- Many useful guides, especially on `Manage files & folders`
    - [Search for files & folders](https://developers.google.com/drive/api/guides/search-files#python)
    - [Create and populate folders](https://developers.google.com/drive/api/guides/folder)

## Plan for migration
- [X] Create a new folder `Migration` in the destination team drive.
- [] Parse directory structure in the source team drive.
- [] Create the same directory structure in the destination team drive.
- [] Copy files from source to destination.