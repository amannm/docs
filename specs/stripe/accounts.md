# Accounts

This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.

For accounts where [controller.requirement_collection](accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, the properties below are always returned.

For accounts where [controller.requirement_collection](accounts/object.md#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, some properties are only returned until you create an [Account Link](account_links.md) or [Account Session](account_sessions.md) to start Connect Onboarding. Learn about the [differences between accounts](https://docs.stripe.com/connect/accounts.md).

## Endpoints

### Create an account

- [POST /v1/accounts](accounts/create.md)

### Update an account

- [POST /v1/accounts/:id](accounts/update.md)

### Retrieve account

- [GET /v1/accounts/:id](accounts/retrieve.md)

### List all connected accounts

- [GET /v1/accounts](accounts/list.md)

### Delete an account

- [DELETE /v1/accounts/:id](accounts/delete.md)

### Reject an account

- [POST /v1/accounts/:id/reject](account/reject.md)
