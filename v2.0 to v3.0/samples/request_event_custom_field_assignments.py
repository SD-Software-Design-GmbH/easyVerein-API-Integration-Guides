import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Replace this by a valid ID of an event and an event custom field in your organization
event_id = '<EVENT_ID>'
custom_field_id = '<CUSTOM_FIELD_ID>'

# =============================================
# Request custom field assignments for an event
# =============================================

# Request an event's custom field assignments in API version `stable`
request_stable = requests.get(f'https://easyverein.com/api/stable/event/{event_id}/custom-fields', headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["results"][0])

# Request an event's custom field assignments in API version `latest`
request_latest = requests.get(f'https://easyverein.com/api/latest/event-custom-field-assignment/?event_object={event_id}', headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["results"][0])

# ==============================================
# Add a new custom field assignment for an event
# ==============================================

# In API version `stable`
data_for_post_stable = {
    'customField': custom_field_id,
    'value': 123
}
request_stable = requests.post(f'https://easyverein.com/api/stable/event/{event_id}/custom-fields', json=data_for_post_stable, headers=header)
request_stable_json = request_stable.json()
print(request_stable_json["id"], request_stable_json["customField"], request_stable_json["addressObject"], request_stable_json["value"])

# In API version `latest`
data_for_post_latest = {
    'custom_field': custom_field_id,
    'value': 123,
    'event_object': event_id,
}
request_latest = requests.post(f'https://easyverein.com/api/latest/event-custom-field-assignment', json=data_for_post_latest, headers=header)
request_latest_json = request_latest.json()
print(request_latest_json["id"], request_latest_json["custom_field"], request_latest_json["event_object"], request_latest_json["value"])

# Save the custom field assignment ID for later
custom_field_assignment_id = request_latest_json["id"]

# ========================================
# bulk-create new custom field assignments
# ========================================

# In API version `stable`
data_for_bulk_create_stable = {
    'entries': [
        {
            'customField': custom_field_id,
            'value': 321
        }
    ]
}
request_stable = requests.post(f'https://easyverein.com/api/stable/event/{event_id}/custom-fields/bulk-create', json=data_for_bulk_create_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_bulk_create_latest = {
    'entries': [
        {
            'custom_field': custom_field_id,
            'value': 321,
            'event_object': event_id
        }
    ]
}
request_latest = requests.post(f'https://easyverein.com/api/latest/event-custom-field-assignment/bulk-create', json=data_for_bulk_create_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))

# ====================================
# bulk-update custom field assignments
# ====================================

# In API version `stable`
data_for_bulk_update_stable = {
    'entries': [
        {
            'id': custom_field_assignment_id,
            'value': 789
        }
    ]
}
request_stable = requests.patch(f'https://easyverein.com/api/stable/event/{event_id}/custom-fields/bulk-update', json=data_for_bulk_update_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_bulk_update_latest = {
    'entries': [
        {
            'id': custom_field_assignment_id,
            'value': 789
        }
    ]
}
request_latest = requests.patch(f'https://easyverein.com/api/latest/event-custom-field-assignment/bulk-update', json=data_for_bulk_update_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))

# ========================================
# Mass action for custom field assignments
# ========================================

# In API version `stable`
data_for_mass_action_stable = {
    "data": {
        "entries": [
            {
                "customField": custom_field_id
            }
        ]
    },
    "ids": [event_id]
}
request_stable = requests.patch(f'https://easyverein.com/api/stable/event/custom-fields/mass-action', json=data_for_mass_action_stable, headers=header)
request_stable_json = request_stable.json()
print(len(request_stable_json))

# In API version `latest`
data_for_mass_action_latest = {
    "data": {
        "entries": [
            {
                "custom_field": custom_field_id
            }
        ]
    },
    "ids": [event_id]
}
request_latest = requests.patch(f'https://easyverein.com/api/latest/event/mass-action-custom-fields', json=data_for_mass_action_latest, headers=header)
request_latest_json = request_latest.json()
print(len(request_latest_json))

