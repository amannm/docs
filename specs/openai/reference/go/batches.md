# Batches

## Create

`client.Batches.New(ctx, body) (*Batch, error)`

**post** `/batches`

Creates and executes a batch from an uploaded file of requests

### Parameters

- `body BatchNewParams`

  - `CompletionWindow param.Field[BatchNewParamsCompletionWindow]`

    The time frame within which the batch should be processed. Currently only `24h` is supported.

    - `const BatchNewParamsCompletionWindow24h BatchNewParamsCompletionWindow = "24h"`

  - `Endpoint param.Field[BatchNewParamsEndpoint]`

    The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, and `/v1/videos` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

    - `const BatchNewParamsEndpointV1Responses BatchNewParamsEndpoint = "/v1/responses"`

    - `const BatchNewParamsEndpointV1ChatCompletions BatchNewParamsEndpoint = "/v1/chat/completions"`

    - `const BatchNewParamsEndpointV1Embeddings BatchNewParamsEndpoint = "/v1/embeddings"`

    - `const BatchNewParamsEndpointV1Completions BatchNewParamsEndpoint = "/v1/completions"`

    - `const BatchNewParamsEndpointV1Moderations BatchNewParamsEndpoint = "/v1/moderations"`

    - `const BatchNewParamsEndpointV1ImagesGenerations BatchNewParamsEndpoint = "/v1/images/generations"`

    - `const BatchNewParamsEndpointV1ImagesEdits BatchNewParamsEndpoint = "/v1/images/edits"`

    - `const BatchNewParamsEndpointV1Videos BatchNewParamsEndpoint = "/v1/videos"`

  - `InputFileID param.Field[string]`

    The ID of an uploaded file that contains requests for the new batch.

    See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

    Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

  - `Metadata param.Field[Metadata]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `OutputExpiresAfter param.Field[BatchNewParamsOutputExpiresAfter]`

    The expiration policy for the output and/or error file that are generated for a batch.

    - `Anchor CreatedAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created.

      - `const CreatedAtCreatedAt CreatedAt = "created_at"`

    - `Seconds int64`

      The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `type Batch struct{…}`

  - `ID string`

  - `CompletionWindow string`

    The time frame within which the batch should be processed.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the batch was created.

  - `Endpoint string`

    The OpenAI API endpoint used by the batch.

  - `InputFileID string`

    The ID of the input file for the batch.

  - `Object Batch`

    The object type, which is always `batch`.

    - `const BatchBatch Batch = "batch"`

  - `Status BatchStatus`

    The current status of the batch.

    - `const BatchStatusValidating BatchStatus = "validating"`

    - `const BatchStatusFailed BatchStatus = "failed"`

    - `const BatchStatusInProgress BatchStatus = "in_progress"`

    - `const BatchStatusFinalizing BatchStatus = "finalizing"`

    - `const BatchStatusCompleted BatchStatus = "completed"`

    - `const BatchStatusExpired BatchStatus = "expired"`

    - `const BatchStatusCancelling BatchStatus = "cancelling"`

    - `const BatchStatusCancelled BatchStatus = "cancelled"`

  - `CancelledAt int64`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `CancellingAt int64`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `CompletedAt int64`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `ErrorFileID string`

    The ID of the file containing the outputs of requests with errors.

  - `Errors BatchErrors`

    - `Data []BatchError`

      - `Code string`

        An error code identifying the error type.

      - `Line int64`

        The line number of the input file where the error occurred, if applicable.

      - `Message string`

        A human-readable message providing more details about the error.

      - `Param string`

        The name of the parameter that caused the error, if applicable.

    - `Object string`

      The object type, which is always `list`.

  - `ExpiredAt int64`

    The Unix timestamp (in seconds) for when the batch expired.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `FailedAt int64`

    The Unix timestamp (in seconds) for when the batch failed.

  - `FinalizingAt int64`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `InProgressAt int64`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Model string`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `OutputFileID string`

    The ID of the file containing the outputs of successfully executed requests.

  - `RequestCounts BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `Completed int64`

      Number of requests that have been completed successfully.

    - `Failed int64`

      Number of requests that have failed.

    - `Total int64`

      Total number of requests in the batch.

  - `Usage BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `InputTokens int64`

      The number of input tokens.

    - `InputTokensDetails BatchUsageInputTokensDetails`

      A detailed breakdown of the input tokens.

      - `CachedTokens int64`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `OutputTokens int64`

      The number of output tokens.

    - `OutputTokensDetails BatchUsageOutputTokensDetails`

      A detailed breakdown of the output tokens.

      - `ReasoningTokens int64`

        The number of reasoning tokens.

    - `TotalTokens int64`

      The total number of tokens used.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  batch, err := client.Batches.New(context.TODO(), openai.BatchNewParams{
    CompletionWindow: openai.BatchNewParamsCompletionWindow24h,
    Endpoint: openai.BatchNewParamsEndpointV1Responses,
    InputFileID: "input_file_id",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", batch.ID)
}
```

## Retrieve

`client.Batches.Get(ctx, batchID) (*Batch, error)`

**get** `/batches/{batch_id}`

Retrieves a batch.

### Parameters

- `batchID string`

### Returns

- `type Batch struct{…}`

  - `ID string`

  - `CompletionWindow string`

    The time frame within which the batch should be processed.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the batch was created.

  - `Endpoint string`

    The OpenAI API endpoint used by the batch.

  - `InputFileID string`

    The ID of the input file for the batch.

  - `Object Batch`

    The object type, which is always `batch`.

    - `const BatchBatch Batch = "batch"`

  - `Status BatchStatus`

    The current status of the batch.

    - `const BatchStatusValidating BatchStatus = "validating"`

    - `const BatchStatusFailed BatchStatus = "failed"`

    - `const BatchStatusInProgress BatchStatus = "in_progress"`

    - `const BatchStatusFinalizing BatchStatus = "finalizing"`

    - `const BatchStatusCompleted BatchStatus = "completed"`

    - `const BatchStatusExpired BatchStatus = "expired"`

    - `const BatchStatusCancelling BatchStatus = "cancelling"`

    - `const BatchStatusCancelled BatchStatus = "cancelled"`

  - `CancelledAt int64`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `CancellingAt int64`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `CompletedAt int64`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `ErrorFileID string`

    The ID of the file containing the outputs of requests with errors.

  - `Errors BatchErrors`

    - `Data []BatchError`

      - `Code string`

        An error code identifying the error type.

      - `Line int64`

        The line number of the input file where the error occurred, if applicable.

      - `Message string`

        A human-readable message providing more details about the error.

      - `Param string`

        The name of the parameter that caused the error, if applicable.

    - `Object string`

      The object type, which is always `list`.

  - `ExpiredAt int64`

    The Unix timestamp (in seconds) for when the batch expired.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `FailedAt int64`

    The Unix timestamp (in seconds) for when the batch failed.

  - `FinalizingAt int64`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `InProgressAt int64`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Model string`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `OutputFileID string`

    The ID of the file containing the outputs of successfully executed requests.

  - `RequestCounts BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `Completed int64`

      Number of requests that have been completed successfully.

    - `Failed int64`

      Number of requests that have failed.

    - `Total int64`

      Total number of requests in the batch.

  - `Usage BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `InputTokens int64`

      The number of input tokens.

    - `InputTokensDetails BatchUsageInputTokensDetails`

      A detailed breakdown of the input tokens.

      - `CachedTokens int64`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `OutputTokens int64`

      The number of output tokens.

    - `OutputTokensDetails BatchUsageOutputTokensDetails`

      A detailed breakdown of the output tokens.

      - `ReasoningTokens int64`

        The number of reasoning tokens.

    - `TotalTokens int64`

      The total number of tokens used.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  batch, err := client.Batches.Get(context.TODO(), "batch_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", batch.ID)
}
```

## Cancel

`client.Batches.Cancel(ctx, batchID) (*Batch, error)`

**post** `/batches/{batch_id}/cancel`

Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.

### Parameters

- `batchID string`

### Returns

- `type Batch struct{…}`

  - `ID string`

  - `CompletionWindow string`

    The time frame within which the batch should be processed.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the batch was created.

  - `Endpoint string`

    The OpenAI API endpoint used by the batch.

  - `InputFileID string`

    The ID of the input file for the batch.

  - `Object Batch`

    The object type, which is always `batch`.

    - `const BatchBatch Batch = "batch"`

  - `Status BatchStatus`

    The current status of the batch.

    - `const BatchStatusValidating BatchStatus = "validating"`

    - `const BatchStatusFailed BatchStatus = "failed"`

    - `const BatchStatusInProgress BatchStatus = "in_progress"`

    - `const BatchStatusFinalizing BatchStatus = "finalizing"`

    - `const BatchStatusCompleted BatchStatus = "completed"`

    - `const BatchStatusExpired BatchStatus = "expired"`

    - `const BatchStatusCancelling BatchStatus = "cancelling"`

    - `const BatchStatusCancelled BatchStatus = "cancelled"`

  - `CancelledAt int64`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `CancellingAt int64`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `CompletedAt int64`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `ErrorFileID string`

    The ID of the file containing the outputs of requests with errors.

  - `Errors BatchErrors`

    - `Data []BatchError`

      - `Code string`

        An error code identifying the error type.

      - `Line int64`

        The line number of the input file where the error occurred, if applicable.

      - `Message string`

        A human-readable message providing more details about the error.

      - `Param string`

        The name of the parameter that caused the error, if applicable.

    - `Object string`

      The object type, which is always `list`.

  - `ExpiredAt int64`

    The Unix timestamp (in seconds) for when the batch expired.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `FailedAt int64`

    The Unix timestamp (in seconds) for when the batch failed.

  - `FinalizingAt int64`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `InProgressAt int64`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Model string`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `OutputFileID string`

    The ID of the file containing the outputs of successfully executed requests.

  - `RequestCounts BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `Completed int64`

      Number of requests that have been completed successfully.

    - `Failed int64`

      Number of requests that have failed.

    - `Total int64`

      Total number of requests in the batch.

  - `Usage BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `InputTokens int64`

      The number of input tokens.

    - `InputTokensDetails BatchUsageInputTokensDetails`

      A detailed breakdown of the input tokens.

      - `CachedTokens int64`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `OutputTokens int64`

      The number of output tokens.

    - `OutputTokensDetails BatchUsageOutputTokensDetails`

      A detailed breakdown of the output tokens.

      - `ReasoningTokens int64`

        The number of reasoning tokens.

    - `TotalTokens int64`

      The total number of tokens used.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  batch, err := client.Batches.Cancel(context.TODO(), "batch_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", batch.ID)
}
```

## List

`client.Batches.List(ctx, query) (*CursorPage[Batch], error)`

**get** `/batches`

List your organization's batches.

### Parameters

- `query BatchListParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

### Returns

- `type Batch struct{…}`

  - `ID string`

  - `CompletionWindow string`

    The time frame within which the batch should be processed.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the batch was created.

  - `Endpoint string`

    The OpenAI API endpoint used by the batch.

  - `InputFileID string`

    The ID of the input file for the batch.

  - `Object Batch`

    The object type, which is always `batch`.

    - `const BatchBatch Batch = "batch"`

  - `Status BatchStatus`

    The current status of the batch.

    - `const BatchStatusValidating BatchStatus = "validating"`

    - `const BatchStatusFailed BatchStatus = "failed"`

    - `const BatchStatusInProgress BatchStatus = "in_progress"`

    - `const BatchStatusFinalizing BatchStatus = "finalizing"`

    - `const BatchStatusCompleted BatchStatus = "completed"`

    - `const BatchStatusExpired BatchStatus = "expired"`

    - `const BatchStatusCancelling BatchStatus = "cancelling"`

    - `const BatchStatusCancelled BatchStatus = "cancelled"`

  - `CancelledAt int64`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `CancellingAt int64`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `CompletedAt int64`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `ErrorFileID string`

    The ID of the file containing the outputs of requests with errors.

  - `Errors BatchErrors`

    - `Data []BatchError`

      - `Code string`

        An error code identifying the error type.

      - `Line int64`

        The line number of the input file where the error occurred, if applicable.

      - `Message string`

        A human-readable message providing more details about the error.

      - `Param string`

        The name of the parameter that caused the error, if applicable.

    - `Object string`

      The object type, which is always `list`.

  - `ExpiredAt int64`

    The Unix timestamp (in seconds) for when the batch expired.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `FailedAt int64`

    The Unix timestamp (in seconds) for when the batch failed.

  - `FinalizingAt int64`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `InProgressAt int64`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Model string`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `OutputFileID string`

    The ID of the file containing the outputs of successfully executed requests.

  - `RequestCounts BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `Completed int64`

      Number of requests that have been completed successfully.

    - `Failed int64`

      Number of requests that have failed.

    - `Total int64`

      Total number of requests in the batch.

  - `Usage BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `InputTokens int64`

      The number of input tokens.

    - `InputTokensDetails BatchUsageInputTokensDetails`

      A detailed breakdown of the input tokens.

      - `CachedTokens int64`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `OutputTokens int64`

      The number of output tokens.

    - `OutputTokensDetails BatchUsageOutputTokensDetails`

      A detailed breakdown of the output tokens.

      - `ReasoningTokens int64`

        The number of reasoning tokens.

    - `TotalTokens int64`

      The total number of tokens used.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Batches.List(context.TODO(), openai.BatchListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Domain Types

### Batch

- `type Batch struct{…}`

  - `ID string`

  - `CompletionWindow string`

    The time frame within which the batch should be processed.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the batch was created.

  - `Endpoint string`

    The OpenAI API endpoint used by the batch.

  - `InputFileID string`

    The ID of the input file for the batch.

  - `Object Batch`

    The object type, which is always `batch`.

    - `const BatchBatch Batch = "batch"`

  - `Status BatchStatus`

    The current status of the batch.

    - `const BatchStatusValidating BatchStatus = "validating"`

    - `const BatchStatusFailed BatchStatus = "failed"`

    - `const BatchStatusInProgress BatchStatus = "in_progress"`

    - `const BatchStatusFinalizing BatchStatus = "finalizing"`

    - `const BatchStatusCompleted BatchStatus = "completed"`

    - `const BatchStatusExpired BatchStatus = "expired"`

    - `const BatchStatusCancelling BatchStatus = "cancelling"`

    - `const BatchStatusCancelled BatchStatus = "cancelled"`

  - `CancelledAt int64`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `CancellingAt int64`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `CompletedAt int64`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `ErrorFileID string`

    The ID of the file containing the outputs of requests with errors.

  - `Errors BatchErrors`

    - `Data []BatchError`

      - `Code string`

        An error code identifying the error type.

      - `Line int64`

        The line number of the input file where the error occurred, if applicable.

      - `Message string`

        A human-readable message providing more details about the error.

      - `Param string`

        The name of the parameter that caused the error, if applicable.

    - `Object string`

      The object type, which is always `list`.

  - `ExpiredAt int64`

    The Unix timestamp (in seconds) for when the batch expired.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `FailedAt int64`

    The Unix timestamp (in seconds) for when the batch failed.

  - `FinalizingAt int64`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `InProgressAt int64`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Model string`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `OutputFileID string`

    The ID of the file containing the outputs of successfully executed requests.

  - `RequestCounts BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `Completed int64`

      Number of requests that have been completed successfully.

    - `Failed int64`

      Number of requests that have failed.

    - `Total int64`

      Total number of requests in the batch.

  - `Usage BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `InputTokens int64`

      The number of input tokens.

    - `InputTokensDetails BatchUsageInputTokensDetails`

      A detailed breakdown of the input tokens.

      - `CachedTokens int64`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `OutputTokens int64`

      The number of output tokens.

    - `OutputTokensDetails BatchUsageOutputTokensDetails`

      A detailed breakdown of the output tokens.

      - `ReasoningTokens int64`

        The number of reasoning tokens.

    - `TotalTokens int64`

      The total number of tokens used.

### Batch Error

- `type BatchError struct{…}`

  - `Code string`

    An error code identifying the error type.

  - `Line int64`

    The line number of the input file where the error occurred, if applicable.

  - `Message string`

    A human-readable message providing more details about the error.

  - `Param string`

    The name of the parameter that caused the error, if applicable.

### Batch Request Counts

- `type BatchRequestCounts struct{…}`

  The request counts for different statuses within the batch.

  - `Completed int64`

    Number of requests that have been completed successfully.

  - `Failed int64`

    Number of requests that have failed.

  - `Total int64`

    Total number of requests in the batch.

### Batch Usage

- `type BatchUsage struct{…}`

  Represents token usage details including input tokens, output tokens, a
  breakdown of output tokens, and the total tokens used. Only populated on
  batches created after September 7, 2025.

  - `InputTokens int64`

    The number of input tokens.

  - `InputTokensDetails BatchUsageInputTokensDetails`

    A detailed breakdown of the input tokens.

    - `CachedTokens int64`

      The number of tokens that were retrieved from the cache. [More on
      prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

  - `OutputTokens int64`

    The number of output tokens.

  - `OutputTokensDetails BatchUsageOutputTokensDetails`

    A detailed breakdown of the output tokens.

    - `ReasoningTokens int64`

      The number of reasoning tokens.

  - `TotalTokens int64`

    The total number of tokens used.
