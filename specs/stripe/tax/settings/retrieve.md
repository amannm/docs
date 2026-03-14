# Retrieve settings

Retrieves Tax `Settings` for a merchant.

## Returns

A Tax `Settings` object.

```curl
curl https://api.stripe.com/v1/tax/settings \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "tax.settings",
  "defaults": {
    "tax_behavior": null,
    "tax_code": "txcd_10000000"
  },
  "head_office": {
    "address": {
      "city": null,
      "country": "US",
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": "CA"
    }
  },
  "livemode": false,
  "status": "active",
  "status_details": {
    "active": {}
  }
}
```
