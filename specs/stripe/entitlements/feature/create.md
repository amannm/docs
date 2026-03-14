# Create a feature

Creates a feature

## Returns

Returns a feature

## Parameters

- `lookup_key` (string, required)
  A unique key you provide as your own system identifier. This may be up to 80 characters.

  The maximum length is 80 characters.

- `name` (string, required)
  The feature’s name, for your own purpose, not meant to be displayable to the customer.

  The maximum length is 80 characters.

- `metadata` (object, optional)
  Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

```curl
curl https://api.stripe.com/v1/entitlements/features \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="My super awesome feature" \
  -d lookup_key=my-super-awesome-feature
```

### Response

```json
{
  "id": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
  "object": "entitlements.feature",
  "livemode": false,
  "name": "My super awesome feature",
  "lookup_key": "my-super-awesome-feature",
  "active": true,
  "metadata": {}
}
```
