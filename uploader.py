import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

import base
from file_explorer import files_in_folder_byext


def main():
    """
    Upload pictures with extra metadata
    """
    paths, names = files_in_folder_byext(['.jpg'], "files", True)
    e = {"custom_category": "meme"}
    for p, n in zip(paths, names):
        base.uploadFile(n, p, 'image/jpeg', e)

if __name__ == '__main__':
    main()
