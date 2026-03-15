# Image Streaming

Stream image generation and editing in real time with server-sent events.
[Learn more about image streaming](https://developers.openai.com/docs/guides/image-generation).

Image edit streaming events

## image\_edit.partial\_image

Emitted when a partial image is available during image editing streaming.

b64\_json: string

Base64-encoded partial image data, suitable for rendering as an image.

background: "transparent" or "opaque" or "auto"

The background setting for the requested edited image.

Accepts one of the following:

"transparent"

"opaque"

"auto"

created\_at: number

The Unix timestamp when the event was created.

output\_format: "png" or "webp" or "jpeg"

The output format for the requested edited image.

Accepts one of the following:

"png"

"webp"

"jpeg"

partial\_image\_index: number

0-based index for the partial image (streaming).

quality: "low" or "medium" or "high" or "auto"

The quality setting for the requested edited image.

Accepts one of the following:

"low"

"medium"

"high"

"auto"

size: "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the requested edited image.

Accepts one of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

type: "image\_edit.partial\_image"

The type of the event. Always `image_edit.partial_image`.

OBJECT

### image\_edit.partial\_image

```
{
  "type": "image_edit.partial_image",
  "b64_json": "...",
  "created_at": 1620000000,
  "size": "1024x1024",
  "quality": "high",
  "background": "transparent",
  "output_format": "png",
  "partial_image_index": 0
}
```

## image\_edit.completed

Emitted when image editing has completed and the final image is available.

b64\_json: string

Base64-encoded final edited image data, suitable for rendering as an image.

background: "transparent" or "opaque" or "auto"

The background setting for the edited image.

Accepts one of the following:

"transparent"

"opaque"

"auto"

created\_at: number

The Unix timestamp when the event was created.

output\_format: "png" or "webp" or "jpeg"

The output format for the edited image.

Accepts one of the following:

"png"

"webp"

"jpeg"

quality: "low" or "medium" or "high" or "auto"

The quality setting for the edited image.

Accepts one of the following:

"low"

"medium"

"high"

"auto"

size: "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the edited image.

Accepts one of the following:

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

type: "image\_edit.completed"

The type of the event. Always `image_edit.completed`.

usage: object { input\_tokens, input\_tokens\_details, output\_tokens, total\_tokens }

For the GPT image models only, the token usage information for the image generation.

input\_tokens: number

The number of tokens (images and text) in the input prompt.

input\_tokens\_details: object { image\_tokens, text\_tokens }

The input tokens detailed information for the image generation.

image\_tokens: number

The number of image tokens in the input prompt.

text\_tokens: number

The number of text tokens in the input prompt.

output\_tokens: number

The number of image tokens in the output image.

total\_tokens: number

The total number of tokens (images and text) used for the image generation.

OBJECT

### image\_edit.completed

```
{
  "type": "image_edit.completed",
  "b64_json": "...",
  "created_at": 1620000000,
  "size": "1024x1024",
  "quality": "high",
  "background": "transparent",
  "output_format": "png",
  "usage": {
    "total_tokens": 100,
    "input_tokens": 50,
    "output_tokens": 50,
    "input_tokens_details": {
      "text_tokens": 10,
      "image_tokens": 40
    }
  }
}
```