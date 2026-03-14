# Cancel a top-up

Cancels a top-up. Only pending top-ups can be canceled.

## Returns

Returns the canceled top-up. If the top-up is already canceled or can’t be canceled, an error is returned.

```curl
curl -X POST https://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",
  "object": "topup",
  "amount": 2000,
  "balance_transaction": null,
  "created": 123456789,
  "currency": "usd",
  "description": "Top-up for Jenny Rosen",
  "expected_availability_date": 123456789,
  "failure_code": null,
  "failure_message": null,
  "livemode": false,
  "source": null,
  "statement_descriptor": "Top-up",
  "status": "canceled",
  "transfer_group": null
}
```
