# Create a ForwardingRequest

Creates a ForwardingRequest object.

## Returns

Returns a ForwardingRequest object.

## Parameters

- `payment_method` (string, required)
  The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

- `replacements` (array of enums, required)
  The field kinds to be replaced in the forwarded request.
Possible enum values:
  - `card_cvc`
    Replace the card cvc field

  - `card_expiry`
    Replace the card expiry fields like month and year

  - `card_number`
    Replace the card number field

  - `cardholder_name`
    Replace the cardholder name field

  - `request_signature`
    Calculate and replace the request signature field

- `request` (object, required)
  The request body and headers to be sent to the destination endpoint.

  - `request.body` (string, optional)
    The body payload to send to the destination endpoint.

  - `request.headers` (array of objects, optional)
    The headers to include in the forwarded request. Can be omitted if no additional headers (excluding Stripe-generated ones such as the Content-Type header) should be included.

    - `request.headers.name` (string, required)
      The header name.

    - `request.headers.value` (string, required)
      The header value.

- `url` (string, required)
  The destination URL for the forwarded request. Must be supported by the config.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/forwarding/requests \
  -u "<<YOUR_SECRET_KEY>>" \
  --data-urlencode url="https://endpoint-url/v1/payments" \
  -d payment_method=pm_card_visa \
  -d "replacements[0]"=card_number \
  -d "replacements[1]"=card_expiry \
  -d "replacements[2]"=card_cvc \
  -d "replacements[3]"=cardholder_name \
  --data-urlencode "request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}" \
  -d "request[headers][0][name]"=Destination-API-Key \
  -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
  -d "request[headers][1][name]"=Destination-Idempotency-Key \
  -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}}
```

### Response

```json
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
```
