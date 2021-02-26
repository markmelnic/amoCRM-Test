import envars
from os import getenv
from amocrm_api import AmoOAuthClient

access_token = open("access_token.txt", "r").read()
refresh_token = open("refresh_token.txt", "r").read()

client = AmoOAuthClient(access_token, refresh_token, "https://"+getenv('SUBDOMAIN'), getenv('CLIENT_ID'), getenv('CLIENT_SECRET'), getenv('REDIRECT'))

info = client.get_account_info()
