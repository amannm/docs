# Advance a test clock

Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to `Ready`.

## Returns

A `TestClock` object with status `Advancing` is returned upon success. Otherwise, this call raises [an error](advance.md#errors).

## Parameters

- `frozen_time` (timestamp, required)
  The time to advance the test clock. Must be after the test clock’s current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.

```curl
curl https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7/advance \
  -u "<<YOUR_SECRET_KEY>>" \
  -d frozen_time=1680199613
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
  "status": "advancing"
}
```
