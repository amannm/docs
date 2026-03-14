# Accounts

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

## Endpoints

### Retrieve an Account

- [GET /v1/financial_connections/accounts/:id](accounts/retrieve.md)

### List Accounts

- [GET /v1/financial_connections/accounts](accounts/list.md)

### Disconnect an Account

- [POST /v1/financial_connections/accounts/:id/disconnect](accounts/disconnect.md)

### Refresh Account data

- [POST /v1/financial_connections/accounts/:id/refresh](accounts/refresh.md)

### Subscribe to data refreshes for an Account

- [POST /v1/financial_connections/accounts/:id/subscribe](accounts/subscribe.md)

### Unsubscribe from data refreshes for an Account

- [POST /v1/financial_connections/accounts/:id/unsubscribe](accounts/unsubscribe.md)
