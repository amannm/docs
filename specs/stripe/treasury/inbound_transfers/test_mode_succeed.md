# Test mode: Succeed an InboundTransfer

Transitions a test mode created InboundTransfer to the `succeeded` status. The InboundTransfer must already be in the `processing` state.

## Returns

Returns the InboundTransfer object in the succeeded state. Returns an error if the InboundTransfer has already succeeded or cannot be succeeded.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/succeed \
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
  "description": "InboundTransfer from my external bank account",
  "failure_details": null,
  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYVxjWLYpw6NpP6LLdBjWjsgc_5Q68S_eJDtpmsSgc_rHslxhpX2qqP0Xqb3fb3uLR2h-INgqgg7E81-mu1FQ",
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
  "status": "succeeded",
  "status_transitions": {
    "failed_at": null,
    "succeeded_at": 1680716025
  },
  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"
}
```
