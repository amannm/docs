# Cancel the current reader action

Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.

## Returns

Returns an updated `Reader` resource.

```curl
curl -X POST https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/cancel_action \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": null,
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1695402450407,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```
