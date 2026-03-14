# Test mode: Fail an OutboundPayment

Transitions a test mode created OutboundPayment to the `failed` status. The OutboundPayment must already be in the `processing` state.

## Returns

Returns the OutboundPayment object in the failed state. Returns an error if the OutboundPayment has already been failed or cannot be failed.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_payments/obp_1MtaD72eZvKYlo2C36lgqC6Y/fail \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "obp_1MtaD72eZvKYlo2C36lgqC6Y",
  "object": "treasury.outbound_payment",
  "amount": 10000,
  "cancelable": false,
  "created": 1680716009,
  "currency": "usd",
  "customer": null,
  "description": "OutboundPayment to a 3rd party",
  "destination_payment_method": null,
  "destination_payment_method_details": {
    "type": "us_bank_account",
    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"
  },
  "end_user_details": {
    "ip_address": null,
    "present": false
  },
  "expected_arrival_date": 1680716009,
  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgbuLATJtPw6NZOxERTeGKynM40SUCL6A1sqeZF9vkrX4q4M0rI4eY7EhfkOVvyileEuRReLgXE2crXLg7sd",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "payment",
  "status": "failed",
  "status_transitions": {
    "failed_at": 1680716010,
    "posted_at": null,
    "returned_at": null,
    "canceled_at": null
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
