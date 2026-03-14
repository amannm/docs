# Refunds

Refund objects allow you to refund a previously created charge that isn’t refunded yet. Funds are refunded to the credit or debit card that’s initially charged.

Related guide: [Refunds](https://docs.stripe.com/docs/refunds.md)

## Endpoints

### Create a refund

- [POST /v1/refunds](refunds/create.md)

### Update a refund

- [POST /v1/refunds/:id](refunds/update.md)

### Retrieve a refund

- [GET /v1/refunds/:id](refunds/retrieve.md)

### List all refunds

- [GET /v1/refunds](refunds/list.md)

### Cancel a refund

- [POST /v1/refunds/:id/cancel](refunds/cancel.md)
