# Tax Registrations

A Tax `Registration` lets us know that your business is registered to collect tax on payments within a region, enabling you to [automatically collect tax](https://docs.stripe.com/docs/tax.md).

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax `Registration` object. For more information on how to register to collect tax, see [our guide](https://docs.stripe.com/docs/tax/registering.md).

Related guide: [Using the Registrations API](https://docs.stripe.com/docs/tax/registrations-api.md)

## Endpoints

### Create a registration

- [POST /v1/tax/registrations](registrations/create.md)

### Update a registration

- [POST /v1/tax/registrations/:id](registrations/update.md)

### Retrieve a registration

- [GET /v1/tax/registrations/:id](registrations/retrieve.md)

### List registrations

- [GET /v1/tax/registrations](registrations/all.md)
