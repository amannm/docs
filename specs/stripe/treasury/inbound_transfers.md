# Inbound Transfers

Use [InboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers.md) to add funds to your [FinancialAccount](inbound_transfers.md#financial_accounts) via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

Related guide: [Moving money with Treasury using InboundTransfer objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers.md)

## Endpoints

### Create an InboundTransfer

- [POST /v1/treasury/inbound_transfers](inbound_transfers/create.md)

### Retrieve an InboundTransfer

- [GET /v1/treasury/inbound_transfers/:id](inbound_transfers/retrieve.md)

### List all InboundTransfers

- [GET /v1/treasury/inbound_transfers](inbound_transfers/list.md)

### Cancel an InboundTransfer

- [POST /v1/treasury/inbound_transfers/:id/cancel](inbound_transfers/cancel.md)

### Test mode: Fail an InboundTransfer

- [POST /v1/test_helpers/treasury/inbound_transfers/:id/fail](inbound_transfers/test_mode_fail.md)

### Test mode: Return an InboundTransfer

- [POST /v1/test_helpers/treasury/inbound_transfers/:id/return](inbound_transfers/test_mode_return.md)

### Test mode: Succeed an InboundTransfer

- [POST /v1/test_helpers/treasury/inbound_transfers/:id/succeed](inbound_transfers/test_mode_succeed.md)
