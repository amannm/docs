# Vector Stores

## List

`VectorStoreListPage vectorStores().list(VectorStoreListParamsparams = VectorStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores`

Returns a list of vector stores.

### Parameters

- `VectorStoreListParams params`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

### Returns

- `class VectorStore:`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that were cancelled.

    - `long completed`

      The number of files that have been successfully processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `Optional<Long> lastActiveAt`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the vector store.

  - `JsonValue; object_ "vector_store"constant`

    The object type, which is always `vector_store`.

    - `VECTOR_STORE("vector_store")`

  - `Status status`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `EXPIRED("expired")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

  - `long usageBytes`

    The total number of bytes used by the files in the vector store.

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStoreListPage;
import com.openai.models.vectorstores.VectorStoreListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStoreListPage page = client.vectorStores().list();
    }
}
```

## Create

`VectorStore vectorStores().create(VectorStoreCreateParamsparams = VectorStoreCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores`

Create a vector store.

### Parameters

- `VectorStoreCreateParams params`

  - `Optional<FileChunkingStrategyParam> chunkingStrategy`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `Optional<String> description`

    A description for the vector store. Can be used to describe the vector store's purpose.

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<List<String>> fileIds`

    A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> name`

    The name of the vector store.

### Returns

- `class VectorStore:`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that were cancelled.

    - `long completed`

      The number of files that have been successfully processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `Optional<Long> lastActiveAt`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the vector store.

  - `JsonValue; object_ "vector_store"constant`

    The object type, which is always `vector_store`.

    - `VECTOR_STORE("vector_store")`

  - `Status status`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `EXPIRED("expired")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

  - `long usageBytes`

    The total number of bytes used by the files in the vector store.

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStore;
import com.openai.models.vectorstores.VectorStoreCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStore vectorStore = client.vectorStores().create();
    }
}
```

## Retrieve

`VectorStore vectorStores().retrieve(VectorStoreRetrieveParamsparams = VectorStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores/{vector_store_id}`

Retrieves a vector store.

### Parameters

- `VectorStoreRetrieveParams params`

  - `Optional<String> vectorStoreId`

### Returns

- `class VectorStore:`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that were cancelled.

    - `long completed`

      The number of files that have been successfully processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `Optional<Long> lastActiveAt`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the vector store.

  - `JsonValue; object_ "vector_store"constant`

    The object type, which is always `vector_store`.

    - `VECTOR_STORE("vector_store")`

  - `Status status`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `EXPIRED("expired")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

  - `long usageBytes`

    The total number of bytes used by the files in the vector store.

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStore;
import com.openai.models.vectorstores.VectorStoreRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStore vectorStore = client.vectorStores().retrieve("vector_store_id");
    }
}
```

## Update

`VectorStore vectorStores().update(VectorStoreUpdateParamsparams = VectorStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores/{vector_store_id}`

Modifies a vector store.

### Parameters

- `VectorStoreUpdateParams params`

  - `Optional<String> vectorStoreId`

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> name`

    The name of the vector store.

### Returns

- `class VectorStore:`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that were cancelled.

    - `long completed`

      The number of files that have been successfully processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `Optional<Long> lastActiveAt`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the vector store.

  - `JsonValue; object_ "vector_store"constant`

    The object type, which is always `vector_store`.

    - `VECTOR_STORE("vector_store")`

  - `Status status`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `EXPIRED("expired")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

  - `long usageBytes`

    The total number of bytes used by the files in the vector store.

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStore;
import com.openai.models.vectorstores.VectorStoreUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStore vectorStore = client.vectorStores().update("vector_store_id");
    }
}
```

## Delete

`VectorStoreDeleted vectorStores().delete(VectorStoreDeleteParamsparams = VectorStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/vector_stores/{vector_store_id}`

Delete a vector store.

### Parameters

- `VectorStoreDeleteParams params`

  - `Optional<String> vectorStoreId`

### Returns

- `class VectorStoreDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "vector_store.deleted"constant`

    - `VECTOR_STORE_DELETED("vector_store.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStoreDeleteParams;
import com.openai.models.vectorstores.VectorStoreDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStoreDeleted vectorStoreDeleted = client.vectorStores().delete("vector_store_id");
    }
}
```

## Search

`VectorStoreSearchPage vectorStores().search(VectorStoreSearchParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores/{vector_store_id}/search`

Search a vector store for relevant chunks based on a query and file attributes filter.

### Parameters

- `VectorStoreSearchParams params`

  - `Optional<String> vectorStoreId`

  - `Query query`

    A query string for a search

    - `String`

    - `List<String>`

  - `Optional<Filters> filters`

    A filter to apply based on file attributes.

    - `class ComparisonFilter:`

      A filter used to compare a specified attribute key to a given value using a defined comparison operation.

      - `String key`

        The key to compare against the value.

      - `Type type`

        Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

        - `eq`: equals
        - `ne`: not equal
        - `gt`: greater than
        - `gte`: greater than or equal
        - `lt`: less than
        - `lte`: less than or equal
        - `in`: in
        - `nin`: not in

        - `EQ("eq")`

        - `NE("ne")`

        - `GT("gt")`

        - `GTE("gte")`

        - `LT("lt")`

        - `LTE("lte")`

      - `Value value`

        The value to compare against the attribute key; supports string, number, or boolean types.

        - `String`

        - `double`

        - `boolean`

        - `List<ComparisonFilterValueItem>`

          - `String`

          - `double`

    - `class CompoundFilter:`

      Combine multiple filters using `and` or `or`.

      - `List<Filter> filters`

        Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

        - `class ComparisonFilter:`

          A filter used to compare a specified attribute key to a given value using a defined comparison operation.

          - `String key`

            The key to compare against the value.

          - `Type type`

            Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

            - `eq`: equals
            - `ne`: not equal
            - `gt`: greater than
            - `gte`: greater than or equal
            - `lt`: less than
            - `lte`: less than or equal
            - `in`: in
            - `nin`: not in

            - `EQ("eq")`

            - `NE("ne")`

            - `GT("gt")`

            - `GTE("gte")`

            - `LT("lt")`

            - `LTE("lte")`

          - `Value value`

            The value to compare against the attribute key; supports string, number, or boolean types.

            - `String`

            - `double`

            - `boolean`

            - `List<ComparisonFilterValueItem>`

              - `String`

              - `double`

        - `JsonValue`

      - `Type type`

        Type of operation: `and` or `or`.

        - `AND("and")`

        - `OR("or")`

  - `Optional<Long> maxNumResults`

    The maximum number of results to return. This number should be between 1 and 50 inclusive.

  - `Optional<RankingOptions> rankingOptions`

    Ranking options for search.

    - `Optional<Ranker> ranker`

      Enable re-ranking; set to `none` to disable, which can help reduce latency.

      - `NONE("none")`

      - `AUTO("auto")`

      - `DEFAULT_2024_11_15("default-2024-11-15")`

    - `Optional<Double> scoreThreshold`

  - `Optional<Boolean> rewriteQuery`

    Whether to rewrite the natural language query for vector search.

### Returns

- `class VectorStoreSearchResponse:`

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `List<Content> content`

    Content chunks from the file.

    - `String text`

      The text content returned from search.

    - `Type type`

      The type of content.

      - `TEXT("text")`

  - `String fileId`

    The ID of the vector store file.

  - `String filename`

    The name of the vector store file.

  - `double score`

    The similarity score for the result.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.VectorStoreSearchPage;
import com.openai.models.vectorstores.VectorStoreSearchParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStoreSearchParams params = VectorStoreSearchParams.builder()
            .vectorStoreId("vs_abc123")
            .query("string")
            .build();
        VectorStoreSearchPage page = client.vectorStores().search(params);
    }
}
```

### Domain Types

### Auto File Chunking Strategy Param

- `class AutoFileChunkingStrategyParam:`

  The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

  - `JsonValue; type "auto"constant`

    Always `auto`.

    - `AUTO("auto")`

### File Chunking Strategy

- `class FileChunkingStrategy: A class that can be one of several variants.union`

  The strategy used to chunk the file.

  - `class StaticFileChunkingStrategyObject:`

    - `StaticFileChunkingStrategy static_`

      - `long chunkOverlapTokens`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `long maxChunkSizeTokens`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `JsonValue; type "static"constant`

      Always `static`.

      - `STATIC("static")`

  - `class OtherFileChunkingStrategyObject:`

    This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

    - `JsonValue; type "other"constant`

      Always `other`.

      - `OTHER("other")`

### File Chunking Strategy Param

- `class FileChunkingStrategyParam: A class that can be one of several variants.union`

  The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `class AutoFileChunkingStrategyParam:`

    The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

    - `JsonValue; type "auto"constant`

      Always `auto`.

      - `AUTO("auto")`

  - `class StaticFileChunkingStrategyObjectParam:`

    Customize your own chunking strategy by setting chunk size and chunk overlap.

    - `StaticFileChunkingStrategy static_`

      - `long chunkOverlapTokens`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `long maxChunkSizeTokens`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `JsonValue; type "static"constant`

      Always `static`.

      - `STATIC("static")`

### Other File Chunking Strategy Object

- `class OtherFileChunkingStrategyObject:`

  This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

  - `JsonValue; type "other"constant`

    Always `other`.

    - `OTHER("other")`

### Static File Chunking Strategy

- `class StaticFileChunkingStrategy:`

  - `long chunkOverlapTokens`

    The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.

  - `long maxChunkSizeTokens`

    The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

### Static File Chunking Strategy Object

- `class StaticFileChunkingStrategyObject:`

  - `StaticFileChunkingStrategy static_`

    - `long chunkOverlapTokens`

      The number of tokens that overlap between chunks. The default value is `400`.

      Note that the overlap must not exceed half of `max_chunk_size_tokens`.

    - `long maxChunkSizeTokens`

      The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

  - `JsonValue; type "static"constant`

    Always `static`.

    - `STATIC("static")`

### Static File Chunking Strategy Object Param

- `class StaticFileChunkingStrategyObjectParam:`

  Customize your own chunking strategy by setting chunk size and chunk overlap.

  - `StaticFileChunkingStrategy static_`

    - `long chunkOverlapTokens`

      The number of tokens that overlap between chunks. The default value is `400`.

      Note that the overlap must not exceed half of `max_chunk_size_tokens`.

    - `long maxChunkSizeTokens`

      The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

  - `JsonValue; type "static"constant`

    Always `static`.

    - `STATIC("static")`

### Vector Store

- `class VectorStore:`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that were cancelled.

    - `long completed`

      The number of files that have been successfully processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `Optional<Long> lastActiveAt`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the vector store.

  - `JsonValue; object_ "vector_store"constant`

    The object type, which is always `vector_store`.

    - `VECTOR_STORE("vector_store")`

  - `Status status`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `EXPIRED("expired")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

  - `long usageBytes`

    The total number of bytes used by the files in the vector store.

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a vector store.

    - `JsonValue; anchor "last_active_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long days`

      The number of days after the anchor time that the vector store will expire.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Vector Store Deleted

- `class VectorStoreDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "vector_store.deleted"constant`

    - `VECTOR_STORE_DELETED("vector_store.deleted")`

## Files

### List

`FileListPage vectorStores().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores/{vector_store_id}/files`

Returns a list of vector store files.

#### Parameters

- `FileListParams params`

  - `Optional<String> vectorStoreId`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<Filter> filter`

    Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

#### Returns

- `class VectorStoreFile:`

  A list of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `Optional<LastError> lastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `SERVER_ERROR("server_error")`

      - `UNSUPPORTED_FILE("unsupported_file")`

      - `INVALID_FILE("invalid_file")`

    - `String message`

      A human-readable description of the error.

  - `JsonValue; object_ "vector_store.file"constant`

    The object type, which is always `vector_store.file`.

    - `VECTOR_STORE_FILE("vector_store.file")`

  - `Status status`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `long usageBytes`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategy> chunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject:`

      - `StaticFileChunkingStrategy static_`

        - `long chunkOverlapTokens`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `long maxChunkSizeTokens`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `JsonValue; type "static"constant`

        Always `static`.

        - `STATIC("static")`

    - `class OtherFileChunkingStrategyObject:`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `JsonValue; type "other"constant`

        Always `other`.

        - `OTHER("other")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.files.FileListPage;
import com.openai.models.vectorstores.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileListPage page = client.vectorStores().files().list("vector_store_id");
    }
}
```

### Create

`VectorStoreFile vectorStores().files().create(FileCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores/{vector_store_id}/files`

Create a vector store file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

#### Parameters

- `FileCreateParams params`

  - `Optional<String> vectorStoreId`

  - `String fileId`

    A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategyParam> chunkingStrategy`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

#### Returns

- `class VectorStoreFile:`

  A list of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `Optional<LastError> lastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `SERVER_ERROR("server_error")`

      - `UNSUPPORTED_FILE("unsupported_file")`

      - `INVALID_FILE("invalid_file")`

    - `String message`

      A human-readable description of the error.

  - `JsonValue; object_ "vector_store.file"constant`

    The object type, which is always `vector_store.file`.

    - `VECTOR_STORE_FILE("vector_store.file")`

  - `Status status`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `long usageBytes`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategy> chunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject:`

      - `StaticFileChunkingStrategy static_`

        - `long chunkOverlapTokens`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `long maxChunkSizeTokens`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `JsonValue; type "static"constant`

        Always `static`.

        - `STATIC("static")`

    - `class OtherFileChunkingStrategyObject:`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `JsonValue; type "other"constant`

        Always `other`.

        - `OTHER("other")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.files.FileCreateParams;
import com.openai.models.vectorstores.files.VectorStoreFile;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileCreateParams params = FileCreateParams.builder()
            .vectorStoreId("vs_abc123")
            .fileId("file_id")
            .build();
        VectorStoreFile vectorStoreFile = client.vectorStores().files().create(params);
    }
}
```

### Update

`VectorStoreFile vectorStores().files().update(FileUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores/{vector_store_id}/files/{file_id}`

Update attributes on a vector store file.

#### Parameters

- `FileUpdateParams params`

  - `String vectorStoreId`

  - `Optional<String> fileId`

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

#### Returns

- `class VectorStoreFile:`

  A list of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `Optional<LastError> lastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `SERVER_ERROR("server_error")`

      - `UNSUPPORTED_FILE("unsupported_file")`

      - `INVALID_FILE("invalid_file")`

    - `String message`

      A human-readable description of the error.

  - `JsonValue; object_ "vector_store.file"constant`

    The object type, which is always `vector_store.file`.

    - `VECTOR_STORE_FILE("vector_store.file")`

  - `Status status`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `long usageBytes`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategy> chunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject:`

      - `StaticFileChunkingStrategy static_`

        - `long chunkOverlapTokens`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `long maxChunkSizeTokens`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `JsonValue; type "static"constant`

        Always `static`.

        - `STATIC("static")`

    - `class OtherFileChunkingStrategyObject:`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `JsonValue; type "other"constant`

        Always `other`.

        - `OTHER("other")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.vectorstores.files.FileUpdateParams;
import com.openai.models.vectorstores.files.VectorStoreFile;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileUpdateParams params = FileUpdateParams.builder()
            .vectorStoreId("vs_abc123")
            .fileId("file-abc123")
            .attributes(FileUpdateParams.Attributes.builder()
                .putAdditionalProperty("foo", JsonValue.from("string"))
                .build())
            .build();
        VectorStoreFile vectorStoreFile = client.vectorStores().files().update(params);
    }
}
```

### Retrieve

`VectorStoreFile vectorStores().files().retrieve(FileRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores/{vector_store_id}/files/{file_id}`

Retrieves a vector store file.

#### Parameters

- `FileRetrieveParams params`

  - `String vectorStoreId`

  - `Optional<String> fileId`

#### Returns

- `class VectorStoreFile:`

  A list of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `Optional<LastError> lastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `SERVER_ERROR("server_error")`

      - `UNSUPPORTED_FILE("unsupported_file")`

      - `INVALID_FILE("invalid_file")`

    - `String message`

      A human-readable description of the error.

  - `JsonValue; object_ "vector_store.file"constant`

    The object type, which is always `vector_store.file`.

    - `VECTOR_STORE_FILE("vector_store.file")`

  - `Status status`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `long usageBytes`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategy> chunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject:`

      - `StaticFileChunkingStrategy static_`

        - `long chunkOverlapTokens`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `long maxChunkSizeTokens`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `JsonValue; type "static"constant`

        Always `static`.

        - `STATIC("static")`

    - `class OtherFileChunkingStrategyObject:`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `JsonValue; type "other"constant`

        Always `other`.

        - `OTHER("other")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.files.FileRetrieveParams;
import com.openai.models.vectorstores.files.VectorStoreFile;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileRetrieveParams params = FileRetrieveParams.builder()
            .vectorStoreId("vs_abc123")
            .fileId("file-abc123")
            .build();
        VectorStoreFile vectorStoreFile = client.vectorStores().files().retrieve(params);
    }
}
```

### Delete

`VectorStoreFileDeleted vectorStores().files().delete(FileDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/vector_stores/{vector_store_id}/files/{file_id}`

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

#### Parameters

- `FileDeleteParams params`

  - `String vectorStoreId`

  - `Optional<String> fileId`

#### Returns

- `class VectorStoreFileDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "vector_store.file.deleted"constant`

    - `VECTOR_STORE_FILE_DELETED("vector_store.file.deleted")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.files.FileDeleteParams;
import com.openai.models.vectorstores.files.VectorStoreFileDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileDeleteParams params = FileDeleteParams.builder()
            .vectorStoreId("vector_store_id")
            .fileId("file_id")
            .build();
        VectorStoreFileDeleted vectorStoreFileDeleted = client.vectorStores().files().delete(params);
    }
}
```

### Content

`FileContentPage vectorStores().files().content(FileContentParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores/{vector_store_id}/files/{file_id}/content`

Retrieve the parsed contents of a vector store file.

#### Parameters

- `FileContentParams params`

  - `String vectorStoreId`

  - `Optional<String> fileId`

#### Returns

- `class FileContentResponse:`

  - `Optional<String> text`

    The text content

  - `Optional<String> type`

    The content type (currently only `"text"`)

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.files.FileContentPage;
import com.openai.models.vectorstores.files.FileContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileContentParams params = FileContentParams.builder()
            .vectorStoreId("vs_abc123")
            .fileId("file-abc123")
            .build();
        FileContentPage page = client.vectorStores().files().content(params);
    }
}
```

#### Domain Types

#### Vector Store File

- `class VectorStoreFile:`

  A list of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `Optional<LastError> lastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `SERVER_ERROR("server_error")`

      - `UNSUPPORTED_FILE("unsupported_file")`

      - `INVALID_FILE("invalid_file")`

    - `String message`

      A human-readable description of the error.

  - `JsonValue; object_ "vector_store.file"constant`

    The object type, which is always `vector_store.file`.

    - `VECTOR_STORE_FILE("vector_store.file")`

  - `Status status`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `long usageBytes`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategy> chunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject:`

      - `StaticFileChunkingStrategy static_`

        - `long chunkOverlapTokens`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `long maxChunkSizeTokens`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `JsonValue; type "static"constant`

        Always `static`.

        - `STATIC("static")`

    - `class OtherFileChunkingStrategyObject:`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `JsonValue; type "other"constant`

        Always `other`.

        - `OTHER("other")`

#### Vector Store File Deleted

- `class VectorStoreFileDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "vector_store.file.deleted"constant`

    - `VECTOR_STORE_FILE_DELETED("vector_store.file.deleted")`

## File Batches

### Create

`VectorStoreFileBatch vectorStores().fileBatches().create(FileBatchCreateParamsparams = FileBatchCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores/{vector_store_id}/file_batches`

Create a vector store file batch.

#### Parameters

- `FileBatchCreateParams params`

  - `Optional<String> vectorStoreId`

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategyParam> chunkingStrategy`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `Optional<List<String>> fileIds`

    A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.  If `attributes` or `chunking_strategy` are provided, they will be  applied to all files in the batch. The maximum batch size is 2000 files. Mutually exclusive with `files`.

  - `Optional<List<File>> files`

    A list of objects that each include a `file_id` plus optional `attributes` or `chunking_strategy`. Use this when you need to override metadata for specific files. The global `attributes` or `chunking_strategy` will be ignored and must be specified for each file. The maximum batch size is 2000 files. Mutually exclusive with `file_ids`.

    - `String fileId`

      A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

    - `Optional<Attributes> attributes`

      Set of 16 key-value pairs that can be attached to an object. This can be
      useful for storing additional information about the object in a structured
      format, and querying for objects via API or the dashboard. Keys are strings
      with a maximum length of 64 characters. Values are strings with a maximum
      length of 512 characters, booleans, or numbers.

      - `String`

      - `double`

      - `boolean`

    - `Optional<FileChunkingStrategyParam> chunkingStrategy`

      The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

      - `class AutoFileChunkingStrategyParam:`

        The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

        - `JsonValue; type "auto"constant`

          Always `auto`.

          - `AUTO("auto")`

      - `class StaticFileChunkingStrategyObjectParam:`

        Customize your own chunking strategy by setting chunk size and chunk overlap.

        - `StaticFileChunkingStrategy static_`

          - `long chunkOverlapTokens`

            The number of tokens that overlap between chunks. The default value is `400`.

            Note that the overlap must not exceed half of `max_chunk_size_tokens`.

          - `long maxChunkSizeTokens`

            The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

        - `JsonValue; type "static"constant`

          Always `static`.

          - `STATIC("static")`

#### Returns

- `class VectorStoreFileBatch:`

  A batch of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that where cancelled.

    - `long completed`

      The number of files that have been processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `JsonValue; object_ "vector_store.files_batch"constant`

    The object type, which is always `vector_store.file_batch`.

    - `VECTOR_STORE_FILES_BATCH("vector_store.files_batch")`

  - `Status status`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.filebatches.FileBatchCreateParams;
import com.openai.models.vectorstores.filebatches.VectorStoreFileBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VectorStoreFileBatch vectorStoreFileBatch = client.vectorStores().fileBatches().create("vs_abc123");
    }
}
```

### Retrieve

`VectorStoreFileBatch vectorStores().fileBatches().retrieve(FileBatchRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores/{vector_store_id}/file_batches/{batch_id}`

Retrieves a vector store file batch.

#### Parameters

- `FileBatchRetrieveParams params`

  - `String vectorStoreId`

  - `Optional<String> batchId`

#### Returns

- `class VectorStoreFileBatch:`

  A batch of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that where cancelled.

    - `long completed`

      The number of files that have been processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `JsonValue; object_ "vector_store.files_batch"constant`

    The object type, which is always `vector_store.file_batch`.

    - `VECTOR_STORE_FILES_BATCH("vector_store.files_batch")`

  - `Status status`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.filebatches.FileBatchRetrieveParams;
import com.openai.models.vectorstores.filebatches.VectorStoreFileBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileBatchRetrieveParams params = FileBatchRetrieveParams.builder()
            .vectorStoreId("vs_abc123")
            .batchId("vsfb_abc123")
            .build();
        VectorStoreFileBatch vectorStoreFileBatch = client.vectorStores().fileBatches().retrieve(params);
    }
}
```

### Cancel

`VectorStoreFileBatch vectorStores().fileBatches().cancel(FileBatchCancelParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel`

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

#### Parameters

- `FileBatchCancelParams params`

  - `String vectorStoreId`

  - `Optional<String> batchId`

#### Returns

- `class VectorStoreFileBatch:`

  A batch of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that where cancelled.

    - `long completed`

      The number of files that have been processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `JsonValue; object_ "vector_store.files_batch"constant`

    The object type, which is always `vector_store.file_batch`.

    - `VECTOR_STORE_FILES_BATCH("vector_store.files_batch")`

  - `Status status`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.filebatches.FileBatchCancelParams;
import com.openai.models.vectorstores.filebatches.VectorStoreFileBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileBatchCancelParams params = FileBatchCancelParams.builder()
            .vectorStoreId("vector_store_id")
            .batchId("batch_id")
            .build();
        VectorStoreFileBatch vectorStoreFileBatch = client.vectorStores().fileBatches().cancel(params);
    }
}
```

### List Files

`FileBatchListFilesPage vectorStores().fileBatches().listFiles(FileBatchListFilesParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/files`

Returns a list of vector store files in a batch.

#### Parameters

- `FileBatchListFilesParams params`

  - `String vectorStoreId`

  - `Optional<String> batchId`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<Filter> filter`

    Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

#### Returns

- `class VectorStoreFile:`

  A list of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `Optional<LastError> lastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `SERVER_ERROR("server_error")`

      - `UNSUPPORTED_FILE("unsupported_file")`

      - `INVALID_FILE("invalid_file")`

    - `String message`

      A human-readable description of the error.

  - `JsonValue; object_ "vector_store.file"constant`

    The object type, which is always `vector_store.file`.

    - `VECTOR_STORE_FILE("vector_store.file")`

  - `Status status`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `long usageBytes`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Optional<Attributes> attributes`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `double`

    - `boolean`

  - `Optional<FileChunkingStrategy> chunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject:`

      - `StaticFileChunkingStrategy static_`

        - `long chunkOverlapTokens`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `long maxChunkSizeTokens`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `JsonValue; type "static"constant`

        Always `static`.

        - `STATIC("static")`

    - `class OtherFileChunkingStrategyObject:`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `JsonValue; type "other"constant`

        Always `other`.

        - `OTHER("other")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.vectorstores.filebatches.FileBatchListFilesPage;
import com.openai.models.vectorstores.filebatches.FileBatchListFilesParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileBatchListFilesParams params = FileBatchListFilesParams.builder()
            .vectorStoreId("vector_store_id")
            .batchId("batch_id")
            .build();
        FileBatchListFilesPage page = client.vectorStores().fileBatches().listFiles(params);
    }
}
```

#### Domain Types

#### Vector Store File Batch

- `class VectorStoreFileBatch:`

  A batch of files attached to a vector store.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts fileCounts`

    - `long cancelled`

      The number of files that where cancelled.

    - `long completed`

      The number of files that have been processed.

    - `long failed`

      The number of files that have failed to process.

    - `long inProgress`

      The number of files that are currently being processed.

    - `long total`

      The total number of files.

  - `JsonValue; object_ "vector_store.files_batch"constant`

    The object type, which is always `vector_store.file_batch`.

    - `VECTOR_STORE_FILES_BATCH("vector_store.files_batch")`

  - `Status status`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

  - `String vectorStoreId`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
