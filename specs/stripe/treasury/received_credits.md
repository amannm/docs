# Received Credits

ReceivedCredits represent funds sent to a [FinancialAccount](received_credits.md#financial_accounts) (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

## Endpoints

### Retrieve a ReceivedCredit

- [GET /v1/treasury/received_credits/:id](received_credits/retrieve.md)

### List all ReceivedCredits

- [GET /v1/treasury/received_credits](received_credits/list.md)

### Test mode: Create a ReceivedCredit

- [POST /v1/test_helpers/treasury/received_credits](received_credits/test_mode_create.md)
