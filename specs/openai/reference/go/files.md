# Files

## List

`client.Files.List(ctx, query) (*CursorPage[FileObject], error)`

**get** `/files`

Returns a list of files.

### Parameters

- `query FileListParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

  - `Order param.Field[FileListParamsOrder]`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `const FileListParamsOrderAsc FileListParamsOrder = "asc"`

    - `const FileListParamsOrderDesc FileListParamsOrder = "desc"`

  - `Purpose param.Field[string]`

    Only return files with the given purpose.

### Returns

- `type FileObject struct{…}`

  The `File` object represents a document that has been uploaded to OpenAI.

  - `ID string`

    The file identifier, which can be referenced in the API endpoints.

  - `Bytes int64`

    The size of the file, in bytes.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the file was created.

  - `Filename string`

    The name of the file.

  - `Object File`

    The object type, which is always `file`.

    - `const FileFile File = "file"`

  - `Purpose FileObjectPurpose`

    The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

    - `const FileObjectPurposeAssistants FileObjectPurpose = "assistants"`

    - `const FileObjectPurposeAssistantsOutput FileObjectPurpose = "assistants_output"`

    - `const FileObjectPurposeBatch FileObjectPurpose = "batch"`

    - `const FileObjectPurposeBatchOutput FileObjectPurpose = "batch_output"`

    - `const FileObjectPurposeFineTune FileObjectPurpose = "fine-tune"`

    - `const FileObjectPurposeFineTuneResults FileObjectPurpose = "fine-tune-results"`

    - `const FileObjectPurposeVision FileObjectPurpose = "vision"`

    - `const FileObjectPurposeUserData FileObjectPurpose = "user_data"`

  - `Status FileObjectStatus`

    Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

    - `const FileObjectStatusUploaded FileObjectStatus = "uploaded"`

    - `const FileObjectStatusProcessed FileObjectStatus = "processed"`

    - `const FileObjectStatusError FileObjectStatus = "error"`

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the file will expire.

  - `StatusDetails string`

    Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

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
  page, err := client.Files.List(context.TODO(), openai.FileListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Create

`client.Files.New(ctx, body) (*FileObject, error)`

**post** `/files`

Upload a file that can be used across various endpoints. Individual files
can be up to 512 MB, and each project can store up to 2.5 TB of files in
total. There is no organization-wide storage limit.

- The Assistants API supports files up to 2 million tokens and of specific
  file types. See the [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools) for
  details.
- The Fine-tuning API only supports `.jsonl` files. The input also has
  certain required formats for fine-tuning
  [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input) or
  [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) models.
- The Batch API only supports `.jsonl` files up to 200 MB in size. The input
  also has a specific required
  [format](https://platform.openai.com/docs/api-reference/batch/request-input).

Please [contact us](https://help.openai.com/) if you need to increase these
storage limits.

### Parameters

- `body FileNewParams`

  - `File param.Field[Reader]`

    The File object (not file name) to be uploaded.

  - `Purpose param.Field[FilePurpose]`

    The intended purpose of the uploaded file. One of:

    - `assistants`: Used in the Assistants API
    - `batch`: Used in the Batch API
    - `fine-tune`: Used for fine-tuning
    - `vision`: Images used for vision fine-tuning
    - `user_data`: Flexible file type for any purpose
    - `evals`: Used for eval data sets

  - `ExpiresAfter param.Field[FileNewParamsExpiresAfter]`

    The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

    - `Anchor CreatedAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

      - `const CreatedAtCreatedAt CreatedAt = "created_at"`

    - `Seconds int64`

      The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `type FileObject struct{…}`

  The `File` object represents a document that has been uploaded to OpenAI.

  - `ID string`

    The file identifier, which can be referenced in the API endpoints.

  - `Bytes int64`

    The size of the file, in bytes.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the file was created.

  - `Filename string`

    The name of the file.

  - `Object File`

    The object type, which is always `file`.

    - `const FileFile File = "file"`

  - `Purpose FileObjectPurpose`

    The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

    - `const FileObjectPurposeAssistants FileObjectPurpose = "assistants"`

    - `const FileObjectPurposeAssistantsOutput FileObjectPurpose = "assistants_output"`

    - `const FileObjectPurposeBatch FileObjectPurpose = "batch"`

    - `const FileObjectPurposeBatchOutput FileObjectPurpose = "batch_output"`

    - `const FileObjectPurposeFineTune FileObjectPurpose = "fine-tune"`

    - `const FileObjectPurposeFineTuneResults FileObjectPurpose = "fine-tune-results"`

    - `const FileObjectPurposeVision FileObjectPurpose = "vision"`

    - `const FileObjectPurposeUserData FileObjectPurpose = "user_data"`

  - `Status FileObjectStatus`

    Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

    - `const FileObjectStatusUploaded FileObjectStatus = "uploaded"`

    - `const FileObjectStatusProcessed FileObjectStatus = "processed"`

    - `const FileObjectStatusError FileObjectStatus = "error"`

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the file will expire.

  - `StatusDetails string`

    Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Example

```go
package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  fileObject, err := client.Files.New(context.TODO(), openai.FileNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
    Purpose: openai.FilePurposeAssistants,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fileObject.ID)
}
```

## Delete

`client.Files.Delete(ctx, fileID) (*FileDeleted, error)`

**delete** `/files/{file_id}`

Delete a file and remove it from all vector stores.

### Parameters

- `fileID string`

### Returns

- `type FileDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object File`

    - `const FileFile File = "file"`

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
  fileDeleted, err := client.Files.Delete(context.TODO(), "file_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fileDeleted.ID)
}
```

## Retrieve

`client.Files.Get(ctx, fileID) (*FileObject, error)`

**get** `/files/{file_id}`

Returns information about a specific file.

### Parameters

- `fileID string`

### Returns

- `type FileObject struct{…}`

  The `File` object represents a document that has been uploaded to OpenAI.

  - `ID string`

    The file identifier, which can be referenced in the API endpoints.

  - `Bytes int64`

    The size of the file, in bytes.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the file was created.

  - `Filename string`

    The name of the file.

  - `Object File`

    The object type, which is always `file`.

    - `const FileFile File = "file"`

  - `Purpose FileObjectPurpose`

    The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

    - `const FileObjectPurposeAssistants FileObjectPurpose = "assistants"`

    - `const FileObjectPurposeAssistantsOutput FileObjectPurpose = "assistants_output"`

    - `const FileObjectPurposeBatch FileObjectPurpose = "batch"`

    - `const FileObjectPurposeBatchOutput FileObjectPurpose = "batch_output"`

    - `const FileObjectPurposeFineTune FileObjectPurpose = "fine-tune"`

    - `const FileObjectPurposeFineTuneResults FileObjectPurpose = "fine-tune-results"`

    - `const FileObjectPurposeVision FileObjectPurpose = "vision"`

    - `const FileObjectPurposeUserData FileObjectPurpose = "user_data"`

  - `Status FileObjectStatus`

    Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

    - `const FileObjectStatusUploaded FileObjectStatus = "uploaded"`

    - `const FileObjectStatusProcessed FileObjectStatus = "processed"`

    - `const FileObjectStatusError FileObjectStatus = "error"`

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the file will expire.

  - `StatusDetails string`

    Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

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
  fileObject, err := client.Files.Get(context.TODO(), "file_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fileObject.ID)
}
```

## Content

`client.Files.Content(ctx, fileID) (*Response, error)`

**get** `/files/{file_id}/content`

Returns the contents of the specified file.

### Parameters

- `fileID string`

### Returns

- `type FileContentResponse interface{…}`

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
  response, err := client.Files.Content(context.TODO(), "file_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

### Domain Types

### File Content

- `type FileContent string`

### File Deleted

- `type FileDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object File`

    - `const FileFile File = "file"`

### File Object

- `type FileObject struct{…}`

  The `File` object represents a document that has been uploaded to OpenAI.

  - `ID string`

    The file identifier, which can be referenced in the API endpoints.

  - `Bytes int64`

    The size of the file, in bytes.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the file was created.

  - `Filename string`

    The name of the file.

  - `Object File`

    The object type, which is always `file`.

    - `const FileFile File = "file"`

  - `Purpose FileObjectPurpose`

    The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

    - `const FileObjectPurposeAssistants FileObjectPurpose = "assistants"`

    - `const FileObjectPurposeAssistantsOutput FileObjectPurpose = "assistants_output"`

    - `const FileObjectPurposeBatch FileObjectPurpose = "batch"`

    - `const FileObjectPurposeBatchOutput FileObjectPurpose = "batch_output"`

    - `const FileObjectPurposeFineTune FileObjectPurpose = "fine-tune"`

    - `const FileObjectPurposeFineTuneResults FileObjectPurpose = "fine-tune-results"`

    - `const FileObjectPurposeVision FileObjectPurpose = "vision"`

    - `const FileObjectPurposeUserData FileObjectPurpose = "user_data"`

  - `Status FileObjectStatus`

    Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

    - `const FileObjectStatusUploaded FileObjectStatus = "uploaded"`

    - `const FileObjectStatusProcessed FileObjectStatus = "processed"`

    - `const FileObjectStatusError FileObjectStatus = "error"`

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the file will expire.

  - `StatusDetails string`

    Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### File Purpose

- `type FilePurpose string`

  The intended purpose of the uploaded file. One of:

  - `assistants`: Used in the Assistants API
  - `batch`: Used in the Batch API
  - `fine-tune`: Used for fine-tuning
  - `vision`: Images used for vision fine-tuning
  - `user_data`: Flexible file type for any purpose
  - `evals`: Used for eval data sets

  - `const FilePurposeAssistants FilePurpose = "assistants"`

  - `const FilePurposeBatch FilePurpose = "batch"`

  - `const FilePurposeFineTune FilePurpose = "fine-tune"`

  - `const FilePurposeVision FilePurpose = "vision"`

  - `const FilePurposeUserData FilePurpose = "user_data"`

  - `const FilePurposeEvals FilePurpose = "evals"`
