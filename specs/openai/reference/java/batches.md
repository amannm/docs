# Batches

## Create

`Batch batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/batches`

Creates and executes a batch from an uploaded file of requests

### Parameters

- `BatchCreateParams params`

  - `CompletionWindow completionWindow`

    The time frame within which the batch should be processed. Currently only `24h` is supported.

    - `_24H("24h")`

  - `Endpoint endpoint`

    The endpoint to be used for all requests in the batch. Currently `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, and `/v1/videos` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

    - `V1_RESPONSES("/v1/responses")`

    - `V1_CHAT_COMPLETIONS("/v1/chat/completions")`

    - `V1_EMBEDDINGS("/v1/embeddings")`

    - `V1_COMPLETIONS("/v1/completions")`

    - `V1_MODERATIONS("/v1/moderations")`

    - `V1_IMAGES_GENERATIONS("/v1/images/generations")`

    - `V1_IMAGES_EDITS("/v1/images/edits")`

    - `V1_VIDEOS("/v1/videos")`

  - `String inputFileId`

    The ID of an uploaded file that contains requests for the new batch.

    See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

    Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 200 MB in size.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<OutputExpiresAfter> outputExpiresAfter`

    The expiration policy for the output and/or error file that are generated for a batch.

    - `JsonValue; anchor "created_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`. Note that the anchor is the file creation time, not the time the batch is created.

      - `CREATED_AT("created_at")`

    - `long seconds`

      The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `class Batch:`

  - `String id`

  - `String completionWindow`

    The time frame within which the batch should be processed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the batch was created.

  - `String endpoint`

    The OpenAI API endpoint used by the batch.

  - `String inputFileId`

    The ID of the input file for the batch.

  - `JsonValue; object_ "batch"constant`

    The object type, which is always `batch`.

    - `BATCH("batch")`

  - `Status status`

    The current status of the batch.

    - `VALIDATING("validating")`

    - `FAILED("failed")`

    - `IN_PROGRESS("in_progress")`

    - `FINALIZING("finalizing")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `Optional<Long> cancellingAt`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `Optional<String> errorFileId`

    The ID of the file containing the outputs of requests with errors.

  - `Optional<Errors> errors`

    - `Optional<List<BatchError>> data`

      - `Optional<String> code`

        An error code identifying the error type.

      - `Optional<Long> line`

        The line number of the input file where the error occurred, if applicable.

      - `Optional<String> message`

        A human-readable message providing more details about the error.

      - `Optional<String> param`

        The name of the parameter that caused the error, if applicable.

    - `Optional<String> object_`

      The object type, which is always `list`.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the batch expired.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the batch failed.

  - `Optional<Long> finalizingAt`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `Optional<Long> inProgressAt`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> model`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `Optional<String> outputFileId`

    The ID of the file containing the outputs of successfully executed requests.

  - `Optional<BatchRequestCounts> requestCounts`

    The request counts for different statuses within the batch.

    - `long completed`

      Number of requests that have been completed successfully.

    - `long failed`

      Number of requests that have failed.

    - `long total`

      Total number of requests in the batch.

  - `Optional<BatchUsage> usage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `long inputTokens`

      The number of input tokens.

    - `InputTokensDetails inputTokensDetails`

      A detailed breakdown of the input tokens.

      - `long cachedTokens`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `long outputTokens`

      The number of output tokens.

    - `OutputTokensDetails outputTokensDetails`

      A detailed breakdown of the output tokens.

      - `long reasoningTokens`

        The number of reasoning tokens.

    - `long totalTokens`

      The total number of tokens used.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.batches.Batch;
import com.openai.models.batches.BatchCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        BatchCreateParams params = BatchCreateParams.builder()
            .completionWindow(BatchCreateParams.CompletionWindow._24H)
            .endpoint(BatchCreateParams.Endpoint.V1_RESPONSES)
            .inputFileId("input_file_id")
            .build();
        Batch batch = client.batches().create(params);
    }
}
```

## Retrieve

`Batch batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/batches/{batch_id}`

Retrieves a batch.

### Parameters

- `BatchRetrieveParams params`

  - `Optional<String> batchId`

### Returns

- `class Batch:`

  - `String id`

  - `String completionWindow`

    The time frame within which the batch should be processed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the batch was created.

  - `String endpoint`

    The OpenAI API endpoint used by the batch.

  - `String inputFileId`

    The ID of the input file for the batch.

  - `JsonValue; object_ "batch"constant`

    The object type, which is always `batch`.

    - `BATCH("batch")`

  - `Status status`

    The current status of the batch.

    - `VALIDATING("validating")`

    - `FAILED("failed")`

    - `IN_PROGRESS("in_progress")`

    - `FINALIZING("finalizing")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `Optional<Long> cancellingAt`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `Optional<String> errorFileId`

    The ID of the file containing the outputs of requests with errors.

  - `Optional<Errors> errors`

    - `Optional<List<BatchError>> data`

      - `Optional<String> code`

        An error code identifying the error type.

      - `Optional<Long> line`

        The line number of the input file where the error occurred, if applicable.

      - `Optional<String> message`

        A human-readable message providing more details about the error.

      - `Optional<String> param`

        The name of the parameter that caused the error, if applicable.

    - `Optional<String> object_`

      The object type, which is always `list`.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the batch expired.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the batch failed.

  - `Optional<Long> finalizingAt`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `Optional<Long> inProgressAt`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> model`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `Optional<String> outputFileId`

    The ID of the file containing the outputs of successfully executed requests.

  - `Optional<BatchRequestCounts> requestCounts`

    The request counts for different statuses within the batch.

    - `long completed`

      Number of requests that have been completed successfully.

    - `long failed`

      Number of requests that have failed.

    - `long total`

      Total number of requests in the batch.

  - `Optional<BatchUsage> usage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `long inputTokens`

      The number of input tokens.

    - `InputTokensDetails inputTokensDetails`

      A detailed breakdown of the input tokens.

      - `long cachedTokens`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `long outputTokens`

      The number of output tokens.

    - `OutputTokensDetails outputTokensDetails`

      A detailed breakdown of the output tokens.

      - `long reasoningTokens`

        The number of reasoning tokens.

    - `long totalTokens`

      The total number of tokens used.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.batches.Batch;
import com.openai.models.batches.BatchRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Batch batch = client.batches().retrieve("batch_id");
    }
}
```

## Cancel

`Batch batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/batches/{batch_id}/cancel`

Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.

### Parameters

- `BatchCancelParams params`

  - `Optional<String> batchId`

### Returns

- `class Batch:`

  - `String id`

  - `String completionWindow`

    The time frame within which the batch should be processed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the batch was created.

  - `String endpoint`

    The OpenAI API endpoint used by the batch.

  - `String inputFileId`

    The ID of the input file for the batch.

  - `JsonValue; object_ "batch"constant`

    The object type, which is always `batch`.

    - `BATCH("batch")`

  - `Status status`

    The current status of the batch.

    - `VALIDATING("validating")`

    - `FAILED("failed")`

    - `IN_PROGRESS("in_progress")`

    - `FINALIZING("finalizing")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `Optional<Long> cancellingAt`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `Optional<String> errorFileId`

    The ID of the file containing the outputs of requests with errors.

  - `Optional<Errors> errors`

    - `Optional<List<BatchError>> data`

      - `Optional<String> code`

        An error code identifying the error type.

      - `Optional<Long> line`

        The line number of the input file where the error occurred, if applicable.

      - `Optional<String> message`

        A human-readable message providing more details about the error.

      - `Optional<String> param`

        The name of the parameter that caused the error, if applicable.

    - `Optional<String> object_`

      The object type, which is always `list`.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the batch expired.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the batch failed.

  - `Optional<Long> finalizingAt`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `Optional<Long> inProgressAt`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> model`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `Optional<String> outputFileId`

    The ID of the file containing the outputs of successfully executed requests.

  - `Optional<BatchRequestCounts> requestCounts`

    The request counts for different statuses within the batch.

    - `long completed`

      Number of requests that have been completed successfully.

    - `long failed`

      Number of requests that have failed.

    - `long total`

      Total number of requests in the batch.

  - `Optional<BatchUsage> usage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `long inputTokens`

      The number of input tokens.

    - `InputTokensDetails inputTokensDetails`

      A detailed breakdown of the input tokens.

      - `long cachedTokens`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `long outputTokens`

      The number of output tokens.

    - `OutputTokensDetails outputTokensDetails`

      A detailed breakdown of the output tokens.

      - `long reasoningTokens`

        The number of reasoning tokens.

    - `long totalTokens`

      The total number of tokens used.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.batches.Batch;
import com.openai.models.batches.BatchCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Batch batch = client.batches().cancel("batch_id");
    }
}
```

## List

`BatchListPage batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/batches`

List your organization's batches.

### Parameters

- `BatchListParams params`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

### Returns

- `class Batch:`

  - `String id`

  - `String completionWindow`

    The time frame within which the batch should be processed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the batch was created.

  - `String endpoint`

    The OpenAI API endpoint used by the batch.

  - `String inputFileId`

    The ID of the input file for the batch.

  - `JsonValue; object_ "batch"constant`

    The object type, which is always `batch`.

    - `BATCH("batch")`

  - `Status status`

    The current status of the batch.

    - `VALIDATING("validating")`

    - `FAILED("failed")`

    - `IN_PROGRESS("in_progress")`

    - `FINALIZING("finalizing")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `Optional<Long> cancellingAt`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `Optional<String> errorFileId`

    The ID of the file containing the outputs of requests with errors.

  - `Optional<Errors> errors`

    - `Optional<List<BatchError>> data`

      - `Optional<String> code`

        An error code identifying the error type.

      - `Optional<Long> line`

        The line number of the input file where the error occurred, if applicable.

      - `Optional<String> message`

        A human-readable message providing more details about the error.

      - `Optional<String> param`

        The name of the parameter that caused the error, if applicable.

    - `Optional<String> object_`

      The object type, which is always `list`.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the batch expired.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the batch failed.

  - `Optional<Long> finalizingAt`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `Optional<Long> inProgressAt`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> model`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `Optional<String> outputFileId`

    The ID of the file containing the outputs of successfully executed requests.

  - `Optional<BatchRequestCounts> requestCounts`

    The request counts for different statuses within the batch.

    - `long completed`

      Number of requests that have been completed successfully.

    - `long failed`

      Number of requests that have failed.

    - `long total`

      Total number of requests in the batch.

  - `Optional<BatchUsage> usage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `long inputTokens`

      The number of input tokens.

    - `InputTokensDetails inputTokensDetails`

      A detailed breakdown of the input tokens.

      - `long cachedTokens`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `long outputTokens`

      The number of output tokens.

    - `OutputTokensDetails outputTokensDetails`

      A detailed breakdown of the output tokens.

      - `long reasoningTokens`

        The number of reasoning tokens.

    - `long totalTokens`

      The total number of tokens used.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.batches.BatchListPage;
import com.openai.models.batches.BatchListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        BatchListPage page = client.batches().list();
    }
}
```

### Domain Types

### Batch

- `class Batch:`

  - `String id`

  - `String completionWindow`

    The time frame within which the batch should be processed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the batch was created.

  - `String endpoint`

    The OpenAI API endpoint used by the batch.

  - `String inputFileId`

    The ID of the input file for the batch.

  - `JsonValue; object_ "batch"constant`

    The object type, which is always `batch`.

    - `BATCH("batch")`

  - `Status status`

    The current status of the batch.

    - `VALIDATING("validating")`

    - `FAILED("failed")`

    - `IN_PROGRESS("in_progress")`

    - `FINALIZING("finalizing")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the batch was cancelled.

  - `Optional<Long> cancellingAt`

    The Unix timestamp (in seconds) for when the batch started cancelling.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the batch was completed.

  - `Optional<String> errorFileId`

    The ID of the file containing the outputs of requests with errors.

  - `Optional<Errors> errors`

    - `Optional<List<BatchError>> data`

      - `Optional<String> code`

        An error code identifying the error type.

      - `Optional<Long> line`

        The line number of the input file where the error occurred, if applicable.

      - `Optional<String> message`

        A human-readable message providing more details about the error.

      - `Optional<String> param`

        The name of the parameter that caused the error, if applicable.

    - `Optional<String> object_`

      The object type, which is always `list`.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the batch expired.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the batch will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the batch failed.

  - `Optional<Long> finalizingAt`

    The Unix timestamp (in seconds) for when the batch started finalizing.

  - `Optional<Long> inProgressAt`

    The Unix timestamp (in seconds) for when the batch started processing.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> model`

    Model ID used to process the batch, like `gpt-5-2025-08-07`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model
    guide](https://platform.openai.com/docs/models) to browse and compare available models.

  - `Optional<String> outputFileId`

    The ID of the file containing the outputs of successfully executed requests.

  - `Optional<BatchRequestCounts> requestCounts`

    The request counts for different statuses within the batch.

    - `long completed`

      Number of requests that have been completed successfully.

    - `long failed`

      Number of requests that have failed.

    - `long total`

      Total number of requests in the batch.

  - `Optional<BatchUsage> usage`

    Represents token usage details including input tokens, output tokens, a
    breakdown of output tokens, and the total tokens used. Only populated on
    batches created after September 7, 2025.

    - `long inputTokens`

      The number of input tokens.

    - `InputTokensDetails inputTokensDetails`

      A detailed breakdown of the input tokens.

      - `long cachedTokens`

        The number of tokens that were retrieved from the cache. [More on
        prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

    - `long outputTokens`

      The number of output tokens.

    - `OutputTokensDetails outputTokensDetails`

      A detailed breakdown of the output tokens.

      - `long reasoningTokens`

        The number of reasoning tokens.

    - `long totalTokens`

      The total number of tokens used.

### Batch Error

- `class BatchError:`

  - `Optional<String> code`

    An error code identifying the error type.

  - `Optional<Long> line`

    The line number of the input file where the error occurred, if applicable.

  - `Optional<String> message`

    A human-readable message providing more details about the error.

  - `Optional<String> param`

    The name of the parameter that caused the error, if applicable.

### Batch Request Counts

- `class BatchRequestCounts:`

  The request counts for different statuses within the batch.

  - `long completed`

    Number of requests that have been completed successfully.

  - `long failed`

    Number of requests that have failed.

  - `long total`

    Total number of requests in the batch.

### Batch Usage

- `class BatchUsage:`

  Represents token usage details including input tokens, output tokens, a
  breakdown of output tokens, and the total tokens used. Only populated on
  batches created after September 7, 2025.

  - `long inputTokens`

    The number of input tokens.

  - `InputTokensDetails inputTokensDetails`

    A detailed breakdown of the input tokens.

    - `long cachedTokens`

      The number of tokens that were retrieved from the cache. [More on
      prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

  - `long outputTokens`

    The number of output tokens.

  - `OutputTokensDetails outputTokensDetails`

    A detailed breakdown of the output tokens.

    - `long reasoningTokens`

      The number of reasoning tokens.

  - `long totalTokens`

    The total number of tokens used.
