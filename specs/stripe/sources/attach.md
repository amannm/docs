# Attach a source

Attaches a Source object to a Customer. The source must be in a chargeable or pending state.

## Returns

Returns the attached Source object.

## Parameters

- `source` (string, required)
  The identifier of the source to be attached.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/sources \
  -u "<<YOUR_SECRET_KEY>>" \
  -d source=src_1NfRGv2eZvKYlo2Cv7NAImBL
```

### Response

```json
{
  "id": "src_1NfRGv2eZvKYlo2Cv7NAImBL",
  "object": "source",
  "ach_credit_transfer": {
    "account_number": "test_52796e3294dc",
    "routing_number": "110000000",
    "fingerprint": "ecpwEzmBOSMOqQTL",
    "bank_name": "TEST BANK",
    "swift_code": "TSTEZ122"
  },
  "amount": 1000,
  "client_secret": "src_client_secret_sBqfX18eq6GPfGxGvVfMByCp",
  "created": 1692121393,
  "currency": "usd",
  "customer": "cus_9s6XKzkNRiz8i3",
  "flow": "receiver",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": null,
    "email": "jenny.rosen@example.com",
    "name": null,
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "receiver": {
    "address": "121042882-38381234567890123",
    "amount_received": 1000,
    "amount_charged": 0,
    "amount_returned": 0,
    "refund_attributes_status": "missing",
    "refund_attributes_method": "email"
  },
  "redaction": null,
  "statement_descriptor": null,
  "status": "chargeable",
  "type": "ach_credit_transfer",
  "usage": "reusable"
}
```
