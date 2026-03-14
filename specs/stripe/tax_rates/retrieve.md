# Retrieve a tax rate

Retrieves a tax rate with the given ID

## Returns

Returns an tax rate if a valid tax rate ID was provided. Raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",
  "object": "tax_rate",
  "active": true,
  "country": null,
  "created": 1682114687,
  "description": "VAT Germany",
  "display_name": "VAT",
  "inclusive": false,
  "jurisdiction": "DE",
  "livemode": false,
  "metadata": {},
  "percentage": 16,
  "state": null,
  "tax_type": null
}
```
