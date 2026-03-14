# Credit Note

Issue a credit note to adjust an invoice’s amount after the invoice is finalized.

Related guide: [Credit notes](https://docs.stripe.com/docs/billing/invoices/credit-notes.md)

## Endpoints

### Create a credit note

- [POST /v1/credit_notes](credit_notes/create.md)

### Update a credit note

- [POST /v1/credit_notes/:id](credit_notes/update.md)

### Retrieve a credit note

- [GET /v1/credit_notes/:id](credit_notes/retrieve.md)

### Retrieve a credit note preview's line items

- [GET /v1/credit_notes/preview/lines](credit_notes/preview_lines.md)

### Retrieve a credit note's line items

- [GET /v1/credit_notes/:id/lines](credit_notes/lines.md)

### List all credit notes

- [GET /v1/credit_notes](credit_notes/list.md)

### Preview a credit note

- [GET /v1/credit_notes/preview](credit_notes/preview.md)

### Void a credit note

- [POST /v1/credit_notes/:id/void](credit_notes/void.md)
