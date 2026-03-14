# Delete a Reader

Deletes a `Reader` object.

## Returns

Returns the `Reader` object that was deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "deleted": true
}
```
