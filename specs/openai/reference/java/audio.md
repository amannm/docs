# Audio

## Domain Types

### Audio Model

- `enum AudioModel:`

  - `WHISPER_1("whisper-1")`

  - `GPT_4O_TRANSCRIBE("gpt-4o-transcribe")`

  - `GPT_4O_MINI_TRANSCRIBE("gpt-4o-mini-transcribe")`

  - `GPT_4O_MINI_TRANSCRIBE_2025_12_15("gpt-4o-mini-transcribe-2025-12-15")`

  - `GPT_4O_TRANSCRIBE_DIARIZE("gpt-4o-transcribe-diarize")`

### Audio Response Format

- `enum AudioResponseFormat:`

  The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

  - `JSON("json")`

  - `TEXT("text")`

  - `SRT("srt")`

  - `VERBOSE_JSON("verbose_json")`

  - `VTT("vtt")`

  - `DIARIZED_JSON("diarized_json")`

## Transcriptions

### Create

`TranscriptionCreateResponse audio().transcriptions().create(TranscriptionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/audio/transcriptions`

Transcribes audio into the input language.

Returns a transcription object in `json`, `diarized_json`, or `verbose_json`
format, or a stream of transcript events.

#### Parameters

- `TranscriptionCreateParams params`

  - `String file`

    The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

  - `AudioModel model`

    ID of the model to use. The options are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `whisper-1` (which is powered by our open source Whisper V2 model), and `gpt-4o-transcribe-diarize`.

    - `WHISPER_1("whisper-1")`

    - `GPT_4O_TRANSCRIBE("gpt-4o-transcribe")`

    - `GPT_4O_MINI_TRANSCRIBE("gpt-4o-mini-transcribe")`

    - `GPT_4O_MINI_TRANSCRIBE_2025_12_15("gpt-4o-mini-transcribe-2025-12-15")`

    - `GPT_4O_TRANSCRIBE_DIARIZE("gpt-4o-transcribe-diarize")`

  - `Optional<ChunkingStrategy> chunkingStrategy`

    Controls how the audio is cut into chunks. When set to `"auto"`, the server first normalizes loudness and then uses voice activity detection (VAD) to choose boundaries. `server_vad` object can be provided to tweak VAD detection parameters manually. If unset, the audio is transcribed as a single block. Required when using `gpt-4o-transcribe-diarize` for inputs longer than 30 seconds.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class VadConfig:`

      - `Type type`

        Must be set to `server_vad` to enable manual chunking using server side VAD.

        - `SERVER_VAD("server_vad")`

      - `Optional<Long> prefixPaddingMs`

        Amount of audio to include before the VAD detected speech (in
        milliseconds).

      - `Optional<Long> silenceDurationMs`

        Duration of silence to detect speech stop (in milliseconds).
        With shorter values the model will respond more quickly,
        but may jump in on short pauses from the user.

      - `Optional<Double> threshold`

        Sensitivity threshold (0.0 to 1.0) for voice activity detection. A
        higher threshold will require louder audio to activate the model, and
        thus might perform better in noisy environments.

  - `Optional<List<TranscriptionInclude>> include`

    Additional information to include in the transcription response.
    `logprobs` will return the log probabilities of the tokens in the
    response to understand the model's confidence in the transcription.
    `logprobs` only works with response_format set to `json` and only with
    the models `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `gpt-4o-mini-transcribe-2025-12-15`. This field is not supported when using `gpt-4o-transcribe-diarize`.

    - `LOGPROBS("logprobs")`

  - `Optional<List<String>> knownSpeakerNames`

    Optional list of speaker names that correspond to the audio samples provided in `known_speaker_references[]`. Each entry should be a short identifier (for example `customer` or `agent`). Up to 4 speakers are supported.

  - `Optional<List<String>> knownSpeakerReferences`

    Optional list of audio samples (as [data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs)) that contain known speaker references matching `known_speaker_names[]`. Each sample must be between 2 and 10 seconds, and can use any of the same input audio formats supported by `file`.

  - `Optional<String> language`

    The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format will improve accuracy and latency.

  - `Optional<String> prompt`

    An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language. This field is not supported when using `gpt-4o-transcribe-diarize`.

  - `Optional<AudioResponseFormat> responseFormat`

    The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, `vtt`, or `diarized_json`. For `gpt-4o-transcribe` and `gpt-4o-mini-transcribe`, the only supported format is `json`. For `gpt-4o-transcribe-diarize`, the supported formats are `json`, `text`, and `diarized_json`, with `diarized_json` required to receive speaker annotations.

  - `Optional<Double> temperature`

    The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

  - `Optional<List<TimestampGranularity>> timestampGranularities`

    The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
    This option is not available for `gpt-4o-transcribe-diarize`.

    - `WORD("word")`

    - `SEGMENT("segment")`

#### Returns

- `class TranscriptionCreateResponse: A class that can be one of several variants.union`

  Represents a transcription response returned by model, based on the provided input.

  - `class Transcription:`

    Represents a transcription response returned by model, based on the provided input.

    - `String text`

      The transcribed text.

    - `Optional<List<Logprob>> logprobs`

      The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

      - `Optional<String> token`

        The token in the transcription.

      - `Optional<List<Double>> bytes`

        The bytes of the token.

      - `Optional<Double> logprob`

        The log probability of the token.

    - `Optional<Usage> usage`

      Token usage statistics for the request.

      - `class Tokens:`

        Usage statistics for models billed by token usage.

        - `long inputTokens`

          Number of input tokens billed for this request.

        - `long outputTokens`

          Number of output tokens generated.

        - `long totalTokens`

          Total number of tokens used (input + output).

        - `JsonValue; type "tokens"constant`

          The type of the usage object. Always `tokens` for this variant.

          - `TOKENS("tokens")`

        - `Optional<InputTokenDetails> inputTokenDetails`

          Details about the input tokens billed for this request.

          - `Optional<Long> audioTokens`

            Number of audio tokens billed for this request.

          - `Optional<Long> textTokens`

            Number of text tokens billed for this request.

      - `class Duration:`

        Usage statistics for models billed by audio input duration.

        - `double seconds`

          Duration of the input audio in seconds.

        - `JsonValue; type "duration"constant`

          The type of the usage object. Always `duration` for this variant.

          - `DURATION("duration")`

  - `class TranscriptionDiarized:`

    Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

    - `double duration`

      Duration of the input audio in seconds.

    - `List<TranscriptionDiarizedSegment> segments`

      Segments of the transcript annotated with timestamps and speaker labels.

      - `String id`

        Unique identifier for the segment.

      - `double end`

        End timestamp of the segment in seconds.

      - `String speaker`

        Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

      - `double start`

        Start timestamp of the segment in seconds.

      - `String text`

        Transcript text for this segment.

      - `JsonValue; type "transcript.text.segment"constant`

        The type of the segment. Always `transcript.text.segment`.

        - `TRANSCRIPT_TEXT_SEGMENT("transcript.text.segment")`

    - `JsonValue; task "transcribe"constant`

      The type of task that was run. Always `transcribe`.

      - `TRANSCRIBE("transcribe")`

    - `String text`

      The concatenated transcript text for the entire audio input.

    - `Optional<Usage> usage`

      Token or duration usage statistics for the request.

      - `class Tokens:`

        Usage statistics for models billed by token usage.

        - `long inputTokens`

          Number of input tokens billed for this request.

        - `long outputTokens`

          Number of output tokens generated.

        - `long totalTokens`

          Total number of tokens used (input + output).

        - `JsonValue; type "tokens"constant`

          The type of the usage object. Always `tokens` for this variant.

          - `TOKENS("tokens")`

        - `Optional<InputTokenDetails> inputTokenDetails`

          Details about the input tokens billed for this request.

          - `Optional<Long> audioTokens`

            Number of audio tokens billed for this request.

          - `Optional<Long> textTokens`

            Number of text tokens billed for this request.

      - `class Duration:`

        Usage statistics for models billed by audio input duration.

        - `double seconds`

          Duration of the input audio in seconds.

        - `JsonValue; type "duration"constant`

          The type of the usage object. Always `duration` for this variant.

          - `DURATION("duration")`

  - `class TranscriptionVerbose:`

    Represents a verbose json transcription response returned by model, based on the provided input.

    - `double duration`

      The duration of the input audio.

    - `String language`

      The language of the input audio.

    - `String text`

      The transcribed text.

    - `Optional<List<TranscriptionSegment>> segments`

      Segments of the transcribed text and their corresponding details.

      - `long id`

        Unique identifier of the segment.

      - `double avgLogprob`

        Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

      - `double compressionRatio`

        Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

      - `double end`

        End time of the segment in seconds.

      - `double noSpeechProb`

        Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

      - `long seek`

        Seek offset of the segment.

      - `double start`

        Start time of the segment in seconds.

      - `double temperature`

        Temperature parameter used for generating the segment.

      - `String text`

        Text content of the segment.

      - `List<long> tokens`

        Array of token IDs for the text content.

    - `Optional<Usage> usage`

      Usage statistics for models billed by audio input duration.

      - `double seconds`

        Duration of the input audio in seconds.

      - `JsonValue; type "duration"constant`

        The type of the usage object. Always `duration` for this variant.

        - `DURATION("duration")`

    - `Optional<List<TranscriptionWord>> words`

      Extracted words and their corresponding timestamps.

      - `double end`

        End time of the word in seconds.

      - `double start`

        Start time of the word in seconds.

      - `String word`

        The text content of the word.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.audio.AudioModel;
import com.openai.models.audio.transcriptions.TranscriptionCreateParams;
import com.openai.models.audio.transcriptions.TranscriptionCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TranscriptionCreateParams params = TranscriptionCreateParams.builder()
            .file(ByteArrayInputStream("some content".getBytes()))
            .model(AudioModel.GPT_4O_TRANSCRIBE)
            .build();
        TranscriptionCreateResponse transcription = client.audio().transcriptions().create(params);
    }
}
```

#### Domain Types

#### Transcription

- `class Transcription:`

  Represents a transcription response returned by model, based on the provided input.

  - `String text`

    The transcribed text.

  - `Optional<List<Logprob>> logprobs`

    The log probabilities of the tokens in the transcription. Only returned with the models `gpt-4o-transcribe` and `gpt-4o-mini-transcribe` if `logprobs` is added to the `include` array.

    - `Optional<String> token`

      The token in the transcription.

    - `Optional<List<Double>> bytes`

      The bytes of the token.

    - `Optional<Double> logprob`

      The log probability of the token.

  - `Optional<Usage> usage`

    Token usage statistics for the request.

    - `class Tokens:`

      Usage statistics for models billed by token usage.

      - `long inputTokens`

        Number of input tokens billed for this request.

      - `long outputTokens`

        Number of output tokens generated.

      - `long totalTokens`

        Total number of tokens used (input + output).

      - `JsonValue; type "tokens"constant`

        The type of the usage object. Always `tokens` for this variant.

        - `TOKENS("tokens")`

      - `Optional<InputTokenDetails> inputTokenDetails`

        Details about the input tokens billed for this request.

        - `Optional<Long> audioTokens`

          Number of audio tokens billed for this request.

        - `Optional<Long> textTokens`

          Number of text tokens billed for this request.

    - `class Duration:`

      Usage statistics for models billed by audio input duration.

      - `double seconds`

        Duration of the input audio in seconds.

      - `JsonValue; type "duration"constant`

        The type of the usage object. Always `duration` for this variant.

        - `DURATION("duration")`

#### Transcription Diarized

- `class TranscriptionDiarized:`

  Represents a diarized transcription response returned by the model, including the combined transcript and speaker-segment annotations.

  - `double duration`

    Duration of the input audio in seconds.

  - `List<TranscriptionDiarizedSegment> segments`

    Segments of the transcript annotated with timestamps and speaker labels.

    - `String id`

      Unique identifier for the segment.

    - `double end`

      End timestamp of the segment in seconds.

    - `String speaker`

      Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

    - `double start`

      Start timestamp of the segment in seconds.

    - `String text`

      Transcript text for this segment.

    - `JsonValue; type "transcript.text.segment"constant`

      The type of the segment. Always `transcript.text.segment`.

      - `TRANSCRIPT_TEXT_SEGMENT("transcript.text.segment")`

  - `JsonValue; task "transcribe"constant`

    The type of task that was run. Always `transcribe`.

    - `TRANSCRIBE("transcribe")`

  - `String text`

    The concatenated transcript text for the entire audio input.

  - `Optional<Usage> usage`

    Token or duration usage statistics for the request.

    - `class Tokens:`

      Usage statistics for models billed by token usage.

      - `long inputTokens`

        Number of input tokens billed for this request.

      - `long outputTokens`

        Number of output tokens generated.

      - `long totalTokens`

        Total number of tokens used (input + output).

      - `JsonValue; type "tokens"constant`

        The type of the usage object. Always `tokens` for this variant.

        - `TOKENS("tokens")`

      - `Optional<InputTokenDetails> inputTokenDetails`

        Details about the input tokens billed for this request.

        - `Optional<Long> audioTokens`

          Number of audio tokens billed for this request.

        - `Optional<Long> textTokens`

          Number of text tokens billed for this request.

    - `class Duration:`

      Usage statistics for models billed by audio input duration.

      - `double seconds`

        Duration of the input audio in seconds.

      - `JsonValue; type "duration"constant`

        The type of the usage object. Always `duration` for this variant.

        - `DURATION("duration")`

#### Transcription Diarized Segment

- `class TranscriptionDiarizedSegment:`

  A segment of diarized transcript text with speaker metadata.

  - `String id`

    Unique identifier for the segment.

  - `double end`

    End timestamp of the segment in seconds.

  - `String speaker`

    Speaker label for this segment. When known speakers are provided, the label matches `known_speaker_names[]`. Otherwise speakers are labeled sequentially using capital letters (`A`, `B`, ...).

  - `double start`

    Start timestamp of the segment in seconds.

  - `String text`

    Transcript text for this segment.

  - `JsonValue; type "transcript.text.segment"constant`

    The type of the segment. Always `transcript.text.segment`.

    - `TRANSCRIPT_TEXT_SEGMENT("transcript.text.segment")`

#### Transcription Include

- `enum TranscriptionInclude:`

  - `LOGPROBS("logprobs")`

#### Transcription Segment

- `class TranscriptionSegment:`

  - `long id`

    Unique identifier of the segment.

  - `double avgLogprob`

    Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

  - `double compressionRatio`

    Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

  - `double end`

    End time of the segment in seconds.

  - `double noSpeechProb`

    Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

  - `long seek`

    Seek offset of the segment.

  - `double start`

    Start time of the segment in seconds.

  - `double temperature`

    Temperature parameter used for generating the segment.

  - `String text`

    Text content of the segment.

  - `List<long> tokens`

    Array of token IDs for the text content.

#### Transcription Stream Event

- `class TranscriptionStreamEvent: A class that can be one of several variants.union`

  Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

  - `class TranscriptionTextSegmentEvent:`

    Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

    - `String id`

      Unique identifier for the segment.

    - `double end`

      End timestamp of the segment in seconds.

    - `String speaker`

      Speaker label for this segment.

    - `double start`

      Start timestamp of the segment in seconds.

    - `String text`

      Transcript text for this segment.

    - `JsonValue; type "transcript.text.segment"constant`

      The type of the event. Always `transcript.text.segment`.

      - `TRANSCRIPT_TEXT_SEGMENT("transcript.text.segment")`

  - `class TranscriptionTextDeltaEvent:`

    Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

    - `String delta`

      The text delta that was additionally transcribed.

    - `JsonValue; type "transcript.text.delta"constant`

      The type of the event. Always `transcript.text.delta`.

      - `TRANSCRIPT_TEXT_DELTA("transcript.text.delta")`

    - `Optional<List<Logprob>> logprobs`

      The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

      - `Optional<String> token`

        The token that was used to generate the log probability.

      - `Optional<List<Long>> bytes`

        The bytes that were used to generate the log probability.

      - `Optional<Double> logprob`

        The log probability of the token.

    - `Optional<String> segmentId`

      Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

  - `class TranscriptionTextDoneEvent:`

    Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

    - `String text`

      The text that was transcribed.

    - `JsonValue; type "transcript.text.done"constant`

      The type of the event. Always `transcript.text.done`.

      - `TRANSCRIPT_TEXT_DONE("transcript.text.done")`

    - `Optional<List<Logprob>> logprobs`

      The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

      - `Optional<String> token`

        The token that was used to generate the log probability.

      - `Optional<List<Long>> bytes`

        The bytes that were used to generate the log probability.

      - `Optional<Double> logprob`

        The log probability of the token.

    - `Optional<Usage> usage`

      Usage statistics for models billed by token usage.

      - `long inputTokens`

        Number of input tokens billed for this request.

      - `long outputTokens`

        Number of output tokens generated.

      - `long totalTokens`

        Total number of tokens used (input + output).

      - `JsonValue; type "tokens"constant`

        The type of the usage object. Always `tokens` for this variant.

        - `TOKENS("tokens")`

      - `Optional<InputTokenDetails> inputTokenDetails`

        Details about the input tokens billed for this request.

        - `Optional<Long> audioTokens`

          Number of audio tokens billed for this request.

        - `Optional<Long> textTokens`

          Number of text tokens billed for this request.

#### Transcription Text Delta Event

- `class TranscriptionTextDeltaEvent:`

  Emitted when there is an additional text delta. This is also the first event emitted when the transcription starts. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

  - `String delta`

    The text delta that was additionally transcribed.

  - `JsonValue; type "transcript.text.delta"constant`

    The type of the event. Always `transcript.text.delta`.

    - `TRANSCRIPT_TEXT_DELTA("transcript.text.delta")`

  - `Optional<List<Logprob>> logprobs`

    The log probabilities of the delta. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

    - `Optional<String> token`

      The token that was used to generate the log probability.

    - `Optional<List<Long>> bytes`

      The bytes that were used to generate the log probability.

    - `Optional<Double> logprob`

      The log probability of the token.

  - `Optional<String> segmentId`

    Identifier of the diarized segment that this delta belongs to. Only present when using `gpt-4o-transcribe-diarize`.

#### Transcription Text Done Event

- `class TranscriptionTextDoneEvent:`

  Emitted when the transcription is complete. Contains the complete transcription text. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `Stream` parameter set to `true`.

  - `String text`

    The text that was transcribed.

  - `JsonValue; type "transcript.text.done"constant`

    The type of the event. Always `transcript.text.done`.

    - `TRANSCRIPT_TEXT_DONE("transcript.text.done")`

  - `Optional<List<Logprob>> logprobs`

    The log probabilities of the individual tokens in the transcription. Only included if you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with the `include[]` parameter set to `logprobs`.

    - `Optional<String> token`

      The token that was used to generate the log probability.

    - `Optional<List<Long>> bytes`

      The bytes that were used to generate the log probability.

    - `Optional<Double> logprob`

      The log probability of the token.

  - `Optional<Usage> usage`

    Usage statistics for models billed by token usage.

    - `long inputTokens`

      Number of input tokens billed for this request.

    - `long outputTokens`

      Number of output tokens generated.

    - `long totalTokens`

      Total number of tokens used (input + output).

    - `JsonValue; type "tokens"constant`

      The type of the usage object. Always `tokens` for this variant.

      - `TOKENS("tokens")`

    - `Optional<InputTokenDetails> inputTokenDetails`

      Details about the input tokens billed for this request.

      - `Optional<Long> audioTokens`

        Number of audio tokens billed for this request.

      - `Optional<Long> textTokens`

        Number of text tokens billed for this request.

#### Transcription Text Segment Event

- `class TranscriptionTextSegmentEvent:`

  Emitted when a diarized transcription returns a completed segment with speaker information. Only emitted when you [create a transcription](https://platform.openai.com/docs/api-reference/audio/create-transcription) with `stream` set to `true` and `response_format` set to `diarized_json`.

  - `String id`

    Unique identifier for the segment.

  - `double end`

    End timestamp of the segment in seconds.

  - `String speaker`

    Speaker label for this segment.

  - `double start`

    Start timestamp of the segment in seconds.

  - `String text`

    Transcript text for this segment.

  - `JsonValue; type "transcript.text.segment"constant`

    The type of the event. Always `transcript.text.segment`.

    - `TRANSCRIPT_TEXT_SEGMENT("transcript.text.segment")`

#### Transcription Verbose

- `class TranscriptionVerbose:`

  Represents a verbose json transcription response returned by model, based on the provided input.

  - `double duration`

    The duration of the input audio.

  - `String language`

    The language of the input audio.

  - `String text`

    The transcribed text.

  - `Optional<List<TranscriptionSegment>> segments`

    Segments of the transcribed text and their corresponding details.

    - `long id`

      Unique identifier of the segment.

    - `double avgLogprob`

      Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

    - `double compressionRatio`

      Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

    - `double end`

      End time of the segment in seconds.

    - `double noSpeechProb`

      Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

    - `long seek`

      Seek offset of the segment.

    - `double start`

      Start time of the segment in seconds.

    - `double temperature`

      Temperature parameter used for generating the segment.

    - `String text`

      Text content of the segment.

    - `List<long> tokens`

      Array of token IDs for the text content.

  - `Optional<Usage> usage`

    Usage statistics for models billed by audio input duration.

    - `double seconds`

      Duration of the input audio in seconds.

    - `JsonValue; type "duration"constant`

      The type of the usage object. Always `duration` for this variant.

      - `DURATION("duration")`

  - `Optional<List<TranscriptionWord>> words`

    Extracted words and their corresponding timestamps.

    - `double end`

      End time of the word in seconds.

    - `double start`

      Start time of the word in seconds.

    - `String word`

      The text content of the word.

#### Transcription Word

- `class TranscriptionWord:`

  - `double end`

    End time of the word in seconds.

  - `double start`

    Start time of the word in seconds.

  - `String word`

    The text content of the word.

## Translations

### Create

`TranslationCreateResponse audio().translations().create(TranslationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/audio/translations`

Translates audio into English.

#### Parameters

- `TranslationCreateParams params`

  - `String file`

    The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

  - `AudioModel model`

    ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

    - `WHISPER_1("whisper-1")`

    - `GPT_4O_TRANSCRIBE("gpt-4o-transcribe")`

    - `GPT_4O_MINI_TRANSCRIBE("gpt-4o-mini-transcribe")`

    - `GPT_4O_MINI_TRANSCRIBE_2025_12_15("gpt-4o-mini-transcribe-2025-12-15")`

    - `GPT_4O_TRANSCRIBE_DIARIZE("gpt-4o-transcribe-diarize")`

  - `Optional<String> prompt`

    An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

  - `Optional<ResponseFormat> responseFormat`

    The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

    - `JSON("json")`

    - `TEXT("text")`

    - `SRT("srt")`

    - `VERBOSE_JSON("verbose_json")`

    - `VTT("vtt")`

  - `Optional<Double> temperature`

    The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

#### Returns

- `class TranslationCreateResponse: A class that can be one of several variants.union`

  - `class Translation:`

    - `String text`

  - `class TranslationVerbose:`

    - `double duration`

      The duration of the input audio.

    - `String language`

      The language of the output translation (always `english`).

    - `String text`

      The translated text.

    - `Optional<List<TranscriptionSegment>> segments`

      Segments of the translated text and their corresponding details.

      - `long id`

        Unique identifier of the segment.

      - `double avgLogprob`

        Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

      - `double compressionRatio`

        Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

      - `double end`

        End time of the segment in seconds.

      - `double noSpeechProb`

        Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

      - `long seek`

        Seek offset of the segment.

      - `double start`

        Start time of the segment in seconds.

      - `double temperature`

        Temperature parameter used for generating the segment.

      - `String text`

        Text content of the segment.

      - `List<long> tokens`

        Array of token IDs for the text content.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.audio.AudioModel;
import com.openai.models.audio.translations.TranslationCreateParams;
import com.openai.models.audio.translations.TranslationCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TranslationCreateParams params = TranslationCreateParams.builder()
            .file(ByteArrayInputStream("some content".getBytes()))
            .model(AudioModel.WHISPER_1)
            .build();
        TranslationCreateResponse translation = client.audio().translations().create(params);
    }
}
```

#### Domain Types

#### Translation

- `class Translation:`

  - `String text`

#### Translation Verbose

- `class TranslationVerbose:`

  - `double duration`

    The duration of the input audio.

  - `String language`

    The language of the output translation (always `english`).

  - `String text`

    The translated text.

  - `Optional<List<TranscriptionSegment>> segments`

    Segments of the translated text and their corresponding details.

    - `long id`

      Unique identifier of the segment.

    - `double avgLogprob`

      Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.

    - `double compressionRatio`

      Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.

    - `double end`

      End time of the segment in seconds.

    - `double noSpeechProb`

      Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.

    - `long seek`

      Seek offset of the segment.

    - `double start`

      Start time of the segment in seconds.

    - `double temperature`

      Temperature parameter used for generating the segment.

    - `String text`

      Text content of the segment.

    - `List<long> tokens`

      Array of token IDs for the text content.

## Speech

### Create

`HttpResponse audio().speech().create(SpeechCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/audio/speech`

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

#### Parameters

- `SpeechCreateParams params`

  - `String input`

    The text to generate audio for. The maximum length is 4096 characters.

  - `SpeechModel model`

    One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

    - `TTS_1("tts-1")`

    - `TTS_1_HD("tts-1-hd")`

    - `GPT_4O_MINI_TTS("gpt-4o-mini-tts")`

    - `GPT_4O_MINI_TTS_2025_12_15("gpt-4o-mini-tts-2025-12-15")`

  - `Voice voice`

    The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

    - `String`

    - `enum UnionMember1:`

      - `ALLOY("alloy")`

      - `ASH("ash")`

      - `BALLAD("ballad")`

      - `CORAL("coral")`

      - `ECHO("echo")`

      - `SAGE("sage")`

      - `SHIMMER("shimmer")`

      - `VERSE("verse")`

      - `MARIN("marin")`

      - `CEDAR("cedar")`

    - `class Id:`

      Custom voice reference.

      - `String id`

        The custom voice ID, e.g. `voice_1234`.

  - `Optional<String> instructions`

    Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

  - `Optional<ResponseFormat> responseFormat`

    The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

    - `MP3("mp3")`

    - `OPUS("opus")`

    - `AAC("aac")`

    - `FLAC("flac")`

    - `WAV("wav")`

    - `PCM("pcm")`

  - `Optional<Double> speed`

    The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

  - `Optional<StreamFormat> streamFormat`

    The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

    - `SSE("sse")`

    - `AUDIO("audio")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.audio.speech.SpeechCreateParams;
import com.openai.models.audio.speech.SpeechModel;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SpeechCreateParams params = SpeechCreateParams.builder()
            .input("input")
            .model(SpeechModel.TTS_1)
            .voice("string")
            .build();
        HttpResponse speech = client.audio().speech().create(params);
    }
}
```

#### Domain Types

#### Speech Model

- `enum SpeechModel:`

  - `TTS_1("tts-1")`

  - `TTS_1_HD("tts-1-hd")`

  - `GPT_4O_MINI_TTS("gpt-4o-mini-tts")`

  - `GPT_4O_MINI_TTS_2025_12_15("gpt-4o-mini-tts-2025-12-15")`

## Voices

## Voice Consents
