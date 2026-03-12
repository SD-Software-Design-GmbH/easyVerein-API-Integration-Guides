# Änderungen in API v3.0 gegenüber API v2.0
Alle Versionen älter als v3.0 bleiben von den Ändrungen hier unberührt

## Schreibweise von Feldnamen

Alle Feldnamen sind nun in snake_case geändert worden und anführende Unterstriche wurden entfernt.
Das betrifft alle Endpunkte und Actions. (Actions sind Aktionen, die auf einzelnen Endpunkten ausgeführt werden können.
Beispielsweise `member/me/permissions` oder auch `member/{member_id}/email-notification`.)

### Im Header jeder Antwort der API:
- Das Feld `tokenRefreshNeeded`, welches impliziert, dass das Token erneuert werden muss, heißt nun `token_refresh_needed`.

### Authentifizierung:
- Das Feld `2FA` im `get-token` Endpunkt heißt nun `2_fa`.
- Das Feld `needs2FA` im `get-token` Endpunkt heißt nun `needs2_fa`.

### Beispiele wie Felder nun heißen:
- Das Feld `contactDetails` im `member` Endpunkt heißt nun `contact_details`.
- Das Feld `_deleteAfterDate` in allen Endpunkten heißt nun `delete_after_date`.
- Das Feld `firstName` im `contact-details` Endpunkt heißt nun `first_name`.
- Das Feld `availableSkr42Spheres` im `organization` Endpunkt heißt jetzt `available_skr42_spheres`.
- Das Feld `_defaultProfilePicture` im `organization` Endpunkt heißt jetzt `default_profile_picture`.

### Beispiele, wie Actions nun Felder erwarten und zurückgeben:
- In der Action `member/{member_id}/change-password` heißen die Felder `currentPassword`, `newPassword` und `2FA` nun `current_password`, `new_password` und `2_fa`.
- In der Action `member/me/permissions` heißen die Felder im Rückgabewert wie z. B. `_isChairman`, `bookkeepingEnabled` und `changeBankDataWhenDebit` heißen jetzt `is_chairman`, `bookkeeping_enabled` und `change_bank_data_when_debit`.
- In der Action `member/email-notification` heißen die Werte für `action` statt z. B. `emailNotificationConfirmResignation` und `emailNotificationConfirmMembership` jetzt `email_notification_confirm_resignation` und `email_notification_confirm_membership`.
- In der Action `contact-details/income-and-expenses` heißen die Rückgabedaten statt z. B. `totalOfOpenInvoices` und `totalOfOpenInvoicesOut` jetzt `total_of_open_invoices` und `total_of_open_invoices_out`.

#### Alle Filter sind ebenfalls betroffen und sind in snake_case!

### Beispiele, wie Filter nun heißen:
- Der Filter `_chairmanPermissionGroup` im `member` Endpunkt heißt nun `chairman_permission_group`.
- Der Filter `customfilter` in einigen Endpunkten heißt nun `custom_filter`.
- Der Filter `usesessionfilter` in einigen Endpunkten heißt nun `use_session_filter`.
- Der Filter `contactDetailsGroups` im `contact-details` Endpunkt heißt nun `contact_details_groups`.


## Geänderte Endpunkte

Alle Endpunkte, die vorher nur als Subendpunkte von anderen Endpunkten zur Verfügung standen, sind jetzt alleinstehende Endpunkte.

Das betrifft folgende Endpunkte:

- `member/{member_id}/groups`
- `member/{member_id}/custom-fields`
- `member/{member_id}/custom-fields/{custom_field_assignment_id}/change-requests`
- `contact-details/{address_id}/custom-fields`
- `contact-details/{address_id}/change-requests`
- `inventory-object/{inventory_object_id}/custom-fields`
- `event/{event_id}/custom-fields`
- `event/{event_id}/participation`
- `custom-field/{custom_field_id}/select-options`

Diese Endpunkte werden durch neue Endpunkte wie folgt abgelöst:

### `member/{member_id}/groups`
- Gruppenmitgliedschaften eines Mitglieds anfragen: `member/{member_id}/groups` => `member-group-assignment?user_object={member_id}`
- Eine einzelne Gruppenmitgliedschaften eines Mitglieds anfragen: `member/{member_id}/groups/{member_group_assignment_id}` => `member-group-assignment/{member_group_assignment_id}`
- Filtern ist zusätzlich möglich mit:  `user_object`, `user_object__in`, `user_object__not`
- Bei `POST` muss immer `user_object` mitgegeben werden.
- Bei `bulk-update`/`bulk-create` muss zusätzlich immer `user_object` mitgegeben werden.
- Es gibt `bulk-update`/`bulk-create` auf diesem Endpunkt.
- Statt `member/groups/mass-action` gibt es `member/mass-action-member-groups`. Die Daten, die übergeben werden, bleiben gleich.

### `member/{member_id}/custom-fields`
- Individuelle Felder eines Mitglieds anfragen: `member/{member_id}/custom-fields` => `member-custom-field-assignment?user_object={member_id}`
- Ein einzelnes individuelles Feld eines Mitglieds anfragen: `member/{member_id}/custom-fields/{custom_field_assignment_id}` => `member-custom-field-assignment/{custom_field_assignment_id}`
- Filtern ist zusätzlich möglich mit:  `user_object`, `user_object__in`, `user_object__not`
- Der Filter `customField` mit mehreren komma-getrennten Werten heißt jetzt `custom_field__in`. `custom_field` filtert nur nach einem einzigen Wert.
- Bei `POST` muss vom Admin mit Schreibrechten auf der Mitgliederverwaltung `user_object` mitgegeben werden. Ansonsten ist das nicht nötig, da ansonsten der Eintrag immer für einen selbst erstellt wird.
- Bei `bulk-update`/`bulk-create` muss zusätzlich `user_object` mitgegeben werden.
- Es gibt `bulk-update`/`bulk-create` auf diesem Endpunkt.
- Statt `member/custom-fields/mass-action` gibt es `member/mass-action-custom-fields`. Die Daten, die übergeben werden, bleiben gleich.

### `member/{member_id}/custom-fields/{custom_field_assignment_id}/change-requests`
- Änderungsanfragen zu einem individuellen Feld eines Mitglieds anfragen: `member/{member_id}/custom-fields/{custom_field_assignment_id}/change-requests` => `member-custom-field-assignment-change-request/?user_custom_field={custom_field_assignment_id}`
- Eine einzelne Änderungsanfragen zu einem individuellen Feld eines Mitglieds anfragen: `member/{member_id}/custom-fields/{custom_field_assignment_id}/change-requests/{member_custom_field_assignment_change_request_id}` => `member-custom-field-assignment-change-request/{member_custom_field_assignment_change_request_id}`
- Filtern ist zusätzlich möglich mit:  `user_custom_field`, `user_custom_field__in`, `user_custom_field__not`, `user_custom_field__custom_field`, `user_custom_field__custom_field__in`, `user_custom_field__custom_field__not`, `user_custom_field__user_object`, `user_custom_field__user_object__in`, `user_custom_field__user_object__not`, `requesting_user`, `requesting_user__in`, `requesting_user__not`
- Bei `POST` muss `custom_field` mitgegeben werden.

### `contact-details/{address_id}/custom-fields`
- Individuelle Felder einer Adresse anfragen: `contact-details/{address_id}/custom-fields` => `contact-details-custom-field-assignment?address_object={address_id}`
- Ein einzelnes individuelles Feld einer Adresse anfragen: `contact-details/{address_id}/custom-fields/{custom_field_assignment_id}` => `contact-details-custom-field-assignment/{custom_field_assignment_id}`
- Filtern ist möglich mit:  `address_object`, `address_object__in`, `address_object__not`, `custom_field`, `custom_field__in`, `custom_field__not`
- Bei `POST` muss `address_object` mitgegeben werden.
- Bei `bulk-update`/`bulk-create` muss zusätzlich `address_object` mitgegeben werden.
- Es gibt `bulk-update`/`bulk-create` auf diesem Endpunkt.
- Statt `contact-details/custom-fields/mass-action` gibt es `contact-details/mass-action-custom-fields`. Die Daten, die übergeben werden, bleiben gleich.


### `contact-details/{address_id}/change-requests`
- Adress-Änderungsanfragen einer Adresse anfragen: `contact-details/{address_id}/custom-fields` => `contact-details-change-request?address={address_id}`
- Eine einzelne Adress-Änderungsanfrage einer Adresse anfragen: `contact-details/{address_id}/custom-fields/{address_change_request_id}` => `contact-details-change-request/{address_change_request_id}`
- Filtern ist zusätzlich möglich mit:  `address`, `address__in`, `address__not`, `requesting_user`, `requesting_user__in`, `requesting_user__not`

### `inventory-object/{inventory_object_id}/custom-fields`
- Individuelle Felder eines Inventargegenstands anfragen: `inventory-object/{inventory_object_id}/custom-fields` => `inventory-object-custom-field-assignment?inventory_object={inventory_object_id}`
- Ein einzelnes individuelles Feld eines Inventargegenstands anfragen: `inventory-object/{member_id}/custom-fields/{custom_field_assignment_id}` => `inventory-object-custom-field-assignment/{custom_field_assignment_id}`
- Filtern ist zusätzlich möglich mit:  `inventory_object`, `inventory_object__in`, `inventory_object__not`
- Bei `POST` muss `inventory_object` mitgegeben werden.
- Bei `bulk-update`/`bulk-create` muss zusätzlich `inventory_object` mitgegeben werden.
- Es gibt `bulk-update`/`bulk-create` auf diesem Endpunkt.
- Statt `inventory-object/custom-fields/mass-action` gibt es `inventory-object/mass-action-custom-fields`.
- Filter `customField` mit mehreren komma-getrennten Werten heißt jetzt `custom_field__in`. `custom_field` filtert nur nach einem einzigen Wert.

### `event/{event_id}/custom-fields`
- Individuelle Felder eines Termins anfragen: `event/{event_id}/custom-fields` => `event-custom-field-assignment?event_object={event_id}`
- Ein einzelnes individuelles Feld eines Termins anfragen: `event/{event_id}/custom-fields/{custom_field_assignment_id}` => `event-custom-field-assignment/{custom_field_assignment_id}`
- Filtern zusätzlich möglich mit:  `event_object`, `event_object__in`, `event_object__not`, `custom_field`, `custom_field__in`, `custom_field__not`
- Bei `POST` muss `event_object` mitgegeben werden.
- Bei `bulk-update`/`bulk-create` muss zusätzlich `event_object` mitgegeben werden.
- Es gibt `bulk-update`/`bulk-create` auf diesem Endpunkt.


### `event/{event_id}/participation`
- Teilnahmen eines Termins anfragen: `event/{event_id}/participation` => `participation/?participation_event={event_id}`
- Eine einzelne Teilnahme anfragen: `event/{event_id}/participation/{participation_id}` => `participation/participation_id`
- Filtern zusätzlich möglich mit: `participation_event`, `participation_event__in`, `participation_event__not`
- Bei `POST` muss `participation_event` mitgegeben werden.
- Bei den Actions `create-interval-participation`, `create-participation-with-price-groups` und `bulk-create-participations-with-price-groups` muss in den Request-Daten (bzw. bei `bulk-create-participations-with-price-groups` in jedem der `entries`) ebenfalls `participation_event` mitgegeben werden.

### `custom-field/{custom_field_id}/select-options`
- Auswahloptionen eines individuellen Felds anfragen: `custom-field/{custom_field_id}/select-options` => `select-option?custom_field={custom_field_id}`
- Eine einzelne Auswahloption eines individuellen Felds anfragen: `custom-field/{custom_field_id}/select-options/{select_option_id}` => `select-option/{select_option_id}`
- Filtern möglich mit:  `custom_field`, `custom_field__in`, `custom_field__not`
- Bei `POST` muss `custom_field` mitgegeben werden.
- Bei `bulk-update`/`bulk-create` muss zusätzlich `custom_field` mitgegeben werden.
- Es gibt `bulk-update`/`bulk-create` auf diesem Endpunkt.

## Weitere Änderungen
- `participation`-Endpunkt:
    - Die `invite`-Action benötigt nicht mehr `participation_address`, sondern eine Liste von Adressen `participation_addresses`.
    - Die `invite-groups`-Action, die bisher auf dem `event`-Endpunkt war, ist jetzt -- analog zu `invite` -- auf dem `participation`-Endpunkt. Zusätzlich muss der Termin als `participation_event` angegeben werden.
