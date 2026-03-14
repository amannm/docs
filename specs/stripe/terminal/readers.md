# Reader

A Reader represents a physical device for accepting payment details.

Related guide: [Connecting to a reader](https://docs.stripe.com/docs/terminal/payments/connect-reader.md)

## Endpoints

### Create a Reader

- [POST /v1/terminal/readers](readers/create.md)

### Update a Reader

- [POST /v1/terminal/readers/:id](readers/update.md)

### Retrieve a Reader

- [GET /v1/terminal/readers/:id](readers/retrieve.md)

### List all Readers

- [GET /v1/terminal/readers](readers/list.md)

### Delete a Reader

- [DELETE /v1/terminal/readers/:id](readers/delete.md)

### Cancel the current reader action

- [POST /v1/terminal/readers/:id/cancel_action](readers/cancel_action.md)

### Collect inputs using a Reader

- [POST /v1/terminal/readers/:id/collect_inputs](readers/collect_inputs.md)

### Confirm a PaymentIntent on the Reader

- [POST /v1/terminal/readers/:id/confirm_payment_intent](readers/confirm_payment_intent.md)

### Hand off a PaymentIntent to a Reader and collect card details

- [POST /v1/terminal/readers/:id/collect_payment_method](readers/collect_payment_method.md)

### Hand-off a PaymentIntent to a Reader

- [POST /v1/terminal/readers/:id/process_payment_intent](readers/process_payment_intent.md)

### Hand-off a SetupIntent to a Reader

- [POST /v1/terminal/readers/:id/process_setup_intent](readers/process_setup_intent.md)

### Refund a Charge or a PaymentIntent in-person

- [POST /v1/terminal/readers/:id/refund_payment](readers/refund_payment.md)

### Set reader display

- [POST /v1/terminal/readers/:id/set_reader_display](readers/set_reader_display.md)

### Simulate a successful input collection

- [POST /v1/test_helpers/terminal/readers/:id/succeed_input_collection](readers/succeed_input_collection.md)

### Simulate an input collection timeout

- [POST /v1/test_helpers/terminal/readers/:id/timeout_input_collection](readers/timeout_input_collection.md)

### Simulate presenting a payment method

- [POST /v1/test_helpers/terminal/readers/:id/present_payment_method](readers/present_payment_method.md)
