# Delete a value list item

Deletes a `ValueListItem` object, removing it from its parent value list.

## Returns

Returns an object with the deleted `ValueListItem` object’s ID and a deleted parameter on success. Otherwise, this call raises [an error](delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
  "object": "radar.value_list_item",
  "deleted": true
}
```
