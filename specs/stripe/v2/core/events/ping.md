# Ping an Event Destination

Send a `ping` event to an event destination.

## Parameters

- `id` (string, required)
  Identifier for the event destination to ping.

## Returns

## Response attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `changes` (object, nullable)
  Before and after changes for the primary related object.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

- `data` (object, nullable)
  Additional data about the event.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `reason` (object, nullable)
  Reason for the event.

  - `reason.request` (object, nullable)
    Information on the API request that instigated the event.

    - `reason.request.id` (string)
      ID of the API request that caused the event.

    - `reason.request.idempotency_key` (string)
      The idempotency key transmitted during the request.

  - `reason.type` (enum)
    Event reason type.
Possible enum values:
    - `request`
      The event was published as the result of an API request.

- `related_object` (object, nullable)
  Object containing the reference to API resource relevant to the event.

  - `related_object.id` (string)
    Unique identifier for the object relevant to the event.

  - `related_object.type` (string)
    Object tag of the resource relevant to the event.

  - `related_object.url` (string)
    URL to retrieve the resource.

- `type` (string)
  The type of the event.

## Error Codes

| HTTP status code | Code      | Description                |
| ---------------- | --------- | -------------------------- |
| 404              | not_found | The resource wasn’t found. |

```curl
curl -X POST https://api.stripe.com/v2/core/event_destinations/evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92/ping \
  -H "Authorization: Bearer <<YOUR_SECRET_KEY>>" \
  -H "Stripe-Version: 2026-02-25.preview"
```

### Response

```json
{
  "id": "evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92",
  "object": "v2.core.event",
  "context": null,
  "created": "2024-10-22T16:26:54.063Z",
  "data": null,
  "livemode": false,
  "reason": null,
  "related_object": {
    "id": "ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6",
    "type": "event_destination",
    "url": "/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6"
  },
  "type": "v2.core.event_destination.ping"
}
```
