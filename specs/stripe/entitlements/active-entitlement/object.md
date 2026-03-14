# The Active Entitlement object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `feature` (string, expandable (can be expanded into an object with the `expand` request parameter))
  The [Feature](https://docs.stripe.com/docs/api/entitlements/feature.md) that the customer is entitled to.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `lookup_key` (string)
  A unique key you provide as your own system identifier. This may be up to 80 characters.

### The Active Entitlement object

```json
{
  "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
  "object": "entitlements.active_entitlement",
  "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
  "lookup_key": "seats-feature",
  "livemode": false
}
```
