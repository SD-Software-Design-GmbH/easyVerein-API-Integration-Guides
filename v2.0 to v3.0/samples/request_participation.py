import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of an event, an address and a price group belonging to the event in your organization
event_id = '<EVENT_ID>'
contact_details_id = '<CONTACT_DETAILS_ID>'
price_group_id = '<PRICE_GROUP_ID>'

# ===================================
# Request participations for an event
# ===================================

# Request participations for an event in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/event/{event_id}/participations', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request participations for an event in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/participation/?participation_event={event_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])

# ====================================
# Add a new participation for an event
# ====================================

# In API version `stable`
data_for_post_stable = {
    'participationAddress': contact_details_id,
    'state': 1,
}
request_stable = requests.post(f'https://easyverein.com/api/stable/event/{event_id}/participations', json=data_for_post_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["id"], request_stable_json["participationEvent"], request_stable_json["participationAddress"], request_stable_json["state"])

# In API version `latest`
data_for_post_latest = {
    'participation_address': contact_details_id,
    'value': 123,
    'participation_event': event_id,
}
request_latest = requests.post(f'https://easyverein.com/api/latest/participation', json=data_for_post_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["id"], request_latest_json["participation_event"], request_latest_json["participation_address"], request_latest_json["state"])

# Save the participation ID for later
participation_id = request_latest_json["id"]

# ====================================
# create-interval-participation action
# ====================================

# In API version `stable`
data_for_create_interval_participation_stable = {
    'participationAddress': contact_details_id,
    'state': 1,
}
request_stable = requests.post(f'https://easyverein.com/api/stable/event/{event_id}/participation/create-interval-participation', json=data_for_create_interval_participation_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json)

# In API version `latest`
data_for_create_interval_participation_latest = {
    'participation_address': contact_details_id,
    'state': 1,
    'participation_event': event_id
}
request_latest = requests.post(f'https://easyverein.com/api/latest/participation/create-interval-participation', json=data_for_create_interval_participation_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json)

# =============================================
# create-participation-with-price-groups action
# =============================================

# In API version `stable`
data_for_create_interval_participation_stable = {
    'participationAddress': contact_details_id,
    'state': 1,
    'participationPriceFroups': [
        {
            'priceGroup': price_group_id,
            'pieces': 123
        }
    ]
}
request_stable = requests.post(f'https://easyverein.com/api/stable/event/{event_id}/participation/create-participation-with-price-groups', json=data_for_create_interval_participation_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json)

# In API version `latest`
data_for_create_interval_participation_latest = {
    'participation_address': contact_details_id,
    'state': 1,
    'participation_price_groups': [
        {
            'price_group': price_group_id,
            'pieces': 123
        }
    ],
    'participation_event': event_id
}
request_latest = requests.post(f'https://easyverein.com/api/latest/participation/create-participation-with-price-groups', json=data_for_create_interval_participation_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json)
