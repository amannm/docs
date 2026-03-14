# Retrieve a tax ID

Retrieves an account or customer `tax_id` object.

## Returns

Returns a `tax_id` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/tax_ids/txi_1NuMB12eZvKYlo2CMecoWkZd \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",
  "object": "tax_id",
  "country": "DE",
  "created": 123456789,
  "customer": null,
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": null,
  "owner": {
    "type": "self",
    "customer": null
  }
}
```
