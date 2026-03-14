# Outbound Transfers

Use [OutboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers.md) to transfer funds from a [FinancialAccount](outbound_transfers.md#financial_accounts) to a PaymentMethod belonging to the same entity. To send funds to a different party, use [OutboundPayments](outbound_transfers.md#outbound_payments) instead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.

Simulate OutboundTransfer state changes with the `/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only be called on test mode objects.

Related guide: [Moving money with Treasury using OutboundTransfer objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers.md)

## Endpoints

### Create an OutboundTransfer

- [POST /v1/treasury/outbound_transfers](outbound_transfers/create.md)

### Retrieve an OutboundTransfer

- [GET /v1/treasury/outbound_transfers/:id](outbound_transfers/retrieve.md)

### List all OutboundTransfers

- [GET /v1/treasury/outbound_transfers](outbound_transfers/list.md)

### Cancel an OutboundTransfer

- [POST /v1/treasury/outbound_transfers/:id/cancel](outbound_transfers/cancel.md)

### Test mode: Fail an OutboundTransfer

- [POST /v1/test_helpers/treasury/outbound_transfers/:id/fail](outbound_transfers/test_mode_fail.md)

### Test mode: Post an OutboundTransfer

- [POST /v1/test_helpers/treasury/outbound_transfers/:id/post](outbound_transfers/test_mode_post.md)

### Test mode: Return an OutboundTransfer

- [POST /v1/test_helpers/treasury/outbound_transfers/:id/return](outbound_transfers/test_mode_return.md)

### Test mode: Update an OutboundTransfer

- [POST /v1/test_helpers/treasury/outbound_transfers/:id](outbound_transfers/test_mode_update.md)
