# Create an InboundTransfer

Creates an InboundTransfer.

## Returns

Returns an InboundTransfer object if there were no issues with InboundTransfer creation. The status of the created InboundTransfer object is initially marked as `processing`.

## Parameters

- `amount` (integer, required)
  Amount (in cents) to be transferred.

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `financial_account` (string, required)
  The FinancialAccount to send funds to.

- `origin_payment_method` (string, required)
  The origin payment method to be debited for the InboundTransfer.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `statement_descriptor` (string, optional)
  The complete description that appears on your customers’ statements. Maximum 10 characters. Can only include -#.$&*, spaces, and alphanumeric characters.

```curl
curl https://api.stripe.com/v1/treasury/inbound_transfers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \
  -d amount=10000 \
  -d currency=usd \
  -d origin_payment_method=pm_1KMDdkGPnV27VyGeAgGz8bsi \
  -d description="InboundTransfer from my bank account"
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
