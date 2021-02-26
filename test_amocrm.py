import envars
from os import getenv
from amocrm.v2 import tokens, Lead, Contact

tokens.default_token_manager(
    client_id=getenv('CLIENT_ID'),
    client_secret=getenv('CLIENT_SECRET'),
    subdomain=getenv('SUBDOMAIN'),
    redirect_url=getenv('REDIRECT'),
    storage=tokens.FileTokensStorage()
)
tokens.default_token_manager.init(code=getenv('CODE'), skip_error=True)

pipid = 3944278

#test_lead = Lead.objects.all()
contact = Contact.objects.get(query="43707481")
print(len(list(contact.leads)))

'''
Lead.objects.create(
    name = "Order id ttt 3939",
    contacts = contact,
    pipeline_id = 3944278
)
'''

lead = Lead.objects.get(query="Order id ttt 3838")
lead.contacts.remove(contact.id)
lead.save()
#Lead.objects.update(object_id=lead.id)

contact = Contact.objects.get(query="43707481")
contact.leads.remove(lead)
contact.save()

print(len(list(contact.leads)))
