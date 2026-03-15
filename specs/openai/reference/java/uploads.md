# Uploads

## Create

`Upload uploads().create(UploadCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

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

- `UploadCreateParams params`

  - `long bytes`

    The number of bytes in the file you are uploading.

  - `String filename`

    The name of the file to upload.

  - `String mimeType`

    The MIME type of the file.

    This must fall within the supported MIME types for your file purpose. See
    the supported MIME types for assistants and vision.

  - `FilePurpose purpose`

    The intended purpose of the uploaded file.

    See the [documentation on File
    purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

    - `JsonValue; anchor "created_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

      - `CREATED_AT("created_at")`

    - `long seconds`

      The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `class Upload:`

  The Upload object can accept byte chunks in the form of Parts.

  - `String id`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `long bytes`

    The intended number of bytes to be uploaded.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `long expiresAt`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `String filename`

    The name of the file to be uploaded.

  - `JsonValue; object_ "upload"constant`

    The object type, which is always "upload".

    - `UPLOAD("upload")`

  - `String purpose`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status status`

    The status of the Upload.

    - `PENDING("pending")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `EXPIRED("expired")`

  - `Optional<FileObject> file`

    The `File` object represents a document that has been uploaded to OpenAI.

    - `String id`

      The file identifier, which can be referenced in the API endpoints.

    - `long bytes`

      The size of the file, in bytes.

    - `long createdAt`

      The Unix timestamp (in seconds) for when the file was created.

    - `String filename`

      The name of the file.

    - `JsonValue; object_ "file"constant`

      The object type, which is always `file`.

      - `FILE("file")`

    - `Purpose purpose`

      The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

      - `ASSISTANTS("assistants")`

      - `ASSISTANTS_OUTPUT("assistants_output")`

      - `BATCH("batch")`

      - `BATCH_OUTPUT("batch_output")`

      - `FINE_TUNE("fine-tune")`

      - `FINE_TUNE_RESULTS("fine-tune-results")`

      - `VISION("vision")`

      - `USER_DATA("user_data")`

    - `Status status`

      Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

      - `UPLOADED("uploaded")`

      - `PROCESSED("processed")`

      - `ERROR("error")`

    - `Optional<Long> expiresAt`

      The Unix timestamp (in seconds) for when the file will expire.

    - `Optional<String> statusDetails`

      Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.files.FilePurpose;
import com.openai.models.uploads.Upload;
import com.openai.models.uploads.UploadCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UploadCreateParams params = UploadCreateParams.builder()
            .bytes(0L)
            .filename("filename")
            .mimeType("mime_type")
            .purpose(FilePurpose.ASSISTANTS)
            .build();
        Upload upload = client.uploads().create(params);
    }
}
```

## Complete

`Upload uploads().complete(UploadCompleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/uploads/{upload_id}/complete`

Completes the [Upload](https://platform.openai.com/docs/api-reference/uploads/object).

Within the returned Upload object, there is a nested [File](https://platform.openai.com/docs/api-reference/files/object) object that is ready to use in the rest of the platform.

You can specify the order of the Parts by passing in an ordered list of the Part IDs.

The number of bytes uploaded upon completion must match the number of bytes initially specified when creating the Upload object. No Parts may be added after an Upload is completed.
Returns the Upload object with status `completed`, including an additional `file` property containing the created usable File object.

### Parameters

- `UploadCompleteParams params`

  - `Optional<String> uploadId`

  - `List<String> partIds`

    The ordered list of Part IDs.

  - `Optional<String> md5`

    The optional md5 checksum for the file contents to verify if the bytes uploaded matches what you expect.

### Returns

- `class Upload:`

  The Upload object can accept byte chunks in the form of Parts.

  - `String id`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `long bytes`

    The intended number of bytes to be uploaded.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `long expiresAt`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `String filename`

    The name of the file to be uploaded.

  - `JsonValue; object_ "upload"constant`

    The object type, which is always "upload".

    - `UPLOAD("upload")`

  - `String purpose`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status status`

    The status of the Upload.

    - `PENDING("pending")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `EXPIRED("expired")`

  - `Optional<FileObject> file`

    The `File` object represents a document that has been uploaded to OpenAI.

    - `String id`

      The file identifier, which can be referenced in the API endpoints.

    - `long bytes`

      The size of the file, in bytes.

    - `long createdAt`

      The Unix timestamp (in seconds) for when the file was created.

    - `String filename`

      The name of the file.

    - `JsonValue; object_ "file"constant`

      The object type, which is always `file`.

      - `FILE("file")`

    - `Purpose purpose`

      The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

      - `ASSISTANTS("assistants")`

      - `ASSISTANTS_OUTPUT("assistants_output")`

      - `BATCH("batch")`

      - `BATCH_OUTPUT("batch_output")`

      - `FINE_TUNE("fine-tune")`

      - `FINE_TUNE_RESULTS("fine-tune-results")`

      - `VISION("vision")`

      - `USER_DATA("user_data")`

    - `Status status`

      Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

      - `UPLOADED("uploaded")`

      - `PROCESSED("processed")`

      - `ERROR("error")`

    - `Optional<Long> expiresAt`

      The Unix timestamp (in seconds) for when the file will expire.

    - `Optional<String> statusDetails`

      Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.uploads.Upload;
import com.openai.models.uploads.UploadCompleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UploadCompleteParams params = UploadCompleteParams.builder()
            .uploadId("upload_abc123")
            .addPartId("string")
            .build();
        Upload upload = client.uploads().complete(params);
    }
}
```

## Cancel

`Upload uploads().cancel(UploadCancelParamsparams = UploadCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/uploads/{upload_id}/cancel`

Cancels the Upload. No Parts may be added after an Upload is cancelled.

Returns the Upload object with status `cancelled`.

### Parameters

- `UploadCancelParams params`

  - `Optional<String> uploadId`

### Returns

- `class Upload:`

  The Upload object can accept byte chunks in the form of Parts.

  - `String id`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `long bytes`

    The intended number of bytes to be uploaded.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `long expiresAt`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `String filename`

    The name of the file to be uploaded.

  - `JsonValue; object_ "upload"constant`

    The object type, which is always "upload".

    - `UPLOAD("upload")`

  - `String purpose`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status status`

    The status of the Upload.

    - `PENDING("pending")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `EXPIRED("expired")`

  - `Optional<FileObject> file`

    The `File` object represents a document that has been uploaded to OpenAI.

    - `String id`

      The file identifier, which can be referenced in the API endpoints.

    - `long bytes`

      The size of the file, in bytes.

    - `long createdAt`

      The Unix timestamp (in seconds) for when the file was created.

    - `String filename`

      The name of the file.

    - `JsonValue; object_ "file"constant`

      The object type, which is always `file`.

      - `FILE("file")`

    - `Purpose purpose`

      The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

      - `ASSISTANTS("assistants")`

      - `ASSISTANTS_OUTPUT("assistants_output")`

      - `BATCH("batch")`

      - `BATCH_OUTPUT("batch_output")`

      - `FINE_TUNE("fine-tune")`

      - `FINE_TUNE_RESULTS("fine-tune-results")`

      - `VISION("vision")`

      - `USER_DATA("user_data")`

    - `Status status`

      Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

      - `UPLOADED("uploaded")`

      - `PROCESSED("processed")`

      - `ERROR("error")`

    - `Optional<Long> expiresAt`

      The Unix timestamp (in seconds) for when the file will expire.

    - `Optional<String> statusDetails`

      Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.uploads.Upload;
import com.openai.models.uploads.UploadCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Upload upload = client.uploads().cancel("upload_abc123");
    }
}
```

### Domain Types

### Upload

- `class Upload:`

  The Upload object can accept byte chunks in the form of Parts.

  - `String id`

    The Upload unique identifier, which can be referenced in API endpoints.

  - `long bytes`

    The intended number of bytes to be uploaded.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the Upload was created.

  - `long expiresAt`

    The Unix timestamp (in seconds) for when the Upload will expire.

  - `String filename`

    The name of the file to be uploaded.

  - `JsonValue; object_ "upload"constant`

    The object type, which is always "upload".

    - `UPLOAD("upload")`

  - `String purpose`

    The intended purpose of the file. [Please refer here](https://platform.openai.com/docs/api-reference/files/object#files/object-purpose) for acceptable values.

  - `Status status`

    The status of the Upload.

    - `PENDING("pending")`

    - `COMPLETED("completed")`

    - `CANCELLED("cancelled")`

    - `EXPIRED("expired")`

  - `Optional<FileObject> file`

    The `File` object represents a document that has been uploaded to OpenAI.

    - `String id`

      The file identifier, which can be referenced in the API endpoints.

    - `long bytes`

      The size of the file, in bytes.

    - `long createdAt`

      The Unix timestamp (in seconds) for when the file was created.

    - `String filename`

      The name of the file.

    - `JsonValue; object_ "file"constant`

      The object type, which is always `file`.

      - `FILE("file")`

    - `Purpose purpose`

      The intended purpose of the file. Supported values are `assistants`, `assistants_output`, `batch`, `batch_output`, `fine-tune`, `fine-tune-results`, `vision`, and `user_data`.

      - `ASSISTANTS("assistants")`

      - `ASSISTANTS_OUTPUT("assistants_output")`

      - `BATCH("batch")`

      - `BATCH_OUTPUT("batch_output")`

      - `FINE_TUNE("fine-tune")`

      - `FINE_TUNE_RESULTS("fine-tune-results")`

      - `VISION("vision")`

      - `USER_DATA("user_data")`

    - `Status status`

      Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

      - `UPLOADED("uploaded")`

      - `PROCESSED("processed")`

      - `ERROR("error")`

    - `Optional<Long> expiresAt`

      The Unix timestamp (in seconds) for when the file will expire.

    - `Optional<String> statusDetails`

      Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

## Parts

### Create

`UploadPart uploads().parts().create(PartCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/uploads/{upload_id}/parts`

Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.

Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.

It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

#### Parameters

- `PartCreateParams params`

  - `Optional<String> uploadId`

  - `String data`

    The chunk of bytes for this Part.

#### Returns

- `class UploadPart:`

  The upload Part represents a chunk of bytes we can add to an Upload object.

  - `String id`

    The upload Part unique identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the Part was created.

  - `JsonValue; object_ "upload.part"constant`

    The object type, which is always `upload.part`.

    - `UPLOAD_PART("upload.part")`

  - `String uploadId`

    The ID of the Upload object that this Part was added to.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.uploads.parts.PartCreateParams;
import com.openai.models.uploads.parts.UploadPart;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PartCreateParams params = PartCreateParams.builder()
            .uploadId("upload_abc123")
            .data(ByteArrayInputStream("some content".getBytes()))
            .build();
        UploadPart uploadPart = client.uploads().parts().create(params);
    }
}
```

#### Domain Types

#### Upload Part

- `class UploadPart:`

  The upload Part represents a chunk of bytes we can add to an Upload object.

  - `String id`

    The upload Part unique identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the Part was created.

  - `JsonValue; object_ "upload.part"constant`

    The object type, which is always `upload.part`.

    - `UPLOAD_PART("upload.part")`

  - `String uploadId`

    The ID of the Upload object that this Part was added to.
