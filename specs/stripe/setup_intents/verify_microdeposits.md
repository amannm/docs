# Verify microdeposits on a SetupIntent

Verifies microdeposits on a SetupIntent object.

## Returns

Returns a SetupIntent object.

## Parameters

- `amounts` (array of integers, optional)
  Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.

- `descriptor_code` (string, optional)
  A six-character code starting with SM present in the microdeposit sent to the bank account.

```curl
curl https://api.stripe.com/v1/setup_intents/seti_1Mm5yZLkdIwHu7ixm0sPzrx4/verify_microdeposits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "amounts[]"=32 \
  -d "amounts[]"=45
```

### Response

```json
{
  "id": "seti_1Mm5yZLkdIwHu7ixm0sPzrx4",
  "object": "setup_intent",
  "application": null,
  "cancellation_reason": null,
  "client_secret": "seti_1Mm5yZLkdIwHu7ixm0sPzrx4_secret_NXAJ5iPM38ITW1pI7o8VZZhoZyDrrWR",
  "created": 1678931491,
  "customer": null,
  "description": null,
  "flow_directions": null,
  "last_setup_error": null,
  "latest_attempt": "setatt_1Mm5yZLkdIwHu7ix7QtOkLAu",
  "livemode": false,
  "mandate": "mandate_1Mm5yaLkdIwHu7ixmNoLkKLC",
  "metadata": {},
  "next_action": null,
  "on_behalf_of": null,
  "payment_method": "pm_1Mm5yZLkdIwHu7ixf89jW57b",
  "payment_method_options": {
    "acss_debit": {
      "currency": "cad",
      "mandate_options": {
        "interval_description": "First of every month",
        "payment_schedule": "interval",
        "transaction_type": "personal"
      },
      "verification_method": "automatic"
    }
  },
  "payment_method_types": [
    "acss_debit"
  ],
  "single_use_mandate": null,
  "status": "succeeded",
  "usage": "off_session"
}
```
