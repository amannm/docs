# List all CreditReversals

Returns a list of CreditReversals.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` CreditReversals, starting after CreditReversal `starting_after`. Each entry in the array is a separate CreditReversal object. If no more CreditReversal are available, the resulting array will be empty.

## Parameters

- `financial_account` (string, optional)
  Returns objects associated with this FinancialAccount.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `received_credit` (string, optional)
  Only return CreditReversals for the ReceivedCredit ID.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return CreditReversals for a given status.
Possible enum values:
  - `canceled`
    The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

  - `posted`
    The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

  - `processing`
    The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).

```curl
curl -G https://api.stripe.com/v1/treasury/credit_reversals \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtkGJLkdIwHu7ix6FAcfxof \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/credit_reversals",
  "has_more": false,
  "data": [
    {
      "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",
      "object": "treasury.credit_reversal",
      "amount": 1000,
      "created": 1680756608,
      "currency": "usd",
      "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",
      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",
      "livemode": false,
      "metadata": {},
      "network": "ach",
      "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",
      "status": "processing",
      "status_transitions": {
        "posted_at": null
      },
      "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"
    }
  ]
}
```
