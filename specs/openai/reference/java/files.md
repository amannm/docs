# Files

## List

`FileListPage files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/files`

Returns a list of files.

### Parameters

- `FileListParams params`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 10,000, and the default is 10,000.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> purpose`

    Only return files with the given purpose.

### Returns

- `class FileObject:`

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
import com.openai.models.files.FileListPage;
import com.openai.models.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileListPage page = client.files().list();
    }
}
```

## Create

`FileObject files().create(FileCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

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

- `FileCreateParams params`

  - `String file`

    The File object (not file name) to be uploaded.

  - `FilePurpose purpose`

    The intended purpose of the uploaded file. One of:

    - `assistants`: Used in the Assistants API
    - `batch`: Used in the Batch API
    - `fine-tune`: Used for fine-tuning
    - `vision`: Images used for vision fine-tuning
    - `user_data`: Flexible file type for any purpose
    - `evals`: Used for eval data sets

  - `Optional<ExpiresAfter> expiresAfter`

    The expiration policy for a file. By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.

    - `JsonValue; anchor "created_at"constant`

      Anchor timestamp after which the expiration policy applies. Supported anchors: `created_at`.

      - `CREATED_AT("created_at")`

    - `long seconds`

      The number of seconds after the anchor time that the file will expire. Must be between 3600 (1 hour) and 2592000 (30 days).

### Returns

- `class FileObject:`

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
import com.openai.models.files.FileCreateParams;
import com.openai.models.files.FileObject;
import com.openai.models.files.FilePurpose;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileCreateParams params = FileCreateParams.builder()
            .file(ByteArrayInputStream("some content".getBytes()))
            .purpose(FilePurpose.ASSISTANTS)
            .build();
        FileObject fileObject = client.files().create(params);
    }
}
```

## Delete

`FileDeleted files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/files/{file_id}`

Delete a file and remove it from all vector stores.

### Parameters

- `FileDeleteParams params`

  - `Optional<String> fileId`

### Returns

- `class FileDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "file"constant`

    - `FILE("file")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.files.FileDeleteParams;
import com.openai.models.files.FileDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileDeleted fileDeleted = client.files().delete("file_id");
    }
}
```

## Retrieve

`FileObject files().retrieve(FileRetrieveParamsparams = FileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/files/{file_id}`

Returns information about a specific file.

### Parameters

- `FileRetrieveParams params`

  - `Optional<String> fileId`

### Returns

- `class FileObject:`

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
import com.openai.models.files.FileObject;
import com.openai.models.files.FileRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileObject fileObject = client.files().retrieve("file_id");
    }
}
```

## Content

`HttpResponse files().content(FileContentParamsparams = FileContentParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/files/{file_id}/content`

Returns the contents of the specified file.

### Parameters

- `FileContentParams params`

  - `Optional<String> fileId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.files.FileContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse response = client.files().content("file_id");
    }
}
```

### Domain Types

### File Deleted

- `class FileDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "file"constant`

    - `FILE("file")`

### File Object

- `class FileObject:`

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

### File Purpose

- `enum FilePurpose:`

  The intended purpose of the uploaded file. One of:

  - `assistants`: Used in the Assistants API
  - `batch`: Used in the Batch API
  - `fine-tune`: Used for fine-tuning
  - `vision`: Images used for vision fine-tuning
  - `user_data`: Flexible file type for any purpose
  - `evals`: Used for eval data sets

  - `ASSISTANTS("assistants")`

  - `BATCH("batch")`

  - `FINE_TUNE("fine-tune")`

  - `VISION("vision")`

  - `USER_DATA("user_data")`

  - `EVALS("evals")`
