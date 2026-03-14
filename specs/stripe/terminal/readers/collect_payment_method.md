# Hand off a PaymentIntent to a Reader and collect card details

Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `payment_intent` (string, required)
  The ID of the PaymentIntent to collect a payment method for.

- `collect_config` (object, optional)
  Configuration overrides for this collection, such as tipping, surcharging, and customer cancellation settings.

  - `collect_config.allow_redisplay` (enum, optional)
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
Possible enum values:
    - `always`
      Use `always` to indicate that this payment method can always be shown to a customer in a checkout flow.

    - `limited`
      Use `limited` to indicate that this payment method can’t always be shown to a customer in a checkout flow. For example, it can only be shown in the context of a specific subscription.

    - `unspecified`
      This is the default value for payment methods where `allow_redisplay` wasn’t set.

  - `collect_config.enable_customer_cancellation` (boolean, optional)
    Enables cancel button on transaction screens.

  - `collect_config.skip_tipping` (boolean, optional)
    Override showing a tipping selection screen on this transaction.

  - `collect_config.tipping` (object, optional)
    Tipping configuration for this transaction.

    - `collect_config.tipping.amount_eligible` (integer, optional)
      Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/collect_payment_method \
  -u "<<YOUR_SECRET_KEY>>" \
  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "collect_payment_method": {
      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"
    },
    "status": "in_progress",
    "type": "collect_payment_method"
  },
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1681320543815,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```
