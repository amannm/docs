# Webhooks

## Unwrap

`webhooks.unwrap() -> void`

**** ``

Validates that the given payload was sent by OpenAI and parses the payload.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.webhooks.unwrap

puts(result)
```

### Domain Types

### Batch Cancelled Webhook Event

- `class BatchCancelledWebhookEvent`

  Sent when a batch API request has been cancelled.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the batch API request was cancelled.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the batch API request.

  - `type: :"batch.cancelled"`

    The type of the event. Always `batch.cancelled`.

    - `:"batch.cancelled"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Batch Completed Webhook Event

- `class BatchCompletedWebhookEvent`

  Sent when a batch API request has been completed.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the batch API request was completed.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the batch API request.

  - `type: :"batch.completed"`

    The type of the event. Always `batch.completed`.

    - `:"batch.completed"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Batch Expired Webhook Event

- `class BatchExpiredWebhookEvent`

  Sent when a batch API request has expired.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the batch API request expired.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the batch API request.

  - `type: :"batch.expired"`

    The type of the event. Always `batch.expired`.

    - `:"batch.expired"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Batch Failed Webhook Event

- `class BatchFailedWebhookEvent`

  Sent when a batch API request has failed.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the batch API request failed.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the batch API request.

  - `type: :"batch.failed"`

    The type of the event. Always `batch.failed`.

    - `:"batch.failed"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Eval Run Canceled Webhook Event

- `class EvalRunCanceledWebhookEvent`

  Sent when an eval run has been canceled.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the eval run was canceled.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the eval run.

  - `type: :"eval.run.canceled"`

    The type of the event. Always `eval.run.canceled`.

    - `:"eval.run.canceled"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Eval Run Failed Webhook Event

- `class EvalRunFailedWebhookEvent`

  Sent when an eval run has failed.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the eval run failed.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the eval run.

  - `type: :"eval.run.failed"`

    The type of the event. Always `eval.run.failed`.

    - `:"eval.run.failed"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Eval Run Succeeded Webhook Event

- `class EvalRunSucceededWebhookEvent`

  Sent when an eval run has succeeded.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the eval run succeeded.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the eval run.

  - `type: :"eval.run.succeeded"`

    The type of the event. Always `eval.run.succeeded`.

    - `:"eval.run.succeeded"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Fine Tuning Job Cancelled Webhook Event

- `class FineTuningJobCancelledWebhookEvent`

  Sent when a fine-tuning job has been cancelled.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the fine-tuning job.

  - `type: :"fine_tuning.job.cancelled"`

    The type of the event. Always `fine_tuning.job.cancelled`.

    - `:"fine_tuning.job.cancelled"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Fine Tuning Job Failed Webhook Event

- `class FineTuningJobFailedWebhookEvent`

  Sent when a fine-tuning job has failed.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the fine-tuning job failed.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the fine-tuning job.

  - `type: :"fine_tuning.job.failed"`

    The type of the event. Always `fine_tuning.job.failed`.

    - `:"fine_tuning.job.failed"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Fine Tuning Job Succeeded Webhook Event

- `class FineTuningJobSucceededWebhookEvent`

  Sent when a fine-tuning job has succeeded.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the fine-tuning job.

  - `type: :"fine_tuning.job.succeeded"`

    The type of the event. Always `fine_tuning.job.succeeded`.

    - `:"fine_tuning.job.succeeded"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Realtime Call Incoming Webhook Event

- `class RealtimeCallIncomingWebhookEvent`

  Sent when Realtime API Receives a incoming SIP call.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the model response was completed.

  - `data: { call_id, sip_headers}`

    Event data payload.

    - `call_id: String`

      The unique ID of this call.

    - `sip_headers: Array[{ name, value}]`

      Headers from the SIP Invite.

      - `name: String`

        Name of the SIP Header.

      - `value: String`

        Value of the SIP Header.

  - `type: :"realtime.call.incoming"`

    The type of the event. Always `realtime.call.incoming`.

    - `:"realtime.call.incoming"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Response Cancelled Webhook Event

- `class ResponseCancelledWebhookEvent`

  Sent when a background response has been cancelled.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the model response was cancelled.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the model response.

  - `type: :"response.cancelled"`

    The type of the event. Always `response.cancelled`.

    - `:"response.cancelled"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Response Completed Webhook Event

- `class ResponseCompletedWebhookEvent`

  Sent when a background response has been completed.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the model response was completed.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the model response.

  - `type: :"response.completed"`

    The type of the event. Always `response.completed`.

    - `:"response.completed"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Response Failed Webhook Event

- `class ResponseFailedWebhookEvent`

  Sent when a background response has failed.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the model response failed.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the model response.

  - `type: :"response.failed"`

    The type of the event. Always `response.failed`.

    - `:"response.failed"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Response Incomplete Webhook Event

- `class ResponseIncompleteWebhookEvent`

  Sent when a background response has been interrupted.

  - `id: String`

    The unique ID of the event.

  - `created_at: Integer`

    The Unix timestamp (in seconds) of when the model response was interrupted.

  - `data: { id}`

    Event data payload.

    - `id: String`

      The unique ID of the model response.

  - `type: :"response.incomplete"`

    The type of the event. Always `response.incomplete`.

    - `:"response.incomplete"`

  - `object: :event`

    The object of the event. Always `event`.

    - `:event`

### Unwrap Webhook Event

- `UnwrapWebhookEvent = BatchCancelledWebhookEvent | BatchCompletedWebhookEvent | BatchExpiredWebhookEvent | 12 more`

  Sent when a batch API request has been cancelled.

  - `class BatchCancelledWebhookEvent`

    Sent when a batch API request has been cancelled.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the batch API request was cancelled.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the batch API request.

    - `type: :"batch.cancelled"`

      The type of the event. Always `batch.cancelled`.

      - `:"batch.cancelled"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class BatchCompletedWebhookEvent`

    Sent when a batch API request has been completed.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the batch API request was completed.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the batch API request.

    - `type: :"batch.completed"`

      The type of the event. Always `batch.completed`.

      - `:"batch.completed"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class BatchExpiredWebhookEvent`

    Sent when a batch API request has expired.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the batch API request expired.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the batch API request.

    - `type: :"batch.expired"`

      The type of the event. Always `batch.expired`.

      - `:"batch.expired"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class BatchFailedWebhookEvent`

    Sent when a batch API request has failed.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the batch API request failed.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the batch API request.

    - `type: :"batch.failed"`

      The type of the event. Always `batch.failed`.

      - `:"batch.failed"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class EvalRunCanceledWebhookEvent`

    Sent when an eval run has been canceled.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the eval run was canceled.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the eval run.

    - `type: :"eval.run.canceled"`

      The type of the event. Always `eval.run.canceled`.

      - `:"eval.run.canceled"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class EvalRunFailedWebhookEvent`

    Sent when an eval run has failed.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the eval run failed.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the eval run.

    - `type: :"eval.run.failed"`

      The type of the event. Always `eval.run.failed`.

      - `:"eval.run.failed"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class EvalRunSucceededWebhookEvent`

    Sent when an eval run has succeeded.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the eval run succeeded.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the eval run.

    - `type: :"eval.run.succeeded"`

      The type of the event. Always `eval.run.succeeded`.

      - `:"eval.run.succeeded"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class FineTuningJobCancelledWebhookEvent`

    Sent when a fine-tuning job has been cancelled.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the fine-tuning job.

    - `type: :"fine_tuning.job.cancelled"`

      The type of the event. Always `fine_tuning.job.cancelled`.

      - `:"fine_tuning.job.cancelled"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class FineTuningJobFailedWebhookEvent`

    Sent when a fine-tuning job has failed.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the fine-tuning job failed.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the fine-tuning job.

    - `type: :"fine_tuning.job.failed"`

      The type of the event. Always `fine_tuning.job.failed`.

      - `:"fine_tuning.job.failed"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class FineTuningJobSucceededWebhookEvent`

    Sent when a fine-tuning job has succeeded.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the fine-tuning job.

    - `type: :"fine_tuning.job.succeeded"`

      The type of the event. Always `fine_tuning.job.succeeded`.

      - `:"fine_tuning.job.succeeded"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class RealtimeCallIncomingWebhookEvent`

    Sent when Realtime API Receives a incoming SIP call.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the model response was completed.

    - `data: { call_id, sip_headers}`

      Event data payload.

      - `call_id: String`

        The unique ID of this call.

      - `sip_headers: Array[{ name, value}]`

        Headers from the SIP Invite.

        - `name: String`

          Name of the SIP Header.

        - `value: String`

          Value of the SIP Header.

    - `type: :"realtime.call.incoming"`

      The type of the event. Always `realtime.call.incoming`.

      - `:"realtime.call.incoming"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class ResponseCancelledWebhookEvent`

    Sent when a background response has been cancelled.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the model response was cancelled.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the model response.

    - `type: :"response.cancelled"`

      The type of the event. Always `response.cancelled`.

      - `:"response.cancelled"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class ResponseCompletedWebhookEvent`

    Sent when a background response has been completed.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the model response was completed.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the model response.

    - `type: :"response.completed"`

      The type of the event. Always `response.completed`.

      - `:"response.completed"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class ResponseFailedWebhookEvent`

    Sent when a background response has failed.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the model response failed.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the model response.

    - `type: :"response.failed"`

      The type of the event. Always `response.failed`.

      - `:"response.failed"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`

  - `class ResponseIncompleteWebhookEvent`

    Sent when a background response has been interrupted.

    - `id: String`

      The unique ID of the event.

    - `created_at: Integer`

      The Unix timestamp (in seconds) of when the model response was interrupted.

    - `data: { id}`

      Event data payload.

      - `id: String`

        The unique ID of the model response.

    - `type: :"response.incomplete"`

      The type of the event. Always `response.incomplete`.

      - `:"response.incomplete"`

    - `object: :event`

      The object of the event. Always `event`.

      - `:event`
