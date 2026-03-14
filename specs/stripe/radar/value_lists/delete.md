# Delete a value list

Deletes a `ValueList` object, also deleting any items contained within the value list. To be deleted, a value list must not be referenced in any rules.

## Returns

Returns an object with the deleted `ValueList` object’s ID and a deleted parameter on success. Otherwise, this call raises [an error](delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",
  "object": "radar.value_list",
  "deleted": true
}
```
