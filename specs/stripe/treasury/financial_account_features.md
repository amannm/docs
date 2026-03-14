# Financial Account Features

Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`. Stripe or the platform can control Features via the requested field.

## Endpoints

### Update FinancialAccount Features

- [POST /v1/treasury/financial_accounts/:id/features](financial_account_features/update.md)

### Retrieve FinancialAccount Features

- [GET /v1/treasury/financial_accounts/:id/features](financial_account_features/retrieve.md)
