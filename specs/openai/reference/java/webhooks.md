# Webhooks

## Domain Types

### Batch Cancelled Webhook Event

- `class BatchCancelledWebhookEvent:`

  Sent when a batch API request has been cancelled.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the batch API request was cancelled.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the batch API request.

  - `JsonValue; type "batch.cancelled"constant`

    The type of the event. Always `batch.cancelled`.

    - `BATCH_CANCELLED("batch.cancelled")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Batch Completed Webhook Event

- `class BatchCompletedWebhookEvent:`

  Sent when a batch API request has been completed.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the batch API request was completed.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the batch API request.

  - `JsonValue; type "batch.completed"constant`

    The type of the event. Always `batch.completed`.

    - `BATCH_COMPLETED("batch.completed")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Batch Expired Webhook Event

- `class BatchExpiredWebhookEvent:`

  Sent when a batch API request has expired.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the batch API request expired.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the batch API request.

  - `JsonValue; type "batch.expired"constant`

    The type of the event. Always `batch.expired`.

    - `BATCH_EXPIRED("batch.expired")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Batch Failed Webhook Event

- `class BatchFailedWebhookEvent:`

  Sent when a batch API request has failed.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the batch API request failed.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the batch API request.

  - `JsonValue; type "batch.failed"constant`

    The type of the event. Always `batch.failed`.

    - `BATCH_FAILED("batch.failed")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Eval Run Canceled Webhook Event

- `class EvalRunCanceledWebhookEvent:`

  Sent when an eval run has been canceled.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the eval run was canceled.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the eval run.

  - `JsonValue; type "eval.run.canceled"constant`

    The type of the event. Always `eval.run.canceled`.

    - `EVAL_RUN_CANCELED("eval.run.canceled")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Eval Run Failed Webhook Event

- `class EvalRunFailedWebhookEvent:`

  Sent when an eval run has failed.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the eval run failed.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the eval run.

  - `JsonValue; type "eval.run.failed"constant`

    The type of the event. Always `eval.run.failed`.

    - `EVAL_RUN_FAILED("eval.run.failed")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Eval Run Succeeded Webhook Event

- `class EvalRunSucceededWebhookEvent:`

  Sent when an eval run has succeeded.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the eval run succeeded.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the eval run.

  - `JsonValue; type "eval.run.succeeded"constant`

    The type of the event. Always `eval.run.succeeded`.

    - `EVAL_RUN_SUCCEEDED("eval.run.succeeded")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Fine Tuning Job Cancelled Webhook Event

- `class FineTuningJobCancelledWebhookEvent:`

  Sent when a fine-tuning job has been cancelled.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the fine-tuning job.

  - `JsonValue; type "fine_tuning.job.cancelled"constant`

    The type of the event. Always `fine_tuning.job.cancelled`.

    - `FINE_TUNING_JOB_CANCELLED("fine_tuning.job.cancelled")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Fine Tuning Job Failed Webhook Event

- `class FineTuningJobFailedWebhookEvent:`

  Sent when a fine-tuning job has failed.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the fine-tuning job failed.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the fine-tuning job.

  - `JsonValue; type "fine_tuning.job.failed"constant`

    The type of the event. Always `fine_tuning.job.failed`.

    - `FINE_TUNING_JOB_FAILED("fine_tuning.job.failed")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Fine Tuning Job Succeeded Webhook Event

- `class FineTuningJobSucceededWebhookEvent:`

  Sent when a fine-tuning job has succeeded.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the fine-tuning job.

  - `JsonValue; type "fine_tuning.job.succeeded"constant`

    The type of the event. Always `fine_tuning.job.succeeded`.

    - `FINE_TUNING_JOB_SUCCEEDED("fine_tuning.job.succeeded")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Realtime Call Incoming Webhook Event

- `class RealtimeCallIncomingWebhookEvent:`

  Sent when Realtime API Receives a incoming SIP call.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the model response was completed.

  - `Data data`

    Event data payload.

    - `String callId`

      The unique ID of this call.

    - `List<SipHeader> sipHeaders`

      Headers from the SIP Invite.

      - `String name`

        Name of the SIP Header.

      - `String value`

        Value of the SIP Header.

  - `JsonValue; type "realtime.call.incoming"constant`

    The type of the event. Always `realtime.call.incoming`.

    - `REALTIME_CALL_INCOMING("realtime.call.incoming")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Response Cancelled Webhook Event

- `class ResponseCancelledWebhookEvent:`

  Sent when a background response has been cancelled.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the model response was cancelled.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the model response.

  - `JsonValue; type "response.cancelled"constant`

    The type of the event. Always `response.cancelled`.

    - `RESPONSE_CANCELLED("response.cancelled")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Response Completed Webhook Event

- `class ResponseCompletedWebhookEvent:`

  Sent when a background response has been completed.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the model response was completed.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the model response.

  - `JsonValue; type "response.completed"constant`

    The type of the event. Always `response.completed`.

    - `RESPONSE_COMPLETED("response.completed")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Response Failed Webhook Event

- `class ResponseFailedWebhookEvent:`

  Sent when a background response has failed.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the model response failed.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the model response.

  - `JsonValue; type "response.failed"constant`

    The type of the event. Always `response.failed`.

    - `RESPONSE_FAILED("response.failed")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Response Incomplete Webhook Event

- `class ResponseIncompleteWebhookEvent:`

  Sent when a background response has been interrupted.

  - `String id`

    The unique ID of the event.

  - `long createdAt`

    The Unix timestamp (in seconds) of when the model response was interrupted.

  - `Data data`

    Event data payload.

    - `String id`

      The unique ID of the model response.

  - `JsonValue; type "response.incomplete"constant`

    The type of the event. Always `response.incomplete`.

    - `RESPONSE_INCOMPLETE("response.incomplete")`

  - `Optional<Object> object_`

    The object of the event. Always `event`.

    - `EVENT("event")`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent: A class that can be one of several variants.union`

  Sent when a batch API request has been cancelled.

  - `class BatchCancelledWebhookEvent:`

    Sent when a batch API request has been cancelled.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the batch API request was cancelled.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the batch API request.

    - `JsonValue; type "batch.cancelled"constant`

      The type of the event. Always `batch.cancelled`.

      - `BATCH_CANCELLED("batch.cancelled")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class BatchCompletedWebhookEvent:`

    Sent when a batch API request has been completed.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the batch API request was completed.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the batch API request.

    - `JsonValue; type "batch.completed"constant`

      The type of the event. Always `batch.completed`.

      - `BATCH_COMPLETED("batch.completed")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class BatchExpiredWebhookEvent:`

    Sent when a batch API request has expired.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the batch API request expired.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the batch API request.

    - `JsonValue; type "batch.expired"constant`

      The type of the event. Always `batch.expired`.

      - `BATCH_EXPIRED("batch.expired")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class BatchFailedWebhookEvent:`

    Sent when a batch API request has failed.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the batch API request failed.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the batch API request.

    - `JsonValue; type "batch.failed"constant`

      The type of the event. Always `batch.failed`.

      - `BATCH_FAILED("batch.failed")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class EvalRunCanceledWebhookEvent:`

    Sent when an eval run has been canceled.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the eval run was canceled.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the eval run.

    - `JsonValue; type "eval.run.canceled"constant`

      The type of the event. Always `eval.run.canceled`.

      - `EVAL_RUN_CANCELED("eval.run.canceled")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class EvalRunFailedWebhookEvent:`

    Sent when an eval run has failed.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the eval run failed.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the eval run.

    - `JsonValue; type "eval.run.failed"constant`

      The type of the event. Always `eval.run.failed`.

      - `EVAL_RUN_FAILED("eval.run.failed")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class EvalRunSucceededWebhookEvent:`

    Sent when an eval run has succeeded.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the eval run succeeded.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the eval run.

    - `JsonValue; type "eval.run.succeeded"constant`

      The type of the event. Always `eval.run.succeeded`.

      - `EVAL_RUN_SUCCEEDED("eval.run.succeeded")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class FineTuningJobCancelledWebhookEvent:`

    Sent when a fine-tuning job has been cancelled.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the fine-tuning job.

    - `JsonValue; type "fine_tuning.job.cancelled"constant`

      The type of the event. Always `fine_tuning.job.cancelled`.

      - `FINE_TUNING_JOB_CANCELLED("fine_tuning.job.cancelled")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class FineTuningJobFailedWebhookEvent:`

    Sent when a fine-tuning job has failed.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the fine-tuning job failed.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the fine-tuning job.

    - `JsonValue; type "fine_tuning.job.failed"constant`

      The type of the event. Always `fine_tuning.job.failed`.

      - `FINE_TUNING_JOB_FAILED("fine_tuning.job.failed")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class FineTuningJobSucceededWebhookEvent:`

    Sent when a fine-tuning job has succeeded.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the fine-tuning job.

    - `JsonValue; type "fine_tuning.job.succeeded"constant`

      The type of the event. Always `fine_tuning.job.succeeded`.

      - `FINE_TUNING_JOB_SUCCEEDED("fine_tuning.job.succeeded")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class RealtimeCallIncomingWebhookEvent:`

    Sent when Realtime API Receives a incoming SIP call.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the model response was completed.

    - `Data data`

      Event data payload.

      - `String callId`

        The unique ID of this call.

      - `List<SipHeader> sipHeaders`

        Headers from the SIP Invite.

        - `String name`

          Name of the SIP Header.

        - `String value`

          Value of the SIP Header.

    - `JsonValue; type "realtime.call.incoming"constant`

      The type of the event. Always `realtime.call.incoming`.

      - `REALTIME_CALL_INCOMING("realtime.call.incoming")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class ResponseCancelledWebhookEvent:`

    Sent when a background response has been cancelled.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the model response was cancelled.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the model response.

    - `JsonValue; type "response.cancelled"constant`

      The type of the event. Always `response.cancelled`.

      - `RESPONSE_CANCELLED("response.cancelled")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class ResponseCompletedWebhookEvent:`

    Sent when a background response has been completed.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the model response was completed.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the model response.

    - `JsonValue; type "response.completed"constant`

      The type of the event. Always `response.completed`.

      - `RESPONSE_COMPLETED("response.completed")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class ResponseFailedWebhookEvent:`

    Sent when a background response has failed.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the model response failed.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the model response.

    - `JsonValue; type "response.failed"constant`

      The type of the event. Always `response.failed`.

      - `RESPONSE_FAILED("response.failed")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`

  - `class ResponseIncompleteWebhookEvent:`

    Sent when a background response has been interrupted.

    - `String id`

      The unique ID of the event.

    - `long createdAt`

      The Unix timestamp (in seconds) of when the model response was interrupted.

    - `Data data`

      Event data payload.

      - `String id`

        The unique ID of the model response.

    - `JsonValue; type "response.incomplete"constant`

      The type of the event. Always `response.incomplete`.

      - `RESPONSE_INCOMPLETE("response.incomplete")`

    - `Optional<Object> object_`

      The object of the event. Always `event`.

      - `EVENT("event")`
