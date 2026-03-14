# Test mode: Post an OutboundPayment

Transitions a test mode created OutboundPayment to the `posted` status. The OutboundPayment must already be in the `processing` state.

## Returns

Returns the OutboundPayment object in the posted state. Returns an error if the OutboundPayment has already been posted or cannot be posted.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_payments/obp_1MtaD72eZvKYlo2C36lgqC6Y/post \
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
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgawWNwbI_w6NZNOI4y6vNpfIP-oQAT5mkBRbOHJN1f08r7jF-UumeywdupuJr7P2cxF8L5JRSVPMmttq_kA",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "payment",
  "status": "posted",
  "status_transitions": {
    "failed_at": null,
    "posted_at": 1680716010,
    "returned_at": null,
    "canceled_at": null
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
