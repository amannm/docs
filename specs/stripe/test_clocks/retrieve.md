# Retrieve a test clock

Retrieves a test clock.

## Returns

Returns the `TestClock` object. Otherwise, this call raises [an error](retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "created": 1680112806,
  "deletes_after": 1680717606,
  "frozen_time": 1577836800,
  "livemode": false,
  "name": null,
  "status": "ready"
}
```
