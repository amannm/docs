# Delete a product

Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with `type=good` is only possible if it has no SKUs associated with it.

## Returns

Returns a deleted object on success. Otherwise, this call raises [an error](delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "prod_NWjs8kKbJWmuuc",
  "object": "product",
  "deleted": true
}
```
