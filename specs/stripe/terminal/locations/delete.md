# Delete a Location

Deletes a `Location` object.

## Returns

Returns the `Location` object that was deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tml_FBakXQG8bQk4Mm",
  "object": "terminal.location",
  "deleted": true
}
```
