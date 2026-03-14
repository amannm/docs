# Cancel an InboundTransfer

Cancels an InboundTransfer.

## Returns

Returns the InboundTransfer object if the cancellation succeeded. Returns an error if the InboundTransfer has already been canceled or cannot be canceled.

```curl
curl -X POST https://api.stripe.com/v1/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",
  "object": "treasury.inbound_transfer",
  "amount": 10000,
  "cancelable": false,
  "created": 1680716025,
  "currency": "usd",
  "description": "InboundTransfer from my external bank account",
  "failure_details": null,
  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgZDF2WUT346NpP69bYKokqfNLTOb3qE8__DQL-vkc_p012AyYJYihh7UHvcsjvgXTDDkgEdUmHTimDXsAT0qA",
  "linked_flows": {
    "received_debit": null
  },
  "livemode": false,
  "metadata": {},
  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",
  "origin_payment_method_details": {
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
  "returned": false,
  "statement_descriptor": "transfer",
  "status": "canceled",
  "status_transitions": {
    "posted_at": null,
    "failed_at": null,
    "canceled_at": 1680716025,
    "returned_at": null
  },
  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"
}
```
