# Retrieve an OutboundPayment

Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.

## Returns

Returns an OutboundPayment object if a valid identifier was provided. Otherwise, returns an error.

```curl
curl https://api.stripe.com/v1/treasury/outbound_payments/obp_1MtaD72eZvKYlo2Cu5d5S1kX \
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
  "customer": "cus_4QFOF3xrvBT2nU",
  "description": "OutboundPayment to a 3rd party",
  "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",
  "destination_payment_method_details": {
    "type": "us_bank_account",
    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"
  },
  "end_user_details": {
    "ip_address": null,
    "present": false
  },
  "expected_arrival_date": 1680716009,
  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "payment",
  "status": "processing",
  "status_transitions": {
    "canceled_at": null,
    "failed_at": null,
    "posted_at": null,
    "returned_at": null
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
