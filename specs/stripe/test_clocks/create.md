# Create a test clock

Creates a new test clock that can be attached to new customers and quotes.

## Returns

The newly created `TestClock` object is returned upon success. Otherwise, this call raises [an error](create.md#errors).

## Parameters

- `frozen_time` (timestamp, required)
  The initial frozen time for this test clock.

- `name` (string, optional)
  The name for this test clock.

  The maximum length is 300 characters.

```curl
curl https://api.stripe.com/v1/test_helpers/test_clocks \
  -u "<<YOUR_SECRET_KEY>>" \
  -d frozen_time=1577836800
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
