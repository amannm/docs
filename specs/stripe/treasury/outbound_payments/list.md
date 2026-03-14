# List all OutboundPayments

Returns a list of OutboundPayments sent from the specified FinancialAccount.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` OutboundPayments, starting after OutboundPayments `starting_after`. Each entry in the array is a separate OutboundPayments object. If no more OutboundPayments are available, the resulting array is empty.

## Parameters

- `financial_account` (string, optional)
  Returns objects associated with this FinancialAccount.

- `created` (object, optional)
  Only return OutboundPayments that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `customer` (string, optional)
  Only return OutboundPayments sent to this customer.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`.

```curl
curl -G https://api.stripe.com/v1/treasury/outbound_payments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/outbound_payments",
  "has_more": false,
  "data": [
    {
      "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",
      "object": "treasury.outbound_payment",
      "amount": 10000,
      "cancelable": false,
      "created": 1680716009,
      "currency": "usd",
      "customer": "cus_4QFOF3xrvBT2nU",
      "description": "OutboundPayment to a 3rd party",
      "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",
      "destination_payment_method_details": {
        "type": "us_bank_account",
        "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"
      },
      "end_user_details": {
        "ip_address": null,
        "present": false
      },
      "expected_arrival_date": 1680716009,
      "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",
      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",
      "livemode": false,
      "metadata": {},
      "returned_details": null,
      "statement_descriptor": "payment",
      "status": "processing",
      "status_transitions": {
        "canceled_at": null,
        "failed_at": null,
        "posted_at": null,
        "returned_at": null
      },
      "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
    }
  ]
}
```
