# Create a CVC update token

Creates a single-use token that represents an updated CVC value that you can use for [CVC re-collection](https://docs.stripe.com/docs/payments/accept-a-payment-synchronously.md#web-recollect-cvc). Use this token when [you confirm a card payment](https://docs.stripe.com/docs/api/payment_intents/confirm.md#confirm_payment_intent-payment_method_options-card-cvc_token) or use a saved card on a `PaymentIntent` with `confirmation_method: manual`.

For most cases, use our [JavaScript library](https://docs.stripe.com/docs/js/tokens/create_token?type=cvc_update) instead of using the API. For a `PaymentIntent` with `confirmation_method: automatic`, use our recommended [payments integration](https://docs.stripe.com/docs/payments/save-during-payment.md#web-recollect-cvc) without tokenizing the CVC value.

## Returns

Returns the created CVC update token if it’s successful. Otherwise, this call raises [an error](create_cvc_update.md#errors).

## Parameters

- `cvc_update` (object, required)
  The updated CVC value this token represents.

  - `cvc_update.cvc` (string, required)
    The CVC value, in string form.

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "cvc_update[cvc]"=123
```

### Response

```json
{
  "id": "cvctok_1NkWsu2eZvKYlo2CFDm6ab7X",
  "object": "token",
  "client_ip": null,
  "created": 1693334608,
  "livemode": false,
  "redaction": null,
  "type": "cvc_update",
  "used": false
}
```
