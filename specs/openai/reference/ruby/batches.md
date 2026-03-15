# Batches

## Create

`batches.create(**kwargs) -> Batch`

**post** `/batches`

Creates and executes a batch from an uploaded file of requests

### Parameters

- `completion_window: :"24h"`

  The time frame within which the batch should be processed. Currently only `24h` is supported.

  - `:"24h"`

- `endpoint: :"/v1/responses" | :"/v1/chat/completions" | :"/v1/embeddings" | 5 more`

  The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, and `/v1/videos` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

  - `:"/v1/responses"`

  - `:"/v1/chat/completions"`

  - `:"/v1/embeddings"`

  - `:"/v1/completions"`

  - `:"/v1/moderations"`

  - `:"/v1/images/generations"`

  - `:"/v1/images/edits"`

  - `:"/v1/videos"`

- `input_file_id: String`

  The ID of an uploaded file that contains requests for the new batch.

  See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

  Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `output_expires_after: { anchor, seconds}`

  The expiration policy for the output and/or error file that are generated for a batch.

  - `anchor: :created_at`

    Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created.

    - `:created_at`

  - `seconds: Integer`

    The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `class Batch`

  - `id: String`

  - `completion_window: String`

    The time frame within which the batch should be processed.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the batch was created.

  - `endpoint: String`

    The OpenAI API endpoint used by the batch.

  - `input_file_id: String`

    The ID of the input file for the batch.

  - `object: :batch`

    The object type, which is always `batch`.

    - `:batch`

  - `status: :validating | :failed | :in_progress | 5 more`

    The current status of the batch.

    - `:validating`

    - `:failed`

    - `:in_progress`

    - `:finalizing`

    - `:completed`

    - `:expired`

    - `:cancelling`

    - `:cancelled`

  - `cancelled_at: Integer`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `cancelling_at: Integer`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `completed_at: Integer`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `error_file_id: String`

    The ID of the file containing the outputs of requests with errors.

  - `errors: { data, object}`

    - `data: Array[BatchError]`

      - `code: String`

        An error code identifying the error type.

      - `line: Integer`

        The line number of the input file where the error occurred, if applicable.

      - `message: String`

        A human-readable message providing more details about the error.

      - `param: String`

        The name of the parameter that caused the error, if applicable.

    - `object: String`

      The object type, which is always `list`.

  - `expired_at: Integer`

    The Unix timestamp (in seconds) for when the batch expired.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `failed_at: Integer`

    The Unix timestamp (in seconds) for when the batch failed.

  - `finalizing_at: Integer`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `in_progress_at: Integer`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `output_file_id: String`

    The ID of the file containing the outputs of successfully executed requests.

  - `request_counts: BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `completed: Integer`

      Number of requests that have been completed successfully.

    - `failed: Integer`

      Number of requests that have failed.

    - `total: Integer`

      Total number of requests in the batch.

  - `usage: BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `input_tokens: Integer`

      The number of input tokens.

    - `input_tokens_details: { cached_tokens}`

      A detailed breakdown of the input tokens.

      - `cached_tokens: Integer`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `output_tokens: Integer`

      The number of output tokens.

    - `output_tokens_details: { reasoning_tokens}`

      A detailed breakdown of the output tokens.

      - `reasoning_tokens: Integer`

        The number of reasoning tokens.

    - `total_tokens: Integer`

      The total number of tokens used.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

batch = openai.batches.create(
  completion_window: :"24h",
  endpoint: :"/v1/responses",
  input_file_id: "input_file_id"
)

puts(batch)
```

## Retrieve

`batches.retrieve(batch_id) -> Batch`

**get** `/batches/{batch_id}`

Retrieves a batch.

### Parameters

- `batch_id: String`

### Returns

- `class Batch`

  - `id: String`

  - `completion_window: String`

    The time frame within which the batch should be processed.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the batch was created.

  - `endpoint: String`

    The OpenAI API endpoint used by the batch.

  - `input_file_id: String`

    The ID of the input file for the batch.

  - `object: :batch`

    The object type, which is always `batch`.

    - `:batch`

  - `status: :validating | :failed | :in_progress | 5 more`

    The current status of the batch.

    - `:validating`

    - `:failed`

    - `:in_progress`

    - `:finalizing`

    - `:completed`

    - `:expired`

    - `:cancelling`

    - `:cancelled`

  - `cancelled_at: Integer`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `cancelling_at: Integer`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `completed_at: Integer`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `error_file_id: String`

    The ID of the file containing the outputs of requests with errors.

  - `errors: { data, object}`

    - `data: Array[BatchError]`

      - `code: String`

        An error code identifying the error type.

      - `line: Integer`

        The line number of the input file where the error occurred, if applicable.

      - `message: String`

        A human-readable message providing more details about the error.

      - `param: String`

        The name of the parameter that caused the error, if applicable.

    - `object: String`

      The object type, which is always `list`.

  - `expired_at: Integer`

    The Unix timestamp (in seconds) for when the batch expired.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `failed_at: Integer`

    The Unix timestamp (in seconds) for when the batch failed.

  - `finalizing_at: Integer`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `in_progress_at: Integer`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `output_file_id: String`

    The ID of the file containing the outputs of successfully executed requests.

  - `request_counts: BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `completed: Integer`

      Number of requests that have been completed successfully.

    - `failed: Integer`

      Number of requests that have failed.

    - `total: Integer`

      Total number of requests in the batch.

  - `usage: BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `input_tokens: Integer`

      The number of input tokens.

    - `input_tokens_details: { cached_tokens}`

      A detailed breakdown of the input tokens.

      - `cached_tokens: Integer`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `output_tokens: Integer`

      The number of output tokens.

    - `output_tokens_details: { reasoning_tokens}`

      A detailed breakdown of the output tokens.

      - `reasoning_tokens: Integer`

        The number of reasoning tokens.

    - `total_tokens: Integer`

      The total number of tokens used.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

batch = openai.batches.retrieve("batch_id")

puts(batch)
```

## Cancel

`batches.cancel(batch_id) -> Batch`

**post** `/batches/{batch_id}/cancel`

Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.

### Parameters

- `batch_id: String`

### Returns

- `class Batch`

  - `id: String`

  - `completion_window: String`

    The time frame within which the batch should be processed.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the batch was created.

  - `endpoint: String`

    The OpenAI API endpoint used by the batch.

  - `input_file_id: String`

    The ID of the input file for the batch.

  - `object: :batch`

    The object type, which is always `batch`.

    - `:batch`

  - `status: :validating | :failed | :in_progress | 5 more`

    The current status of the batch.

    - `:validating`

    - `:failed`

    - `:in_progress`

    - `:finalizing`

    - `:completed`

    - `:expired`

    - `:cancelling`

    - `:cancelled`

  - `cancelled_at: Integer`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `cancelling_at: Integer`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `completed_at: Integer`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `error_file_id: String`

    The ID of the file containing the outputs of requests with errors.

  - `errors: { data, object}`

    - `data: Array[BatchError]`

      - `code: String`

        An error code identifying the error type.

      - `line: Integer`

        The line number of the input file where the error occurred, if applicable.

      - `message: String`

        A human-readable message providing more details about the error.

      - `param: String`

        The name of the parameter that caused the error, if applicable.

    - `object: String`

      The object type, which is always `list`.

  - `expired_at: Integer`

    The Unix timestamp (in seconds) for when the batch expired.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `failed_at: Integer`

    The Unix timestamp (in seconds) for when the batch failed.

  - `finalizing_at: Integer`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `in_progress_at: Integer`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `output_file_id: String`

    The ID of the file containing the outputs of successfully executed requests.

  - `request_counts: BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `completed: Integer`

      Number of requests that have been completed successfully.

    - `failed: Integer`

      Number of requests that have failed.

    - `total: Integer`

      Total number of requests in the batch.

  - `usage: BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `input_tokens: Integer`

      The number of input tokens.

    - `input_tokens_details: { cached_tokens}`

      A detailed breakdown of the input tokens.

      - `cached_tokens: Integer`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `output_tokens: Integer`

      The number of output tokens.

    - `output_tokens_details: { reasoning_tokens}`

      A detailed breakdown of the output tokens.

      - `reasoning_tokens: Integer`

        The number of reasoning tokens.

    - `total_tokens: Integer`

      The total number of tokens used.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

batch = openai.batches.cancel("batch_id")

puts(batch)
```

## List

`batches.list(**kwargs) -> CursorPage<Batch>`

**get** `/batches`

List your organization's batches.

### Parameters

- `after: String`

  A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- `limit: Integer`

  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

### Returns

- `class Batch`

  - `id: String`

  - `completion_window: String`

    The time frame within which the batch should be processed.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the batch was created.

  - `endpoint: String`

    The OpenAI API endpoint used by the batch.

  - `input_file_id: String`

    The ID of the input file for the batch.

  - `object: :batch`

    The object type, which is always `batch`.

    - `:batch`

  - `status: :validating | :failed | :in_progress | 5 more`

    The current status of the batch.

    - `:validating`

    - `:failed`

    - `:in_progress`

    - `:finalizing`

    - `:completed`

    - `:expired`

    - `:cancelling`

    - `:cancelled`

  - `cancelled_at: Integer`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `cancelling_at: Integer`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `completed_at: Integer`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `error_file_id: String`

    The ID of the file containing the outputs of requests with errors.

  - `errors: { data, object}`

    - `data: Array[BatchError]`

      - `code: String`

        An error code identifying the error type.

      - `line: Integer`

        The line number of the input file where the error occurred, if applicable.

      - `message: String`

        A human-readable message providing more details about the error.

      - `param: String`

        The name of the parameter that caused the error, if applicable.

    - `object: String`

      The object type, which is always `list`.

  - `expired_at: Integer`

    The Unix timestamp (in seconds) for when the batch expired.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `failed_at: Integer`

    The Unix timestamp (in seconds) for when the batch failed.

  - `finalizing_at: Integer`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `in_progress_at: Integer`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `output_file_id: String`

    The ID of the file containing the outputs of successfully executed requests.

  - `request_counts: BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `completed: Integer`

      Number of requests that have been completed successfully.

    - `failed: Integer`

      Number of requests that have failed.

    - `total: Integer`

      Total number of requests in the batch.

  - `usage: BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `input_tokens: Integer`

      The number of input tokens.

    - `input_tokens_details: { cached_tokens}`

      A detailed breakdown of the input tokens.

      - `cached_tokens: Integer`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `output_tokens: Integer`

      The number of output tokens.

    - `output_tokens_details: { reasoning_tokens}`

      A detailed breakdown of the output tokens.

      - `reasoning_tokens: Integer`

        The number of reasoning tokens.

    - `total_tokens: Integer`

      The total number of tokens used.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.batches.list

puts(page)
```

### Domain Types

### Batch

- `class Batch`

  - `id: String`

  - `completion_window: String`

    The time frame within which the batch should be processed.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the batch was created.

  - `endpoint: String`

    The OpenAI API endpoint used by the batch.

  - `input_file_id: String`

    The ID of the input file for the batch.

  - `object: :batch`

    The object type, which is always `batch`.

    - `:batch`

  - `status: :validating | :failed | :in_progress | 5 more`

    The current status of the batch.

    - `:validating`

    - `:failed`

    - `:in_progress`

    - `:finalizing`

    - `:completed`

    - `:expired`

    - `:cancelling`

    - `:cancelled`

  - `cancelled_at: Integer`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `cancelling_at: Integer`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `completed_at: Integer`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `error_file_id: String`

    The ID of the file containing the outputs of requests with errors.

  - `errors: { data, object}`

    - `data: Array[BatchError]`

      - `code: String`

        An error code identifying the error type.

      - `line: Integer`

        The line number of the input file where the error occurred, if applicable.

      - `message: String`

        A human-readable message providing more details about the error.

      - `param: String`

        The name of the parameter that caused the error, if applicable.

    - `object: String`

      The object type, which is always `list`.

  - `expired_at: Integer`

    The Unix timestamp (in seconds) for when the batch expired.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `failed_at: Integer`

    The Unix timestamp (in seconds) for when the batch failed.

  - `finalizing_at: Integer`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `in_progress_at: Integer`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `output_file_id: String`

    The ID of the file containing the outputs of successfully executed requests.

  - `request_counts: BatchRequestCounts`

    The request counts for different statuses within the batch.

    - `completed: Integer`

      Number of requests that have been completed successfully.

    - `failed: Integer`

      Number of requests that have failed.

    - `total: Integer`

      Total number of requests in the batch.

  - `usage: BatchUsage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `input_tokens: Integer`

      The number of input tokens.

    - `input_tokens_details: { cached_tokens}`

      A detailed breakdown of the input tokens.

      - `cached_tokens: Integer`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `output_tokens: Integer`

      The number of output tokens.

    - `output_tokens_details: { reasoning_tokens}`

      A detailed breakdown of the output tokens.

      - `reasoning_tokens: Integer`

        The number of reasoning tokens.

    - `total_tokens: Integer`

      The total number of tokens used.

### Batch Error

- `class BatchError`

  - `code: String`

    An error code identifying the error type.

  - `line: Integer`

    The line number of the input file where the error occurred, if applicable.

  - `message: String`

    A human-readable message providing more details about the error.

  - `param: String`

    The name of the parameter that caused the error, if applicable.

### Batch Request Counts

- `class BatchRequestCounts`

  The request counts for different statuses within the batch.

  - `completed: Integer`

    Number of requests that have been completed successfully.

  - `failed: Integer`

    Number of requests that have failed.

  - `total: Integer`

    Total number of requests in the batch.

### Batch Usage

- `class BatchUsage`

  Represents token usage details including input tokens, output tokens, a
  breakdown of output tokens, and the total tokens used. Only populated on
  batches created after September 7, 2025.

  - `input_tokens: Integer`

    The number of input tokens.

  - `input_tokens_details: { cached_tokens}`

    A detailed breakdown of the input tokens.

    - `cached_tokens: Integer`

      The number of tokens that were retrieved from the cache. [More on
      prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

  - `output_tokens: Integer`

    The number of output tokens.

  - `output_tokens_details: { reasoning_tokens}`

    A detailed breakdown of the output tokens.

    - `reasoning_tokens: Integer`

      The number of reasoning tokens.

  - `total_tokens: Integer`

    The total number of tokens used.
