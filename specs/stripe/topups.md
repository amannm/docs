# Top-ups

To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.

Related guide: [Topping up your platform account](https://docs.stripe.com/docs/connect/top-ups.md)

## Endpoints

### Create a top-up

- [POST /v1/topups](topups/create.md)

### Update a top-up

- [POST /v1/topups/:id](topups/update.md)

### Retrieve a top-up

- [GET /v1/topups/:id](topups/retrieve.md)

### List all top-ups

- [GET /v1/topups](topups/list.md)

### Cancel a top-up

- [POST /v1/topups/:id/cancel](topups/cancel.md)
