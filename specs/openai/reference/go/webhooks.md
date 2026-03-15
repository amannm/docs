# Webhooks

## Unwrap

`client.Webhooks.Unwrap(ctx) error`

**** ``

Validates that the given payload was sent by OpenAI and parses the payload.

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Webhooks.Unwrap(context.TODO())
  if err != nil {
    panic(err.Error())
  }
}
```

### Domain Types

### Batch Cancelled Webhook Event

- `type BatchCancelledWebhookEvent struct{…}`

  Sent when a batch API request has been cancelled.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the batch API request was cancelled.

  - `Data BatchCancelledWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the batch API request.

  - `Type BatchCancelled`

    The type of the event. Always `batch.cancelled`.

    - `const BatchCancelledBatchCancelled BatchCancelled = "batch.cancelled"`

  - `Object BatchCancelledWebhookEventObject`

    The object of the event. Always `event`.

    - `const BatchCancelledWebhookEventObjectEvent BatchCancelledWebhookEventObject = "event"`

### Batch Completed Webhook Event

- `type BatchCompletedWebhookEvent struct{…}`

  Sent when a batch API request has been completed.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the batch API request was completed.

  - `Data BatchCompletedWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the batch API request.

  - `Type BatchCompleted`

    The type of the event. Always `batch.completed`.

    - `const BatchCompletedBatchCompleted BatchCompleted = "batch.completed"`

  - `Object BatchCompletedWebhookEventObject`

    The object of the event. Always `event`.

    - `const BatchCompletedWebhookEventObjectEvent BatchCompletedWebhookEventObject = "event"`

### Batch Expired Webhook Event

- `type BatchExpiredWebhookEvent struct{…}`

  Sent when a batch API request has expired.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the batch API request expired.

  - `Data BatchExpiredWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the batch API request.

  - `Type BatchExpired`

    The type of the event. Always `batch.expired`.

    - `const BatchExpiredBatchExpired BatchExpired = "batch.expired"`

  - `Object BatchExpiredWebhookEventObject`

    The object of the event. Always `event`.

    - `const BatchExpiredWebhookEventObjectEvent BatchExpiredWebhookEventObject = "event"`

### Batch Failed Webhook Event

- `type BatchFailedWebhookEvent struct{…}`

  Sent when a batch API request has failed.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the batch API request failed.

  - `Data BatchFailedWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the batch API request.

  - `Type BatchFailed`

    The type of the event. Always `batch.failed`.

    - `const BatchFailedBatchFailed BatchFailed = "batch.failed"`

  - `Object BatchFailedWebhookEventObject`

    The object of the event. Always `event`.

    - `const BatchFailedWebhookEventObjectEvent BatchFailedWebhookEventObject = "event"`

### Eval Run Canceled Webhook Event

- `type EvalRunCanceledWebhookEvent struct{…}`

  Sent when an eval run has been canceled.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the eval run was canceled.

  - `Data EvalRunCanceledWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the eval run.

  - `Type EvalRunCanceled`

    The type of the event. Always `eval.run.canceled`.

    - `const EvalRunCanceledEvalRunCanceled EvalRunCanceled = "eval.run.canceled"`

  - `Object EvalRunCanceledWebhookEventObject`

    The object of the event. Always `event`.

    - `const EvalRunCanceledWebhookEventObjectEvent EvalRunCanceledWebhookEventObject = "event"`

### Eval Run Failed Webhook Event

- `type EvalRunFailedWebhookEvent struct{…}`

  Sent when an eval run has failed.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the eval run failed.

  - `Data EvalRunFailedWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the eval run.

  - `Type EvalRunFailed`

    The type of the event. Always `eval.run.failed`.

    - `const EvalRunFailedEvalRunFailed EvalRunFailed = "eval.run.failed"`

  - `Object EvalRunFailedWebhookEventObject`

    The object of the event. Always `event`.

    - `const EvalRunFailedWebhookEventObjectEvent EvalRunFailedWebhookEventObject = "event"`

### Eval Run Succeeded Webhook Event

- `type EvalRunSucceededWebhookEvent struct{…}`

  Sent when an eval run has succeeded.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the eval run succeeded.

  - `Data EvalRunSucceededWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the eval run.

  - `Type EvalRunSucceeded`

    The type of the event. Always `eval.run.succeeded`.

    - `const EvalRunSucceededEvalRunSucceeded EvalRunSucceeded = "eval.run.succeeded"`

  - `Object EvalRunSucceededWebhookEventObject`

    The object of the event. Always `event`.

    - `const EvalRunSucceededWebhookEventObjectEvent EvalRunSucceededWebhookEventObject = "event"`

### Fine Tuning Job Cancelled Webhook Event

- `type FineTuningJobCancelledWebhookEvent struct{…}`

  Sent when a fine-tuning job has been cancelled.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

  - `Data FineTuningJobCancelledWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the fine-tuning job.

  - `Type FineTuningJobCancelled`

    The type of the event. Always `fine_tuning.job.cancelled`.

    - `const FineTuningJobCancelledFineTuningJobCancelled FineTuningJobCancelled = "fine_tuning.job.cancelled"`

  - `Object FineTuningJobCancelledWebhookEventObject`

    The object of the event. Always `event`.

    - `const FineTuningJobCancelledWebhookEventObjectEvent FineTuningJobCancelledWebhookEventObject = "event"`

### Fine Tuning Job Failed Webhook Event

- `type FineTuningJobFailedWebhookEvent struct{…}`

  Sent when a fine-tuning job has failed.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the fine-tuning job failed.

  - `Data FineTuningJobFailedWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the fine-tuning job.

  - `Type FineTuningJobFailed`

    The type of the event. Always `fine_tuning.job.failed`.

    - `const FineTuningJobFailedFineTuningJobFailed FineTuningJobFailed = "fine_tuning.job.failed"`

  - `Object FineTuningJobFailedWebhookEventObject`

    The object of the event. Always `event`.

    - `const FineTuningJobFailedWebhookEventObjectEvent FineTuningJobFailedWebhookEventObject = "event"`

### Fine Tuning Job Succeeded Webhook Event

- `type FineTuningJobSucceededWebhookEvent struct{…}`

  Sent when a fine-tuning job has succeeded.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

  - `Data FineTuningJobSucceededWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the fine-tuning job.

  - `Type FineTuningJobSucceeded`

    The type of the event. Always `fine_tuning.job.succeeded`.

    - `const FineTuningJobSucceededFineTuningJobSucceeded FineTuningJobSucceeded = "fine_tuning.job.succeeded"`

  - `Object FineTuningJobSucceededWebhookEventObject`

    The object of the event. Always `event`.

    - `const FineTuningJobSucceededWebhookEventObjectEvent FineTuningJobSucceededWebhookEventObject = "event"`

### Realtime Call Incoming Webhook Event

- `type RealtimeCallIncomingWebhookEvent struct{…}`

  Sent when Realtime API Receives a incoming SIP call.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the model response was completed.

  - `Data RealtimeCallIncomingWebhookEventData`

    Event data payload.

    - `CallID string`

      The unique ID of this call.

    - `SipHeaders []RealtimeCallIncomingWebhookEventDataSipHeader`

      Headers from the SIP Invite.

      - `Name string`

        Name of the SIP Header.

      - `Value string`

        Value of the SIP Header.

  - `Type RealtimeCallIncoming`

    The type of the event. Always `realtime.call.incoming`.

    - `const RealtimeCallIncomingRealtimeCallIncoming RealtimeCallIncoming = "realtime.call.incoming"`

  - `Object RealtimeCallIncomingWebhookEventObject`

    The object of the event. Always `event`.

    - `const RealtimeCallIncomingWebhookEventObjectEvent RealtimeCallIncomingWebhookEventObject = "event"`

### Response Cancelled Webhook Event

- `type ResponseCancelledWebhookEvent struct{…}`

  Sent when a background response has been cancelled.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the model response was cancelled.

  - `Data ResponseCancelledWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the model response.

  - `Type ResponseCancelled`

    The type of the event. Always `response.cancelled`.

    - `const ResponseCancelledResponseCancelled ResponseCancelled = "response.cancelled"`

  - `Object ResponseCancelledWebhookEventObject`

    The object of the event. Always `event`.

    - `const ResponseCancelledWebhookEventObjectEvent ResponseCancelledWebhookEventObject = "event"`

### Response Completed Webhook Event

- `type ResponseCompletedWebhookEvent struct{…}`

  Sent when a background response has been completed.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the model response was completed.

  - `Data ResponseCompletedWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the model response.

  - `Type ResponseCompleted`

    The type of the event. Always `response.completed`.

    - `const ResponseCompletedResponseCompleted ResponseCompleted = "response.completed"`

  - `Object ResponseCompletedWebhookEventObject`

    The object of the event. Always `event`.

    - `const ResponseCompletedWebhookEventObjectEvent ResponseCompletedWebhookEventObject = "event"`

### Response Failed Webhook Event

- `type ResponseFailedWebhookEvent struct{…}`

  Sent when a background response has failed.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the model response failed.

  - `Data ResponseFailedWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the model response.

  - `Type ResponseFailed`

    The type of the event. Always `response.failed`.

    - `const ResponseFailedResponseFailed ResponseFailed = "response.failed"`

  - `Object ResponseFailedWebhookEventObject`

    The object of the event. Always `event`.

    - `const ResponseFailedWebhookEventObjectEvent ResponseFailedWebhookEventObject = "event"`

### Response Incomplete Webhook Event

- `type ResponseIncompleteWebhookEvent struct{…}`

  Sent when a background response has been interrupted.

  - `ID string`

    The unique ID of the event.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the model response was interrupted.

  - `Data ResponseIncompleteWebhookEventData`

    Event data payload.

    - `ID string`

      The unique ID of the model response.

  - `Type ResponseIncomplete`

    The type of the event. Always `response.incomplete`.

    - `const ResponseIncompleteResponseIncomplete ResponseIncomplete = "response.incomplete"`

  - `Object ResponseIncompleteWebhookEventObject`

    The object of the event. Always `event`.

    - `const ResponseIncompleteWebhookEventObjectEvent ResponseIncompleteWebhookEventObject = "event"`

### Unwrap Webhook Event

- `type UnwrapWebhookEventUnion interface{…}`

  Sent when a batch API request has been cancelled.

  - `type BatchCancelledWebhookEvent struct{…}`

    Sent when a batch API request has been cancelled.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the batch API request was cancelled.

    - `Data BatchCancelledWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the batch API request.

    - `Type BatchCancelled`

      The type of the event. Always `batch.cancelled`.

      - `const BatchCancelledBatchCancelled BatchCancelled = "batch.cancelled"`

    - `Object BatchCancelledWebhookEventObject`

      The object of the event. Always `event`.

      - `const BatchCancelledWebhookEventObjectEvent BatchCancelledWebhookEventObject = "event"`

  - `type BatchCompletedWebhookEvent struct{…}`

    Sent when a batch API request has been completed.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the batch API request was completed.

    - `Data BatchCompletedWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the batch API request.

    - `Type BatchCompleted`

      The type of the event. Always `batch.completed`.

      - `const BatchCompletedBatchCompleted BatchCompleted = "batch.completed"`

    - `Object BatchCompletedWebhookEventObject`

      The object of the event. Always `event`.

      - `const BatchCompletedWebhookEventObjectEvent BatchCompletedWebhookEventObject = "event"`

  - `type BatchExpiredWebhookEvent struct{…}`

    Sent when a batch API request has expired.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the batch API request expired.

    - `Data BatchExpiredWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the batch API request.

    - `Type BatchExpired`

      The type of the event. Always `batch.expired`.

      - `const BatchExpiredBatchExpired BatchExpired = "batch.expired"`

    - `Object BatchExpiredWebhookEventObject`

      The object of the event. Always `event`.

      - `const BatchExpiredWebhookEventObjectEvent BatchExpiredWebhookEventObject = "event"`

  - `type BatchFailedWebhookEvent struct{…}`

    Sent when a batch API request has failed.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the batch API request failed.

    - `Data BatchFailedWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the batch API request.

    - `Type BatchFailed`

      The type of the event. Always `batch.failed`.

      - `const BatchFailedBatchFailed BatchFailed = "batch.failed"`

    - `Object BatchFailedWebhookEventObject`

      The object of the event. Always `event`.

      - `const BatchFailedWebhookEventObjectEvent BatchFailedWebhookEventObject = "event"`

  - `type EvalRunCanceledWebhookEvent struct{…}`

    Sent when an eval run has been canceled.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the eval run was canceled.

    - `Data EvalRunCanceledWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the eval run.

    - `Type EvalRunCanceled`

      The type of the event. Always `eval.run.canceled`.

      - `const EvalRunCanceledEvalRunCanceled EvalRunCanceled = "eval.run.canceled"`

    - `Object EvalRunCanceledWebhookEventObject`

      The object of the event. Always `event`.

      - `const EvalRunCanceledWebhookEventObjectEvent EvalRunCanceledWebhookEventObject = "event"`

  - `type EvalRunFailedWebhookEvent struct{…}`

    Sent when an eval run has failed.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the eval run failed.

    - `Data EvalRunFailedWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the eval run.

    - `Type EvalRunFailed`

      The type of the event. Always `eval.run.failed`.

      - `const EvalRunFailedEvalRunFailed EvalRunFailed = "eval.run.failed"`

    - `Object EvalRunFailedWebhookEventObject`

      The object of the event. Always `event`.

      - `const EvalRunFailedWebhookEventObjectEvent EvalRunFailedWebhookEventObject = "event"`

  - `type EvalRunSucceededWebhookEvent struct{…}`

    Sent when an eval run has succeeded.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the eval run succeeded.

    - `Data EvalRunSucceededWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the eval run.

    - `Type EvalRunSucceeded`

      The type of the event. Always `eval.run.succeeded`.

      - `const EvalRunSucceededEvalRunSucceeded EvalRunSucceeded = "eval.run.succeeded"`

    - `Object EvalRunSucceededWebhookEventObject`

      The object of the event. Always `event`.

      - `const EvalRunSucceededWebhookEventObjectEvent EvalRunSucceededWebhookEventObject = "event"`

  - `type FineTuningJobCancelledWebhookEvent struct{…}`

    Sent when a fine-tuning job has been cancelled.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

    - `Data FineTuningJobCancelledWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the fine-tuning job.

    - `Type FineTuningJobCancelled`

      The type of the event. Always `fine_tuning.job.cancelled`.

      - `const FineTuningJobCancelledFineTuningJobCancelled FineTuningJobCancelled = "fine_tuning.job.cancelled"`

    - `Object FineTuningJobCancelledWebhookEventObject`

      The object of the event. Always `event`.

      - `const FineTuningJobCancelledWebhookEventObjectEvent FineTuningJobCancelledWebhookEventObject = "event"`

  - `type FineTuningJobFailedWebhookEvent struct{…}`

    Sent when a fine-tuning job has failed.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the fine-tuning job failed.

    - `Data FineTuningJobFailedWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the fine-tuning job.

    - `Type FineTuningJobFailed`

      The type of the event. Always `fine_tuning.job.failed`.

      - `const FineTuningJobFailedFineTuningJobFailed FineTuningJobFailed = "fine_tuning.job.failed"`

    - `Object FineTuningJobFailedWebhookEventObject`

      The object of the event. Always `event`.

      - `const FineTuningJobFailedWebhookEventObjectEvent FineTuningJobFailedWebhookEventObject = "event"`

  - `type FineTuningJobSucceededWebhookEvent struct{…}`

    Sent when a fine-tuning job has succeeded.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

    - `Data FineTuningJobSucceededWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the fine-tuning job.

    - `Type FineTuningJobSucceeded`

      The type of the event. Always `fine_tuning.job.succeeded`.

      - `const FineTuningJobSucceededFineTuningJobSucceeded FineTuningJobSucceeded = "fine_tuning.job.succeeded"`

    - `Object FineTuningJobSucceededWebhookEventObject`

      The object of the event. Always `event`.

      - `const FineTuningJobSucceededWebhookEventObjectEvent FineTuningJobSucceededWebhookEventObject = "event"`

  - `type RealtimeCallIncomingWebhookEvent struct{…}`

    Sent when Realtime API Receives a incoming SIP call.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the model response was completed.

    - `Data RealtimeCallIncomingWebhookEventData`

      Event data payload.

      - `CallID string`

        The unique ID of this call.

      - `SipHeaders []RealtimeCallIncomingWebhookEventDataSipHeader`

        Headers from the SIP Invite.

        - `Name string`

          Name of the SIP Header.

        - `Value string`

          Value of the SIP Header.

    - `Type RealtimeCallIncoming`

      The type of the event. Always `realtime.call.incoming`.

      - `const RealtimeCallIncomingRealtimeCallIncoming RealtimeCallIncoming = "realtime.call.incoming"`

    - `Object RealtimeCallIncomingWebhookEventObject`

      The object of the event. Always `event`.

      - `const RealtimeCallIncomingWebhookEventObjectEvent RealtimeCallIncomingWebhookEventObject = "event"`

  - `type ResponseCancelledWebhookEvent struct{…}`

    Sent when a background response has been cancelled.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the model response was cancelled.

    - `Data ResponseCancelledWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the model response.

    - `Type ResponseCancelled`

      The type of the event. Always `response.cancelled`.

      - `const ResponseCancelledResponseCancelled ResponseCancelled = "response.cancelled"`

    - `Object ResponseCancelledWebhookEventObject`

      The object of the event. Always `event`.

      - `const ResponseCancelledWebhookEventObjectEvent ResponseCancelledWebhookEventObject = "event"`

  - `type ResponseCompletedWebhookEvent struct{…}`

    Sent when a background response has been completed.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the model response was completed.

    - `Data ResponseCompletedWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the model response.

    - `Type ResponseCompleted`

      The type of the event. Always `response.completed`.

      - `const ResponseCompletedResponseCompleted ResponseCompleted = "response.completed"`

    - `Object ResponseCompletedWebhookEventObject`

      The object of the event. Always `event`.

      - `const ResponseCompletedWebhookEventObjectEvent ResponseCompletedWebhookEventObject = "event"`

  - `type ResponseFailedWebhookEvent struct{…}`

    Sent when a background response has failed.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the model response failed.

    - `Data ResponseFailedWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the model response.

    - `Type ResponseFailed`

      The type of the event. Always `response.failed`.

      - `const ResponseFailedResponseFailed ResponseFailed = "response.failed"`

    - `Object ResponseFailedWebhookEventObject`

      The object of the event. Always `event`.

      - `const ResponseFailedWebhookEventObjectEvent ResponseFailedWebhookEventObject = "event"`

  - `type ResponseIncompleteWebhookEvent struct{…}`

    Sent when a background response has been interrupted.

    - `ID string`

      The unique ID of the event.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) of when the model response was interrupted.

    - `Data ResponseIncompleteWebhookEventData`

      Event data payload.

      - `ID string`

        The unique ID of the model response.

    - `Type ResponseIncomplete`

      The type of the event. Always `response.incomplete`.

      - `const ResponseIncompleteResponseIncomplete ResponseIncomplete = "response.incomplete"`

    - `Object ResponseIncompleteWebhookEventObject`

      The object of the event. Always `event`.

      - `const ResponseIncompleteWebhookEventObjectEvent ResponseIncompleteWebhookEventObject = "event"`
