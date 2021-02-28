import envars
from os import getenv
from amocrm.v2 import tokens, Lead, Contact, account

tokens.default_token_manager(
    client_id=getenv('CLIENT_ID'),
    client_secret=getenv('CLIENT_SECRET'),
    subdomain=getenv('S_SUBDOMAIN'),
    redirect_url=getenv('REDIRECT'),
    storage=tokens.FileTokensStorage()
)
tokens.default_token_manager.init(code=getenv('NEW_CODE'), skip_error=True)
