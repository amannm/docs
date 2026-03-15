# Shared

## Domain Types

### All Models

- `type AllModels interface{…}`

  - `string`

  - `type ChatModel string`

    - `const ChatModelGPT5_4 ChatModel = "gpt-5.4"`

    - `const ChatModelGPT5_3ChatLatest ChatModel = "gpt-5.3-chat-latest"`

    - `const ChatModelGPT5_2 ChatModel = "gpt-5.2"`

    - `const ChatModelGPT5_2_2025_12_11 ChatModel = "gpt-5.2-2025-12-11"`

    - `const ChatModelGPT5_2ChatLatest ChatModel = "gpt-5.2-chat-latest"`

    - `const ChatModelGPT5_2Pro ChatModel = "gpt-5.2-pro"`

    - `const ChatModelGPT5_2Pro2025_12_11 ChatModel = "gpt-5.2-pro-2025-12-11"`

    - `const ChatModelGPT5_1 ChatModel = "gpt-5.1"`

    - `const ChatModelGPT5_1_2025_11_13 ChatModel = "gpt-5.1-2025-11-13"`

    - `const ChatModelGPT5_1Codex ChatModel = "gpt-5.1-codex"`

    - `const ChatModelGPT5_1Mini ChatModel = "gpt-5.1-mini"`

    - `const ChatModelGPT5_1ChatLatest ChatModel = "gpt-5.1-chat-latest"`

    - `const ChatModelGPT5 ChatModel = "gpt-5"`

    - `const ChatModelGPT5Mini ChatModel = "gpt-5-mini"`

    - `const ChatModelGPT5Nano ChatModel = "gpt-5-nano"`

    - `const ChatModelGPT5_2025_08_07 ChatModel = "gpt-5-2025-08-07"`

    - `const ChatModelGPT5Mini2025_08_07 ChatModel = "gpt-5-mini-2025-08-07"`

    - `const ChatModelGPT5Nano2025_08_07 ChatModel = "gpt-5-nano-2025-08-07"`

    - `const ChatModelGPT5ChatLatest ChatModel = "gpt-5-chat-latest"`

    - `const ChatModelGPT4_1 ChatModel = "gpt-4.1"`

    - `const ChatModelGPT4_1Mini ChatModel = "gpt-4.1-mini"`

    - `const ChatModelGPT4_1Nano ChatModel = "gpt-4.1-nano"`

    - `const ChatModelGPT4_1_2025_04_14 ChatModel = "gpt-4.1-2025-04-14"`

    - `const ChatModelGPT4_1Mini2025_04_14 ChatModel = "gpt-4.1-mini-2025-04-14"`

    - `const ChatModelGPT4_1Nano2025_04_14 ChatModel = "gpt-4.1-nano-2025-04-14"`

    - `const ChatModelO4Mini ChatModel = "o4-mini"`

    - `const ChatModelO4Mini2025_04_16 ChatModel = "o4-mini-2025-04-16"`

    - `const ChatModelO3 ChatModel = "o3"`

    - `const ChatModelO3_2025_04_16 ChatModel = "o3-2025-04-16"`

    - `const ChatModelO3Mini ChatModel = "o3-mini"`

    - `const ChatModelO3Mini2025_01_31 ChatModel = "o3-mini-2025-01-31"`

    - `const ChatModelO1 ChatModel = "o1"`

    - `const ChatModelO1_2024_12_17 ChatModel = "o1-2024-12-17"`

    - `const ChatModelO1Preview ChatModel = "o1-preview"`

    - `const ChatModelO1Preview2024_09_12 ChatModel = "o1-preview-2024-09-12"`

    - `const ChatModelO1Mini ChatModel = "o1-mini"`

    - `const ChatModelO1Mini2024_09_12 ChatModel = "o1-mini-2024-09-12"`

    - `const ChatModelGPT4o ChatModel = "gpt-4o"`

    - `const ChatModelGPT4o2024_11_20 ChatModel = "gpt-4o-2024-11-20"`

    - `const ChatModelGPT4o2024_08_06 ChatModel = "gpt-4o-2024-08-06"`

    - `const ChatModelGPT4o2024_05_13 ChatModel = "gpt-4o-2024-05-13"`

    - `const ChatModelGPT4oAudioPreview ChatModel = "gpt-4o-audio-preview"`

    - `const ChatModelGPT4oAudioPreview2024_10_01 ChatModel = "gpt-4o-audio-preview-2024-10-01"`

    - `const ChatModelGPT4oAudioPreview2024_12_17 ChatModel = "gpt-4o-audio-preview-2024-12-17"`

    - `const ChatModelGPT4oAudioPreview2025_06_03 ChatModel = "gpt-4o-audio-preview-2025-06-03"`

    - `const ChatModelGPT4oMiniAudioPreview ChatModel = "gpt-4o-mini-audio-preview"`

    - `const ChatModelGPT4oMiniAudioPreview2024_12_17 ChatModel = "gpt-4o-mini-audio-preview-2024-12-17"`

    - `const ChatModelGPT4oSearchPreview ChatModel = "gpt-4o-search-preview"`

    - `const ChatModelGPT4oMiniSearchPreview ChatModel = "gpt-4o-mini-search-preview"`

    - `const ChatModelGPT4oSearchPreview2025_03_11 ChatModel = "gpt-4o-search-preview-2025-03-11"`

    - `const ChatModelGPT4oMiniSearchPreview2025_03_11 ChatModel = "gpt-4o-mini-search-preview-2025-03-11"`

    - `const ChatModelChatgpt4oLatest ChatModel = "chatgpt-4o-latest"`

    - `const ChatModelCodexMiniLatest ChatModel = "codex-mini-latest"`

    - `const ChatModelGPT4oMini ChatModel = "gpt-4o-mini"`

    - `const ChatModelGPT4oMini2024_07_18 ChatModel = "gpt-4o-mini-2024-07-18"`

    - `const ChatModelGPT4Turbo ChatModel = "gpt-4-turbo"`

    - `const ChatModelGPT4Turbo2024_04_09 ChatModel = "gpt-4-turbo-2024-04-09"`

    - `const ChatModelGPT4_0125Preview ChatModel = "gpt-4-0125-preview"`

    - `const ChatModelGPT4TurboPreview ChatModel = "gpt-4-turbo-preview"`

    - `const ChatModelGPT4_1106Preview ChatModel = "gpt-4-1106-preview"`

    - `const ChatModelGPT4VisionPreview ChatModel = "gpt-4-vision-preview"`

    - `const ChatModelGPT4 ChatModel = "gpt-4"`

    - `const ChatModelGPT4_0314 ChatModel = "gpt-4-0314"`

    - `const ChatModelGPT4_0613 ChatModel = "gpt-4-0613"`

    - `const ChatModelGPT4_32k ChatModel = "gpt-4-32k"`

    - `const ChatModelGPT4_32k0314 ChatModel = "gpt-4-32k-0314"`

    - `const ChatModelGPT4_32k0613 ChatModel = "gpt-4-32k-0613"`

    - `const ChatModelGPT3_5Turbo ChatModel = "gpt-3.5-turbo"`

    - `const ChatModelGPT3_5Turbo16k ChatModel = "gpt-3.5-turbo-16k"`

    - `const ChatModelGPT3_5Turbo0301 ChatModel = "gpt-3.5-turbo-0301"`

    - `const ChatModelGPT3_5Turbo0613 ChatModel = "gpt-3.5-turbo-0613"`

    - `const ChatModelGPT3_5Turbo1106 ChatModel = "gpt-3.5-turbo-1106"`

    - `const ChatModelGPT3_5Turbo0125 ChatModel = "gpt-3.5-turbo-0125"`

    - `const ChatModelGPT3_5Turbo16k0613 ChatModel = "gpt-3.5-turbo-16k-0613"`

  - `AllModels`

    - `const AllModelsO1Pro AllModels = "o1-pro"`

    - `const AllModelsO1Pro2025_03_19 AllModels = "o1-pro-2025-03-19"`

    - `const AllModelsO3Pro AllModels = "o3-pro"`

    - `const AllModelsO3Pro2025_06_10 AllModels = "o3-pro-2025-06-10"`

    - `const AllModelsO3DeepResearch AllModels = "o3-deep-research"`

    - `const AllModelsO3DeepResearch2025_06_26 AllModels = "o3-deep-research-2025-06-26"`

    - `const AllModelsO4MiniDeepResearch AllModels = "o4-mini-deep-research"`

    - `const AllModelsO4MiniDeepResearch2025_06_26 AllModels = "o4-mini-deep-research-2025-06-26"`

    - `const AllModelsComputerUsePreview AllModels = "computer-use-preview"`

    - `const AllModelsComputerUsePreview2025_03_11 AllModels = "computer-use-preview-2025-03-11"`

    - `const AllModelsGPT5Codex AllModels = "gpt-5-codex"`

    - `const AllModelsGPT5Pro AllModels = "gpt-5-pro"`

    - `const AllModelsGPT5Pro2025_10_06 AllModels = "gpt-5-pro-2025-10-06"`

    - `const AllModelsGPT5_1CodexMax AllModels = "gpt-5.1-codex-max"`

### Chat Model

- `type ChatModel string`

  - `const ChatModelGPT5_4 ChatModel = "gpt-5.4"`

  - `const ChatModelGPT5_3ChatLatest ChatModel = "gpt-5.3-chat-latest"`

  - `const ChatModelGPT5_2 ChatModel = "gpt-5.2"`

  - `const ChatModelGPT5_2_2025_12_11 ChatModel = "gpt-5.2-2025-12-11"`

  - `const ChatModelGPT5_2ChatLatest ChatModel = "gpt-5.2-chat-latest"`

  - `const ChatModelGPT5_2Pro ChatModel = "gpt-5.2-pro"`

  - `const ChatModelGPT5_2Pro2025_12_11 ChatModel = "gpt-5.2-pro-2025-12-11"`

  - `const ChatModelGPT5_1 ChatModel = "gpt-5.1"`

  - `const ChatModelGPT5_1_2025_11_13 ChatModel = "gpt-5.1-2025-11-13"`

  - `const ChatModelGPT5_1Codex ChatModel = "gpt-5.1-codex"`

  - `const ChatModelGPT5_1Mini ChatModel = "gpt-5.1-mini"`

  - `const ChatModelGPT5_1ChatLatest ChatModel = "gpt-5.1-chat-latest"`

  - `const ChatModelGPT5 ChatModel = "gpt-5"`

  - `const ChatModelGPT5Mini ChatModel = "gpt-5-mini"`

  - `const ChatModelGPT5Nano ChatModel = "gpt-5-nano"`

  - `const ChatModelGPT5_2025_08_07 ChatModel = "gpt-5-2025-08-07"`

  - `const ChatModelGPT5Mini2025_08_07 ChatModel = "gpt-5-mini-2025-08-07"`

  - `const ChatModelGPT5Nano2025_08_07 ChatModel = "gpt-5-nano-2025-08-07"`

  - `const ChatModelGPT5ChatLatest ChatModel = "gpt-5-chat-latest"`

  - `const ChatModelGPT4_1 ChatModel = "gpt-4.1"`

  - `const ChatModelGPT4_1Mini ChatModel = "gpt-4.1-mini"`

  - `const ChatModelGPT4_1Nano ChatModel = "gpt-4.1-nano"`

  - `const ChatModelGPT4_1_2025_04_14 ChatModel = "gpt-4.1-2025-04-14"`

  - `const ChatModelGPT4_1Mini2025_04_14 ChatModel = "gpt-4.1-mini-2025-04-14"`

  - `const ChatModelGPT4_1Nano2025_04_14 ChatModel = "gpt-4.1-nano-2025-04-14"`

  - `const ChatModelO4Mini ChatModel = "o4-mini"`

  - `const ChatModelO4Mini2025_04_16 ChatModel = "o4-mini-2025-04-16"`

  - `const ChatModelO3 ChatModel = "o3"`

  - `const ChatModelO3_2025_04_16 ChatModel = "o3-2025-04-16"`

  - `const ChatModelO3Mini ChatModel = "o3-mini"`

  - `const ChatModelO3Mini2025_01_31 ChatModel = "o3-mini-2025-01-31"`

  - `const ChatModelO1 ChatModel = "o1"`

  - `const ChatModelO1_2024_12_17 ChatModel = "o1-2024-12-17"`

  - `const ChatModelO1Preview ChatModel = "o1-preview"`

  - `const ChatModelO1Preview2024_09_12 ChatModel = "o1-preview-2024-09-12"`

  - `const ChatModelO1Mini ChatModel = "o1-mini"`

  - `const ChatModelO1Mini2024_09_12 ChatModel = "o1-mini-2024-09-12"`

  - `const ChatModelGPT4o ChatModel = "gpt-4o"`

  - `const ChatModelGPT4o2024_11_20 ChatModel = "gpt-4o-2024-11-20"`

  - `const ChatModelGPT4o2024_08_06 ChatModel = "gpt-4o-2024-08-06"`

  - `const ChatModelGPT4o2024_05_13 ChatModel = "gpt-4o-2024-05-13"`

  - `const ChatModelGPT4oAudioPreview ChatModel = "gpt-4o-audio-preview"`

  - `const ChatModelGPT4oAudioPreview2024_10_01 ChatModel = "gpt-4o-audio-preview-2024-10-01"`

  - `const ChatModelGPT4oAudioPreview2024_12_17 ChatModel = "gpt-4o-audio-preview-2024-12-17"`

  - `const ChatModelGPT4oAudioPreview2025_06_03 ChatModel = "gpt-4o-audio-preview-2025-06-03"`

  - `const ChatModelGPT4oMiniAudioPreview ChatModel = "gpt-4o-mini-audio-preview"`

  - `const ChatModelGPT4oMiniAudioPreview2024_12_17 ChatModel = "gpt-4o-mini-audio-preview-2024-12-17"`

  - `const ChatModelGPT4oSearchPreview ChatModel = "gpt-4o-search-preview"`

  - `const ChatModelGPT4oMiniSearchPreview ChatModel = "gpt-4o-mini-search-preview"`

  - `const ChatModelGPT4oSearchPreview2025_03_11 ChatModel = "gpt-4o-search-preview-2025-03-11"`

  - `const ChatModelGPT4oMiniSearchPreview2025_03_11 ChatModel = "gpt-4o-mini-search-preview-2025-03-11"`

  - `const ChatModelChatgpt4oLatest ChatModel = "chatgpt-4o-latest"`

  - `const ChatModelCodexMiniLatest ChatModel = "codex-mini-latest"`

  - `const ChatModelGPT4oMini ChatModel = "gpt-4o-mini"`

  - `const ChatModelGPT4oMini2024_07_18 ChatModel = "gpt-4o-mini-2024-07-18"`

  - `const ChatModelGPT4Turbo ChatModel = "gpt-4-turbo"`

  - `const ChatModelGPT4Turbo2024_04_09 ChatModel = "gpt-4-turbo-2024-04-09"`

  - `const ChatModelGPT4_0125Preview ChatModel = "gpt-4-0125-preview"`

  - `const ChatModelGPT4TurboPreview ChatModel = "gpt-4-turbo-preview"`

  - `const ChatModelGPT4_1106Preview ChatModel = "gpt-4-1106-preview"`

  - `const ChatModelGPT4VisionPreview ChatModel = "gpt-4-vision-preview"`

  - `const ChatModelGPT4 ChatModel = "gpt-4"`

  - `const ChatModelGPT4_0314 ChatModel = "gpt-4-0314"`

  - `const ChatModelGPT4_0613 ChatModel = "gpt-4-0613"`

  - `const ChatModelGPT4_32k ChatModel = "gpt-4-32k"`

  - `const ChatModelGPT4_32k0314 ChatModel = "gpt-4-32k-0314"`

  - `const ChatModelGPT4_32k0613 ChatModel = "gpt-4-32k-0613"`

  - `const ChatModelGPT3_5Turbo ChatModel = "gpt-3.5-turbo"`

  - `const ChatModelGPT3_5Turbo16k ChatModel = "gpt-3.5-turbo-16k"`

  - `const ChatModelGPT3_5Turbo0301 ChatModel = "gpt-3.5-turbo-0301"`

  - `const ChatModelGPT3_5Turbo0613 ChatModel = "gpt-3.5-turbo-0613"`

  - `const ChatModelGPT3_5Turbo1106 ChatModel = "gpt-3.5-turbo-1106"`

  - `const ChatModelGPT3_5Turbo0125 ChatModel = "gpt-3.5-turbo-0125"`

  - `const ChatModelGPT3_5Turbo16k0613 ChatModel = "gpt-3.5-turbo-16k-0613"`

### Comparison Filter

- `type ComparisonFilter struct{…}`

  A filter used to compare a specified attribute key to a given value using a defined comparison operation.

  - `Key string`

    The key to compare against the value.

  - `Type ComparisonFilterType`

    Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    - `in`: in
    - `nin`: not in

    - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

    - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

    - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

    - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

    - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

    - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

  - `Value ComparisonFilterValueUnion`

    The value to compare against the attribute key; supports string, number, or boolean types.

    - `string`

    - `float64`

    - `bool`

    - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

      - `string`

      - `float64`

### Compound Filter

- `type CompoundFilter struct{…}`

  Combine multiple filters using `and` or `or`.

  - `Filters []ComparisonFilter`

    Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

    - `type ComparisonFilter struct{…}`

      A filter used to compare a specified attribute key to a given value using a defined comparison operation.

      - `Key string`

        The key to compare against the value.

      - `Type ComparisonFilterType`

        Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

        - `eq`: equals
        - `ne`: not equal
        - `gt`: greater than
        - `gte`: greater than or equal
        - `lt`: less than
        - `lte`: less than or equal
        - `in`: in
        - `nin`: not in

        - `const ComparisonFilterTypeEq ComparisonFilterType = "eq"`

        - `const ComparisonFilterTypeNe ComparisonFilterType = "ne"`

        - `const ComparisonFilterTypeGt ComparisonFilterType = "gt"`

        - `const ComparisonFilterTypeGte ComparisonFilterType = "gte"`

        - `const ComparisonFilterTypeLt ComparisonFilterType = "lt"`

        - `const ComparisonFilterTypeLte ComparisonFilterType = "lte"`

      - `Value ComparisonFilterValueUnion`

        The value to compare against the attribute key; supports string, number, or boolean types.

        - `string`

        - `float64`

        - `bool`

        - `type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion`

          - `string`

          - `float64`

  - `Type CompoundFilterType`

    Type of operation: `and` or `or`.

    - `const CompoundFilterTypeAnd CompoundFilterType = "and"`

    - `const CompoundFilterTypeOr CompoundFilterType = "or"`

### Custom Tool Input Format

- `type CustomToolInputFormatUnion interface{…}`

  The input format for the custom tool. Default is unconstrained text.

  - `type CustomToolInputFormatText struct{…}`

    Unconstrained free-form text.

    - `Type Text`

      Unconstrained text format. Always `text`.

      - `const TextText Text = "text"`

  - `type CustomToolInputFormatGrammar struct{…}`

    A grammar defined by the user.

    - `Definition string`

      The grammar definition.

    - `Syntax string`

      The syntax of the grammar definition. One of `lark` or `regex`.

      - `const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"`

      - `const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"`

    - `Type Grammar`

      Grammar format. Always `grammar`.

      - `const GrammarGrammar Grammar = "grammar"`

### Error Object

- `type ErrorObject struct{…}`

  - `Code string`

  - `Message string`

  - `Param string`

  - `Type string`

### Function Definition

- `type FunctionDefinition struct{…}`

  - `Name string`

    The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

  - `Description string`

    A description of what the function does, used by the model to choose when and how to call the function.

  - `Parameters FunctionParameters`

    The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.

  - `Strict bool`

    Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

### Function Parameters

- `type FunctionParameters map[string, any]`

  The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

  Omitting `parameters` defines a function with an empty parameter list.

### Metadata

- `type Metadata map[string, string]`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

### Reasoning

- `type Reasoning struct{…}`

  **gpt-5 and o-series models only**

  Configuration options for
  [reasoning models](https://platform.openai.com/docs/guides/reasoning).

  - `Effort ReasoningEffort`

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
    reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.

    - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
    - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
    - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
    - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

    - `const ReasoningEffortNone ReasoningEffort = "none"`

    - `const ReasoningEffortMinimal ReasoningEffort = "minimal"`

    - `const ReasoningEffortLow ReasoningEffort = "low"`

    - `const ReasoningEffortMedium ReasoningEffort = "medium"`

    - `const ReasoningEffortHigh ReasoningEffort = "high"`

    - `const ReasoningEffortXhigh ReasoningEffort = "xhigh"`

  - `GenerateSummary ReasoningGenerateSummary`

    **Deprecated:** use `summary` instead.

    A summary of the reasoning performed by the model. This can be
    useful for debugging and understanding the model's reasoning process.
    One of `auto`, `concise`, or `detailed`.

    - `const ReasoningGenerateSummaryAuto ReasoningGenerateSummary = "auto"`

    - `const ReasoningGenerateSummaryConcise ReasoningGenerateSummary = "concise"`

    - `const ReasoningGenerateSummaryDetailed ReasoningGenerateSummary = "detailed"`

  - `Summary ReasoningSummary`

    A summary of the reasoning performed by the model. This can be
    useful for debugging and understanding the model's reasoning process.
    One of `auto`, `concise`, or `detailed`.

    `concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

    - `const ReasoningSummaryAuto ReasoningSummary = "auto"`

    - `const ReasoningSummaryConcise ReasoningSummary = "concise"`

    - `const ReasoningSummaryDetailed ReasoningSummary = "detailed"`

### Reasoning Effort

- `type ReasoningEffort string`

  Constrains effort on reasoning for
  [reasoning models](https://platform.openai.com/docs/guides/reasoning).
  Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
  reasoning effort can result in faster responses and fewer tokens used
  on reasoning in a response.

  - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
  - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
  - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
  - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

  - `const ReasoningEffortNone ReasoningEffort = "none"`

  - `const ReasoningEffortMinimal ReasoningEffort = "minimal"`

  - `const ReasoningEffortLow ReasoningEffort = "low"`

  - `const ReasoningEffortMedium ReasoningEffort = "medium"`

  - `const ReasoningEffortHigh ReasoningEffort = "high"`

  - `const ReasoningEffortXhigh ReasoningEffort = "xhigh"`

### Response Format JSON Object

- `type ResponseFormatJSONObject struct{…}`

  JSON object response format. An older method of generating JSON responses.
  Using `json_schema` is recommended for models that support it. Note that the
  model will not generate JSON without a system or user message instructing it
  to do so.

  - `Type JSONObject`

    The type of response format being defined. Always `json_object`.

    - `const JSONObjectJSONObject JSONObject = "json_object"`

### Response Format JSON Schema

- `type ResponseFormatJSONSchema struct{…}`

  JSON Schema response format. Used to generate structured JSON responses.
  Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

  - `JSONSchema ResponseFormatJSONSchemaJSONSchema`

    Structured Outputs configuration options, including a JSON Schema.

    - `Name string`

      The name of the response format. Must be a-z, A-Z, 0-9, or contain
      underscores and dashes, with a maximum length of 64.

    - `Description string`

      A description of what the response format is for, used by the model to
      determine how to respond in the format.

    - `Schema map[string, any]`

      The schema for the response format, described as a JSON Schema object.
      Learn how to build JSON schemas [here](https://json-schema.org/).

    - `Strict bool`

      Whether to enable strict schema adherence when generating the output.
      If set to true, the model will always follow the exact schema defined
      in the `schema` field. Only a subset of JSON Schema is supported when
      `strict` is `true`. To learn more, read the [Structured Outputs
      guide](https://platform.openai.com/docs/guides/structured-outputs).

  - `Type JSONSchema`

    The type of response format being defined. Always `json_schema`.

    - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

### Response Format Text

- `type ResponseFormatText struct{…}`

  Default response format. Used to generate text responses.

  - `Type Text`

    The type of response format being defined. Always `text`.

    - `const TextText Text = "text"`

### Response Format Text Grammar

- `type ResponseFormatTextGrammar struct{…}`

  A custom grammar for the model to follow when generating text.
  Learn more in the [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars).

  - `Grammar string`

    The custom grammar for the model to follow.

  - `Type Grammar`

    The type of response format being defined. Always `grammar`.

    - `const GrammarGrammar Grammar = "grammar"`

### Response Format Text Python

- `type ResponseFormatTextPython struct{…}`

  Configure the model to generate valid Python code. See the
  [custom grammars guide](https://platform.openai.com/docs/guides/custom-grammars) for more details.

  - `Type Python`

    The type of response format being defined. Always `python`.

    - `const PythonPython Python = "python"`

### Responses Model

- `type ResponsesModel interface{…}`

  - `string`

  - `type ChatModel string`

    - `const ChatModelGPT5_4 ChatModel = "gpt-5.4"`

    - `const ChatModelGPT5_3ChatLatest ChatModel = "gpt-5.3-chat-latest"`

    - `const ChatModelGPT5_2 ChatModel = "gpt-5.2"`

    - `const ChatModelGPT5_2_2025_12_11 ChatModel = "gpt-5.2-2025-12-11"`

    - `const ChatModelGPT5_2ChatLatest ChatModel = "gpt-5.2-chat-latest"`

    - `const ChatModelGPT5_2Pro ChatModel = "gpt-5.2-pro"`

    - `const ChatModelGPT5_2Pro2025_12_11 ChatModel = "gpt-5.2-pro-2025-12-11"`

    - `const ChatModelGPT5_1 ChatModel = "gpt-5.1"`

    - `const ChatModelGPT5_1_2025_11_13 ChatModel = "gpt-5.1-2025-11-13"`

    - `const ChatModelGPT5_1Codex ChatModel = "gpt-5.1-codex"`

    - `const ChatModelGPT5_1Mini ChatModel = "gpt-5.1-mini"`

    - `const ChatModelGPT5_1ChatLatest ChatModel = "gpt-5.1-chat-latest"`

    - `const ChatModelGPT5 ChatModel = "gpt-5"`

    - `const ChatModelGPT5Mini ChatModel = "gpt-5-mini"`

    - `const ChatModelGPT5Nano ChatModel = "gpt-5-nano"`

    - `const ChatModelGPT5_2025_08_07 ChatModel = "gpt-5-2025-08-07"`

    - `const ChatModelGPT5Mini2025_08_07 ChatModel = "gpt-5-mini-2025-08-07"`

    - `const ChatModelGPT5Nano2025_08_07 ChatModel = "gpt-5-nano-2025-08-07"`

    - `const ChatModelGPT5ChatLatest ChatModel = "gpt-5-chat-latest"`

    - `const ChatModelGPT4_1 ChatModel = "gpt-4.1"`

    - `const ChatModelGPT4_1Mini ChatModel = "gpt-4.1-mini"`

    - `const ChatModelGPT4_1Nano ChatModel = "gpt-4.1-nano"`

    - `const ChatModelGPT4_1_2025_04_14 ChatModel = "gpt-4.1-2025-04-14"`

    - `const ChatModelGPT4_1Mini2025_04_14 ChatModel = "gpt-4.1-mini-2025-04-14"`

    - `const ChatModelGPT4_1Nano2025_04_14 ChatModel = "gpt-4.1-nano-2025-04-14"`

    - `const ChatModelO4Mini ChatModel = "o4-mini"`

    - `const ChatModelO4Mini2025_04_16 ChatModel = "o4-mini-2025-04-16"`

    - `const ChatModelO3 ChatModel = "o3"`

    - `const ChatModelO3_2025_04_16 ChatModel = "o3-2025-04-16"`

    - `const ChatModelO3Mini ChatModel = "o3-mini"`

    - `const ChatModelO3Mini2025_01_31 ChatModel = "o3-mini-2025-01-31"`

    - `const ChatModelO1 ChatModel = "o1"`

    - `const ChatModelO1_2024_12_17 ChatModel = "o1-2024-12-17"`

    - `const ChatModelO1Preview ChatModel = "o1-preview"`

    - `const ChatModelO1Preview2024_09_12 ChatModel = "o1-preview-2024-09-12"`

    - `const ChatModelO1Mini ChatModel = "o1-mini"`

    - `const ChatModelO1Mini2024_09_12 ChatModel = "o1-mini-2024-09-12"`

    - `const ChatModelGPT4o ChatModel = "gpt-4o"`

    - `const ChatModelGPT4o2024_11_20 ChatModel = "gpt-4o-2024-11-20"`

    - `const ChatModelGPT4o2024_08_06 ChatModel = "gpt-4o-2024-08-06"`

    - `const ChatModelGPT4o2024_05_13 ChatModel = "gpt-4o-2024-05-13"`

    - `const ChatModelGPT4oAudioPreview ChatModel = "gpt-4o-audio-preview"`

    - `const ChatModelGPT4oAudioPreview2024_10_01 ChatModel = "gpt-4o-audio-preview-2024-10-01"`

    - `const ChatModelGPT4oAudioPreview2024_12_17 ChatModel = "gpt-4o-audio-preview-2024-12-17"`

    - `const ChatModelGPT4oAudioPreview2025_06_03 ChatModel = "gpt-4o-audio-preview-2025-06-03"`

    - `const ChatModelGPT4oMiniAudioPreview ChatModel = "gpt-4o-mini-audio-preview"`

    - `const ChatModelGPT4oMiniAudioPreview2024_12_17 ChatModel = "gpt-4o-mini-audio-preview-2024-12-17"`

    - `const ChatModelGPT4oSearchPreview ChatModel = "gpt-4o-search-preview"`

    - `const ChatModelGPT4oMiniSearchPreview ChatModel = "gpt-4o-mini-search-preview"`

    - `const ChatModelGPT4oSearchPreview2025_03_11 ChatModel = "gpt-4o-search-preview-2025-03-11"`

    - `const ChatModelGPT4oMiniSearchPreview2025_03_11 ChatModel = "gpt-4o-mini-search-preview-2025-03-11"`

    - `const ChatModelChatgpt4oLatest ChatModel = "chatgpt-4o-latest"`

    - `const ChatModelCodexMiniLatest ChatModel = "codex-mini-latest"`

    - `const ChatModelGPT4oMini ChatModel = "gpt-4o-mini"`

    - `const ChatModelGPT4oMini2024_07_18 ChatModel = "gpt-4o-mini-2024-07-18"`

    - `const ChatModelGPT4Turbo ChatModel = "gpt-4-turbo"`

    - `const ChatModelGPT4Turbo2024_04_09 ChatModel = "gpt-4-turbo-2024-04-09"`

    - `const ChatModelGPT4_0125Preview ChatModel = "gpt-4-0125-preview"`

    - `const ChatModelGPT4TurboPreview ChatModel = "gpt-4-turbo-preview"`

    - `const ChatModelGPT4_1106Preview ChatModel = "gpt-4-1106-preview"`

    - `const ChatModelGPT4VisionPreview ChatModel = "gpt-4-vision-preview"`

    - `const ChatModelGPT4 ChatModel = "gpt-4"`

    - `const ChatModelGPT4_0314 ChatModel = "gpt-4-0314"`

    - `const ChatModelGPT4_0613 ChatModel = "gpt-4-0613"`

    - `const ChatModelGPT4_32k ChatModel = "gpt-4-32k"`

    - `const ChatModelGPT4_32k0314 ChatModel = "gpt-4-32k-0314"`

    - `const ChatModelGPT4_32k0613 ChatModel = "gpt-4-32k-0613"`

    - `const ChatModelGPT3_5Turbo ChatModel = "gpt-3.5-turbo"`

    - `const ChatModelGPT3_5Turbo16k ChatModel = "gpt-3.5-turbo-16k"`

    - `const ChatModelGPT3_5Turbo0301 ChatModel = "gpt-3.5-turbo-0301"`

    - `const ChatModelGPT3_5Turbo0613 ChatModel = "gpt-3.5-turbo-0613"`

    - `const ChatModelGPT3_5Turbo1106 ChatModel = "gpt-3.5-turbo-1106"`

    - `const ChatModelGPT3_5Turbo0125 ChatModel = "gpt-3.5-turbo-0125"`

    - `const ChatModelGPT3_5Turbo16k0613 ChatModel = "gpt-3.5-turbo-16k-0613"`

  - `type ResponsesModel string`

    - `const ResponsesModelO1Pro ResponsesModel = "o1-pro"`

    - `const ResponsesModelO1Pro2025_03_19 ResponsesModel = "o1-pro-2025-03-19"`

    - `const ResponsesModelO3Pro ResponsesModel = "o3-pro"`

    - `const ResponsesModelO3Pro2025_06_10 ResponsesModel = "o3-pro-2025-06-10"`

    - `const ResponsesModelO3DeepResearch ResponsesModel = "o3-deep-research"`

    - `const ResponsesModelO3DeepResearch2025_06_26 ResponsesModel = "o3-deep-research-2025-06-26"`

    - `const ResponsesModelO4MiniDeepResearch ResponsesModel = "o4-mini-deep-research"`

    - `const ResponsesModelO4MiniDeepResearch2025_06_26 ResponsesModel = "o4-mini-deep-research-2025-06-26"`

    - `const ResponsesModelComputerUsePreview ResponsesModel = "computer-use-preview"`

    - `const ResponsesModelComputerUsePreview2025_03_11 ResponsesModel = "computer-use-preview-2025-03-11"`

    - `const ResponsesModelGPT5Codex ResponsesModel = "gpt-5-codex"`

    - `const ResponsesModelGPT5Pro ResponsesModel = "gpt-5-pro"`

    - `const ResponsesModelGPT5Pro2025_10_06 ResponsesModel = "gpt-5-pro-2025-10-06"`

    - `const ResponsesModelGPT5_1CodexMax ResponsesModel = "gpt-5.1-codex-max"`