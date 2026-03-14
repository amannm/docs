# Retrieve a Location

Retrieves a `Location` object.

## Returns

Returns a `Location` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tml_FBakXQG8bQk4Mm",
  "object": "terminal.location",
  "address": {
    "city": "San Francisco",
    "country": "US",
    "line1": "1234 Main Street",
    "line2": "",
    "postal_code": "94111",
    "state": "CA"
  },
  "display_name": "My First Store",
  "livemode": false,
  "metadata": {}
}
```
