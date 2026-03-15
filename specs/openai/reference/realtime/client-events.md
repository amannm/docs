# Client events

These are events that the OpenAI Realtime WebSocket server will accept from the client.

## session.update

Send this event to update the session’s configuration.
The client may send this event at any time to update any field
except for `voice` and `model`. `voice` can be updated only if there have been no other audio outputs yet.

When the server receives a `session.update`, it will respond
with a `session.updated` event showing the full, effective configuration.
Only the fields that are present in the `session.update` are updated. To clear a field like
`instructions`, pass an empty string. To clear a field like `tools`, pass an empty array.
To clear a field like `turn_detection`, pass `null`.

session: [RealtimeSessionCreateRequest](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_session_create_request%20%3E%20(schema)) { type, audio, include, 9 more }  or [RealtimeTranscriptionSessionCreateRequest](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_create_request%20%3E%20(schema)) { type, audio, include }

Update the Realtime session. Choose either a realtime
session or a transcription session.

Accepts one of the following:

RealtimeSessionCreateRequest = object { type, audio, include, 9 more }

Realtime session object configuration.

type: "realtime"

The type of session to create. Always `realtime` for the Realtime API.

audio: optional [RealtimeAudioConfig](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config%20%3E%20(schema)) { input, output }

Configuration for input and output audio.

input: optional [RealtimeAudioConfigInput](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_input%20%3E%20(schema)) { format, noise\_reduction, transcription, turn\_detection }

format: optional [RealtimeAudioFormats](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the input audio.

Accepts one of the following:

PCMAudioFormat = object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

PCMUAudioFormat = object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

PCMAAudioFormat = object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

noise\_reduction: optional object { type }

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

type: optional [NoiseReductionType](index.md#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

Accepts one of the following:

"near\_field"

"far\_field"

transcription: optional [AudioTranscription](index.md#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { language, model, prompt }

Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](https://developers.openai.com/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.

language: optional string

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

model: optional string or "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 2 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 2 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

Accepts one of the following:

"whisper-1"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe"

"gpt-4o-transcribe-diarize"

prompt: optional string

An optional text to guide the model's style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://developers.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example "expect words related to technology".

turn\_detection: optional [RealtimeAudioInputTurnDetection](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_input_turn_detection%20%3E%20(schema))

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with "uhhm", the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

Accepts one of the following:

ServerVad = object { type, create\_response, idle\_timeout\_ms, 4 more }

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

type: "server\_vad"

Type of turn detection, `server_vad` to turn on simple Server VAD.

create\_response: optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

idle\_timeout\_ms: optional number

Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response's audio has finished playing,
i.e. it's set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

minimum5000

maximum30000

interrupt\_response: optional boolean

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

prefix\_padding\_ms: optional number

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms: optional number

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold: optional number

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

SemanticVad = object { type, create\_response, eagerness, interrupt\_response }

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

type: "semantic\_vad"

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

create\_response: optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs.

eagerness: optional "low" or "medium" or "high" or "auto"

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

Accepts one of the following:

"low"

"medium"

"high"

"auto"

interrupt\_response: optional boolean

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

output: optional [RealtimeAudioConfigOutput](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_config_output%20%3E%20(schema)) { format, speed, voice }

format: optional [RealtimeAudioFormats](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

Accepts one of the following:

PCMAudioFormat = object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

PCMUAudioFormat = object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

PCMAAudioFormat = object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

speed: optional number

The speed of the model's spoken response as a multiple of the original speed.
1.0 is the default speed. 0.25 is the minimum speed. 1.5 is the maximum speed. This value can only be changed in between model turns, not while a response is in progress.

This parameter is a post-processing adjustment to the audio after it is generated, it's
also possible to prompt the model to speak faster or slower.

maximum1.5

minimum0.25

voice: optional string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`,
`marin`, and `cedar`. You may also provide a custom voice object with
an `id`, for example `{ "id": "voice_1234" }`. Voice cannot be changed
during the session once the model has responded with audio at least once.
We recommend `marin` and `cedar` for best quality.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "alloy" or "ash" or "ballad" or 7 more

Accepts one of the following:

"alloy"

"ash"

"ballad"

"coral"

"echo"

"sage"

"shimmer"

"verse"

"marin"

"cedar"

ID = object { id }

Custom voice reference.

id: string

The custom voice ID, e.g. `voice_1234`.

include: optional array of "item.input\_audio\_transcription.logprobs"

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

instructions: optional string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. "be extremely succinct", "act friendly", "here are examples of good responses") and on audio behavior (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.

Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

max\_output\_tokens: optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

Accepts one of the following:

UnionMember0 = number

UnionMember1 = "inf"

model: optional string or "gpt-realtime" or "gpt-realtime-1.5" or "gpt-realtime-2025-08-28" or 13 more

The Realtime model used for this session.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "gpt-realtime" or "gpt-realtime-1.5" or "gpt-realtime-2025-08-28" or 13 more

The Realtime model used for this session.

Accepts one of the following:

"gpt-realtime"

"gpt-realtime-1.5"

"gpt-realtime-2025-08-28"

"gpt-4o-realtime-preview"

"gpt-4o-realtime-preview-2024-10-01"

"gpt-4o-realtime-preview-2024-12-17"

"gpt-4o-realtime-preview-2025-06-03"

"gpt-4o-mini-realtime-preview"

"gpt-4o-mini-realtime-preview-2024-12-17"

"gpt-realtime-mini"

"gpt-realtime-mini-2025-10-06"

"gpt-realtime-mini-2025-12-15"

"gpt-audio-1.5"

"gpt-audio-mini"

"gpt-audio-mini-2025-10-06"

"gpt-audio-mini-2025-12-15"

output\_modalities: optional array of "text" or "audio"

The set of modalities the model can respond with. It defaults to `["audio"]`, indicating
that the model will respond with audio plus a transcript. `["text"]` can be used to make
the model respond with text only. It is not possible to request both `text` and `audio` at the same time.

Accepts one of the following:

"text"

"audio"

prompt: optional [ResponsePrompt](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema)) { id, variables, version }

Reference to a prompt template and its variables.
[Learn more](https://developers.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables: optional map[string or [ResponseInputText](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or [ResponseInputImage](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  or [ResponseInputFile](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, file\_data, file\_id, 2 more } ]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

Accepts one of the following:

UnionMember0 = string

ResponseInputText = object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage = object { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://developers.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

Accepts one of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string

The ID of the file to be sent to the model.

image\_url: optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

ResponseInputFile = object { type, file\_data, file\_id, 2 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

file\_data: optional string

The content of the file to be sent to the model.

file\_id: optional string

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

filename: optional string

The name of the file to be sent to the model.

version: optional string

Optional version of the prompt template.

tool\_choice: optional [RealtimeToolChoiceConfig](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_tool_choice_config%20%3E%20(schema))

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

Accepts one of the following:

ToolChoiceOptions = "none" or "auto" or "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

Accepts one of the following:

"none"

"auto"

"required"

ToolChoiceFunction = object { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

ToolChoiceMcp = object { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name: optional string

The name of the tool to call on the server.

tools: optional [RealtimeToolsConfig](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_tools_config%20%3E%20(schema)) { , McpTool }

Tools available to the model.

Accepts one of the following:

RealtimeFunctionTool = object { description, name, parameters, type }

description: optional string

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

name: optional string

The name of the function.

parameters: optional unknown

Parameters of the function in JSON Schema.

type: optional "function"

The type of the tool, i.e. `function`.

McpTool = object { server\_label, type, allowed\_tools, 7 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://developers.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools: optional array of string or object { read\_only, tool\_names }

List of allowed tool names or a filter object.

Accepts one of the following:

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter = object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

authorization: optional string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url` or `connector_id` must be provided. Learn more about service
connectors [here](https://developers.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

- Dropbox: `connector_dropbox`
- Gmail: `connector_gmail`
- Google Calendar: `connector_googlecalendar`
- Google Drive: `connector_googledrive`
- Microsoft Teams: `connector_microsoftteams`
- Outlook Calendar: `connector_outlookcalendar`
- Outlook Email: `connector_outlookemail`
- SharePoint: `connector_sharepoint`

Accepts one of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

Whether this MCP tool is deferred and discovered via tool search.

headers: optional map[string]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never"

Specify which of the MCP server's tools require approval.

Accepts one of the following:

McpToolApprovalFilter = object { always, never }

Specify which of the MCP server's tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

never: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

Accepts one of the following:

"always"

"never"

server\_description: optional string

Optional description of the MCP server, used to provide more context.

server\_url: optional string

The URL for the MCP server. One of `server_url` or `connector_id` must be
provided.

tracing: optional [RealtimeTracingConfig](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_tracing_config%20%3E%20(schema))

Realtime API can write session traces to the [Traces Dashboard](https://developers.openai.com/logs?api=traces). Set to null to disable tracing. Once
tracing is enabled for a session, the configuration cannot be modified.

`auto` will create a trace for the session with default values for the
workflow name, group id, and metadata.

Accepts one of the following:

Auto = "auto"

Enables tracing and sets default values for tracing configuration options. Always `auto`.

TracingConfiguration = object { group\_id, metadata, workflow\_name }

Granular configuration for tracing.

group\_id: optional string

The group id to attach to this trace to enable filtering and
grouping in the Traces Dashboard.

metadata: optional unknown

The arbitrary metadata to attach to this trace to enable
filtering in the Traces Dashboard.

workflow\_name: optional string

The name of the workflow to attach to this trace. This is used to
name the trace in the Traces Dashboard.

truncation: optional [RealtimeTruncation](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_truncation%20%3E%20(schema))

When the number of tokens in a conversation exceeds the model's input token limit, the conversation be truncated, meaning messages (starting from the oldest) will not be included in the model's context. A 32k context model with 4,096 max output tokens can only include 28,224 tokens in the context before truncation occurs.

Clients can configure truncation behavior to truncate with a lower max token limit, which is an effective way to control token usage and cost.

Truncation will reduce the number of cached tokens on the next turn (busting the cache), since messages are dropped from the beginning of the context. However, clients can also configure truncation to retain messages up to a fraction of the maximum context size, which will reduce the need for future truncations and thus improve the cache rate.

Truncation can be disabled entirely, which means the server will never truncate but would instead return an error if the conversation exceeds the model's input token limit.

Accepts one of the following:

UnionMember0 = "auto" or "disabled"

The truncation strategy to use for the session. `auto` is the default truncation strategy. `disabled` will disable truncation and emit errors when the conversation exceeds the input token limit.

Accepts one of the following:

"auto"

"disabled"

RetentionRatioTruncation = object { retention\_ratio, type, token\_limits }

Retain a fraction of the conversation tokens when the conversation exceeds the input token limit. This allows you to amortize truncations across multiple turns, which can help improve cached token usage.

retention\_ratio: number

Fraction of post-instruction conversation tokens to retain (`0.0` - `1.0`) when the conversation exceeds the input token limit. Setting this to `0.8` means that messages will be dropped until 80% of the maximum allowed tokens are used. This helps reduce the frequency of truncations and improve cache rates.

minimum0

maximum1

type: "retention\_ratio"

Use retention ratio truncation.

token\_limits: optional object { post\_instructions }

Optional custom token limits for this truncation strategy. If not provided, the model's default token limits will be used.

post\_instructions: optional number

Maximum tokens allowed in the conversation after instructions (which including tool definitions). For example, setting this to 5,000 would mean that truncation would occur when the conversation exceeds 5,000 tokens after instructions. This cannot be higher than the model's context window size minus the maximum output tokens.

minimum0

RealtimeTranscriptionSessionCreateRequest = object { type, audio, include }

Realtime transcription session object configuration.

type: "transcription"

The type of session to create. Always `transcription` for transcription sessions.

audio: optional [RealtimeTranscriptionSessionAudio](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio%20%3E%20(schema)) { input }

Configuration for input and output audio.

input: optional [RealtimeTranscriptionSessionAudioInput](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio_input%20%3E%20(schema)) { format, noise\_reduction, transcription, turn\_detection }

format: optional [RealtimeAudioFormats](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The PCM audio format. Only a 24kHz sample rate is supported.

Accepts one of the following:

PCMAudioFormat = object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

PCMUAudioFormat = object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

PCMAAudioFormat = object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

noise\_reduction: optional object { type }

Configuration for input audio noise reduction. This can be set to `null` to turn off.
Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.

type: optional [NoiseReductionType](index.md#(resource)%20realtime%20%3E%20(model)%20noise_reduction_type%20%3E%20(schema))

Type of noise reduction. `near_field` is for close-talking microphones such as headphones, `far_field` is for far-field microphones such as laptop or conference room microphones.

Accepts one of the following:

"near\_field"

"far\_field"

transcription: optional [AudioTranscription](index.md#(resource)%20realtime%20%3E%20(model)%20audio_transcription%20%3E%20(schema)) { language, model, prompt }

Configuration for input audio transcription, defaults to off and can be set to `null` to turn off once on. Input audio transcription is not native to the model, since the model consumes audio directly. Transcription runs asynchronously through [the /audio/transcriptions endpoint](https://developers.openai.com/docs/api-reference/audio/createTranscription) and should be treated as guidance of input audio content rather than precisely what the model heard. The client can optionally set the language and prompt for transcription, these offer additional guidance to the transcription service.

language: optional string

The language of the input audio. Supplying the input language in
[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en`) format
will improve accuracy and latency.

model: optional string or "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 2 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "whisper-1" or "gpt-4o-mini-transcribe" or "gpt-4o-mini-transcribe-2025-12-15" or 2 more

The model to use for transcription. Current options are `whisper-1`, `gpt-4o-mini-transcribe`, `gpt-4o-mini-transcribe-2025-12-15`, `gpt-4o-transcribe`, and `gpt-4o-transcribe-diarize`. Use `gpt-4o-transcribe-diarize` when you need diarization with speaker labels.

Accepts one of the following:

"whisper-1"

"gpt-4o-mini-transcribe"

"gpt-4o-mini-transcribe-2025-12-15"

"gpt-4o-transcribe"

"gpt-4o-transcribe-diarize"

prompt: optional string

An optional text to guide the model's style or continue a previous audio
segment.
For `whisper-1`, the [prompt is a list of keywords](https://developers.openai.com/docs/guides/speech-to-text#prompting).
For `gpt-4o-transcribe` models (excluding `gpt-4o-transcribe-diarize`), the prompt is a free text string, for example "expect words related to technology".

turn\_detection: optional [RealtimeTranscriptionSessionAudioInputTurnDetection](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_transcription_session_audio_input_turn_detection%20%3E%20(schema))

Configuration for turn detection, ether Server VAD or Semantic VAD. This can be set to `null` to turn off, in which case the client must manually trigger model response.

Server VAD means that the model will detect the start and end of speech based on audio volume and respond at the end of user speech.

Semantic VAD is more advanced and uses a turn detection model (in conjunction with VAD) to semantically estimate whether the user has finished speaking, then dynamically sets a timeout based on this probability. For example, if user audio trails off with "uhhm", the model will score a low probability of turn end and wait longer for the user to continue speaking. This can be useful for more natural conversations, but may have a higher latency.

Accepts one of the following:

ServerVad = object { type, create\_response, idle\_timeout\_ms, 4 more }

Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.

type: "server\_vad"

Type of turn detection, `server_vad` to turn on simple Server VAD.

create\_response: optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs. If `interrupt_response` is set to `false` this may fail to create a response if the model is already responding.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

idle\_timeout\_ms: optional number

Optional timeout after which a model response will be triggered automatically. This is
useful for situations in which a long pause from the user is unexpected, such as a phone
call. The model will effectively prompt the user to continue the conversation based
on the current context.

The timeout value will be applied after the last model response's audio has finished playing,
i.e. it's set to the `response.done` time plus audio playback duration.

An `input_audio_buffer.timeout_triggered` event (plus events
associated with the Response) will be emitted when the timeout is reached.
Idle timeout is currently only supported for `server_vad` mode.

minimum5000

maximum30000

interrupt\_response: optional boolean

Whether or not to automatically interrupt (cancel) any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs. If `true` then the response will be cancelled, otherwise it will continue until complete.

If both `create_response` and `interrupt_response` are set to `false`, the model will never respond automatically but VAD events will still be emitted.

prefix\_padding\_ms: optional number

Used only for `server_vad` mode. Amount of audio to include before the VAD detected speech (in
milliseconds). Defaults to 300ms.

silence\_duration\_ms: optional number

Used only for `server_vad` mode. Duration of silence to detect speech stop (in milliseconds). Defaults
to 500ms. With shorter values the model will respond more quickly,
but may jump in on short pauses from the user.

threshold: optional number

Used only for `server_vad` mode. Activation threshold for VAD (0.0 to 1.0), this defaults to 0.5. A
higher threshold will require louder audio to activate the model, and
thus might perform better in noisy environments.

SemanticVad = object { type, create\_response, eagerness, interrupt\_response }

Server-side semantic turn detection which uses a model to determine when the user has finished speaking.

type: "semantic\_vad"

Type of turn detection, `semantic_vad` to turn on Semantic VAD.

create\_response: optional boolean

Whether or not to automatically generate a response when a VAD stop event occurs.

eagerness: optional "low" or "medium" or "high" or "auto"

Used only for `semantic_vad` mode. The eagerness of the model to respond. `low` will wait longer for the user to continue speaking, `high` will respond more quickly. `auto` is the default and is equivalent to `medium`. `low`, `medium`, and `high` have max timeouts of 8s, 4s, and 2s respectively.

Accepts one of the following:

"low"

"medium"

"high"

"auto"

interrupt\_response: optional boolean

Whether or not to automatically interrupt any ongoing response with output to the default
conversation (i.e. `conversation` of `auto`) when a VAD start event occurs.

include: optional array of "item.input\_audio\_transcription.logprobs"

Additional fields to include in server outputs.

`item.input_audio_transcription.logprobs`: Include logprobs for input audio transcription.

type: "session.update"

The event type, must be `session.update`.

event\_id: optional string

Optional client-generated ID used to identify this event. This is an arbitrary string that a client may assign. It will be passed back if there is an error with the event, but the corresponding `session.updated` event will not include it.

maxLength512

OBJECT

### session.update

```
{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "instructions": "You are a creative assistant that helps with design tasks.",
    "tools": [
      {
        "type": "function",
        "name": "display_color_palette",
        "description": "Call this function when a user asks for a color palette.",
        "parameters": {
          "type": "object",
          "properties": {
            "theme": {
              "type": "string",
              "description": "Description of the theme for the color scheme."
            },
            "colors": {
              "type": "array",
              "description": "Array of five hex color codes based on the theme.",
              "items": {
                "type": "string",
                "description": "Hex color code"
              }
            }
          },
          "required": [
            "theme",
            "colors"
          ]
        }
      }
    ],
    "tool_choice": "auto"
  }
}
```

## input\_audio\_buffer.append

Send this event to append audio bytes to the input audio buffer. The audio
buffer is temporary storage you can write to and later commit. A "commit" will create a new
user message item in the conversation history from the buffer content and clear the buffer.
Input audio transcription (if enabled) will be generated when the buffer is committed.

If VAD is enabled the audio buffer is used to detect speech and the server will decide
when to commit. When Server VAD is disabled, you must commit the audio buffer
manually. Input audio noise reduction operates on writes to the audio buffer.

The client may choose how much audio to place in each event up to a maximum
of 15 MiB, for example streaming smaller chunks from the client may allow the
VAD to be more responsive. Unlike most other client events, the server will
not send a confirmation response to this event.

audio: string

Base64-encoded audio bytes. This must be in the format specified by the
`input_audio_format` field in the session configuration.

type: "input\_audio\_buffer.append"

The event type, must be `input_audio_buffer.append`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### input\_audio\_buffer.append

```
{
    "event_id": "event_456",
    "type": "input_audio_buffer.append",
    "audio": "Base64EncodedAudioData"
}
```

## input\_audio\_buffer.commit

Send this event to commit the user input audio buffer, which will create a new user message item in the conversation. This event will produce an error if the input audio buffer is empty. When in Server VAD mode, the client does not need to send this event, the server will commit the audio buffer automatically.

Committing the input audio buffer will trigger input audio transcription (if enabled in session configuration), but it will not create a response from the model. The server will respond with an `input_audio_buffer.committed` event.

type: "input\_audio\_buffer.commit"

The event type, must be `input_audio_buffer.commit`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### input\_audio\_buffer.commit

```
{
    "event_id": "event_789",
    "type": "input_audio_buffer.commit"
}
```

## input\_audio\_buffer.clear

Send this event to clear the audio bytes in the buffer. The server will
respond with an `input_audio_buffer.cleared` event.

type: "input\_audio\_buffer.clear"

The event type, must be `input_audio_buffer.clear`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### input\_audio\_buffer.clear

```
{
    "event_id": "event_012",
    "type": "input_audio_buffer.clear"
}
```

## conversation.item.create

Add a new Item to the Conversation's context, including messages, function
calls, and function call responses. This event can be used both to populate a
"history" of the conversation and to add new items mid-stream, but has the
current limitation that it cannot populate assistant audio messages.

If successful, the server will respond with a `conversation.item.created`
event, otherwise an `error` event will be sent.

item: [ConversationItem](index.md#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

A single item within a Realtime conversation.

Accepts one of the following:

RealtimeConversationItemSystemMessage = object { content, role, type, 3 more }

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.

content: array of object { text, type }

The content of the message.

text: optional string

The text content.

type: optional "input\_text"

The content type. Always `input_text` for system messages.

role: "system"

The role of the message sender. Always `system`.

type: "message"

The type of the item. Always `message`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemUserMessage = object { content, role, type, 3 more }

A user message item in a Realtime conversation.

content: array of object { audio, detail, image\_url, 3 more }

The content of the message.

audio: optional string

Base64-encoded audio bytes (for `input_audio`), these will be parsed as the format specified in the session input audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

detail: optional "auto" or "low" or "high"

The detail level of the image (for `input_image`). `auto` will default to `high`.

Accepts one of the following:

"auto"

"low"

"high"

image\_url: optional string

Base64-encoded image bytes (for `input_image`) as a data URI. For example `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...`. Supported formats are PNG and JPEG.

text: optional string

The text content (for `input_text`).

transcript: optional string

Transcript of the audio (for `input_audio`). This is not sent to the model, but will be attached to the message item for reference.

type: optional "input\_text" or "input\_audio" or "input\_image"

The content type (`input_text`, `input_audio`, or `input_image`).

Accepts one of the following:

"input\_text"

"input\_audio"

"input\_image"

role: "user"

The role of the message sender. Always `user`.

type: "message"

The type of the item. Always `message`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemAssistantMessage = object { content, role, type, 3 more }

An assistant message item in a Realtime conversation.

content: array of object { audio, text, transcript, type }

The content of the message.

audio: optional string

Base64-encoded audio bytes, these will be parsed as the format specified in the session output audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

text: optional string

The text content.

transcript: optional string

The transcript of the audio content, this will always be present if the output type is `audio`.

type: optional "output\_text" or "output\_audio"

The content type, `output_text` or `output_audio` depending on the session `output_modalities` configuration.

Accepts one of the following:

"output\_text"

"output\_audio"

role: "assistant"

The role of the message sender. Always `assistant`.

type: "message"

The type of the item. Always `message`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemFunctionCall = object { arguments, name, type, 4 more }

A function call item in a Realtime conversation.

arguments: string

The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{"arg1": "value1", "arg2": 42}`.

name: string

The name of the function being called.

type: "function\_call"

The type of the item. Always `function_call`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

call\_id: optional string

The ID of the function call.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemFunctionCallOutput = object { call\_id, output, type, 3 more }

A function call output item in a Realtime conversation.

call\_id: string

The ID of the function call this output is for.

output: string

The output of the function call, this is free text and can contain any information or simply be empty.

type: "function\_call\_output"

The type of the item. Always `function_call_output`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeMcpApprovalResponse = object { id, approval\_request\_id, approve, 2 more }

A Realtime item responding to an MCP approval request.

id: string

The unique ID of the approval response.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

reason: optional string

Optional reason for the decision.

RealtimeMcpListTools = object { server\_label, tools, type, id }

A Realtime item listing tools available on an MCP server.

server\_label: string

The label of the MCP server.

tools: array of object { input\_schema, name, annotations, description }

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool's input.

name: string

The name of the tool.

annotations: optional unknown

Additional annotations about the tool.

description: optional string

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

id: optional string

The unique ID of the list.

RealtimeMcpToolCall = object { id, arguments, name, 5 more }

A Realtime item representing an invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

approval\_request\_id: optional string

The ID of an associated approval request, if any.

error: optional [RealtimeMcpProtocolError](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)) { code, message, type }  or [RealtimeMcpToolExecutionError](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)) { message, type }  or [RealtimeMcphttpError](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)) { code, message, type }

The error from the tool call, if any.

Accepts one of the following:

RealtimeMcpProtocolError = object { code, message, type }

code: number

message: string

type: "protocol\_error"

RealtimeMcpToolExecutionError = object { message, type }

message: string

type: "tool\_execution\_error"

RealtimeMcphttpError = object { code, message, type }

code: number

message: string

type: "http\_error"

output: optional string

The output from the tool call.

RealtimeMcpApprovalRequest = object { id, arguments, name, 2 more }

A Realtime item requesting human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

type: "conversation.item.create"

The event type, must be `conversation.item.create`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

previous\_item\_id: optional string

The ID of the preceding item after which the new item will be inserted. If not set, the new item will be appended to the end of the conversation.

If set to `root`, the new item will be added to the beginning of the conversation.

If set to an existing ID, it allows an item to be inserted mid-conversation. If the ID cannot be found, an error will be returned and the item will not be added.

OBJECT

### conversation.item.create

```
{
  "type": "conversation.item.create",
  "item": {
    "type": "message",
    "role": "user",
    "content": [
      {
        "type": "input_text",
        "text": "hi"
      }
    ]
  }
}
```

## conversation.item.retrieve

Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.
The server will respond with a `conversation.item.retrieved` event,
unless the item does not exist in the conversation history, in which case the
server will respond with an error.

item\_id: string

The ID of the item to retrieve.

type: "conversation.item.retrieve"

The event type, must be `conversation.item.retrieve`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### conversation.item.retrieve

```
{
    "event_id": "event_901",
    "type": "conversation.item.retrieve",
    "item_id": "item_003"
}
```

## conversation.item.truncate

Send this event to truncate a previous assistant message’s audio. The server
will produce audio faster than realtime, so this event is useful when the user
interrupts to truncate audio that has already been sent to the client but not
yet played. This will synchronize the server's understanding of the audio with
the client's playback.

Truncating audio will delete the server-side text transcript to ensure there
is not text in the context that hasn't been heard by the user.

If successful, the server will respond with a `conversation.item.truncated`
event.

audio\_end\_ms: number

Inclusive duration up to which audio is truncated, in milliseconds. If
the audio\_end\_ms is greater than the actual audio duration, the server
will respond with an error.

content\_index: number

The index of the content part to truncate. Set this to `0`.

item\_id: string

The ID of the assistant message item to truncate. Only assistant message
items can be truncated.

type: "conversation.item.truncate"

The event type, must be `conversation.item.truncate`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### conversation.item.truncate

```
{
    "event_id": "event_678",
    "type": "conversation.item.truncate",
    "item_id": "item_002",
    "content_index": 0,
    "audio_end_ms": 1500
}
```

## conversation.item.delete

Send this event when you want to remove any item from the conversation
history. The server will respond with a `conversation.item.deleted` event,
unless the item does not exist in the conversation history, in which case the
server will respond with an error.

item\_id: string

The ID of the item to delete.

type: "conversation.item.delete"

The event type, must be `conversation.item.delete`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

OBJECT

### conversation.item.delete

```
{
    "event_id": "event_901",
    "type": "conversation.item.delete",
    "item_id": "item_003"
}
```

## response.create

This event instructs the server to create a Response, which means triggering
model inference. When in Server VAD mode, the server will create Responses
automatically.

A Response will include at least one Item, and may have two, in which case
the second will be a function call. These Items will be appended to the
conversation history by default.

The server will respond with a `response.created` event, events for Items
and content created, and finally a `response.done` event to indicate the
Response is complete.

The `response.create` event includes inference configuration like
`instructions` and `tools`. If these are set, they will override the Session's
configuration for this Response only.

Responses can be created out-of-band of the default Conversation, meaning that they can
have arbitrary input, and it's possible to disable writing the output to the Conversation.
Only one Response can write to the default Conversation at a time, but otherwise multiple
Responses can be created in parallel. The `metadata` field is a good way to disambiguate
multiple simultaneous Responses.

Clients can set `conversation` to `none` to create a Response that does not write to the default
Conversation. Arbitrary input can be provided with the `input` field, which is an array accepting
raw Items and references to existing Items.

type: "response.create"

The event type, must be `response.create`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

response: optional [RealtimeResponseCreateParams](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_params%20%3E%20(schema)) { audio, conversation, input, 7 more }

Create a new Realtime response with these parameters

audio: optional [RealtimeResponseCreateAudioOutput](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_response_create_audio_output%20%3E%20(schema)) { output }

Configuration for audio input and output.

output: optional object { format, voice }

format: optional [RealtimeAudioFormats](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_audio_formats%20%3E%20(schema))

The format of the output audio.

Accepts one of the following:

PCMAudioFormat = object { rate, type }

The PCM audio format. Only a 24kHz sample rate is supported.

rate: optional 24000

The sample rate of the audio. Always `24000`.

type: optional "audio/pcm"

The audio format. Always `audio/pcm`.

PCMUAudioFormat = object { type }

The G.711 μ-law format.

type: optional "audio/pcmu"

The audio format. Always `audio/pcmu`.

PCMAAudioFormat = object { type }

The G.711 A-law format.

type: optional "audio/pcma"

The audio format. Always `audio/pcma`.

voice: optional string or "alloy" or "ash" or "ballad" or 7 more or object { id }

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`,
`marin`, and `cedar`. You may also provide a custom voice object with
an `id`, for example `{ "id": "voice_1234" }`. Voice cannot be changed
during the session once the model has responded with audio at least once.
We recommend `marin` and `cedar` for best quality.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "alloy" or "ash" or "ballad" or 7 more

Accepts one of the following:

"alloy"

"ash"

"ballad"

"coral"

"echo"

"sage"

"shimmer"

"verse"

"marin"

"cedar"

ID = object { id }

Custom voice reference.

id: string

The custom voice ID, e.g. `voice_1234`.

conversation: optional string or "auto" or "none"

Controls which conversation the response is added to. Currently supports
`auto` and `none`, with `auto` as the default value. The `auto` value
means that the contents of the response will be added to the default
conversation. Set this to `none` to create an out-of-band response which
will not add items to default conversation.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "auto" or "none"

Controls which conversation the response is added to. Currently supports
`auto` and `none`, with `auto` as the default value. The `auto` value
means that the contents of the response will be added to the default
conversation. Set this to `none` to create an out-of-band response which
will not add items to default conversation.

Accepts one of the following:

"auto"

"none"

input: optional array of [ConversationItem](index.md#(resource)%20realtime%20%3E%20(model)%20conversation_item%20%3E%20(schema))

Input items to include in the prompt for the model. Using this field
creates a new context for this Response instead of using the default
conversation. An empty array `[]` will clear the context for this Response.
Note that this can include references to items that previously appeared in the session
using their id.

Accepts one of the following:

RealtimeConversationItemSystemMessage = object { content, role, type, 3 more }

A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation's behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.

content: array of object { text, type }

The content of the message.

text: optional string

The text content.

type: optional "input\_text"

The content type. Always `input_text` for system messages.

role: "system"

The role of the message sender. Always `system`.

type: "message"

The type of the item. Always `message`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemUserMessage = object { content, role, type, 3 more }

A user message item in a Realtime conversation.

content: array of object { audio, detail, image\_url, 3 more }

The content of the message.

audio: optional string

Base64-encoded audio bytes (for `input_audio`), these will be parsed as the format specified in the session input audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

detail: optional "auto" or "low" or "high"

The detail level of the image (for `input_image`). `auto` will default to `high`.

Accepts one of the following:

"auto"

"low"

"high"

image\_url: optional string

Base64-encoded image bytes (for `input_image`) as a data URI. For example `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...`. Supported formats are PNG and JPEG.

text: optional string

The text content (for `input_text`).

transcript: optional string

Transcript of the audio (for `input_audio`). This is not sent to the model, but will be attached to the message item for reference.

type: optional "input\_text" or "input\_audio" or "input\_image"

The content type (`input_text`, `input_audio`, or `input_image`).

Accepts one of the following:

"input\_text"

"input\_audio"

"input\_image"

role: "user"

The role of the message sender. Always `user`.

type: "message"

The type of the item. Always `message`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemAssistantMessage = object { content, role, type, 3 more }

An assistant message item in a Realtime conversation.

content: array of object { audio, text, transcript, type }

The content of the message.

audio: optional string

Base64-encoded audio bytes, these will be parsed as the format specified in the session output audio type configuration. This defaults to PCM 16-bit 24kHz mono if not specified.

text: optional string

The text content.

transcript: optional string

The transcript of the audio content, this will always be present if the output type is `audio`.

type: optional "output\_text" or "output\_audio"

The content type, `output_text` or `output_audio` depending on the session `output_modalities` configuration.

Accepts one of the following:

"output\_text"

"output\_audio"

role: "assistant"

The role of the message sender. Always `assistant`.

type: "message"

The type of the item. Always `message`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemFunctionCall = object { arguments, name, type, 4 more }

A function call item in a Realtime conversation.

arguments: string

The arguments of the function call. This is a JSON-encoded string representing the arguments passed to the function, for example `{"arg1": "value1", "arg2": 42}`.

name: string

The name of the function being called.

type: "function\_call"

The type of the item. Always `function_call`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

call\_id: optional string

The ID of the function call.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeConversationItemFunctionCallOutput = object { call\_id, output, type, 3 more }

A function call output item in a Realtime conversation.

call\_id: string

The ID of the function call this output is for.

output: string

The output of the function call, this is free text and can contain any information or simply be empty.

type: "function\_call\_output"

The type of the item. Always `function_call_output`.

id: optional string

The unique ID of the item. This may be provided by the client or generated by the server.

object: optional "realtime.item"

Identifier for the API object being returned - always `realtime.item`. Optional when creating a new item.

status: optional "completed" or "incomplete" or "in\_progress"

The status of the item. Has no effect on the conversation.

Accepts one of the following:

"completed"

"incomplete"

"in\_progress"

RealtimeMcpApprovalResponse = object { id, approval\_request\_id, approve, 2 more }

A Realtime item responding to an MCP approval request.

id: string

The unique ID of the approval response.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

reason: optional string

Optional reason for the decision.

RealtimeMcpListTools = object { server\_label, tools, type, id }

A Realtime item listing tools available on an MCP server.

server\_label: string

The label of the MCP server.

tools: array of object { input\_schema, name, annotations, description }

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool's input.

name: string

The name of the tool.

annotations: optional unknown

Additional annotations about the tool.

description: optional string

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

id: optional string

The unique ID of the list.

RealtimeMcpToolCall = object { id, arguments, name, 5 more }

A Realtime item representing an invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

approval\_request\_id: optional string

The ID of an associated approval request, if any.

error: optional [RealtimeMcpProtocolError](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_protocol_error%20%3E%20(schema)) { code, message, type }  or [RealtimeMcpToolExecutionError](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_mcp_tool_execution_error%20%3E%20(schema)) { message, type }  or [RealtimeMcphttpError](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_mcphttp_error%20%3E%20(schema)) { code, message, type }

The error from the tool call, if any.

Accepts one of the following:

RealtimeMcpProtocolError = object { code, message, type }

code: number

message: string

type: "protocol\_error"

RealtimeMcpToolExecutionError = object { message, type }

message: string

type: "tool\_execution\_error"

RealtimeMcphttpError = object { code, message, type }

code: number

message: string

type: "http\_error"

output: optional string

The output from the tool call.

RealtimeMcpApprovalRequest = object { id, arguments, name, 2 more }

A Realtime item requesting human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

instructions: optional string

The default system instructions (i.e. system message) prepended to model calls. This field allows the client to guide the model on desired responses. The model can be instructed on response content and format, (e.g. "be extremely succinct", "act friendly", "here are examples of good responses") and on audio behavior (e.g. "talk quickly", "inject emotion into your voice", "laugh frequently"). The instructions are not guaranteed to be followed by the model, but they provide guidance to the model on the desired behavior.
Note that the server sets default instructions which will be used if this field is not set and are visible in the `session.created` event at the start of the session.

max\_output\_tokens: optional number or "inf"

Maximum number of output tokens for a single assistant response,
inclusive of tool calls. Provide an integer between 1 and 4096 to
limit output tokens, or `inf` for the maximum available tokens for a
given model. Defaults to `inf`.

Accepts one of the following:

UnionMember0 = number

UnionMember1 = "inf"

metadata: optional [Metadata](../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

output\_modalities: optional array of "text" or "audio"

The set of modalities the model used to respond, currently the only possible values are
`[\"audio\"]`, `[\"text\"]`. Audio output always include a text transcript. Setting the
output to mode `text` will disable audio output from the model.

Accepts one of the following:

"text"

"audio"

prompt: optional [ResponsePrompt](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema)) { id, variables, version }

Reference to a prompt template and its variables.
[Learn more](https://developers.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables: optional map[string or [ResponseInputText](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  or [ResponseInputImage](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, image\_url }  or [ResponseInputFile](../responses/index.md#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, file\_data, file\_id, 2 more } ]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

Accepts one of the following:

UnionMember0 = string

ResponseInputText = object { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage = object { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://developers.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

Accepts one of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string

The ID of the file to be sent to the model.

image\_url: optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

ResponseInputFile = object { type, file\_data, file\_id, 2 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

file\_data: optional string

The content of the file to be sent to the model.

file\_id: optional string

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

filename: optional string

The name of the file to be sent to the model.

version: optional string

Optional version of the prompt template.

tool\_choice: optional [ToolChoiceOptions](../responses/index.md#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) or [ToolChoiceFunction](../responses/index.md#(resource)%20responses%20%3E%20(model)%20tool_choice_function%20%3E%20(schema)) { name, type }  or [ToolChoiceMcp](../responses/index.md#(resource)%20responses%20%3E%20(model)%20tool_choice_mcp%20%3E%20(schema)) { server\_label, type, name }

How the model chooses tools. Provide one of the string modes or force a specific
function/MCP tool.

Accepts one of the following:

ToolChoiceOptions = "none" or "auto" or "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

Accepts one of the following:

"none"

"auto"

"required"

ToolChoiceFunction = object { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

ToolChoiceMcp = object { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name: optional string

The name of the tool to call on the server.

tools: optional array of [RealtimeFunctionTool](index.md#(resource)%20realtime%20%3E%20(model)%20realtime_function_tool%20%3E%20(schema)) { description, name, parameters, type }  or object { server\_label, type, allowed\_tools, 7 more }

Tools available to the model.

Accepts one of the following:

RealtimeFunctionTool = object { description, name, parameters, type }

description: optional string

The description of the function, including guidance on when and how
to call it, and guidance about what to tell the user when calling
(if anything).

name: optional string

The name of the function.

parameters: optional unknown

Parameters of the function in JSON Schema.

type: optional "function"

The type of the tool, i.e. `function`.

McpTool = object { server\_label, type, allowed\_tools, 7 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://developers.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools: optional array of string or object { read\_only, tool\_names }

List of allowed tool names or a filter object.

Accepts one of the following:

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter = object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

authorization: optional string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url` or `connector_id` must be provided. Learn more about service
connectors [here](https://developers.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

- Dropbox: `connector_dropbox`
- Gmail: `connector_gmail`
- Google Calendar: `connector_googlecalendar`
- Google Drive: `connector_googledrive`
- Microsoft Teams: `connector_microsoftteams`
- Outlook Calendar: `connector_outlookcalendar`
- Outlook Email: `connector_outlookemail`
- SharePoint: `connector_sharepoint`

Accepts one of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

Whether this MCP tool is deferred and discovered via tool search.

headers: optional map[string]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never"

Specify which of the MCP server's tools require approval.

Accepts one of the following:

McpToolApprovalFilter = object { always, never }

Specify which of the MCP server's tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

never: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

Accepts one of the following:

"always"

"never"

server\_description: optional string

Optional description of the MCP server, used to provide more context.

server\_url: optional string

The URL for the MCP server. One of `server_url` or `connector_id` must be
provided.

OBJECT

### response.create

```
// Trigger a response with the default Conversation and no special parameters
{
  "type": "response.create",
}

// Trigger an out-of-band response that does not write to the default Conversation
{
  "type": "response.create",
  "response": {
    "instructions": "Provide a concise answer.",
    "tools": [], // clear any session tools
    "conversation": "none",
    "output_modalities": ["text"],
    "metadata": {
      "response_purpose": "summarization"
    },
    "input": [
      {
        "type": "item_reference",
        "id": "item_12345"
      },
      {
        "type": "message",
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Summarize the above message in one sentence."
          }
        ]
      }
    ]
  }
}
```

## response.cancel

Send this event to cancel an in-progress response. The server will respond
with a `response.done` event with a status of `response.status=cancelled`. If
there is no response to cancel, the server will respond with an error. It's safe
to call `response.cancel` even if no response is in progress, an error will be
returned the session will remain unaffected.

type: "response.cancel"

The event type, must be `response.cancel`.

event\_id: optional string

Optional client-generated ID used to identify this event.

maxLength512

response\_id: optional string

A specific response ID to cancel - if not provided, will cancel an
in-progress response in the default conversation.

OBJECT

### response.cancel

```
{
    "type": "response.cancel",
    "response_id": "resp_12345"
}
```

## output\_audio\_buffer.clear

**WebRTC/SIP Only:** Emit to cut off the current audio response. This will trigger the server to
stop generating audio and emit a `output_audio_buffer.cleared` event. This
event should be preceded by a `response.cancel` client event to stop the
generation of the current response.
[Learn more](https://developers.openai.com/docs/guides/realtime-conversations#client-and-server-events-for-audio-in-webrtc).

type: "output\_audio\_buffer.clear"

The event type, must be `output_audio_buffer.clear`.

event\_id: optional string

The unique ID of the client event used for error handling.

OBJECT

### output\_audio\_buffer.clear

```
{
    "event_id": "optional_client_event_id",
    "type": "output_audio_buffer.clear"
}
```