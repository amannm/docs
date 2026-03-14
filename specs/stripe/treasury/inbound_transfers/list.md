# List all InboundTransfers

Returns a list of InboundTransfers sent from the specified FinancialAccount.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` InboundTransfers, starting after InboundTransfer `starting_after`. Each entry in the array is a separate InboundTransfer object. If no more InboundTransfers are available, the resulting array is empty.

## Parameters

- `financial_account` (string, optional)
  Returns objects associated with this FinancialAccount.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`.

```curl
curl -G https://api.stripe.com/v1/treasury/inbound_transfers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtaDM2eZvKYlo2CvXrQknN4 \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/inbound_transfers",
  "has_more": false,
  "data": [
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
  ]
}
```
