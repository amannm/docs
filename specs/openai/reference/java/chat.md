# Chat

## Completions

### Create

`ChatCompletion chat().completions().create(ChatCompletionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/chat/completions`

**Starting a new project?** We recommend trying [Responses](https://platform.openai.com/docs/api-reference/responses)
to take advantage of the latest OpenAI platform features. Compare
[Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

---

Creates a model response for the given chat conversation. Learn more in the
[text generation](https://platform.openai.com/docs/guides/text-generation), [vision](https://platform.openai.com/docs/guides/vision),
and [audio](https://platform.openai.com/docs/guides/audio) guides.

Parameter support can differ depending on the model used to generate the
response, particularly for newer reasoning models. Parameters that are only
supported for reasoning models are noted below. For the current state of
unsupported parameters in reasoning models,
[refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

Returns a chat completion object, or a streamed sequence of chat completion
chunk objects if the request is streamed.

#### Parameters

- `ChatCompletionCreateParams params`

  - `List<ChatCompletionMessageParam> messages`

    A list of messages comprising the conversation so far. Depending on the
    [model](https://platform.openai.com/docs/models) you use, different message types (modalities) are
    supported, like [text](https://platform.openai.com/docs/guides/text-generation),
    [images](https://platform.openai.com/docs/guides/vision), and [audio](https://platform.openai.com/docs/guides/audio).

    - `class ChatCompletionDeveloperMessageParam:`

      Developer-provided instructions that the model should follow, regardless of
      messages sent by the user. With o1 models and newer, `developer` messages
      replace the previous `system` messages.

      - `Content content`

        The contents of the developer message.

        - `String`

        - `List<ChatCompletionContentPartText>`

          - `String text`

            The text content.

          - `JsonValue; type "text"constant`

            The type of the content part.

            - `TEXT("text")`

      - `JsonValue; role "developer"constant`

        The role of the messages author, in this case `developer`.

        - `DEVELOPER("developer")`

      - `Optional<String> name`

        An optional name for the participant. Provides the model information to differentiate between participants of the same role.

    - `class ChatCompletionSystemMessageParam:`

      Developer-provided instructions that the model should follow, regardless of
      messages sent by the user. With o1 models and newer, use `developer` messages
      for this purpose instead.

      - `Content content`

        The contents of the system message.

        - `String`

        - `List<ChatCompletionContentPartText>`

          - `String text`

            The text content.

          - `JsonValue; type "text"constant`

            The type of the content part.

            - `TEXT("text")`

      - `JsonValue; role "system"constant`

        The role of the messages author, in this case `system`.

        - `SYSTEM("system")`

      - `Optional<String> name`

        An optional name for the participant. Provides the model information to differentiate between participants of the same role.

    - `class ChatCompletionUserMessageParam:`

      Messages sent by an end user, containing prompts or additional context
      information.

      - `Content content`

        The contents of the user message.

        - `String`

        - `List<ChatCompletionContentPart>`

          - `class ChatCompletionContentPartText:`

            Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

            - `String text`

              The text content.

            - `JsonValue; type "text"constant`

              The type of the content part.

              - `TEXT("text")`

          - `class ChatCompletionContentPartImage:`

            Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

            - `ImageUrl imageUrl`

              - `String url`

                Either a URL of the image or the base64 encoded image data.

              - `Optional<Detail> detail`

                Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

            - `JsonValue; type "image_url"constant`

              The type of the content part.

              - `IMAGE_URL("image_url")`

          - `class ChatCompletionContentPartInputAudio:`

            Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

            - `InputAudio inputAudio`

              - `String data`

                Base64 encoded audio data.

              - `Format format`

                The format of the encoded audio data. Currently supports "wav" and "mp3".

                - `WAV("wav")`

                - `MP3("mp3")`

            - `JsonValue; type "input_audio"constant`

              The type of the content part. Always `input_audio`.

              - `INPUT_AUDIO("input_audio")`

          - `File`

            - `FileObject file`

              - `Optional<String> fileData`

                The base64 encoded file data, used when passing the file to the model
                as a string.

              - `Optional<String> fileId`

                The ID of an uploaded file to use as input.

              - `Optional<String> filename`

                The name of the file, used when passing the file to the model as a
                string.

            - `JsonValue; type "file"constant`

              The type of the content part. Always `file`.

              - `FILE("file")`

      - `JsonValue; role "user"constant`

        The role of the messages author, in this case `user`.

        - `USER("user")`

      - `Optional<String> name`

        An optional name for the participant. Provides the model information to differentiate between participants of the same role.

    - `class ChatCompletionAssistantMessageParam:`

      Messages sent by the model in response to user messages.

      - `JsonValue; role "assistant"constant`

        The role of the messages author, in this case `assistant`.

        - `ASSISTANT("assistant")`

      - `Optional<Audio> audio`

        Data about a previous audio response from the model.
        [Learn more](https://platform.openai.com/docs/guides/audio).

        - `String id`

          Unique identifier for a previous audio response from the model.

      - `Optional<Content> content`

        The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

        - `String`

        - `List<ChatCompletionRequestAssistantMessageContentPart>`

          - `class ChatCompletionContentPartText:`

            Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

            - `String text`

              The text content.

            - `JsonValue; type "text"constant`

              The type of the content part.

              - `TEXT("text")`

          - `class ChatCompletionContentPartRefusal:`

            - `String refusal`

              The refusal message generated by the model.

            - `JsonValue; type "refusal"constant`

              The type of the content part.

              - `REFUSAL("refusal")`

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `Optional<String> name`

        An optional name for the participant. Provides the model information to differentiate between participants of the same role.

      - `Optional<String> refusal`

        The refusal message by the assistant.

      - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

        The tool calls generated by the model, such as function calls.

        - `class ChatCompletionMessageFunctionToolCall:`

          A call to a function tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Function function`

            The function that the model called.

            - `String arguments`

              The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

            - `String name`

              The name of the function to call.

          - `JsonValue; type "function"constant`

            The type of the tool. Currently, only `function` is supported.

            - `FUNCTION("function")`

        - `class ChatCompletionMessageCustomToolCall:`

          A call to a custom tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Custom custom`

            The custom tool that the model called.

            - `String input`

              The input for the custom tool call generated by the model.

            - `String name`

              The name of the custom tool to call.

          - `JsonValue; type "custom"constant`

            The type of the tool. Always `custom`.

            - `CUSTOM("custom")`

    - `class ChatCompletionToolMessageParam:`

      - `Content content`

        The contents of the tool message.

        - `String`

        - `List<ChatCompletionContentPartText>`

          - `String text`

            The text content.

          - `JsonValue; type "text"constant`

            The type of the content part.

            - `TEXT("text")`

      - `JsonValue; role "tool"constant`

        The role of the messages author, in this case `tool`.

        - `TOOL("tool")`

      - `String toolCallId`

        Tool call that this message is responding to.

    - `class ChatCompletionFunctionMessageParam:`

      - `Optional<String> content`

        The contents of the function message.

      - `String name`

        The name of the function to call.

      - `JsonValue; role "function"constant`

        The role of the messages author, in this case `function`.

        - `FUNCTION("function")`

  - `ChatModel model`

    Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
    offers a wide range of models with different capabilities, performance
    characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
    to browse and compare available models.

    - `GPT_5_4("gpt-5.4")`

    - `GPT_5_3_CHAT_LATEST("gpt-5.3-chat-latest")`

    - `GPT_5_2("gpt-5.2")`

    - `GPT_5_2_2025_12_11("gpt-5.2-2025-12-11")`

    - `GPT_5_2_CHAT_LATEST("gpt-5.2-chat-latest")`

    - `GPT_5_2_PRO("gpt-5.2-pro")`

    - `GPT_5_2_PRO_2025_12_11("gpt-5.2-pro-2025-12-11")`

    - `GPT_5_1("gpt-5.1")`

    - `GPT_5_1_2025_11_13("gpt-5.1-2025-11-13")`

    - `GPT_5_1_CODEX("gpt-5.1-codex")`

    - `GPT_5_1_MINI("gpt-5.1-mini")`

    - `GPT_5_1_CHAT_LATEST("gpt-5.1-chat-latest")`

    - `GPT_5("gpt-5")`

    - `GPT_5_MINI("gpt-5-mini")`

    - `GPT_5_NANO("gpt-5-nano")`

    - `GPT_5_2025_08_07("gpt-5-2025-08-07")`

    - `GPT_5_MINI_2025_08_07("gpt-5-mini-2025-08-07")`

    - `GPT_5_NANO_2025_08_07("gpt-5-nano-2025-08-07")`

    - `GPT_5_CHAT_LATEST("gpt-5-chat-latest")`

    - `GPT_4_1("gpt-4.1")`

    - `GPT_4_1_MINI("gpt-4.1-mini")`

    - `GPT_4_1_NANO("gpt-4.1-nano")`

    - `GPT_4_1_2025_04_14("gpt-4.1-2025-04-14")`

    - `GPT_4_1_MINI_2025_04_14("gpt-4.1-mini-2025-04-14")`

    - `GPT_4_1_NANO_2025_04_14("gpt-4.1-nano-2025-04-14")`

    - `O4_MINI("o4-mini")`

    - `O4_MINI_2025_04_16("o4-mini-2025-04-16")`

    - `O3("o3")`

    - `O3_2025_04_16("o3-2025-04-16")`

    - `O3_MINI("o3-mini")`

    - `O3_MINI_2025_01_31("o3-mini-2025-01-31")`

    - `O1("o1")`

    - `O1_2024_12_17("o1-2024-12-17")`

    - `O1_PREVIEW("o1-preview")`

    - `O1_PREVIEW_2024_09_12("o1-preview-2024-09-12")`

    - `O1_MINI("o1-mini")`

    - `O1_MINI_2024_09_12("o1-mini-2024-09-12")`

    - `GPT_4O("gpt-4o")`

    - `GPT_4O_2024_11_20("gpt-4o-2024-11-20")`

    - `GPT_4O_2024_08_06("gpt-4o-2024-08-06")`

    - `GPT_4O_2024_05_13("gpt-4o-2024-05-13")`

    - `GPT_4O_AUDIO_PREVIEW("gpt-4o-audio-preview")`

    - `GPT_4O_AUDIO_PREVIEW_2024_10_01("gpt-4o-audio-preview-2024-10-01")`

    - `GPT_4O_AUDIO_PREVIEW_2024_12_17("gpt-4o-audio-preview-2024-12-17")`

    - `GPT_4O_AUDIO_PREVIEW_2025_06_03("gpt-4o-audio-preview-2025-06-03")`

    - `GPT_4O_MINI_AUDIO_PREVIEW("gpt-4o-mini-audio-preview")`

    - `GPT_4O_MINI_AUDIO_PREVIEW_2024_12_17("gpt-4o-mini-audio-preview-2024-12-17")`

    - `GPT_4O_SEARCH_PREVIEW("gpt-4o-search-preview")`

    - `GPT_4O_MINI_SEARCH_PREVIEW("gpt-4o-mini-search-preview")`

    - `GPT_4O_SEARCH_PREVIEW_2025_03_11("gpt-4o-search-preview-2025-03-11")`

    - `GPT_4O_MINI_SEARCH_PREVIEW_2025_03_11("gpt-4o-mini-search-preview-2025-03-11")`

    - `CHATGPT_4O_LATEST("chatgpt-4o-latest")`

    - `CODEX_MINI_LATEST("codex-mini-latest")`

    - `GPT_4O_MINI("gpt-4o-mini")`

    - `GPT_4O_MINI_2024_07_18("gpt-4o-mini-2024-07-18")`

    - `GPT_4_TURBO("gpt-4-turbo")`

    - `GPT_4_TURBO_2024_04_09("gpt-4-turbo-2024-04-09")`

    - `GPT_4_0125_PREVIEW("gpt-4-0125-preview")`

    - `GPT_4_TURBO_PREVIEW("gpt-4-turbo-preview")`

    - `GPT_4_1106_PREVIEW("gpt-4-1106-preview")`

    - `GPT_4_VISION_PREVIEW("gpt-4-vision-preview")`

    - `GPT_4("gpt-4")`

    - `GPT_4_0314("gpt-4-0314")`

    - `GPT_4_0613("gpt-4-0613")`

    - `GPT_4_32K("gpt-4-32k")`

    - `GPT_4_32K_0314("gpt-4-32k-0314")`

    - `GPT_4_32K_0613("gpt-4-32k-0613")`

    - `GPT_3_5_TURBO("gpt-3.5-turbo")`

    - `GPT_3_5_TURBO_16K("gpt-3.5-turbo-16k")`

    - `GPT_3_5_TURBO_0301("gpt-3.5-turbo-0301")`

    - `GPT_3_5_TURBO_0613("gpt-3.5-turbo-0613")`

    - `GPT_3_5_TURBO_1106("gpt-3.5-turbo-1106")`

    - `GPT_3_5_TURBO_0125("gpt-3.5-turbo-0125")`

    - `GPT_3_5_TURBO_16K_0613("gpt-3.5-turbo-16k-0613")`

  - `Optional<ChatCompletionAudioParam> audio`

    Parameters for audio output. Required when audio output is requested with
    `modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

  - `Optional<Double> frequencyPenalty`

    Number between -2.0 and 2.0. Positive values penalize new tokens based on
    their existing frequency in the text so far, decreasing the model's
    likelihood to repeat the same line verbatim.

  - `Optional<FunctionCall> functionCall`

    Deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model.

    `none` means the model will not call a function and instead generates a
    message.

    `auto` means the model can pick between generating a message or calling a
    function.

    Specifying a particular function via `{"name": "my_function"}` forces the
    model to call that function.

    `none` is the default when no functions are present. `auto` is the default
    if functions are present.

    - `enum FunctionCallMode:`

      `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function.

      - `NONE("none")`

      - `AUTO("auto")`

    - `class ChatCompletionFunctionCallOption:`

      Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

      - `String name`

        The name of the function to call.

  - `Optional<List<Function>> functions`

    Deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.

    - `String name`

      The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

    - `Optional<String> description`

      A description of what the function does, used by the model to choose when and how to call the function.

    - `Optional<FunctionParameters> parameters`

      The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

      Omitting `parameters` defines a function with an empty parameter list.

  - `Optional<LogitBias> logitBias`

    Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the
    tokenizer) to an associated bias value from -100 to 100. Mathematically,
    the bias is added to the logits generated by the model prior to sampling.
    The exact effect will vary per model, but values between -1 and 1 should
    decrease or increase likelihood of selection; values like -100 or 100
    should result in a ban or exclusive selection of the relevant token.

  - `Optional<Boolean> logprobs`

    Whether to return log probabilities of the output tokens or not. If true,
    returns the log probabilities of each output token returned in the
    `content` of `message`.

  - `Optional<Long> maxCompletionTokens`

    An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

  - `Optional<Long> maxTokens`

    The maximum number of [tokens](https://developers.openai.com/tokenizer) that can be generated in the
    chat completion. This value can be used to control
    [costs](https://openai.com/api/pricing/) for text generated via API.

    This value is now deprecated in favor of `max_completion_tokens`, and is
    not compatible with [o-series models](https://platform.openai.com/docs/guides/reasoning).

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<List<Modality>> modalities`

    Output types that you would like the model to generate.
    Most models are capable of generating text, which is the default:

    `["text"]`

    The `gpt-4o-audio-preview` model can also be used to
    [generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate
    both text and audio responses, you can use:

    `["text", "audio"]`

    - `TEXT("text")`

    - `AUDIO("audio")`

  - `Optional<Long> n`

    How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

  - `Optional<Boolean> parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<ChatCompletionPredictionContent> prediction`

    Static predicted output content, such as the content of a text file that is
    being regenerated.

  - `Optional<Double> presencePenalty`

    Number between -2.0 and 2.0. Positive values penalize new tokens based on
    whether they appear in the text so far, increasing the model's likelihood
    to talk about new topics.

  - `Optional<String> promptCacheKey`

    Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

  - `Optional<PromptCacheRetention> promptCacheRetention`

    The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).

    - `IN_MEMORY("in-memory")`

    - `_24H("24h")`

  - `Optional<ReasoningEffort> reasoningEffort`

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
    reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.

    - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
    - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
    - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
    - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

  - `Optional<ResponseFormat> responseFormat`

    An object specifying the format that the model must output.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
    Structured Outputs which ensures the model will match your supplied JSON
    schema. Learn more in the [Structured Outputs
    guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables the older JSON mode, which
    ensures the message the model generates is valid JSON. Using `json_schema`
    is preferred for models that support it.

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

  - `Optional<String> safetyIdentifier`

    A stable identifier used to help detect users of your application that may be violating OpenAI's usage policies.
    The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

  - `Optional<Long> seed`

    This feature is in Beta.
    If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
    Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<Stop> stop`

    Not supported with latest reasoning models `o3` and `o4-mini`.

    Up to 4 sequences where the API will stop generating further tokens. The
    returned text will not contain the stop sequence.

    - `String`

    - `List<String>`

  - `Optional<Boolean> store`

    Whether or not to store the output of this chat completion request for
    use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or
    [evals](https://platform.openai.com/docs/guides/evals) products.

    Supports text and image inputs. Note: image inputs over 8MB will be dropped.

  - `Optional<ChatCompletionStreamOptions> streamOptions`

    Options for streaming response. Only set this when you set `stream: true`.

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
    We generally recommend altering this or `top_p` but not both.

  - `Optional<ChatCompletionToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tool and instead generates a message.
    `auto` means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools.
    Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    `none` is the default when no tools are present. `auto` is the default if tools are present.

  - `Optional<List<ChatCompletionTool>> tools`

    A list of tools the model may call. You can provide either
    [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools) or
    [function tools](https://platform.openai.com/docs/guides/function-calling).

    - `class ChatCompletionFunctionTool:`

      A function tool that can be used to generate a response.

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of the tool. Currently, only `function` is supported.

        - `FUNCTION("function")`

    - `class ChatCompletionCustomTool:`

      A custom tool that processes input using a specified format.

      - `Custom custom`

        Properties of the custom tool.

        - `String name`

          The name of the custom tool, used to identify it in tool calls.

        - `Optional<String> description`

          Optional description of the custom tool, used to provide more context.

        - `Optional<Format> format`

          The input format for the custom tool. Default is unconstrained text.

          - `JsonValue;`

            - `JsonValue; type "text"constant`

              Unconstrained text format. Always `text`.

              - `TEXT("text")`

          - `class Grammar:`

            A grammar defined by the user.

            - `InnerGrammar grammar`

              Your chosen grammar.

              - `String definition`

                The grammar definition.

              - `Syntax syntax`

                The syntax of the grammar definition. One of `lark` or `regex`.

                - `LARK("lark")`

                - `REGEX("regex")`

            - `JsonValue; type "grammar"constant`

              Grammar format. Always `grammar`.

              - `GRAMMAR("grammar")`

      - `JsonValue; type "custom"constant`

        The type of the custom tool. Always `custom`.

        - `CUSTOM("custom")`

  - `Optional<Long> topLogprobs`

    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
    `logprobs` must be set to `true` if this parameter is used.

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling,
    where the model considers the results of the tokens with top_p probability
    mass. So 0.1 means only the tokens comprising the top 10% probability mass
    are considered.

    We generally recommend altering this or `temperature` but not both.

  - `Optional<String> user`

    This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
    A stable identifier for your end-users.
    Used to boost cache hit rates by better bucketing similar requests and  to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

  - `Optional<Verbosity> verbosity`

    Constrains the verbosity of the model's response. Lower values will result in
    more concise responses, while higher values will result in more verbose responses.
    Currently supported values are `low`, `medium`, and `high`.

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

  - `Optional<WebSearchOptions> webSearchOptions`

    This tool searches the web for relevant results to use in a response.
    Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

    - `Optional<SearchContextSize> searchContextSize`

      High level guidance for the amount of context window space to use for the
      search. One of `low`, `medium`, or `high`. `medium` is the default.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

    - `Optional<UserLocation> userLocation`

      Approximate location parameters for the search.

      - `Approximate approximate`

        Approximate location parameters for the search.

        - `Optional<String> city`

          Free text input for the city of the user, e.g. `San Francisco`.

        - `Optional<String> country`

          The two-letter
          [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user,
          e.g. `US`.

        - `Optional<String> region`

          Free text input for the region of the user, e.g. `California`.

        - `Optional<String> timezone`

          The [IANA timezone](https://timeapi.io/documentation/iana-timezones)
          of the user, e.g. `America/Los_Angeles`.

      - `JsonValue; type "approximate"constant`

        The type of location approximation. Always `approximate`.

        - `APPROXIMATE("approximate")`

#### Returns

- `class ChatCompletion:`

  Represents a chat completion response returned by model, based on the provided input.

  - `String id`

    A unique identifier for the chat completion.

  - `List<Choice> choices`

    A list of chat completion choices. Can be more than one if `n` is greater than 1.

    - `FinishReason finishReason`

      The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
      `length` if the maximum number of tokens specified in the request was reached,
      `content_filter` if content was omitted due to a flag from our content filters,
      `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

      - `STOP("stop")`

      - `LENGTH("length")`

      - `TOOL_CALLS("tool_calls")`

      - `CONTENT_FILTER("content_filter")`

      - `FUNCTION_CALL("function_call")`

    - `long index`

      The index of the choice in the list of choices.

    - `Optional<Logprobs> logprobs`

      Log probability information for the choice.

      - `Optional<List<ChatCompletionTokenLogprob>> content`

        A list of message content tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

      - `Optional<List<ChatCompletionTokenLogprob>> refusal`

        A list of message refusal tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

    - `ChatCompletionMessage message`

      A chat completion message generated by the model.

      - `Optional<String> content`

        The contents of the message.

      - `Optional<String> refusal`

        The refusal message generated by the model.

      - `JsonValue; role "assistant"constant`

        The role of the author of this message.

        - `ASSISTANT("assistant")`

      - `Optional<List<Annotation>> annotations`

        Annotations for the message, when applicable, as when using the
        [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        - `JsonValue; type "url_citation"constant`

          The type of the URL citation. Always `url_citation`.

          - `URL_CITATION("url_citation")`

        - `UrlCitation urlCitation`

          A URL citation when using web search.

          - `long endIndex`

            The index of the last character of the URL citation in the message.

          - `long startIndex`

            The index of the first character of the URL citation in the message.

          - `String title`

            The title of the web resource.

          - `String url`

            The URL of the web resource.

      - `Optional<ChatCompletionAudio> audio`

        If the audio output modality is requested, this object contains data
        about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - `String id`

          Unique identifier for this audio response.

        - `String data`

          Base64 encoded audio bytes generated by the model, in the format
          specified in the request.

        - `long expiresAt`

          The Unix timestamp (in seconds) for when this audio response will
          no longer be accessible on the server for use in multi-turn
          conversations.

        - `String transcript`

          Transcript of the audio generated by the model.

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

        The tool calls generated by the model, such as function calls.

        - `class ChatCompletionMessageFunctionToolCall:`

          A call to a function tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Function function`

            The function that the model called.

            - `String arguments`

              The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

            - `String name`

              The name of the function to call.

          - `JsonValue; type "function"constant`

            The type of the tool. Currently, only `function` is supported.

            - `FUNCTION("function")`

        - `class ChatCompletionMessageCustomToolCall:`

          A call to a custom tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Custom custom`

            The custom tool that the model called.

            - `String input`

              The input for the custom tool call generated by the model.

            - `String name`

              The name of the custom tool to call.

          - `JsonValue; type "custom"constant`

            The type of the tool. Always `custom`.

            - `CUSTOM("custom")`

  - `long created`

    The Unix timestamp (in seconds) of when the chat completion was created.

  - `String model`

    The model used for the chat completion.

  - `JsonValue; object_ "chat.completion"constant`

    The object type, which is always `chat.completion`.

    - `CHAT_COMPLETION("chat.completion")`

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<String> systemFingerprint`

    This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

  - `Optional<CompletionUsage> usage`

    Usage statistics for the completion request.

    - `long completionTokens`

      Number of tokens in the generated completion.

    - `long promptTokens`

      Number of tokens in the prompt.

    - `long totalTokens`

      Total number of tokens used in the request (prompt + completion).

    - `Optional<CompletionTokensDetails> completionTokensDetails`

      Breakdown of tokens used in a completion.

      - `Optional<Long> acceptedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that appeared in the completion.

      - `Optional<Long> audioTokens`

        Audio input tokens generated by the model.

      - `Optional<Long> reasoningTokens`

        Tokens generated by the model for reasoning.

      - `Optional<Long> rejectedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that did not appear in the completion. However, like
        reasoning tokens, these tokens are still counted in the total
        completion tokens for purposes of billing, output, and context window
        limits.

    - `Optional<PromptTokensDetails> promptTokensDetails`

      Breakdown of tokens used in the prompt.

      - `Optional<Long> audioTokens`

        Audio input tokens present in the prompt.

      - `Optional<Long> cachedTokens`

        Cached tokens present in the prompt.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
            .addDeveloperMessage("string")
            .model(ChatModel.GPT_5_4)
            .build();
        ChatCompletion chatCompletion = client.chat().completions().create(params);
    }
}
```

### List

`ChatCompletionListPage chat().completions().list(ChatCompletionListParamsparams = ChatCompletionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/chat/completions`

List stored Chat Completions. Only Chat Completions that have been stored
with the `store` parameter set to `true` will be returned.

#### Parameters

- `ChatCompletionListParams params`

  - `Optional<String> after`

    Identifier for the last chat completion from the previous pagination request.

  - `Optional<Long> limit`

    Number of Chat Completions to retrieve.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> model`

    The model used to generate the Chat Completions.

  - `Optional<Order> order`

    Sort order for Chat Completions by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

    - `ASC("asc")`

    - `DESC("desc")`

#### Returns

- `class ChatCompletion:`

  Represents a chat completion response returned by model, based on the provided input.

  - `String id`

    A unique identifier for the chat completion.

  - `List<Choice> choices`

    A list of chat completion choices. Can be more than one if `n` is greater than 1.

    - `FinishReason finishReason`

      The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
      `length` if the maximum number of tokens specified in the request was reached,
      `content_filter` if content was omitted due to a flag from our content filters,
      `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

      - `STOP("stop")`

      - `LENGTH("length")`

      - `TOOL_CALLS("tool_calls")`

      - `CONTENT_FILTER("content_filter")`

      - `FUNCTION_CALL("function_call")`

    - `long index`

      The index of the choice in the list of choices.

    - `Optional<Logprobs> logprobs`

      Log probability information for the choice.

      - `Optional<List<ChatCompletionTokenLogprob>> content`

        A list of message content tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

      - `Optional<List<ChatCompletionTokenLogprob>> refusal`

        A list of message refusal tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

    - `ChatCompletionMessage message`

      A chat completion message generated by the model.

      - `Optional<String> content`

        The contents of the message.

      - `Optional<String> refusal`

        The refusal message generated by the model.

      - `JsonValue; role "assistant"constant`

        The role of the author of this message.

        - `ASSISTANT("assistant")`

      - `Optional<List<Annotation>> annotations`

        Annotations for the message, when applicable, as when using the
        [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        - `JsonValue; type "url_citation"constant`

          The type of the URL citation. Always `url_citation`.

          - `URL_CITATION("url_citation")`

        - `UrlCitation urlCitation`

          A URL citation when using web search.

          - `long endIndex`

            The index of the last character of the URL citation in the message.

          - `long startIndex`

            The index of the first character of the URL citation in the message.

          - `String title`

            The title of the web resource.

          - `String url`

            The URL of the web resource.

      - `Optional<ChatCompletionAudio> audio`

        If the audio output modality is requested, this object contains data
        about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - `String id`

          Unique identifier for this audio response.

        - `String data`

          Base64 encoded audio bytes generated by the model, in the format
          specified in the request.

        - `long expiresAt`

          The Unix timestamp (in seconds) for when this audio response will
          no longer be accessible on the server for use in multi-turn
          conversations.

        - `String transcript`

          Transcript of the audio generated by the model.

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

        The tool calls generated by the model, such as function calls.

        - `class ChatCompletionMessageFunctionToolCall:`

          A call to a function tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Function function`

            The function that the model called.

            - `String arguments`

              The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

            - `String name`

              The name of the function to call.

          - `JsonValue; type "function"constant`

            The type of the tool. Currently, only `function` is supported.

            - `FUNCTION("function")`

        - `class ChatCompletionMessageCustomToolCall:`

          A call to a custom tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Custom custom`

            The custom tool that the model called.

            - `String input`

              The input for the custom tool call generated by the model.

            - `String name`

              The name of the custom tool to call.

          - `JsonValue; type "custom"constant`

            The type of the tool. Always `custom`.

            - `CUSTOM("custom")`

  - `long created`

    The Unix timestamp (in seconds) of when the chat completion was created.

  - `String model`

    The model used for the chat completion.

  - `JsonValue; object_ "chat.completion"constant`

    The object type, which is always `chat.completion`.

    - `CHAT_COMPLETION("chat.completion")`

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<String> systemFingerprint`

    This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

  - `Optional<CompletionUsage> usage`

    Usage statistics for the completion request.

    - `long completionTokens`

      Number of tokens in the generated completion.

    - `long promptTokens`

      Number of tokens in the prompt.

    - `long totalTokens`

      Total number of tokens used in the request (prompt + completion).

    - `Optional<CompletionTokensDetails> completionTokensDetails`

      Breakdown of tokens used in a completion.

      - `Optional<Long> acceptedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that appeared in the completion.

      - `Optional<Long> audioTokens`

        Audio input tokens generated by the model.

      - `Optional<Long> reasoningTokens`

        Tokens generated by the model for reasoning.

      - `Optional<Long> rejectedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that did not appear in the completion. However, like
        reasoning tokens, these tokens are still counted in the total
        completion tokens for purposes of billing, output, and context window
        limits.

    - `Optional<PromptTokensDetails> promptTokensDetails`

      Breakdown of tokens used in the prompt.

      - `Optional<Long> audioTokens`

        Audio input tokens present in the prompt.

      - `Optional<Long> cachedTokens`

        Cached tokens present in the prompt.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.chat.completions.ChatCompletionListPage;
import com.openai.models.chat.completions.ChatCompletionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletionListPage page = client.chat().completions().list();
    }
}
```

### Retrieve

`ChatCompletion chat().completions().retrieve(ChatCompletionRetrieveParamsparams = ChatCompletionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/chat/completions/{completion_id}`

Get a stored chat completion. Only Chat Completions that have been created
with the `store` parameter set to `true` will be returned.

#### Parameters

- `ChatCompletionRetrieveParams params`

  - `Optional<String> completionId`

#### Returns

- `class ChatCompletion:`

  Represents a chat completion response returned by model, based on the provided input.

  - `String id`

    A unique identifier for the chat completion.

  - `List<Choice> choices`

    A list of chat completion choices. Can be more than one if `n` is greater than 1.

    - `FinishReason finishReason`

      The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
      `length` if the maximum number of tokens specified in the request was reached,
      `content_filter` if content was omitted due to a flag from our content filters,
      `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

      - `STOP("stop")`

      - `LENGTH("length")`

      - `TOOL_CALLS("tool_calls")`

      - `CONTENT_FILTER("content_filter")`

      - `FUNCTION_CALL("function_call")`

    - `long index`

      The index of the choice in the list of choices.

    - `Optional<Logprobs> logprobs`

      Log probability information for the choice.

      - `Optional<List<ChatCompletionTokenLogprob>> content`

        A list of message content tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

      - `Optional<List<ChatCompletionTokenLogprob>> refusal`

        A list of message refusal tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

    - `ChatCompletionMessage message`

      A chat completion message generated by the model.

      - `Optional<String> content`

        The contents of the message.

      - `Optional<String> refusal`

        The refusal message generated by the model.

      - `JsonValue; role "assistant"constant`

        The role of the author of this message.

        - `ASSISTANT("assistant")`

      - `Optional<List<Annotation>> annotations`

        Annotations for the message, when applicable, as when using the
        [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        - `JsonValue; type "url_citation"constant`

          The type of the URL citation. Always `url_citation`.

          - `URL_CITATION("url_citation")`

        - `UrlCitation urlCitation`

          A URL citation when using web search.

          - `long endIndex`

            The index of the last character of the URL citation in the message.

          - `long startIndex`

            The index of the first character of the URL citation in the message.

          - `String title`

            The title of the web resource.

          - `String url`

            The URL of the web resource.

      - `Optional<ChatCompletionAudio> audio`

        If the audio output modality is requested, this object contains data
        about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - `String id`

          Unique identifier for this audio response.

        - `String data`

          Base64 encoded audio bytes generated by the model, in the format
          specified in the request.

        - `long expiresAt`

          The Unix timestamp (in seconds) for when this audio response will
          no longer be accessible on the server for use in multi-turn
          conversations.

        - `String transcript`

          Transcript of the audio generated by the model.

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

        The tool calls generated by the model, such as function calls.

        - `class ChatCompletionMessageFunctionToolCall:`

          A call to a function tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Function function`

            The function that the model called.

            - `String arguments`

              The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

            - `String name`

              The name of the function to call.

          - `JsonValue; type "function"constant`

            The type of the tool. Currently, only `function` is supported.

            - `FUNCTION("function")`

        - `class ChatCompletionMessageCustomToolCall:`

          A call to a custom tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Custom custom`

            The custom tool that the model called.

            - `String input`

              The input for the custom tool call generated by the model.

            - `String name`

              The name of the custom tool to call.

          - `JsonValue; type "custom"constant`

            The type of the tool. Always `custom`.

            - `CUSTOM("custom")`

  - `long created`

    The Unix timestamp (in seconds) of when the chat completion was created.

  - `String model`

    The model used for the chat completion.

  - `JsonValue; object_ "chat.completion"constant`

    The object type, which is always `chat.completion`.

    - `CHAT_COMPLETION("chat.completion")`

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<String> systemFingerprint`

    This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

  - `Optional<CompletionUsage> usage`

    Usage statistics for the completion request.

    - `long completionTokens`

      Number of tokens in the generated completion.

    - `long promptTokens`

      Number of tokens in the prompt.

    - `long totalTokens`

      Total number of tokens used in the request (prompt + completion).

    - `Optional<CompletionTokensDetails> completionTokensDetails`

      Breakdown of tokens used in a completion.

      - `Optional<Long> acceptedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that appeared in the completion.

      - `Optional<Long> audioTokens`

        Audio input tokens generated by the model.

      - `Optional<Long> reasoningTokens`

        Tokens generated by the model for reasoning.

      - `Optional<Long> rejectedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that did not appear in the completion. However, like
        reasoning tokens, these tokens are still counted in the total
        completion tokens for purposes of billing, output, and context window
        limits.

    - `Optional<PromptTokensDetails> promptTokensDetails`

      Breakdown of tokens used in the prompt.

      - `Optional<Long> audioTokens`

        Audio input tokens present in the prompt.

      - `Optional<Long> cachedTokens`

        Cached tokens present in the prompt.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletion chatCompletion = client.chat().completions().retrieve("completion_id");
    }
}
```

### Update

`ChatCompletion chat().completions().update(ChatCompletionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/chat/completions/{completion_id}`

Modify a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be modified. Currently,
the only supported modification is to update the `metadata` field.

#### Parameters

- `ChatCompletionUpdateParams params`

  - `Optional<String> completionId`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

#### Returns

- `class ChatCompletion:`

  Represents a chat completion response returned by model, based on the provided input.

  - `String id`

    A unique identifier for the chat completion.

  - `List<Choice> choices`

    A list of chat completion choices. Can be more than one if `n` is greater than 1.

    - `FinishReason finishReason`

      The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
      `length` if the maximum number of tokens specified in the request was reached,
      `content_filter` if content was omitted due to a flag from our content filters,
      `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

      - `STOP("stop")`

      - `LENGTH("length")`

      - `TOOL_CALLS("tool_calls")`

      - `CONTENT_FILTER("content_filter")`

      - `FUNCTION_CALL("function_call")`

    - `long index`

      The index of the choice in the list of choices.

    - `Optional<Logprobs> logprobs`

      Log probability information for the choice.

      - `Optional<List<ChatCompletionTokenLogprob>> content`

        A list of message content tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

      - `Optional<List<ChatCompletionTokenLogprob>> refusal`

        A list of message refusal tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

    - `ChatCompletionMessage message`

      A chat completion message generated by the model.

      - `Optional<String> content`

        The contents of the message.

      - `Optional<String> refusal`

        The refusal message generated by the model.

      - `JsonValue; role "assistant"constant`

        The role of the author of this message.

        - `ASSISTANT("assistant")`

      - `Optional<List<Annotation>> annotations`

        Annotations for the message, when applicable, as when using the
        [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        - `JsonValue; type "url_citation"constant`

          The type of the URL citation. Always `url_citation`.

          - `URL_CITATION("url_citation")`

        - `UrlCitation urlCitation`

          A URL citation when using web search.

          - `long endIndex`

            The index of the last character of the URL citation in the message.

          - `long startIndex`

            The index of the first character of the URL citation in the message.

          - `String title`

            The title of the web resource.

          - `String url`

            The URL of the web resource.

      - `Optional<ChatCompletionAudio> audio`

        If the audio output modality is requested, this object contains data
        about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - `String id`

          Unique identifier for this audio response.

        - `String data`

          Base64 encoded audio bytes generated by the model, in the format
          specified in the request.

        - `long expiresAt`

          The Unix timestamp (in seconds) for when this audio response will
          no longer be accessible on the server for use in multi-turn
          conversations.

        - `String transcript`

          Transcript of the audio generated by the model.

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

        The tool calls generated by the model, such as function calls.

        - `class ChatCompletionMessageFunctionToolCall:`

          A call to a function tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Function function`

            The function that the model called.

            - `String arguments`

              The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

            - `String name`

              The name of the function to call.

          - `JsonValue; type "function"constant`

            The type of the tool. Currently, only `function` is supported.

            - `FUNCTION("function")`

        - `class ChatCompletionMessageCustomToolCall:`

          A call to a custom tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Custom custom`

            The custom tool that the model called.

            - `String input`

              The input for the custom tool call generated by the model.

            - `String name`

              The name of the custom tool to call.

          - `JsonValue; type "custom"constant`

            The type of the tool. Always `custom`.

            - `CUSTOM("custom")`

  - `long created`

    The Unix timestamp (in seconds) of when the chat completion was created.

  - `String model`

    The model used for the chat completion.

  - `JsonValue; object_ "chat.completion"constant`

    The object type, which is always `chat.completion`.

    - `CHAT_COMPLETION("chat.completion")`

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<String> systemFingerprint`

    This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

  - `Optional<CompletionUsage> usage`

    Usage statistics for the completion request.

    - `long completionTokens`

      Number of tokens in the generated completion.

    - `long promptTokens`

      Number of tokens in the prompt.

    - `long totalTokens`

      Total number of tokens used in the request (prompt + completion).

    - `Optional<CompletionTokensDetails> completionTokensDetails`

      Breakdown of tokens used in a completion.

      - `Optional<Long> acceptedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that appeared in the completion.

      - `Optional<Long> audioTokens`

        Audio input tokens generated by the model.

      - `Optional<Long> reasoningTokens`

        Tokens generated by the model for reasoning.

      - `Optional<Long> rejectedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that did not appear in the completion. However, like
        reasoning tokens, these tokens are still counted in the total
        completion tokens for purposes of billing, output, and context window
        limits.

    - `Optional<PromptTokensDetails> promptTokensDetails`

      Breakdown of tokens used in the prompt.

      - `Optional<Long> audioTokens`

        Audio input tokens present in the prompt.

      - `Optional<Long> cachedTokens`

        Cached tokens present in the prompt.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletionUpdateParams params = ChatCompletionUpdateParams.builder()
            .completionId("completion_id")
            .metadata(ChatCompletionUpdateParams.Metadata.builder()
                .putAdditionalProperty("foo", JsonValue.from("string"))
                .build())
            .build();
        ChatCompletion chatCompletion = client.chat().completions().update(params);
    }
}
```

### Delete

`ChatCompletionDeleted chat().completions().delete(ChatCompletionDeleteParamsparams = ChatCompletionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/chat/completions/{completion_id}`

Delete a stored chat completion. Only Chat Completions that have been
created with the `store` parameter set to `true` can be deleted.

#### Parameters

- `ChatCompletionDeleteParams params`

  - `Optional<String> completionId`

#### Returns

- `class ChatCompletionDeleted:`

  - `String id`

    The ID of the chat completion that was deleted.

  - `boolean deleted`

    Whether the chat completion was deleted.

  - `JsonValue; object_ "chat.completion.deleted"constant`

    The type of object being deleted.

    - `CHAT_COMPLETION_DELETED("chat.completion.deleted")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.chat.completions.ChatCompletionDeleteParams;
import com.openai.models.chat.completions.ChatCompletionDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletionDeleted chatCompletionDeleted = client.chat().completions().delete("completion_id");
    }
}
```

#### Domain Types

#### Chat Completion

- `class ChatCompletion:`

  Represents a chat completion response returned by model, based on the provided input.

  - `String id`

    A unique identifier for the chat completion.

  - `List<Choice> choices`

    A list of chat completion choices. Can be more than one if `n` is greater than 1.

    - `FinishReason finishReason`

      The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
      `length` if the maximum number of tokens specified in the request was reached,
      `content_filter` if content was omitted due to a flag from our content filters,
      `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

      - `STOP("stop")`

      - `LENGTH("length")`

      - `TOOL_CALLS("tool_calls")`

      - `CONTENT_FILTER("content_filter")`

      - `FUNCTION_CALL("function_call")`

    - `long index`

      The index of the choice in the list of choices.

    - `Optional<Logprobs> logprobs`

      Log probability information for the choice.

      - `Optional<List<ChatCompletionTokenLogprob>> content`

        A list of message content tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

      - `Optional<List<ChatCompletionTokenLogprob>> refusal`

        A list of message refusal tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

    - `ChatCompletionMessage message`

      A chat completion message generated by the model.

      - `Optional<String> content`

        The contents of the message.

      - `Optional<String> refusal`

        The refusal message generated by the model.

      - `JsonValue; role "assistant"constant`

        The role of the author of this message.

        - `ASSISTANT("assistant")`

      - `Optional<List<Annotation>> annotations`

        Annotations for the message, when applicable, as when using the
        [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

        - `JsonValue; type "url_citation"constant`

          The type of the URL citation. Always `url_citation`.

          - `URL_CITATION("url_citation")`

        - `UrlCitation urlCitation`

          A URL citation when using web search.

          - `long endIndex`

            The index of the last character of the URL citation in the message.

          - `long startIndex`

            The index of the first character of the URL citation in the message.

          - `String title`

            The title of the web resource.

          - `String url`

            The URL of the web resource.

      - `Optional<ChatCompletionAudio> audio`

        If the audio output modality is requested, this object contains data
        about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

        - `String id`

          Unique identifier for this audio response.

        - `String data`

          Base64 encoded audio bytes generated by the model, in the format
          specified in the request.

        - `long expiresAt`

          The Unix timestamp (in seconds) for when this audio response will
          no longer be accessible on the server for use in multi-turn
          conversations.

        - `String transcript`

          Transcript of the audio generated by the model.

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

        The tool calls generated by the model, such as function calls.

        - `class ChatCompletionMessageFunctionToolCall:`

          A call to a function tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Function function`

            The function that the model called.

            - `String arguments`

              The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

            - `String name`

              The name of the function to call.

          - `JsonValue; type "function"constant`

            The type of the tool. Currently, only `function` is supported.

            - `FUNCTION("function")`

        - `class ChatCompletionMessageCustomToolCall:`

          A call to a custom tool created by the model.

          - `String id`

            The ID of the tool call.

          - `Custom custom`

            The custom tool that the model called.

            - `String input`

              The input for the custom tool call generated by the model.

            - `String name`

              The name of the custom tool to call.

          - `JsonValue; type "custom"constant`

            The type of the tool. Always `custom`.

            - `CUSTOM("custom")`

  - `long created`

    The Unix timestamp (in seconds) of when the chat completion was created.

  - `String model`

    The model used for the chat completion.

  - `JsonValue; object_ "chat.completion"constant`

    The object type, which is always `chat.completion`.

    - `CHAT_COMPLETION("chat.completion")`

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<String> systemFingerprint`

    This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

  - `Optional<CompletionUsage> usage`

    Usage statistics for the completion request.

    - `long completionTokens`

      Number of tokens in the generated completion.

    - `long promptTokens`

      Number of tokens in the prompt.

    - `long totalTokens`

      Total number of tokens used in the request (prompt + completion).

    - `Optional<CompletionTokensDetails> completionTokensDetails`

      Breakdown of tokens used in a completion.

      - `Optional<Long> acceptedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that appeared in the completion.

      - `Optional<Long> audioTokens`

        Audio input tokens generated by the model.

      - `Optional<Long> reasoningTokens`

        Tokens generated by the model for reasoning.

      - `Optional<Long> rejectedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that did not appear in the completion. However, like
        reasoning tokens, these tokens are still counted in the total
        completion tokens for purposes of billing, output, and context window
        limits.

    - `Optional<PromptTokensDetails> promptTokensDetails`

      Breakdown of tokens used in the prompt.

      - `Optional<Long> audioTokens`

        Audio input tokens present in the prompt.

      - `Optional<Long> cachedTokens`

        Cached tokens present in the prompt.

#### Chat Completion Allowed Tool Choice

- `class ChatCompletionAllowedToolChoice:`

  Constrains the tools available to the model to a pre-defined set.

  - `ChatCompletionAllowedTools allowedTools`

    Constrains the tools available to the model to a pre-defined set.

    - `Mode mode`

      Constrains the tools available to the model to a pre-defined set.

      `auto` allows the model to pick from among the allowed tools and generate a
      message.

      `required` requires the model to call one or more of the allowed tools.

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `List<Tool> tools`

      A list of tool definitions that the model should be allowed to call.

      For the Chat Completions API, the list of tool definitions might look like:

      ```json
      [
        { "type": "function", "function": { "name": "get_weather" } },
        { "type": "function", "function": { "name": "get_time" } }
      ]
      ```

  - `JsonValue; type "allowed_tools"constant`

    Allowed tool configuration type. Always `allowed_tools`.

    - `ALLOWED_TOOLS("allowed_tools")`

#### Chat Completion Assistant Message Param

- `class ChatCompletionAssistantMessageParam:`

  Messages sent by the model in response to user messages.

  - `JsonValue; role "assistant"constant`

    The role of the messages author, in this case `assistant`.

    - `ASSISTANT("assistant")`

  - `Optional<Audio> audio`

    Data about a previous audio response from the model.
    [Learn more](https://platform.openai.com/docs/guides/audio).

    - `String id`

      Unique identifier for a previous audio response from the model.

  - `Optional<Content> content`

    The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

    - `String`

    - `List<ChatCompletionRequestAssistantMessageContentPart>`

      - `class ChatCompletionContentPartText:`

        Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

        - `String text`

          The text content.

        - `JsonValue; type "text"constant`

          The type of the content part.

          - `TEXT("text")`

      - `class ChatCompletionContentPartRefusal:`

        - `String refusal`

          The refusal message generated by the model.

        - `JsonValue; type "refusal"constant`

          The type of the content part.

          - `REFUSAL("refusal")`

  - `Optional<FunctionCall> functionCall`

    Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

    - `String arguments`

      The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

    - `String name`

      The name of the function to call.

  - `Optional<String> name`

    An optional name for the participant. Provides the model information to differentiate between participants of the same role.

  - `Optional<String> refusal`

    The refusal message by the assistant.

  - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

    The tool calls generated by the model, such as function calls.

    - `class ChatCompletionMessageFunctionToolCall:`

      A call to a function tool created by the model.

      - `String id`

        The ID of the tool call.

      - `Function function`

        The function that the model called.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `JsonValue; type "function"constant`

        The type of the tool. Currently, only `function` is supported.

        - `FUNCTION("function")`

    - `class ChatCompletionMessageCustomToolCall:`

      A call to a custom tool created by the model.

      - `String id`

        The ID of the tool call.

      - `Custom custom`

        The custom tool that the model called.

        - `String input`

          The input for the custom tool call generated by the model.

        - `String name`

          The name of the custom tool to call.

      - `JsonValue; type "custom"constant`

        The type of the tool. Always `custom`.

        - `CUSTOM("custom")`

#### Chat Completion Audio

- `class ChatCompletionAudio:`

  If the audio output modality is requested, this object contains data
  about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

  - `String id`

    Unique identifier for this audio response.

  - `String data`

    Base64 encoded audio bytes generated by the model, in the format
    specified in the request.

  - `long expiresAt`

    The Unix timestamp (in seconds) for when this audio response will
    no longer be accessible on the server for use in multi-turn
    conversations.

  - `String transcript`

    Transcript of the audio generated by the model.

#### Chat Completion Audio Param

- `class ChatCompletionAudioParam:`

  Parameters for audio output. Required when audio output is requested with
  `modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

  - `Format format`

    Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
    `opus`, or `pcm16`.

    - `WAV("wav")`

    - `AAC("aac")`

    - `MP3("mp3")`

    - `FLAC("flac")`

    - `OPUS("opus")`

    - `PCM16("pcm16")`

  - `Voice voice`

    The voice the model uses to respond. Supported built-in voices are
    `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`,
    `sage`, `shimmer`, `marin`, and `cedar`. You may also provide a
    custom voice object with an `id`, for example `{ "id": "voice_1234" }`.

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

#### Chat Completion Chunk

- `class ChatCompletionChunk:`

  Represents a streamed chunk of a chat completion response returned
  by the model, based on the provided input.
  [Learn more](https://platform.openai.com/docs/guides/streaming-responses).

  - `String id`

    A unique identifier for the chat completion. Each chunk has the same ID.

  - `List<Choice> choices`

    A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
    last chunk if you set `stream_options: {"include_usage": true}`.

    - `Delta delta`

      A chat completion delta generated by streamed model responses.

      - `Optional<String> content`

        The contents of the chunk message.

      - `Optional<FunctionCall> functionCall`

        Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

        - `Optional<String> arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `Optional<String> name`

          The name of the function to call.

      - `Optional<String> refusal`

        The refusal message generated by the model.

      - `Optional<Role> role`

        The role of the author of this message.

        - `DEVELOPER("developer")`

        - `SYSTEM("system")`

        - `USER("user")`

        - `ASSISTANT("assistant")`

        - `TOOL("tool")`

      - `Optional<List<ToolCall>> toolCalls`

        - `long index`

        - `Optional<String> id`

          The ID of the tool call.

        - `Optional<Function> function`

          - `Optional<String> arguments`

            The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

          - `Optional<String> name`

            The name of the function to call.

        - `Optional<Type> type`

          The type of the tool. Currently, only `function` is supported.

          - `FUNCTION("function")`

    - `Optional<FinishReason> finishReason`

      The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
      `length` if the maximum number of tokens specified in the request was reached,
      `content_filter` if content was omitted due to a flag from our content filters,
      `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

      - `STOP("stop")`

      - `LENGTH("length")`

      - `TOOL_CALLS("tool_calls")`

      - `CONTENT_FILTER("content_filter")`

      - `FUNCTION_CALL("function_call")`

    - `long index`

      The index of the choice in the list of choices.

    - `Optional<Logprobs> logprobs`

      Log probability information for the choice.

      - `Optional<List<ChatCompletionTokenLogprob>> content`

        A list of message content tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

      - `Optional<List<ChatCompletionTokenLogprob>> refusal`

        A list of message refusal tokens with log probability information.

        - `String token`

          The token.

        - `Optional<List<Long>> bytes`

          A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

        - `double logprob`

          The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

        - `List<TopLogprob> topLogprobs`

          List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

          - `String token`

            The token.

          - `Optional<List<Long>> bytes`

            A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

          - `double logprob`

            The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

  - `long created`

    The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

  - `String model`

    The model to generate the completion.

  - `JsonValue; object_ "chat.completion.chunk"constant`

    The object type, which is always `chat.completion.chunk`.

    - `CHAT_COMPLETION_CHUNK("chat.completion.chunk")`

  - `Optional<ServiceTier> serviceTier`

    Specifies the processing type used for serving the request.

    - If set to 'auto', then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use 'default'.
    - If set to 'default', then the request will be processed with the standard pricing and performance for the selected model.
    - If set to '[flex](https://platform.openai.com/docs/guides/flex-processing)' or '[priority](https://openai.com/api-priority-processing/)', then the request will be processed with the corresponding service tier.
    - When not set, the default behavior is 'auto'.

    When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `SCALE("scale")`

    - `PRIORITY("priority")`

  - `Optional<String> systemFingerprint`

    This fingerprint represents the backend configuration that the model runs with.
    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

  - `Optional<CompletionUsage> usage`

    An optional field that will only be present when you set
    `stream_options: {"include_usage": true}` in your request. When present, it
    contains a null value **except for the last chunk** which contains the
    token usage statistics for the entire request.

    **NOTE:** If the stream is interrupted or cancelled, you may not
    receive the final usage chunk which contains the total token usage for
    the request.

    - `long completionTokens`

      Number of tokens in the generated completion.

    - `long promptTokens`

      Number of tokens in the prompt.

    - `long totalTokens`

      Total number of tokens used in the request (prompt + completion).

    - `Optional<CompletionTokensDetails> completionTokensDetails`

      Breakdown of tokens used in a completion.

      - `Optional<Long> acceptedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that appeared in the completion.

      - `Optional<Long> audioTokens`

        Audio input tokens generated by the model.

      - `Optional<Long> reasoningTokens`

        Tokens generated by the model for reasoning.

      - `Optional<Long> rejectedPredictionTokens`

        When using Predicted Outputs, the number of tokens in the
        prediction that did not appear in the completion. However, like
        reasoning tokens, these tokens are still counted in the total
        completion tokens for purposes of billing, output, and context window
        limits.

    - `Optional<PromptTokensDetails> promptTokensDetails`

      Breakdown of tokens used in the prompt.

      - `Optional<Long> audioTokens`

        Audio input tokens present in the prompt.

      - `Optional<Long> cachedTokens`

        Cached tokens present in the prompt.

#### Chat Completion Content Part

- `class ChatCompletionContentPart: A class that can be one of several variants.union`

  Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

  - `class ChatCompletionContentPartText:`

    Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

    - `String text`

      The text content.

    - `JsonValue; type "text"constant`

      The type of the content part.

      - `TEXT("text")`

  - `class ChatCompletionContentPartImage:`

    Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

    - `ImageUrl imageUrl`

      - `String url`

        Either a URL of the image or the base64 encoded image data.

      - `Optional<Detail> detail`

        Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

    - `JsonValue; type "image_url"constant`

      The type of the content part.

      - `IMAGE_URL("image_url")`

  - `class ChatCompletionContentPartInputAudio:`

    Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

    - `InputAudio inputAudio`

      - `String data`

        Base64 encoded audio data.

      - `Format format`

        The format of the encoded audio data. Currently supports "wav" and "mp3".

        - `WAV("wav")`

        - `MP3("mp3")`

    - `JsonValue; type "input_audio"constant`

      The type of the content part. Always `input_audio`.

      - `INPUT_AUDIO("input_audio")`

  - `File`

    - `FileObject file`

      - `Optional<String> fileData`

        The base64 encoded file data, used when passing the file to the model
        as a string.

      - `Optional<String> fileId`

        The ID of an uploaded file to use as input.

      - `Optional<String> filename`

        The name of the file, used when passing the file to the model as a
        string.

    - `JsonValue; type "file"constant`

      The type of the content part. Always `file`.

      - `FILE("file")`

#### Chat Completion Content Part Image

- `class ChatCompletionContentPartImage:`

  Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

  - `ImageUrl imageUrl`

    - `String url`

      Either a URL of the image or the base64 encoded image data.

    - `Optional<Detail> detail`

      Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

      - `AUTO("auto")`

      - `LOW("low")`

      - `HIGH("high")`

  - `JsonValue; type "image_url"constant`

    The type of the content part.

    - `IMAGE_URL("image_url")`

#### Chat Completion Content Part Input Audio

- `class ChatCompletionContentPartInputAudio:`

  Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

  - `InputAudio inputAudio`

    - `String data`

      Base64 encoded audio data.

    - `Format format`

      The format of the encoded audio data. Currently supports "wav" and "mp3".

      - `WAV("wav")`

      - `MP3("mp3")`

  - `JsonValue; type "input_audio"constant`

    The type of the content part. Always `input_audio`.

    - `INPUT_AUDIO("input_audio")`

#### Chat Completion Content Part Refusal

- `class ChatCompletionContentPartRefusal:`

  - `String refusal`

    The refusal message generated by the model.

  - `JsonValue; type "refusal"constant`

    The type of the content part.

    - `REFUSAL("refusal")`

#### Chat Completion Content Part Text

- `class ChatCompletionContentPartText:`

  Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

  - `String text`

    The text content.

  - `JsonValue; type "text"constant`

    The type of the content part.

    - `TEXT("text")`

#### Chat Completion Custom Tool

- `class ChatCompletionCustomTool:`

  A custom tool that processes input using a specified format.

  - `Custom custom`

    Properties of the custom tool.

    - `String name`

      The name of the custom tool, used to identify it in tool calls.

    - `Optional<String> description`

      Optional description of the custom tool, used to provide more context.

    - `Optional<Format> format`

      The input format for the custom tool. Default is unconstrained text.

      - `JsonValue;`

        - `JsonValue; type "text"constant`

          Unconstrained text format. Always `text`.

          - `TEXT("text")`

      - `class Grammar:`

        A grammar defined by the user.

        - `InnerGrammar grammar`

          Your chosen grammar.

          - `String definition`

            The grammar definition.

          - `Syntax syntax`

            The syntax of the grammar definition. One of `lark` or `regex`.

            - `LARK("lark")`

            - `REGEX("regex")`

        - `JsonValue; type "grammar"constant`

          Grammar format. Always `grammar`.

          - `GRAMMAR("grammar")`

  - `JsonValue; type "custom"constant`

    The type of the custom tool. Always `custom`.

    - `CUSTOM("custom")`

#### Chat Completion Deleted

- `class ChatCompletionDeleted:`

  - `String id`

    The ID of the chat completion that was deleted.

  - `boolean deleted`

    Whether the chat completion was deleted.

  - `JsonValue; object_ "chat.completion.deleted"constant`

    The type of object being deleted.

    - `CHAT_COMPLETION_DELETED("chat.completion.deleted")`

#### Chat Completion Developer Message Param

- `class ChatCompletionDeveloperMessageParam:`

  Developer-provided instructions that the model should follow, regardless of
  messages sent by the user. With o1 models and newer, `developer` messages
  replace the previous `system` messages.

  - `Content content`

    The contents of the developer message.

    - `String`

    - `List<ChatCompletionContentPartText>`

      - `String text`

        The text content.

      - `JsonValue; type "text"constant`

        The type of the content part.

        - `TEXT("text")`

  - `JsonValue; role "developer"constant`

    The role of the messages author, in this case `developer`.

    - `DEVELOPER("developer")`

  - `Optional<String> name`

    An optional name for the participant. Provides the model information to differentiate between participants of the same role.

#### Chat Completion Function Call Option

- `class ChatCompletionFunctionCallOption:`

  Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

  - `String name`

    The name of the function to call.

#### Chat Completion Function Message Param

- `class ChatCompletionFunctionMessageParam:`

  - `Optional<String> content`

    The contents of the function message.

  - `String name`

    The name of the function to call.

  - `JsonValue; role "function"constant`

    The role of the messages author, in this case `function`.

    - `FUNCTION("function")`

#### Chat Completion Function Tool

- `class ChatCompletionFunctionTool:`

  A function tool that can be used to generate a response.

  - `FunctionDefinition function`

    - `String name`

      The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

    - `Optional<String> description`

      A description of what the function does, used by the model to choose when and how to call the function.

    - `Optional<FunctionParameters> parameters`

      The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

      Omitting `parameters` defines a function with an empty parameter list.

    - `Optional<Boolean> strict`

      Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

  - `JsonValue; type "function"constant`

    The type of the tool. Currently, only `function` is supported.

    - `FUNCTION("function")`

#### Chat Completion Message

- `class ChatCompletionMessage:`

  A chat completion message generated by the model.

  - `Optional<String> content`

    The contents of the message.

  - `Optional<String> refusal`

    The refusal message generated by the model.

  - `JsonValue; role "assistant"constant`

    The role of the author of this message.

    - `ASSISTANT("assistant")`

  - `Optional<List<Annotation>> annotations`

    Annotations for the message, when applicable, as when using the
    [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

    - `JsonValue; type "url_citation"constant`

      The type of the URL citation. Always `url_citation`.

      - `URL_CITATION("url_citation")`

    - `UrlCitation urlCitation`

      A URL citation when using web search.

      - `long endIndex`

        The index of the last character of the URL citation in the message.

      - `long startIndex`

        The index of the first character of the URL citation in the message.

      - `String title`

        The title of the web resource.

      - `String url`

        The URL of the web resource.

  - `Optional<ChatCompletionAudio> audio`

    If the audio output modality is requested, this object contains data
    about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

    - `String id`

      Unique identifier for this audio response.

    - `String data`

      Base64 encoded audio bytes generated by the model, in the format
      specified in the request.

    - `long expiresAt`

      The Unix timestamp (in seconds) for when this audio response will
      no longer be accessible on the server for use in multi-turn
      conversations.

    - `String transcript`

      Transcript of the audio generated by the model.

  - `Optional<FunctionCall> functionCall`

    Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

    - `String arguments`

      The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

    - `String name`

      The name of the function to call.

  - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

    The tool calls generated by the model, such as function calls.

    - `class ChatCompletionMessageFunctionToolCall:`

      A call to a function tool created by the model.

      - `String id`

        The ID of the tool call.

      - `Function function`

        The function that the model called.

        - `String arguments`

          The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

        - `String name`

          The name of the function to call.

      - `JsonValue; type "function"constant`

        The type of the tool. Currently, only `function` is supported.

        - `FUNCTION("function")`

    - `class ChatCompletionMessageCustomToolCall:`

      A call to a custom tool created by the model.

      - `String id`

        The ID of the tool call.

      - `Custom custom`

        The custom tool that the model called.

        - `String input`

          The input for the custom tool call generated by the model.

        - `String name`

          The name of the custom tool to call.

      - `JsonValue; type "custom"constant`

        The type of the tool. Always `custom`.

        - `CUSTOM("custom")`

#### Chat Completion Message Custom Tool Call

- `class ChatCompletionMessageCustomToolCall:`

  A call to a custom tool created by the model.

  - `String id`

    The ID of the tool call.

  - `Custom custom`

    The custom tool that the model called.

    - `String input`

      The input for the custom tool call generated by the model.

    - `String name`

      The name of the custom tool to call.

  - `JsonValue; type "custom"constant`

    The type of the tool. Always `custom`.

    - `CUSTOM("custom")`

#### Chat Completion Message Function Tool Call

- `class ChatCompletionMessageFunctionToolCall:`

  A call to a function tool created by the model.

  - `String id`

    The ID of the tool call.

  - `Function function`

    The function that the model called.

    - `String arguments`

      The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

    - `String name`

      The name of the function to call.

  - `JsonValue; type "function"constant`

    The type of the tool. Currently, only `function` is supported.

    - `FUNCTION("function")`

#### Chat Completion Message Param

- `class ChatCompletionMessageParam: A class that can be one of several variants.union`

  Developer-provided instructions that the model should follow, regardless of
  messages sent by the user. With o1 models and newer, `developer` messages
  replace the previous `system` messages.

  - `class ChatCompletionDeveloperMessageParam:`

    Developer-provided instructions that the model should follow, regardless of
    messages sent by the user. With o1 models and newer, `developer` messages
    replace the previous `system` messages.

    - `Content content`

      The contents of the developer message.

      - `String`

      - `List<ChatCompletionContentPartText>`

        - `String text`

          The text content.

        - `JsonValue; type "text"constant`

          The type of the content part.

          - `TEXT("text")`

    - `JsonValue; role "developer"constant`

      The role of the messages author, in this case `developer`.

      - `DEVELOPER("developer")`

    - `Optional<String> name`

      An optional name for the participant. Provides the model information to differentiate between participants of the same role.

  - `class ChatCompletionSystemMessageParam:`

    Developer-provided instructions that the model should follow, regardless of
    messages sent by the user. With o1 models and newer, use `developer` messages
    for this purpose instead.

    - `Content content`

      The contents of the system message.

      - `String`

      - `List<ChatCompletionContentPartText>`

        - `String text`

          The text content.

        - `JsonValue; type "text"constant`

          The type of the content part.

          - `TEXT("text")`

    - `JsonValue; role "system"constant`

      The role of the messages author, in this case `system`.

      - `SYSTEM("system")`

    - `Optional<String> name`

      An optional name for the participant. Provides the model information to differentiate between participants of the same role.

  - `class ChatCompletionUserMessageParam:`

    Messages sent by an end user, containing prompts or additional context
    information.

    - `Content content`

      The contents of the user message.

      - `String`

      - `List<ChatCompletionContentPart>`

        - `class ChatCompletionContentPartText:`

          Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

          - `String text`

            The text content.

          - `JsonValue; type "text"constant`

            The type of the content part.

            - `TEXT("text")`

        - `class ChatCompletionContentPartImage:`

          Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

          - `ImageUrl imageUrl`

            - `String url`

              Either a URL of the image or the base64 encoded image data.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class ChatCompletionContentPartInputAudio:`

          Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

          - `InputAudio inputAudio`

            - `String data`

              Base64 encoded audio data.

            - `Format format`

              The format of the encoded audio data. Currently supports "wav" and "mp3".

              - `WAV("wav")`

              - `MP3("mp3")`

          - `JsonValue; type "input_audio"constant`

            The type of the content part. Always `input_audio`.

            - `INPUT_AUDIO("input_audio")`

        - `File`

          - `FileObject file`

            - `Optional<String> fileData`

              The base64 encoded file data, used when passing the file to the model
              as a string.

            - `Optional<String> fileId`

              The ID of an uploaded file to use as input.

            - `Optional<String> filename`

              The name of the file, used when passing the file to the model as a
              string.

          - `JsonValue; type "file"constant`

            The type of the content part. Always `file`.

            - `FILE("file")`

    - `JsonValue; role "user"constant`

      The role of the messages author, in this case `user`.

      - `USER("user")`

    - `Optional<String> name`

      An optional name for the participant. Provides the model information to differentiate between participants of the same role.

  - `class ChatCompletionAssistantMessageParam:`

    Messages sent by the model in response to user messages.

    - `JsonValue; role "assistant"constant`

      The role of the messages author, in this case `assistant`.

      - `ASSISTANT("assistant")`

    - `Optional<Audio> audio`

      Data about a previous audio response from the model.
      [Learn more](https://platform.openai.com/docs/guides/audio).

      - `String id`

        Unique identifier for a previous audio response from the model.

    - `Optional<Content> content`

      The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

      - `String`

      - `List<ChatCompletionRequestAssistantMessageContentPart>`

        - `class ChatCompletionContentPartText:`

          Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

          - `String text`

            The text content.

          - `JsonValue; type "text"constant`

            The type of the content part.

            - `TEXT("text")`

        - `class ChatCompletionContentPartRefusal:`

          - `String refusal`

            The refusal message generated by the model.

          - `JsonValue; type "refusal"constant`

            The type of the content part.

            - `REFUSAL("refusal")`

    - `Optional<FunctionCall> functionCall`

      Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

      - `String arguments`

        The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

      - `String name`

        The name of the function to call.

    - `Optional<String> name`

      An optional name for the participant. Provides the model information to differentiate between participants of the same role.

    - `Optional<String> refusal`

      The refusal message by the assistant.

    - `Optional<List<ChatCompletionMessageToolCall>> toolCalls`

      The tool calls generated by the model, such as function calls.

      - `class ChatCompletionMessageFunctionToolCall:`

        A call to a function tool created by the model.

        - `String id`

          The ID of the tool call.

        - `Function function`

          The function that the model called.

          - `String arguments`

            The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

          - `String name`

            The name of the function to call.

        - `JsonValue; type "function"constant`

          The type of the tool. Currently, only `function` is supported.

          - `FUNCTION("function")`

      - `class ChatCompletionMessageCustomToolCall:`

        A call to a custom tool created by the model.

        - `String id`

          The ID of the tool call.

        - `Custom custom`

          The custom tool that the model called.

          - `String input`

            The input for the custom tool call generated by the model.

          - `String name`

            The name of the custom tool to call.

        - `JsonValue; type "custom"constant`

          The type of the tool. Always `custom`.

          - `CUSTOM("custom")`

  - `class ChatCompletionToolMessageParam:`

    - `Content content`

      The contents of the tool message.

      - `String`

      - `List<ChatCompletionContentPartText>`

        - `String text`

          The text content.

        - `JsonValue; type "text"constant`

          The type of the content part.

          - `TEXT("text")`

    - `JsonValue; role "tool"constant`

      The role of the messages author, in this case `tool`.

      - `TOOL("tool")`

    - `String toolCallId`

      Tool call that this message is responding to.

  - `class ChatCompletionFunctionMessageParam:`

    - `Optional<String> content`

      The contents of the function message.

    - `String name`

      The name of the function to call.

    - `JsonValue; role "function"constant`

      The role of the messages author, in this case `function`.

      - `FUNCTION("function")`

#### Chat Completion Message Tool Call

- `class ChatCompletionMessageToolCall: A class that can be one of several variants.union`

  A call to a function tool created by the model.

  - `class ChatCompletionMessageFunctionToolCall:`

    A call to a function tool created by the model.

    - `String id`

      The ID of the tool call.

    - `Function function`

      The function that the model called.

      - `String arguments`

        The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

      - `String name`

        The name of the function to call.

    - `JsonValue; type "function"constant`

      The type of the tool. Currently, only `function` is supported.

      - `FUNCTION("function")`

  - `class ChatCompletionMessageCustomToolCall:`

    A call to a custom tool created by the model.

    - `String id`

      The ID of the tool call.

    - `Custom custom`

      The custom tool that the model called.

      - `String input`

        The input for the custom tool call generated by the model.

      - `String name`

        The name of the custom tool to call.

    - `JsonValue; type "custom"constant`

      The type of the tool. Always `custom`.

      - `CUSTOM("custom")`

#### Chat Completion Modality

- `enum ChatCompletionModality:`

  - `TEXT("text")`

  - `AUDIO("audio")`

#### Chat Completion Named Tool Choice

- `class ChatCompletionNamedToolChoice:`

  Specifies a tool the model should use. Use to force the model to call a specific function.

  - `Function function`

    - `String name`

      The name of the function to call.

  - `JsonValue; type "function"constant`

    For function calling, the type is always `function`.

    - `FUNCTION("function")`

#### Chat Completion Named Tool Choice Custom

- `class ChatCompletionNamedToolChoiceCustom:`

  Specifies a tool the model should use. Use to force the model to call a specific custom tool.

  - `Custom custom`

    - `String name`

      The name of the custom tool to call.

  - `JsonValue; type "custom"constant`

    For custom tool calling, the type is always `custom`.

    - `CUSTOM("custom")`

#### Chat Completion Prediction Content

- `class ChatCompletionPredictionContent:`

  Static predicted output content, such as the content of a text file that is
  being regenerated.

  - `Content content`

    The content that should be matched when generating a model response.
    If generated tokens would match this content, the entire model response
    can be returned much more quickly.

    - `String`

    - `List<ChatCompletionContentPartText>`

      - `String text`

        The text content.

      - `JsonValue; type "text"constant`

        The type of the content part.

        - `TEXT("text")`

  - `JsonValue; type "content"constant`

    The type of the predicted content you want to provide. This type is
    currently always `content`.

    - `CONTENT("content")`

#### Chat Completion Role

- `enum ChatCompletionRole:`

  The role of the author of a message

  - `DEVELOPER("developer")`

  - `SYSTEM("system")`

  - `USER("user")`

  - `ASSISTANT("assistant")`

  - `TOOL("tool")`

  - `FUNCTION("function")`

#### Chat Completion Store Message

- `class ChatCompletionStoreMessage:`

  A chat completion message generated by the model.

  - `String id`

    The identifier of the chat message.

  - `Optional<List<ContentPart>> contentParts`

    If a content parts array was provided, this is an array of `text` and `image_url` parts.
    Otherwise, null.

    - `class ChatCompletionContentPartText:`

      Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

      - `String text`

        The text content.

      - `JsonValue; type "text"constant`

        The type of the content part.

        - `TEXT("text")`

    - `class ChatCompletionContentPartImage:`

      Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

      - `ImageUrl imageUrl`

        - `String url`

          Either a URL of the image or the base64 encoded image data.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

#### Chat Completion Stream Options

- `class ChatCompletionStreamOptions:`

  Options for streaming response. Only set this when you set `stream: true`.

  - `Optional<Boolean> includeObfuscation`

    When true, stream obfuscation will be enabled. Stream obfuscation adds
    random characters to an `obfuscation` field on streaming delta events to
    normalize payload sizes as a mitigation to certain side-channel attacks.
    These obfuscation fields are included by default, but add a small amount
    of overhead to the data stream. You can set `include_obfuscation` to
    false to optimize for bandwidth if you trust the network links between
    your application and the OpenAI API.

  - `Optional<Boolean> includeUsage`

    If set, an additional chunk will be streamed before the `data: [DONE]`
    message. The `usage` field on this chunk shows the token usage statistics
    for the entire request, and the `choices` field will always be an empty
    array.

    All other chunks will also include a `usage` field, but with a null
    value. **NOTE:** If the stream is interrupted, you may not receive the
    final usage chunk which contains the total token usage for the request.

#### Chat Completion System Message Param

- `class ChatCompletionSystemMessageParam:`

  Developer-provided instructions that the model should follow, regardless of
  messages sent by the user. With o1 models and newer, use `developer` messages
  for this purpose instead.

  - `Content content`

    The contents of the system message.

    - `String`

    - `List<ChatCompletionContentPartText>`

      - `String text`

        The text content.

      - `JsonValue; type "text"constant`

        The type of the content part.

        - `TEXT("text")`

  - `JsonValue; role "system"constant`

    The role of the messages author, in this case `system`.

    - `SYSTEM("system")`

  - `Optional<String> name`

    An optional name for the participant. Provides the model information to differentiate between participants of the same role.

#### Chat Completion Token Logprob

- `class ChatCompletionTokenLogprob:`

  - `String token`

    The token.

  - `Optional<List<Long>> bytes`

    A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

  - `double logprob`

    The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

  - `List<TopLogprob> topLogprobs`

    List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested `top_logprobs` returned.

    - `String token`

      The token.

    - `Optional<List<Long>> bytes`

      A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

    - `double logprob`

      The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

#### Chat Completion Tool

- `class ChatCompletionTool: A class that can be one of several variants.union`

  A function tool that can be used to generate a response.

  - `class ChatCompletionFunctionTool:`

    A function tool that can be used to generate a response.

    - `FunctionDefinition function`

      - `String name`

        The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

      - `Optional<String> description`

        A description of what the function does, used by the model to choose when and how to call the function.

      - `Optional<FunctionParameters> parameters`

        The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

        Omitting `parameters` defines a function with an empty parameter list.

      - `Optional<Boolean> strict`

        Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

    - `JsonValue; type "function"constant`

      The type of the tool. Currently, only `function` is supported.

      - `FUNCTION("function")`

  - `class ChatCompletionCustomTool:`

    A custom tool that processes input using a specified format.

    - `Custom custom`

      Properties of the custom tool.

      - `String name`

        The name of the custom tool, used to identify it in tool calls.

      - `Optional<String> description`

        Optional description of the custom tool, used to provide more context.

      - `Optional<Format> format`

        The input format for the custom tool. Default is unconstrained text.

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            Unconstrained text format. Always `text`.

            - `TEXT("text")`

        - `class Grammar:`

          A grammar defined by the user.

          - `InnerGrammar grammar`

            Your chosen grammar.

            - `String definition`

              The grammar definition.

            - `Syntax syntax`

              The syntax of the grammar definition. One of `lark` or `regex`.

              - `LARK("lark")`

              - `REGEX("regex")`

          - `JsonValue; type "grammar"constant`

            Grammar format. Always `grammar`.

            - `GRAMMAR("grammar")`

    - `JsonValue; type "custom"constant`

      The type of the custom tool. Always `custom`.

      - `CUSTOM("custom")`

#### Chat Completion Tool Choice Option

- `class ChatCompletionToolChoiceOption: A class that can be one of several variants.union`

  Controls which (if any) tool is called by the model.
  `none` means the model will not call any tool and instead generates a message.
  `auto` means the model can pick between generating a message or calling one or more tools.
  `required` means the model must call one or more tools.
  Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

  `none` is the default when no tools are present. `auto` is the default if tools are present.

  - `Auto`

    - `NONE("none")`

    - `AUTO("auto")`

    - `REQUIRED("required")`

  - `class ChatCompletionAllowedToolChoice:`

    Constrains the tools available to the model to a pre-defined set.

    - `ChatCompletionAllowedTools allowedTools`

      Constrains the tools available to the model to a pre-defined set.

      - `Mode mode`

        Constrains the tools available to the model to a pre-defined set.

        `auto` allows the model to pick from among the allowed tools and generate a
        message.

        `required` requires the model to call one or more of the allowed tools.

        - `AUTO("auto")`

        - `REQUIRED("required")`

      - `List<Tool> tools`

        A list of tool definitions that the model should be allowed to call.

        For the Chat Completions API, the list of tool definitions might look like:

        ```json
        [
          { "type": "function", "function": { "name": "get_weather" } },
          { "type": "function", "function": { "name": "get_time" } }
        ]
        ```

    - `JsonValue; type "allowed_tools"constant`

      Allowed tool configuration type. Always `allowed_tools`.

      - `ALLOWED_TOOLS("allowed_tools")`

  - `class ChatCompletionNamedToolChoice:`

    Specifies a tool the model should use. Use to force the model to call a specific function.

    - `Function function`

      - `String name`

        The name of the function to call.

    - `JsonValue; type "function"constant`

      For function calling, the type is always `function`.

      - `FUNCTION("function")`

  - `class ChatCompletionNamedToolChoiceCustom:`

    Specifies a tool the model should use. Use to force the model to call a specific custom tool.

    - `Custom custom`

      - `String name`

        The name of the custom tool to call.

    - `JsonValue; type "custom"constant`

      For custom tool calling, the type is always `custom`.

      - `CUSTOM("custom")`

#### Chat Completion Tool Message Param

- `class ChatCompletionToolMessageParam:`

  - `Content content`

    The contents of the tool message.

    - `String`

    - `List<ChatCompletionContentPartText>`

      - `String text`

        The text content.

      - `JsonValue; type "text"constant`

        The type of the content part.

        - `TEXT("text")`

  - `JsonValue; role "tool"constant`

    The role of the messages author, in this case `tool`.

    - `TOOL("tool")`

  - `String toolCallId`

    Tool call that this message is responding to.

#### Chat Completion User Message Param

- `class ChatCompletionUserMessageParam:`

  Messages sent by an end user, containing prompts or additional context
  information.

  - `Content content`

    The contents of the user message.

    - `String`

    - `List<ChatCompletionContentPart>`

      - `class ChatCompletionContentPartText:`

        Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

        - `String text`

          The text content.

        - `JsonValue; type "text"constant`

          The type of the content part.

          - `TEXT("text")`

      - `class ChatCompletionContentPartImage:`

        Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

        - `ImageUrl imageUrl`

          - `String url`

            Either a URL of the image or the base64 encoded image data.

          - `Optional<Detail> detail`

            Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

            - `AUTO("auto")`

            - `LOW("low")`

            - `HIGH("high")`

        - `JsonValue; type "image_url"constant`

          The type of the content part.

          - `IMAGE_URL("image_url")`

      - `class ChatCompletionContentPartInputAudio:`

        Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

        - `InputAudio inputAudio`

          - `String data`

            Base64 encoded audio data.

          - `Format format`

            The format of the encoded audio data. Currently supports "wav" and "mp3".

            - `WAV("wav")`

            - `MP3("mp3")`

        - `JsonValue; type "input_audio"constant`

          The type of the content part. Always `input_audio`.

          - `INPUT_AUDIO("input_audio")`

      - `File`

        - `FileObject file`

          - `Optional<String> fileData`

            The base64 encoded file data, used when passing the file to the model
            as a string.

          - `Optional<String> fileId`

            The ID of an uploaded file to use as input.

          - `Optional<String> filename`

            The name of the file, used when passing the file to the model as a
            string.

        - `JsonValue; type "file"constant`

          The type of the content part. Always `file`.

          - `FILE("file")`

  - `JsonValue; role "user"constant`

    The role of the messages author, in this case `user`.

    - `USER("user")`

  - `Optional<String> name`

    An optional name for the participant. Provides the model information to differentiate between participants of the same role.

#### Chat Completion Allowed Tools

- `class ChatCompletionAllowedTools:`

  Constrains the tools available to the model to a pre-defined set.

  - `Mode mode`

    Constrains the tools available to the model to a pre-defined set.

    `auto` allows the model to pick from among the allowed tools and generate a
    message.

    `required` requires the model to call one or more of the allowed tools.

    - `AUTO("auto")`

    - `REQUIRED("required")`

  - `List<Tool> tools`

    A list of tool definitions that the model should be allowed to call.

    For the Chat Completions API, the list of tool definitions might look like:

    ```json
    [
      { "type": "function", "function": { "name": "get_weather" } },
      { "type": "function", "function": { "name": "get_time" } }
    ]
    ```

### Messages

#### List

`MessageListPage chat().completions().messages().list(MessageListParamsparams = MessageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/chat/completions/{completion_id}/messages`

Get the messages in a stored chat completion. Only Chat Completions that
have been created with the `store` parameter set to `true` will be
returned.

##### Parameters

- `MessageListParams params`

  - `Optional<String> completionId`

  - `Optional<String> after`

    Identifier for the last message from the previous pagination request.

  - `Optional<Long> limit`

    Number of messages to retrieve.

  - `Optional<Order> order`

    Sort order for messages by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

    - `ASC("asc")`

    - `DESC("desc")`

##### Returns

- `class ChatCompletionStoreMessage:`

  A chat completion message generated by the model.

  - `String id`

    The identifier of the chat message.

  - `Optional<List<ContentPart>> contentParts`

    If a content parts array was provided, this is an array of `text` and `image_url` parts.
    Otherwise, null.

    - `class ChatCompletionContentPartText:`

      Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

      - `String text`

        The text content.

      - `JsonValue; type "text"constant`

        The type of the content part.

        - `TEXT("text")`

    - `class ChatCompletionContentPartImage:`

      Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

      - `ImageUrl imageUrl`

        - `String url`

          Either a URL of the image or the base64 encoded image data.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.chat.completions.messages.MessageListPage;
import com.openai.models.chat.completions.messages.MessageListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageListPage page = client.chat().completions().messages().list("completion_id");
    }
}
```
