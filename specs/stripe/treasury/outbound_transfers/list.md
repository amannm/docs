# List all OutboundTransfers

Returns a list of OutboundTransfers sent from the specified FinancialAccount.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` OutboundTransfers, starting after OutboundTransfer `starting_after`. Each entry in the array is a separate OutboundTransfer object. If no more OutboundTransfers are available, the resulting array is empty.

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
  Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`.

```curl
curl -G https://api.stripe.com/v1/treasury/outbound_transfers \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3 \
  -d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/outbound_transfers",
  "has_more": false,
  "data": [
    {
      "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",
      "object": "treasury.outbound_transfer",
      "amount": 500,
      "cancelable": true,
      "created": 1680717489,
      "currency": "usd",
      "description": "OutboundTransfer to my external bank account",
      "destination_payment_method": "pm_1234567890",
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
      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA",
      "livemode": false,
      "metadata": {},
      "returned_details": null,
      "statement_descriptor": "transfer",
      "status": "processing",
      "status_transitions": {
        "canceled_at": null,
        "failed_at": null,
        "posted_at": null,
        "returned_at": null
      },
      "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"
    }
  ]
}
```
