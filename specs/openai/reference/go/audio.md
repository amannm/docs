# Audio

## Domain Types

### Audio Model

- `type AudioModel string`

  - `const AudioModelWhisper1 AudioModel = "whisper-1"`

  - `const AudioModelGPT4oTranscribe AudioModel = "gpt-4o-transcribe"`

  - `const AudioModelGPT4oMiniTranscribe AudioModel = "gpt-4o-mini-transcribe"`

  - `const AudioModelGPT4oMiniTranscribe2025_12_15 AudioModel = "gpt-4o-mini-transcribe-2025-12-15"`

  - `const AudioModelGPT4oTranscribeDiarize AudioModel = "gpt-4o-transcribe-diarize"`

### Audio Response Format

- `type AudioResponseFormat string`

  The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

  - `const AudioResponseFormatJSON AudioResponseFormat = "json"`

  - `const AudioResponseFormatText AudioResponseFormat = "text"`

  - `const AudioResponseFormatSRT AudioResponseFormat = "srt"`

  - `const AudioResponseFormatVerboseJSON AudioResponseFormat = "verbose_json"`

  - `const AudioResponseFormatVTT AudioResponseFormat = "vtt"`

  - `const AudioResponseFormatDiarizedJSON AudioResponseFormat = "diarized_json"`

## Transcriptions

### Create

`client.Audio.Transcriptions.New(ctx, body) (*AudioTranscriptionNewResponseUnion, error)`

**post** `/audio/transcriptions`

Transcribes audio into the input language.

Returns a transcription object in `json`, `diarized_json`, or `verbose_json`
format, or a stream of transcript events.

#### Parameters

- `body AudioTranscriptionNewParams`

  - `File param.Field[Reader]`

    The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

  - `Model param.Field[AudioModel]`

    ID of the model to use. The options are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `whisper-1` (which is powered by our open source Whisper V2 model), and `gpt-4o-transcribe-diarize`.

    - `string`

    - `type AudioModel string`

      - `const AudioModelWhisper1 AudioModel = "whisper-1"`

      - `const AudioModelGPT4oTranscribe AudioModel = "gpt-4o-transcribe"`

      - `const AudioModelGPT4oMiniTranscribe AudioModel = "gpt-4o-mini-transcribe"`

      - `const AudioModelGPT4oMiniTranscribe2025_12_15 AudioModel = "gpt-4o-mini-transcribe-2025-12-15"`

      - `const AudioModelGPT4oTranscribeDiarize AudioModel = "gpt-4o-transcribe-diarize"`

  - `ChunkingStrategy param.Field[AudioTranscriptionNewParamsChunkingStrategyUnion]`

    Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block. Required when using `gpt-4o-transcribe-diarize` for inputs longer than 30 seconds.

    - `Auto`

      - `const AutoAuto Auto = "auto"`

    - `AudioTranscriptionNewParamsChunkingStrategyVadConfig`

      - `Type string`

        Must be set to `server_vad` to enable manual chunking using server side VAD.

        - `const AudioTranscriptionNewParamsChunkingStrategyVadConfigTypeServerVad AudioTranscriptionNewParamsChunkingStrategyVadConfigType = "server_vad"`

      - `PrefixPaddingMs int64`

        Amount of audio to include before the VAD detected speech (in
        milliseconds).

      - `SilenceDurationMs int64`

        Duration of silence to detect speech stop (in milliseconds).
        With shorter values the model will respond more quickly,
        but may jump in on short pauses from the user.

      - `Threshold float64`

        Sensitivity threshold (0.0 to 1.0) for voice activity detection. A
        higher threshold will require louder audio to activate the model, and
        thus might perform better in noisy environments.

  - `Include param.Field[[]TranscriptionInclude]`

    Additional information to include in the transcription response.
    `logprobs` will return the log probabilities of the tokens in the
    response to understand the model's confidence in the transcription.
    `logprobs` only works with response_format set to `json` and only with
    the models `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `gpt-4o-mini-transcribe-2025-12-15`. This field is not supported when using `gpt-4o-transcribe-diarize`.

    - `const TranscriptionIncludeLogprobs TranscriptionInclude = "logprobs"`

  - `KnownSpeakerNames param.Field[[]string]`

    Optional list of speaker names that correspond to the audio samples provided in `known_speaker_references[]`. Each entry should be a short identifier (for example `customer` or `agent`). Up to 4 speakers are supported.

  - `KnownSpeakerReferences param.Field[[]string]`

    Optional list of audio samples (as [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)) that contain known speaker references matching `known_speaker_names[]`. Each sample must be between 2 and 10 seconds, and can use any of the same input audio formats supported by `file`.

  - `Language param.Field[string]`

    The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.

  - `Prompt param.Field[string]`

    An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language. This field is not supported when using `gpt-4o-transcribe-diarize`.

  - `ResponseFormat param.Field[AudioResponseFormat]`

    The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

  - ``

  - `Temperature param.Field[float64]`

    The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

  - `TimestampGranularities param.Field[[]string]`

    The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
    This option is not available for `gpt-4o-transcribe-diarize`.

    - `const AudioTranscriptionNewParamsTimestampGranularityWord AudioTranscriptionNewParamsTimestampGranularity = "word"`

    - `const AudioTranscriptionNewParamsTimestampGranularitySegment AudioTranscriptionNewParamsTimestampGranularity = "segment"`

#### Returns

- `type AudioTranscriptionNewResponseUnion interface{…}`

  Represents a transcription response returned by model, based on the provided input.

  - `type Transcription struct{…}`

    Represents a transcription response returned by model, based on the provided input.

    - `Text string`

      The transcribed text.

    - `Logprobs []TranscriptionLogprob`

      The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

      - `Token string`

        The token in the transcription.

      - `Bytes []float64`

        The bytes of the token.

      - `Logprob float64`

        The log probability of the token.

    - `Usage TranscriptionUsageUnion`

      Token usage statistics for the request.

      - `type TranscriptionUsageTokens struct{…}`

        Usage statistics for models billed by token usage.

        - `InputTokens int64`

          Number of input tokens billed for this request.

        - `OutputTokens int64`

          Number of output tokens generated.

        - `TotalTokens int64`

          Total number of tokens used (input + output).

        - `Type Tokens`

          The type of the usage object. Always `tokens` for this variant.

          - `const TokensTokens Tokens = "tokens"`

        - `InputTokenDetails TranscriptionUsageTokensInputTokenDetails`

          Details about the input tokens billed for this request.

          - `AudioTokens int64`

            Number of audio tokens billed for this request.

          - `TextTokens int64`

            Number of text tokens billed for this request.

      - `type TranscriptionUsageDuration struct{…}`

        Usage statistics for models billed by audio input duration.

        - `Seconds float64`

          Duration of the input audio in seconds.

        - `Type Duration`

          The type of the usage object. Always `duration` for this variant.

          - `const DurationDuration Duration = "duration"`

  - `type TranscriptionVerbose struct{…}`

    Represents a verbose json transcription response returned by model, based on the provided input.

    - `Duration float64`

      The duration of the input audio.

    - `Language string`

      The language of the input audio.

    - `Text string`

      The transcribed text.

    - `Segments []TranscriptionSegment`

      Segments of the transcribed text and their corresponding details.

      - `ID int64`

        Unique identifier of the segment.

      - `AvgLogprob float64`

        Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

      - `CompressionRatio float64`

        Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

      - `End float64`

        End time of the segment in seconds.

      - `NoSpeechProb float64`

        Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

      - `Seek int64`

        Seek offset of the segment.

      - `Start float64`

        Start time of the segment in seconds.

      - `Temperature float64`

        Temperature parameter used for generating the segment.

      - `Text string`

        Text content of the segment.

      - `Tokens []int64`

        Array of token IDs for the text content.

    - `Usage TranscriptionVerboseUsage`

      Usage statistics for models billed by audio input duration.

      - `Seconds float64`

        Duration of the input audio in seconds.

      - `Type Duration`

        The type of the usage object. Always `duration` for this variant.

        - `const DurationDuration Duration = "duration"`

    - `Words []TranscriptionWord`

      Extracted words and their corresponding timestamps.

      - `End float64`

        End time of the word in seconds.

      - `Start float64`

        Start time of the word in seconds.

      - `Word string`

        The text content of the word.

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
  transcription, err := client.Audio.Transcriptions.New(context.TODO(), openai.AudioTranscriptionNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
    Model: openai.AudioModelGPT4oTranscribe,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", transcription)
}
```

#### Domain Types

#### Transcription

- `type Transcription struct{…}`

  Represents a transcription response returned by model, based on the provided input.

  - `Text string`

    The transcribed text.

  - `Logprobs []TranscriptionLogprob`

    The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

    - `Token string`

      The token in the transcription.

    - `Bytes []float64`

      The bytes of the token.

    - `Logprob float64`

      The log probability of the token.

  - `Usage TranscriptionUsageUnion`

    Token usage statistics for the request.

    - `type TranscriptionUsageTokens struct{…}`

      Usage statistics for models billed by token usage.

      - `InputTokens int64`

        Number of input tokens billed for this request.

      - `OutputTokens int64`

        Number of output tokens generated.

      - `TotalTokens int64`

        Total number of tokens used (input + output).

      - `Type Tokens`

        The type of the usage object. Always `tokens` for this variant.

        - `const TokensTokens Tokens = "tokens"`

      - `InputTokenDetails TranscriptionUsageTokensInputTokenDetails`

        Details about the input tokens billed for this request.

        - `AudioTokens int64`

          Number of audio tokens billed for this request.

        - `TextTokens int64`

          Number of text tokens billed for this request.

    - `type TranscriptionUsageDuration struct{…}`

      Usage statistics for models billed by audio input duration.

      - `Seconds float64`

        Duration of the input audio in seconds.

      - `Type Duration`

        The type of the usage object. Always `duration` for this variant.

        - `const DurationDuration Duration = "duration"`

#### Transcription Diarized

- `type TranscriptionDiarized struct{…}`

  Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

  - `Duration float64`

    Duration of the input audio in seconds.

  - `Segments []TranscriptionDiarizedSegment`

    Segments of the transcript annotated with timestamps and speaker labels.

    - `ID string`

      Unique identifier for the segment.

    - `End float64`

      End timestamp of the segment in seconds.

    - `Speaker string`

      Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

    - `Start float64`

      Start timestamp of the segment in seconds.

    - `Text string`

      Transcript text for this segment.

    - `Type TranscriptTextSegment`

      The type of the segment. Always `transcript.text.segment`.

      - `const TranscriptTextSegmentTranscriptTextSegment TranscriptTextSegment = "transcript.text.segment"`

  - `Task Transcribe`

    The type of task that was run. Always `transcribe`.

    - `const TranscribeTranscribe Transcribe = "transcribe"`

  - `Text string`

    The concatenated transcript text for the entire audio input.

  - `Usage TranscriptionDiarizedUsageUnion`

    Token or duration usage statistics for the request.

    - `TranscriptionDiarizedUsageTokens`

      - `InputTokens int64`

        Number of input tokens billed for this request.

      - `OutputTokens int64`

        Number of output tokens generated.

      - `TotalTokens int64`

        Total number of tokens used (input + output).

      - `Type Tokens`

        The type of the usage object. Always `tokens` for this variant.

        - `const TokensTokens Tokens = "tokens"`

      - `InputTokenDetails TranscriptionDiarizedUsageTokensInputTokenDetails`

        Details about the input tokens billed for this request.

        - `AudioTokens int64`

          Number of audio tokens billed for this request.

        - `TextTokens int64`

          Number of text tokens billed for this request.

    - `TranscriptionDiarizedUsageDuration`

      - `Seconds float64`

        Duration of the input audio in seconds.

      - `Type Duration`

        The type of the usage object. Always `duration` for this variant.

        - `const DurationDuration Duration = "duration"`

#### Transcription Diarized Segment

- `type TranscriptionDiarizedSegment struct{…}`

  A segment of diarized transcript text with speaker metadata.

  - `ID string`

    Unique identifier for the segment.

  - `End float64`

    End timestamp of the segment in seconds.

  - `Speaker string`

    Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

  - `Start float64`

    Start timestamp of the segment in seconds.

  - `Text string`

    Transcript text for this segment.

  - `Type TranscriptTextSegment`

    The type of the segment. Always `transcript.text.segment`.

    - `const TranscriptTextSegmentTranscriptTextSegment TranscriptTextSegment = "transcript.text.segment"`

#### Transcription Include

- `type TranscriptionInclude string`

  - `const TranscriptionIncludeLogprobs TranscriptionInclude = "logprobs"`

#### Transcription Segment

- `type TranscriptionSegment struct{…}`

  - `ID int64`

    Unique identifier of the segment.

  - `AvgLogprob float64`

    Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

  - `CompressionRatio float64`

    Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

  - `End float64`

    End time of the segment in seconds.

  - `NoSpeechProb float64`

    Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

  - `Seek int64`

    Seek offset of the segment.

  - `Start float64`

    Start time of the segment in seconds.

  - `Temperature float64`

    Temperature parameter used for generating the segment.

  - `Text string`

    Text content of the segment.

  - `Tokens []int64`

    Array of token IDs for the text content.

#### Transcription Stream Event

- `type TranscriptionStreamEventUnion interface{…}`

  Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

  - `type TranscriptionTextSegmentEvent struct{…}`

    Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

    - `ID string`

      Unique identifier for the segment.

    - `End float64`

      End timestamp of the segment in seconds.

    - `Speaker string`

      Speaker label for this segment.

    - `Start float64`

      Start timestamp of the segment in seconds.

    - `Text string`

      Transcript text for this segment.

    - `Type TranscriptTextSegment`

      The type of the event. Always `transcript.text.segment`.

      - `const TranscriptTextSegmentTranscriptTextSegment TranscriptTextSegment = "transcript.text.segment"`

  - `type TranscriptionTextDeltaEvent struct{…}`

    Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

    - `Delta string`

      The text delta that was additionally transcribed.

    - `Type TranscriptTextDelta`

      The type of the event. Always `transcript.text.delta`.

      - `const TranscriptTextDeltaTranscriptTextDelta TranscriptTextDelta = "transcript.text.delta"`

    - `Logprobs []TranscriptionTextDeltaEventLogprob`

      The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

      - `Token string`

        The token that was used to generate the log probability.

      - `Bytes []int64`

        The bytes that were used to generate the log probability.

      - `Logprob float64`

        The log probability of the token.

    - `SegmentID string`

      Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

  - `type TranscriptionTextDoneEvent struct{…}`

    Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

    - `Text string`

      The text that was transcribed.

    - `Type TranscriptTextDone`

      The type of the event. Always `transcript.text.done`.

      - `const TranscriptTextDoneTranscriptTextDone TranscriptTextDone = "transcript.text.done"`

    - `Logprobs []TranscriptionTextDoneEventLogprob`

      The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

      - `Token string`

        The token that was used to generate the log probability.

      - `Bytes []int64`

        The bytes that were used to generate the log probability.

      - `Logprob float64`

        The log probability of the token.

    - `Usage TranscriptionTextDoneEventUsage`

      Usage statistics for models billed by token usage.

      - `InputTokens int64`

        Number of input tokens billed for this request.

      - `OutputTokens int64`

        Number of output tokens generated.

      - `TotalTokens int64`

        Total number of tokens used (input + output).

      - `Type Tokens`

        The type of the usage object. Always `tokens` for this variant.

        - `const TokensTokens Tokens = "tokens"`

      - `InputTokenDetails TranscriptionTextDoneEventUsageInputTokenDetails`

        Details about the input tokens billed for this request.

        - `AudioTokens int64`

          Number of audio tokens billed for this request.

        - `TextTokens int64`

          Number of text tokens billed for this request.

#### Transcription Text Delta Event

- `type TranscriptionTextDeltaEvent struct{…}`

  Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

  - `Delta string`

    The text delta that was additionally transcribed.

  - `Type TranscriptTextDelta`

    The type of the event. Always `transcript.text.delta`.

    - `const TranscriptTextDeltaTranscriptTextDelta TranscriptTextDelta = "transcript.text.delta"`

  - `Logprobs []TranscriptionTextDeltaEventLogprob`

    The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

    - `Token string`

      The token that was used to generate the log probability.

    - `Bytes []int64`

      The bytes that were used to generate the log probability.

    - `Logprob float64`

      The log probability of the token.

  - `SegmentID string`

    Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

#### Transcription Text Done Event

- `type TranscriptionTextDoneEvent struct{…}`

  Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

  - `Text string`

    The text that was transcribed.

  - `Type TranscriptTextDone`

    The type of the event. Always `transcript.text.done`.

    - `const TranscriptTextDoneTranscriptTextDone TranscriptTextDone = "transcript.text.done"`

  - `Logprobs []TranscriptionTextDoneEventLogprob`

    The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

    - `Token string`

      The token that was used to generate the log probability.

    - `Bytes []int64`

      The bytes that were used to generate the log probability.

    - `Logprob float64`

      The log probability of the token.

  - `Usage TranscriptionTextDoneEventUsage`

    Usage statistics for models billed by token usage.

    - `InputTokens int64`

      Number of input tokens billed for this request.

    - `OutputTokens int64`

      Number of output tokens generated.

    - `TotalTokens int64`

      Total number of tokens used (input + output).

    - `Type Tokens`

      The type of the usage object. Always `tokens` for this variant.

      - `const TokensTokens Tokens = "tokens"`

    - `InputTokenDetails TranscriptionTextDoneEventUsageInputTokenDetails`

      Details about the input tokens billed for this request.

      - `AudioTokens int64`

        Number of audio tokens billed for this request.

      - `TextTokens int64`

        Number of text tokens billed for this request.

#### Transcription Text Segment Event

- `type TranscriptionTextSegmentEvent struct{…}`

  Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

  - `ID string`

    Unique identifier for the segment.

  - `End float64`

    End timestamp of the segment in seconds.

  - `Speaker string`

    Speaker label for this segment.

  - `Start float64`

    Start timestamp of the segment in seconds.

  - `Text string`

    Transcript text for this segment.

  - `Type TranscriptTextSegment`

    The type of the event. Always `transcript.text.segment`.

    - `const TranscriptTextSegmentTranscriptTextSegment TranscriptTextSegment = "transcript.text.segment"`

#### Transcription Verbose

- `type TranscriptionVerbose struct{…}`

  Represents a verbose json transcription response returned by model, based on the provided input.

  - `Duration float64`

    The duration of the input audio.

  - `Language string`

    The language of the input audio.

  - `Text string`

    The transcribed text.

  - `Segments []TranscriptionSegment`

    Segments of the transcribed text and their corresponding details.

    - `ID int64`

      Unique identifier of the segment.

    - `AvgLogprob float64`

      Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

    - `CompressionRatio float64`

      Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

    - `End float64`

      End time of the segment in seconds.

    - `NoSpeechProb float64`

      Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

    - `Seek int64`

      Seek offset of the segment.

    - `Start float64`

      Start time of the segment in seconds.

    - `Temperature float64`

      Temperature parameter used for generating the segment.

    - `Text string`

      Text content of the segment.

    - `Tokens []int64`

      Array of token IDs for the text content.

  - `Usage TranscriptionVerboseUsage`

    Usage statistics for models billed by audio input duration.

    - `Seconds float64`

      Duration of the input audio in seconds.

    - `Type Duration`

      The type of the usage object. Always `duration` for this variant.

      - `const DurationDuration Duration = "duration"`

  - `Words []TranscriptionWord`

    Extracted words and their corresponding timestamps.

    - `End float64`

      End time of the word in seconds.

    - `Start float64`

      Start time of the word in seconds.

    - `Word string`

      The text content of the word.

#### Transcription Word

- `type TranscriptionWord struct{…}`

  - `End float64`

    End time of the word in seconds.

  - `Start float64`

    Start time of the word in seconds.

  - `Word string`

    The text content of the word.

## Translations

### Create

`client.Audio.Translations.New(ctx, body) (*Translation, error)`

**post** `/audio/translations`

Translates audio into English.

#### Parameters

- `body AudioTranslationNewParams`

  - `File param.Field[Reader]`

    The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

  - `Model param.Field[AudioModel]`

    ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

    - `string`

    - `type AudioModel string`

      - `const AudioModelWhisper1 AudioModel = "whisper-1"`

      - `const AudioModelGPT4oTranscribe AudioModel = "gpt-4o-transcribe"`

      - `const AudioModelGPT4oMiniTranscribe AudioModel = "gpt-4o-mini-transcribe"`

      - `const AudioModelGPT4oMiniTranscribe2025_12_15 AudioModel = "gpt-4o-mini-transcribe-2025-12-15"`

      - `const AudioModelGPT4oTranscribeDiarize AudioModel = "gpt-4o-transcribe-diarize"`

  - `Prompt param.Field[string]`

    An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

  - `ResponseFormat param.Field[AudioTranslationNewParamsResponseFormat]`

    The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

    - `const AudioTranslationNewParamsResponseFormatJSON AudioTranslationNewParamsResponseFormat = "json"`

    - `const AudioTranslationNewParamsResponseFormatText AudioTranslationNewParamsResponseFormat = "text"`

    - `const AudioTranslationNewParamsResponseFormatSRT AudioTranslationNewParamsResponseFormat = "srt"`

    - `const AudioTranslationNewParamsResponseFormatVerboseJSON AudioTranslationNewParamsResponseFormat = "verbose_json"`

    - `const AudioTranslationNewParamsResponseFormatVTT AudioTranslationNewParamsResponseFormat = "vtt"`

  - `Temperature param.Field[float64]`

    The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

#### Returns

- `type AudioTranslationNewResponse interface{…}`

  - `type Translation struct{…}`

    - `Text string`

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
  translation, err := client.Audio.Translations.New(context.TODO(), openai.AudioTranslationNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("some file contents"))),
    Model: openai.AudioModelWhisper1,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", translation)
}
```

#### Domain Types

#### Translation

- `type Translation struct{…}`

  - `Text string`

#### Translation Verbose

- `type TranslationVerbose struct{…}`

  - `Duration float64`

    The duration of the input audio.

  - `Language string`

    The language of the output translation (always `english`).

  - `Text string`

    The translated text.

  - `Segments []TranscriptionSegment`

    Segments of the translated text and their corresponding details.

    - `ID int64`

      Unique identifier of the segment.

    - `AvgLogprob float64`

      Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

    - `CompressionRatio float64`

      Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

    - `End float64`

      End time of the segment in seconds.

    - `NoSpeechProb float64`

      Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

    - `Seek int64`

      Seek offset of the segment.

    - `Start float64`

      Start time of the segment in seconds.

    - `Temperature float64`

      Temperature parameter used for generating the segment.

    - `Text string`

      Text content of the segment.

    - `Tokens []int64`

      Array of token IDs for the text content.

## Speech

### Create

`client.Audio.Speech.New(ctx, body) (*Response, error)`

**post** `/audio/speech`

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

#### Parameters

- `body AudioSpeechNewParams`

  - `Input param.Field[string]`

    The text to generate audio for. The maximum length is 4096 characters.

  - `Model param.Field[SpeechModel]`

    One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

    - `string`

    - `type SpeechModel string`

      - `const SpeechModelTTS1 SpeechModel = "tts-1"`

      - `const SpeechModelTTS1HD SpeechModel = "tts-1-hd"`

      - `const SpeechModelGPT4oMiniTTS SpeechModel = "gpt-4o-mini-tts"`

      - `const SpeechModelGPT4oMiniTTS2025_12_15 SpeechModel = "gpt-4o-mini-tts-2025-12-15"`

  - `Voice param.Field[AudioSpeechNewParamsVoiceUnion]`

    The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

    - `string`

    - `type AudioSpeechNewParamsVoiceString string`

      - `const AudioSpeechNewParamsVoiceStringAlloy AudioSpeechNewParamsVoiceString = "alloy"`

      - `const AudioSpeechNewParamsVoiceStringAsh AudioSpeechNewParamsVoiceString = "ash"`

      - `const AudioSpeechNewParamsVoiceStringBallad AudioSpeechNewParamsVoiceString = "ballad"`

      - `const AudioSpeechNewParamsVoiceStringCoral AudioSpeechNewParamsVoiceString = "coral"`

      - `const AudioSpeechNewParamsVoiceStringEcho AudioSpeechNewParamsVoiceString = "echo"`

      - `const AudioSpeechNewParamsVoiceStringSage AudioSpeechNewParamsVoiceString = "sage"`

      - `const AudioSpeechNewParamsVoiceStringShimmer AudioSpeechNewParamsVoiceString = "shimmer"`

      - `const AudioSpeechNewParamsVoiceStringVerse AudioSpeechNewParamsVoiceString = "verse"`

      - `const AudioSpeechNewParamsVoiceStringMarin AudioSpeechNewParamsVoiceString = "marin"`

      - `const AudioSpeechNewParamsVoiceStringCedar AudioSpeechNewParamsVoiceString = "cedar"`

    - `type AudioSpeechNewParamsVoiceID struct{…}`

      Custom voice reference.

      - `ID string`

        The custom voice ID, e.g. `voice_1234`.

  - `Instructions param.Field[string]`

    Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

  - `ResponseFormat param.Field[AudioSpeechNewParamsResponseFormat]`

    The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

    - `const AudioSpeechNewParamsResponseFormatMP3 AudioSpeechNewParamsResponseFormat = "mp3"`

    - `const AudioSpeechNewParamsResponseFormatOpus AudioSpeechNewParamsResponseFormat = "opus"`

    - `const AudioSpeechNewParamsResponseFormatAAC AudioSpeechNewParamsResponseFormat = "aac"`

    - `const AudioSpeechNewParamsResponseFormatFLAC AudioSpeechNewParamsResponseFormat = "flac"`

    - `const AudioSpeechNewParamsResponseFormatWAV AudioSpeechNewParamsResponseFormat = "wav"`

    - `const AudioSpeechNewParamsResponseFormatPCM AudioSpeechNewParamsResponseFormat = "pcm"`

  - `Speed param.Field[float64]`

    The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

  - `StreamFormat param.Field[AudioSpeechNewParamsStreamFormat]`

    The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

    - `const AudioSpeechNewParamsStreamFormatSSE AudioSpeechNewParamsStreamFormat = "sse"`

    - `const AudioSpeechNewParamsStreamFormatAudio AudioSpeechNewParamsStreamFormat = "audio"`

#### Returns

- `type AudioSpeechNewResponse interface{…}`

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
  speech, err := client.Audio.Speech.New(context.TODO(), openai.AudioSpeechNewParams{
    Input: "input",
    Model: openai.SpeechModelTTS1,
    Voice: openai.AudioSpeechNewParamsVoiceUnion{
      OfString: openai.String("string"),
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", speech)
}
```

#### Domain Types

#### Speech Model

- `type SpeechModel string`

  - `const SpeechModelTTS1 SpeechModel = "tts-1"`

  - `const SpeechModelTTS1HD SpeechModel = "tts-1-hd"`

  - `const SpeechModelGPT4oMiniTTS SpeechModel = "gpt-4o-mini-tts"`

  - `const SpeechModelGPT4oMiniTTS2025_12_15 SpeechModel = "gpt-4o-mini-tts-2025-12-15"`

## Voices

## Voice Consents
