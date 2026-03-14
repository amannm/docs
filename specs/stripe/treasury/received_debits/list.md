# List all ReceivedDebits

Returns a list of ReceivedDebits.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` ReceivedDebits, starting after ReceivedDebit `starting_after`. Each entry in the array is a separate ReceivedDebit object. If no more ReceivedDebits are available, the resulting array will be empty.

## Parameters

- `financial_account` (string, optional)
  The FinancialAccount that funds were pulled from.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return ReceivedDebits that have the given status: `succeeded` or `failed`.
Possible enum values:
  - `failed`
    The ReceivedDebit was declined, and no Transaction was created.

  - `succeeded`
    The ReceivedDebit was approved.

```curl
curl -G https://api.stripe.com/v1/treasury/received_debits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/received_debits",
  "has_more": false,
  "data": [
    {
      "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
      "object": "treasury.received_debit",
      "amount": 1000,
      "created": 1680755530,
      "currency": "usd",
      "description": "Stripe Test",
      "failure_code": null,
      "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
      "initiating_payment_method_details": {
        "billing_details": {
          "address": {
            "city": null,
            "country": null,
            "line1": null,
            "line2": null,
            "postal_code": null,
            "state": null
          },
          "email": null,
          "name": "Jane Austen"
        },
        "type": "us_bank_account",
        "us_bank_account": {
          "bank_name": "STRIPE TEST BANK",
          "last4": "6789",
          "routing_number": "110000000"
        }
      },
      "linked_flows": {
        "debit_reversal": null,
        "inbound_transfer": null,
        "issuing_authorization": null,
        "issuing_transaction": null,
        "payout": null
      },
      "livemode": false,
      "network": "ach",
      "reversal_details": {
        "deadline": 1681084800,
        "restricted_reason": null
      },
      "status": "succeeded",
      "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"
    }
  ]
}
```
