# Retrieve an active entitlement

Retrieve an active entitlement

## Returns

Returns an active entitlement

## Parameters

- `id` (string, required)
  The ID of the entitlement.

```curl
curl https://api.stripe.com/v1/entitlements/active_entitlements/ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
  "object": "entitlements.active_entitlement",
  "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
  "lookup_key": "seats-feature",
  "livemode": false
}
```
