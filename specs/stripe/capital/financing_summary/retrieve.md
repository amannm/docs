# Retrieve financing summary

Retrieve the financing summary object for the account.

## Returns

Returns a financing summary object for the account.

```curl
curl https://api.stripe.com/v1/capital/financing_summary \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

### Response

```json
{
  "object": "capital.financing_summary",
  "details": {
    "advance_amount": 100000,
    "advance_paid_out_at": 1688424277.0578003,
    "currency": "usd",
    "current_repayment_interval": null,
    "fee_amount": 10000,
    "paid_amount": 100263,
    "remaining_amount": 9737,
    "repayments_begin_at": 1688424277.0577993,
    "withhold_rate": 0.05
  },
  "financing_offer": "financingoffer_1NPvU12eZvKYlo2CotjdGRzu",
  "status": "accepted"
}
```
