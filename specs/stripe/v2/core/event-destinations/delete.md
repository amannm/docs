# Delete an Event Destination

Delete an event destination.

## Parameters

- `id` (string, required)
  Identifier for the event destination to delete.

## Returns

## Response attributes

- `id` (string)
  Identifier for the deleted event destination.

- `object` (string)
  The type of the deleted resource.

## Error Codes

| HTTP status code | Code              | Description                                                     |
| ---------------- | ----------------- | --------------------------------------------------------------- |
| 404              | not_found         | The resource wasn’t found.                                      |
| 409              | idempotency_error | An idempotent retry occurred with different request parameters. |

```curl
curl -X DELETE https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-02-25.preview"
```

### Response

```json
{
  "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
  "object": "v2.core.event_destination"
}
```
