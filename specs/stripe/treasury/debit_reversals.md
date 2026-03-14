# Debit Reversals

You can reverse some [ReceivedDebits](debit_reversals.md#received_debits) depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

## Endpoints

### Create a DebitReversal

- [POST /v1/treasury/debit_reversals](debit_reversals/create.md)

### Retrieve a DebitReversal

- [GET /v1/treasury/debit_reversals/:id](debit_reversals/retrieve.md)

### List all DebitReversals

- [GET /v1/treasury/debit_reversals](debit_reversals/list.md)
