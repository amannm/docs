# Videos

## Create

`Video videos().create(VideoCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/videos`

Create a new video generation job from a prompt and optional reference assets.

### Parameters

- `VideoCreateParams params`

  - `String prompt`

    Text prompt that describes the video to generate.

  - `Optional<InputReference> inputReference`

    Optional reference asset upload or reference object that guides generation.

    - `String`

    - `class ImageInputReferenceParam:`

      - `Optional<String> fileId`

      - `Optional<String> imageUrl`

        A fully qualified URL or base64-encoded data URL.

  - `Optional<VideoModel> model`

    The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

  - `Optional<VideoSeconds> seconds`

    Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

  - `Optional<VideoSize> size`

    Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

### Returns

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.Video;
import com.openai.models.videos.VideoCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoCreateParams params = VideoCreateParams.builder()
            .prompt("x")
            .build();
        Video video = client.videos().create(params);
    }
}
```

## Edit

`Video videos().edit(VideoEditParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/videos/edits`

Create a new video generation job by editing a source video or existing generated video.

### Parameters

- `VideoEditParams params`

  - `String prompt`

    Text prompt that describes how to edit the source video.

  - `Video video`

    Reference to the completed video to edit.

    - `String`

    - `class VideoReferenceInputParam:`

      Reference to the completed video.

      - `String id`

        The identifier of the completed video.

### Returns

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.Video;
import com.openai.models.videos.VideoEditParams;
import java.io.ByteArrayInputStream;
import java.io.InputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoEditParams params = VideoEditParams.builder()
            .prompt("x")
            .video(ByteArrayInputStream("some content".getBytes()))
            .build();
        Video video = client.videos().edit(params);
    }
}
```

## Extend

`Video videos().extend(VideoExtendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/videos/extensions`

Create an extension of a completed video.

### Parameters

- `VideoExtendParams params`

  - `String prompt`

    Updated text prompt that directs the extension generation.

  - `VideoSeconds seconds`

    Length of the newly generated extension segment in seconds (allowed values: 4, 8, 12, 16, 20).

  - `Video video`

    Reference to the completed video to extend.

    - `String`

    - `class VideoReferenceInputParam:`

      Reference to the completed video.

      - `String id`

        The identifier of the completed video.

### Returns

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.Video;
import com.openai.models.videos.VideoExtendParams;
import com.openai.models.videos.VideoSeconds;
import java.io.ByteArrayInputStream;
import java.io.InputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoExtendParams params = VideoExtendParams.builder()
            .prompt("x")
            .seconds(VideoSeconds._4)
            .video(ByteArrayInputStream("some content".getBytes()))
            .build();
        Video video = client.videos().extend(params);
    }
}
```

## Create Character

`VideoCreateCharacterResponse videos().createCharacter(VideoCreateCharacterParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/videos/characters`

Create a character from an uploaded video.

### Parameters

- `VideoCreateCharacterParams params`

  - `String name`

    Display name for this API character.

  - `String video`

    Video file used to create a character.

### Returns

- `class VideoCreateCharacterResponse:`

  - `Optional<String> id`

    Identifier for the character creation cameo.

  - `long createdAt`

    Unix timestamp (in seconds) when the character was created.

  - `Optional<String> name`

    Display name for the character.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.VideoCreateCharacterParams;
import com.openai.models.videos.VideoCreateCharacterResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoCreateCharacterParams params = VideoCreateCharacterParams.builder()
            .name("x")
            .video(ByteArrayInputStream("some content".getBytes()))
            .build();
        VideoCreateCharacterResponse response = client.videos().createCharacter(params);
    }
}
```

## Get Character

`VideoGetCharacterResponse videos().getCharacter(VideoGetCharacterParamsparams = VideoGetCharacterParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/videos/characters/{character_id}`

Fetch a character.

### Parameters

- `VideoGetCharacterParams params`

  - `Optional<String> characterId`

### Returns

- `class VideoGetCharacterResponse:`

  - `Optional<String> id`

    Identifier for the character creation cameo.

  - `long createdAt`

    Unix timestamp (in seconds) when the character was created.

  - `Optional<String> name`

    Display name for the character.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.VideoGetCharacterParams;
import com.openai.models.videos.VideoGetCharacterResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoGetCharacterResponse response = client.videos().getCharacter("char_123");
    }
}
```

## List

`VideoListPage videos().list(VideoListParamsparams = VideoListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/videos`

List recently generated videos for the current project.

### Parameters

- `VideoListParams params`

  - `Optional<String> after`

    Identifier for the last item from the previous pagination request

  - `Optional<Long> limit`

    Number of items to retrieve

  - `Optional<Order> order`

    Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

### Returns

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.VideoListPage;
import com.openai.models.videos.VideoListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoListPage page = client.videos().list();
    }
}
```

## Retrieve

`Video videos().retrieve(VideoRetrieveParamsparams = VideoRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/videos/{video_id}`

Fetch the latest metadata for a generated video.

### Parameters

- `VideoRetrieveParams params`

  - `Optional<String> videoId`

### Returns

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.Video;
import com.openai.models.videos.VideoRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Video video = client.videos().retrieve("video_123");
    }
}
```

## Delete

`VideoDeleteResponse videos().delete(VideoDeleteParamsparams = VideoDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/videos/{video_id}`

Permanently delete a completed or failed video and its stored assets.

### Parameters

- `VideoDeleteParams params`

  - `Optional<String> videoId`

### Returns

- `class VideoDeleteResponse:`

  Confirmation payload returned after deleting a video.

  - `String id`

    Identifier of the deleted video.

  - `boolean deleted`

    Indicates that the video resource was deleted.

  - `JsonValue; object_ "video.deleted"constant`

    The object type that signals the deletion response.

    - `VIDEO_DELETED("video.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.VideoDeleteParams;
import com.openai.models.videos.VideoDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoDeleteResponse video = client.videos().delete("video_123");
    }
}
```

## Remix

`Video videos().remix(VideoRemixParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/videos/{video_id}/remix`

Create a remix of a completed video using a refreshed prompt.

### Parameters

- `VideoRemixParams params`

  - `Optional<String> videoId`

  - `String prompt`

    Updated text prompt that directs the remix generation.

### Returns

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.videos.Video;
import com.openai.models.videos.VideoRemixParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VideoRemixParams params = VideoRemixParams.builder()
            .videoId("video_123")
            .prompt("x")
            .build();
        Video video = client.videos().remix(params);
    }
}
```

## Download Content

`HttpResponse videos().downloadContent(VideoDownloadContentParamsparams = VideoDownloadContentParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/videos/{video_id}/content`

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

### Parameters

- `VideoDownloadContentParams params`

  - `Optional<String> videoId`

  - `Optional<Variant> variant`

    Which downloadable asset to return. Defaults to the MP4 video.

    - `VIDEO("video")`

    - `THUMBNAIL("thumbnail")`

    - `SPRITESHEET("spritesheet")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.videos.VideoDownloadContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse response = client.videos().downloadContent("video_123");
    }
}
```

### Domain Types

### Image Input Reference Param

- `class ImageInputReferenceParam:`

  - `Optional<String> fileId`

  - `Optional<String> imageUrl`

    A fully qualified URL or base64-encoded data URL.

### Video

- `class Video:`

  Structured information describing a generated video job.

  - `String id`

    Unique identifier for the video job.

  - `Optional<Long> completedAt`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `long createdAt`

    Unix timestamp (seconds) for when the job was created.

  - `Optional<VideoCreateError> error`

    Error payload that explains why generation failed, if applicable.

    - `String code`

      A machine-readable error code that was returned.

    - `String message`

      A human-readable description of the error that was returned.

  - `Optional<Long> expiresAt`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `VideoModel model`

    The video generation model that produced the job.

    - `SORA_2("sora-2")`

    - `SORA_2_PRO("sora-2-pro")`

    - `SORA_2_2025_10_06("sora-2-2025-10-06")`

    - `SORA_2_PRO_2025_10_06("sora-2-pro-2025-10-06")`

    - `SORA_2_2025_12_08("sora-2-2025-12-08")`

  - `JsonValue; object_ "video"constant`

    The object type, which is always `video`.

    - `VIDEO("video")`

  - `long progress`

    Approximate completion percentage for the generation task.

  - `Optional<String> prompt`

    The prompt that was used to generate the video.

  - `Optional<String> remixedFromVideoId`

    Identifier of the source video if this video is a remix.

  - `VideoSeconds seconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `_4("4")`

    - `_8("8")`

    - `_12("12")`

  - `VideoSize size`

    The resolution of the generated video.

    - `_720X1280("720x1280")`

    - `_1280X720("1280x720")`

    - `_1024X1792("1024x1792")`

    - `_1792X1024("1792x1024")`

  - `Status status`

    Current lifecycle status of the video job.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

### Video Create Error

- `class VideoCreateError:`

  An error that occurred while generating the response.

  - `String code`

    A machine-readable error code that was returned.

  - `String message`

    A human-readable description of the error that was returned.

### Video Seconds

- `enum VideoSeconds:`

  - `_4("4")`

  - `_8("8")`

  - `_12("12")`

### Video Size

- `enum VideoSize:`

  - `_720X1280("720x1280")`

  - `_1280X720("1280x720")`

  - `_1024X1792("1024x1792")`

  - `_1792X1024("1792x1024")`
