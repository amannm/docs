# Report Run event types

This is a list of all public [thin events](https://docs.stripe.com/event-destinations.md#thin-events) we currently send for updates to Report Run, which are continually evolving and expanding. The payload of thin events is unversioned. During processing, you must fetch the versioned event from the API or fetch the resource’s current state.

## API event types

### `v2.reporting.report_run.created`

Occurs when a ReportRun is created.

Related object: [Report Run](object.md)

## Attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `related_object` (object)
  Object containing the reference to API resource relevant to the event.

  - `related_object.id` (string)
    Unique identifier for the object relevant to the event.

  - `related_object.type` (string, value is "v2.reporting.report_run")
    Object tag of the resource relevant to the event.

  - `related_object.url` (string)
    URL to retrieve the resource.

- `type` (string, value is "v2.reporting.report_run.created")
  The type of the event.

## Fetched attributes

- `changes` (object)
  Changes that the event makes to properties in the related object. See the [Report Run](object.md) object for the structure of `before` and `after`.

  - `changes.after` (object, nullable)
    Updated values of properties that the event changed. This is `null` for deletion events.

  - `changes.before` (object, nullable)
    Values of properties before the event changes. This is `null` for creation events.

- `data` (object)
  Additional data about the event.

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

### Event payload

```json
{
  "created": "2025-08-26T00:00:00.000Z",
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "type": "v2.reporting.report_run.created",
  "livemode": false,
  "reason": {
    "type": "request",
    "request": {
      "id": "req_xxx",
      "idempotency_key": "xxx"
    }
  },
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  }
}
```

### Event handler

```curl
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```

### Fetched payload

```json
{
  "created": "2025-08-26T00:00:00.000Z",
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "type": "v2.reporting.report_run.created",
  "livemode": false,
  "reason": {
    "type": "request",
    "request": {
      "id": "req_xxx",
      "idempotency_key": "xxx"
    }
  },
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  },
  "data": {},
  "changes": {
    "before": null,
    "after": {
      "created": "2025-08-26T00:00:00.000Z",
      "id": "reprun_test_xxx",
      "object": "v2.reporting.report_run",
      "report": "report_test_xxx",
      "report_name": "test report name",
      "report_parameters": {
        "interval_start": "2025-08-18T00:00:00.000Z",
        "interval_end": "2025-08-25T00:00:00.000Z"
      },
      "result": null,
      "result_options": {
        "compress_file": false
      },
      "status": "running",
      "status_details": {},
      "livemode": false
    }
  }
}
```

### `v2.reporting.report_run.failed`

Occurs when a ReportRun has failed to complete.

Related object: [Report Run](object.md)

## Attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `related_object` (object)
  Object containing the reference to API resource relevant to the event.

  - `related_object.id` (string)
    Unique identifier for the object relevant to the event.

  - `related_object.type` (string, value is "v2.reporting.report_run")
    Object tag of the resource relevant to the event.

  - `related_object.url` (string)
    URL to retrieve the resource.

- `type` (string, value is "v2.reporting.report_run.failed")
  The type of the event.

## Fetched attributes

- `changes` (object)
  Changes that the event makes to properties in the related object. See the [Report Run](object.md) object for the structure of `before` and `after`.

  - `changes.after` (object, nullable)
    Updated values of properties that the event changed. This is `null` for deletion events.

  - `changes.before` (object, nullable)
    Values of properties before the event changes. This is `null` for creation events.

- `data` (object)
  Additional data about the event.

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

### Event payload

```json
{
  "created": "2025-08-26T00:00:00.000Z",
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "type": "v2.reporting.report_run.failed",
  "livemode": false,
  "reason": null,
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  }
}
```

### Event handler

```curl
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```

### Fetched payload

```json
{
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "created": "2025-08-26T00:00:00.000Z",
  "data": {},
  "reason": null,
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  },
  "type": "v2.reporting.report_run.failed",
  "livemode": false,
  "changes": {
    "before": {
      "status": "running",
      "status_details": {}
    },
    "after": {
      "status": "failed",
      "status_details": {
        "failed": {
          "error_code": "file_size_above_limit",
          "error_message": "The file generated by this request exceeds the 5 GB limit."
        }
      }
    }
  }
}
```

### `v2.reporting.report_run.succeeded`

Occurs when a ReportRun has successfully completed.

Related object: [Report Run](object.md)

## Attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `related_object` (object)
  Object containing the reference to API resource relevant to the event.

  - `related_object.id` (string)
    Unique identifier for the object relevant to the event.

  - `related_object.type` (string, value is "v2.reporting.report_run")
    Object tag of the resource relevant to the event.

  - `related_object.url` (string)
    URL to retrieve the resource.

- `type` (string, value is "v2.reporting.report_run.succeeded")
  The type of the event.

## Fetched attributes

- `changes` (object)
  Changes that the event makes to properties in the related object. See the [Report Run](object.md) object for the structure of `before` and `after`.

  - `changes.after` (object, nullable)
    Updated values of properties that the event changed. This is `null` for deletion events.

  - `changes.before` (object, nullable)
    Values of properties before the event changes. This is `null` for creation events.

- `data` (object)
  Additional data about the event.

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

### Event payload

```json
{
  "created": "2025-08-26T00:00:00.000Z",
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "type": "v2.reporting.report_run.succeeded",
  "livemode": false,
  "reason": null,
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  }
}
```

### Event handler

```curl
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```

### Fetched payload

```json
{
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "created": "2025-08-26T00:00:00.000Z",
  "data": {},
  "reason": null,
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  },
  "type": "v2.reporting.report_run.succeeded",
  "livemode": false,
  "changes": {
    "before": {
      "status": "running"
    },
    "after": {
      "status": "succeeded"
    }
  }
}
```

### `v2.reporting.report_run.updated`

Occurs when a ReportRun is updated.

Related object: [Report Run](object.md)

## Attributes

- `id` (string)
  Unique identifier for the event.

- `object` (string, value is "v2.core.event")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `context` (string, nullable)
  Authentication context needed to fetch the event or related object.

- `created` (timestamp)
  Time at which the object was created.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `related_object` (object)
  Object containing the reference to API resource relevant to the event.

  - `related_object.id` (string)
    Unique identifier for the object relevant to the event.

  - `related_object.type` (string, value is "v2.reporting.report_run")
    Object tag of the resource relevant to the event.

  - `related_object.url` (string)
    URL to retrieve the resource.

- `type` (string, value is "v2.reporting.report_run.updated")
  The type of the event.

## Fetched attributes

- `changes` (object)
  Changes that the event makes to properties in the related object. See the [Report Run](object.md) object for the structure of `before` and `after`.

  - `changes.after` (object, nullable)
    Updated values of properties that the event changed. This is `null` for deletion events.

  - `changes.before` (object, nullable)
    Values of properties before the event changes. This is `null` for creation events.

- `data` (object)
  Additional data about the event.

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

### Event payload

```json
{
  "created": "2025-08-26T00:00:00Z",
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "type": "v2.reporting.report_run.updated",
  "livemode": false,
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  }
}
```

### Event handler

```curl
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```bash
# Select a client library to see examples of
# parsing and retrieving event details.
```

### Event handler

```ruby
client = Stripe::StripeClient.new("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = request.env['HTTP_STRIPE_SIGNATURE']

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```python
client = StripeClient("{{YOUR_API_KEY}}")

endpoint_secret = 'whsec_...'
signature_header = ''

thin_event = client.parse_thin_event(
  payload,
  signature_header,
  endpoint_secret
)

event = client.v2.core.events.retrieve(thin_event.id)
```

### Event handler

```php
$stripe = new StripeStripeClient('{{YOUR_API_KEY}}');

$endpoint_secret = 'whsec_...';
$signature_header = $_SERVER['HTTP_STRIPE_SIGNATURE'];

$thin_event = $client->parseThinEvent(
  $payload,
  $signature_header,
  $endpoint_secret
);

$event = $client->v2->core->events->retrieve($thin_event->id);
```

### Event handler

```java
StripeClient client = new StripeClient("{{YOUR_API_KEY}}");

String signatureHeader = request.headers("Stripe-Signature");
String endpointSecret = "whsec_...";

com.stripe.model.ThinEvent thinEvent = client.parseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

com.stripe.model.v2.Event event = client.v2().core().events().retrieve(
  thinEvent.getId()
);
```

### Event handler

```javascript
const stripe = require('stripe')('{{YOUR_API_KEY}}');

const endpoint_secret = 'whsec_...'
const signature_header = '...'

const thinEvent = stripe.parseThinEvent(
  payload,
  signature_header,
  endpoint_secret
);

const event = await stripe.v2.core.events.retrieve(thinEvent.id);

```

### Event handler

```go
err = webhook.ValidatePayload(
  payload,
  signatureHeader,
  endpointSecret
)

if err != nil {
    fmt.Fprintf(os.Stderr, "Error reading request body: %v
", err)
    return
}

var thinEvent map[string]interface{}

if err := json.Unmarshal(payload, &thinEvent); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse thin event body json: %v
", err.Error()
    )
    return
}

eventID := thinEvent["id"].(string)

var event map[string]interface{}
resp, err := client.RawRequest(
  http.MethodGet,
  "/v2/core/events/"+eventID,
  "",
  nil
)
if err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to get pull event: %v
",
      err.Error()
    )
    return
}

if err := json.Unmarshal(resp.RawJSON, &event); err != nil {
    fmt.Fprintf(
      os.Stderr,
      "Failed to parse pull event body json: %v
",
      err.Error()
    )
    return
}
```

### Event handler

```dotnet
var client = new StripeClient("{{YOUR_API_KEY}}");

string endpointSecret = "whsec_...";
string signatureHeader = Request.Headers["Stripe-Signature"];

var thinEvent = client.ParseThinEvent(
  payload,
  signatureHeader,
  endpointSecret
);

var event = await client.V2.Core.Events.GetAsync(thinEvent.Id);
```

### Fetched payload

```json
{
  "id": "evt_test_xxx",
  "object": "v2.core.event",
  "created": "2025-08-26T00:00:00Z",
  "data": {},
  "reason": null,
  "related_object": {
    "id": "reprun_test_xxx",
    "type": "v2.reporting.report_run",
    "url": "/v2/reporting/report_runs/reprun_test_xxx"
  },
  "type": "v2.reporting.report_run.updated",
  "livemode": false,
  "changes": {
    "before": {
      "status": "running"
    },
    "after": {
      "status": "succeeded"
    }
  }
}
```
