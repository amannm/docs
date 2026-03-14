# Meters

Meters specify how to aggregate meter events over a billing period. Meter events represent the actions that customers take in your system. Meters attach to prices and form the basis of the bill.

Related guide: [Usage based billing](https://docs.stripe.com/billing/subscriptions/usage-based.md)

## Endpoints

### Create a billing meter

- [POST /v1/billing/meters](meter/create.md)

### Update a billing meter

- [POST /v1/billing/meters/:id](meter/update.md)

### Retrieve a billing meter

- [GET /v1/billing/meters/:id](meter/retrieve.md)

### List billing meters

- [GET /v1/billing/meters](meter/list.md)

### Deactivate a billing meter

- [POST /v1/billing/meters/:id/deactivate](meter/deactivate.md)

### Reactivate a billing meter

- [POST /v1/billing/meters/:id/reactivate](meter/reactivate.md)
