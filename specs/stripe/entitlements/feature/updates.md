# Updates a feature

Update a feature’s metadata or permanently deactivate it.

## Returns

The updated feature.

## Parameters

- `active` (boolean, optional)
  Inactive features cannot be attached to new products and will not be returned from the features list endpoint.

- `metadata` (object, optional)
  Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string, optional)
  The feature’s name, for your own purpose, not meant to be displayable to the customer.

  The maximum length is 80 characters.

```curl
curl https://api.stripe.com/v1/entitlements/features/feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
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
  "metadata": {
    "order_id": "6735"
  }
}
```
