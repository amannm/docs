# Shared

## Domain Types

### All Models

- `AllModels = string or "gpt-5.4" or "gpt-5.3-chat-latest" or "gpt-5.2" or 71 more or "o1-pro" or "o1-pro-2025-03-19" or "o3-pro" or 11 more`

  - `UnionMember0 = string`

  - `UnionMember1 = "gpt-5.4" or "gpt-5.3-chat-latest" or "gpt-5.2" or 71 more`

    - `"gpt-5.4"`

    - `"gpt-5.3-chat-latest"`

    - `"gpt-5.2"`

    - `"gpt-5.2-2025-12-11"`

    - `"gpt-5.2-chat-latest"`

    - `"gpt-5.2-pro"`

    - `"gpt-5.2-pro-2025-12-11"`

    - `"gpt-5.1"`

    - `"gpt-5.1-2025-11-13"`

    - `"gpt-5.1-codex"`

    - `"gpt-5.1-mini"`

    - `"gpt-5.1-chat-latest"`

    - `"gpt-5"`

    - `"gpt-5-mini"`

    - `"gpt-5-nano"`

    - `"gpt-5-2025-08-07"`

    - `"gpt-5-mini-2025-08-07"`

    - `"gpt-5-nano-2025-08-07"`

    - `"gpt-5-chat-latest"`

    - `"gpt-4.1"`

    - `"gpt-4.1-mini"`

    - `"gpt-4.1-nano"`

    - `"gpt-4.1-2025-04-14"`

    - `"gpt-4.1-mini-2025-04-14"`

    - `"gpt-4.1-nano-2025-04-14"`

    - `"o4-mini"`

    - `"o4-mini-2025-04-16"`

    - `"o3"`

    - `"o3-2025-04-16"`

    - `"o3-mini"`

    - `"o3-mini-2025-01-31"`

    - `"o1"`

    - `"o1-2024-12-17"`

    - `"o1-preview"`

    - `"o1-preview-2024-09-12"`

    - `"o1-mini"`

    - `"o1-mini-2024-09-12"`

    - `"gpt-4o"`

    - `"gpt-4o-2024-11-20"`

    - `"gpt-4o-2024-08-06"`

    - `"gpt-4o-2024-05-13"`

    - `"gpt-4o-audio-preview"`

    - `"gpt-4o-audio-preview-2024-10-01"`

    - `"gpt-4o-audio-preview-2024-12-17"`

    - `"gpt-4o-audio-preview-2025-06-03"`

    - `"gpt-4o-mini-audio-preview"`

    - `"gpt-4o-mini-audio-preview-2024-12-17"`

    - `"gpt-4o-search-preview"`

    - `"gpt-4o-mini-search-preview"`

    - `"gpt-4o-search-preview-2025-03-11"`

    - `"gpt-4o-mini-search-preview-2025-03-11"`

    - `"chatgpt-4o-latest"`

    - `"codex-mini-latest"`

    - `"gpt-4o-mini"`

    - `"gpt-4o-mini-2024-07-18"`

    - `"gpt-4-turbo"`

    - `"gpt-4-turbo-2024-04-09"`

    - `"gpt-4-0125-preview"`

    - `"gpt-4-turbo-preview"`

    - `"gpt-4-1106-preview"`

    - `"gpt-4-vision-preview"`

    - `"gpt-4"`

    - `"gpt-4-0314"`

    - `"gpt-4-0613"`

    - `"gpt-4-32k"`

    - `"gpt-4-32k-0314"`

    - `"gpt-4-32k-0613"`

    - `"gpt-3.5-turbo"`

    - `"gpt-3.5-turbo-16k"`

    - `"gpt-3.5-turbo-0301"`

    - `"gpt-3.5-turbo-0613"`

    - `"gpt-3.5-turbo-1106"`

    - `"gpt-3.5-turbo-0125"`

    - `"gpt-3.5-turbo-16k-0613"`

  - `ResponsesOnlyModel = "o1-pro" or "o1-pro-2025-03-19" or "o3-pro" or 11 more`

    - `"o1-pro"`

    - `"o1-pro-2025-03-19"`

    - `"o3-pro"`

    - `"o3-pro-2025-06-10"`

    - `"o3-deep-research"`

    - `"o3-deep-research-2025-06-26"`

    - `"o4-mini-deep-research"`

    - `"o4-mini-deep-research-2025-06-26"`

    - `"computer-use-preview"`

    - `"computer-use-preview-2025-03-11"`

    - `"gpt-5-codex"`

    - `"gpt-5-pro"`

    - `"gpt-5-pro-2025-10-06"`

    - `"gpt-5.1-codex-max"`

### Comparison Filter

- `ComparisonFilter = object { key, type, value }`

  A filter used to compare a specified attribute key to a given value using a defined comparison operation.

  - `key: string`

    The key to compare against the value.

  - `type: "eq" or "ne" or "gt" or 3 more`

    Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    - `in`: in
    - `nin`: not in

    - `"eq"`

    - `"ne"`

    - `"gt"`

    - `"gte"`

    - `"lt"`

    - `"lte"`

  - `value: string or number or boolean or array of string or number`

    The value to compare against the attribute key; supports string, number, or boolean types.

    - `UnionMember0 = string`

    - `UnionMember1 = number`

    - `UnionMember2 = boolean`

    - `UnionMember3 = array of string or number`

      - `UnionMember0 = string`

      - `UnionMember1 = number`

### Compound Filter

- `CompoundFilter = object { filters, type }`

  Combine multiple filters using `and` or `or`.

  - `filters: array of ComparisonFilter or unknown`

    Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

    - `ComparisonFilter = object { key, type, value }`

      A filter used to compare a specified attribute key to a given value using a defined comparison operation.

      - `key: string`

        The key to compare against the value.

      - `type: "eq" or "ne" or "gt" or 3 more`

        Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

        - `eq`: equals
        - `ne`: not equal
        - `gt`: greater than
        - `gte`: greater than or equal
        - `lt`: less than
        - `lte`: less than or equal
        - `in`: in
        - `nin`: not in

        - `"eq"`

        - `"ne"`

        - `"gt"`

        - `"gte"`

        - `"lt"`

        - `"lte"`

      - `value: string or number or boolean or array of string or number`

        The value to compare against the attribute key; supports string, number, or boolean types.

        - `UnionMember0 = string`

        - `UnionMember1 = number`

        - `UnionMember2 = boolean`

        - `UnionMember3 = array of string or number`

          - `UnionMember0 = string`

          - `UnionMember1 = number`

    - `UnionMember1 = unknown`

  - `type: "and" or "or"`

    Type of operation: `and` or `or`.

    - `"and"`

    - `"or"`

### Custom Tool Input Format

- `CustomToolInputFormat = object { type }  or object { definition, syntax, type }`

  The input format for the custom tool. Default is unconstrained text.

  - `Text = object { type }`

    Unconstrained free-form text.

    - `type: "text"`

      Unconstrained text format. Always `text`.

      - `"text"`

  - `Grammar = object { definition, syntax, type }`

    A grammar defined by the user.

    - `definition: string`

      The grammar definition.

    - `syntax: "lark" or "regex"`

      The syntax of the grammar definition. One of `lark` or `regex`.

      - `"lark"`

      - `"regex"`

    - `type: "grammar"`

      Grammar format. Always `grammar`.

      - `"grammar"`

### Error Object

- `ErrorObject = object { code, message, param, type }`

  - `code: string`

  - `message: string`

  - `param: string`

  - `type: string`

### Function Definition

- `FunctionDefinition = object { name, description, parameters, strict }`

  - `name: string`

    The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

  - `description: optional string`

    A description of what the function does, used by the model to choose when and how to call the function.

  - `parameters: optional FunctionParameters`

    The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

    Omitting `parameters` defines a function with an empty parameter list.

  - `strict: optional boolean`

    Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://developers.openai.com/docs/guides/function-calling).

### Function Parameters

- `FunctionParameters = map[unknown]`

  The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://developers.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

  Omitting `parameters` defines a function with an empty parameter list.

### Metadata

- `Metadata = map[string]`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

### Reasoning

- `Reasoning = object { effort, generate_summary, summary }`

  **gpt-5 and o-series models only**

  Configuration options for
  [reasoning models](https://platform.openai.com/docs/guides/reasoning).

  - `effort: optional ReasoningEffort`

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
    reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.

    - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
    - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
    - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
    - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

    - `"none"`

    - `"minimal"`

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

  - `generate_summary: optional "auto" or "concise" or "detailed"`

    **Deprecated:** use `summary` instead.

    A summary of the reasoning performed by the model. This can be
    useful for debugging and understanding the model's reasoning process.
    One of `auto`, `concise`, or `detailed`.

    - `"auto"`

    - `"concise"`

    - `"detailed"`

  - `summary: optional "auto" or "concise" or "detailed"`

    A summary of the reasoning performed by the model. This can be
    useful for debugging and understanding the model's reasoning process.
    One of `auto`, `concise`, or `detailed`.

    `concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

    - `"auto"`

    - `"concise"`

    - `"detailed"`

### Reasoning Effort

- `ReasoningEffort = "none" or "minimal" or "low" or 3 more`

  Constrains effort on reasoning for
  [reasoning models](https://platform.openai.com/docs/guides/reasoning).
  Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
  reasoning effort can result in faster responses and fewer tokens used
  on reasoning in a response.

  - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
  - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
  - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
  - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

  - `"none"`

  - `"minimal"`

  - `"low"`

  - `"medium"`

  - `"high"`

  - `"xhigh"`

### Response Format JSON Object

- `ResponseFormatJSONObject = object { type }`

  JSON object response format. An older method of generating JSON responses.
  Using `json_schema` is recommended for models that support it. Note that the
  model will not generate JSON without a system or user message instructing it
  to do so.

  - `type: "json_object"`

    The type of response format being defined. Always `json_object`.

    - `"json_object"`

### Response Format JSON Schema

- `ResponseFormatJSONSchema = object { json_schema, type }`

  JSON Schema response format. Used to generate structured JSON responses.
  Learn more about [Structured Outputs](https://developers.openai.com/docs/guides/structured-outputs).

  - `json_schema: object { name, description, schema, strict }`

    Structured Outputs configuration options, including a JSON Schema.

    - `name: string`

      The name of the response format. Must be a-z, A-Z, 0-9, or contain
      underscores and dashes, with a maximum length of 64.

    - `description: optional string`

      A description of what the response format is for, used by the model to
      determine how to respond in the format.

    - `schema: optional map[unknown]`

      The schema for the response format, described as a JSON Schema object.
      Learn how to build JSON schemas [here](https://json-schema.org/).

    - `strict: optional boolean`

      Whether to enable strict schema adherence when generating the output.
      If set to true, the model will always follow the exact schema defined
      in the `schema` field. Only a subset of JSON Schema is supported when
      `strict` is `true`. To learn more, read the [Structured Outputs
      guide](https://developers.openai.com/docs/guides/structured-outputs).

  - `type: "json_schema"`

    The type of response format being defined. Always `json_schema`.

    - `"json_schema"`

### Response Format Text

- `ResponseFormatText = object { type }`

  Default response format. Used to generate text responses.

  - `type: "text"`

    The type of response format being defined. Always `text`.

    - `"text"`

### Response Format Text Grammar

- `ResponseFormatTextGrammar = object { grammar, type }`

  A custom grammar for the model to follow when generating text.
  Learn more in the [custom grammars guide](https://developers.openai.com/docs/guides/custom-grammars).

  - `grammar: string`

    The custom grammar for the model to follow.

  - `type: "grammar"`

    The type of response format being defined. Always `grammar`.

    - `"grammar"`

### Response Format Text Python

- `ResponseFormatTextPython = object { type }`

  Configure the model to generate valid Python code. See the
  [custom grammars guide](https://developers.openai.com/docs/guides/custom-grammars) for more details.

  - `type: "python"`

    The type of response format being defined. Always `python`.

    - `"python"`

### Responses Model

- `ResponsesModel = string or "gpt-5.4" or "gpt-5.3-chat-latest" or "gpt-5.2" or 71 more or "o1-pro" or "o1-pro-2025-03-19" or "o3-pro" or 11 more`

  - `UnionMember0 = string`

  - `UnionMember1 = "gpt-5.4" or "gpt-5.3-chat-latest" or "gpt-5.2" or 71 more`

    - `"gpt-5.4"`

    - `"gpt-5.3-chat-latest"`

    - `"gpt-5.2"`

    - `"gpt-5.2-2025-12-11"`

    - `"gpt-5.2-chat-latest"`

    - `"gpt-5.2-pro"`

    - `"gpt-5.2-pro-2025-12-11"`

    - `"gpt-5.1"`

    - `"gpt-5.1-2025-11-13"`

    - `"gpt-5.1-codex"`

    - `"gpt-5.1-mini"`

    - `"gpt-5.1-chat-latest"`

    - `"gpt-5"`

    - `"gpt-5-mini"`

    - `"gpt-5-nano"`

    - `"gpt-5-2025-08-07"`

    - `"gpt-5-mini-2025-08-07"`

    - `"gpt-5-nano-2025-08-07"`

    - `"gpt-5-chat-latest"`

    - `"gpt-4.1"`

    - `"gpt-4.1-mini"`

    - `"gpt-4.1-nano"`

    - `"gpt-4.1-2025-04-14"`

    - `"gpt-4.1-mini-2025-04-14"`

    - `"gpt-4.1-nano-2025-04-14"`

    - `"o4-mini"`

    - `"o4-mini-2025-04-16"`

    - `"o3"`

    - `"o3-2025-04-16"`

    - `"o3-mini"`

    - `"o3-mini-2025-01-31"`

    - `"o1"`

    - `"o1-2024-12-17"`

    - `"o1-preview"`

    - `"o1-preview-2024-09-12"`

    - `"o1-mini"`

    - `"o1-mini-2024-09-12"`

    - `"gpt-4o"`

    - `"gpt-4o-2024-11-20"`

    - `"gpt-4o-2024-08-06"`

    - `"gpt-4o-2024-05-13"`

    - `"gpt-4o-audio-preview"`

    - `"gpt-4o-audio-preview-2024-10-01"`

    - `"gpt-4o-audio-preview-2024-12-17"`

    - `"gpt-4o-audio-preview-2025-06-03"`

    - `"gpt-4o-mini-audio-preview"`

    - `"gpt-4o-mini-audio-preview-2024-12-17"`

    - `"gpt-4o-search-preview"`

    - `"gpt-4o-mini-search-preview"`

    - `"gpt-4o-search-preview-2025-03-11"`

    - `"gpt-4o-mini-search-preview-2025-03-11"`

    - `"chatgpt-4o-latest"`

    - `"codex-mini-latest"`

    - `"gpt-4o-mini"`

    - `"gpt-4o-mini-2024-07-18"`

    - `"gpt-4-turbo"`

    - `"gpt-4-turbo-2024-04-09"`

    - `"gpt-4-0125-preview"`

    - `"gpt-4-turbo-preview"`

    - `"gpt-4-1106-preview"`

    - `"gpt-4-vision-preview"`

    - `"gpt-4"`

    - `"gpt-4-0314"`

    - `"gpt-4-0613"`

    - `"gpt-4-32k"`

    - `"gpt-4-32k-0314"`

    - `"gpt-4-32k-0613"`

    - `"gpt-3.5-turbo"`

    - `"gpt-3.5-turbo-16k"`

    - `"gpt-3.5-turbo-0301"`

    - `"gpt-3.5-turbo-0613"`

    - `"gpt-3.5-turbo-1106"`

    - `"gpt-3.5-turbo-0125"`

    - `"gpt-3.5-turbo-16k-0613"`

  - `ResponsesOnlyModel = "o1-pro" or "o1-pro-2025-03-19" or "o3-pro" or 11 more`

    - `"o1-pro"`

    - `"o1-pro-2025-03-19"`

    - `"o3-pro"`

    - `"o3-pro-2025-06-10"`

    - `"o3-deep-research"`

    - `"o3-deep-research-2025-06-26"`

    - `"o4-mini-deep-research"`

    - `"o4-mini-deep-research-2025-06-26"`

    - `"computer-use-preview"`

    - `"computer-use-preview-2025-03-11"`

    - `"gpt-5-codex"`

    - `"gpt-5-pro"`

    - `"gpt-5-pro-2025-10-06"`

    - `"gpt-5.1-codex-max"`