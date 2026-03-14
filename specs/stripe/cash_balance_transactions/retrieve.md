# Retrieve a cash balance transaction

Retrieves a specific cash balance transaction, which updated the customer’s [cash balance](https://docs.stripe.com/docs/payments/customer-balance.md).

## Returns

Returns a cash balance transaction object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions/ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",
  "object": "customer_cash_balance_transaction",
  "created": 1690829143,
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
