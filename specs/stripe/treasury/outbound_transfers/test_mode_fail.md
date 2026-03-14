# Test mode: Fail an OutboundTransfer

Transitions a test mode created OutboundTransfer to the `failed` status. The OutboundTransfer must already be in the `processing` state.

## Returns

Returns the OutboundTransfer object in the failed state. Returns an error if the OutboundTransfer has already been failed or cannot be failed.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/fail \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",
  "object": "treasury.outbound_transfer",
  "amount": 10000,
  "cancelable": false,
  "created": 1680717489,
  "currency": "usd",
  "description": "OutboundTransfer to my external bank account",
  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",
  "destination_payment_method_details": {
    "billing_details": {
      "address": {
        "city": "San Francisco",
        "country": "US",
        "line1": "1234 Fake Street",
        "line2": null,
        "postal_code": "94102",
        "state": "CA"
      },
      "email": null,
      "name": "Jane Austen"
    },
    "type": "us_bank_account",
    "us_bank_account": {
      "account_holder_type": "company",
      "account_type": "checking",
      "bank_name": "STRIPE TEST BANK",
      "fingerprint": "AP24Iso0btGp4N10",
      "last4": "6789",
      "network": "ach",
      "routing_number": "110000000"
    }
  },
  "expected_arrival_date": 1680825600,
  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYw-nE9MNI6NpOJppCfj7fBzxZ9vepfiOLlViIJsILsSUiUv3teC30OLgOpgL7B0UBbYYtz0t7gi1a1WHo4Ew",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "transfer",
  "status": "failed",
  "status_transitions": {
    "failed_at": 1680717489,
    "canceled_at": null,
    "posted_at": null,
    "returned_at": null
  },
  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"
}
```
