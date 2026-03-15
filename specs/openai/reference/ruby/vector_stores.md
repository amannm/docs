# Vector Stores

## List

`vector_stores.list(**kwargs) -> CursorPage<VectorStore>`

**get** `/vector_stores`

Returns a list of vector stores.

### Parameters

- `after: String`

  A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- `before: String`

  A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

- `limit: Integer`

  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

  - `:asc`

  - `:desc`

### Returns

- `class VectorStore`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that were cancelled.

    - `completed: Integer`

      The number of files that have been successfully processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `last_active_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the vector store.

  - `object: :vector_store`

    The object type, which is always `vector_store`.

    - `:vector_store`

  - `status: :expired | :in_progress | :completed`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `:expired`

    - `:in_progress`

    - `:completed`

  - `usage_bytes: Integer`

    The total number of bytes used by the files in the vector store.

  - `expires_after: { anchor, days}`

    The expiration policy for a vector store.

    - `anchor: :last_active_at`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `:last_active_at`

    - `days: Integer`

      The number of days after the anchor time that the vector store will expire.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.vector_stores.list

puts(page)
```

## Create

`vector_stores.create(**kwargs) -> VectorStore`

**post** `/vector_stores`

Create a vector store.

### Parameters

- `chunking_strategy: FileChunkingStrategyParam`

  The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `class AutoFileChunkingStrategyParam`

    The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

    - `type: :auto`

      Always `auto`.

      - `:auto`

  - `class StaticFileChunkingStrategyObjectParam`

    Customize your own chunking strategy by setting chunk size and chunk overlap.

    - `static: StaticFileChunkingStrategy`

      - `chunk_overlap_tokens: Integer`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `max_chunk_size_tokens: Integer`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `type: :static`

      Always `static`.

      - `:static`

- `description: String`

  A description for the vector store. Can be used to describe the vector store's purpose.

- `expires_after: { anchor, days}`

  The expiration policy for a vector store.

  - `anchor: :last_active_at`

    Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

    - `:last_active_at`

  - `days: Integer`

    The number of days after the anchor time that the vector store will expire.

- `file_ids: Array[String]`

  A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `name: String`

  The name of the vector store.

### Returns

- `class VectorStore`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that were cancelled.

    - `completed: Integer`

      The number of files that have been successfully processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `last_active_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the vector store.

  - `object: :vector_store`

    The object type, which is always `vector_store`.

    - `:vector_store`

  - `status: :expired | :in_progress | :completed`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `:expired`

    - `:in_progress`

    - `:completed`

  - `usage_bytes: Integer`

    The total number of bytes used by the files in the vector store.

  - `expires_after: { anchor, days}`

    The expiration policy for a vector store.

    - `anchor: :last_active_at`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `:last_active_at`

    - `days: Integer`

      The number of days after the anchor time that the vector store will expire.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store = openai.vector_stores.create

puts(vector_store)
```

## Retrieve

`vector_stores.retrieve(vector_store_id) -> VectorStore`

**get** `/vector_stores/{vector_store_id}`

Retrieves a vector store.

### Parameters

- `vector_store_id: String`

### Returns

- `class VectorStore`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that were cancelled.

    - `completed: Integer`

      The number of files that have been successfully processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `last_active_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the vector store.

  - `object: :vector_store`

    The object type, which is always `vector_store`.

    - `:vector_store`

  - `status: :expired | :in_progress | :completed`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `:expired`

    - `:in_progress`

    - `:completed`

  - `usage_bytes: Integer`

    The total number of bytes used by the files in the vector store.

  - `expires_after: { anchor, days}`

    The expiration policy for a vector store.

    - `anchor: :last_active_at`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `:last_active_at`

    - `days: Integer`

      The number of days after the anchor time that the vector store will expire.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store = openai.vector_stores.retrieve("vector_store_id")

puts(vector_store)
```

## Update

`vector_stores.update(vector_store_id, **kwargs) -> VectorStore`

**post** `/vector_stores/{vector_store_id}`

Modifies a vector store.

### Parameters

- `vector_store_id: String`

- `expires_after: { anchor, days}`

  The expiration policy for a vector store.

  - `anchor: :last_active_at`

    Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

    - `:last_active_at`

  - `days: Integer`

    The number of days after the anchor time that the vector store will expire.

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `name: String`

  The name of the vector store.

### Returns

- `class VectorStore`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that were cancelled.

    - `completed: Integer`

      The number of files that have been successfully processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `last_active_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the vector store.

  - `object: :vector_store`

    The object type, which is always `vector_store`.

    - `:vector_store`

  - `status: :expired | :in_progress | :completed`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `:expired`

    - `:in_progress`

    - `:completed`

  - `usage_bytes: Integer`

    The total number of bytes used by the files in the vector store.

  - `expires_after: { anchor, days}`

    The expiration policy for a vector store.

    - `anchor: :last_active_at`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `:last_active_at`

    - `days: Integer`

      The number of days after the anchor time that the vector store will expire.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store = openai.vector_stores.update("vector_store_id")

puts(vector_store)
```

## Delete

`vector_stores.delete(vector_store_id) -> VectorStoreDeleted`

**delete** `/vector_stores/{vector_store_id}`

Delete a vector store.

### Parameters

- `vector_store_id: String`

### Returns

- `class VectorStoreDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"vector_store.deleted"`

    - `:"vector_store.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_deleted = openai.vector_stores.delete("vector_store_id")

puts(vector_store_deleted)
```

## Search

`vector_stores.search(vector_store_id, **kwargs) -> Page<VectorStoreSearchResponse>`

**post** `/vector_stores/{vector_store_id}/search`

Search a vector store for relevant chunks based on a query and file attributes filter.

### Parameters

- `vector_store_id: String`

- `query: String | Array[String]`

  A query string for a search

  - `String`

  - `Array[String]`

- `filters: ComparisonFilter | CompoundFilter`

  A filter to apply based on file attributes.

  - `class ComparisonFilter`

    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

    - `key: String`

      The key to compare against the value.

    - `type: :eq | :ne | :gt | 3 more`

      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

      - `eq`: equals
      - `ne`: not equal
      - `gt`: greater than
      - `gte`: greater than or equal
      - `lt`: less than
      - `lte`: less than or equal
      - `in`: in
      - `nin`: not in

      - `:eq`

      - `:ne`

      - `:gt`

      - `:gte`

      - `:lt`

      - `:lte`

    - `value: String | Float | bool | Array[String | Float]`

      The value to compare against the attribute key; supports string, number, or boolean types.

      - `String`

      - `Float`

      - `bool`

      - `Array[String | Float]`

        - `String`

        - `Float`

  - `class CompoundFilter`

    Combine multiple filters using `and` or `or`.

    - `filters: Array[ComparisonFilter | untyped]`

      Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

      - `class ComparisonFilter`

        A filter used to compare a specified attribute key to a given value using a defined comparison operation.

        - `key: String`

          The key to compare against the value.

        - `type: :eq | :ne | :gt | 3 more`

          Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

          - `eq`: equals
          - `ne`: not equal
          - `gt`: greater than
          - `gte`: greater than or equal
          - `lt`: less than
          - `lte`: less than or equal
          - `in`: in
          - `nin`: not in

          - `:eq`

          - `:ne`

          - `:gt`

          - `:gte`

          - `:lt`

          - `:lte`

        - `value: String | Float | bool | Array[String | Float]`

          The value to compare against the attribute key; supports string, number, or boolean types.

          - `String`

          - `Float`

          - `bool`

          - `Array[String | Float]`

            - `String`

            - `Float`

      - `untyped`

    - `type: :and | :or`

      Type of operation: `and` or `or`.

      - `:and`

      - `:or`

- `max_num_results: Integer`

  The maximum number of results to return. This number should be between 1 and 50 inclusive.

- `ranking_options: { ranker, score_threshold}`

  Ranking options for search.

  - `ranker: :none | :auto | :"default-2024-11-15"`

    Enable re-ranking; set to `none` to disable, which can help reduce latency.

    - `:none`

    - `:auto`

    - `:"default-2024-11-15"`

  - `score_threshold: Float`

- `rewrite_query: bool`

  Whether to rewrite the natural language query for vector search.

### Returns

- `class VectorStoreSearchResponse`

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `content: Array[{ text, type}]`

    Content chunks from the file.

    - `text: String`

      The text content returned from search.

    - `type: :text`

      The type of content.

      - `:text`

  - `file_id: String`

    The ID of the vector store file.

  - `filename: String`

    The name of the vector store file.

  - `score: Float`

    The similarity score for the result.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.vector_stores.search("vs_abc123", query: "string")

puts(page)
```

### Domain Types

### Auto File Chunking Strategy Param

- `class AutoFileChunkingStrategyParam`

  The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

  - `type: :auto`

    Always `auto`.

    - `:auto`

### File Chunking Strategy

- `FileChunkingStrategy = StaticFileChunkingStrategyObject | OtherFileChunkingStrategyObject`

  The strategy used to chunk the file.

  - `class StaticFileChunkingStrategyObject`

    - `static: StaticFileChunkingStrategy`

      - `chunk_overlap_tokens: Integer`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `max_chunk_size_tokens: Integer`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `type: :static`

      Always `static`.

      - `:static`

  - `class OtherFileChunkingStrategyObject`

    This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

    - `type: :other`

      Always `other`.

      - `:other`

### File Chunking Strategy Param

- `FileChunkingStrategyParam = AutoFileChunkingStrategyParam | StaticFileChunkingStrategyObjectParam`

  The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `class AutoFileChunkingStrategyParam`

    The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

    - `type: :auto`

      Always `auto`.

      - `:auto`

  - `class StaticFileChunkingStrategyObjectParam`

    Customize your own chunking strategy by setting chunk size and chunk overlap.

    - `static: StaticFileChunkingStrategy`

      - `chunk_overlap_tokens: Integer`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `max_chunk_size_tokens: Integer`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `type: :static`

      Always `static`.

      - `:static`

### Other File Chunking Strategy Object

- `class OtherFileChunkingStrategyObject`

  This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

  - `type: :other`

    Always `other`.

    - `:other`

### Static File Chunking Strategy

- `class StaticFileChunkingStrategy`

  - `chunk_overlap_tokens: Integer`

    The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.

  - `max_chunk_size_tokens: Integer`

    The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

### Static File Chunking Strategy Object

- `class StaticFileChunkingStrategyObject`

  - `static: StaticFileChunkingStrategy`

    - `chunk_overlap_tokens: Integer`

      The number of tokens that overlap between chunks. The default value is `400`.

      Note that the overlap must not exceed half of `max_chunk_size_tokens`.

    - `max_chunk_size_tokens: Integer`

      The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

  - `type: :static`

    Always `static`.

    - `:static`

### Static File Chunking Strategy Object Param

- `class StaticFileChunkingStrategyObjectParam`

  Customize your own chunking strategy by setting chunk size and chunk overlap.

  - `static: StaticFileChunkingStrategy`

    - `chunk_overlap_tokens: Integer`

      The number of tokens that overlap between chunks. The default value is `400`.

      Note that the overlap must not exceed half of `max_chunk_size_tokens`.

    - `max_chunk_size_tokens: Integer`

      The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

  - `type: :static`

    Always `static`.

    - `:static`

### Vector Store

- `class VectorStore`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that were cancelled.

    - `completed: Integer`

      The number of files that have been successfully processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `last_active_at: Integer`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the vector store.

  - `object: :vector_store`

    The object type, which is always `vector_store`.

    - `:vector_store`

  - `status: :expired | :in_progress | :completed`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `:expired`

    - `:in_progress`

    - `:completed`

  - `usage_bytes: Integer`

    The total number of bytes used by the files in the vector store.

  - `expires_after: { anchor, days}`

    The expiration policy for a vector store.

    - `anchor: :last_active_at`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `:last_active_at`

    - `days: Integer`

      The number of days after the anchor time that the vector store will expire.

  - `expires_at: Integer`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Vector Store Deleted

- `class VectorStoreDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"vector_store.deleted"`

    - `:"vector_store.deleted"`

## Files

### List

`vector_stores.files.list(vector_store_id, **kwargs) -> CursorPage<VectorStoreFile>`

**get** `/vector_stores/{vector_store_id}/files`

Returns a list of vector store files.

#### Parameters

- `vector_store_id: String`

- `after: String`

  A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- `before: String`

  A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

- `filter: :in_progress | :completed | :failed | :cancelled`

  Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

  - `:in_progress`

  - `:completed`

  - `:failed`

  - `:cancelled`

- `limit: Integer`

  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

  - `:asc`

  - `:desc`

#### Returns

- `class VectorStoreFile`

  A list of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `last_error: { code, message}`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `code: :server_error | :unsupported_file | :invalid_file`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `:server_error`

      - `:unsupported_file`

      - `:invalid_file`

    - `message: String`

      A human-readable description of the error.

  - `object: :"vector_store.file"`

    The object type, which is always `vector_store.file`.

    - `:"vector_store.file"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `usage_bytes: Integer`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject`

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

    - `class OtherFileChunkingStrategyObject`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `type: :other`

        Always `other`.

        - `:other`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.vector_stores.files.list("vector_store_id")

puts(page)
```

### Create

`vector_stores.files.create(vector_store_id, **kwargs) -> VectorStoreFile`

**post** `/vector_stores/{vector_store_id}/files`

Create a vector store file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

#### Parameters

- `vector_store_id: String`

- `file_id: String`

  A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

- `attributes: Hash[Symbol, String | Float | bool]`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard. Keys are strings
  with a maximum length of 64 characters. Values are strings with a maximum
  length of 512 characters, booleans, or numbers.

  - `String`

  - `Float`

  - `bool`

- `chunking_strategy: FileChunkingStrategyParam`

  The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `class AutoFileChunkingStrategyParam`

    The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

    - `type: :auto`

      Always `auto`.

      - `:auto`

  - `class StaticFileChunkingStrategyObjectParam`

    Customize your own chunking strategy by setting chunk size and chunk overlap.

    - `static: StaticFileChunkingStrategy`

      - `chunk_overlap_tokens: Integer`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `max_chunk_size_tokens: Integer`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `type: :static`

      Always `static`.

      - `:static`

#### Returns

- `class VectorStoreFile`

  A list of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `last_error: { code, message}`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `code: :server_error | :unsupported_file | :invalid_file`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `:server_error`

      - `:unsupported_file`

      - `:invalid_file`

    - `message: String`

      A human-readable description of the error.

  - `object: :"vector_store.file"`

    The object type, which is always `vector_store.file`.

    - `:"vector_store.file"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `usage_bytes: Integer`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject`

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

    - `class OtherFileChunkingStrategyObject`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `type: :other`

        Always `other`.

        - `:other`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file = openai.vector_stores.files.create("vs_abc123", file_id: "file_id")

puts(vector_store_file)
```

### Update

`vector_stores.files.update(file_id, **kwargs) -> VectorStoreFile`

**post** `/vector_stores/{vector_store_id}/files/{file_id}`

Update attributes on a vector store file.

#### Parameters

- `vector_store_id: String`

- `file_id: String`

- `attributes: Hash[Symbol, String | Float | bool]`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard. Keys are strings
  with a maximum length of 64 characters. Values are strings with a maximum
  length of 512 characters, booleans, or numbers.

  - `String`

  - `Float`

  - `bool`

#### Returns

- `class VectorStoreFile`

  A list of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `last_error: { code, message}`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `code: :server_error | :unsupported_file | :invalid_file`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `:server_error`

      - `:unsupported_file`

      - `:invalid_file`

    - `message: String`

      A human-readable description of the error.

  - `object: :"vector_store.file"`

    The object type, which is always `vector_store.file`.

    - `:"vector_store.file"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `usage_bytes: Integer`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject`

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

    - `class OtherFileChunkingStrategyObject`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `type: :other`

        Always `other`.

        - `:other`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file = openai.vector_stores.files.update(
  "file-abc123",
  vector_store_id: "vs_abc123",
  attributes: {foo: "string"}
)

puts(vector_store_file)
```

### Retrieve

`vector_stores.files.retrieve(file_id, **kwargs) -> VectorStoreFile`

**get** `/vector_stores/{vector_store_id}/files/{file_id}`

Retrieves a vector store file.

#### Parameters

- `vector_store_id: String`

- `file_id: String`

#### Returns

- `class VectorStoreFile`

  A list of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `last_error: { code, message}`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `code: :server_error | :unsupported_file | :invalid_file`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `:server_error`

      - `:unsupported_file`

      - `:invalid_file`

    - `message: String`

      A human-readable description of the error.

  - `object: :"vector_store.file"`

    The object type, which is always `vector_store.file`.

    - `:"vector_store.file"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `usage_bytes: Integer`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject`

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

    - `class OtherFileChunkingStrategyObject`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `type: :other`

        Always `other`.

        - `:other`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file = openai.vector_stores.files.retrieve("file-abc123", vector_store_id: "vs_abc123")

puts(vector_store_file)
```

### Delete

`vector_stores.files.delete(file_id, **kwargs) -> VectorStoreFileDeleted`

**delete** `/vector_stores/{vector_store_id}/files/{file_id}`

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

#### Parameters

- `vector_store_id: String`

- `file_id: String`

#### Returns

- `class VectorStoreFileDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"vector_store.file.deleted"`

    - `:"vector_store.file.deleted"`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file_deleted = openai.vector_stores.files.delete("file_id", vector_store_id: "vector_store_id")

puts(vector_store_file_deleted)
```

### Content

`vector_stores.files.content(file_id, **kwargs) -> Page<FileContentResponse>`

**get** `/vector_stores/{vector_store_id}/files/{file_id}/content`

Retrieve the parsed contents of a vector store file.

#### Parameters

- `vector_store_id: String`

- `file_id: String`

#### Returns

- `class FileContentResponse`

  - `text: String`

    The text content

  - `type: String`

    The content type (currently only `"text"`)

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.vector_stores.files.content("file-abc123", vector_store_id: "vs_abc123")

puts(page)
```

#### Domain Types

#### Vector Store File

- `class VectorStoreFile`

  A list of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `last_error: { code, message}`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `code: :server_error | :unsupported_file | :invalid_file`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `:server_error`

      - `:unsupported_file`

      - `:invalid_file`

    - `message: String`

      A human-readable description of the error.

  - `object: :"vector_store.file"`

    The object type, which is always `vector_store.file`.

    - `:"vector_store.file"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `usage_bytes: Integer`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject`

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

    - `class OtherFileChunkingStrategyObject`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `type: :other`

        Always `other`.

        - `:other`

#### Vector Store File Deleted

- `class VectorStoreFileDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: :"vector_store.file.deleted"`

    - `:"vector_store.file.deleted"`

## File Batches

### Create

`vector_stores.file_batches.create(vector_store_id, **kwargs) -> VectorStoreFileBatch`

**post** `/vector_stores/{vector_store_id}/file_batches`

Create a vector store file batch.

#### Parameters

- `vector_store_id: String`

- `attributes: Hash[Symbol, String | Float | bool]`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard. Keys are strings
  with a maximum length of 64 characters. Values are strings with a maximum
  length of 512 characters, booleans, or numbers.

  - `String`

  - `Float`

  - `bool`

- `chunking_strategy: FileChunkingStrategyParam`

  The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `class AutoFileChunkingStrategyParam`

    The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

    - `type: :auto`

      Always `auto`.

      - `:auto`

  - `class StaticFileChunkingStrategyObjectParam`

    Customize your own chunking strategy by setting chunk size and chunk overlap.

    - `static: StaticFileChunkingStrategy`

      - `chunk_overlap_tokens: Integer`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `max_chunk_size_tokens: Integer`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `type: :static`

      Always `static`.

      - `:static`

- `file_ids: Array[String]`

  A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.  If `attributes` or `chunking_strategy` are provided, they will be  applied to all files in the batch. The maximum batch size is 2000 files. Mutually exclusive with `files`.

- `files: Array[{ file_id, attributes, chunking_strategy}]`

  A list of objects that each include a `file_id` plus optional `attributes` or `chunking_strategy`. Use this when you need to override metadata for specific files. The global `attributes` or `chunking_strategy` will be ignored and must be specified for each file. The maximum batch size is 2000 files. Mutually exclusive with `file_ids`.

  - `file_id: String`

    A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategyParam`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

    - `class AutoFileChunkingStrategyParam`

      The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

      - `type: :auto`

        Always `auto`.

        - `:auto`

    - `class StaticFileChunkingStrategyObjectParam`

      Customize your own chunking strategy by setting chunk size and chunk overlap.

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

#### Returns

- `class VectorStoreFileBatch`

  A batch of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that where cancelled.

    - `completed: Integer`

      The number of files that have been processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `object: :"vector_store.files_batch"`

    The object type, which is always `vector_store.file_batch`.

    - `:"vector_store.files_batch"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file_batch = openai.vector_stores.file_batches.create("vs_abc123")

puts(vector_store_file_batch)
```

### Retrieve

`vector_stores.file_batches.retrieve(batch_id, **kwargs) -> VectorStoreFileBatch`

**get** `/vector_stores/{vector_store_id}/file_batches/{batch_id}`

Retrieves a vector store file batch.

#### Parameters

- `vector_store_id: String`

- `batch_id: String`

#### Returns

- `class VectorStoreFileBatch`

  A batch of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that where cancelled.

    - `completed: Integer`

      The number of files that have been processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `object: :"vector_store.files_batch"`

    The object type, which is always `vector_store.file_batch`.

    - `:"vector_store.files_batch"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file_batch = openai.vector_stores.file_batches.retrieve("vsfb_abc123", vector_store_id: "vs_abc123")

puts(vector_store_file_batch)
```

### Cancel

`vector_stores.file_batches.cancel(batch_id, **kwargs) -> VectorStoreFileBatch`

**post** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel`

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

#### Parameters

- `vector_store_id: String`

- `batch_id: String`

#### Returns

- `class VectorStoreFileBatch`

  A batch of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that where cancelled.

    - `completed: Integer`

      The number of files that have been processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `object: :"vector_store.files_batch"`

    The object type, which is always `vector_store.file_batch`.

    - `:"vector_store.files_batch"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vector_store_file_batch = openai.vector_stores.file_batches.cancel("batch_id", vector_store_id: "vector_store_id")

puts(vector_store_file_batch)
```

### List Files

`vector_stores.file_batches.list_files(batch_id, **kwargs) -> CursorPage<VectorStoreFile>`

**get** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/files`

Returns a list of vector store files in a batch.

#### Parameters

- `vector_store_id: String`

- `batch_id: String`

- `after: String`

  A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- `before: String`

  A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

- `filter: :in_progress | :completed | :failed | :cancelled`

  Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

  - `:in_progress`

  - `:completed`

  - `:failed`

  - `:cancelled`

- `limit: Integer`

  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

  - `:asc`

  - `:desc`

#### Returns

- `class VectorStoreFile`

  A list of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `last_error: { code, message}`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `code: :server_error | :unsupported_file | :invalid_file`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `:server_error`

      - `:unsupported_file`

      - `:invalid_file`

    - `message: String`

      A human-readable description of the error.

  - `object: :"vector_store.file"`

    The object type, which is always `vector_store.file`.

    - `:"vector_store.file"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `usage_bytes: Integer`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `attributes: Hash[Symbol, String | Float | bool]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `String`

    - `Float`

    - `bool`

  - `chunking_strategy: FileChunkingStrategy`

    The strategy used to chunk the file.

    - `class StaticFileChunkingStrategyObject`

      - `static: StaticFileChunkingStrategy`

        - `chunk_overlap_tokens: Integer`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `max_chunk_size_tokens: Integer`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `type: :static`

        Always `static`.

        - `:static`

    - `class OtherFileChunkingStrategyObject`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `type: :other`

        Always `other`.

        - `:other`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.vector_stores.file_batches.list_files("batch_id", vector_store_id: "vector_store_id")

puts(page)
```

#### Domain Types

#### Vector Store File Batch

- `class VectorStoreFileBatch`

  A batch of files attached to a vector store.

  - `id: String`

    The identifier, which can be referenced in API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `file_counts: { cancelled, completed, failed, 2 more}`

    - `cancelled: Integer`

      The number of files that where cancelled.

    - `completed: Integer`

      The number of files that have been processed.

    - `failed: Integer`

      The number of files that have failed to process.

    - `in_progress: Integer`

      The number of files that are currently being processed.

    - `total: Integer`

      The total number of files.

  - `object: :"vector_store.files_batch"`

    The object type, which is always `vector_store.file_batch`.

    - `:"vector_store.files_batch"`

  - `status: :in_progress | :completed | :cancelled | :failed`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `:in_progress`

    - `:completed`

    - `:cancelled`

    - `:failed`

  - `vector_store_id: String`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
