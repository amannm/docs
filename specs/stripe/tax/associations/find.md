# Find a Tax Association

Finds a tax association object by PaymentIntent id.

## Returns

A `Tax Association` object.

## Parameters

- `payment_intent` (string, required)
  Valid [PaymentIntent](https://docs.stripe.com/docs/api/payment_intents/object.md) id

```curl
curl -G https://api.stripe.com/v1/tax/associations/find \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-02-25.clover; payment_intent_with_tax_api_beta=v1" \
  -d payment_intent=pi_3PY55JRw02rhjhAj04XgRlJF
```

### Response

```json
{
  "id": "taxa_1PYP5RRw02rhjhAjNemx66hC",
  "object": "tax.association",
  "calculation": "taxcalc_1PYP4vRw02rhjhAjPfzylM7p",
  "payment_intent": "pi_3PYP4zRw02rhjhAj1UotslTI",
  "tax_transaction_attempts": [
    {
      "source": "pi_1PXmsSE5ebw4kUHWK7FIhQlS",
      "status": "committed",
      "committed": {
        "transaction": "tax_1PXmsRE5ebw4kUHWLyVEiMis"
      }
    },
    {
      "source": "re_1PXmsSE5ebw4kUHWK7FIhQlS",
      "status": "committed",
      "committed": {
        "transaction": "tax_1PXmsgE5ebw4kUHW7Gg8jvpX"
      }
    }
  ]
}
```
