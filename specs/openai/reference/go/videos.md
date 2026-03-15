# Videos

## Create

`client.Videos.New(ctx, body) (*Video, error)`

**post** `/videos`

Create a new video generation job from a prompt and optional reference assets.

### Parameters

- `body VideoNewParams`

  - `Prompt param.Field[string]`

    Text prompt that describes the video to generate.

  - `InputReference param.Field[VideoNewParamsInputReferenceUnion]`

    Optional reference asset upload or reference object that guides generation.

    - `Reader`

    - `type ImageInputReferenceParamResp struct{…}`

      - `FileID string`

      - `ImageURL string`

        A fully qualified URL or base64-encoded data URL.

  - `Model param.Field[VideoModel]`

    The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

  - `Seconds param.Field[VideoSeconds]`

    Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

  - `Size param.Field[VideoSize]`

    Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

### Returns

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

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
  video, err := client.Videos.New(context.TODO(), openai.VideoNewParams{
    Prompt: "x",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", video.ID)
}
```

## Edit

`client.Videos.Edit(ctx, body) (*Video, error)`

**post** `/videos/edits`

Create a new video generation job by editing a source video or existing generated video.

### Parameters

- `body VideoEditParams`

  - `Prompt param.Field[string]`

    Text prompt that describes how to edit the source video.

  - `Video param.Field[VideoEditParamsVideoUnion]`

    Reference to the completed video to edit.

    - `Reader`

    - `type VideoEditParamsVideoVideoReferenceInputParam struct{…}`

      Reference to the completed video.

      - `ID string`

        The identifier of the completed video.

### Returns

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

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
  video, err := client.Videos.Edit(context.TODO(), openai.VideoEditParams{
    Prompt: "x",
    Video: openai.VideoEditParamsVideoUnion{
      OfFile: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", video.ID)
}
```

## Extend

`client.Videos.Extend(ctx, body) (*Video, error)`

**post** `/videos/extensions`

Create an extension of a completed video.

### Parameters

- `body VideoExtendParams`

  - `Prompt param.Field[string]`

    Updated text prompt that directs the extension generation.

  - `Seconds param.Field[VideoSeconds]`

    Length of the newly generated extension segment in seconds (allowed values: 4, 8, 12, 16, 20).

  - `Video param.Field[VideoExtendParamsVideoUnion]`

    Reference to the completed video to extend.

    - `Reader`

    - `type VideoExtendParamsVideoVideoReferenceInputParam struct{…}`

      Reference to the completed video.

      - `ID string`

        The identifier of the completed video.

### Returns

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

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
  video, err := client.Videos.Extend(context.TODO(), openai.VideoExtendParams{
    Prompt: "x",
    Seconds: openai.VideoSeconds4,
    Video: openai.VideoExtendParamsVideoUnion{
      OfFile: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", video.ID)
}
```

## Create Character

`client.Videos.NewCharacter(ctx, body) (*VideoNewCharacterResponse, error)`

**post** `/videos/characters`

Create a character from an uploaded video.

### Parameters

- `body VideoNewCharacterParams`

  - `Name param.Field[string]`

    Display name for this API character.

  - `Video param.Field[Reader]`

    Video file used to create a character.

### Returns

- `type VideoNewCharacterResponse struct{…}`

  - `ID string`

    Identifier for the character creation cameo.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the character was created.

  - `Name string`

    Display name for the character.

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
  response, err := client.Videos.NewCharacter(context.TODO(), openai.VideoNewCharacterParams{
    Name: "x",
    Video: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.ID)
}
```

## Get Character

`client.Videos.GetCharacter(ctx, characterID) (*VideoGetCharacterResponse, error)`

**get** `/videos/characters/{character_id}`

Fetch a character.

### Parameters

- `characterID string`

### Returns

- `type VideoGetCharacterResponse struct{…}`

  - `ID string`

    Identifier for the character creation cameo.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the character was created.

  - `Name string`

    Display name for the character.

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
  response, err := client.Videos.GetCharacter(context.TODO(), "char_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.ID)
}
```

## List

`client.Videos.List(ctx, query) (*ConversationCursorPage[Video], error)`

**get** `/videos`

List recently generated videos for the current project.

### Parameters

- `query VideoListParams`

  - `After param.Field[string]`

    Identifier for the last item from the previous pagination request

  - `Limit param.Field[int64]`

    Number of items to retrieve

  - `Order param.Field[VideoListParamsOrder]`

    Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

    - `const VideoListParamsOrderAsc VideoListParamsOrder = "asc"`

    - `const VideoListParamsOrderDesc VideoListParamsOrder = "desc"`

### Returns

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

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
  page, err := client.Videos.List(context.TODO(), openai.VideoListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Videos.Get(ctx, videoID) (*Video, error)`

**get** `/videos/{video_id}`

Fetch the latest metadata for a generated video.

### Parameters

- `videoID string`

### Returns

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

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
  video, err := client.Videos.Get(context.TODO(), "video_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", video.ID)
}
```

## Delete

`client.Videos.Delete(ctx, videoID) (*VideoDeleteResponse, error)`

**delete** `/videos/{video_id}`

Permanently delete a completed or failed video and its stored assets.

### Parameters

- `videoID string`

### Returns

- `type VideoDeleteResponse struct{…}`

  Confirmation payload returned after deleting a video.

  - `ID string`

    Identifier of the deleted video.

  - `Deleted bool`

    Indicates that the video resource was deleted.

  - `Object VideoDeleted`

    The object type that signals the deletion response.

    - `const VideoDeletedVideoDeleted VideoDeleted = "video.deleted"`

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
  video, err := client.Videos.Delete(context.TODO(), "video_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", video.ID)
}
```

## Remix

`client.Videos.Remix(ctx, videoID, body) (*Video, error)`

**post** `/videos/{video_id}/remix`

Create a remix of a completed video using a refreshed prompt.

### Parameters

- `videoID string`

- `body VideoRemixParams`

  - `Prompt param.Field[string]`

    Updated text prompt that directs the remix generation.

### Returns

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

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
  video, err := client.Videos.Remix(
    context.TODO(),
    "video_123",
    openai.VideoRemixParams{
      Prompt: "x",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", video.ID)
}
```

## Download Content

`client.Videos.DownloadContent(ctx, videoID, query) (*Response, error)`

**get** `/videos/{video_id}/content`

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

### Parameters

- `videoID string`

- `query VideoDownloadContentParams`

  - `Variant param.Field[VideoDownloadContentParamsVariant]`

    Which downloadable asset to return. Defaults to the MP4 video.

    - `const VideoDownloadContentParamsVariantVideo VideoDownloadContentParamsVariant = "video"`

    - `const VideoDownloadContentParamsVariantThumbnail VideoDownloadContentParamsVariant = "thumbnail"`

    - `const VideoDownloadContentParamsVariantSpritesheet VideoDownloadContentParamsVariant = "spritesheet"`

### Returns

- `type VideoDownloadContentResponse interface{…}`

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
  response, err := client.Videos.DownloadContent(
    context.TODO(),
    "video_123",
    openai.VideoDownloadContentParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

### Domain Types

### Image Input Reference Param

- `type ImageInputReferenceParamResp struct{…}`

  - `FileID string`

  - `ImageURL string`

    A fully qualified URL or base64-encoded data URL.

### Video

- `type Video struct{…}`

  Structured information describing a generated video job.

  - `ID string`

    Unique identifier for the video job.

  - `CompletedAt int64`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the job was created.

  - `Error VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `Code string`

      A machine-readable error code that was returned.

    - `Message string`

      A human-readable description of the error that was returned.

  - `ExpiresAt int64`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `Model VideoModel`

    The video generation model that produced the job.

    - `string`

    - `type VideoModel string`

      - `const VideoModelSora2 VideoModel = "sora-2"`

      - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

      - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

      - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

      - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

  - `Object Video`

    The object type, which is always `video`.

    - `const VideoVideo Video = "video"`

  - `Progress int64`

    Approximate completion percentage for the generation task.

  - `Prompt string`

    The prompt that was used to generate the video.

  - `RemixedFromVideoID string`

    Identifier of the source video if this video is a remix.

  - `Seconds VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `string`

    - `type VideoSeconds string`

      - `const VideoSeconds4 VideoSeconds = "4"`

      - `const VideoSeconds8 VideoSeconds = "8"`

      - `const VideoSeconds12 VideoSeconds = "12"`

  - `Size VideoSize`

    The resolution of the generated video.

    - `const VideoSize720x1280 VideoSize = "720x1280"`

    - `const VideoSize1280x720 VideoSize = "1280x720"`

    - `const VideoSize1024x1792 VideoSize = "1024x1792"`

    - `const VideoSize1792x1024 VideoSize = "1792x1024"`

  - `Status VideoStatus`

    Current lifecycle status of the video job.

    - `const VideoStatusQueued VideoStatus = "queued"`

    - `const VideoStatusInProgress VideoStatus = "in_progress"`

    - `const VideoStatusCompleted VideoStatus = "completed"`

    - `const VideoStatusFailed VideoStatus = "failed"`

### Video Create Error

- `type VideoCreateError struct{…}`

  An error that occurred while generating the response.

  - `Code string`

    A machine-readable error code that was returned.

  - `Message string`

    A human-readable description of the error that was returned.

### Video Model

- `type VideoModel interface{…}`

  - `string`

  - `type VideoModel string`

    - `const VideoModelSora2 VideoModel = "sora-2"`

    - `const VideoModelSora2Pro VideoModel = "sora-2-pro"`

    - `const VideoModelSora2_2025_10_06 VideoModel = "sora-2-2025-10-06"`

    - `const VideoModelSora2Pro2025_10_06 VideoModel = "sora-2-pro-2025-10-06"`

    - `const VideoModelSora2_2025_12_08 VideoModel = "sora-2-2025-12-08"`

### Video Seconds

- `type VideoSeconds string`

  - `const VideoSeconds4 VideoSeconds = "4"`

  - `const VideoSeconds8 VideoSeconds = "8"`

  - `const VideoSeconds12 VideoSeconds = "12"`

### Video Size

- `type VideoSize string`

  - `const VideoSize720x1280 VideoSize = "720x1280"`

  - `const VideoSize1280x720 VideoSize = "1280x720"`

  - `const VideoSize1024x1792 VideoSize = "1024x1792"`

  - `const VideoSize1792x1024 VideoSize = "1792x1024"`
