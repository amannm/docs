# Outbound Payments

Use [OutboundPayments](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments.md) to send funds to another party’s external bank account or [FinancialAccount](outbound_payments.md#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](outbound_payments.md#outbound_transfers).

Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.

Related guide: [Moving money with Treasury using OutboundPayment objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments.md)

## Endpoints

### Create an OutboundPayment

- [POST /v1/treasury/outbound_payments](outbound_payments/create.md)

### Retrieve an OutboundPayment

- [GET /v1/treasury/outbound_payments/:id](outbound_payments/retrieve.md)

### List all OutboundPayments

- [GET /v1/treasury/outbound_payments](outbound_payments/list.md)

### Cancel an OutboundPayment

- [POST /v1/treasury/outbound_payments/:id/cancel](outbound_payments/cancel.md)

### Test mode: Fail an OutboundPayment

- [POST /v1/test_helpers/treasury/outbound_payments/:id/fail](outbound_payments/test_mode_fail.md)

### Test mode: Post an OutboundPayment

- [POST /v1/test_helpers/treasury/outbound_payments/:id/post](outbound_payments/test_mode_post.md)

### Test mode: Return an OutboundPayment

- [POST /v1/test_helpers/treasury/outbound_payments/:id/return](outbound_payments/test_mode_return.md)

### Test mode: Update an OutboundPayment

- [POST /v1/test_helpers/treasury/outbound_payments/:id](outbound_payments/test_mode_update.md)
