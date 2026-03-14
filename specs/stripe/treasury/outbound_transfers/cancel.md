# Cancel an OutboundTransfer

An OutboundTransfer can be canceled if the funds have not yet been paid out.

## Returns

Returns the OutboundTransfer object if the cancellation succeeded. Returns an error if the object has already been canceled or cannot be canceled.

```curl
curl -X POST https://api.stripe.com/v1/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/cancel \
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
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgbFx5vTNec6NpPKphE93zYcPDgqrHcZhLW_fmKqG9Mu9HUNa_164u93bqkgnPNnYtd3_5Rv_F3YISrR2qg3FQ",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "transfer",
  "status": "canceled",
  "status_transitions": {
    "posted_at": null,
    "failed_at": null,
    "canceled_at": 1680717489,
    "returned_at": null
  },
  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"
}
```
