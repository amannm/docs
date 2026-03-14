# Cards

You can [create physical or virtual cards](https://docs.stripe.com/docs/issuing.md) that are issued to cardholders.

## Endpoints

### Create a card

- [POST /v1/issuing/cards](cards/create.md)

### Update a card

- [POST /v1/issuing/cards/:id](cards/update.md)

### Retrieve a card

- [GET /v1/issuing/cards/:id](cards/retrieve.md)

### List all cards

- [GET /v1/issuing/cards](cards/list.md)

### Deliver a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/deliver](cards/test_mode_deliver.md)

### Fail a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/fail](cards/test_mode_fail.md)

### Return a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/return](cards/test_mode_return.md)

### Ship a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/ship](cards/test_mode_ship.md)

### Submit a testmode card

- [POST /v1/test_helpers/issuing/cards/:id/shipping/submit](cards/test_mode_submit.md)
