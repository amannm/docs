# Create a top-up

Top up the balance of an account

## Returns

Returns the top-up object.

## Parameters

- `amount` (integer, required)
  A positive integer representing how much to transfer.

- `currency` (string, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `source` (string, optional)
  The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://docs.stripe.com/docs/connect/testing.md#testing-top-ups)).

- `statement_descriptor` (string, optional)
  Extra information about a top-up for the source’s bank statement. Limited to 15 ASCII characters.

- `transfer_group` (string, optional)
  A string that identifies this top-up as part of a group.

```curl
curl https://api.stripe.com/v1/topups \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=2000 \
  -d currency=usd \
  -d description="Top-up for Jenny Rosen" \
  -d statement_descriptor=Top-up
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
  "status": "pending",
  "transfer_group": null
}
```
