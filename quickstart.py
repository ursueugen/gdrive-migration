from __future__ import print_function
from googleapiclient.errors import HttpError
from utils import get_creds, get_gdrive_api_service


# If modifying these scopes, delete the file token.json.
# For more info on scopes, check https://developers.google.com/identity/protocols/oauth2/scopes#drive
SCOPES = ["https://www.googleapis.com/auth/drive"]  # See, edit, create, and delete all of your Google Drive files


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = get_creds()
    
    try:
        service = get_gdrive_api_service(creds)
        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer): Error handling
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()