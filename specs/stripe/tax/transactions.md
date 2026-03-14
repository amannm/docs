# Tax Transactions

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: [Calculate tax in your custom payment flow](https://docs.stripe.com/docs/tax/custom.md#tax-transaction)

## Endpoints

### Create a reversal transaction

- [POST /v1/tax/transactions/create_reversal](transactions/create_reversal.md)

### Create a transaction from a calculation

- [POST /v1/tax/transactions/create_from_calculation](transactions/create_from_calculation.md)

### Retrieve a transaction

- [GET /v1/tax/transactions/:id](transactions/retrieve.md)

### Retrieve a transaction's line items

- [GET /v1/tax/transactions/:id/line_items](transactions/line_items.md)
