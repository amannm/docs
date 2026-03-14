# Cards

You can store multiple cards on a customer in order to charge the customer later. You can also store multiple debit cards on a recipient in order to transfer to those cards later.

Related guide: [Card payments with Sources](https://docs.stripe.com/docs/sources/cards.md)

## Endpoints

### Create a card

- [POST /v1/customers/:id/sources](cards/create.md)

### Update a card

- [POST /v1/customers/:id/sources/:id](cards/update.md)

### Retrieve a card

- [GET /v1/customers/:id/cards/:id](cards/retrieve.md)

### List all cards

- [GET /v1/customers/:id/cards](cards/list.md)

### Delete a card

- [DELETE /v1/customers/:id/sources/:id](cards/delete.md)
