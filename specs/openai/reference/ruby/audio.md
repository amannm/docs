# Audio

## Domain Types

### Audio Model

- `AudioModel = :"whisper-1" | :"gpt-4o-transcribe" | :"gpt-4o-mini-transcribe" | 2 more`

  - `:"whisper-1"`

  - `:"gpt-4o-transcribe"`

  - `:"gpt-4o-mini-transcribe"`

  - `:"gpt-4o-mini-transcribe-2025-12-15"`

  - `:"gpt-4o-transcribe-diarize"`

### Audio Response Format

- `AudioResponseFormat = :json | :text | :srt | 3 more`

  The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

  - `:json`

  - `:text`

  - `:srt`

  - `:verbose_json`

  - `:vtt`

  - `:diarized_json`

## Transcriptions

### Create

`audio.transcriptions.create(**kwargs) -> TranscriptionCreateResponse`

**post** `/audio/transcriptions`

Transcribes audio into the input language.

Returns a transcription object in `json`, `diarized_json`, or `verbose_json`
format, or a stream of transcript events.

#### Parameters

- `file: String`

  The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

- `model: String | AudioModel`

  ID of the model to use. The options are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `whisper-1` (which is powered by our open source Whisper V2 model), and `gpt-4o-transcribe-diarize`.

  - `String`

  - `AudioModel = :"whisper-1" | :"gpt-4o-transcribe" | :"gpt-4o-mini-transcribe" | 2 more`

    - `:"whisper-1"`

    - `:"gpt-4o-transcribe"`

    - `:"gpt-4o-mini-transcribe"`

    - `:"gpt-4o-mini-transcribe-2025-12-15"`

    - `:"gpt-4o-transcribe-diarize"`

- `chunking_strategy: :auto | { type, prefix_padding_ms, silence_duration_ms, threshold}`

  Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block. Required when using `gpt-4o-transcribe-diarize` for inputs longer than 30 seconds.

  - `ChunkingStrategy = :auto`

    Automatically set chunking parameters based on the audio. Must be set to `"auto"`.

    - `:auto`

  - `class VadConfig`

    - `type: :server_vad`

      Must be set to `server_vad` to enable manual chunking using server side VAD.

      - `:server_vad`

    - `prefix_padding_ms: Integer`

      Amount of audio to include before the VAD detected speech (in
      milliseconds).

    - `silence_duration_ms: Integer`

      Duration of silence to detect speech stop (in milliseconds).
      With shorter values the model will respond more quickly,
      but may jump in on short pauses from the user.

    - `threshold: Float`

      Sensitivity threshold (0.0 to 1.0) for voice activity detection. A
      higher threshold will require louder audio to activate the model, and
      thus might perform better in noisy environments.

- `include: Array[TranscriptionInclude]`

  Additional information to include in the transcription response.
  `logprobs` will return the log probabilities of the tokens in the
  response to understand the model's confidence in the transcription.
  `logprobs` only works with response_format set to `json` and only with
  the models `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `gpt-4o-mini-transcribe-2025-12-15`. This field is not supported when using `gpt-4o-transcribe-diarize`.

  - `:logprobs`

- `known_speaker_names: Array[String]`

  Optional list of speaker names that correspond to the audio samples provided in `known_speaker_references[]`. Each entry should be a short identifier (for example `customer` or `agent`). Up to 4 speakers are supported.

- `known_speaker_references: Array[String]`

  Optional list of audio samples (as [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)) that contain known speaker references matching `known_speaker_names[]`. Each sample must be between 2 and 10 seconds, and can use any of the same input audio formats supported by `file`.

- `language: String`

  The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.

- `prompt: String`

  An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language. This field is not supported when using `gpt-4o-transcribe-diarize`.

- `response_format: AudioResponseFormat`

  The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

  - `:json`

  - `:text`

  - `:srt`

  - `:verbose_json`

  - `:vtt`

  - `:diarized_json`

- `stream: false`

  If set to true, the model response data will be streamed to the client
  as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
  See the [Streaming section of the Speech-to-Text guide](https://platform.openai.com/docs/guides/speech-to-text?lang=curl#streaming-transcriptions)
  for more information.

  Note: Streaming is not supported for the `whisper-1` model and will be ignored.

  - `false`

- `temperature: Float`

  The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

- `timestamp_granularities: Array[:word | :segment]`

  The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
  This option is not available for `gpt-4o-transcribe-diarize`.

  - `:word`

  - `:segment`

#### Returns

- `TranscriptionCreateResponse = Transcription | TranscriptionDiarized | TranscriptionVerbose`

  Represents a transcription response returned by model, based on the provided input.

  - `class Transcription`

    Represents a transcription response returned by model, based on the provided input.

    - `text: String`

      The transcribed text.

    - `logprobs: Array[{ token, bytes, logprob}]`

      The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

      - `token: String`

        The token in the transcription.

      - `bytes: Array[Float]`

        The bytes of the token.

      - `logprob: Float`

        The log probability of the token.

    - `usage: { input_tokens, output_tokens, total_tokens, 2 more} | { seconds, type}`

      Token usage statistics for the request.

      - `class Tokens`

        Usage statistics for models billed by token usage.

        - `input_tokens: Integer`

          Number of input tokens billed for this request.

        - `output_tokens: Integer`

          Number of output tokens generated.

        - `total_tokens: Integer`

          Total number of tokens used (input + output).

        - `type: :tokens`

          The type of the usage object. Always `tokens` for this variant.

          - `:tokens`

        - `input_token_details: { audio_tokens, text_tokens}`

          Details about the input tokens billed for this request.

          - `audio_tokens: Integer`

            Number of audio tokens billed for this request.

          - `text_tokens: Integer`

            Number of text tokens billed for this request.

      - `class Duration`

        Usage statistics for models billed by audio input duration.

        - `seconds: Float`

          Duration of the input audio in seconds.

        - `type: :duration`

          The type of the usage object. Always `duration` for this variant.

          - `:duration`

  - `class TranscriptionDiarized`

    Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

    - `duration: Float`

      Duration of the input audio in seconds.

    - `segments: Array[TranscriptionDiarizedSegment]`

      Segments of the transcript annotated with timestamps and speaker labels.

      - `id: String`

        Unique identifier for the segment.

      - `end_: Float`

        End timestamp of the segment in seconds.

      - `speaker: String`

        Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

      - `start: Float`

        Start timestamp of the segment in seconds.

      - `text: String`

        Transcript text for this segment.

      - `type: :"transcript.text.segment"`

        The type of the segment. Always `transcript.text.segment`.

        - `:"transcript.text.segment"`

    - `task: :transcribe`

      The type of task that was run. Always `transcribe`.

      - `:transcribe`

    - `text: String`

      The concatenated transcript text for the entire audio input.

    - `usage: { input_tokens, output_tokens, total_tokens, 2 more} | { seconds, type}`

      Token or duration usage statistics for the request.

      - `class Tokens`

        Usage statistics for models billed by token usage.

        - `input_tokens: Integer`

          Number of input tokens billed for this request.

        - `output_tokens: Integer`

          Number of output tokens generated.

        - `total_tokens: Integer`

          Total number of tokens used (input + output).

        - `type: :tokens`

          The type of the usage object. Always `tokens` for this variant.

          - `:tokens`

        - `input_token_details: { audio_tokens, text_tokens}`

          Details about the input tokens billed for this request.

          - `audio_tokens: Integer`

            Number of audio tokens billed for this request.

          - `text_tokens: Integer`

            Number of text tokens billed for this request.

      - `class Duration`

        Usage statistics for models billed by audio input duration.

        - `seconds: Float`

          Duration of the input audio in seconds.

        - `type: :duration`

          The type of the usage object. Always `duration` for this variant.

          - `:duration`

  - `class TranscriptionVerbose`

    Represents a verbose json transcription response returned by model, based on the provided input.

    - `duration: Float`

      The duration of the input audio.

    - `language: String`

      The language of the input audio.

    - `text: String`

      The transcribed text.

    - `segments: Array[TranscriptionSegment]`

      Segments of the transcribed text and their corresponding details.

      - `id: Integer`

        Unique identifier of the segment.

      - `avg_logprob: Float`

        Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

      - `compression_ratio: Float`

        Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

      - `end_: Float`

        End time of the segment in seconds.

      - `no_speech_prob: Float`

        Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

      - `seek: Integer`

        Seek offset of the segment.

      - `start: Float`

        Start time of the segment in seconds.

      - `temperature: Float`

        Temperature parameter used for generating the segment.

      - `text: String`

        Text content of the segment.

      - `tokens: Array[Integer]`

        Array of token IDs for the text content.

    - `usage: { seconds, type}`

      Usage statistics for models billed by audio input duration.

      - `seconds: Float`

        Duration of the input audio in seconds.

      - `type: :duration`

        The type of the usage object. Always `duration` for this variant.

        - `:duration`

    - `words: Array[TranscriptionWord]`

      Extracted words and their corresponding timestamps.

      - `end_: Float`

        End time of the word in seconds.

      - `start: Float`

        Start time of the word in seconds.

      - `word: String`

        The text content of the word.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

transcription = openai.audio.transcriptions.create(file: Pathname(__FILE__), model: :"gpt-4o-transcribe")

puts(transcription)
```

#### Domain Types

#### Transcription

- `class Transcription`

  Represents a transcription response returned by model, based on the provided input.

  - `text: String`

    The transcribed text.

  - `logprobs: Array[{ token, bytes, logprob}]`

    The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

    - `token: String`

      The token in the transcription.

    - `bytes: Array[Float]`

      The bytes of the token.

    - `logprob: Float`

      The log probability of the token.

  - `usage: { input_tokens, output_tokens, total_tokens, 2 more} | { seconds, type}`

    Token usage statistics for the request.

    - `class Tokens`

      Usage statistics for models billed by token usage.

      - `input_tokens: Integer`

        Number of input tokens billed for this request.

      - `output_tokens: Integer`

        Number of output tokens generated.

      - `total_tokens: Integer`

        Total number of tokens used (input + output).

      - `type: :tokens`

        The type of the usage object. Always `tokens` for this variant.

        - `:tokens`

      - `input_token_details: { audio_tokens, text_tokens}`

        Details about the input tokens billed for this request.

        - `audio_tokens: Integer`

          Number of audio tokens billed for this request.

        - `text_tokens: Integer`

          Number of text tokens billed for this request.

    - `class Duration`

      Usage statistics for models billed by audio input duration.

      - `seconds: Float`

        Duration of the input audio in seconds.

      - `type: :duration`

        The type of the usage object. Always `duration` for this variant.

        - `:duration`

#### Transcription Diarized

- `class TranscriptionDiarized`

  Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

  - `duration: Float`

    Duration of the input audio in seconds.

  - `segments: Array[TranscriptionDiarizedSegment]`

    Segments of the transcript annotated with timestamps and speaker labels.

    - `id: String`

      Unique identifier for the segment.

    - `end_: Float`

      End timestamp of the segment in seconds.

    - `speaker: String`

      Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

    - `start: Float`

      Start timestamp of the segment in seconds.

    - `text: String`

      Transcript text for this segment.

    - `type: :"transcript.text.segment"`

      The type of the segment. Always `transcript.text.segment`.

      - `:"transcript.text.segment"`

  - `task: :transcribe`

    The type of task that was run. Always `transcribe`.

    - `:transcribe`

  - `text: String`

    The concatenated transcript text for the entire audio input.

  - `usage: { input_tokens, output_tokens, total_tokens, 2 more} | { seconds, type}`

    Token or duration usage statistics for the request.

    - `class Tokens`

      Usage statistics for models billed by token usage.

      - `input_tokens: Integer`

        Number of input tokens billed for this request.

      - `output_tokens: Integer`

        Number of output tokens generated.

      - `total_tokens: Integer`

        Total number of tokens used (input + output).

      - `type: :tokens`

        The type of the usage object. Always `tokens` for this variant.

        - `:tokens`

      - `input_token_details: { audio_tokens, text_tokens}`

        Details about the input tokens billed for this request.

        - `audio_tokens: Integer`

          Number of audio tokens billed for this request.

        - `text_tokens: Integer`

          Number of text tokens billed for this request.

    - `class Duration`

      Usage statistics for models billed by audio input duration.

      - `seconds: Float`

        Duration of the input audio in seconds.

      - `type: :duration`

        The type of the usage object. Always `duration` for this variant.

        - `:duration`

#### Transcription Diarized Segment

- `class TranscriptionDiarizedSegment`

  A segment of diarized transcript text with speaker metadata.

  - `id: String`

    Unique identifier for the segment.

  - `end_: Float`

    End timestamp of the segment in seconds.

  - `speaker: String`

    Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

  - `start: Float`

    Start timestamp of the segment in seconds.

  - `text: String`

    Transcript text for this segment.

  - `type: :"transcript.text.segment"`

    The type of the segment. Always `transcript.text.segment`.

    - `:"transcript.text.segment"`

#### Transcription Include

- `TranscriptionInclude = :logprobs`

  - `:logprobs`

#### Transcription Segment

- `class TranscriptionSegment`

  - `id: Integer`

    Unique identifier of the segment.

  - `avg_logprob: Float`

    Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

  - `compression_ratio: Float`

    Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

  - `end_: Float`

    End time of the segment in seconds.

  - `no_speech_prob: Float`

    Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

  - `seek: Integer`

    Seek offset of the segment.

  - `start: Float`

    Start time of the segment in seconds.

  - `temperature: Float`

    Temperature parameter used for generating the segment.

  - `text: String`

    Text content of the segment.

  - `tokens: Array[Integer]`

    Array of token IDs for the text content.

#### Transcription Stream Event

- `TranscriptionStreamEvent = TranscriptionTextSegmentEvent | TranscriptionTextDeltaEvent | TranscriptionTextDoneEvent`

  Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

  - `class TranscriptionTextSegmentEvent`

    Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

    - `id: String`

      Unique identifier for the segment.

    - `end_: Float`

      End timestamp of the segment in seconds.

    - `speaker: String`

      Speaker label for this segment.

    - `start: Float`

      Start timestamp of the segment in seconds.

    - `text: String`

      Transcript text for this segment.

    - `type: :"transcript.text.segment"`

      The type of the event. Always `transcript.text.segment`.

      - `:"transcript.text.segment"`

  - `class TranscriptionTextDeltaEvent`

    Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

    - `delta: String`

      The text delta that was additionally transcribed.

    - `type: :"transcript.text.delta"`

      The type of the event. Always `transcript.text.delta`.

      - `:"transcript.text.delta"`

    - `logprobs: Array[{ token, bytes, logprob}]`

      The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

      - `token: String`

        The token that was used to generate the log probability.

      - `bytes: Array[Integer]`

        The bytes that were used to generate the log probability.

      - `logprob: Float`

        The log probability of the token.

    - `segment_id: String`

      Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

  - `class TranscriptionTextDoneEvent`

    Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

    - `text: String`

      The text that was transcribed.

    - `type: :"transcript.text.done"`

      The type of the event. Always `transcript.text.done`.

      - `:"transcript.text.done"`

    - `logprobs: Array[{ token, bytes, logprob}]`

      The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

      - `token: String`

        The token that was used to generate the log probability.

      - `bytes: Array[Integer]`

        The bytes that were used to generate the log probability.

      - `logprob: Float`

        The log probability of the token.

    - `usage: { input_tokens, output_tokens, total_tokens, 2 more}`

      Usage statistics for models billed by token usage.

      - `input_tokens: Integer`

        Number of input tokens billed for this request.

      - `output_tokens: Integer`

        Number of output tokens generated.

      - `total_tokens: Integer`

        Total number of tokens used (input + output).

      - `type: :tokens`

        The type of the usage object. Always `tokens` for this variant.

        - `:tokens`

      - `input_token_details: { audio_tokens, text_tokens}`

        Details about the input tokens billed for this request.

        - `audio_tokens: Integer`

          Number of audio tokens billed for this request.

        - `text_tokens: Integer`

          Number of text tokens billed for this request.

#### Transcription Text Delta Event

- `class TranscriptionTextDeltaEvent`

  Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

  - `delta: String`

    The text delta that was additionally transcribed.

  - `type: :"transcript.text.delta"`

    The type of the event. Always `transcript.text.delta`.

    - `:"transcript.text.delta"`

  - `logprobs: Array[{ token, bytes, logprob}]`

    The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

    - `token: String`

      The token that was used to generate the log probability.

    - `bytes: Array[Integer]`

      The bytes that were used to generate the log probability.

    - `logprob: Float`

      The log probability of the token.

  - `segment_id: String`

    Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

#### Transcription Text Done Event

- `class TranscriptionTextDoneEvent`

  Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

  - `text: String`

    The text that was transcribed.

  - `type: :"transcript.text.done"`

    The type of the event. Always `transcript.text.done`.

    - `:"transcript.text.done"`

  - `logprobs: Array[{ token, bytes, logprob}]`

    The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

    - `token: String`

      The token that was used to generate the log probability.

    - `bytes: Array[Integer]`

      The bytes that were used to generate the log probability.

    - `logprob: Float`

      The log probability of the token.

  - `usage: { input_tokens, output_tokens, total_tokens, 2 more}`

    Usage statistics for models billed by token usage.

    - `input_tokens: Integer`

      Number of input tokens billed for this request.

    - `output_tokens: Integer`

      Number of output tokens generated.

    - `total_tokens: Integer`

      Total number of tokens used (input + output).

    - `type: :tokens`

      The type of the usage object. Always `tokens` for this variant.

      - `:tokens`

    - `input_token_details: { audio_tokens, text_tokens}`

      Details about the input tokens billed for this request.

      - `audio_tokens: Integer`

        Number of audio tokens billed for this request.

      - `text_tokens: Integer`

        Number of text tokens billed for this request.

#### Transcription Text Segment Event

- `class TranscriptionTextSegmentEvent`

  Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

  - `id: String`

    Unique identifier for the segment.

  - `end_: Float`

    End timestamp of the segment in seconds.

  - `speaker: String`

    Speaker label for this segment.

  - `start: Float`

    Start timestamp of the segment in seconds.

  - `text: String`

    Transcript text for this segment.

  - `type: :"transcript.text.segment"`

    The type of the event. Always `transcript.text.segment`.

    - `:"transcript.text.segment"`

#### Transcription Verbose

- `class TranscriptionVerbose`

  Represents a verbose json transcription response returned by model, based on the provided input.

  - `duration: Float`

    The duration of the input audio.

  - `language: String`

    The language of the input audio.

  - `text: String`

    The transcribed text.

  - `segments: Array[TranscriptionSegment]`

    Segments of the transcribed text and their corresponding details.

    - `id: Integer`

      Unique identifier of the segment.

    - `avg_logprob: Float`

      Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

    - `compression_ratio: Float`

      Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

    - `end_: Float`

      End time of the segment in seconds.

    - `no_speech_prob: Float`

      Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

    - `seek: Integer`

      Seek offset of the segment.

    - `start: Float`

      Start time of the segment in seconds.

    - `temperature: Float`

      Temperature parameter used for generating the segment.

    - `text: String`

      Text content of the segment.

    - `tokens: Array[Integer]`

      Array of token IDs for the text content.

  - `usage: { seconds, type}`

    Usage statistics for models billed by audio input duration.

    - `seconds: Float`

      Duration of the input audio in seconds.

    - `type: :duration`

      The type of the usage object. Always `duration` for this variant.

      - `:duration`

  - `words: Array[TranscriptionWord]`

    Extracted words and their corresponding timestamps.

    - `end_: Float`

      End time of the word in seconds.

    - `start: Float`

      Start time of the word in seconds.

    - `word: String`

      The text content of the word.

#### Transcription Word

- `class TranscriptionWord`

  - `end_: Float`

    End time of the word in seconds.

  - `start: Float`

    Start time of the word in seconds.

  - `word: String`

    The text content of the word.

## Translations

### Create

`audio.translations.create(**kwargs) -> TranslationCreateResponse`

**post** `/audio/translations`

Translates audio into English.

#### Parameters

- `file: String`

  The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

- `model: String | AudioModel`

  ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

  - `String`

  - `AudioModel = :"whisper-1" | :"gpt-4o-transcribe" | :"gpt-4o-mini-transcribe" | 2 more`

    - `:"whisper-1"`

    - `:"gpt-4o-transcribe"`

    - `:"gpt-4o-mini-transcribe"`

    - `:"gpt-4o-mini-transcribe-2025-12-15"`

    - `:"gpt-4o-transcribe-diarize"`

- `prompt: String`

  An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

- `response_format: :json | :text | :srt | 2 more`

  The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

  - `:json`

  - `:text`

  - `:srt`

  - `:verbose_json`

  - `:vtt`

- `temperature: Float`

  The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

#### Returns

- `TranslationCreateResponse = Translation | TranslationVerbose`

  - `class Translation`

    - `text: String`

  - `class TranslationVerbose`

    - `duration: Float`

      The duration of the input audio.

    - `language: String`

      The language of the output translation (always `english`).

    - `text: String`

      The translated text.

    - `segments: Array[TranscriptionSegment]`

      Segments of the translated text and their corresponding details.

      - `id: Integer`

        Unique identifier of the segment.

      - `avg_logprob: Float`

        Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

      - `compression_ratio: Float`

        Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

      - `end_: Float`

        End time of the segment in seconds.

      - `no_speech_prob: Float`

        Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

      - `seek: Integer`

        Seek offset of the segment.

      - `start: Float`

        Start time of the segment in seconds.

      - `temperature: Float`

        Temperature parameter used for generating the segment.

      - `text: String`

        Text content of the segment.

      - `tokens: Array[Integer]`

        Array of token IDs for the text content.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

translation = openai.audio.translations.create(file: Pathname(__FILE__), model: :"whisper-1")

puts(translation)
```

#### Domain Types

#### Translation

- `class Translation`

  - `text: String`

#### Translation Verbose

- `class TranslationVerbose`

  - `duration: Float`

    The duration of the input audio.

  - `language: String`

    The language of the output translation (always `english`).

  - `text: String`

    The translated text.

  - `segments: Array[TranscriptionSegment]`

    Segments of the translated text and their corresponding details.

    - `id: Integer`

      Unique identifier of the segment.

    - `avg_logprob: Float`

      Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

    - `compression_ratio: Float`

      Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

    - `end_: Float`

      End time of the segment in seconds.

    - `no_speech_prob: Float`

      Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

    - `seek: Integer`

      Seek offset of the segment.

    - `start: Float`

      Start time of the segment in seconds.

    - `temperature: Float`

      Temperature parameter used for generating the segment.

    - `text: String`

      Text content of the segment.

    - `tokens: Array[Integer]`

      Array of token IDs for the text content.

## Speech

### Create

`audio.speech.create(**kwargs) -> StringIO`

**post** `/audio/speech`

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

#### Parameters

- `input: String`

  The text to generate audio for. The maximum length is 4096 characters.

- `model: String | SpeechModel`

  One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

  - `String`

  - `SpeechModel = :"tts-1" | :"tts-1-hd" | :"gpt-4o-mini-tts" | :"gpt-4o-mini-tts-2025-12-15"`

    - `:"tts-1"`

    - `:"tts-1-hd"`

    - `:"gpt-4o-mini-tts"`

    - `:"gpt-4o-mini-tts-2025-12-15"`

- `voice: String | :alloy | :ash | :ballad | 7 more | { id}`

  The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

  - `String`

  - `:alloy | :ash | :ballad | 7 more`

    - `:alloy`

    - `:ash`

    - `:ballad`

    - `:coral`

    - `:echo`

    - `:sage`

    - `:shimmer`

    - `:verse`

    - `:marin`

    - `:cedar`

  - `class ID`

    Custom voice reference.

    - `id: String`

      The custom voice ID, e.g. `voice_1234`.

- `instructions: String`

  Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

- `response_format: :mp3 | :opus | :aac | 3 more`

  The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

  - `:mp3`

  - `:opus`

  - `:aac`

  - `:flac`

  - `:wav`

  - `:pcm`

- `speed: Float`

  The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

- `stream_format: :sse | :audio`

  The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

  - `:sse`

  - `:audio`

#### Returns

- `StringIO`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

speech = openai.audio.speech.create(input: "input", model: :"tts-1", voice: "string")

puts(speech)
```

#### Domain Types

#### Speech Model

- `SpeechModel = :"tts-1" | :"tts-1-hd" | :"gpt-4o-mini-tts" | :"gpt-4o-mini-tts-2025-12-15"`

  - `:"tts-1"`

  - `:"tts-1-hd"`

  - `:"gpt-4o-mini-tts"`

  - `:"gpt-4o-mini-tts-2025-12-15"`

## Voices

## Voice Consents
