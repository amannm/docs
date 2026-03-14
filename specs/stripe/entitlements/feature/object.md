# The Feature object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active` (boolean)
  Inactive features cannot be attached to new products and will not be returned from the features list endpoint.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `lookup_key` (string)
  A unique key you provide as your own system identifier. This may be up to 80 characters.

- `metadata` (object)
  Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `name` (string)
  The feature’s name, for your own purpose, not meant to be displayable to the customer.

  The maximum length is 80 characters.

### The Feature object

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
