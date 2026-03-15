# Videos

## Create

`videos.create(**kwargs) -> Video`

**post** `/videos`

Create a new video generation job from a prompt and optional reference assets.

### Parameters

- `prompt: String`

  Text prompt that describes the video to generate.

- `input_reference: String | ImageInputReferenceParam`

  Optional reference asset upload or reference object that guides generation.

  - `String`

    Optional reference asset upload or reference object that guides generation.

  - `class ImageInputReferenceParam`

    - `file_id: String`

    - `image_url: String`

      A fully qualified URL or base64-encoded data URL.

- `model: VideoModel`

  The video generation model to use (allowed values: sora-2, sora-2-pro). Defaults to `sora-2`.

  - `String`

  - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

    - `:"sora-2"`

    - `:"sora-2-pro"`

    - `:"sora-2-2025-10-06"`

    - `:"sora-2-pro-2025-10-06"`

    - `:"sora-2-2025-12-08"`

- `seconds: VideoSeconds`

  Clip duration in seconds (allowed values: 4, 8, 12). Defaults to 4 seconds.

  - `:"4"`

  - `:"8"`

  - `:"12"`

- `size: VideoSize`

  Output resolution formatted as width x height (allowed values: 720x1280, 1280x720, 1024x1792, 1792x1024). Defaults to 720x1280.

  - `:"720x1280"`

  - `:"1280x720"`

  - `:"1024x1792"`

  - `:"1792x1024"`

### Returns

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

video = openai.videos.create(prompt: "x")

puts(video)
```

## Edit

`videos.edit(**kwargs) -> Video`

**post** `/videos/edits`

Create a new video generation job by editing a source video or existing generated video.

### Parameters

- `prompt: String`

  Text prompt that describes how to edit the source video.

- `video: String | { id}`

  Reference to the completed video to edit.

  - `String`

    Reference to the completed video to edit.

  - `class VideoReferenceInputParam`

    Reference to the completed video.

    - `id: String`

      The identifier of the completed video.

### Returns

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

video = openai.videos.edit(prompt: "x", video: Pathname(__FILE__))

puts(video)
```

## Extend

`videos.extend_(**kwargs) -> Video`

**post** `/videos/extensions`

Create an extension of a completed video.

### Parameters

- `prompt: String`

  Updated text prompt that directs the extension generation.

- `seconds: VideoSeconds`

  Length of the newly generated extension segment in seconds (allowed values: 4, 8, 12, 16, 20).

  - `:"4"`

  - `:"8"`

  - `:"12"`

- `video: String | { id}`

  Reference to the completed video to extend.

  - `String`

    Reference to the completed video to extend.

  - `class VideoReferenceInputParam`

    Reference to the completed video.

    - `id: String`

      The identifier of the completed video.

### Returns

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

video = openai.videos.extend_(prompt: "x", seconds: :"4", video: Pathname(__FILE__))

puts(video)
```

## Create Character

`videos.create_character(**kwargs) -> VideoCreateCharacterResponse`

**post** `/videos/characters`

Create a character from an uploaded video.

### Parameters

- `name: String`

  Display name for this API character.

- `video: String`

  Video file used to create a character.

### Returns

- `class VideoCreateCharacterResponse`

  - `id: String`

    Identifier for the character creation cameo.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the character was created.

  - `name: String`

    Display name for the character.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.videos.create_character(name: "x", video: Pathname(__FILE__))

puts(response)
```

## Get Character

`videos.get_character(character_id) -> VideoGetCharacterResponse`

**get** `/videos/characters/{character_id}`

Fetch a character.

### Parameters

- `character_id: String`

### Returns

- `class VideoGetCharacterResponse`

  - `id: String`

    Identifier for the character creation cameo.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the character was created.

  - `name: String`

    Display name for the character.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.videos.get_character("char_123")

puts(response)
```

## List

`videos.list(**kwargs) -> ConversationCursorPage<Video>`

**get** `/videos`

List recently generated videos for the current project.

### Parameters

- `after: String`

  Identifier for the last item from the previous pagination request

- `limit: Integer`

  Number of items to retrieve

- `order: :asc | :desc`

  Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

  - `:asc`

  - `:desc`

### Returns

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.videos.list

puts(page)
```

## Retrieve

`videos.retrieve(video_id) -> Video`

**get** `/videos/{video_id}`

Fetch the latest metadata for a generated video.

### Parameters

- `video_id: String`

### Returns

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

video = openai.videos.retrieve("video_123")

puts(video)
```

## Delete

`videos.delete(video_id) -> VideoDeleteResponse`

**delete** `/videos/{video_id}`

Permanently delete a completed or failed video and its stored assets.

### Parameters

- `video_id: String`

### Returns

- `class VideoDeleteResponse`

  Confirmation payload returned after deleting a video.

  - `id: String`

    Identifier of the deleted video.

  - `deleted: bool`

    Indicates that the video resource was deleted.

  - `object: :"video.deleted"`

    The object type that signals the deletion response.

    - `:"video.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

video = openai.videos.delete("video_123")

puts(video)
```

## Remix

`videos.remix(video_id, **kwargs) -> Video`

**post** `/videos/{video_id}/remix`

Create a remix of a completed video using a refreshed prompt.

### Parameters

- `video_id: String`

- `prompt: String`

  Updated text prompt that directs the remix generation.

### Returns

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

video = openai.videos.remix("video_123", prompt: "x")

puts(video)
```

## Download Content

`videos.download_content(video_id, **kwargs) -> StringIO`

**get** `/videos/{video_id}/content`

Download the generated video bytes or a derived preview asset.

Streams the rendered video content for the specified video job.

### Parameters

- `video_id: String`

- `variant: :video | :thumbnail | :spritesheet`

  Which downloadable asset to return. Defaults to the MP4 video.

  - `:video`

  - `:thumbnail`

  - `:spritesheet`

### Returns

- `StringIO`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.videos.download_content("video_123")

puts(response)
```

### Domain Types

### Image Input Reference Param

- `class ImageInputReferenceParam`

  - `file_id: String`

  - `image_url: String`

    A fully qualified URL or base64-encoded data URL.

### Video

- `class Video`

  Structured information describing a generated video job.

  - `id: String`

    Unique identifier for the video job.

  - `completed_at: Integer`

    Unix timestamp (seconds) for when the job completed, if finished.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the job was created.

  - `error: VideoCreateError`

    Error payload that explains why generation failed, if applicable.

    - `code: String`

      A machine-readable error code that was returned.

    - `message: String`

      A human-readable description of the error that was returned.

  - `expires_at: Integer`

    Unix timestamp (seconds) for when the downloadable assets expire, if set.

  - `model: VideoModel`

    The video generation model that produced the job.

    - `String`

    - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

      - `:"sora-2"`

      - `:"sora-2-pro"`

      - `:"sora-2-2025-10-06"`

      - `:"sora-2-pro-2025-10-06"`

      - `:"sora-2-2025-12-08"`

  - `object: :video`

    The object type, which is always `video`.

    - `:video`

  - `progress: Integer`

    Approximate completion percentage for the generation task.

  - `prompt: String`

    The prompt that was used to generate the video.

  - `remixed_from_video_id: String`

    Identifier of the source video if this video is a remix.

  - `seconds: String | VideoSeconds`

    Duration of the generated clip in seconds. For extensions, this is the stitched total duration.

    - `String`

    - `VideoSeconds = :"4" | :"8" | :"12"`

      - `:"4"`

      - `:"8"`

      - `:"12"`

  - `size: VideoSize`

    The resolution of the generated video.

    - `:"720x1280"`

    - `:"1280x720"`

    - `:"1024x1792"`

    - `:"1792x1024"`

  - `status: :queued | :in_progress | :completed | :failed`

    Current lifecycle status of the video job.

    - `:queued`

    - `:in_progress`

    - `:completed`

    - `:failed`

### Video Create Error

- `class VideoCreateError`

  An error that occurred while generating the response.

  - `code: String`

    A machine-readable error code that was returned.

  - `message: String`

    A human-readable description of the error that was returned.

### Video Model

- `VideoModel = String | :"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

  - `String`

  - `:"sora-2" | :"sora-2-pro" | :"sora-2-2025-10-06" | 2 more`

    - `:"sora-2"`

    - `:"sora-2-pro"`

    - `:"sora-2-2025-10-06"`

    - `:"sora-2-pro-2025-10-06"`

    - `:"sora-2-2025-12-08"`

### Video Seconds

- `VideoSeconds = :"4" | :"8" | :"12"`

  - `:"4"`

  - `:"8"`

  - `:"12"`

### Video Size

- `VideoSize = :"720x1280" | :"1280x720" | :"1024x1792" | :"1792x1024"`

  - `:"720x1280"`

  - `:"1280x720"`

  - `:"1024x1792"`

  - `:"1792x1024"`
