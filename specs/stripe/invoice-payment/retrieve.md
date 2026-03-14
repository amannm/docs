# Retrieve an InvoicePayment

Retrieves the invoice payment with the given ID.

## Returns

Returns an [invoice_payment](https://docs.stripe.com/docs/api/invoices/payments.md) object if a valid invoice payment ID was provided. Otherwise, this call raises [an error](retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/invoice_payments/inpay_1M3USa2eZvKYlo2CBjuwbq0N \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "inpay_1M3USa2eZvKYlo2CBjuwbq0N",
  "object": "invoice_payment",
  "amount_paid": 2000,
  "amount_requested": 2000,
  "created": 1391288554,
  "currency": "usd",
  "invoice": "in_103Q0w2eZvKYlo2C5PYwf6Wf",
  "is_default": true,
  "livemode": false,
  "payment": {
    "type": "payment_intent",
    "payment_intent": "pi_103Q0w2eZvKYlo2C364X582Z"
  },
  "status": "paid",
  "status_transitions": {
    "canceled_at": null,
    "paid_at": 1391288554
  }
}
```
