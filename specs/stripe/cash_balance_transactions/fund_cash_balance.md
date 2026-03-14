# Fund a test mode cash balance

Create an incoming testmode bank transfer

## Returns

Returns a specific cash balance transaction, which funded the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

## Parameters

- `amount` (integer, required)
  Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).

- `currency` (enum, required)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `reference` (string, optional)
  A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe’s [reconciliation algorithm](https://docs.stripe.com/docs/payments/customer-balance/reconciliation.md) applies to different user inputs.

```curl
curl https://api.stripe.com/v1/test_helpers/customers/cus_9s6XKzkNRiz8i3/fund_cash_balance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d amount=5000 \
  -d currency=eur
```

### Response

```json
{
  "id": "ccsbtxn_1NlhIV2eZvKYlo2CKwRcXkii",
  "object": "customer_cash_balance_transaction",
  "created": 1693612963,
  "currency": "eur",
  "customer": "cus_9s6XKzkNRiz8i3",
  "ending_balance": 10000,
  "funded": {
    "bank_transfer": {
      "eu_bank_transfer": {
        "bic": "BANKDEAAXXX",
        "iban_last4": "7089",
        "sender_name": "Sample Business GmbH"
      },
      "reference": "Payment for Invoice 28278FC-155",
      "type": "eu_bank_transfer"
    }
  },
  "livemode": false,
  "net_amount": 5000,
  "type": "funded"
}
```
