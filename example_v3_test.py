import sendgrid
import json

import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

status, msg = client.asm_groups.post("Magic Key 2", "Unlock your Emails", False)
print status
print msg

status, msg = client.asm_groups.get()
print status
print msg

"""

status, msg = client.asm_groups.get()
print status
print msg

status, msg = client.asm_groups.post("Magic Key", "Unlock your Emails")
print status
print msg

status, msg = client.asm_groups.get()
print status
print msg

# In the global suppression list
status, msg = client.asm_global_suppressions.get('elmer.thomas+test_global@gmail.com')
print status
print msg

# Not in the global suppression list
status, msg = client.asm_global_suppressions.get('elmer.thomas@gmail.com')
print status
print msg

status, msg = client.apikeys.get()
print status
print msg

status, msg = client.asm_suppressions.delete(67,'elmer+test@thinkingserious.com')
print status
print msg

status, msg = client.asm_suppressions.post(60, ['elmer+test@thinkingserious.com', 'elmer.thomas@yahoo.com'])
print status
print msg

status, msg = client.asm_suppressions.get(None,'elmer.thomas@yahoo.com')
print status
print msg

status, msg = client.asm_groups.get([66,67,50])
print status
print msg

name = "My Amazing API Key"
status, msg = client.apikeys.post(name)
msg = json.loads(msg)
api_key_id = msg['api_key_id']
print status
print msg

name = "My NEW API Key 3000"
status, msg = client.apikeys.patch(api_key_id, name)
print status
print msg

status, msg = client.apikeys.delete(api_key_id)
print status

status, msg = client.apikeys.get()
print status
print msg

# Get a list of all valid API Keys from your account
status, msg = client.apikeys.get()
print status
print msg

# Create a new API Key
name = "My API Key 10"
status, msg = client.apikeys.post(name)
print status
print msg

# Delete an API Key with a given api_key_id
api_key_id = "zc0r5sW5TTuBQGsMPMUx0A"
status, msg = client.apikeys.delete(api_key_id)
print status
print msg

# Update the name of an API Key, given an api_key_id
api_key_id = "API_KEY"
name = "My API Key 3"
status, msg = client.apikeys.patch(api_key_id, name)
print status
print msg
"""