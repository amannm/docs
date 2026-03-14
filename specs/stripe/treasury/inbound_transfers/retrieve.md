# Retrieve an InboundTransfer

Retrieves the details of an existing InboundTransfer.

## Returns

Returns an InboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

```curl
curl https://api.stripe.com/v1/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",
  "object": "treasury.inbound_transfer",
  "amount": 10000,
  "cancelable": true,
  "created": 1680716025,
  "currency": "usd",
  "description": "InboundTransfer from my bank account",
  "failure_details": null,
  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww",
  "linked_flows": {
    "received_debit": null
  },
  "livemode": false,
  "metadata": {},
  "origin_payment_method": "pm_1KMDdkGPnV27VyGeAgGz8bsi",
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
  "status": "processing",
  "status_transitions": {
    "failed_at": null,
    "succeeded_at": null
  },
  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"
}
```
