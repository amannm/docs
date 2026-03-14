# Delete a test clock

Deletes a test clock.

## Returns

The deleted `TestClock` object is returned upon success. Otherwise, this call raises [an error](delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",
  "object": "test_helpers.test_clock",
  "deleted": true
}
```
