from logging import FATAL
import envars
from os import getenv
from amocrm.v2 import tokens
from amocrm_api import AmoOAuthClient

tokens.default_token_manager(
    client_id=getenv('CLIENT_ID'),
    client_secret=getenv('CLIENT_SECRET'),
    subdomain=getenv('S_SUBDOMAIN'),
    redirect_url=getenv('REDIRECT'),
    storage=tokens.FileTokensStorage()
)
tokens.default_token_manager.init(code=getenv('NEW_CODE'), skip_error=True)

access_token = open("access_token.txt", "r").read()
refresh_token = open("refresh_token.txt", "r").read()

client = AmoOAuthClient(access_token, refresh_token, getenv('F_SUBDOMAIN'), getenv('CLIENT_ID'), getenv('CLIENT_SECRET'), getenv('REDIRECT'))
