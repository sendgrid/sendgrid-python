import sendgrid
import json

import os
if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

client = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

start_date = '2015-10-01'
end_date = None
aggregated_by = 'week' # must be day, week or month
status, msg = client.stats.get(
                start_date=start_date, 
                end_date=end_date, 
                aggregated_by=aggregated_by)
print status
print msg

"""
email = 'example@example.com'
status, msg = client.asm_global_suppressions.delete(email)
print status
print msg

status, msg = client.suppressions.get()
print status
print msg

status, msg = client.asm_global_suppressions.post(['example@example.com'])
print status
print msg

group_id = 70
status, msg = client.asm_suppressions.get(group_id)
print status
print msg

status, msg = client.asm_groups.post("Magic Key 2", "Unlock your Emails", False)
print status
print msg

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
status, msg = client.asm_global_suppressions.get('example@example.com')
print status
print msg

# Not in the global suppression list
status, msg = client.asm_global_suppressions.get('example@example.com')
print status
print msg

status, msg = client.apikeys.get()
print status
print msg

status, msg = client.asm_suppressions.delete(67,'example@example.com')
print status
print msg

status, msg = client.asm_suppressions.post(60, ['example@example.com', 'example@example.com])
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