# Delete a Configuration

Deletes a `Configuration` object.

## Returns

Returns the `Configuration` object that was deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/terminal/configurations/tmc_FQqbaQCiy0m1xc \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "deleted": true
}
```
