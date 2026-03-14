# Delete a tax ID

Deletes an existing account or customer `tax_id` object.

## Returns

Returns an object with a deleted parameter on success. If the `tax_id` object does not exist, this call raises [an error](delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/tax_ids/txi_1NuMB12eZvKYlo2CMecoWkZd \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",
  "object": "tax_id",
  "deleted": true
}
```
