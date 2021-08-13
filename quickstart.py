import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

import base


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the latest files the user has access to.
    """
    creds = None
    # The token file is created automatically when the authorization flow
    # completes for the first time.
    if os.path.exists(base.TOKEN):
        creds = Credentials.from_authorized_user_file(base.TOKEN, base.SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', base.SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(base.TOKEN, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    try:
        results = service.files().list(
            pageSize=2, fields="nextPageToken, files(id, name, appProperties)").execute()
    except:
        results = service.files().list(
            pageSize=2, fields="nextPageToken, files(id, name, description)").execute()

    items = results.get('files')

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            if 'appProperties' in list(item.keys()):
                print(u'{0} ({1}): appProperties {2}'.format(item['name'], item['id'], item['appProperties']))
            else:
                print(item.keys())
                print(u'{0} ({1}) description: {2}'.format(item['name'], item['id'], item['description']))
if __name__ == '__main__':
    main()
