# List all ForwardingRequests

Lists all ForwardingRequest objects.

## Returns

Returns a list of ForwardingRequest objects.

## Parameters

- `created` (object, optional)
  Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.

  - `created.gt` (integer, optional)
    Return results where the `created` field is greater than this value.

  - `created.gte` (integer, optional)
    Return results where the `created` field is greater than or equal to this value.

  - `created.lt` (integer, optional)
    Return results where the `created` field is less than this value.

  - `created.lte` (integer, optional)
    Return results where the `created` field is less than or equal to this value.

- `ending_before` (string, optional)
  A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.

```curl
curl -G https://api.stripe.com/v1/forwarding/requests \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/forwarding/requests",
  "has_more": false,
  "data": [
    {
      "id": "fwdreq_123",
      "object": "forwarding.request",
      "created": 1234567890,
      "livemode": false,
      "payment_method": "pm_456",
      "request_details": {
        "body": "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"424242******4242\",\"expiryMonth\":\"03\",\"expiryYear\":\"2030\",\"cvc\":\"***\",\"holderName\":\"First Last\"},\"reference\":\"{{REFERENCE_ID}}\"}",
        "headers": [
          {
            "name": "Destination-API-Key",
            "value": "{{DESTINATION_API_KEY}}"
          },
          {
            "name": "Destination-Idempotency-Key",
            "value": "{{DESTINATION_IDEMPOTENCY_KEY}}"
          },
          {
            "name": "Content-Type",
            "value": "application/json"
          }
        ],
        "http_method": "POST"
      },
      "request_context": {
        "destination_ip_address": "35.190.113.80",
        "destination_duration": 234
      },
      "response_details": {
        "body": "{\"transactionId\":\"example1234\"}",
        "headers": [
          {
            "name": "Content-Type",
            "value": "application/json;charset=UTF-8"
          }
        ],
        "status": 200
      },
      "url": "https://endpoint-url/v1/payments",
      "replacements": [
        "card_number",
        "card_expiry",
        "card_cvc",
        "cardholder_name"
      ]
    }
  ]
}
```
