# Retrieve a registration

Returns a Tax `Registration` object.

## Returns

A Tax `Registration` object.

```curl
curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "taxreg_NkyGPRPytKq66j",
  "object": "tax.registration",
  "active_from": 1682036640,
  "country": "US",
  "country_options": {
    "us": {
      "state": "CA",
      "type": "state_sales_tax"
    }
  },
  "created": 1682006400,
  "expires_at": null,
  "livemode": false,
  "status": "active"
}
```
