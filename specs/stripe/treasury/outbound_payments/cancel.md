# Cancel an OutboundPayment

Cancel an OutboundPayment.

## Returns

Returns the OutboundPayment object if the cancellation succeeded. Returns an error if the OutboundPayment has already been canceled or cannot be canceled.

```curl
curl -X POST https://api.stripe.com/v1/treasury/outbound_payments/obp_1MtaD72eZvKYlo2Cu5d5S1kX/cancel \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",
  "object": "treasury.outbound_payment",
  "amount": 10000,
  "cancelable": false,
  "created": 1680716009,
  "currency": "usd",
  "customer": null,
  "description": "OutboundPayment to a 3rd party",
  "destination_payment_method": null,
  "destination_payment_method_details": {
    "billing_details": {
      "address": {
        "city": null,
        "country": null,
        "line1": null,
        "line2": null,
        "postal_code": null,
        "state": null
      },
      "email": null,
      "name": null
    },
    "financial_account": {
      "id": "fa_1LpyM72eZvKYlo2CiUmr2kuV",
      "network": "stripe"
    },
    "type": "financial_account"
  },
  "end_user_details": {
    "ip_address": null,
    "present": false
  },
  "expected_arrival_date": 1680716009,
  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgakyczTzCY6NZMi6lMnZXTYms--WBYQzUXzaEJ_JwErEK5FXXW8F9Qy7fEzKvsHEOzyjS9AtIuK8sUjgWdU",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "payment",
  "status": "canceled",
  "status_transitions": {
    "posted_at": null,
    "failed_at": null,
    "canceled_at": 1680716010,
    "returned_at": null
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
