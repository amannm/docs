# Attach a feature to a product

Creates a product_feature, which represents a feature attachment to a product

## Returns

Returns a product_feature

## Parameters

- `entitlement_feature` (string, required)
  The ID of the [Feature](https://docs.stripe.com/docs/api/entitlements/feature.md) object attached to this product.

```curl
curl https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc/features \
  -u "<<YOUR_SECRET_KEY>>" \
  -d entitlement_feature=feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu
```

### Response

```json
{
  "id": "prodft_BcMBZUWCIOEgEc",
  "object": "product_feature",
  "livemode": false,
  "entitlement_feature": {
    "id": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
    "object": "entitlements.feature",
    "livemode": false,
    "name": "My super awesome feature",
    "lookup_key": "my-super-awesome-feature",
    "metadata": {}
  }
}
```
