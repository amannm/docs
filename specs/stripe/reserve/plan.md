# Reserve Plans

ReservePlans are used to automatically place holds on a merchant’s funds until the plan expires.       It takes a portion of each incoming Charge (including those resulting from a Transfer from a platform account).

## Endpoints

### Create a ReservePlan

- [POST /v1/reserve/plans](plan/create.md)

### Update a ReservePlan

- [POST /v1/reserve/plans/:id](plan/update.md)

### Retrieve a ReservePlan

- [GET /v1/reserve/plans/:id](plan/retrieve.md)

### List ReservePlans

- [GET /v1/reserve/plans](plan/list.md)

### Disable a ReservePlan

- [POST /v1/reserve/plans/:id/disable](plan/disable.md)
