# Confirm a PaymentIntent on the Reader

Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.

## Returns

Returns an updated `Reader` resource.

## Parameters

- `payment_intent` (string, required)
  The ID of the PaymentIntent to confirm.

- `confirm_config` (object, optional)
  Configuration overrides for this confirmation, such as surcharge settings and return URL.

  - `confirm_config.return_url` (string, optional)
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. If you’d prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/confirm_payment_intent \
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
    "type": "confirm_payment_intent"
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
