# Streaming

Stream the result of executing a Run or resuming a Run after submitting tool outputs.
You can stream events from the [Create Thread and Run](https://developers.openai.com/docs/api-reference/runs/createThreadAndRun),
[Create Run](https://developers.openai.com/docs/api-reference/runs/createRun), and [Submit Tool Outputs](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs)
endpoints by passing `"stream": true`. The response will be a [Server-Sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) stream.
Our Node and Python SDKs provide helpful utilities to make streaming easy. Reference the
[Assistants API quickstart](https://developers.openai.com/docs/assistants/overview) to learn more.

Streaming events

## event

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

```
event: thread.created
data: {"id": "thread_123", "object": "thread", ...}
```

We emit events whenever a new object is created, transitions to a new state, or is being
streamed in parts (deltas). For example, we emit `thread.run.created` when a new run
is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses
to create a message during a run, we emit a `thread.message.created event`, a
`thread.message.in_progress` event, many `thread.message.delta` events, and finally a
`thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully
in your code. See the [Assistants API quickstart](https://developers.openai.com/docs/assistants/overview) to learn how to
integrate the Assistants API with streaming.

UnionMember0 = object { data, event, enabled }

Occurs when a new [thread](https://developers.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](../index.md#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](https://developers.openai.com/docs/api-reference/messages).

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the thread was created.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread"

The object type, which is always `thread`.

tool\_resources: object { code\_interpreter, file\_search }

A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: optional object { file\_ids }

file\_ids: optional array of string

A list of [file](https://developers.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: optional object { vector\_store\_ids }

vector\_store\_ids: optional array of string

The [vector store](https://developers.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

event: "thread.created"

enabled: optional boolean

Whether to enable input audio transcription.

UnionMember1 = object { data, event }

Occurs when a new [run](https://developers.openai.com/docs/api-reference/runs/object) is created.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.created"

UnionMember2 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.queued"

UnionMember3 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.in\_progress"

UnionMember4 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.requires\_action"

UnionMember5 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.completed"

UnionMember6 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.incomplete"

UnionMember7 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) fails.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.failed"

UnionMember8 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.cancelling"

UnionMember9 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.cancelled"

UnionMember10 = object { data, event }

Occurs when a [run](https://developers.openai.com/docs/api-reference/runs/object) expires.

data: [Run](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

Accepts one of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://developers.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](../index.md#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://developers.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://developers.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://developers.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Accepts one of the following:

UnionMember0 = "auto"

`auto` is the default value

ResponseFormatText = object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject = object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema = object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://developers.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

status: "queued" or "in\_progress" or "requires\_action" or 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

Accepts one of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Accepts one of the following:

UnionMember0 = "none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

Accepts one of the following:

"none"

"auto"

"required"

AssistantToolChoice = object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

Accepts one of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](../index.md#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](https://developers.openai.com/docs/api-reference/assistants) used for this run.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://developers.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool = object { function, type }

function: [FunctionDefinition](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

Accepts one of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

event: "thread.run.expired"

UnionMember11 = object { data, event }

Occurs when a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

Accepts one of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

Accepts one of the following:

MessageCreationStepDetails = object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails = object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [CodeInterpreterToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCall = object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogOutput = object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

CodeInterpreterImageOutput = object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall = object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall = object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

Accepts one of the following:

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

event: "thread.run.step.created"

UnionMember12 = object { data, event }

Occurs when a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

Accepts one of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

Accepts one of the following:

MessageCreationStepDetails = object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails = object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [CodeInterpreterToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCall = object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogOutput = object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

CodeInterpreterImageOutput = object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall = object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall = object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

Accepts one of the following:

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

event: "thread.run.step.in\_progress"

UnionMember13 = object { data, event }

Occurs when parts of a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: string

The identifier of the run step, which can be referenced in API endpoints.

delta: object { step\_details }

The delta containing the fields that have changed on the run step.

step\_details: optional [RunStepDeltaMessageDelta](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type, message\_creation }  or [ToolCallDeltaObject](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type, tool\_calls }

The details of the run step.

Accepts one of the following:

RunStepDeltaMessageDelta = object { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation: optional object { message\_id }

message\_id: optional string

The ID of the message that was created by this run step.

ToolCallDeltaObject = object { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls: optional array of [CodeInterpreterToolCallDelta](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index, type, id, code\_interpreter }  or [FileSearchToolCallDelta](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file\_search, index, type, id }  or [FunctionToolCallDelta](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index, type, id, function }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCallDelta = object { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: optional string

The ID of the tool call.

code\_interpreter: optional object { input, outputs }

The Code Interpreter tool call definition.

input: optional string

The input to the Code Interpreter tool call.

outputs: optional array of [CodeInterpreterLogs](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  or [CodeInterpreterOutputImage](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogs = object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage = object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta = object { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: optional string

The ID of the tool call object.

FunctionToolCallDelta = object { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id: optional string

The ID of the tool call object.

function: optional object { arguments, name, output }

The definition of the function that was called.

arguments: optional string

The arguments passed to the function.

name: optional string

The name of the function.

output: optional string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

object: "thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

event: "thread.run.step.delta"

UnionMember14 = object { data, event }

Occurs when a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

Accepts one of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

Accepts one of the following:

MessageCreationStepDetails = object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails = object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [CodeInterpreterToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCall = object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogOutput = object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

CodeInterpreterImageOutput = object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall = object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall = object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

Accepts one of the following:

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

event: "thread.run.step.completed"

UnionMember15 = object { data, event }

Occurs when a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

Accepts one of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

Accepts one of the following:

MessageCreationStepDetails = object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails = object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [CodeInterpreterToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCall = object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogOutput = object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

CodeInterpreterImageOutput = object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall = object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall = object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

Accepts one of the following:

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

event: "thread.run.step.failed"

UnionMember16 = object { data, event }

Occurs when a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

Accepts one of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

Accepts one of the following:

MessageCreationStepDetails = object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails = object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [CodeInterpreterToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCall = object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogOutput = object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

CodeInterpreterImageOutput = object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall = object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall = object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

Accepts one of the following:

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

event: "thread.run.step.cancelled"

UnionMember17 = object { data, event }

Occurs when a [run step](https://developers.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

Accepts one of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

Accepts one of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

Accepts one of the following:

MessageCreationStepDetails = object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails = object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [CodeInterpreterToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](../index.md#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

Accepts one of the following:

CodeInterpreterToolCall = object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

Accepts one of the following:

CodeInterpreterLogOutput = object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

CodeInterpreterImageOutput = object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://developers.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall = object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

Accepts one of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall = object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://developers.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://developers.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

Accepts one of the following:

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

event: "thread.run.step.expired"

UnionMember18 = object { data, event }

Occurs when a [message](https://developers.openai.com/docs/api-reference/messages/object) is created.

data: [Message](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

If applicable, the ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) that authored this message.

attachments: array of object { file\_id, tools }

A list of files attached to the message, and the tools they were added to.

file\_id: optional string

The ID of the file to attach to the message.

tools: optional array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or object { type }

The tools to add this file to.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type }

type: "file\_search"

The type of tool being defined: `file_search`

completed\_at: number

The Unix timestamp (in seconds) for when the message was completed.

content: array of [ImageFileContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  or [RefusalContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

The content of the message in array of text and/or images.

Accepts one of the following:

ImageFileContentBlock = object { image\_file, type }

References an image [File](https://developers.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

file\_id: string

The [File](https://developers.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

ImageURLContentBlock = object { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

TextContentBlock = object { text, type }

The text content that is part of a message.

text: [Text](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

annotations: array of [FileCitationAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  or [FilePathAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

Accepts one of the following:

FileCitationAnnotation = object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file\_search" tool to search files.

end\_index: number

minimum0

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation = object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

RefusalContentBlock = object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

incomplete\_at: number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

incomplete\_details: object { reason }

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" or "max\_tokens" or "run\_cancelled" or 2 more

The reason the message is incomplete.

Accepts one of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

Accepts one of the following:

"user"

"assistant"

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

Accepts one of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](https://developers.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: "thread.message.created"

UnionMember19 = object { data, event }

Occurs when a [message](https://developers.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

If applicable, the ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) that authored this message.

attachments: array of object { file\_id, tools }

A list of files attached to the message, and the tools they were added to.

file\_id: optional string

The ID of the file to attach to the message.

tools: optional array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or object { type }

The tools to add this file to.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type }

type: "file\_search"

The type of tool being defined: `file_search`

completed\_at: number

The Unix timestamp (in seconds) for when the message was completed.

content: array of [ImageFileContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  or [RefusalContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

The content of the message in array of text and/or images.

Accepts one of the following:

ImageFileContentBlock = object { image\_file, type }

References an image [File](https://developers.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

file\_id: string

The [File](https://developers.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

ImageURLContentBlock = object { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

TextContentBlock = object { text, type }

The text content that is part of a message.

text: [Text](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

annotations: array of [FileCitationAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  or [FilePathAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

Accepts one of the following:

FileCitationAnnotation = object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file\_search" tool to search files.

end\_index: number

minimum0

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation = object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

RefusalContentBlock = object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

incomplete\_at: number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

incomplete\_details: object { reason }

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" or "max\_tokens" or "run\_cancelled" or 2 more

The reason the message is incomplete.

Accepts one of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

Accepts one of the following:

"user"

"assistant"

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

Accepts one of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](https://developers.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: "thread.message.in\_progress"

UnionMember20 = object { data, event }

Occurs when parts of a [Message](https://developers.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

id: string

The identifier of the message, which can be referenced in API endpoints.

delta: [MessageDelta](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema)) { content, role }

The delta containing the fields that have changed on the Message.

content: optional array of [ImageFileDeltaBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta_block%20%3E%20(schema)) { index, type, image\_file }  or [TextDeltaBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta_block%20%3E%20(schema)) { index, type, text }  or [RefusalDeltaBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_delta_block%20%3E%20(schema)) { index, type, refusal }  or [ImageURLDeltaBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta_block%20%3E%20(schema)) { index, type, image\_url }

The content of the message in array of text and/or images.

Accepts one of the following:

ImageFileDeltaBlock = object { index, type, image\_file }

References an image [File](https://developers.openai.com/docs/api-reference/files) in the content of a message.

index: number

The index of the content part in the message.

type: "image\_file"

Always `image_file`.

image\_file: optional [ImageFileDelta](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_delta%20%3E%20(schema)) { detail, file\_id }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

Accepts one of the following:

"auto"

"low"

"high"

file\_id: optional string

The [File](https://developers.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

TextDeltaBlock = object { index, type, text }

The text content that is part of a message.

index: number

The index of the content part in the message.

type: "text"

Always `text`.

text: optional [TextDelta](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text_delta%20%3E%20(schema)) { annotations, value }

annotations: optional array of [FileCitationDeltaAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }  or [FilePathDeltaAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_delta_annotation%20%3E%20(schema)) { index, type, end\_index, 3 more }

Accepts one of the following:

FileCitationDeltaAnnotation = object { index, type, end\_index, 3 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file\_search" tool to search files.

index: number

The index of the annotation in the text content part.

type: "file\_citation"

Always `file_citation`.

end\_index: optional number

minimum0

file\_citation: optional object { file\_id, quote }

file\_id: optional string

The ID of the specific File the citation is from.

quote: optional string

The specific quote in the file.

start\_index: optional number

minimum0

text: optional string

The text in the message content that needs to be replaced.

FilePathDeltaAnnotation = object { index, type, end\_index, 3 more }

A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

index: number

The index of the annotation in the text content part.

type: "file\_path"

Always `file_path`.

end\_index: optional number

minimum0

file\_path: optional object { file\_id }

file\_id: optional string

The ID of the file that was generated.

start\_index: optional number

minimum0

text: optional string

The text in the message content that needs to be replaced.

value: optional string

The data that makes up the text.

RefusalDeltaBlock = object { index, type, refusal }

The refusal content that is part of a message.

index: number

The index of the refusal part in the message.

type: "refusal"

Always `refusal`.

refusal: optional string

ImageURLDeltaBlock = object { index, type, image\_url }

References an image URL in the content of a message.

index: number

The index of the content part in the message.

type: "image\_url"

Always `image_url`.

image\_url: optional [ImageURLDelta](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_delta%20%3E%20(schema)) { detail, url }

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

Accepts one of the following:

"auto"

"low"

"high"

url: optional string

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

role: optional "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

Accepts one of the following:

"user"

"assistant"

object: "thread.message.delta"

The object type, which is always `thread.message.delta`.

event: "thread.message.delta"

UnionMember21 = object { data, event }

Occurs when a [message](https://developers.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

If applicable, the ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) that authored this message.

attachments: array of object { file\_id, tools }

A list of files attached to the message, and the tools they were added to.

file\_id: optional string

The ID of the file to attach to the message.

tools: optional array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or object { type }

The tools to add this file to.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type }

type: "file\_search"

The type of tool being defined: `file_search`

completed\_at: number

The Unix timestamp (in seconds) for when the message was completed.

content: array of [ImageFileContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  or [RefusalContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

The content of the message in array of text and/or images.

Accepts one of the following:

ImageFileContentBlock = object { image\_file, type }

References an image [File](https://developers.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

file\_id: string

The [File](https://developers.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

ImageURLContentBlock = object { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

TextContentBlock = object { text, type }

The text content that is part of a message.

text: [Text](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

annotations: array of [FileCitationAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  or [FilePathAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

Accepts one of the following:

FileCitationAnnotation = object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file\_search" tool to search files.

end\_index: number

minimum0

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation = object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

RefusalContentBlock = object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

incomplete\_at: number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

incomplete\_details: object { reason }

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" or "max\_tokens" or "run\_cancelled" or 2 more

The reason the message is incomplete.

Accepts one of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

Accepts one of the following:

"user"

"assistant"

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

Accepts one of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](https://developers.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: "thread.message.completed"

UnionMember22 = object { data, event }

Occurs when a [message](https://developers.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](https://developers.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

If applicable, the ID of the [assistant](https://developers.openai.com/docs/api-reference/assistants) that authored this message.

attachments: array of object { file\_id, tools }

A list of files attached to the message, and the tools they were added to.

file\_id: optional string

The ID of the file to attach to the message.

tools: optional array of [CodeInterpreterTool](../index.md#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or object { type }

The tools to add this file to.

Accepts one of the following:

CodeInterpreterTool = object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool = object { type }

type: "file\_search"

The type of tool being defined: `file_search`

completed\_at: number

The Unix timestamp (in seconds) for when the message was completed.

content: array of [ImageFileContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file_content_block%20%3E%20(schema)) { image\_file, type }  or [ImageURLContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url_content_block%20%3E%20(schema)) { image\_url, type }  or [TextContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text_content_block%20%3E%20(schema)) { text, type }  or [RefusalContentBlock](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20refusal_content_block%20%3E%20(schema)) { refusal, type }

The content of the message in array of text and/or images.

Accepts one of the following:

ImageFileContentBlock = object { image\_file, type }

References an image [File](https://developers.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema)) { file\_id, detail }

file\_id: string

The [File](https://developers.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_file"

Always `image_file`.

ImageURLContentBlock = object { image\_url, type }

References an image URL in the content of a message.

image\_url: [ImageURL](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema)) { url, detail }

url: string

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

Accepts one of the following:

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

TextContentBlock = object { text, type }

The text content that is part of a message.

text: [Text](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema)) { annotations, value }

annotations: array of [FileCitationAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_citation_annotation%20%3E%20(schema)) { end\_index, file\_citation, start\_index, 2 more }  or [FilePathAnnotation](../index.md#(resource)%20beta.threads.messages%20%3E%20(model)%20file_path_annotation%20%3E%20(schema)) { end\_index, file\_path, start\_index, 2 more }

Accepts one of the following:

FileCitationAnnotation = object { end\_index, file\_citation, start\_index, 2 more }

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file\_search" tool to search files.

end\_index: number

minimum0

file\_citation: object { file\_id }

file\_id: string

The ID of the specific File the citation is from.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_citation"

Always `file_citation`.

FilePathAnnotation = object { end\_index, file\_path, start\_index, 2 more }

A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: number

minimum0

file\_path: object { file\_id }

file\_id: string

The ID of the file that was generated.

start\_index: number

minimum0

text: string

The text in the message content that needs to be replaced.

type: "file\_path"

Always `file_path`.

value: string

The data that makes up the text.

type: "text"

Always `text`.

RefusalContentBlock = object { refusal, type }

The refusal content generated by the assistant.

refusal: string

type: "refusal"

Always `refusal`.

created\_at: number

The Unix timestamp (in seconds) for when the message was created.

incomplete\_at: number

The Unix timestamp (in seconds) for when the message was marked as incomplete.

incomplete\_details: object { reason }

On an incomplete message, details about why the message is incomplete.

reason: "content\_filter" or "max\_tokens" or "run\_cancelled" or 2 more

The reason the message is incomplete.

Accepts one of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: [Metadata](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.message"

The object type, which is always `thread.message`.

role: "user" or "assistant"

The entity that produced the message. One of `user` or `assistant`.

Accepts one of the following:

"user"

"assistant"

run\_id: string

The ID of the [run](https://developers.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: "in\_progress" or "incomplete" or "completed"

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

Accepts one of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: string

The [thread](https://developers.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: "thread.message.incomplete"

ErrorEvent = object { data, event }

Occurs when an [error](https://developers.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data: [ErrorObject](../../$shared.md#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema)) { code, message, param, type }

code: string

message: string

param: string

type: string

event: "error"

DoneEvent = object { data, event }

Occurs when a stream ends.

data: "[DONE]"

event: "done"

OBJECT

### event

```
{}
```