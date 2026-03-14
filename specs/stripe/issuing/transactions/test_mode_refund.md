# Refund a test-mode transaction

Refund a test-mode Transaction.

## Returns

A `Transaction` object. This will be the `Transaction` object of type `capture` referenced in the request’s URL, not the new `Transaction` object of type `refund` that will be created as a side-effect of this API call. To find the newly created `Transaction` object, you can use the [Retrieve an authorization](https://stripe.com/docs/api/issuing/authorizations/retrieve) API, whose response will contain a list of related `Transaction` IDs, including the newly created `Transaction` of type `refund`. You can also use the [List all transactions](https://stripe.com/docs/api/issuing/transactions/list) API, or listen for the `issuing_transaction.created` webhook event to retrieve the newly created `Transaction` of type `refund`.

## Parameters

- `refund_amount` (integer, optional)
  The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/transactions/ipi_1GswaK2eZvKYlo2Co7wmNJhD/refund \
  -u "<<YOUR_SECRET_KEY>>" \
  -d refund_amount=1000
```

### Response

```json
{
  "id": "ipi_1GswaK2eZvKYlo2Co7wmNJhD",
  "object": "issuing.transaction",
  "amount": -1000,
  "amount_details": {
    "atm_fee": null,
    "cashback_amount": null
  },
  "authorization": "iauth_1GswaJ2eZvKYlo2Ct9mFMJ4S",
  "balance_transaction": "txn_1GswaK2eZvKYlo2CJAFFIuHg",
  "card": "ic_1Gswa82eZvKYlo2CP2jveFil",
  "cardholder": "ich_1Gswa82eZvKYlo2CvobneLSo",
  "created": 1591905672,
  "currency": "usd",
  "dispute": null,
  "livemode": false,
  "merchant_amount": -1000,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "computer_software_stores",
    "category_code": "5734",
    "city": "SAN FRANCISCO",
    "country": "US",
    "name": "STRIPE.COM",
    "network_id": "1234567890",
    "postal_code": "94103",
    "state": "CA",
    "terminal_id": null
  },
  "metadata": {
    "order_id": "6735"
  },
  "redaction": null,
  "type": "capture",
  "wallet": null
}
```
