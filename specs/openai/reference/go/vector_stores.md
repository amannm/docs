# Vector Stores

## List

`client.VectorStores.List(ctx, query) (*CursorPage[VectorStore], error)`

**get** `/vector_stores`

Returns a list of vector stores.

### Parameters

- `query VectorStoreListParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Before param.Field[string]`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Order param.Field[VectorStoreListParamsOrder]`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `const VectorStoreListParamsOrderAsc VectorStoreListParamsOrder = "asc"`

    - `const VectorStoreListParamsOrderDesc VectorStoreListParamsOrder = "desc"`

### Returns

- `type VectorStore struct{…}`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts VectorStoreFileCounts`

    - `Cancelled int64`

      The number of files that were cancelled.

    - `Completed int64`

      The number of files that have been successfully processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `LastActiveAt int64`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name string`

    The name of the vector store.

  - `Object VectorStore`

    The object type, which is always `vector_store`.

    - `const VectorStoreVectorStore VectorStore = "vector_store"`

  - `Status VectorStoreStatus`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `const VectorStoreStatusExpired VectorStoreStatus = "expired"`

    - `const VectorStoreStatusInProgress VectorStoreStatus = "in_progress"`

    - `const VectorStoreStatusCompleted VectorStoreStatus = "completed"`

  - `UsageBytes int64`

    The total number of bytes used by the files in the vector store.

  - `ExpiresAfter VectorStoreExpiresAfter`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the vector store will expire.

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
  page, err := client.VectorStores.List(context.TODO(), openai.VectorStoreListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Create

`client.VectorStores.New(ctx, body) (*VectorStore, error)`

**post** `/vector_stores`

Create a vector store.

### Parameters

- `body VectorStoreNewParams`

  - `ChunkingStrategy param.Field[FileChunkingStrategyParamUnionResp]`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `Description param.Field[string]`

    A description for the vector store. Can be used to describe the vector store's purpose.

  - `ExpiresAfter param.Field[VectorStoreNewParamsExpiresAfter]`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `FileIDs param.Field[[]string]`

    A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

  - `Metadata param.Field[Metadata]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name param.Field[string]`

    The name of the vector store.

### Returns

- `type VectorStore struct{…}`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts VectorStoreFileCounts`

    - `Cancelled int64`

      The number of files that were cancelled.

    - `Completed int64`

      The number of files that have been successfully processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `LastActiveAt int64`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name string`

    The name of the vector store.

  - `Object VectorStore`

    The object type, which is always `vector_store`.

    - `const VectorStoreVectorStore VectorStore = "vector_store"`

  - `Status VectorStoreStatus`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `const VectorStoreStatusExpired VectorStoreStatus = "expired"`

    - `const VectorStoreStatusInProgress VectorStoreStatus = "in_progress"`

    - `const VectorStoreStatusCompleted VectorStoreStatus = "completed"`

  - `UsageBytes int64`

    The total number of bytes used by the files in the vector store.

  - `ExpiresAfter VectorStoreExpiresAfter`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the vector store will expire.

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
  vectorStore, err := client.VectorStores.New(context.TODO(), openai.VectorStoreNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStore.ID)
}
```

## Retrieve

`client.VectorStores.Get(ctx, vectorStoreID) (*VectorStore, error)`

**get** `/vector_stores/{vector_store_id}`

Retrieves a vector store.

### Parameters

- `vectorStoreID string`

### Returns

- `type VectorStore struct{…}`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts VectorStoreFileCounts`

    - `Cancelled int64`

      The number of files that were cancelled.

    - `Completed int64`

      The number of files that have been successfully processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `LastActiveAt int64`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name string`

    The name of the vector store.

  - `Object VectorStore`

    The object type, which is always `vector_store`.

    - `const VectorStoreVectorStore VectorStore = "vector_store"`

  - `Status VectorStoreStatus`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `const VectorStoreStatusExpired VectorStoreStatus = "expired"`

    - `const VectorStoreStatusInProgress VectorStoreStatus = "in_progress"`

    - `const VectorStoreStatusCompleted VectorStoreStatus = "completed"`

  - `UsageBytes int64`

    The total number of bytes used by the files in the vector store.

  - `ExpiresAfter VectorStoreExpiresAfter`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the vector store will expire.

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
  vectorStore, err := client.VectorStores.Get(context.TODO(), "vector_store_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStore.ID)
}
```

## Update

`client.VectorStores.Update(ctx, vectorStoreID, body) (*VectorStore, error)`

**post** `/vector_stores/{vector_store_id}`

Modifies a vector store.

### Parameters

- `vectorStoreID string`

- `body VectorStoreUpdateParams`

  - `ExpiresAfter param.Field[VectorStoreUpdateParamsExpiresAfter]`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `Metadata param.Field[Metadata]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name param.Field[string]`

    The name of the vector store.

### Returns

- `type VectorStore struct{…}`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts VectorStoreFileCounts`

    - `Cancelled int64`

      The number of files that were cancelled.

    - `Completed int64`

      The number of files that have been successfully processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `LastActiveAt int64`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name string`

    The name of the vector store.

  - `Object VectorStore`

    The object type, which is always `vector_store`.

    - `const VectorStoreVectorStore VectorStore = "vector_store"`

  - `Status VectorStoreStatus`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `const VectorStoreStatusExpired VectorStoreStatus = "expired"`

    - `const VectorStoreStatusInProgress VectorStoreStatus = "in_progress"`

    - `const VectorStoreStatusCompleted VectorStoreStatus = "completed"`

  - `UsageBytes int64`

    The total number of bytes used by the files in the vector store.

  - `ExpiresAfter VectorStoreExpiresAfter`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the vector store will expire.

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
  vectorStore, err := client.VectorStores.Update(
    context.TODO(),
    "vector_store_id",
    openai.VectorStoreUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStore.ID)
}
```

## Delete

`client.VectorStores.Delete(ctx, vectorStoreID) (*VectorStoreDeleted, error)`

**delete** `/vector_stores/{vector_store_id}`

Delete a vector store.

### Parameters

- `vectorStoreID string`

### Returns

- `type VectorStoreDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object VectorStoreDeleted`

    - `const VectorStoreDeletedVectorStoreDeleted VectorStoreDeleted = "vector_store.deleted"`

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
  vectorStoreDeleted, err := client.VectorStores.Delete(context.TODO(), "vector_store_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreDeleted.ID)
}
```

## Search

`client.VectorStores.Search(ctx, vectorStoreID, body) (*Page[VectorStoreSearchResponse], error)`

**post** `/vector_stores/{vector_store_id}/search`

Search a vector store for relevant chunks based on a query and file attributes filter.

### Parameters

- `vectorStoreID string`

- `body VectorStoreSearchParams`

  - `Query param.Field[VectorStoreSearchParamsQueryUnion]`

    A query string for a search

    - `string`

    - `type VectorStoreSearchParamsQueryArray []string`

  - `Filters param.Field[VectorStoreSearchParamsFiltersUnion]`

    A filter to apply based on file attributes.

    - `type ComparisonFilter struct{…}`

      A filter used to compare a specified attribute key to a given value using a defined comparison operation.

      - `Key string`

        The key to compare against the value.

      - `Type ComparisonFilterType`

        Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

        - `eq`: equals
        - `ne`: not equal
        - `gt`: greater than
        - `gte`: greater than or equal
        - `lt`: less than
        - `lte`: less than or equal
        - `in`: in
        - `nin`: not in

        - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

        - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

        - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

        - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

        - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

        - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

      - `Value ComparisonFilterValueUnion`

        The value to compare against the attribute key; supports string, number, or boolean types.

        - `string`

        - `float64`

        - `bool`

        - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

          - `string`

          - `float64`

    - `type CompoundFilter struct{…}`

      Combine multiple filters using `and` or `or`.

      - `Filters []ComparisonFilter`

        Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

        - `type ComparisonFilter struct{…}`

          A filter used to compare a specified attribute key to a given value using a defined comparison operation.

          - `Key string`

            The key to compare against the value.

          - `Type ComparisonFilterType`

            Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

            - `eq`: equals
            - `ne`: not equal
            - `gt`: greater than
            - `gte`: greater than or equal
            - `lt`: less than
            - `lte`: less than or equal
            - `in`: in
            - `nin`: not in

            - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

            - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

            - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

            - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

            - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

            - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

          - `Value ComparisonFilterValueUnion`

            The value to compare against the attribute key; supports string, number, or boolean types.

            - `string`

            - `float64`

            - `bool`

            - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

              - `string`

              - `float64`

      - `Type CompoundFilterType`

        Type of operation: `and` or `or`.

        - `const CompoundFilterTypeAnd CompoundFilterType = "and"`

        - `const CompoundFilterTypeOr CompoundFilterType = "or"`

  - `MaxNumResults param.Field[int64]`

    The maximum number of results to return. This number should be between 1 and 50 inclusive.

  - `RankingOptions param.Field[VectorStoreSearchParamsRankingOptions]`

    Ranking options for search.

    - `Ranker string`

      Enable re-ranking; set to `none` to disable, which can help reduce latency.

      - `const VectorStoreSearchParamsRankingOptionsRankerNone VectorStoreSearchParamsRankingOptionsRanker = "none"`

      - `const VectorStoreSearchParamsRankingOptionsRankerAuto VectorStoreSearchParamsRankingOptionsRanker = "auto"`

      - `const VectorStoreSearchParamsRankingOptionsRankerDefault2024_11_15 VectorStoreSearchParamsRankingOptionsRanker = "default-2024-11-15"`

    - `ScoreThreshold float64`

  - `RewriteQuery param.Field[bool]`

    Whether to rewrite the natural language query for vector search.

### Returns

- `type VectorStoreSearchResponse struct{…}`

  - `Attributes map[string, VectorStoreSearchResponseAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `Content []VectorStoreSearchResponseContent`

    Content chunks from the file.

    - `Text string`

      The text content returned from search.

    - `Type string`

      The type of content.

      - `const VectorStoreSearchResponseContentTypeText VectorStoreSearchResponseContentType = "text"`

  - `FileID string`

    The ID of the vector store file.

  - `Filename string`

    The name of the vector store file.

  - `Score float64`

    The similarity score for the result.

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
  page, err := client.VectorStores.Search(
    context.TODO(),
    "vs_abc123",
    openai.VectorStoreSearchParams{
      Query: openai.VectorStoreSearchParamsQueryUnion{
        OfString: openai.String("string"),
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Domain Types

### Auto File Chunking Strategy Param

- `type AutoFileChunkingStrategyParamResp struct{…}`

  The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

  - `Type Auto`

    Always `auto`.

    - `const AutoAuto Auto = "auto"`

### File Chunking Strategy

- `type FileChunkingStrategyUnion interface{…}`

  The strategy used to chunk the file.

  - `type StaticFileChunkingStrategyObject struct{…}`

    - `Static StaticFileChunkingStrategy`

      - `ChunkOverlapTokens int64`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `MaxChunkSizeTokens int64`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `Type Static`

      Always `static`.

      - `const StaticStatic Static = "static"`

  - `type OtherFileChunkingStrategyObject struct{…}`

    This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

    - `Type Other`

      Always `other`.

      - `const OtherOther Other = "other"`

### File Chunking Strategy Param

- `type FileChunkingStrategyParamUnionResp interface{…}`

  The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `type AutoFileChunkingStrategyParamResp struct{…}`

    The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

    - `Type Auto`

      Always `auto`.

      - `const AutoAuto Auto = "auto"`

  - `type StaticFileChunkingStrategyObjectParamResp struct{…}`

    Customize your own chunking strategy by setting chunk size and chunk overlap.

    - `Static StaticFileChunkingStrategy`

      - `ChunkOverlapTokens int64`

        The number of tokens that overlap between chunks. The default value is `400`.

        Note that the overlap must not exceed half of `max_chunk_size_tokens`.

      - `MaxChunkSizeTokens int64`

        The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

    - `Type Static`

      Always `static`.

      - `const StaticStatic Static = "static"`

### Other File Chunking Strategy Object

- `type OtherFileChunkingStrategyObject struct{…}`

  This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

  - `Type Other`

    Always `other`.

    - `const OtherOther Other = "other"`

### Static File Chunking Strategy

- `type StaticFileChunkingStrategy struct{…}`

  - `ChunkOverlapTokens int64`

    The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.

  - `MaxChunkSizeTokens int64`

    The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

### Static File Chunking Strategy Object

- `type StaticFileChunkingStrategyObject struct{…}`

  - `Static StaticFileChunkingStrategy`

    - `ChunkOverlapTokens int64`

      The number of tokens that overlap between chunks. The default value is `400`.

      Note that the overlap must not exceed half of `max_chunk_size_tokens`.

    - `MaxChunkSizeTokens int64`

      The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

  - `Type Static`

    Always `static`.

    - `const StaticStatic Static = "static"`

### Static File Chunking Strategy Object Param

- `type StaticFileChunkingStrategyObjectParamResp struct{…}`

  Customize your own chunking strategy by setting chunk size and chunk overlap.

  - `Static StaticFileChunkingStrategy`

    - `ChunkOverlapTokens int64`

      The number of tokens that overlap between chunks. The default value is `400`.

      Note that the overlap must not exceed half of `max_chunk_size_tokens`.

    - `MaxChunkSizeTokens int64`

      The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

  - `Type Static`

    Always `static`.

    - `const StaticStatic Static = "static"`

### Vector Store

- `type VectorStore struct{…}`

  A vector store is a collection of processed files can be used by the `file_search` tool.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store was created.

  - `FileCounts VectorStoreFileCounts`

    - `Cancelled int64`

      The number of files that were cancelled.

    - `Completed int64`

      The number of files that have been successfully processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `LastActiveAt int64`

    The Unix timestamp (in seconds) for when the vector store was last active.

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Name string`

    The name of the vector store.

  - `Object VectorStore`

    The object type, which is always `vector_store`.

    - `const VectorStoreVectorStore VectorStore = "vector_store"`

  - `Status VectorStoreStatus`

    The status of the vector store, which can be either `expired`, `in_progress`, or `completed`. A status of `completed` indicates that the vector store is ready for use.

    - `const VectorStoreStatusExpired VectorStoreStatus = "expired"`

    - `const VectorStoreStatusInProgress VectorStoreStatus = "in_progress"`

    - `const VectorStoreStatusCompleted VectorStoreStatus = "completed"`

  - `UsageBytes int64`

    The total number of bytes used by the files in the vector store.

  - `ExpiresAfter VectorStoreExpiresAfter`

    The expiration policy for a vector store.

    - `Anchor LastActiveAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `last_active_at`.

      - `const LastActiveAtLastActiveAt LastActiveAt = "last_active_at"`

    - `Days int64`

      The number of days after the anchor time that the vector store will expire.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the vector store will expire.

### Vector Store Deleted

- `type VectorStoreDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object VectorStoreDeleted`

    - `const VectorStoreDeletedVectorStoreDeleted VectorStoreDeleted = "vector_store.deleted"`

## Files

### List

`client.VectorStores.Files.List(ctx, vectorStoreID, query) (*CursorPage[VectorStoreFile], error)`

**get** `/vector_stores/{vector_store_id}/files`

Returns a list of vector store files.

#### Parameters

- `vectorStoreID string`

- `query VectorStoreFileListParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Before param.Field[string]`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Filter param.Field[VectorStoreFileListParamsFilter]`

    Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

    - `const VectorStoreFileListParamsFilterInProgress VectorStoreFileListParamsFilter = "in_progress"`

    - `const VectorStoreFileListParamsFilterCompleted VectorStoreFileListParamsFilter = "completed"`

    - `const VectorStoreFileListParamsFilterFailed VectorStoreFileListParamsFilter = "failed"`

    - `const VectorStoreFileListParamsFilterCancelled VectorStoreFileListParamsFilter = "cancelled"`

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Order param.Field[VectorStoreFileListParamsOrder]`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `const VectorStoreFileListParamsOrderAsc VectorStoreFileListParamsOrder = "asc"`

    - `const VectorStoreFileListParamsOrderDesc VectorStoreFileListParamsOrder = "desc"`

#### Returns

- `type VectorStoreFile struct{…}`

  A list of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `LastError VectorStoreFileLastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code string`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server_error"`

      - `const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported_file"`

      - `const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid_file"`

    - `Message string`

      A human-readable description of the error.

  - `Object VectorStoreFile`

    The object type, which is always `vector_store.file`.

    - `const VectorStoreFileVectorStoreFile VectorStoreFile = "vector_store.file"`

  - `Status VectorStoreFileStatus`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in_progress"`

    - `const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"`

    - `const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"`

    - `const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"`

  - `UsageBytes int64`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Attributes map[string, VectorStoreFileAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy FileChunkingStrategyUnion`

    The strategy used to chunk the file.

    - `type StaticFileChunkingStrategyObject struct{…}`

      - `Static StaticFileChunkingStrategy`

        - `ChunkOverlapTokens int64`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `MaxChunkSizeTokens int64`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `Type Static`

        Always `static`.

        - `const StaticStatic Static = "static"`

    - `type OtherFileChunkingStrategyObject struct{…}`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `Type Other`

        Always `other`.

        - `const OtherOther Other = "other"`

#### Example

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
  page, err := client.VectorStores.Files.List(
    context.TODO(),
    "vector_store_id",
    openai.VectorStoreFileListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Create

`client.VectorStores.Files.New(ctx, vectorStoreID, body) (*VectorStoreFile, error)`

**post** `/vector_stores/{vector_store_id}/files`

Create a vector store file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

#### Parameters

- `vectorStoreID string`

- `body VectorStoreFileNewParams`

  - `FileID param.Field[string]`

    A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

  - `Attributes param.Field[map[string, VectorStoreFileNewParamsAttributeUnion]]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy param.Field[FileChunkingStrategyParamUnionResp]`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

#### Returns

- `type VectorStoreFile struct{…}`

  A list of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `LastError VectorStoreFileLastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code string`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server_error"`

      - `const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported_file"`

      - `const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid_file"`

    - `Message string`

      A human-readable description of the error.

  - `Object VectorStoreFile`

    The object type, which is always `vector_store.file`.

    - `const VectorStoreFileVectorStoreFile VectorStoreFile = "vector_store.file"`

  - `Status VectorStoreFileStatus`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in_progress"`

    - `const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"`

    - `const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"`

    - `const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"`

  - `UsageBytes int64`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Attributes map[string, VectorStoreFileAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy FileChunkingStrategyUnion`

    The strategy used to chunk the file.

    - `type StaticFileChunkingStrategyObject struct{…}`

      - `Static StaticFileChunkingStrategy`

        - `ChunkOverlapTokens int64`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `MaxChunkSizeTokens int64`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `Type Static`

        Always `static`.

        - `const StaticStatic Static = "static"`

    - `type OtherFileChunkingStrategyObject struct{…}`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `Type Other`

        Always `other`.

        - `const OtherOther Other = "other"`

#### Example

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
  vectorStoreFile, err := client.VectorStores.Files.New(
    context.TODO(),
    "vs_abc123",
    openai.VectorStoreFileNewParams{
      FileID: "file_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFile.ID)
}
```

### Update

`client.VectorStores.Files.Update(ctx, vectorStoreID, fileID, body) (*VectorStoreFile, error)`

**post** `/vector_stores/{vector_store_id}/files/{file_id}`

Update attributes on a vector store file.

#### Parameters

- `vectorStoreID string`

- `fileID string`

- `body VectorStoreFileUpdateParams`

  - `Attributes param.Field[map[string, VectorStoreFileUpdateParamsAttributeUnion]]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

#### Returns

- `type VectorStoreFile struct{…}`

  A list of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `LastError VectorStoreFileLastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code string`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server_error"`

      - `const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported_file"`

      - `const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid_file"`

    - `Message string`

      A human-readable description of the error.

  - `Object VectorStoreFile`

    The object type, which is always `vector_store.file`.

    - `const VectorStoreFileVectorStoreFile VectorStoreFile = "vector_store.file"`

  - `Status VectorStoreFileStatus`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in_progress"`

    - `const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"`

    - `const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"`

    - `const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"`

  - `UsageBytes int64`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Attributes map[string, VectorStoreFileAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy FileChunkingStrategyUnion`

    The strategy used to chunk the file.

    - `type StaticFileChunkingStrategyObject struct{…}`

      - `Static StaticFileChunkingStrategy`

        - `ChunkOverlapTokens int64`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `MaxChunkSizeTokens int64`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `Type Static`

        Always `static`.

        - `const StaticStatic Static = "static"`

    - `type OtherFileChunkingStrategyObject struct{…}`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `Type Other`

        Always `other`.

        - `const OtherOther Other = "other"`

#### Example

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
  vectorStoreFile, err := client.VectorStores.Files.Update(
    context.TODO(),
    "vs_abc123",
    "file-abc123",
    openai.VectorStoreFileUpdateParams{
      Attributes: map[string]openai.VectorStoreFileUpdateParamsAttributeUnion{
      "foo": openai.VectorStoreFileUpdateParamsAttributeUnion{
        OfString: openai.String("string"),
      },
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFile.ID)
}
```

### Retrieve

`client.VectorStores.Files.Get(ctx, vectorStoreID, fileID) (*VectorStoreFile, error)`

**get** `/vector_stores/{vector_store_id}/files/{file_id}`

Retrieves a vector store file.

#### Parameters

- `vectorStoreID string`

- `fileID string`

#### Returns

- `type VectorStoreFile struct{…}`

  A list of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `LastError VectorStoreFileLastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code string`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server_error"`

      - `const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported_file"`

      - `const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid_file"`

    - `Message string`

      A human-readable description of the error.

  - `Object VectorStoreFile`

    The object type, which is always `vector_store.file`.

    - `const VectorStoreFileVectorStoreFile VectorStoreFile = "vector_store.file"`

  - `Status VectorStoreFileStatus`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in_progress"`

    - `const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"`

    - `const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"`

    - `const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"`

  - `UsageBytes int64`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Attributes map[string, VectorStoreFileAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy FileChunkingStrategyUnion`

    The strategy used to chunk the file.

    - `type StaticFileChunkingStrategyObject struct{…}`

      - `Static StaticFileChunkingStrategy`

        - `ChunkOverlapTokens int64`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `MaxChunkSizeTokens int64`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `Type Static`

        Always `static`.

        - `const StaticStatic Static = "static"`

    - `type OtherFileChunkingStrategyObject struct{…}`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `Type Other`

        Always `other`.

        - `const OtherOther Other = "other"`

#### Example

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
  vectorStoreFile, err := client.VectorStores.Files.Get(
    context.TODO(),
    "vs_abc123",
    "file-abc123",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFile.ID)
}
```

### Delete

`client.VectorStores.Files.Delete(ctx, vectorStoreID, fileID) (*VectorStoreFileDeleted, error)`

**delete** `/vector_stores/{vector_store_id}/files/{file_id}`

Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

#### Parameters

- `vectorStoreID string`

- `fileID string`

#### Returns

- `type VectorStoreFileDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object VectorStoreFileDeleted`

    - `const VectorStoreFileDeletedVectorStoreFileDeleted VectorStoreFileDeleted = "vector_store.file.deleted"`

#### Example

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
  vectorStoreFileDeleted, err := client.VectorStores.Files.Delete(
    context.TODO(),
    "vector_store_id",
    "file_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFileDeleted.ID)
}
```

### Content

`client.VectorStores.Files.Content(ctx, vectorStoreID, fileID) (*Page[VectorStoreFileContentResponse], error)`

**get** `/vector_stores/{vector_store_id}/files/{file_id}/content`

Retrieve the parsed contents of a vector store file.

#### Parameters

- `vectorStoreID string`

- `fileID string`

#### Returns

- `type VectorStoreFileContentResponse struct{…}`

  - `Text string`

    The text content

  - `Type string`

    The content type (currently only `"text"`)

#### Example

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
  page, err := client.VectorStores.Files.Content(
    context.TODO(),
    "vs_abc123",
    "file-abc123",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Domain Types

#### Vector Store File

- `type VectorStoreFile struct{…}`

  A list of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `LastError VectorStoreFileLastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code string`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server_error"`

      - `const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported_file"`

      - `const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid_file"`

    - `Message string`

      A human-readable description of the error.

  - `Object VectorStoreFile`

    The object type, which is always `vector_store.file`.

    - `const VectorStoreFileVectorStoreFile VectorStoreFile = "vector_store.file"`

  - `Status VectorStoreFileStatus`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in_progress"`

    - `const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"`

    - `const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"`

    - `const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"`

  - `UsageBytes int64`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Attributes map[string, VectorStoreFileAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy FileChunkingStrategyUnion`

    The strategy used to chunk the file.

    - `type StaticFileChunkingStrategyObject struct{…}`

      - `Static StaticFileChunkingStrategy`

        - `ChunkOverlapTokens int64`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `MaxChunkSizeTokens int64`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `Type Static`

        Always `static`.

        - `const StaticStatic Static = "static"`

    - `type OtherFileChunkingStrategyObject struct{…}`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `Type Other`

        Always `other`.

        - `const OtherOther Other = "other"`

#### Vector Store File Deleted

- `type VectorStoreFileDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object VectorStoreFileDeleted`

    - `const VectorStoreFileDeletedVectorStoreFileDeleted VectorStoreFileDeleted = "vector_store.file.deleted"`

## File Batches

### Create

`client.VectorStores.FileBatches.New(ctx, vectorStoreID, body) (*VectorStoreFileBatch, error)`

**post** `/vector_stores/{vector_store_id}/file_batches`

Create a vector store file batch.

#### Parameters

- `vectorStoreID string`

- `body VectorStoreFileBatchNewParams`

  - `Attributes param.Field[map[string, VectorStoreFileBatchNewParamsAttributeUnion]]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy param.Field[FileChunkingStrategyParamUnionResp]`

    The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

  - `FileIDs param.Field[[]string]`

    A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.  If `attributes` or `chunking_strategy` are provided, they will be  applied to all files in the batch. The maximum batch size is 2000 files. Mutually exclusive with `files`.

  - `Files param.Field[[]VectorStoreFileBatchNewParamsFile]`

    A list of objects that each include a `file_id` plus optional `attributes` or `chunking_strategy`. Use this when you need to override metadata for specific files. The global `attributes` or `chunking_strategy` will be ignored and must be specified for each file. The maximum batch size is 2000 files. Mutually exclusive with `file_ids`.

    - `FileID string`

      A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

    - `Attributes map[string, VectorStoreFileBatchNewParamsFileAttributeUnion]`

      Set of 16 key-value pairs that can be attached to an object. This can be
      useful for storing additional information about the object in a structured
      format, and querying for objects via API or the dashboard. Keys are strings
      with a maximum length of 64 characters. Values are strings with a maximum
      length of 512 characters, booleans, or numbers.

      - `string`

      - `float64`

      - `bool`

    - `ChunkingStrategy FileChunkingStrategyParamUnionResp`

      The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

      - `type AutoFileChunkingStrategyParamResp struct{…}`

        The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

        - `Type Auto`

          Always `auto`.

          - `const AutoAuto Auto = "auto"`

      - `type StaticFileChunkingStrategyObjectParamResp struct{…}`

        Customize your own chunking strategy by setting chunk size and chunk overlap.

        - `Static StaticFileChunkingStrategy`

          - `ChunkOverlapTokens int64`

            The number of tokens that overlap between chunks. The default value is `400`.

            Note that the overlap must not exceed half of `max_chunk_size_tokens`.

          - `MaxChunkSizeTokens int64`

            The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

        - `Type Static`

          Always `static`.

          - `const StaticStatic Static = "static"`

#### Returns

- `type VectorStoreFileBatch struct{…}`

  A batch of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts VectorStoreFileBatchFileCounts`

    - `Cancelled int64`

      The number of files that where cancelled.

    - `Completed int64`

      The number of files that have been processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `Object VectorStoreFilesBatch`

    The object type, which is always `vector_store.file_batch`.

    - `const VectorStoreFilesBatchVectorStoreFilesBatch VectorStoreFilesBatch = "vector_store.files_batch"`

  - `Status VectorStoreFileBatchStatus`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `const VectorStoreFileBatchStatusInProgress VectorStoreFileBatchStatus = "in_progress"`

    - `const VectorStoreFileBatchStatusCompleted VectorStoreFileBatchStatus = "completed"`

    - `const VectorStoreFileBatchStatusCancelled VectorStoreFileBatchStatus = "cancelled"`

    - `const VectorStoreFileBatchStatusFailed VectorStoreFileBatchStatus = "failed"`

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

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
  vectorStoreFileBatch, err := client.VectorStores.FileBatches.New(
    context.TODO(),
    "vs_abc123",
    openai.VectorStoreFileBatchNewParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFileBatch.ID)
}
```

### Retrieve

`client.VectorStores.FileBatches.Get(ctx, vectorStoreID, batchID) (*VectorStoreFileBatch, error)`

**get** `/vector_stores/{vector_store_id}/file_batches/{batch_id}`

Retrieves a vector store file batch.

#### Parameters

- `vectorStoreID string`

- `batchID string`

#### Returns

- `type VectorStoreFileBatch struct{…}`

  A batch of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts VectorStoreFileBatchFileCounts`

    - `Cancelled int64`

      The number of files that where cancelled.

    - `Completed int64`

      The number of files that have been processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `Object VectorStoreFilesBatch`

    The object type, which is always `vector_store.file_batch`.

    - `const VectorStoreFilesBatchVectorStoreFilesBatch VectorStoreFilesBatch = "vector_store.files_batch"`

  - `Status VectorStoreFileBatchStatus`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `const VectorStoreFileBatchStatusInProgress VectorStoreFileBatchStatus = "in_progress"`

    - `const VectorStoreFileBatchStatusCompleted VectorStoreFileBatchStatus = "completed"`

    - `const VectorStoreFileBatchStatusCancelled VectorStoreFileBatchStatus = "cancelled"`

    - `const VectorStoreFileBatchStatusFailed VectorStoreFileBatchStatus = "failed"`

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

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
  vectorStoreFileBatch, err := client.VectorStores.FileBatches.Get(
    context.TODO(),
    "vs_abc123",
    "vsfb_abc123",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFileBatch.ID)
}
```

### Cancel

`client.VectorStores.FileBatches.Cancel(ctx, vectorStoreID, batchID) (*VectorStoreFileBatch, error)`

**post** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel`

Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

#### Parameters

- `vectorStoreID string`

- `batchID string`

#### Returns

- `type VectorStoreFileBatch struct{…}`

  A batch of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts VectorStoreFileBatchFileCounts`

    - `Cancelled int64`

      The number of files that where cancelled.

    - `Completed int64`

      The number of files that have been processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `Object VectorStoreFilesBatch`

    The object type, which is always `vector_store.file_batch`.

    - `const VectorStoreFilesBatchVectorStoreFilesBatch VectorStoreFilesBatch = "vector_store.files_batch"`

  - `Status VectorStoreFileBatchStatus`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `const VectorStoreFileBatchStatusInProgress VectorStoreFileBatchStatus = "in_progress"`

    - `const VectorStoreFileBatchStatusCompleted VectorStoreFileBatchStatus = "completed"`

    - `const VectorStoreFileBatchStatusCancelled VectorStoreFileBatchStatus = "cancelled"`

    - `const VectorStoreFileBatchStatusFailed VectorStoreFileBatchStatus = "failed"`

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

#### Example

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
  vectorStoreFileBatch, err := client.VectorStores.FileBatches.Cancel(
    context.TODO(),
    "vector_store_id",
    "batch_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", vectorStoreFileBatch.ID)
}
```

### List Files

`client.VectorStores.FileBatches.ListFiles(ctx, vectorStoreID, batchID, query) (*CursorPage[VectorStoreFile], error)`

**get** `/vector_stores/{vector_store_id}/file_batches/{batch_id}/files`

Returns a list of vector store files in a batch.

#### Parameters

- `vectorStoreID string`

- `batchID string`

- `query VectorStoreFileBatchListFilesParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Before param.Field[string]`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Filter param.Field[VectorStoreFileBatchListFilesParamsFilter]`

    Filter by file status. One of `in_progress`, `completed`, `failed`, `cancelled`.

    - `const VectorStoreFileBatchListFilesParamsFilterInProgress VectorStoreFileBatchListFilesParamsFilter = "in_progress"`

    - `const VectorStoreFileBatchListFilesParamsFilterCompleted VectorStoreFileBatchListFilesParamsFilter = "completed"`

    - `const VectorStoreFileBatchListFilesParamsFilterFailed VectorStoreFileBatchListFilesParamsFilter = "failed"`

    - `const VectorStoreFileBatchListFilesParamsFilterCancelled VectorStoreFileBatchListFilesParamsFilter = "cancelled"`

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Order param.Field[VectorStoreFileBatchListFilesParamsOrder]`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `const VectorStoreFileBatchListFilesParamsOrderAsc VectorStoreFileBatchListFilesParamsOrder = "asc"`

    - `const VectorStoreFileBatchListFilesParamsOrderDesc VectorStoreFileBatchListFilesParamsOrder = "desc"`

#### Returns

- `type VectorStoreFile struct{…}`

  A list of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store file was created.

  - `LastError VectorStoreFileLastError`

    The last error associated with this vector store file. Will be `null` if there are no errors.

    - `Code string`

      One of `server_error`, `unsupported_file`, or `invalid_file`.

      - `const VectorStoreFileLastErrorCodeServerError VectorStoreFileLastErrorCode = "server_error"`

      - `const VectorStoreFileLastErrorCodeUnsupportedFile VectorStoreFileLastErrorCode = "unsupported_file"`

      - `const VectorStoreFileLastErrorCodeInvalidFile VectorStoreFileLastErrorCode = "invalid_file"`

    - `Message string`

      A human-readable description of the error.

  - `Object VectorStoreFile`

    The object type, which is always `vector_store.file`.

    - `const VectorStoreFileVectorStoreFile VectorStoreFile = "vector_store.file"`

  - `Status VectorStoreFileStatus`

    The status of the vector store file, which can be either `in_progress`, `completed`, `cancelled`, or `failed`. The status `completed` indicates that the vector store file is ready for use.

    - `const VectorStoreFileStatusInProgress VectorStoreFileStatus = "in_progress"`

    - `const VectorStoreFileStatusCompleted VectorStoreFileStatus = "completed"`

    - `const VectorStoreFileStatusCancelled VectorStoreFileStatus = "cancelled"`

    - `const VectorStoreFileStatusFailed VectorStoreFileStatus = "failed"`

  - `UsageBytes int64`

    The total vector store usage in bytes. Note that this may be different from the original file size.

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

  - `Attributes map[string, VectorStoreFileAttributeUnion]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard. Keys are strings
    with a maximum length of 64 characters. Values are strings with a maximum
    length of 512 characters, booleans, or numbers.

    - `string`

    - `float64`

    - `bool`

  - `ChunkingStrategy FileChunkingStrategyUnion`

    The strategy used to chunk the file.

    - `type StaticFileChunkingStrategyObject struct{…}`

      - `Static StaticFileChunkingStrategy`

        - `ChunkOverlapTokens int64`

          The number of tokens that overlap between chunks. The default value is `400`.

          Note that the overlap must not exceed half of `max_chunk_size_tokens`.

        - `MaxChunkSizeTokens int64`

          The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

      - `Type Static`

        Always `static`.

        - `const StaticStatic Static = "static"`

    - `type OtherFileChunkingStrategyObject struct{…}`

      This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.

      - `Type Other`

        Always `other`.

        - `const OtherOther Other = "other"`

#### Example

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
  page, err := client.VectorStores.FileBatches.ListFiles(
    context.TODO(),
    "vector_store_id",
    "batch_id",
    openai.VectorStoreFileBatchListFilesParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Domain Types

#### Vector Store File Batch

- `type VectorStoreFileBatch struct{…}`

  A batch of files attached to a vector store.

  - `ID string`

    The identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the vector store files batch was created.

  - `FileCounts VectorStoreFileBatchFileCounts`

    - `Cancelled int64`

      The number of files that where cancelled.

    - `Completed int64`

      The number of files that have been processed.

    - `Failed int64`

      The number of files that have failed to process.

    - `InProgress int64`

      The number of files that are currently being processed.

    - `Total int64`

      The total number of files.

  - `Object VectorStoreFilesBatch`

    The object type, which is always `vector_store.file_batch`.

    - `const VectorStoreFilesBatchVectorStoreFilesBatch VectorStoreFilesBatch = "vector_store.files_batch"`

  - `Status VectorStoreFileBatchStatus`

    The status of the vector store files batch, which can be either `in_progress`, `completed`, `cancelled` or `failed`.

    - `const VectorStoreFileBatchStatusInProgress VectorStoreFileBatchStatus = "in_progress"`

    - `const VectorStoreFileBatchStatusCompleted VectorStoreFileBatchStatus = "completed"`

    - `const VectorStoreFileBatchStatusCancelled VectorStoreFileBatchStatus = "cancelled"`

    - `const VectorStoreFileBatchStatusFailed VectorStoreFileBatchStatus = "failed"`

  - `VectorStoreID string`

    The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.
