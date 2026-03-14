# Remove a feature from a product

Deletes the feature attachment to a product

## Returns

Returns an object with a deleted parameter on success. If the product feature ID does not exist, this call raises [an error](remove.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc/features/prodft_BcMBZUWCIOEgEc \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "prodft_BcMBZUWCIOEgEc",
  "object": "product_feature",
  "deleted": true
}
```
