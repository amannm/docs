# Uploads

## Create

`client.Uploads.New(ctx, body) (*Upload, error)`

**post** `/uploads`

Creates an intermediate [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object
that you can add [Parts](https://platform.openai.com/docs/api-reference/uploads/part-object) to.
Currently, an Upload can accept at most 8 GB in total and expires after an
hour after you create it.

Once you complete the Upload, we will create a
[File](https://platform.openai.com/docs/api-reference/files/object) object that contains all the parts
you uploaded. This File is usable in the rest of our platform as a regular
File object.

For certain `purpose` values, the correct `mime_type` must be specified.
Please refer to documentation for the
[supported MIME types for your use case](https://platform.openai.com/docs/assistants/tools/file-search#supported-files).

For guidance on the proper filename extensions for each purpose, please
follow the documentation on [creating a
File](https://platform.openai.com/docs/api-reference/files/create).

Returns the Upload object with status `pending`.

### Parameters

- `body UploadNewParams`

  - `Bytes param.Field[int64]`

    The number of bytes in the file you are uploading.

  - `Filename param.Field[string]`

    The name of the file to upload.

  - `MimeType param.Field[string]`

    The MIME type of the file.

    This must fall within the supported MIME types for your file purpose. See
    the supported MIME types for assistants and vision.

  - `Purpose param.Field[FilePurpose]`

    The intended purpose of the uploaded file.

    See the [documentation on File
    purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).

  - `ExpiresAfter param.Field[UploadNewParamsExpiresAfter]`

    The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

    - `Anchor CreatedAt`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

      - `const CreatedAtCreatedAt CreatedAt = "created_at"`

    - `Seconds int64`

      The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `type Upload struct{…}`

  The Upload object can accept byte chunks in the form of Parts.

  - `ID string`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `Bytes int64`

    The intended number of bytes to be uploaded.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `Filename string`

    The name of the file to be uploaded.

  - `Object Upload`

    The object type, which is always "upload".

    - `const UploadUpload Upload = "upload"`

  - `Purpose string`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status UploadStatus`

    The status of the Upload.

    - `const UploadStatusPending UploadStatus = "pending"`

    - `const UploadStatusCompleted UploadStatus = "completed"`

    - `const UploadStatusCancelled UploadStatus = "cancelled"`

    - `const UploadStatusExpired UploadStatus = "expired"`

  - `File FileObject`

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
  upload, err := client.Uploads.New(context.TODO(), openai.UploadNewParams{
    Bytes: 0,
    Filename: "filename",
    MimeType: "mime_type",
    Purpose: openai.FilePurposeAssistants,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", upload.ID)
}
```

## Complete

`client.Uploads.Complete(ctx, uploadID, body) (*Upload, error)`

**post** `/uploads/{upload_id}/complete`

Completes the [Upload](https://platform.openai.com/docs/api-reference/uploads/object).

Within the returned Upload object, there is a nested [File](https://platform.openai.com/docs/api-reference/files/object) object that is ready to use in the rest of the platform.

You can specify the order of the Parts by passing in an ordered list of the Part IDs.

The number of bytes uploaded upon completion must match the number of bytes initially specified when creating the Upload object. No Parts may be added after an Upload is completed.
Returns the Upload object with status `completed`, including an additional `file` property containing the created usable File object.

### Parameters

- `uploadID string`

- `body UploadCompleteParams`

  - `PartIDs param.Field[[]string]`

    The ordered list of Part IDs.

  - `Md5 param.Field[string]`

    The optional md5 checksum for the file contents to verify if the bytes uploaded matches what you expect.

### Returns

- `type Upload struct{…}`

  The Upload object can accept byte chunks in the form of Parts.

  - `ID string`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `Bytes int64`

    The intended number of bytes to be uploaded.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `Filename string`

    The name of the file to be uploaded.

  - `Object Upload`

    The object type, which is always "upload".

    - `const UploadUpload Upload = "upload"`

  - `Purpose string`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status UploadStatus`

    The status of the Upload.

    - `const UploadStatusPending UploadStatus = "pending"`

    - `const UploadStatusCompleted UploadStatus = "completed"`

    - `const UploadStatusCancelled UploadStatus = "cancelled"`

    - `const UploadStatusExpired UploadStatus = "expired"`

  - `File FileObject`

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
  upload, err := client.Uploads.Complete(
    context.TODO(),
    "upload_abc123",
    openai.UploadCompleteParams{
      PartIDs: []string{"string"},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", upload.ID)
}
```

## Cancel

`client.Uploads.Cancel(ctx, uploadID) (*Upload, error)`

**post** `/uploads/{upload_id}/cancel`

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

### Parameters

- `uploadID string`

### Returns

- `type Upload struct{…}`

  The Upload object can accept byte chunks in the form of Parts.

  - `ID string`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `Bytes int64`

    The intended number of bytes to be uploaded.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `Filename string`

    The name of the file to be uploaded.

  - `Object Upload`

    The object type, which is always "upload".

    - `const UploadUpload Upload = "upload"`

  - `Purpose string`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status UploadStatus`

    The status of the Upload.

    - `const UploadStatusPending UploadStatus = "pending"`

    - `const UploadStatusCompleted UploadStatus = "completed"`

    - `const UploadStatusCancelled UploadStatus = "cancelled"`

    - `const UploadStatusExpired UploadStatus = "expired"`

  - `File FileObject`

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
  upload, err := client.Uploads.Cancel(context.TODO(), "upload_abc123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", upload.ID)
}
```

### Domain Types

### Upload

- `type Upload struct{…}`

  The Upload object can accept byte chunks in the form of Parts.

  - `ID string`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `Bytes int64`

    The intended number of bytes to be uploaded.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `Filename string`

    The name of the file to be uploaded.

  - `Object Upload`

    The object type, which is always "upload".

    - `const UploadUpload Upload = "upload"`

  - `Purpose string`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status UploadStatus`

    The status of the Upload.

    - `const UploadStatusPending UploadStatus = "pending"`

    - `const UploadStatusCompleted UploadStatus = "completed"`

    - `const UploadStatusCancelled UploadStatus = "cancelled"`

    - `const UploadStatusExpired UploadStatus = "expired"`

  - `File FileObject`

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

## Parts

### Create

`client.Uploads.Parts.New(ctx, uploadID, body) (*UploadPart, error)`

**post** `/uploads/{upload_id}/parts`

Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

#### Parameters

- `uploadID string`

- `body UploadPartNewParams`

  - `Data param.Field[Reader]`

    The chunk of bytes for this Part.

#### Returns

- `type UploadPart struct{…}`

  The upload Part represents a chunk of bytes we can add to an Upload object.

  - `ID string`

    The upload Part unique identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the Part was created.

  - `Object UploadPart`

    The object type, which is always `upload.part`.

    - `const UploadPartUploadPart UploadPart = "upload.part"`

  - `UploadID string`

    The ID of the Upload object that this Part was added to.

#### Example

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
  uploadPart, err := client.Uploads.Parts.New(
    context.TODO(),
    "upload_abc123",
    openai.UploadPartNewParams{
      Data: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", uploadPart.ID)
}
```

#### Domain Types

#### Upload Part

- `type UploadPart struct{…}`

  The upload Part represents a chunk of bytes we can add to an Upload object.

  - `ID string`

    The upload Part unique identifier, which can be referenced in API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the Part was created.

  - `Object UploadPart`

    The object type, which is always `upload.part`.

    - `const UploadPartUploadPart UploadPart = "upload.part"`

  - `UploadID string`

    The ID of the Upload object that this Part was added to.
