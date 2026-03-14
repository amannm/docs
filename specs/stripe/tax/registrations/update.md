# Update a registration

Updates an existing Tax `Registration` object.

A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting `expires_at`.

## Returns

A Tax `Registration` object.

## Parameters

- `active_from` (string | timestamp, optional)
  Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.

- `expires_at` (string | timestamp, optional)
  If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.

```curl
curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \
  -u "<<YOUR_SECRET_KEY>>" \
  -d expires_at=now
```

### Response

```json
{
  "id": "taxreg_NkyGPRPytKq66j",
  "object": "tax.registration",
  "active_from": 1683036640,
  "country": "US",
  "country_options": {
    "us": {
      "state": "CA",
      "type": "state_sales_tax"
    }
  },
  "created": 1682006400,
  "expires_at": 1684072000,
  "livemode": false,
  "status": "active"
}
```
