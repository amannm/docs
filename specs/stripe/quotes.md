# Quote

A Quote is a way to model prices that you’d like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.

## Endpoints

### Create a quote

- [POST /v1/quotes](quotes/create.md)

### Update a quote

- [POST /v1/quotes/:id](quotes/update.md)

### Retrieve a quote

- [GET /v1/quotes/:id](quotes/retrieve.md)

### Retrieve a quote's line items

- [GET /v1/quotes/:id/line_items](quotes/line_items/list.md)

### Retrieve a quote's upfront line items

- [GET /v1/quotes/:id/computed_upfront_line_items](quotes/line_items/upfront/list.md)

### List all quotes

- [GET /v1/quotes](quotes/list.md)

### Accept a quote

- [POST /v1/quotes/:id/accept](quotes/accept.md)

### Cancel a quote

- [POST /v1/quotes/:id/cancel](quotes/cancel.md)

### Download quote PDF

- [GET /v1/quotes/:id/pdf](quotes/pdf.md)

### Finalize a quote

- [POST /v1/quotes/:id/finalize](quotes/finalize.md)
