# List all features

Retrieve a list of features

## Returns

Returns a list of your features

## Parameters

- `archived` (boolean, optional)
  If set, filter results to only include features with the given archive status.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `lookup_key` (string, optional)
  If set, filter results to only include features with the given lookup_key.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/entitlements/features \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/entitlements/features",
  "has_more": false,
  "data": [
    {
      "id": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
      "object": "entitlements.feature",
      "livemode": false,
      "name": "My super awesome feature",
      "lookup_key": "my-super-awesome-feature",
      "active": true,
      "metadata": {}
    }
  ]
}
```
