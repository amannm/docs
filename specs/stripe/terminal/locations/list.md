# List all Locations

Returns a list of `Location` objects.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` locations, starting after location `starting_after`. Each entry in the array is a separate Terminal `location` object. If no more locations are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/terminal/locations \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/terminal/locations",
  "has_more": false,
  "data": [
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
  ]
}
```
