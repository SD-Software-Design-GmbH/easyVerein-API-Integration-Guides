import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of an event object in your organization
event_id = '<EVENT_ID>'

# Request an event's custom field assignments in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/event/{event_id}/custom-fields', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request an event's custom field assignments in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/event-custom-field-assignment/?event_object={event_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])
