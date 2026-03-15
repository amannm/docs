# Evals

## List

`evals.list(**kwargs) -> CursorPage<EvalListResponse>`

**get** `/evals`

List evaluations for a project.

### Parameters

- `after: String`

  Identifier for the last eval from the previous pagination request.

- `limit: Integer`

  Number of evals to retrieve.

- `order: :asc | :desc`

  Sort order for evals by timestamp. Use `asc` for ascending order or `desc` for descending order.

  - `:asc`

  - `:desc`

- `order_by: :created_at | :updated_at`

  Evals can be ordered by creation time or last updated time. Use
  `created_at` for creation time or `updated_at` for last updated time.

  - `:created_at`

  - `:updated_at`

### Returns

- `class EvalListResponse`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `id: String`

    Unique identifier for the evaluation.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the eval was created.

  - `data_source_config: EvalCustomDataSourceConfig | { schema, type, metadata} | EvalStoredCompletionsDataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :custom`

        The type of data source. Always `custom`.

        - `:custom`

    - `class Logs`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :logs`

        The type of data source. Always `logs`.

        - `:logs`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig`

      Deprecated in favor of LogsDataSourceConfig.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :stored_completions`

        The type of data source. Always `stored_completions`.

        - `:stored_completions`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the evaluation.

  - `object: :eval`

    The object type.

    - `:eval`

  - `testing_criteria: Array[LabelModelGrader | StringCheckGrader | TextSimilarityGrader & { pass_threshold} | 2 more]`

    A list of testing criteria.

    - `class LabelModelGrader`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `input: Array[{ content, role, type}]`

        - `content: String | ResponseInputText | { text, type} | 3 more`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

            A text input to the model.

          - `class ResponseInputText`

            A text input to the model.

            - `text: String`

              The text input to the model.

            - `type: :input_text`

              The type of the input item. Always `input_text`.

              - `:input_text`

          - `class OutputText`

            A text output from the model.

            - `text: String`

              The text output from the model.

            - `type: :output_text`

              The type of the output text. Always `output_text`.

              - `:output_text`

          - `class InputImage`

            An image input block used within EvalItem content arrays.

            - `image_url: String`

              The URL of the image input.

            - `type: :input_image`

              The type of the image input. Always `input_image`.

              - `:input_image`

            - `detail: String`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio`

            An audio input to the model.

            - `input_audio: { data, format_}`

              - `data: String`

                Base64-encoded audio data.

              - `format_: :mp3 | :wav`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `:mp3`

                - `:wav`

            - `type: :input_audio`

              The type of the input item. Always `input_audio`.

              - `:input_audio`

          - `Array[GraderInputItem]`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `String`

              A text input to the model.

            - `class ResponseInputText`

              A text input to the model.

              - `text: String`

                The text input to the model.

              - `type: :input_text`

                The type of the input item. Always `input_text`.

                - `:input_text`

            - `class OutputText`

              A text output from the model.

              - `text: String`

                The text output from the model.

              - `type: :output_text`

                The type of the output text. Always `output_text`.

                - `:output_text`

            - `class InputImage`

              An image input block used within EvalItem content arrays.

              - `image_url: String`

                The URL of the image input.

              - `type: :input_image`

                The type of the image input. Always `input_image`.

                - `:input_image`

              - `detail: String`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio`

              An audio input to the model.

              - `input_audio: { data, format_}`

                - `data: String`

                  Base64-encoded audio data.

                - `format_: :mp3 | :wav`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `:mp3`

                  - `:wav`

              - `type: :input_audio`

                The type of the input item. Always `input_audio`.

                - `:input_audio`

        - `role: :user | :assistant | :system | :developer`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `:user`

          - `:assistant`

          - `:system`

          - `:developer`

        - `type: :message`

          The type of the message input. Always `message`.

          - `:message`

      - `labels: Array[String]`

        The labels to assign to each item in the evaluation.

      - `model: String`

        The model to use for the evaluation. Must support structured outputs.

      - `name: String`

        The name of the grader.

      - `passing_labels: Array[String]`

        The labels that indicate a passing result. Must be a subset of labels.

      - `type: :label_model`

        The object type, which is always `label_model`.

        - `:label_model`

    - `class StringCheckGrader`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `input: String`

        The input text. This may include template strings.

      - `name: String`

        The name of the grader.

      - `operation: :eq | :ne | :like | :ilike`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `:eq`

        - `:ne`

        - `:like`

        - `:ilike`

      - `reference: String`

        The reference text. This may include template strings.

      - `type: :string_check`

        The object type, which is always `string_check`.

        - `:string_check`

    - `class EvalGraderTextSimilarity`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderPython`

      A PythonGrader object that runs a python script on the input.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderScoreModel`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `pass_threshold: Float`

        The threshold for the score.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.evals.list

puts(page)
```

## Create

`evals.create(**kwargs) -> EvalCreateResponse`

**post** `/evals`

Create the structure of an evaluation that can be used to test a model's performance.
An evaluation is a set of testing criteria and the config for a data source, which dictates the schema of the data used in the evaluation. After creating an evaluation, you can run it on different models and model parameters. We support several types of graders and datasources.
For more information, see the [Evals guide](https://platform.openai.com/docs/guides/evals).

### Parameters

- `data_source_config: { item_schema, type, include_sample_schema} | { type, metadata} | { type, metadata}`

  The configuration for the data source used for the evaluation runs. Dictates the schema of the data used in the evaluation.

  - `class Custom`

    A CustomDataSourceConfig object that defines the schema for the data source used for the evaluation runs.
    This schema is used to define the shape of the data that will be:

    - Used to define your testing criteria and
    - What data is required when creating a run

    - `item_schema: Hash[Symbol, untyped]`

      The json schema for each row in the data source.

    - `type: :custom`

      The type of data source. Always `custom`.

      - `:custom`

    - `include_sample_schema: bool`

      Whether the eval should expect you to populate the sample namespace (ie, by generating responses off of your data source)

  - `class Logs`

    A data source config which specifies the metadata property of your logs query.
    This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.

    - `type: :logs`

      The type of data source. Always `logs`.

      - `:logs`

    - `metadata: Hash[Symbol, untyped]`

      Metadata filters for the logs data source.

  - `class StoredCompletions`

    Deprecated in favor of LogsDataSourceConfig.

    - `type: :stored_completions`

      The type of data source. Always `stored_completions`.

      - `:stored_completions`

    - `metadata: Hash[Symbol, untyped]`

      Metadata filters for the stored completions data source.

- `testing_criteria: Array[{ input, labels, model, 3 more} | StringCheckGrader | TextSimilarityGrader & { pass_threshold} | 2 more]`

  A list of graders for all eval runs in this group. Graders can reference variables in the data source using double curly braces notation, like `{{item.variable_name}}`. To reference the model's output, use the `sample` namespace (ie, `{{sample.output_text}}`).

  - `class LabelModel`

    A LabelModelGrader object which uses a model to assign labels to each item
    in the evaluation.

    - `input: Array[{ content, role} | { content, role, type}]`

      A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

      - `class SimpleInputMessage`

        - `content: String`

          The content of the message.

        - `role: String`

          The role of the message (e.g. "system", "assistant", "user").

      - `class EvalItem`

        A message input to the model with a role indicating instruction following
        hierarchy. Instructions given with the `developer` or `system` role take
        precedence over instructions given with the `user` role. Messages with the
        `assistant` role are presumed to have been generated by the model in previous
        interactions.

        - `content: String | ResponseInputText | { text, type} | 3 more`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

            A text input to the model.

          - `class ResponseInputText`

            A text input to the model.

            - `text: String`

              The text input to the model.

            - `type: :input_text`

              The type of the input item. Always `input_text`.

              - `:input_text`

          - `class OutputText`

            A text output from the model.

            - `text: String`

              The text output from the model.

            - `type: :output_text`

              The type of the output text. Always `output_text`.

              - `:output_text`

          - `class InputImage`

            An image input block used within EvalItem content arrays.

            - `image_url: String`

              The URL of the image input.

            - `type: :input_image`

              The type of the image input. Always `input_image`.

              - `:input_image`

            - `detail: String`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio`

            An audio input to the model.

            - `input_audio: { data, format_}`

              - `data: String`

                Base64-encoded audio data.

              - `format_: :mp3 | :wav`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `:mp3`

                - `:wav`

            - `type: :input_audio`

              The type of the input item. Always `input_audio`.

              - `:input_audio`

          - `Array[GraderInputItem]`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `String`

              A text input to the model.

            - `class ResponseInputText`

              A text input to the model.

              - `text: String`

                The text input to the model.

              - `type: :input_text`

                The type of the input item. Always `input_text`.

                - `:input_text`

            - `class OutputText`

              A text output from the model.

              - `text: String`

                The text output from the model.

              - `type: :output_text`

                The type of the output text. Always `output_text`.

                - `:output_text`

            - `class InputImage`

              An image input block used within EvalItem content arrays.

              - `image_url: String`

                The URL of the image input.

              - `type: :input_image`

                The type of the image input. Always `input_image`.

                - `:input_image`

              - `detail: String`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio`

              An audio input to the model.

              - `input_audio: { data, format_}`

                - `data: String`

                  Base64-encoded audio data.

                - `format_: :mp3 | :wav`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `:mp3`

                  - `:wav`

              - `type: :input_audio`

                The type of the input item. Always `input_audio`.

                - `:input_audio`

        - `role: :user | :assistant | :system | :developer`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `:user`

          - `:assistant`

          - `:system`

          - `:developer`

        - `type: :message`

          The type of the message input. Always `message`.

          - `:message`

    - `labels: Array[String]`

      The labels to classify to each item in the evaluation.

    - `model: String`

      The model to use for the evaluation. Must support structured outputs.

    - `name: String`

      The name of the grader.

    - `passing_labels: Array[String]`

      The labels that indicate a passing result. Must be a subset of labels.

    - `type: :label_model`

      The object type, which is always `label_model`.

      - `:label_model`

  - `class StringCheckGrader`

    A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

    - `input: String`

      The input text. This may include template strings.

    - `name: String`

      The name of the grader.

    - `operation: :eq | :ne | :like | :ilike`

      The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

      - `:eq`

      - `:ne`

      - `:like`

      - `:ilike`

    - `reference: String`

      The reference text. This may include template strings.

    - `type: :string_check`

      The object type, which is always `string_check`.

      - `:string_check`

  - `class TextSimilarity`

    A TextSimilarityGrader object which grades text based on similarity metrics.

    - `pass_threshold: Float`

      The threshold for the score.

  - `class Python`

    A PythonGrader object that runs a python script on the input.

    - `pass_threshold: Float`

      The threshold for the score.

  - `class ScoreModel`

    A ScoreModelGrader object that uses a model to assign a score to the input.

    - `pass_threshold: Float`

      The threshold for the score.

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `name: String`

  The name of the evaluation.

### Returns

- `class EvalCreateResponse`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `id: String`

    Unique identifier for the evaluation.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the eval was created.

  - `data_source_config: EvalCustomDataSourceConfig | { schema, type, metadata} | EvalStoredCompletionsDataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :custom`

        The type of data source. Always `custom`.

        - `:custom`

    - `class Logs`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :logs`

        The type of data source. Always `logs`.

        - `:logs`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig`

      Deprecated in favor of LogsDataSourceConfig.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :stored_completions`

        The type of data source. Always `stored_completions`.

        - `:stored_completions`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the evaluation.

  - `object: :eval`

    The object type.

    - `:eval`

  - `testing_criteria: Array[LabelModelGrader | StringCheckGrader | TextSimilarityGrader & { pass_threshold} | 2 more]`

    A list of testing criteria.

    - `class LabelModelGrader`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `input: Array[{ content, role, type}]`

        - `content: String | ResponseInputText | { text, type} | 3 more`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

            A text input to the model.

          - `class ResponseInputText`

            A text input to the model.

            - `text: String`

              The text input to the model.

            - `type: :input_text`

              The type of the input item. Always `input_text`.

              - `:input_text`

          - `class OutputText`

            A text output from the model.

            - `text: String`

              The text output from the model.

            - `type: :output_text`

              The type of the output text. Always `output_text`.

              - `:output_text`

          - `class InputImage`

            An image input block used within EvalItem content arrays.

            - `image_url: String`

              The URL of the image input.

            - `type: :input_image`

              The type of the image input. Always `input_image`.

              - `:input_image`

            - `detail: String`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio`

            An audio input to the model.

            - `input_audio: { data, format_}`

              - `data: String`

                Base64-encoded audio data.

              - `format_: :mp3 | :wav`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `:mp3`

                - `:wav`

            - `type: :input_audio`

              The type of the input item. Always `input_audio`.

              - `:input_audio`

          - `Array[GraderInputItem]`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `String`

              A text input to the model.

            - `class ResponseInputText`

              A text input to the model.

              - `text: String`

                The text input to the model.

              - `type: :input_text`

                The type of the input item. Always `input_text`.

                - `:input_text`

            - `class OutputText`

              A text output from the model.

              - `text: String`

                The text output from the model.

              - `type: :output_text`

                The type of the output text. Always `output_text`.

                - `:output_text`

            - `class InputImage`

              An image input block used within EvalItem content arrays.

              - `image_url: String`

                The URL of the image input.

              - `type: :input_image`

                The type of the image input. Always `input_image`.

                - `:input_image`

              - `detail: String`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio`

              An audio input to the model.

              - `input_audio: { data, format_}`

                - `data: String`

                  Base64-encoded audio data.

                - `format_: :mp3 | :wav`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `:mp3`

                  - `:wav`

              - `type: :input_audio`

                The type of the input item. Always `input_audio`.

                - `:input_audio`

        - `role: :user | :assistant | :system | :developer`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `:user`

          - `:assistant`

          - `:system`

          - `:developer`

        - `type: :message`

          The type of the message input. Always `message`.

          - `:message`

      - `labels: Array[String]`

        The labels to assign to each item in the evaluation.

      - `model: String`

        The model to use for the evaluation. Must support structured outputs.

      - `name: String`

        The name of the grader.

      - `passing_labels: Array[String]`

        The labels that indicate a passing result. Must be a subset of labels.

      - `type: :label_model`

        The object type, which is always `label_model`.

        - `:label_model`

    - `class StringCheckGrader`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `input: String`

        The input text. This may include template strings.

      - `name: String`

        The name of the grader.

      - `operation: :eq | :ne | :like | :ilike`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `:eq`

        - `:ne`

        - `:like`

        - `:ilike`

      - `reference: String`

        The reference text. This may include template strings.

      - `type: :string_check`

        The object type, which is always `string_check`.

        - `:string_check`

    - `class EvalGraderTextSimilarity`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderPython`

      A PythonGrader object that runs a python script on the input.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderScoreModel`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `pass_threshold: Float`

        The threshold for the score.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

eval_ = openai.evals.create(
  data_source_config: {item_schema: {foo: "bar"}, type: :custom},
  testing_criteria: [
    {
      input: [{content: "content", role: "role"}],
      labels: ["string"],
      model: "model",
      name: "name",
      passing_labels: ["string"],
      type: :label_model
    }
  ]
)

puts(eval_)
```

## Retrieve

`evals.retrieve(eval_id) -> EvalRetrieveResponse`

**get** `/evals/{eval_id}`

Get an evaluation by ID.

### Parameters

- `eval_id: String`

### Returns

- `class EvalRetrieveResponse`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `id: String`

    Unique identifier for the evaluation.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the eval was created.

  - `data_source_config: EvalCustomDataSourceConfig | { schema, type, metadata} | EvalStoredCompletionsDataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :custom`

        The type of data source. Always `custom`.

        - `:custom`

    - `class Logs`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :logs`

        The type of data source. Always `logs`.

        - `:logs`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig`

      Deprecated in favor of LogsDataSourceConfig.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :stored_completions`

        The type of data source. Always `stored_completions`.

        - `:stored_completions`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the evaluation.

  - `object: :eval`

    The object type.

    - `:eval`

  - `testing_criteria: Array[LabelModelGrader | StringCheckGrader | TextSimilarityGrader & { pass_threshold} | 2 more]`

    A list of testing criteria.

    - `class LabelModelGrader`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `input: Array[{ content, role, type}]`

        - `content: String | ResponseInputText | { text, type} | 3 more`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

            A text input to the model.

          - `class ResponseInputText`

            A text input to the model.

            - `text: String`

              The text input to the model.

            - `type: :input_text`

              The type of the input item. Always `input_text`.

              - `:input_text`

          - `class OutputText`

            A text output from the model.

            - `text: String`

              The text output from the model.

            - `type: :output_text`

              The type of the output text. Always `output_text`.

              - `:output_text`

          - `class InputImage`

            An image input block used within EvalItem content arrays.

            - `image_url: String`

              The URL of the image input.

            - `type: :input_image`

              The type of the image input. Always `input_image`.

              - `:input_image`

            - `detail: String`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio`

            An audio input to the model.

            - `input_audio: { data, format_}`

              - `data: String`

                Base64-encoded audio data.

              - `format_: :mp3 | :wav`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `:mp3`

                - `:wav`

            - `type: :input_audio`

              The type of the input item. Always `input_audio`.

              - `:input_audio`

          - `Array[GraderInputItem]`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `String`

              A text input to the model.

            - `class ResponseInputText`

              A text input to the model.

              - `text: String`

                The text input to the model.

              - `type: :input_text`

                The type of the input item. Always `input_text`.

                - `:input_text`

            - `class OutputText`

              A text output from the model.

              - `text: String`

                The text output from the model.

              - `type: :output_text`

                The type of the output text. Always `output_text`.

                - `:output_text`

            - `class InputImage`

              An image input block used within EvalItem content arrays.

              - `image_url: String`

                The URL of the image input.

              - `type: :input_image`

                The type of the image input. Always `input_image`.

                - `:input_image`

              - `detail: String`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio`

              An audio input to the model.

              - `input_audio: { data, format_}`

                - `data: String`

                  Base64-encoded audio data.

                - `format_: :mp3 | :wav`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `:mp3`

                  - `:wav`

              - `type: :input_audio`

                The type of the input item. Always `input_audio`.

                - `:input_audio`

        - `role: :user | :assistant | :system | :developer`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `:user`

          - `:assistant`

          - `:system`

          - `:developer`

        - `type: :message`

          The type of the message input. Always `message`.

          - `:message`

      - `labels: Array[String]`

        The labels to assign to each item in the evaluation.

      - `model: String`

        The model to use for the evaluation. Must support structured outputs.

      - `name: String`

        The name of the grader.

      - `passing_labels: Array[String]`

        The labels that indicate a passing result. Must be a subset of labels.

      - `type: :label_model`

        The object type, which is always `label_model`.

        - `:label_model`

    - `class StringCheckGrader`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `input: String`

        The input text. This may include template strings.

      - `name: String`

        The name of the grader.

      - `operation: :eq | :ne | :like | :ilike`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `:eq`

        - `:ne`

        - `:like`

        - `:ilike`

      - `reference: String`

        The reference text. This may include template strings.

      - `type: :string_check`

        The object type, which is always `string_check`.

        - `:string_check`

    - `class EvalGraderTextSimilarity`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderPython`

      A PythonGrader object that runs a python script on the input.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderScoreModel`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `pass_threshold: Float`

        The threshold for the score.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

eval_ = openai.evals.retrieve("eval_id")

puts(eval_)
```

## Update

`evals.update(eval_id, **kwargs) -> EvalUpdateResponse`

**post** `/evals/{eval_id}`

Update certain properties of an evaluation.

### Parameters

- `eval_id: String`

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `name: String`

  Rename the evaluation.

### Returns

- `class EvalUpdateResponse`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `id: String`

    Unique identifier for the evaluation.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the eval was created.

  - `data_source_config: EvalCustomDataSourceConfig | { schema, type, metadata} | EvalStoredCompletionsDataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :custom`

        The type of data source. Always `custom`.

        - `:custom`

    - `class Logs`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :logs`

        The type of data source. Always `logs`.

        - `:logs`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig`

      Deprecated in favor of LogsDataSourceConfig.

      - `schema: Hash[Symbol, untyped]`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `type: :stored_completions`

        The type of data source. Always `stored_completions`.

        - `:stored_completions`

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `name: String`

    The name of the evaluation.

  - `object: :eval`

    The object type.

    - `:eval`

  - `testing_criteria: Array[LabelModelGrader | StringCheckGrader | TextSimilarityGrader & { pass_threshold} | 2 more]`

    A list of testing criteria.

    - `class LabelModelGrader`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `input: Array[{ content, role, type}]`

        - `content: String | ResponseInputText | { text, type} | 3 more`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

            A text input to the model.

          - `class ResponseInputText`

            A text input to the model.

            - `text: String`

              The text input to the model.

            - `type: :input_text`

              The type of the input item. Always `input_text`.

              - `:input_text`

          - `class OutputText`

            A text output from the model.

            - `text: String`

              The text output from the model.

            - `type: :output_text`

              The type of the output text. Always `output_text`.

              - `:output_text`

          - `class InputImage`

            An image input block used within EvalItem content arrays.

            - `image_url: String`

              The URL of the image input.

            - `type: :input_image`

              The type of the image input. Always `input_image`.

              - `:input_image`

            - `detail: String`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio`

            An audio input to the model.

            - `input_audio: { data, format_}`

              - `data: String`

                Base64-encoded audio data.

              - `format_: :mp3 | :wav`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `:mp3`

                - `:wav`

            - `type: :input_audio`

              The type of the input item. Always `input_audio`.

              - `:input_audio`

          - `Array[GraderInputItem]`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `String`

              A text input to the model.

            - `class ResponseInputText`

              A text input to the model.

              - `text: String`

                The text input to the model.

              - `type: :input_text`

                The type of the input item. Always `input_text`.

                - `:input_text`

            - `class OutputText`

              A text output from the model.

              - `text: String`

                The text output from the model.

              - `type: :output_text`

                The type of the output text. Always `output_text`.

                - `:output_text`

            - `class InputImage`

              An image input block used within EvalItem content arrays.

              - `image_url: String`

                The URL of the image input.

              - `type: :input_image`

                The type of the image input. Always `input_image`.

                - `:input_image`

              - `detail: String`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio`

              An audio input to the model.

              - `input_audio: { data, format_}`

                - `data: String`

                  Base64-encoded audio data.

                - `format_: :mp3 | :wav`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `:mp3`

                  - `:wav`

              - `type: :input_audio`

                The type of the input item. Always `input_audio`.

                - `:input_audio`

        - `role: :user | :assistant | :system | :developer`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `:user`

          - `:assistant`

          - `:system`

          - `:developer`

        - `type: :message`

          The type of the message input. Always `message`.

          - `:message`

      - `labels: Array[String]`

        The labels to assign to each item in the evaluation.

      - `model: String`

        The model to use for the evaluation. Must support structured outputs.

      - `name: String`

        The name of the grader.

      - `passing_labels: Array[String]`

        The labels that indicate a passing result. Must be a subset of labels.

      - `type: :label_model`

        The object type, which is always `label_model`.

        - `:label_model`

    - `class StringCheckGrader`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `input: String`

        The input text. This may include template strings.

      - `name: String`

        The name of the grader.

      - `operation: :eq | :ne | :like | :ilike`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `:eq`

        - `:ne`

        - `:like`

        - `:ilike`

      - `reference: String`

        The reference text. This may include template strings.

      - `type: :string_check`

        The object type, which is always `string_check`.

        - `:string_check`

    - `class EvalGraderTextSimilarity`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderPython`

      A PythonGrader object that runs a python script on the input.

      - `pass_threshold: Float`

        The threshold for the score.

    - `class EvalGraderScoreModel`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `pass_threshold: Float`

        The threshold for the score.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

eval_ = openai.evals.update("eval_id")

puts(eval_)
```

## Delete

`evals.delete(eval_id) -> EvalDeleteResponse`

**delete** `/evals/{eval_id}`

Delete an evaluation.

### Parameters

- `eval_id: String`

### Returns

- `class EvalDeleteResponse`

  - `deleted: bool`

  - `eval_id: String`

  - `object: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

eval_ = openai.evals.delete("eval_id")

puts(eval_)
```

### Domain Types

### Eval Custom Data Source Config

- `class EvalCustomDataSourceConfig`

  A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
  The response schema defines the shape of the data that will be:

  - Used to define your testing criteria and
  - What data is required when creating a run

  - `schema: Hash[Symbol, untyped]`

    The json schema for the run data source items.
    Learn how to build JSON schemas [here](https://json-schema.org/).

  - `type: :custom`

    The type of data source. Always `custom`.

    - `:custom`

### Eval Stored Completions Data Source Config

- `class EvalStoredCompletionsDataSourceConfig`

  Deprecated in favor of LogsDataSourceConfig.

  - `schema: Hash[Symbol, untyped]`

    The json schema for the run data source items.
    Learn how to build JSON schemas [here](https://json-schema.org/).

  - `type: :stored_completions`

    The type of data source. Always `stored_completions`.

    - `:stored_completions`

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

## Runs

### List

`evals.runs.list(eval_id, **kwargs) -> CursorPage<RunListResponse>`

**get** `/evals/{eval_id}/runs`

Get a list of runs for an evaluation.

#### Parameters

- `eval_id: String`

- `after: String`

  Identifier for the last run from the previous pagination request.

- `limit: Integer`

  Number of runs to retrieve.

- `order: :asc | :desc`

  Sort order for runs by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

  - `:asc`

  - `:desc`

- `status: :queued | :in_progress | :completed | 2 more`

  Filter runs by status. One of `queued` | `in_progress` | `failed` | `completed` | `canceled`.

  - `:queued`

  - `:in_progress`

  - `:completed`

  - `:canceled`

  - `:failed`

#### Returns

- `class RunListResponse`

  A schema representing an evaluation run.

  - `id: String`

    Unique identifier for the evaluation run.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `data_source: CreateEvalJSONLRunDataSource | CreateEvalCompletionsRunDataSource | { source, type, input_messages, 2 more}`

    Information about the run's data source.

    - `class CreateEvalJSONLRunDataSource`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `source: { content, type} | { id, type}`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

      - `type: :jsonl`

        The type of data source. Always `jsonl`.

        - `:jsonl`

    - `class CreateEvalCompletionsRunDataSource`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 3 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class StoredCompletions`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `type: :stored_completions`

            The type of source. Always `stored_completions`.

            - `:stored_completions`

          - `created_after: Integer`

            An optional Unix timestamp to filter items created after this time.

          - `created_before: Integer`

            An optional Unix timestamp to filter items created before this time.

          - `limit: Integer`

            An optional maximum number of items to return.

          - `metadata: Metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `model: String`

            An optional model to filter by (e.g., 'gpt-4o').

      - `type: :completions`

        The type of run data source. Always `completions`.

        - `:completions`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[EasyInputMessage | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputMessageContentList`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                  A text input to the model.

                - `Array[ResponseInputContent]`

                  A list of one or many input items to the model, containing different content
                  types.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class ResponseInputImage`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `detail: :low | :high | :auto | :original`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `:low`

                      - `:high`

                      - `:auto`

                      - `:original`

                    - `type: :input_image`

                      The type of the input item. Always `input_image`.

                      - `:input_image`

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `image_url: String`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile`

                    A file input to the model.

                    - `type: :input_file`

                      The type of the input item. Always `input_file`.

                      - `:input_file`

                    - `file_data: String`

                      The content of the file to be sent to the model.

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `file_url: String`

                      The URL of the file to be sent to the model.

                    - `filename: String`

                      The name of the file to be sent to the model.

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `phase: :commentary | :final_answer`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `:commentary`

                - `:final_answer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, response_format, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `response_format: ResponseFormatText | ResponseFormatJSONSchema | ResponseFormatJSONObject`

          An object specifying the format that the model must output.

          Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
          Structured Outputs which ensures the model will match your supplied JSON
          schema. Learn more in the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

          Setting to `{ "type": "json_object" }` enables the older JSON mode, which
          ensures the message the model generates is valid JSON. Using `json_schema`
          is preferred for models that support it.

          - `class ResponseFormatText`

            Default response format. Used to generate text responses.

            - `type: :text`

              The type of response format being defined. Always `text`.

              - `:text`

          - `class ResponseFormatJSONSchema`

            JSON Schema response format. Used to generate structured JSON responses.
            Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

            - `json_schema: { name, description, schema, strict}`

              Structured Outputs configuration options, including a JSON Schema.

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `type: :json_schema`

              The type of response format being defined. Always `json_schema`.

              - `:json_schema`

          - `class ResponseFormatJSONObject`

            JSON object response format. An older method of generating JSON responses.
            Using `json_schema` is recommended for models that support it. Note that the
            model will not generate JSON without a system or user message instructing it
            to do so.

            - `type: :json_object`

              The type of response format being defined. Always `json_object`.

              - `:json_object`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `tools: Array[ChatCompletionFunctionTool]`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

          - `function: FunctionDefinition`

            - `name: String`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `description: String`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `parameters: FunctionParameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `strict: bool`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `type: :function`

            The type of the tool. Currently, only `function` is supported.

            - `:function`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 8 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class Responses`

          A EvalResponsesSource object describing a run data source configuration.

          - `type: :responses`

            The type of run data source. Always `responses`.

            - `:responses`

          - `created_after: Integer`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `created_before: Integer`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `instructions_search: String`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `metadata: untyped`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `model: String`

            The name of the model to find responses for. This is a query parameter used to select responses.

          - `reasoning_effort: ReasoningEffort`

            Constrains effort on reasoning for
            [reasoning models](https://platform.openai.com/docs/guides/reasoning).
            Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
            reasoning effort can result in faster responses and fewer tokens used
            on reasoning in a response.

            - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
            - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
            - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
            - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

            - `:none`

            - `:minimal`

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

          - `temperature: Float`

            Sampling temperature. This is a query parameter used to select responses.

          - `tools: Array[String]`

            List of tool names. This is a query parameter used to select responses.

          - `top_p: Float`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `users: Array[String]`

            List of user identifiers. This is a query parameter used to select responses.

      - `type: :responses`

        The type of run data source. Always `responses`.

        - `:responses`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[{ content, role} | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage`

              - `content: String`

                The content of the message.

              - `role: String`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, seed, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `text: { format_}`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `format_: ResponseFormatTextConfig`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText`

              Default response format. Used to generate text responses.

              - `type: :text`

                The type of response format being defined. Always `text`.

                - `:text`

            - `class ResponseFormatTextJSONSchemaConfig`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `type: :json_schema`

                The type of response format being defined. Always `json_schema`.

                - `:json_schema`

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJSONObject`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `type: :json_object`

                The type of response format being defined. Always `json_object`.

                - `:json_object`

        - `tools: Array[Tool]`

          An array of tools the model may call while generating a response. You
          can specify which tool to use by setting the `tool_choice` parameter.

          The two categories of tools you can provide the model are:

          - **Built-in tools**: Tools that are provided by OpenAI that extend the
            model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
            or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
            [built-in tools](https://platform.openai.com/docs/guides/tools).
          - **Function calls (custom tools)**: Functions that are defined by you,
            enabling the model to call your own code. Learn more about
            [function calling](https://platform.openai.com/docs/guides/function-calling).

          - `class FunctionTool`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `name: String`

              The name of the function to call.

            - `parameters: Hash[Symbol, untyped]`

              A JSON schema object describing the parameters of the function.

            - `strict: bool`

              Whether to enforce strict parameter validation. Default `true`.

            - `type: :function`

              The type of the function tool. Always `function`.

              - `:function`

            - `defer_loading: bool`

              Whether this function is deferred and loaded via tool search.

            - `description: String`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `type: :file_search`

              The type of the file search tool. Always `file_search`.

              - `:file_search`

            - `vector_store_ids: Array[String]`

              The IDs of the vector stores to search.

            - `filters: ComparisonFilter | CompoundFilter`

              A filter to apply.

              - `class ComparisonFilter`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `key: String`

                  The key to compare against the value.

                - `type: :eq | :ne | :gt | 3 more`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `:eq`

                  - `:ne`

                  - `:gt`

                  - `:gte`

                  - `:lt`

                  - `:lte`

                - `value: String | Float | bool | Array[String | Float]`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `Float`

                  - `bool`

                  - `Array[String | Float]`

                    - `String`

                    - `Float`

              - `class CompoundFilter`

                Combine multiple filters using `and` or `or`.

                - `filters: Array[ComparisonFilter | untyped]`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `key: String`

                      The key to compare against the value.

                    - `type: :eq | :ne | :gt | 3 more`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `:eq`

                      - `:ne`

                      - `:gt`

                      - `:gte`

                      - `:lt`

                      - `:lte`

                    - `value: String | Float | bool | Array[String | Float]`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `Float`

                      - `bool`

                      - `Array[String | Float]`

                        - `String`

                        - `Float`

                  - `untyped`

                - `type: :and | :or`

                  Type of operation: `and` or `or`.

                  - `:and`

                  - `:or`

            - `max_num_results: Integer`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `ranking_options: { hybrid_search, ranker, score_threshold}`

              Ranking options for search.

              - `hybrid_search: { embedding_weight, text_weight}`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `embedding_weight: Float`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `text_weight: Float`

                  The weight of the text in the reciprocal ranking fusion.

              - `ranker: :auto | :"default-2024-11-15"`

                The ranker to use for the file search.

                - `:auto`

                - `:"default-2024-11-15"`

              - `score_threshold: Float`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `type: :computer`

              The type of the computer tool. Always `computer`.

              - `:computer`

          - `class ComputerUsePreviewTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `display_height: Integer`

              The height of the computer display.

            - `display_width: Integer`

              The width of the computer display.

            - `environment: :windows | :mac | :linux | 2 more`

              The type of computer environment to control.

              - `:windows`

              - `:mac`

              - `:linux`

              - `:ubuntu`

              - `:browser`

            - `type: :computer_use_preview`

              The type of the computer use tool. Always `computer_use_preview`.

              - `:computer_use_preview`

          - `class WebSearchTool`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search | :web_search_2025_08_26`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `:web_search`

              - `:web_search_2025_08_26`

            - `filters: { allowed_domains}`

              Filters for the search.

              - `allowed_domains: Array[String]`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { city, country, region, 2 more}`

              The approximate location of the user.

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

          - `class Mcp`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

            - `server_label: String`

              A label for this MCP server, used to identify it in tool calls.

            - `type: :mcp`

              The type of the MCP tool. Always `mcp`.

              - `:mcp`

            - `allowed_tools: Array[String] | { read_only, tool_names}`

              List of allowed tool names or a filter object.

              - `Array[String]`

                A string array of allowed tool names

              - `class McpToolFilter`

                A filter object to specify which tools are allowed.

                - `read_only: bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `tool_names: Array[String]`

                  List of allowed tool names.

            - `authorization: String`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `connector_id: :connector_dropbox | :connector_gmail | :connector_googlecalendar | 5 more`

              Identifier for service connectors, like those available in ChatGPT. One of
              `server_url` or `connector_id` must be provided. Learn more about service
              connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

              Currently supported `connector_id` values are:

              - Dropbox: `connector_dropbox`
              - Gmail: `connector_gmail`
              - Google Calendar: `connector_googlecalendar`
              - Google Drive: `connector_googledrive`
              - Microsoft Teams: `connector_microsoftteams`
              - Outlook Calendar: `connector_outlookcalendar`
              - Outlook Email: `connector_outlookemail`
              - SharePoint: `connector_sharepoint`

              - `:connector_dropbox`

              - `:connector_gmail`

              - `:connector_googlecalendar`

              - `:connector_googledrive`

              - `:connector_microsoftteams`

              - `:connector_outlookcalendar`

              - `:connector_outlookemail`

              - `:connector_sharepoint`

            - `defer_loading: bool`

              Whether this MCP tool is deferred and discovered via tool search.

            - `headers: Hash[Symbol, String]`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `require_approval: { always, never} | :always | :never`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `always: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

                - `never: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

              - `McpToolApprovalSetting = :always | :never`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `:always`

                - `:never`

            - `server_description: String`

              Optional description of the MCP server, used to provide more context.

            - `server_url: String`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `class CodeInterpreter`

            A tool that runs Python code to help generate a response to a prompt.

            - `container: String | { type, file_ids, memory_limit, network_policy}`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

                The container ID.

              - `class CodeInterpreterToolAuto`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `type: :auto`

                  Always `auto`.

                  - `:auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the code interpreter container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

            - `type: :code_interpreter`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `:code_interpreter`

          - `class ImageGeneration`

            A tool that generates images using the GPT image models.

            - `type: :image_generation`

              The type of the image generation tool. Always `image_generation`.

              - `:image_generation`

            - `action: :generate | :edit | :auto`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `:generate`

              - `:edit`

              - `:auto`

            - `background: :transparent | :opaque | :auto`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `:transparent`

              - `:opaque`

              - `:auto`

            - `input_fidelity: :high | :low`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `:high`

              - `:low`

            - `input_image_mask: { file_id, image_url}`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `file_id: String`

                File ID for the mask image.

              - `image_url: String`

                Base64-encoded mask image.

            - `model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

              The image generation model to use. Default: `gpt-image-1`.

              - `String`

              - `:"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

                The image generation model to use. Default: `gpt-image-1`.

                - `:"gpt-image-1"`

                - `:"gpt-image-1-mini"`

                - `:"gpt-image-1.5"`

            - `moderation: :auto | :low`

              Moderation level for the generated image. Default: `auto`.

              - `:auto`

              - `:low`

            - `output_compression: Integer`

              Compression level for the output image. Default: 100.

            - `output_format: :png | :webp | :jpeg`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `:png`

              - `:webp`

              - `:jpeg`

            - `partial_images: Integer`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `quality: :low | :medium | :high | :auto`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `:low`

              - `:medium`

              - `:high`

              - `:auto`

            - `size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `:"1024x1024"`

              - `:"1024x1536"`

              - `:"1536x1024"`

              - `:auto`

          - `class LocalShell`

            A tool that allows the model to execute shell commands in a local environment.

            - `type: :local_shell`

              The type of the local shell tool. Always `local_shell`.

              - `:local_shell`

          - `class FunctionShellTool`

            A tool that allows the model to execute shell commands.

            - `type: :shell`

              The type of the shell tool. Always `shell`.

              - `:shell`

            - `environment: ContainerAuto | LocalEnvironment | ContainerReference`

              - `class ContainerAuto`

                - `type: :container_auto`

                  Automatically creates a container for this request

                  - `:container_auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

                - `skills: Array[SkillReference | InlineSkill]`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference`

                    - `skill_id: String`

                      The ID of the referenced skill.

                    - `type: :skill_reference`

                      References a skill created with the /v1/skills endpoint.

                      - `:skill_reference`

                    - `version: String`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill`

                    - `description: String`

                      The description of the skill.

                    - `name: String`

                      The name of the skill.

                    - `source: InlineSkillSource`

                      Inline skill payload

                      - `data: String`

                        Base64-encoded skill zip bundle.

                      - `media_type: :"application/zip"`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `:"application/zip"`

                      - `type: :base64`

                        The type of the inline skill source. Must be `base64`.

                        - `:base64`

                    - `type: :inline`

                      Defines an inline skill for this request.

                      - `:inline`

              - `class LocalEnvironment`

                - `type: :local`

                  Use a local computer environment.

                  - `:local`

                - `skills: Array[LocalSkill]`

                  An optional list of skills.

                  - `description: String`

                    The description of the skill.

                  - `name: String`

                    The name of the skill.

                  - `path: String`

                    The path to the directory containing the skill.

              - `class ContainerReference`

                - `container_id: String`

                  The ID of the referenced container.

                - `type: :container_reference`

                  References a container created with the /v1/containers endpoint

                  - `:container_reference`

          - `class CustomTool`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `name: String`

              The name of the custom tool, used to identify it in tool calls.

            - `type: :custom`

              The type of the custom tool. Always `custom`.

              - `:custom`

            - `defer_loading: bool`

              Whether this tool should be deferred and discovered via tool search.

            - `description: String`

              Optional description of the custom tool, used to provide more context.

            - `format_: CustomToolInputFormat`

              The input format for the custom tool. Default is unconstrained text.

              - `class Text`

                Unconstrained free-form text.

                - `type: :text`

                  Unconstrained text format. Always `text`.

                  - `:text`

              - `class Grammar`

                A grammar defined by the user.

                - `definition: String`

                  The grammar definition.

                - `syntax: :lark | :regex`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `:lark`

                  - `:regex`

                - `type: :grammar`

                  Grammar format. Always `grammar`.

                  - `:grammar`

          - `class NamespaceTool`

            Groups function/custom tools under a shared namespace.

            - `description: String`

              A description of the namespace shown to the model.

            - `name: String`

              The namespace name used in tool calls (for example, `crm`).

            - `tools: Array[{ name, type, defer_loading, 3 more} | CustomTool]`

              The function/custom tools available inside this namespace.

              - `class Function`

                - `name: String`

                - `type: :function`

                  - `:function`

                - `defer_loading: bool`

                  Whether this function should be deferred and discovered via tool search.

                - `description: String`

                - `parameters: untyped`

                - `strict: bool`

              - `class CustomTool`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `name: String`

                  The name of the custom tool, used to identify it in tool calls.

                - `type: :custom`

                  The type of the custom tool. Always `custom`.

                  - `:custom`

                - `defer_loading: bool`

                  Whether this tool should be deferred and discovered via tool search.

                - `description: String`

                  Optional description of the custom tool, used to provide more context.

                - `format_: CustomToolInputFormat`

                  The input format for the custom tool. Default is unconstrained text.

                  - `class Text`

                    Unconstrained free-form text.

                    - `type: :text`

                      Unconstrained text format. Always `text`.

                      - `:text`

                  - `class Grammar`

                    A grammar defined by the user.

                    - `definition: String`

                      The grammar definition.

                    - `syntax: :lark | :regex`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `:lark`

                      - `:regex`

                    - `type: :grammar`

                      Grammar format. Always `grammar`.

                      - `:grammar`

            - `type: :namespace`

              The type of the tool. Always `namespace`.

              - `:namespace`

          - `class ToolSearchTool`

            Hosted or BYOT tool search configuration for deferred tools.

            - `type: :tool_search`

              The type of the tool. Always `tool_search`.

              - `:tool_search`

            - `description: String`

              Description shown to the model for a client-executed tool search tool.

            - `execution: :server | :client`

              Whether tool search is executed by the server or by the client.

              - `:server`

              - `:client`

            - `parameters: untyped`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search_preview | :web_search_preview_2025_03_11`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `:web_search_preview`

              - `:web_search_preview_2025_03_11`

            - `search_content_types: Array[:text | :image]`

              - `:text`

              - `:image`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { type, city, country, 2 more}`

              The user's location.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `type: :apply_patch`

              The type of the tool. Always `apply_patch`.

              - `:apply_patch`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `error: EvalAPIError`

    An object representing an error response from the Eval API.

    - `code: String`

      The error code.

    - `message: String`

      The error message.

  - `eval_id: String`

    The identifier of the associated evaluation.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    The model that is evaluated, if applicable.

  - `name: String`

    The name of the evaluation run.

  - `object: :"eval.run"`

    The type of the object. Always "eval.run".

    - `:"eval.run"`

  - `per_model_usage: Array[{ cached_tokens, completion_tokens, invocation_count, 3 more}]`

    Usage statistics for each model during the evaluation run.

    - `cached_tokens: Integer`

      The number of tokens retrieved from cache.

    - `completion_tokens: Integer`

      The number of completion tokens generated.

    - `invocation_count: Integer`

      The number of invocations.

    - `model_name: String`

      The name of the model.

    - `prompt_tokens: Integer`

      The number of prompt tokens used.

    - `total_tokens: Integer`

      The total number of tokens used.

  - `per_testing_criteria_results: Array[{ failed, passed, testing_criteria}]`

    Results per testing criteria applied during the evaluation run.

    - `failed: Integer`

      Number of tests failed for this criteria.

    - `passed: Integer`

      Number of tests passed for this criteria.

    - `testing_criteria: String`

      A description of the testing criteria.

  - `report_url: String`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `result_counts: { errored, failed, passed, total}`

    Counters summarizing the outcomes of the evaluation run.

    - `errored: Integer`

      Number of output items that resulted in an error.

    - `failed: Integer`

      Number of output items that failed to pass the evaluation.

    - `passed: Integer`

      Number of output items that passed the evaluation.

    - `total: Integer`

      Total number of executed output items.

  - `status: String`

    The status of the evaluation run.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.evals.runs.list("eval_id")

puts(page)
```

### Create

`evals.runs.create(eval_id, **kwargs) -> RunCreateResponse`

**post** `/evals/{eval_id}/runs`

Kicks off a new run for a given evaluation, specifying the data source, and what model configuration to use to test. The datasource will be validated against the schema specified in the config of the evaluation.

#### Parameters

- `eval_id: String`

- `data_source: CreateEvalJSONLRunDataSource | CreateEvalCompletionsRunDataSource | { source, type, input_messages, 2 more}`

  Details about the run's data source.

  - `class CreateEvalJSONLRunDataSource`

    A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

    - `source: { content, type} | { id, type}`

      Determines what populates the `item` namespace in the data source.

      - `class FileContent`

        - `content: Array[{ item, sample}]`

          The content of the jsonl file.

          - `item: Hash[Symbol, untyped]`

          - `sample: Hash[Symbol, untyped]`

        - `type: :file_content`

          The type of jsonl source. Always `file_content`.

          - `:file_content`

      - `class FileID`

        - `id: String`

          The identifier of the file.

        - `type: :file_id`

          The type of jsonl source. Always `file_id`.

          - `:file_id`

    - `type: :jsonl`

      The type of data source. Always `jsonl`.

      - `:jsonl`

  - `class CreateEvalCompletionsRunDataSource`

    A CompletionsRunDataSource object describing a model sampling configuration.

    - `source: { content, type} | { id, type} | { type, created_after, created_before, 3 more}`

      Determines what populates the `item` namespace in this run's data source.

      - `class FileContent`

        - `content: Array[{ item, sample}]`

          The content of the jsonl file.

          - `item: Hash[Symbol, untyped]`

          - `sample: Hash[Symbol, untyped]`

        - `type: :file_content`

          The type of jsonl source. Always `file_content`.

          - `:file_content`

      - `class FileID`

        - `id: String`

          The identifier of the file.

        - `type: :file_id`

          The type of jsonl source. Always `file_id`.

          - `:file_id`

      - `class StoredCompletions`

        A StoredCompletionsRunDataSource configuration describing a set of filters

        - `type: :stored_completions`

          The type of source. Always `stored_completions`.

          - `:stored_completions`

        - `created_after: Integer`

          An optional Unix timestamp to filter items created after this time.

        - `created_before: Integer`

          An optional Unix timestamp to filter items created before this time.

        - `limit: Integer`

          An optional maximum number of items to return.

        - `metadata: Metadata`

          Set of 16 key-value pairs that can be attached to an object. This can be
          useful for storing additional information about the object in a structured
          format, and querying for objects via API or the dashboard.

          Keys are strings with a maximum length of 64 characters. Values are strings
          with a maximum length of 512 characters.

        - `model: String`

          An optional model to filter by (e.g., 'gpt-4o').

    - `type: :completions`

      The type of run data source. Always `completions`.

      - `:completions`

    - `input_messages: { template, type} | { item_reference, type}`

      Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

      - `class Template`

        - `template: Array[EasyInputMessage | { content, role, type}]`

          A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

          - `class EasyInputMessage`

            A message input to the model with a role indicating instruction following
            hierarchy. Instructions given with the `developer` or `system` role take
            precedence over instructions given with the `user` role. Messages with the
            `assistant` role are presumed to have been generated by the model in previous
            interactions.

            - `content: String | ResponseInputMessageContentList`

              Text, image, or audio input to the model, used to generate a response.
              Can also contain previous assistant responses.

              - `String`

                A text input to the model.

              - `Array[ResponseInputContent]`

                A list of one or many input items to the model, containing different content
                types.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class ResponseInputImage`

                  An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                  - `detail: :low | :high | :auto | :original`

                    The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                    - `:low`

                    - `:high`

                    - `:auto`

                    - `:original`

                  - `type: :input_image`

                    The type of the input item. Always `input_image`.

                    - `:input_image`

                  - `file_id: String`

                    The ID of the file to be sent to the model.

                  - `image_url: String`

                    The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                - `class ResponseInputFile`

                  A file input to the model.

                  - `type: :input_file`

                    The type of the input item. Always `input_file`.

                    - `:input_file`

                  - `file_data: String`

                    The content of the file to be sent to the model.

                  - `file_id: String`

                    The ID of the file to be sent to the model.

                  - `file_url: String`

                    The URL of the file to be sent to the model.

                  - `filename: String`

                    The name of the file to be sent to the model.

            - `role: :user | :assistant | :system | :developer`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `:user`

              - `:assistant`

              - `:system`

              - `:developer`

            - `phase: :commentary | :final_answer`

              Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
              For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
              phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

              - `:commentary`

              - `:final_answer`

            - `type: :message`

              The type of the message input. Always `message`.

              - `:message`

          - `class EvalItem`

            A message input to the model with a role indicating instruction following
            hierarchy. Instructions given with the `developer` or `system` role take
            precedence over instructions given with the `user` role. Messages with the
            `assistant` role are presumed to have been generated by the model in previous
            interactions.

            - `content: String | ResponseInputText | { text, type} | 3 more`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `String`

                A text input to the model.

              - `class ResponseInputText`

                A text input to the model.

                - `text: String`

                  The text input to the model.

                - `type: :input_text`

                  The type of the input item. Always `input_text`.

                  - `:input_text`

              - `class OutputText`

                A text output from the model.

                - `text: String`

                  The text output from the model.

                - `type: :output_text`

                  The type of the output text. Always `output_text`.

                  - `:output_text`

              - `class InputImage`

                An image input block used within EvalItem content arrays.

                - `image_url: String`

                  The URL of the image input.

                - `type: :input_image`

                  The type of the image input. Always `input_image`.

                  - `:input_image`

                - `detail: String`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `class ResponseInputAudio`

                An audio input to the model.

                - `input_audio: { data, format_}`

                  - `data: String`

                    Base64-encoded audio data.

                  - `format_: :mp3 | :wav`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `:mp3`

                    - `:wav`

                - `type: :input_audio`

                  The type of the input item. Always `input_audio`.

                  - `:input_audio`

              - `Array[GraderInputItem]`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

            - `role: :user | :assistant | :system | :developer`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `:user`

              - `:assistant`

              - `:system`

              - `:developer`

            - `type: :message`

              The type of the message input. Always `message`.

              - `:message`

        - `type: :template`

          The type of input messages. Always `template`.

          - `:template`

      - `class ItemReference`

        - `item_reference: String`

          A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

        - `type: :item_reference`

          The type of input messages. Always `item_reference`.

          - `:item_reference`

    - `model: String`

      The name of the model to use for generating completions (e.g. "o3-mini").

    - `sampling_params: { max_completion_tokens, reasoning_effort, response_format, 4 more}`

      - `max_completion_tokens: Integer`

        The maximum number of tokens in the generated output.

      - `reasoning_effort: ReasoningEffort`

        Constrains effort on reasoning for
        [reasoning models](https://platform.openai.com/docs/guides/reasoning).
        Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
        reasoning effort can result in faster responses and fewer tokens used
        on reasoning in a response.

        - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
        - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
        - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
        - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

      - `response_format: ResponseFormatText | ResponseFormatJSONSchema | ResponseFormatJSONObject`

        An object specifying the format that the model must output.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
        Structured Outputs which ensures the model will match your supplied JSON
        schema. Learn more in the [Structured Outputs
        guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables the older JSON mode, which
        ensures the message the model generates is valid JSON. Using `json_schema`
        is preferred for models that support it.

        - `class ResponseFormatText`

          Default response format. Used to generate text responses.

          - `type: :text`

            The type of response format being defined. Always `text`.

            - `:text`

        - `class ResponseFormatJSONSchema`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `json_schema: { name, description, schema, strict}`

            Structured Outputs configuration options, including a JSON Schema.

            - `name: String`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `description: String`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `schema: Hash[Symbol, untyped]`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `strict: bool`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `type: :json_schema`

            The type of response format being defined. Always `json_schema`.

            - `:json_schema`

        - `class ResponseFormatJSONObject`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `type: :json_object`

            The type of response format being defined. Always `json_object`.

            - `:json_object`

      - `seed: Integer`

        A seed value to initialize the randomness, during sampling.

      - `temperature: Float`

        A higher temperature increases randomness in the outputs.

      - `tools: Array[ChatCompletionFunctionTool]`

        A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

        - `function: FunctionDefinition`

          - `name: String`

            The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

          - `description: String`

            A description of what the function does, used by the model to choose when and how to call the function.

          - `parameters: FunctionParameters`

            The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

            Omitting `parameters` defines a function with an empty parameter list.

          - `strict: bool`

            Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

        - `type: :function`

          The type of the tool. Currently, only `function` is supported.

          - `:function`

      - `top_p: Float`

        An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `class CreateEvalResponsesRunDataSource`

    A ResponsesRunDataSource object describing a model sampling configuration.

    - `source: { content, type} | { id, type} | { type, created_after, created_before, 8 more}`

      Determines what populates the `item` namespace in this run's data source.

      - `class FileContent`

        - `content: Array[{ item, sample}]`

          The content of the jsonl file.

          - `item: Hash[Symbol, untyped]`

          - `sample: Hash[Symbol, untyped]`

        - `type: :file_content`

          The type of jsonl source. Always `file_content`.

          - `:file_content`

      - `class FileID`

        - `id: String`

          The identifier of the file.

        - `type: :file_id`

          The type of jsonl source. Always `file_id`.

          - `:file_id`

      - `class Responses`

        A EvalResponsesSource object describing a run data source configuration.

        - `type: :responses`

          The type of run data source. Always `responses`.

          - `:responses`

        - `created_after: Integer`

          Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

        - `created_before: Integer`

          Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

        - `instructions_search: String`

          Optional string to search the 'instructions' field. This is a query parameter used to select responses.

        - `metadata: untyped`

          Metadata filter for the responses. This is a query parameter used to select responses.

        - `model: String`

          The name of the model to find responses for. This is a query parameter used to select responses.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `temperature: Float`

          Sampling temperature. This is a query parameter used to select responses.

        - `tools: Array[String]`

          List of tool names. This is a query parameter used to select responses.

        - `top_p: Float`

          Nucleus sampling parameter. This is a query parameter used to select responses.

        - `users: Array[String]`

          List of user identifiers. This is a query parameter used to select responses.

    - `type: :responses`

      The type of run data source. Always `responses`.

      - `:responses`

    - `input_messages: { template, type} | { item_reference, type}`

      Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

      - `class Template`

        - `template: Array[{ content, role} | { content, role, type}]`

          A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

          - `class ChatMessage`

            - `content: String`

              The content of the message.

            - `role: String`

              The role of the message (e.g. "system", "assistant", "user").

          - `class EvalItem`

            A message input to the model with a role indicating instruction following
            hierarchy. Instructions given with the `developer` or `system` role take
            precedence over instructions given with the `user` role. Messages with the
            `assistant` role are presumed to have been generated by the model in previous
            interactions.

            - `content: String | ResponseInputText | { text, type} | 3 more`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `String`

                A text input to the model.

              - `class ResponseInputText`

                A text input to the model.

                - `text: String`

                  The text input to the model.

                - `type: :input_text`

                  The type of the input item. Always `input_text`.

                  - `:input_text`

              - `class OutputText`

                A text output from the model.

                - `text: String`

                  The text output from the model.

                - `type: :output_text`

                  The type of the output text. Always `output_text`.

                  - `:output_text`

              - `class InputImage`

                An image input block used within EvalItem content arrays.

                - `image_url: String`

                  The URL of the image input.

                - `type: :input_image`

                  The type of the image input. Always `input_image`.

                  - `:input_image`

                - `detail: String`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `class ResponseInputAudio`

                An audio input to the model.

                - `input_audio: { data, format_}`

                  - `data: String`

                    Base64-encoded audio data.

                  - `format_: :mp3 | :wav`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `:mp3`

                    - `:wav`

                - `type: :input_audio`

                  The type of the input item. Always `input_audio`.

                  - `:input_audio`

              - `Array[GraderInputItem]`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

            - `role: :user | :assistant | :system | :developer`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `:user`

              - `:assistant`

              - `:system`

              - `:developer`

            - `type: :message`

              The type of the message input. Always `message`.

              - `:message`

        - `type: :template`

          The type of input messages. Always `template`.

          - `:template`

      - `class ItemReference`

        - `item_reference: String`

          A reference to a variable in the `item` namespace. Ie, "item.name"

        - `type: :item_reference`

          The type of input messages. Always `item_reference`.

          - `:item_reference`

    - `model: String`

      The name of the model to use for generating completions (e.g. "o3-mini").

    - `sampling_params: { max_completion_tokens, reasoning_effort, seed, 4 more}`

      - `max_completion_tokens: Integer`

        The maximum number of tokens in the generated output.

      - `reasoning_effort: ReasoningEffort`

        Constrains effort on reasoning for
        [reasoning models](https://platform.openai.com/docs/guides/reasoning).
        Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
        reasoning effort can result in faster responses and fewer tokens used
        on reasoning in a response.

        - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
        - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
        - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
        - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

      - `seed: Integer`

        A seed value to initialize the randomness, during sampling.

      - `temperature: Float`

        A higher temperature increases randomness in the outputs.

      - `text: { format_}`

        Configuration options for a text response from the model. Can be plain
        text or structured JSON data. Learn more:

        - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
        - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

        - `format_: ResponseFormatTextConfig`

          An object specifying the format that the model must output.

          Configuring `{ "type": "json_schema" }` enables Structured Outputs,
          which ensures the model will match your supplied JSON schema. Learn more in the
          [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

          The default format is `{ "type": "text" }` with no additional options.

          **Not recommended for gpt-4o and newer models:**

          Setting to `{ "type": "json_object" }` enables the older JSON mode, which
          ensures the message the model generates is valid JSON. Using `json_schema`
          is preferred for models that support it.

          - `class ResponseFormatText`

            Default response format. Used to generate text responses.

            - `type: :text`

              The type of response format being defined. Always `text`.

              - `:text`

          - `class ResponseFormatTextJSONSchemaConfig`

            JSON Schema response format. Used to generate structured JSON responses.
            Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

            - `name: String`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `schema: Hash[Symbol, untyped]`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `type: :json_schema`

              The type of response format being defined. Always `json_schema`.

              - `:json_schema`

            - `description: String`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `strict: bool`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `class ResponseFormatJSONObject`

            JSON object response format. An older method of generating JSON responses.
            Using `json_schema` is recommended for models that support it. Note that the
            model will not generate JSON without a system or user message instructing it
            to do so.

            - `type: :json_object`

              The type of response format being defined. Always `json_object`.

              - `:json_object`

      - `tools: Array[Tool]`

        An array of tools the model may call while generating a response. You
        can specify which tool to use by setting the `tool_choice` parameter.

        The two categories of tools you can provide the model are:

        - **Built-in tools**: Tools that are provided by OpenAI that extend the
          model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
          or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
          [built-in tools](https://platform.openai.com/docs/guides/tools).
        - **Function calls (custom tools)**: Functions that are defined by you,
          enabling the model to call your own code. Learn more about
          [function calling](https://platform.openai.com/docs/guides/function-calling).

        - `class FunctionTool`

          Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

          - `name: String`

            The name of the function to call.

          - `parameters: Hash[Symbol, untyped]`

            A JSON schema object describing the parameters of the function.

          - `strict: bool`

            Whether to enforce strict parameter validation. Default `true`.

          - `type: :function`

            The type of the function tool. Always `function`.

            - `:function`

          - `defer_loading: bool`

            Whether this function is deferred and loaded via tool search.

          - `description: String`

            A description of the function. Used by the model to determine whether or not to call the function.

        - `class FileSearchTool`

          A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

          - `type: :file_search`

            The type of the file search tool. Always `file_search`.

            - `:file_search`

          - `vector_store_ids: Array[String]`

            The IDs of the vector stores to search.

          - `filters: ComparisonFilter | CompoundFilter`

            A filter to apply.

            - `class ComparisonFilter`

              A filter used to compare a specified attribute key to a given value using a defined comparison operation.

              - `key: String`

                The key to compare against the value.

              - `type: :eq | :ne | :gt | 3 more`

                Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                - `eq`: equals
                - `ne`: not equal
                - `gt`: greater than
                - `gte`: greater than or equal
                - `lt`: less than
                - `lte`: less than or equal
                - `in`: in
                - `nin`: not in

                - `:eq`

                - `:ne`

                - `:gt`

                - `:gte`

                - `:lt`

                - `:lte`

              - `value: String | Float | bool | Array[String | Float]`

                The value to compare against the attribute key; supports string, number, or boolean types.

                - `String`

                - `Float`

                - `bool`

                - `Array[String | Float]`

                  - `String`

                  - `Float`

            - `class CompoundFilter`

              Combine multiple filters using `and` or `or`.

              - `filters: Array[ComparisonFilter | untyped]`

                Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                - `class ComparisonFilter`

                  A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                  - `key: String`

                    The key to compare against the value.

                  - `type: :eq | :ne | :gt | 3 more`

                    Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                    - `eq`: equals
                    - `ne`: not equal
                    - `gt`: greater than
                    - `gte`: greater than or equal
                    - `lt`: less than
                    - `lte`: less than or equal
                    - `in`: in
                    - `nin`: not in

                    - `:eq`

                    - `:ne`

                    - `:gt`

                    - `:gte`

                    - `:lt`

                    - `:lte`

                  - `value: String | Float | bool | Array[String | Float]`

                    The value to compare against the attribute key; supports string, number, or boolean types.

                    - `String`

                    - `Float`

                    - `bool`

                    - `Array[String | Float]`

                      - `String`

                      - `Float`

                - `untyped`

              - `type: :and | :or`

                Type of operation: `and` or `or`.

                - `:and`

                - `:or`

          - `max_num_results: Integer`

            The maximum number of results to return. This number should be between 1 and 50 inclusive.

          - `ranking_options: { hybrid_search, ranker, score_threshold}`

            Ranking options for search.

            - `hybrid_search: { embedding_weight, text_weight}`

              Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

              - `embedding_weight: Float`

                The weight of the embedding in the reciprocal ranking fusion.

              - `text_weight: Float`

                The weight of the text in the reciprocal ranking fusion.

            - `ranker: :auto | :"default-2024-11-15"`

              The ranker to use for the file search.

              - `:auto`

              - `:"default-2024-11-15"`

            - `score_threshold: Float`

              The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

        - `class ComputerTool`

          A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

          - `type: :computer`

            The type of the computer tool. Always `computer`.

            - `:computer`

        - `class ComputerUsePreviewTool`

          A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

          - `display_height: Integer`

            The height of the computer display.

          - `display_width: Integer`

            The width of the computer display.

          - `environment: :windows | :mac | :linux | 2 more`

            The type of computer environment to control.

            - `:windows`

            - `:mac`

            - `:linux`

            - `:ubuntu`

            - `:browser`

          - `type: :computer_use_preview`

            The type of the computer use tool. Always `computer_use_preview`.

            - `:computer_use_preview`

        - `class WebSearchTool`

          Search the Internet for sources related to the prompt. Learn more about the
          [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

          - `type: :web_search | :web_search_2025_08_26`

            The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

            - `:web_search`

            - `:web_search_2025_08_26`

          - `filters: { allowed_domains}`

            Filters for the search.

            - `allowed_domains: Array[String]`

              Allowed domains for the search. If not provided, all domains are allowed.
              Subdomains of the provided domains are allowed as well.

              Example: `["pubmed.ncbi.nlm.nih.gov"]`

          - `search_context_size: :low | :medium | :high`

            High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

            - `:low`

            - `:medium`

            - `:high`

          - `user_location: { city, country, region, 2 more}`

            The approximate location of the user.

            - `city: String`

              Free text input for the city of the user, e.g. `San Francisco`.

            - `country: String`

              The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

            - `region: String`

              Free text input for the region of the user, e.g. `California`.

            - `timezone: String`

              The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

            - `type: :approximate`

              The type of location approximation. Always `approximate`.

              - `:approximate`

        - `class Mcp`

          Give the model access to additional tools via remote Model Context Protocol
          (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

          - `server_label: String`

            A label for this MCP server, used to identify it in tool calls.

          - `type: :mcp`

            The type of the MCP tool. Always `mcp`.

            - `:mcp`

          - `allowed_tools: Array[String] | { read_only, tool_names}`

            List of allowed tool names or a filter object.

            - `Array[String]`

              A string array of allowed tool names

            - `class McpToolFilter`

              A filter object to specify which tools are allowed.

              - `read_only: bool`

                Indicates whether or not a tool modifies data or is read-only. If an
                MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                it will match this filter.

              - `tool_names: Array[String]`

                List of allowed tool names.

          - `authorization: String`

            An OAuth access token that can be used with a remote MCP server, either
            with a custom MCP server URL or a service connector. Your application
            must handle the OAuth authorization flow and provide the token here.

          - `connector_id: :connector_dropbox | :connector_gmail | :connector_googlecalendar | 5 more`

            Identifier for service connectors, like those available in ChatGPT. One of
            `server_url` or `connector_id` must be provided. Learn more about service
            connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

            Currently supported `connector_id` values are:

            - Dropbox: `connector_dropbox`
            - Gmail: `connector_gmail`
            - Google Calendar: `connector_googlecalendar`
            - Google Drive: `connector_googledrive`
            - Microsoft Teams: `connector_microsoftteams`
            - Outlook Calendar: `connector_outlookcalendar`
            - Outlook Email: `connector_outlookemail`
            - SharePoint: `connector_sharepoint`

            - `:connector_dropbox`

            - `:connector_gmail`

            - `:connector_googlecalendar`

            - `:connector_googledrive`

            - `:connector_microsoftteams`

            - `:connector_outlookcalendar`

            - `:connector_outlookemail`

            - `:connector_sharepoint`

          - `defer_loading: bool`

            Whether this MCP tool is deferred and discovered via tool search.

          - `headers: Hash[Symbol, String]`

            Optional HTTP headers to send to the MCP server. Use for authentication
            or other purposes.

          - `require_approval: { always, never} | :always | :never`

            Specify which of the MCP server's tools require approval.

            - `class McpToolApprovalFilter`

              Specify which of the MCP server's tools require approval. Can be
              `always`, `never`, or a filter object associated with tools
              that require approval.

              - `always: { read_only, tool_names}`

                A filter object to specify which tools are allowed.

                - `read_only: bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `tool_names: Array[String]`

                  List of allowed tool names.

              - `never: { read_only, tool_names}`

                A filter object to specify which tools are allowed.

                - `read_only: bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `tool_names: Array[String]`

                  List of allowed tool names.

            - `McpToolApprovalSetting = :always | :never`

              Specify a single approval policy for all tools. One of `always` or
              `never`. When set to `always`, all tools will require approval. When
              set to `never`, all tools will not require approval.

              - `:always`

              - `:never`

          - `server_description: String`

            Optional description of the MCP server, used to provide more context.

          - `server_url: String`

            The URL for the MCP server. One of `server_url` or `connector_id` must be
            provided.

        - `class CodeInterpreter`

          A tool that runs Python code to help generate a response to a prompt.

          - `container: String | { type, file_ids, memory_limit, network_policy}`

            The code interpreter container. Can be a container ID or an object that
            specifies uploaded file IDs to make available to your code, along with an
            optional `memory_limit` setting.

            - `String`

              The container ID.

            - `class CodeInterpreterToolAuto`

              Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

              - `type: :auto`

                Always `auto`.

                - `:auto`

              - `file_ids: Array[String]`

                An optional list of uploaded files to make available to your code.

              - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                The memory limit for the code interpreter container.

                - `:"1g"`

                - `:"4g"`

                - `:"16g"`

                - `:"64g"`

              - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                Network access policy for the container.

                - `class ContainerNetworkPolicyDisabled`

                  - `type: :disabled`

                    Disable outbound network access. Always `disabled`.

                    - `:disabled`

                - `class ContainerNetworkPolicyAllowlist`

                  - `allowed_domains: Array[String]`

                    A list of allowed domains when type is `allowlist`.

                  - `type: :allowlist`

                    Allow outbound network access only to specified domains. Always `allowlist`.

                    - `:allowlist`

                  - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                    Optional domain-scoped secrets for allowlisted domains.

                    - `domain: String`

                      The domain associated with the secret.

                    - `name: String`

                      The name of the secret to inject for the domain.

                    - `value: String`

                      The secret value to inject for the domain.

          - `type: :code_interpreter`

            The type of the code interpreter tool. Always `code_interpreter`.

            - `:code_interpreter`

        - `class ImageGeneration`

          A tool that generates images using the GPT image models.

          - `type: :image_generation`

            The type of the image generation tool. Always `image_generation`.

            - `:image_generation`

          - `action: :generate | :edit | :auto`

            Whether to generate a new image or edit an existing image. Default: `auto`.

            - `:generate`

            - `:edit`

            - `:auto`

          - `background: :transparent | :opaque | :auto`

            Background type for the generated image. One of `transparent`,
            `opaque`, or `auto`. Default: `auto`.

            - `:transparent`

            - `:opaque`

            - `:auto`

          - `input_fidelity: :high | :low`

            Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

            - `:high`

            - `:low`

          - `input_image_mask: { file_id, image_url}`

            Optional mask for inpainting. Contains `image_url`
            (string, optional) and `file_id` (string, optional).

            - `file_id: String`

              File ID for the mask image.

            - `image_url: String`

              Base64-encoded mask image.

          - `model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

            The image generation model to use. Default: `gpt-image-1`.

            - `String`

            - `:"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

              The image generation model to use. Default: `gpt-image-1`.

              - `:"gpt-image-1"`

              - `:"gpt-image-1-mini"`

              - `:"gpt-image-1.5"`

          - `moderation: :auto | :low`

            Moderation level for the generated image. Default: `auto`.

            - `:auto`

            - `:low`

          - `output_compression: Integer`

            Compression level for the output image. Default: 100.

          - `output_format: :png | :webp | :jpeg`

            The output format of the generated image. One of `png`, `webp`, or
            `jpeg`. Default: `png`.

            - `:png`

            - `:webp`

            - `:jpeg`

          - `partial_images: Integer`

            Number of partial images to generate in streaming mode, from 0 (default value) to 3.

          - `quality: :low | :medium | :high | :auto`

            The quality of the generated image. One of `low`, `medium`, `high`,
            or `auto`. Default: `auto`.

            - `:low`

            - `:medium`

            - `:high`

            - `:auto`

          - `size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto`

            The size of the generated image. One of `1024x1024`, `1024x1536`,
            `1536x1024`, or `auto`. Default: `auto`.

            - `:"1024x1024"`

            - `:"1024x1536"`

            - `:"1536x1024"`

            - `:auto`

        - `class LocalShell`

          A tool that allows the model to execute shell commands in a local environment.

          - `type: :local_shell`

            The type of the local shell tool. Always `local_shell`.

            - `:local_shell`

        - `class FunctionShellTool`

          A tool that allows the model to execute shell commands.

          - `type: :shell`

            The type of the shell tool. Always `shell`.

            - `:shell`

          - `environment: ContainerAuto | LocalEnvironment | ContainerReference`

            - `class ContainerAuto`

              - `type: :container_auto`

                Automatically creates a container for this request

                - `:container_auto`

              - `file_ids: Array[String]`

                An optional list of uploaded files to make available to your code.

              - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                The memory limit for the container.

                - `:"1g"`

                - `:"4g"`

                - `:"16g"`

                - `:"64g"`

              - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                Network access policy for the container.

                - `class ContainerNetworkPolicyDisabled`

                  - `type: :disabled`

                    Disable outbound network access. Always `disabled`.

                    - `:disabled`

                - `class ContainerNetworkPolicyAllowlist`

                  - `allowed_domains: Array[String]`

                    A list of allowed domains when type is `allowlist`.

                  - `type: :allowlist`

                    Allow outbound network access only to specified domains. Always `allowlist`.

                    - `:allowlist`

                  - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                    Optional domain-scoped secrets for allowlisted domains.

                    - `domain: String`

                      The domain associated with the secret.

                    - `name: String`

                      The name of the secret to inject for the domain.

                    - `value: String`

                      The secret value to inject for the domain.

              - `skills: Array[SkillReference | InlineSkill]`

                An optional list of skills referenced by id or inline data.

                - `class SkillReference`

                  - `skill_id: String`

                    The ID of the referenced skill.

                  - `type: :skill_reference`

                    References a skill created with the /v1/skills endpoint.

                    - `:skill_reference`

                  - `version: String`

                    Optional skill version. Use a positive integer or 'latest'. Omit for default.

                - `class InlineSkill`

                  - `description: String`

                    The description of the skill.

                  - `name: String`

                    The name of the skill.

                  - `source: InlineSkillSource`

                    Inline skill payload

                    - `data: String`

                      Base64-encoded skill zip bundle.

                    - `media_type: :"application/zip"`

                      The media type of the inline skill payload. Must be `application/zip`.

                      - `:"application/zip"`

                    - `type: :base64`

                      The type of the inline skill source. Must be `base64`.

                      - `:base64`

                  - `type: :inline`

                    Defines an inline skill for this request.

                    - `:inline`

            - `class LocalEnvironment`

              - `type: :local`

                Use a local computer environment.

                - `:local`

              - `skills: Array[LocalSkill]`

                An optional list of skills.

                - `description: String`

                  The description of the skill.

                - `name: String`

                  The name of the skill.

                - `path: String`

                  The path to the directory containing the skill.

            - `class ContainerReference`

              - `container_id: String`

                The ID of the referenced container.

              - `type: :container_reference`

                References a container created with the /v1/containers endpoint

                - `:container_reference`

        - `class CustomTool`

          A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

          - `name: String`

            The name of the custom tool, used to identify it in tool calls.

          - `type: :custom`

            The type of the custom tool. Always `custom`.

            - `:custom`

          - `defer_loading: bool`

            Whether this tool should be deferred and discovered via tool search.

          - `description: String`

            Optional description of the custom tool, used to provide more context.

          - `format_: CustomToolInputFormat`

            The input format for the custom tool. Default is unconstrained text.

            - `class Text`

              Unconstrained free-form text.

              - `type: :text`

                Unconstrained text format. Always `text`.

                - `:text`

            - `class Grammar`

              A grammar defined by the user.

              - `definition: String`

                The grammar definition.

              - `syntax: :lark | :regex`

                The syntax of the grammar definition. One of `lark` or `regex`.

                - `:lark`

                - `:regex`

              - `type: :grammar`

                Grammar format. Always `grammar`.

                - `:grammar`

        - `class NamespaceTool`

          Groups function/custom tools under a shared namespace.

          - `description: String`

            A description of the namespace shown to the model.

          - `name: String`

            The namespace name used in tool calls (for example, `crm`).

          - `tools: Array[{ name, type, defer_loading, 3 more} | CustomTool]`

            The function/custom tools available inside this namespace.

            - `class Function`

              - `name: String`

              - `type: :function`

                - `:function`

              - `defer_loading: bool`

                Whether this function should be deferred and discovered via tool search.

              - `description: String`

              - `parameters: untyped`

              - `strict: bool`

            - `class CustomTool`

              A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

              - `name: String`

                The name of the custom tool, used to identify it in tool calls.

              - `type: :custom`

                The type of the custom tool. Always `custom`.

                - `:custom`

              - `defer_loading: bool`

                Whether this tool should be deferred and discovered via tool search.

              - `description: String`

                Optional description of the custom tool, used to provide more context.

              - `format_: CustomToolInputFormat`

                The input format for the custom tool. Default is unconstrained text.

                - `class Text`

                  Unconstrained free-form text.

                  - `type: :text`

                    Unconstrained text format. Always `text`.

                    - `:text`

                - `class Grammar`

                  A grammar defined by the user.

                  - `definition: String`

                    The grammar definition.

                  - `syntax: :lark | :regex`

                    The syntax of the grammar definition. One of `lark` or `regex`.

                    - `:lark`

                    - `:regex`

                  - `type: :grammar`

                    Grammar format. Always `grammar`.

                    - `:grammar`

          - `type: :namespace`

            The type of the tool. Always `namespace`.

            - `:namespace`

        - `class ToolSearchTool`

          Hosted or BYOT tool search configuration for deferred tools.

          - `type: :tool_search`

            The type of the tool. Always `tool_search`.

            - `:tool_search`

          - `description: String`

            Description shown to the model for a client-executed tool search tool.

          - `execution: :server | :client`

            Whether tool search is executed by the server or by the client.

            - `:server`

            - `:client`

          - `parameters: untyped`

            Parameter schema for a client-executed tool search tool.

        - `class WebSearchPreviewTool`

          This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

          - `type: :web_search_preview | :web_search_preview_2025_03_11`

            The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

            - `:web_search_preview`

            - `:web_search_preview_2025_03_11`

          - `search_content_types: Array[:text | :image]`

            - `:text`

            - `:image`

          - `search_context_size: :low | :medium | :high`

            High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

            - `:low`

            - `:medium`

            - `:high`

          - `user_location: { type, city, country, 2 more}`

            The user's location.

            - `type: :approximate`

              The type of location approximation. Always `approximate`.

              - `:approximate`

            - `city: String`

              Free text input for the city of the user, e.g. `San Francisco`.

            - `country: String`

              The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

            - `region: String`

              Free text input for the region of the user, e.g. `California`.

            - `timezone: String`

              The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

        - `class ApplyPatchTool`

          Allows the assistant to create, delete, or update files using unified diffs.

          - `type: :apply_patch`

            The type of the tool. Always `apply_patch`.

            - `:apply_patch`

      - `top_p: Float`

        An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `name: String`

  The name of the run.

#### Returns

- `class RunCreateResponse`

  A schema representing an evaluation run.

  - `id: String`

    Unique identifier for the evaluation run.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `data_source: CreateEvalJSONLRunDataSource | CreateEvalCompletionsRunDataSource | { source, type, input_messages, 2 more}`

    Information about the run's data source.

    - `class CreateEvalJSONLRunDataSource`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `source: { content, type} | { id, type}`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

      - `type: :jsonl`

        The type of data source. Always `jsonl`.

        - `:jsonl`

    - `class CreateEvalCompletionsRunDataSource`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 3 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class StoredCompletions`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `type: :stored_completions`

            The type of source. Always `stored_completions`.

            - `:stored_completions`

          - `created_after: Integer`

            An optional Unix timestamp to filter items created after this time.

          - `created_before: Integer`

            An optional Unix timestamp to filter items created before this time.

          - `limit: Integer`

            An optional maximum number of items to return.

          - `metadata: Metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `model: String`

            An optional model to filter by (e.g., 'gpt-4o').

      - `type: :completions`

        The type of run data source. Always `completions`.

        - `:completions`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[EasyInputMessage | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputMessageContentList`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                  A text input to the model.

                - `Array[ResponseInputContent]`

                  A list of one or many input items to the model, containing different content
                  types.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class ResponseInputImage`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `detail: :low | :high | :auto | :original`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `:low`

                      - `:high`

                      - `:auto`

                      - `:original`

                    - `type: :input_image`

                      The type of the input item. Always `input_image`.

                      - `:input_image`

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `image_url: String`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile`

                    A file input to the model.

                    - `type: :input_file`

                      The type of the input item. Always `input_file`.

                      - `:input_file`

                    - `file_data: String`

                      The content of the file to be sent to the model.

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `file_url: String`

                      The URL of the file to be sent to the model.

                    - `filename: String`

                      The name of the file to be sent to the model.

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `phase: :commentary | :final_answer`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `:commentary`

                - `:final_answer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, response_format, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `response_format: ResponseFormatText | ResponseFormatJSONSchema | ResponseFormatJSONObject`

          An object specifying the format that the model must output.

          Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
          Structured Outputs which ensures the model will match your supplied JSON
          schema. Learn more in the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

          Setting to `{ "type": "json_object" }` enables the older JSON mode, which
          ensures the message the model generates is valid JSON. Using `json_schema`
          is preferred for models that support it.

          - `class ResponseFormatText`

            Default response format. Used to generate text responses.

            - `type: :text`

              The type of response format being defined. Always `text`.

              - `:text`

          - `class ResponseFormatJSONSchema`

            JSON Schema response format. Used to generate structured JSON responses.
            Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

            - `json_schema: { name, description, schema, strict}`

              Structured Outputs configuration options, including a JSON Schema.

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `type: :json_schema`

              The type of response format being defined. Always `json_schema`.

              - `:json_schema`

          - `class ResponseFormatJSONObject`

            JSON object response format. An older method of generating JSON responses.
            Using `json_schema` is recommended for models that support it. Note that the
            model will not generate JSON without a system or user message instructing it
            to do so.

            - `type: :json_object`

              The type of response format being defined. Always `json_object`.

              - `:json_object`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `tools: Array[ChatCompletionFunctionTool]`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

          - `function: FunctionDefinition`

            - `name: String`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `description: String`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `parameters: FunctionParameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `strict: bool`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `type: :function`

            The type of the tool. Currently, only `function` is supported.

            - `:function`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 8 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class Responses`

          A EvalResponsesSource object describing a run data source configuration.

          - `type: :responses`

            The type of run data source. Always `responses`.

            - `:responses`

          - `created_after: Integer`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `created_before: Integer`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `instructions_search: String`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `metadata: untyped`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `model: String`

            The name of the model to find responses for. This is a query parameter used to select responses.

          - `reasoning_effort: ReasoningEffort`

            Constrains effort on reasoning for
            [reasoning models](https://platform.openai.com/docs/guides/reasoning).
            Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
            reasoning effort can result in faster responses and fewer tokens used
            on reasoning in a response.

            - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
            - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
            - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
            - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

            - `:none`

            - `:minimal`

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

          - `temperature: Float`

            Sampling temperature. This is a query parameter used to select responses.

          - `tools: Array[String]`

            List of tool names. This is a query parameter used to select responses.

          - `top_p: Float`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `users: Array[String]`

            List of user identifiers. This is a query parameter used to select responses.

      - `type: :responses`

        The type of run data source. Always `responses`.

        - `:responses`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[{ content, role} | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage`

              - `content: String`

                The content of the message.

              - `role: String`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, seed, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `text: { format_}`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `format_: ResponseFormatTextConfig`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText`

              Default response format. Used to generate text responses.

              - `type: :text`

                The type of response format being defined. Always `text`.

                - `:text`

            - `class ResponseFormatTextJSONSchemaConfig`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `type: :json_schema`

                The type of response format being defined. Always `json_schema`.

                - `:json_schema`

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJSONObject`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `type: :json_object`

                The type of response format being defined. Always `json_object`.

                - `:json_object`

        - `tools: Array[Tool]`

          An array of tools the model may call while generating a response. You
          can specify which tool to use by setting the `tool_choice` parameter.

          The two categories of tools you can provide the model are:

          - **Built-in tools**: Tools that are provided by OpenAI that extend the
            model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
            or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
            [built-in tools](https://platform.openai.com/docs/guides/tools).
          - **Function calls (custom tools)**: Functions that are defined by you,
            enabling the model to call your own code. Learn more about
            [function calling](https://platform.openai.com/docs/guides/function-calling).

          - `class FunctionTool`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `name: String`

              The name of the function to call.

            - `parameters: Hash[Symbol, untyped]`

              A JSON schema object describing the parameters of the function.

            - `strict: bool`

              Whether to enforce strict parameter validation. Default `true`.

            - `type: :function`

              The type of the function tool. Always `function`.

              - `:function`

            - `defer_loading: bool`

              Whether this function is deferred and loaded via tool search.

            - `description: String`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `type: :file_search`

              The type of the file search tool. Always `file_search`.

              - `:file_search`

            - `vector_store_ids: Array[String]`

              The IDs of the vector stores to search.

            - `filters: ComparisonFilter | CompoundFilter`

              A filter to apply.

              - `class ComparisonFilter`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `key: String`

                  The key to compare against the value.

                - `type: :eq | :ne | :gt | 3 more`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `:eq`

                  - `:ne`

                  - `:gt`

                  - `:gte`

                  - `:lt`

                  - `:lte`

                - `value: String | Float | bool | Array[String | Float]`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `Float`

                  - `bool`

                  - `Array[String | Float]`

                    - `String`

                    - `Float`

              - `class CompoundFilter`

                Combine multiple filters using `and` or `or`.

                - `filters: Array[ComparisonFilter | untyped]`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `key: String`

                      The key to compare against the value.

                    - `type: :eq | :ne | :gt | 3 more`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `:eq`

                      - `:ne`

                      - `:gt`

                      - `:gte`

                      - `:lt`

                      - `:lte`

                    - `value: String | Float | bool | Array[String | Float]`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `Float`

                      - `bool`

                      - `Array[String | Float]`

                        - `String`

                        - `Float`

                  - `untyped`

                - `type: :and | :or`

                  Type of operation: `and` or `or`.

                  - `:and`

                  - `:or`

            - `max_num_results: Integer`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `ranking_options: { hybrid_search, ranker, score_threshold}`

              Ranking options for search.

              - `hybrid_search: { embedding_weight, text_weight}`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `embedding_weight: Float`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `text_weight: Float`

                  The weight of the text in the reciprocal ranking fusion.

              - `ranker: :auto | :"default-2024-11-15"`

                The ranker to use for the file search.

                - `:auto`

                - `:"default-2024-11-15"`

              - `score_threshold: Float`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `type: :computer`

              The type of the computer tool. Always `computer`.

              - `:computer`

          - `class ComputerUsePreviewTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `display_height: Integer`

              The height of the computer display.

            - `display_width: Integer`

              The width of the computer display.

            - `environment: :windows | :mac | :linux | 2 more`

              The type of computer environment to control.

              - `:windows`

              - `:mac`

              - `:linux`

              - `:ubuntu`

              - `:browser`

            - `type: :computer_use_preview`

              The type of the computer use tool. Always `computer_use_preview`.

              - `:computer_use_preview`

          - `class WebSearchTool`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search | :web_search_2025_08_26`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `:web_search`

              - `:web_search_2025_08_26`

            - `filters: { allowed_domains}`

              Filters for the search.

              - `allowed_domains: Array[String]`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { city, country, region, 2 more}`

              The approximate location of the user.

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

          - `class Mcp`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

            - `server_label: String`

              A label for this MCP server, used to identify it in tool calls.

            - `type: :mcp`

              The type of the MCP tool. Always `mcp`.

              - `:mcp`

            - `allowed_tools: Array[String] | { read_only, tool_names}`

              List of allowed tool names or a filter object.

              - `Array[String]`

                A string array of allowed tool names

              - `class McpToolFilter`

                A filter object to specify which tools are allowed.

                - `read_only: bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `tool_names: Array[String]`

                  List of allowed tool names.

            - `authorization: String`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `connector_id: :connector_dropbox | :connector_gmail | :connector_googlecalendar | 5 more`

              Identifier for service connectors, like those available in ChatGPT. One of
              `server_url` or `connector_id` must be provided. Learn more about service
              connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

              Currently supported `connector_id` values are:

              - Dropbox: `connector_dropbox`
              - Gmail: `connector_gmail`
              - Google Calendar: `connector_googlecalendar`
              - Google Drive: `connector_googledrive`
              - Microsoft Teams: `connector_microsoftteams`
              - Outlook Calendar: `connector_outlookcalendar`
              - Outlook Email: `connector_outlookemail`
              - SharePoint: `connector_sharepoint`

              - `:connector_dropbox`

              - `:connector_gmail`

              - `:connector_googlecalendar`

              - `:connector_googledrive`

              - `:connector_microsoftteams`

              - `:connector_outlookcalendar`

              - `:connector_outlookemail`

              - `:connector_sharepoint`

            - `defer_loading: bool`

              Whether this MCP tool is deferred and discovered via tool search.

            - `headers: Hash[Symbol, String]`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `require_approval: { always, never} | :always | :never`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `always: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

                - `never: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

              - `McpToolApprovalSetting = :always | :never`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `:always`

                - `:never`

            - `server_description: String`

              Optional description of the MCP server, used to provide more context.

            - `server_url: String`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `class CodeInterpreter`

            A tool that runs Python code to help generate a response to a prompt.

            - `container: String | { type, file_ids, memory_limit, network_policy}`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

                The container ID.

              - `class CodeInterpreterToolAuto`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `type: :auto`

                  Always `auto`.

                  - `:auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the code interpreter container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

            - `type: :code_interpreter`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `:code_interpreter`

          - `class ImageGeneration`

            A tool that generates images using the GPT image models.

            - `type: :image_generation`

              The type of the image generation tool. Always `image_generation`.

              - `:image_generation`

            - `action: :generate | :edit | :auto`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `:generate`

              - `:edit`

              - `:auto`

            - `background: :transparent | :opaque | :auto`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `:transparent`

              - `:opaque`

              - `:auto`

            - `input_fidelity: :high | :low`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `:high`

              - `:low`

            - `input_image_mask: { file_id, image_url}`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `file_id: String`

                File ID for the mask image.

              - `image_url: String`

                Base64-encoded mask image.

            - `model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

              The image generation model to use. Default: `gpt-image-1`.

              - `String`

              - `:"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

                The image generation model to use. Default: `gpt-image-1`.

                - `:"gpt-image-1"`

                - `:"gpt-image-1-mini"`

                - `:"gpt-image-1.5"`

            - `moderation: :auto | :low`

              Moderation level for the generated image. Default: `auto`.

              - `:auto`

              - `:low`

            - `output_compression: Integer`

              Compression level for the output image. Default: 100.

            - `output_format: :png | :webp | :jpeg`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `:png`

              - `:webp`

              - `:jpeg`

            - `partial_images: Integer`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `quality: :low | :medium | :high | :auto`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `:low`

              - `:medium`

              - `:high`

              - `:auto`

            - `size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `:"1024x1024"`

              - `:"1024x1536"`

              - `:"1536x1024"`

              - `:auto`

          - `class LocalShell`

            A tool that allows the model to execute shell commands in a local environment.

            - `type: :local_shell`

              The type of the local shell tool. Always `local_shell`.

              - `:local_shell`

          - `class FunctionShellTool`

            A tool that allows the model to execute shell commands.

            - `type: :shell`

              The type of the shell tool. Always `shell`.

              - `:shell`

            - `environment: ContainerAuto | LocalEnvironment | ContainerReference`

              - `class ContainerAuto`

                - `type: :container_auto`

                  Automatically creates a container for this request

                  - `:container_auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

                - `skills: Array[SkillReference | InlineSkill]`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference`

                    - `skill_id: String`

                      The ID of the referenced skill.

                    - `type: :skill_reference`

                      References a skill created with the /v1/skills endpoint.

                      - `:skill_reference`

                    - `version: String`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill`

                    - `description: String`

                      The description of the skill.

                    - `name: String`

                      The name of the skill.

                    - `source: InlineSkillSource`

                      Inline skill payload

                      - `data: String`

                        Base64-encoded skill zip bundle.

                      - `media_type: :"application/zip"`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `:"application/zip"`

                      - `type: :base64`

                        The type of the inline skill source. Must be `base64`.

                        - `:base64`

                    - `type: :inline`

                      Defines an inline skill for this request.

                      - `:inline`

              - `class LocalEnvironment`

                - `type: :local`

                  Use a local computer environment.

                  - `:local`

                - `skills: Array[LocalSkill]`

                  An optional list of skills.

                  - `description: String`

                    The description of the skill.

                  - `name: String`

                    The name of the skill.

                  - `path: String`

                    The path to the directory containing the skill.

              - `class ContainerReference`

                - `container_id: String`

                  The ID of the referenced container.

                - `type: :container_reference`

                  References a container created with the /v1/containers endpoint

                  - `:container_reference`

          - `class CustomTool`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `name: String`

              The name of the custom tool, used to identify it in tool calls.

            - `type: :custom`

              The type of the custom tool. Always `custom`.

              - `:custom`

            - `defer_loading: bool`

              Whether this tool should be deferred and discovered via tool search.

            - `description: String`

              Optional description of the custom tool, used to provide more context.

            - `format_: CustomToolInputFormat`

              The input format for the custom tool. Default is unconstrained text.

              - `class Text`

                Unconstrained free-form text.

                - `type: :text`

                  Unconstrained text format. Always `text`.

                  - `:text`

              - `class Grammar`

                A grammar defined by the user.

                - `definition: String`

                  The grammar definition.

                - `syntax: :lark | :regex`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `:lark`

                  - `:regex`

                - `type: :grammar`

                  Grammar format. Always `grammar`.

                  - `:grammar`

          - `class NamespaceTool`

            Groups function/custom tools under a shared namespace.

            - `description: String`

              A description of the namespace shown to the model.

            - `name: String`

              The namespace name used in tool calls (for example, `crm`).

            - `tools: Array[{ name, type, defer_loading, 3 more} | CustomTool]`

              The function/custom tools available inside this namespace.

              - `class Function`

                - `name: String`

                - `type: :function`

                  - `:function`

                - `defer_loading: bool`

                  Whether this function should be deferred and discovered via tool search.

                - `description: String`

                - `parameters: untyped`

                - `strict: bool`

              - `class CustomTool`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `name: String`

                  The name of the custom tool, used to identify it in tool calls.

                - `type: :custom`

                  The type of the custom tool. Always `custom`.

                  - `:custom`

                - `defer_loading: bool`

                  Whether this tool should be deferred and discovered via tool search.

                - `description: String`

                  Optional description of the custom tool, used to provide more context.

                - `format_: CustomToolInputFormat`

                  The input format for the custom tool. Default is unconstrained text.

                  - `class Text`

                    Unconstrained free-form text.

                    - `type: :text`

                      Unconstrained text format. Always `text`.

                      - `:text`

                  - `class Grammar`

                    A grammar defined by the user.

                    - `definition: String`

                      The grammar definition.

                    - `syntax: :lark | :regex`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `:lark`

                      - `:regex`

                    - `type: :grammar`

                      Grammar format. Always `grammar`.

                      - `:grammar`

            - `type: :namespace`

              The type of the tool. Always `namespace`.

              - `:namespace`

          - `class ToolSearchTool`

            Hosted or BYOT tool search configuration for deferred tools.

            - `type: :tool_search`

              The type of the tool. Always `tool_search`.

              - `:tool_search`

            - `description: String`

              Description shown to the model for a client-executed tool search tool.

            - `execution: :server | :client`

              Whether tool search is executed by the server or by the client.

              - `:server`

              - `:client`

            - `parameters: untyped`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search_preview | :web_search_preview_2025_03_11`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `:web_search_preview`

              - `:web_search_preview_2025_03_11`

            - `search_content_types: Array[:text | :image]`

              - `:text`

              - `:image`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { type, city, country, 2 more}`

              The user's location.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `type: :apply_patch`

              The type of the tool. Always `apply_patch`.

              - `:apply_patch`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `error: EvalAPIError`

    An object representing an error response from the Eval API.

    - `code: String`

      The error code.

    - `message: String`

      The error message.

  - `eval_id: String`

    The identifier of the associated evaluation.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    The model that is evaluated, if applicable.

  - `name: String`

    The name of the evaluation run.

  - `object: :"eval.run"`

    The type of the object. Always "eval.run".

    - `:"eval.run"`

  - `per_model_usage: Array[{ cached_tokens, completion_tokens, invocation_count, 3 more}]`

    Usage statistics for each model during the evaluation run.

    - `cached_tokens: Integer`

      The number of tokens retrieved from cache.

    - `completion_tokens: Integer`

      The number of completion tokens generated.

    - `invocation_count: Integer`

      The number of invocations.

    - `model_name: String`

      The name of the model.

    - `prompt_tokens: Integer`

      The number of prompt tokens used.

    - `total_tokens: Integer`

      The total number of tokens used.

  - `per_testing_criteria_results: Array[{ failed, passed, testing_criteria}]`

    Results per testing criteria applied during the evaluation run.

    - `failed: Integer`

      Number of tests failed for this criteria.

    - `passed: Integer`

      Number of tests passed for this criteria.

    - `testing_criteria: String`

      A description of the testing criteria.

  - `report_url: String`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `result_counts: { errored, failed, passed, total}`

    Counters summarizing the outcomes of the evaluation run.

    - `errored: Integer`

      Number of output items that resulted in an error.

    - `failed: Integer`

      Number of output items that failed to pass the evaluation.

    - `passed: Integer`

      Number of output items that passed the evaluation.

    - `total: Integer`

      Total number of executed output items.

  - `status: String`

    The status of the evaluation run.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

run = openai.evals.runs.create(
  "eval_id",
  data_source: {source: {content: [{item: {foo: "bar"}}], type: :file_content}, type: :jsonl}
)

puts(run)
```

### Retrieve

`evals.runs.retrieve(run_id, **kwargs) -> RunRetrieveResponse`

**get** `/evals/{eval_id}/runs/{run_id}`

Get an evaluation run by ID.

#### Parameters

- `eval_id: String`

- `run_id: String`

#### Returns

- `class RunRetrieveResponse`

  A schema representing an evaluation run.

  - `id: String`

    Unique identifier for the evaluation run.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `data_source: CreateEvalJSONLRunDataSource | CreateEvalCompletionsRunDataSource | { source, type, input_messages, 2 more}`

    Information about the run's data source.

    - `class CreateEvalJSONLRunDataSource`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `source: { content, type} | { id, type}`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

      - `type: :jsonl`

        The type of data source. Always `jsonl`.

        - `:jsonl`

    - `class CreateEvalCompletionsRunDataSource`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 3 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class StoredCompletions`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `type: :stored_completions`

            The type of source. Always `stored_completions`.

            - `:stored_completions`

          - `created_after: Integer`

            An optional Unix timestamp to filter items created after this time.

          - `created_before: Integer`

            An optional Unix timestamp to filter items created before this time.

          - `limit: Integer`

            An optional maximum number of items to return.

          - `metadata: Metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `model: String`

            An optional model to filter by (e.g., 'gpt-4o').

      - `type: :completions`

        The type of run data source. Always `completions`.

        - `:completions`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[EasyInputMessage | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputMessageContentList`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                  A text input to the model.

                - `Array[ResponseInputContent]`

                  A list of one or many input items to the model, containing different content
                  types.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class ResponseInputImage`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `detail: :low | :high | :auto | :original`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `:low`

                      - `:high`

                      - `:auto`

                      - `:original`

                    - `type: :input_image`

                      The type of the input item. Always `input_image`.

                      - `:input_image`

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `image_url: String`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile`

                    A file input to the model.

                    - `type: :input_file`

                      The type of the input item. Always `input_file`.

                      - `:input_file`

                    - `file_data: String`

                      The content of the file to be sent to the model.

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `file_url: String`

                      The URL of the file to be sent to the model.

                    - `filename: String`

                      The name of the file to be sent to the model.

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `phase: :commentary | :final_answer`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `:commentary`

                - `:final_answer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, response_format, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `response_format: ResponseFormatText | ResponseFormatJSONSchema | ResponseFormatJSONObject`

          An object specifying the format that the model must output.

          Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
          Structured Outputs which ensures the model will match your supplied JSON
          schema. Learn more in the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

          Setting to `{ "type": "json_object" }` enables the older JSON mode, which
          ensures the message the model generates is valid JSON. Using `json_schema`
          is preferred for models that support it.

          - `class ResponseFormatText`

            Default response format. Used to generate text responses.

            - `type: :text`

              The type of response format being defined. Always `text`.

              - `:text`

          - `class ResponseFormatJSONSchema`

            JSON Schema response format. Used to generate structured JSON responses.
            Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

            - `json_schema: { name, description, schema, strict}`

              Structured Outputs configuration options, including a JSON Schema.

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `type: :json_schema`

              The type of response format being defined. Always `json_schema`.

              - `:json_schema`

          - `class ResponseFormatJSONObject`

            JSON object response format. An older method of generating JSON responses.
            Using `json_schema` is recommended for models that support it. Note that the
            model will not generate JSON without a system or user message instructing it
            to do so.

            - `type: :json_object`

              The type of response format being defined. Always `json_object`.

              - `:json_object`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `tools: Array[ChatCompletionFunctionTool]`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

          - `function: FunctionDefinition`

            - `name: String`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `description: String`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `parameters: FunctionParameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `strict: bool`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `type: :function`

            The type of the tool. Currently, only `function` is supported.

            - `:function`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 8 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class Responses`

          A EvalResponsesSource object describing a run data source configuration.

          - `type: :responses`

            The type of run data source. Always `responses`.

            - `:responses`

          - `created_after: Integer`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `created_before: Integer`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `instructions_search: String`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `metadata: untyped`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `model: String`

            The name of the model to find responses for. This is a query parameter used to select responses.

          - `reasoning_effort: ReasoningEffort`

            Constrains effort on reasoning for
            [reasoning models](https://platform.openai.com/docs/guides/reasoning).
            Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
            reasoning effort can result in faster responses and fewer tokens used
            on reasoning in a response.

            - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
            - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
            - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
            - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

            - `:none`

            - `:minimal`

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

          - `temperature: Float`

            Sampling temperature. This is a query parameter used to select responses.

          - `tools: Array[String]`

            List of tool names. This is a query parameter used to select responses.

          - `top_p: Float`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `users: Array[String]`

            List of user identifiers. This is a query parameter used to select responses.

      - `type: :responses`

        The type of run data source. Always `responses`.

        - `:responses`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[{ content, role} | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage`

              - `content: String`

                The content of the message.

              - `role: String`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, seed, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `text: { format_}`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `format_: ResponseFormatTextConfig`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText`

              Default response format. Used to generate text responses.

              - `type: :text`

                The type of response format being defined. Always `text`.

                - `:text`

            - `class ResponseFormatTextJSONSchemaConfig`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `type: :json_schema`

                The type of response format being defined. Always `json_schema`.

                - `:json_schema`

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJSONObject`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `type: :json_object`

                The type of response format being defined. Always `json_object`.

                - `:json_object`

        - `tools: Array[Tool]`

          An array of tools the model may call while generating a response. You
          can specify which tool to use by setting the `tool_choice` parameter.

          The two categories of tools you can provide the model are:

          - **Built-in tools**: Tools that are provided by OpenAI that extend the
            model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
            or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
            [built-in tools](https://platform.openai.com/docs/guides/tools).
          - **Function calls (custom tools)**: Functions that are defined by you,
            enabling the model to call your own code. Learn more about
            [function calling](https://platform.openai.com/docs/guides/function-calling).

          - `class FunctionTool`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `name: String`

              The name of the function to call.

            - `parameters: Hash[Symbol, untyped]`

              A JSON schema object describing the parameters of the function.

            - `strict: bool`

              Whether to enforce strict parameter validation. Default `true`.

            - `type: :function`

              The type of the function tool. Always `function`.

              - `:function`

            - `defer_loading: bool`

              Whether this function is deferred and loaded via tool search.

            - `description: String`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `type: :file_search`

              The type of the file search tool. Always `file_search`.

              - `:file_search`

            - `vector_store_ids: Array[String]`

              The IDs of the vector stores to search.

            - `filters: ComparisonFilter | CompoundFilter`

              A filter to apply.

              - `class ComparisonFilter`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `key: String`

                  The key to compare against the value.

                - `type: :eq | :ne | :gt | 3 more`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `:eq`

                  - `:ne`

                  - `:gt`

                  - `:gte`

                  - `:lt`

                  - `:lte`

                - `value: String | Float | bool | Array[String | Float]`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `Float`

                  - `bool`

                  - `Array[String | Float]`

                    - `String`

                    - `Float`

              - `class CompoundFilter`

                Combine multiple filters using `and` or `or`.

                - `filters: Array[ComparisonFilter | untyped]`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `key: String`

                      The key to compare against the value.

                    - `type: :eq | :ne | :gt | 3 more`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `:eq`

                      - `:ne`

                      - `:gt`

                      - `:gte`

                      - `:lt`

                      - `:lte`

                    - `value: String | Float | bool | Array[String | Float]`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `Float`

                      - `bool`

                      - `Array[String | Float]`

                        - `String`

                        - `Float`

                  - `untyped`

                - `type: :and | :or`

                  Type of operation: `and` or `or`.

                  - `:and`

                  - `:or`

            - `max_num_results: Integer`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `ranking_options: { hybrid_search, ranker, score_threshold}`

              Ranking options for search.

              - `hybrid_search: { embedding_weight, text_weight}`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `embedding_weight: Float`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `text_weight: Float`

                  The weight of the text in the reciprocal ranking fusion.

              - `ranker: :auto | :"default-2024-11-15"`

                The ranker to use for the file search.

                - `:auto`

                - `:"default-2024-11-15"`

              - `score_threshold: Float`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `type: :computer`

              The type of the computer tool. Always `computer`.

              - `:computer`

          - `class ComputerUsePreviewTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `display_height: Integer`

              The height of the computer display.

            - `display_width: Integer`

              The width of the computer display.

            - `environment: :windows | :mac | :linux | 2 more`

              The type of computer environment to control.

              - `:windows`

              - `:mac`

              - `:linux`

              - `:ubuntu`

              - `:browser`

            - `type: :computer_use_preview`

              The type of the computer use tool. Always `computer_use_preview`.

              - `:computer_use_preview`

          - `class WebSearchTool`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search | :web_search_2025_08_26`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `:web_search`

              - `:web_search_2025_08_26`

            - `filters: { allowed_domains}`

              Filters for the search.

              - `allowed_domains: Array[String]`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { city, country, region, 2 more}`

              The approximate location of the user.

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

          - `class Mcp`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

            - `server_label: String`

              A label for this MCP server, used to identify it in tool calls.

            - `type: :mcp`

              The type of the MCP tool. Always `mcp`.

              - `:mcp`

            - `allowed_tools: Array[String] | { read_only, tool_names}`

              List of allowed tool names or a filter object.

              - `Array[String]`

                A string array of allowed tool names

              - `class McpToolFilter`

                A filter object to specify which tools are allowed.

                - `read_only: bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `tool_names: Array[String]`

                  List of allowed tool names.

            - `authorization: String`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `connector_id: :connector_dropbox | :connector_gmail | :connector_googlecalendar | 5 more`

              Identifier for service connectors, like those available in ChatGPT. One of
              `server_url` or `connector_id` must be provided. Learn more about service
              connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

              Currently supported `connector_id` values are:

              - Dropbox: `connector_dropbox`
              - Gmail: `connector_gmail`
              - Google Calendar: `connector_googlecalendar`
              - Google Drive: `connector_googledrive`
              - Microsoft Teams: `connector_microsoftteams`
              - Outlook Calendar: `connector_outlookcalendar`
              - Outlook Email: `connector_outlookemail`
              - SharePoint: `connector_sharepoint`

              - `:connector_dropbox`

              - `:connector_gmail`

              - `:connector_googlecalendar`

              - `:connector_googledrive`

              - `:connector_microsoftteams`

              - `:connector_outlookcalendar`

              - `:connector_outlookemail`

              - `:connector_sharepoint`

            - `defer_loading: bool`

              Whether this MCP tool is deferred and discovered via tool search.

            - `headers: Hash[Symbol, String]`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `require_approval: { always, never} | :always | :never`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `always: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

                - `never: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

              - `McpToolApprovalSetting = :always | :never`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `:always`

                - `:never`

            - `server_description: String`

              Optional description of the MCP server, used to provide more context.

            - `server_url: String`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `class CodeInterpreter`

            A tool that runs Python code to help generate a response to a prompt.

            - `container: String | { type, file_ids, memory_limit, network_policy}`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

                The container ID.

              - `class CodeInterpreterToolAuto`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `type: :auto`

                  Always `auto`.

                  - `:auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the code interpreter container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

            - `type: :code_interpreter`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `:code_interpreter`

          - `class ImageGeneration`

            A tool that generates images using the GPT image models.

            - `type: :image_generation`

              The type of the image generation tool. Always `image_generation`.

              - `:image_generation`

            - `action: :generate | :edit | :auto`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `:generate`

              - `:edit`

              - `:auto`

            - `background: :transparent | :opaque | :auto`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `:transparent`

              - `:opaque`

              - `:auto`

            - `input_fidelity: :high | :low`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `:high`

              - `:low`

            - `input_image_mask: { file_id, image_url}`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `file_id: String`

                File ID for the mask image.

              - `image_url: String`

                Base64-encoded mask image.

            - `model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

              The image generation model to use. Default: `gpt-image-1`.

              - `String`

              - `:"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

                The image generation model to use. Default: `gpt-image-1`.

                - `:"gpt-image-1"`

                - `:"gpt-image-1-mini"`

                - `:"gpt-image-1.5"`

            - `moderation: :auto | :low`

              Moderation level for the generated image. Default: `auto`.

              - `:auto`

              - `:low`

            - `output_compression: Integer`

              Compression level for the output image. Default: 100.

            - `output_format: :png | :webp | :jpeg`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `:png`

              - `:webp`

              - `:jpeg`

            - `partial_images: Integer`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `quality: :low | :medium | :high | :auto`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `:low`

              - `:medium`

              - `:high`

              - `:auto`

            - `size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `:"1024x1024"`

              - `:"1024x1536"`

              - `:"1536x1024"`

              - `:auto`

          - `class LocalShell`

            A tool that allows the model to execute shell commands in a local environment.

            - `type: :local_shell`

              The type of the local shell tool. Always `local_shell`.

              - `:local_shell`

          - `class FunctionShellTool`

            A tool that allows the model to execute shell commands.

            - `type: :shell`

              The type of the shell tool. Always `shell`.

              - `:shell`

            - `environment: ContainerAuto | LocalEnvironment | ContainerReference`

              - `class ContainerAuto`

                - `type: :container_auto`

                  Automatically creates a container for this request

                  - `:container_auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

                - `skills: Array[SkillReference | InlineSkill]`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference`

                    - `skill_id: String`

                      The ID of the referenced skill.

                    - `type: :skill_reference`

                      References a skill created with the /v1/skills endpoint.

                      - `:skill_reference`

                    - `version: String`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill`

                    - `description: String`

                      The description of the skill.

                    - `name: String`

                      The name of the skill.

                    - `source: InlineSkillSource`

                      Inline skill payload

                      - `data: String`

                        Base64-encoded skill zip bundle.

                      - `media_type: :"application/zip"`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `:"application/zip"`

                      - `type: :base64`

                        The type of the inline skill source. Must be `base64`.

                        - `:base64`

                    - `type: :inline`

                      Defines an inline skill for this request.

                      - `:inline`

              - `class LocalEnvironment`

                - `type: :local`

                  Use a local computer environment.

                  - `:local`

                - `skills: Array[LocalSkill]`

                  An optional list of skills.

                  - `description: String`

                    The description of the skill.

                  - `name: String`

                    The name of the skill.

                  - `path: String`

                    The path to the directory containing the skill.

              - `class ContainerReference`

                - `container_id: String`

                  The ID of the referenced container.

                - `type: :container_reference`

                  References a container created with the /v1/containers endpoint

                  - `:container_reference`

          - `class CustomTool`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `name: String`

              The name of the custom tool, used to identify it in tool calls.

            - `type: :custom`

              The type of the custom tool. Always `custom`.

              - `:custom`

            - `defer_loading: bool`

              Whether this tool should be deferred and discovered via tool search.

            - `description: String`

              Optional description of the custom tool, used to provide more context.

            - `format_: CustomToolInputFormat`

              The input format for the custom tool. Default is unconstrained text.

              - `class Text`

                Unconstrained free-form text.

                - `type: :text`

                  Unconstrained text format. Always `text`.

                  - `:text`

              - `class Grammar`

                A grammar defined by the user.

                - `definition: String`

                  The grammar definition.

                - `syntax: :lark | :regex`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `:lark`

                  - `:regex`

                - `type: :grammar`

                  Grammar format. Always `grammar`.

                  - `:grammar`

          - `class NamespaceTool`

            Groups function/custom tools under a shared namespace.

            - `description: String`

              A description of the namespace shown to the model.

            - `name: String`

              The namespace name used in tool calls (for example, `crm`).

            - `tools: Array[{ name, type, defer_loading, 3 more} | CustomTool]`

              The function/custom tools available inside this namespace.

              - `class Function`

                - `name: String`

                - `type: :function`

                  - `:function`

                - `defer_loading: bool`

                  Whether this function should be deferred and discovered via tool search.

                - `description: String`

                - `parameters: untyped`

                - `strict: bool`

              - `class CustomTool`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `name: String`

                  The name of the custom tool, used to identify it in tool calls.

                - `type: :custom`

                  The type of the custom tool. Always `custom`.

                  - `:custom`

                - `defer_loading: bool`

                  Whether this tool should be deferred and discovered via tool search.

                - `description: String`

                  Optional description of the custom tool, used to provide more context.

                - `format_: CustomToolInputFormat`

                  The input format for the custom tool. Default is unconstrained text.

                  - `class Text`

                    Unconstrained free-form text.

                    - `type: :text`

                      Unconstrained text format. Always `text`.

                      - `:text`

                  - `class Grammar`

                    A grammar defined by the user.

                    - `definition: String`

                      The grammar definition.

                    - `syntax: :lark | :regex`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `:lark`

                      - `:regex`

                    - `type: :grammar`

                      Grammar format. Always `grammar`.

                      - `:grammar`

            - `type: :namespace`

              The type of the tool. Always `namespace`.

              - `:namespace`

          - `class ToolSearchTool`

            Hosted or BYOT tool search configuration for deferred tools.

            - `type: :tool_search`

              The type of the tool. Always `tool_search`.

              - `:tool_search`

            - `description: String`

              Description shown to the model for a client-executed tool search tool.

            - `execution: :server | :client`

              Whether tool search is executed by the server or by the client.

              - `:server`

              - `:client`

            - `parameters: untyped`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search_preview | :web_search_preview_2025_03_11`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `:web_search_preview`

              - `:web_search_preview_2025_03_11`

            - `search_content_types: Array[:text | :image]`

              - `:text`

              - `:image`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { type, city, country, 2 more}`

              The user's location.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `type: :apply_patch`

              The type of the tool. Always `apply_patch`.

              - `:apply_patch`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `error: EvalAPIError`

    An object representing an error response from the Eval API.

    - `code: String`

      The error code.

    - `message: String`

      The error message.

  - `eval_id: String`

    The identifier of the associated evaluation.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    The model that is evaluated, if applicable.

  - `name: String`

    The name of the evaluation run.

  - `object: :"eval.run"`

    The type of the object. Always "eval.run".

    - `:"eval.run"`

  - `per_model_usage: Array[{ cached_tokens, completion_tokens, invocation_count, 3 more}]`

    Usage statistics for each model during the evaluation run.

    - `cached_tokens: Integer`

      The number of tokens retrieved from cache.

    - `completion_tokens: Integer`

      The number of completion tokens generated.

    - `invocation_count: Integer`

      The number of invocations.

    - `model_name: String`

      The name of the model.

    - `prompt_tokens: Integer`

      The number of prompt tokens used.

    - `total_tokens: Integer`

      The total number of tokens used.

  - `per_testing_criteria_results: Array[{ failed, passed, testing_criteria}]`

    Results per testing criteria applied during the evaluation run.

    - `failed: Integer`

      Number of tests failed for this criteria.

    - `passed: Integer`

      Number of tests passed for this criteria.

    - `testing_criteria: String`

      A description of the testing criteria.

  - `report_url: String`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `result_counts: { errored, failed, passed, total}`

    Counters summarizing the outcomes of the evaluation run.

    - `errored: Integer`

      Number of output items that resulted in an error.

    - `failed: Integer`

      Number of output items that failed to pass the evaluation.

    - `passed: Integer`

      Number of output items that passed the evaluation.

    - `total: Integer`

      Total number of executed output items.

  - `status: String`

    The status of the evaluation run.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

run = openai.evals.runs.retrieve("run_id", eval_id: "eval_id")

puts(run)
```

### Cancel

`evals.runs.cancel(run_id, **kwargs) -> RunCancelResponse`

**post** `/evals/{eval_id}/runs/{run_id}`

Cancel an ongoing evaluation run.

#### Parameters

- `eval_id: String`

- `run_id: String`

#### Returns

- `class RunCancelResponse`

  A schema representing an evaluation run.

  - `id: String`

    Unique identifier for the evaluation run.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `data_source: CreateEvalJSONLRunDataSource | CreateEvalCompletionsRunDataSource | { source, type, input_messages, 2 more}`

    Information about the run's data source.

    - `class CreateEvalJSONLRunDataSource`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `source: { content, type} | { id, type}`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

      - `type: :jsonl`

        The type of data source. Always `jsonl`.

        - `:jsonl`

    - `class CreateEvalCompletionsRunDataSource`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 3 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class StoredCompletions`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `type: :stored_completions`

            The type of source. Always `stored_completions`.

            - `:stored_completions`

          - `created_after: Integer`

            An optional Unix timestamp to filter items created after this time.

          - `created_before: Integer`

            An optional Unix timestamp to filter items created before this time.

          - `limit: Integer`

            An optional maximum number of items to return.

          - `metadata: Metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `model: String`

            An optional model to filter by (e.g., 'gpt-4o').

      - `type: :completions`

        The type of run data source. Always `completions`.

        - `:completions`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[EasyInputMessage | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputMessageContentList`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                  A text input to the model.

                - `Array[ResponseInputContent]`

                  A list of one or many input items to the model, containing different content
                  types.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class ResponseInputImage`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `detail: :low | :high | :auto | :original`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `:low`

                      - `:high`

                      - `:auto`

                      - `:original`

                    - `type: :input_image`

                      The type of the input item. Always `input_image`.

                      - `:input_image`

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `image_url: String`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile`

                    A file input to the model.

                    - `type: :input_file`

                      The type of the input item. Always `input_file`.

                      - `:input_file`

                    - `file_data: String`

                      The content of the file to be sent to the model.

                    - `file_id: String`

                      The ID of the file to be sent to the model.

                    - `file_url: String`

                      The URL of the file to be sent to the model.

                    - `filename: String`

                      The name of the file to be sent to the model.

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `phase: :commentary | :final_answer`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `:commentary`

                - `:final_answer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, response_format, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `response_format: ResponseFormatText | ResponseFormatJSONSchema | ResponseFormatJSONObject`

          An object specifying the format that the model must output.

          Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
          Structured Outputs which ensures the model will match your supplied JSON
          schema. Learn more in the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

          Setting to `{ "type": "json_object" }` enables the older JSON mode, which
          ensures the message the model generates is valid JSON. Using `json_schema`
          is preferred for models that support it.

          - `class ResponseFormatText`

            Default response format. Used to generate text responses.

            - `type: :text`

              The type of response format being defined. Always `text`.

              - `:text`

          - `class ResponseFormatJSONSchema`

            JSON Schema response format. Used to generate structured JSON responses.
            Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

            - `json_schema: { name, description, schema, strict}`

              Structured Outputs configuration options, including a JSON Schema.

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `type: :json_schema`

              The type of response format being defined. Always `json_schema`.

              - `:json_schema`

          - `class ResponseFormatJSONObject`

            JSON object response format. An older method of generating JSON responses.
            Using `json_schema` is recommended for models that support it. Note that the
            model will not generate JSON without a system or user message instructing it
            to do so.

            - `type: :json_object`

              The type of response format being defined. Always `json_object`.

              - `:json_object`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `tools: Array[ChatCompletionFunctionTool]`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

          - `function: FunctionDefinition`

            - `name: String`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `description: String`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `parameters: FunctionParameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `strict: bool`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `type: :function`

            The type of the tool. Currently, only `function` is supported.

            - `:function`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `source: { content, type} | { id, type} | { type, created_after, created_before, 8 more}`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent`

          - `content: Array[{ item, sample}]`

            The content of the jsonl file.

            - `item: Hash[Symbol, untyped]`

            - `sample: Hash[Symbol, untyped]`

          - `type: :file_content`

            The type of jsonl source. Always `file_content`.

            - `:file_content`

        - `class FileID`

          - `id: String`

            The identifier of the file.

          - `type: :file_id`

            The type of jsonl source. Always `file_id`.

            - `:file_id`

        - `class Responses`

          A EvalResponsesSource object describing a run data source configuration.

          - `type: :responses`

            The type of run data source. Always `responses`.

            - `:responses`

          - `created_after: Integer`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `created_before: Integer`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `instructions_search: String`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `metadata: untyped`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `model: String`

            The name of the model to find responses for. This is a query parameter used to select responses.

          - `reasoning_effort: ReasoningEffort`

            Constrains effort on reasoning for
            [reasoning models](https://platform.openai.com/docs/guides/reasoning).
            Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
            reasoning effort can result in faster responses and fewer tokens used
            on reasoning in a response.

            - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
            - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
            - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
            - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

            - `:none`

            - `:minimal`

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

          - `temperature: Float`

            Sampling temperature. This is a query parameter used to select responses.

          - `tools: Array[String]`

            List of tool names. This is a query parameter used to select responses.

          - `top_p: Float`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `users: Array[String]`

            List of user identifiers. This is a query parameter used to select responses.

      - `type: :responses`

        The type of run data source. Always `responses`.

        - `:responses`

      - `input_messages: { template, type} | { item_reference, type}`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template`

          - `template: Array[{ content, role} | { content, role, type}]`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage`

              - `content: String`

                The content of the message.

              - `role: String`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `content: String | ResponseInputText | { text, type} | 3 more`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                  A text input to the model.

                - `class ResponseInputText`

                  A text input to the model.

                  - `text: String`

                    The text input to the model.

                  - `type: :input_text`

                    The type of the input item. Always `input_text`.

                    - `:input_text`

                - `class OutputText`

                  A text output from the model.

                  - `text: String`

                    The text output from the model.

                  - `type: :output_text`

                    The type of the output text. Always `output_text`.

                    - `:output_text`

                - `class InputImage`

                  An image input block used within EvalItem content arrays.

                  - `image_url: String`

                    The URL of the image input.

                  - `type: :input_image`

                    The type of the image input. Always `input_image`.

                    - `:input_image`

                  - `detail: String`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio`

                  An audio input to the model.

                  - `input_audio: { data, format_}`

                    - `data: String`

                      Base64-encoded audio data.

                    - `format_: :mp3 | :wav`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `:mp3`

                      - `:wav`

                  - `type: :input_audio`

                    The type of the input item. Always `input_audio`.

                    - `:input_audio`

                - `Array[GraderInputItem]`

                  A list of inputs, each of which may be either an input text, output text, input
                  image, or input audio object.

                  - `String`

                    A text input to the model.

                  - `class ResponseInputText`

                    A text input to the model.

                    - `text: String`

                      The text input to the model.

                    - `type: :input_text`

                      The type of the input item. Always `input_text`.

                      - `:input_text`

                  - `class OutputText`

                    A text output from the model.

                    - `text: String`

                      The text output from the model.

                    - `type: :output_text`

                      The type of the output text. Always `output_text`.

                      - `:output_text`

                  - `class InputImage`

                    An image input block used within EvalItem content arrays.

                    - `image_url: String`

                      The URL of the image input.

                    - `type: :input_image`

                      The type of the image input. Always `input_image`.

                      - `:input_image`

                    - `detail: String`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio`

                    An audio input to the model.

                    - `input_audio: { data, format_}`

                      - `data: String`

                        Base64-encoded audio data.

                      - `format_: :mp3 | :wav`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `:mp3`

                        - `:wav`

                    - `type: :input_audio`

                      The type of the input item. Always `input_audio`.

                      - `:input_audio`

              - `role: :user | :assistant | :system | :developer`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `:user`

                - `:assistant`

                - `:system`

                - `:developer`

              - `type: :message`

                The type of the message input. Always `message`.

                - `:message`

          - `type: :template`

            The type of input messages. Always `template`.

            - `:template`

        - `class ItemReference`

          - `item_reference: String`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `type: :item_reference`

            The type of input messages. Always `item_reference`.

            - `:item_reference`

      - `model: String`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `sampling_params: { max_completion_tokens, reasoning_effort, seed, 4 more}`

        - `max_completion_tokens: Integer`

          The maximum number of tokens in the generated output.

        - `reasoning_effort: ReasoningEffort`

          Constrains effort on reasoning for
          [reasoning models](https://platform.openai.com/docs/guides/reasoning).
          Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
          reasoning effort can result in faster responses and fewer tokens used
          on reasoning in a response.

          - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
          - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
          - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
          - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

        - `seed: Integer`

          A seed value to initialize the randomness, during sampling.

        - `temperature: Float`

          A higher temperature increases randomness in the outputs.

        - `text: { format_}`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `format_: ResponseFormatTextConfig`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText`

              Default response format. Used to generate text responses.

              - `type: :text`

                The type of response format being defined. Always `text`.

                - `:text`

            - `class ResponseFormatTextJSONSchemaConfig`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `name: String`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `schema: Hash[Symbol, untyped]`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `type: :json_schema`

                The type of response format being defined. Always `json_schema`.

                - `:json_schema`

              - `description: String`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `strict: bool`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJSONObject`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `type: :json_object`

                The type of response format being defined. Always `json_object`.

                - `:json_object`

        - `tools: Array[Tool]`

          An array of tools the model may call while generating a response. You
          can specify which tool to use by setting the `tool_choice` parameter.

          The two categories of tools you can provide the model are:

          - **Built-in tools**: Tools that are provided by OpenAI that extend the
            model's capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
            or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
            [built-in tools](https://platform.openai.com/docs/guides/tools).
          - **Function calls (custom tools)**: Functions that are defined by you,
            enabling the model to call your own code. Learn more about
            [function calling](https://platform.openai.com/docs/guides/function-calling).

          - `class FunctionTool`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `name: String`

              The name of the function to call.

            - `parameters: Hash[Symbol, untyped]`

              A JSON schema object describing the parameters of the function.

            - `strict: bool`

              Whether to enforce strict parameter validation. Default `true`.

            - `type: :function`

              The type of the function tool. Always `function`.

              - `:function`

            - `defer_loading: bool`

              Whether this function is deferred and loaded via tool search.

            - `description: String`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `type: :file_search`

              The type of the file search tool. Always `file_search`.

              - `:file_search`

            - `vector_store_ids: Array[String]`

              The IDs of the vector stores to search.

            - `filters: ComparisonFilter | CompoundFilter`

              A filter to apply.

              - `class ComparisonFilter`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `key: String`

                  The key to compare against the value.

                - `type: :eq | :ne | :gt | 3 more`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `:eq`

                  - `:ne`

                  - `:gt`

                  - `:gte`

                  - `:lt`

                  - `:lte`

                - `value: String | Float | bool | Array[String | Float]`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `Float`

                  - `bool`

                  - `Array[String | Float]`

                    - `String`

                    - `Float`

              - `class CompoundFilter`

                Combine multiple filters using `and` or `or`.

                - `filters: Array[ComparisonFilter | untyped]`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `key: String`

                      The key to compare against the value.

                    - `type: :eq | :ne | :gt | 3 more`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `:eq`

                      - `:ne`

                      - `:gt`

                      - `:gte`

                      - `:lt`

                      - `:lte`

                    - `value: String | Float | bool | Array[String | Float]`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `Float`

                      - `bool`

                      - `Array[String | Float]`

                        - `String`

                        - `Float`

                  - `untyped`

                - `type: :and | :or`

                  Type of operation: `and` or `or`.

                  - `:and`

                  - `:or`

            - `max_num_results: Integer`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `ranking_options: { hybrid_search, ranker, score_threshold}`

              Ranking options for search.

              - `hybrid_search: { embedding_weight, text_weight}`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `embedding_weight: Float`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `text_weight: Float`

                  The weight of the text in the reciprocal ranking fusion.

              - `ranker: :auto | :"default-2024-11-15"`

                The ranker to use for the file search.

                - `:auto`

                - `:"default-2024-11-15"`

              - `score_threshold: Float`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `type: :computer`

              The type of the computer tool. Always `computer`.

              - `:computer`

          - `class ComputerUsePreviewTool`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `display_height: Integer`

              The height of the computer display.

            - `display_width: Integer`

              The width of the computer display.

            - `environment: :windows | :mac | :linux | 2 more`

              The type of computer environment to control.

              - `:windows`

              - `:mac`

              - `:linux`

              - `:ubuntu`

              - `:browser`

            - `type: :computer_use_preview`

              The type of the computer use tool. Always `computer_use_preview`.

              - `:computer_use_preview`

          - `class WebSearchTool`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search | :web_search_2025_08_26`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `:web_search`

              - `:web_search_2025_08_26`

            - `filters: { allowed_domains}`

              Filters for the search.

              - `allowed_domains: Array[String]`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { city, country, region, 2 more}`

              The approximate location of the user.

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

          - `class Mcp`

            Give the model access to additional tools via remote Model Context Protocol
            (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

            - `server_label: String`

              A label for this MCP server, used to identify it in tool calls.

            - `type: :mcp`

              The type of the MCP tool. Always `mcp`.

              - `:mcp`

            - `allowed_tools: Array[String] | { read_only, tool_names}`

              List of allowed tool names or a filter object.

              - `Array[String]`

                A string array of allowed tool names

              - `class McpToolFilter`

                A filter object to specify which tools are allowed.

                - `read_only: bool`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `tool_names: Array[String]`

                  List of allowed tool names.

            - `authorization: String`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `connector_id: :connector_dropbox | :connector_gmail | :connector_googlecalendar | 5 more`

              Identifier for service connectors, like those available in ChatGPT. One of
              `server_url` or `connector_id` must be provided. Learn more about service
              connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

              Currently supported `connector_id` values are:

              - Dropbox: `connector_dropbox`
              - Gmail: `connector_gmail`
              - Google Calendar: `connector_googlecalendar`
              - Google Drive: `connector_googledrive`
              - Microsoft Teams: `connector_microsoftteams`
              - Outlook Calendar: `connector_outlookcalendar`
              - Outlook Email: `connector_outlookemail`
              - SharePoint: `connector_sharepoint`

              - `:connector_dropbox`

              - `:connector_gmail`

              - `:connector_googlecalendar`

              - `:connector_googledrive`

              - `:connector_microsoftteams`

              - `:connector_outlookcalendar`

              - `:connector_outlookemail`

              - `:connector_sharepoint`

            - `defer_loading: bool`

              Whether this MCP tool is deferred and discovered via tool search.

            - `headers: Hash[Symbol, String]`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `require_approval: { always, never} | :always | :never`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `always: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

                - `never: { read_only, tool_names}`

                  A filter object to specify which tools are allowed.

                  - `read_only: bool`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `tool_names: Array[String]`

                    List of allowed tool names.

              - `McpToolApprovalSetting = :always | :never`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `:always`

                - `:never`

            - `server_description: String`

              Optional description of the MCP server, used to provide more context.

            - `server_url: String`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `class CodeInterpreter`

            A tool that runs Python code to help generate a response to a prompt.

            - `container: String | { type, file_ids, memory_limit, network_policy}`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

                The container ID.

              - `class CodeInterpreterToolAuto`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `type: :auto`

                  Always `auto`.

                  - `:auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the code interpreter container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

            - `type: :code_interpreter`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `:code_interpreter`

          - `class ImageGeneration`

            A tool that generates images using the GPT image models.

            - `type: :image_generation`

              The type of the image generation tool. Always `image_generation`.

              - `:image_generation`

            - `action: :generate | :edit | :auto`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `:generate`

              - `:edit`

              - `:auto`

            - `background: :transparent | :opaque | :auto`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `:transparent`

              - `:opaque`

              - `:auto`

            - `input_fidelity: :high | :low`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `:high`

              - `:low`

            - `input_image_mask: { file_id, image_url}`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `file_id: String`

                File ID for the mask image.

              - `image_url: String`

                Base64-encoded mask image.

            - `model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

              The image generation model to use. Default: `gpt-image-1`.

              - `String`

              - `:"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-1.5"`

                The image generation model to use. Default: `gpt-image-1`.

                - `:"gpt-image-1"`

                - `:"gpt-image-1-mini"`

                - `:"gpt-image-1.5"`

            - `moderation: :auto | :low`

              Moderation level for the generated image. Default: `auto`.

              - `:auto`

              - `:low`

            - `output_compression: Integer`

              Compression level for the output image. Default: 100.

            - `output_format: :png | :webp | :jpeg`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `:png`

              - `:webp`

              - `:jpeg`

            - `partial_images: Integer`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `quality: :low | :medium | :high | :auto`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `:low`

              - `:medium`

              - `:high`

              - `:auto`

            - `size: :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `:"1024x1024"`

              - `:"1024x1536"`

              - `:"1536x1024"`

              - `:auto`

          - `class LocalShell`

            A tool that allows the model to execute shell commands in a local environment.

            - `type: :local_shell`

              The type of the local shell tool. Always `local_shell`.

              - `:local_shell`

          - `class FunctionShellTool`

            A tool that allows the model to execute shell commands.

            - `type: :shell`

              The type of the shell tool. Always `shell`.

              - `:shell`

            - `environment: ContainerAuto | LocalEnvironment | ContainerReference`

              - `class ContainerAuto`

                - `type: :container_auto`

                  Automatically creates a container for this request

                  - `:container_auto`

                - `file_ids: Array[String]`

                  An optional list of uploaded files to make available to your code.

                - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

                  The memory limit for the container.

                  - `:"1g"`

                  - `:"4g"`

                  - `:"16g"`

                  - `:"64g"`

                - `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled`

                    - `type: :disabled`

                      Disable outbound network access. Always `disabled`.

                      - `:disabled`

                  - `class ContainerNetworkPolicyAllowlist`

                    - `allowed_domains: Array[String]`

                      A list of allowed domains when type is `allowlist`.

                    - `type: :allowlist`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `:allowlist`

                    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `domain: String`

                        The domain associated with the secret.

                      - `name: String`

                        The name of the secret to inject for the domain.

                      - `value: String`

                        The secret value to inject for the domain.

                - `skills: Array[SkillReference | InlineSkill]`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference`

                    - `skill_id: String`

                      The ID of the referenced skill.

                    - `type: :skill_reference`

                      References a skill created with the /v1/skills endpoint.

                      - `:skill_reference`

                    - `version: String`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill`

                    - `description: String`

                      The description of the skill.

                    - `name: String`

                      The name of the skill.

                    - `source: InlineSkillSource`

                      Inline skill payload

                      - `data: String`

                        Base64-encoded skill zip bundle.

                      - `media_type: :"application/zip"`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `:"application/zip"`

                      - `type: :base64`

                        The type of the inline skill source. Must be `base64`.

                        - `:base64`

                    - `type: :inline`

                      Defines an inline skill for this request.

                      - `:inline`

              - `class LocalEnvironment`

                - `type: :local`

                  Use a local computer environment.

                  - `:local`

                - `skills: Array[LocalSkill]`

                  An optional list of skills.

                  - `description: String`

                    The description of the skill.

                  - `name: String`

                    The name of the skill.

                  - `path: String`

                    The path to the directory containing the skill.

              - `class ContainerReference`

                - `container_id: String`

                  The ID of the referenced container.

                - `type: :container_reference`

                  References a container created with the /v1/containers endpoint

                  - `:container_reference`

          - `class CustomTool`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `name: String`

              The name of the custom tool, used to identify it in tool calls.

            - `type: :custom`

              The type of the custom tool. Always `custom`.

              - `:custom`

            - `defer_loading: bool`

              Whether this tool should be deferred and discovered via tool search.

            - `description: String`

              Optional description of the custom tool, used to provide more context.

            - `format_: CustomToolInputFormat`

              The input format for the custom tool. Default is unconstrained text.

              - `class Text`

                Unconstrained free-form text.

                - `type: :text`

                  Unconstrained text format. Always `text`.

                  - `:text`

              - `class Grammar`

                A grammar defined by the user.

                - `definition: String`

                  The grammar definition.

                - `syntax: :lark | :regex`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `:lark`

                  - `:regex`

                - `type: :grammar`

                  Grammar format. Always `grammar`.

                  - `:grammar`

          - `class NamespaceTool`

            Groups function/custom tools under a shared namespace.

            - `description: String`

              A description of the namespace shown to the model.

            - `name: String`

              The namespace name used in tool calls (for example, `crm`).

            - `tools: Array[{ name, type, defer_loading, 3 more} | CustomTool]`

              The function/custom tools available inside this namespace.

              - `class Function`

                - `name: String`

                - `type: :function`

                  - `:function`

                - `defer_loading: bool`

                  Whether this function should be deferred and discovered via tool search.

                - `description: String`

                - `parameters: untyped`

                - `strict: bool`

              - `class CustomTool`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `name: String`

                  The name of the custom tool, used to identify it in tool calls.

                - `type: :custom`

                  The type of the custom tool. Always `custom`.

                  - `:custom`

                - `defer_loading: bool`

                  Whether this tool should be deferred and discovered via tool search.

                - `description: String`

                  Optional description of the custom tool, used to provide more context.

                - `format_: CustomToolInputFormat`

                  The input format for the custom tool. Default is unconstrained text.

                  - `class Text`

                    Unconstrained free-form text.

                    - `type: :text`

                      Unconstrained text format. Always `text`.

                      - `:text`

                  - `class Grammar`

                    A grammar defined by the user.

                    - `definition: String`

                      The grammar definition.

                    - `syntax: :lark | :regex`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `:lark`

                      - `:regex`

                    - `type: :grammar`

                      Grammar format. Always `grammar`.

                      - `:grammar`

            - `type: :namespace`

              The type of the tool. Always `namespace`.

              - `:namespace`

          - `class ToolSearchTool`

            Hosted or BYOT tool search configuration for deferred tools.

            - `type: :tool_search`

              The type of the tool. Always `tool_search`.

              - `:tool_search`

            - `description: String`

              Description shown to the model for a client-executed tool search tool.

            - `execution: :server | :client`

              Whether tool search is executed by the server or by the client.

              - `:server`

              - `:client`

            - `parameters: untyped`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `type: :web_search_preview | :web_search_preview_2025_03_11`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `:web_search_preview`

              - `:web_search_preview_2025_03_11`

            - `search_content_types: Array[:text | :image]`

              - `:text`

              - `:image`

            - `search_context_size: :low | :medium | :high`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `:low`

              - `:medium`

              - `:high`

            - `user_location: { type, city, country, 2 more}`

              The user's location.

              - `type: :approximate`

                The type of location approximation. Always `approximate`.

                - `:approximate`

              - `city: String`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `country: String`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `region: String`

                Free text input for the region of the user, e.g. `California`.

              - `timezone: String`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `type: :apply_patch`

              The type of the tool. Always `apply_patch`.

              - `:apply_patch`

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `error: EvalAPIError`

    An object representing an error response from the Eval API.

    - `code: String`

      The error code.

    - `message: String`

      The error message.

  - `eval_id: String`

    The identifier of the associated evaluation.

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `model: String`

    The model that is evaluated, if applicable.

  - `name: String`

    The name of the evaluation run.

  - `object: :"eval.run"`

    The type of the object. Always "eval.run".

    - `:"eval.run"`

  - `per_model_usage: Array[{ cached_tokens, completion_tokens, invocation_count, 3 more}]`

    Usage statistics for each model during the evaluation run.

    - `cached_tokens: Integer`

      The number of tokens retrieved from cache.

    - `completion_tokens: Integer`

      The number of completion tokens generated.

    - `invocation_count: Integer`

      The number of invocations.

    - `model_name: String`

      The name of the model.

    - `prompt_tokens: Integer`

      The number of prompt tokens used.

    - `total_tokens: Integer`

      The total number of tokens used.

  - `per_testing_criteria_results: Array[{ failed, passed, testing_criteria}]`

    Results per testing criteria applied during the evaluation run.

    - `failed: Integer`

      Number of tests failed for this criteria.

    - `passed: Integer`

      Number of tests passed for this criteria.

    - `testing_criteria: String`

      A description of the testing criteria.

  - `report_url: String`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `result_counts: { errored, failed, passed, total}`

    Counters summarizing the outcomes of the evaluation run.

    - `errored: Integer`

      Number of output items that resulted in an error.

    - `failed: Integer`

      Number of output items that failed to pass the evaluation.

    - `passed: Integer`

      Number of output items that passed the evaluation.

    - `total: Integer`

      Total number of executed output items.

  - `status: String`

    The status of the evaluation run.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.evals.runs.cancel("run_id", eval_id: "eval_id")

puts(response)
```

### Delete

`evals.runs.delete(run_id, **kwargs) -> RunDeleteResponse`

**delete** `/evals/{eval_id}/runs/{run_id}`

Delete an eval run.

#### Parameters

- `eval_id: String`

- `run_id: String`

#### Returns

- `class RunDeleteResponse`

  - `deleted: bool`

  - `object: String`

  - `run_id: String`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

run = openai.evals.runs.delete("run_id", eval_id: "eval_id")

puts(run)
```

#### Domain Types

#### Create Eval Completions Run Data Source

- `class CreateEvalCompletionsRunDataSource`

  A CompletionsRunDataSource object describing a model sampling configuration.

  - `source: { content, type} | { id, type} | { type, created_after, created_before, 3 more}`

    Determines what populates the `item` namespace in this run's data source.

    - `class FileContent`

      - `content: Array[{ item, sample}]`

        The content of the jsonl file.

        - `item: Hash[Symbol, untyped]`

        - `sample: Hash[Symbol, untyped]`

      - `type: :file_content`

        The type of jsonl source. Always `file_content`.

        - `:file_content`

    - `class FileID`

      - `id: String`

        The identifier of the file.

      - `type: :file_id`

        The type of jsonl source. Always `file_id`.

        - `:file_id`

    - `class StoredCompletions`

      A StoredCompletionsRunDataSource configuration describing a set of filters

      - `type: :stored_completions`

        The type of source. Always `stored_completions`.

        - `:stored_completions`

      - `created_after: Integer`

        An optional Unix timestamp to filter items created after this time.

      - `created_before: Integer`

        An optional Unix timestamp to filter items created before this time.

      - `limit: Integer`

        An optional maximum number of items to return.

      - `metadata: Metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `model: String`

        An optional model to filter by (e.g., 'gpt-4o').

  - `type: :completions`

    The type of run data source. Always `completions`.

    - `:completions`

  - `input_messages: { template, type} | { item_reference, type}`

    Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

    - `class Template`

      - `template: Array[EasyInputMessage | { content, role, type}]`

        A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

        - `class EasyInputMessage`

          A message input to the model with a role indicating instruction following
          hierarchy. Instructions given with the `developer` or `system` role take
          precedence over instructions given with the `user` role. Messages with the
          `assistant` role are presumed to have been generated by the model in previous
          interactions.

          - `content: String | ResponseInputMessageContentList`

            Text, image, or audio input to the model, used to generate a response.
            Can also contain previous assistant responses.

            - `String`

              A text input to the model.

            - `Array[ResponseInputContent]`

              A list of one or many input items to the model, containing different content
              types.

              - `class ResponseInputText`

                A text input to the model.

                - `text: String`

                  The text input to the model.

                - `type: :input_text`

                  The type of the input item. Always `input_text`.

                  - `:input_text`

              - `class ResponseInputImage`

                An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                - `detail: :low | :high | :auto | :original`

                  The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                  - `:low`

                  - `:high`

                  - `:auto`

                  - `:original`

                - `type: :input_image`

                  The type of the input item. Always `input_image`.

                  - `:input_image`

                - `file_id: String`

                  The ID of the file to be sent to the model.

                - `image_url: String`

                  The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `class ResponseInputFile`

                A file input to the model.

                - `type: :input_file`

                  The type of the input item. Always `input_file`.

                  - `:input_file`

                - `file_data: String`

                  The content of the file to be sent to the model.

                - `file_id: String`

                  The ID of the file to be sent to the model.

                - `file_url: String`

                  The URL of the file to be sent to the model.

                - `filename: String`

                  The name of the file to be sent to the model.

          - `role: :user | :assistant | :system | :developer`

            The role of the message input. One of `user`, `assistant`, `system`, or
            `developer`.

            - `:user`

            - `:assistant`

            - `:system`

            - `:developer`

          - `phase: :commentary | :final_answer`

            Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
            For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
            phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

            - `:commentary`

            - `:final_answer`

          - `type: :message`

            The type of the message input. Always `message`.

            - `:message`

        - `class EvalItem`

          A message input to the model with a role indicating instruction following
          hierarchy. Instructions given with the `developer` or `system` role take
          precedence over instructions given with the `user` role. Messages with the
          `assistant` role are presumed to have been generated by the model in previous
          interactions.

          - `content: String | ResponseInputText | { text, type} | 3 more`

            Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

            - `String`

              A text input to the model.

            - `class ResponseInputText`

              A text input to the model.

              - `text: String`

                The text input to the model.

              - `type: :input_text`

                The type of the input item. Always `input_text`.

                - `:input_text`

            - `class OutputText`

              A text output from the model.

              - `text: String`

                The text output from the model.

              - `type: :output_text`

                The type of the output text. Always `output_text`.

                - `:output_text`

            - `class InputImage`

              An image input block used within EvalItem content arrays.

              - `image_url: String`

                The URL of the image input.

              - `type: :input_image`

                The type of the image input. Always `input_image`.

                - `:input_image`

              - `detail: String`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio`

              An audio input to the model.

              - `input_audio: { data, format_}`

                - `data: String`

                  Base64-encoded audio data.

                - `format_: :mp3 | :wav`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `:mp3`

                  - `:wav`

              - `type: :input_audio`

                The type of the input item. Always `input_audio`.

                - `:input_audio`

            - `Array[GraderInputItem]`

              A list of inputs, each of which may be either an input text, output text, input
              image, or input audio object.

              - `String`

                A text input to the model.

              - `class ResponseInputText`

                A text input to the model.

                - `text: String`

                  The text input to the model.

                - `type: :input_text`

                  The type of the input item. Always `input_text`.

                  - `:input_text`

              - `class OutputText`

                A text output from the model.

                - `text: String`

                  The text output from the model.

                - `type: :output_text`

                  The type of the output text. Always `output_text`.

                  - `:output_text`

              - `class InputImage`

                An image input block used within EvalItem content arrays.

                - `image_url: String`

                  The URL of the image input.

                - `type: :input_image`

                  The type of the image input. Always `input_image`.

                  - `:input_image`

                - `detail: String`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `class ResponseInputAudio`

                An audio input to the model.

                - `input_audio: { data, format_}`

                  - `data: String`

                    Base64-encoded audio data.

                  - `format_: :mp3 | :wav`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `:mp3`

                    - `:wav`

                - `type: :input_audio`

                  The type of the input item. Always `input_audio`.

                  - `:input_audio`

          - `role: :user | :assistant | :system | :developer`

            The role of the message input. One of `user`, `assistant`, `system`, or
            `developer`.

            - `:user`

            - `:assistant`

            - `:system`

            - `:developer`

          - `type: :message`

            The type of the message input. Always `message`.

            - `:message`

      - `type: :template`

        The type of input messages. Always `template`.

        - `:template`

    - `class ItemReference`

      - `item_reference: String`

        A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

      - `type: :item_reference`

        The type of input messages. Always `item_reference`.

        - `:item_reference`

  - `model: String`

    The name of the model to use for generating completions (e.g. "o3-mini").

  - `sampling_params: { max_completion_tokens, reasoning_effort, response_format, 4 more}`

    - `max_completion_tokens: Integer`

      The maximum number of tokens in the generated output.

    - `reasoning_effort: ReasoningEffort`

      Constrains effort on reasoning for
      [reasoning models](https://platform.openai.com/docs/guides/reasoning).
      Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
      reasoning effort can result in faster responses and fewer tokens used
      on reasoning in a response.

      - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
      - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
      - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
      - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

    - `response_format: ResponseFormatText | ResponseFormatJSONSchema | ResponseFormatJSONObject`

      An object specifying the format that the model must output.

      Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
      Structured Outputs which ensures the model will match your supplied JSON
      schema. Learn more in the [Structured Outputs
      guide](https://platform.openai.com/docs/guides/structured-outputs).

      Setting to `{ "type": "json_object" }` enables the older JSON mode, which
      ensures the message the model generates is valid JSON. Using `json_schema`
      is preferred for models that support it.

      - `class ResponseFormatText`

        Default response format. Used to generate text responses.

        - `type: :text`

          The type of response format being defined. Always `text`.

          - `:text`

      - `class ResponseFormatJSONSchema`

        JSON Schema response format. Used to generate structured JSON responses.
        Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

        - `json_schema: { name, description, schema, strict}`

          Structured Outputs configuration options, including a JSON Schema.

          - `name: String`

            The name of the response format. Must be a-z, A-Z, 0-9, or contain
            underscores and dashes, with a maximum length of 64.

          - `description: String`

            A description of what the response format is for, used by the model to
            determine how to respond in the format.

          - `schema: Hash[Symbol, untyped]`

            The schema for the response format, described as a JSON Schema object.
            Learn how to build JSON schemas [here](https://json-schema.org/).

          - `strict: bool`

            Whether to enable strict schema adherence when generating the output.
            If set to true, the model will always follow the exact schema defined
            in the `schema` field. Only a subset of JSON Schema is supported when
            `strict` is `true`. To learn more, read the [Structured Outputs
            guide](https://platform.openai.com/docs/guides/structured-outputs).

        - `type: :json_schema`

          The type of response format being defined. Always `json_schema`.

          - `:json_schema`

      - `class ResponseFormatJSONObject`

        JSON object response format. An older method of generating JSON responses.
        Using `json_schema` is recommended for models that support it. Note that the
        model will not generate JSON without a system or user message instructing it
        to do so.

        - `type: :json_object`

          The type of response format being defined. Always `json_object`.

          - `:json_object`

    - `seed: Integer`

      A seed value to initialize the randomness, during sampling.

    - `temperature: Float`

      A higher temperature increases randomness in the outputs.

    - `tools: Array[ChatCompletionFunctionTool]`

      A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

      - `function: FunctionDefinition`

        - `name: String`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `description: String`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `parameters: FunctionParameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `strict: bool`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `type: :function`

        The type of the tool. Currently, only `function` is supported.

        - `:function`

    - `top_p: Float`

      An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

#### Create Eval JSONL Run Data Source

- `class CreateEvalJSONLRunDataSource`

  A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

  - `source: { content, type} | { id, type}`

    Determines what populates the `item` namespace in the data source.

    - `class FileContent`

      - `content: Array[{ item, sample}]`

        The content of the jsonl file.

        - `item: Hash[Symbol, untyped]`

        - `sample: Hash[Symbol, untyped]`

      - `type: :file_content`

        The type of jsonl source. Always `file_content`.

        - `:file_content`

    - `class FileID`

      - `id: String`

        The identifier of the file.

      - `type: :file_id`

        The type of jsonl source. Always `file_id`.

        - `:file_id`

  - `type: :jsonl`

    The type of data source. Always `jsonl`.

    - `:jsonl`

#### Eval API Error

- `class EvalAPIError`

  An object representing an error response from the Eval API.

  - `code: String`

    The error code.

  - `message: String`

    The error message.

### Output Items

#### List

`evals.runs.output_items.list(run_id, **kwargs) -> CursorPage<OutputItemListResponse>`

**get** `/evals/{eval_id}/runs/{run_id}/output_items`

Get a list of output items for an evaluation run.

##### Parameters

- `eval_id: String`

- `run_id: String`

- `after: String`

  Identifier for the last output item from the previous pagination request.

- `limit: Integer`

  Number of output items to retrieve.

- `order: :asc | :desc`

  Sort order for output items by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

  - `:asc`

  - `:desc`

- `status: :fail | :pass`

  Filter output items by status. Use `failed` to filter by failed output
  items or `pass` to filter by passed output items.

  - `:fail`

  - `:pass`

##### Returns

- `class OutputItemListResponse`

  A schema representing an evaluation run output item.

  - `id: String`

    Unique identifier for the evaluation run output item.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `datasource_item: Hash[Symbol, untyped]`

    Details of the input data source item.

  - `datasource_item_id: Integer`

    The identifier for the data source item.

  - `eval_id: String`

    The identifier of the evaluation group.

  - `object: :"eval.run.output_item"`

    The type of the object. Always "eval.run.output_item".

    - `:"eval.run.output_item"`

  - `results: Array[{ name, passed, score, 2 more}]`

    A list of grader results for this output item.

    - `name: String`

      The name of the grader.

    - `passed: bool`

      Whether the grader considered the output a pass.

    - `score: Float`

      The numeric score produced by the grader.

    - `sample: Hash[Symbol, untyped]`

      Optional sample or intermediate data produced by the grader.

    - `type: String`

      The grader type (for example, "string-check-grader").

  - `run_id: String`

    The identifier of the evaluation run associated with this output item.

  - `sample: { error, finish_reason, input, 7 more}`

    A sample containing the input and output of the evaluation run.

    - `error: EvalAPIError`

      An object representing an error response from the Eval API.

      - `code: String`

        The error code.

      - `message: String`

        The error message.

    - `finish_reason: String`

      The reason why the sample generation was finished.

    - `input: Array[{ content, role}]`

      An array of input messages.

      - `content: String`

        The content of the message.

      - `role: String`

        The role of the message sender (e.g., system, user, developer).

    - `max_completion_tokens: Integer`

      The maximum number of tokens allowed for completion.

    - `model: String`

      The model used for generating the sample.

    - `output: Array[{ content, role}]`

      An array of output messages.

      - `content: String`

        The content of the message.

      - `role: String`

        The role of the message (e.g. "system", "assistant", "user").

    - `seed: Integer`

      The seed used for generating the sample.

    - `temperature: Float`

      The sampling temperature used.

    - `top_p: Float`

      The top_p value used for sampling.

    - `usage: { cached_tokens, completion_tokens, prompt_tokens, total_tokens}`

      Token usage details for the sample.

      - `cached_tokens: Integer`

        The number of tokens retrieved from cache.

      - `completion_tokens: Integer`

        The number of completion tokens generated.

      - `prompt_tokens: Integer`

        The number of prompt tokens used.

      - `total_tokens: Integer`

        The total number of tokens used.

  - `status: String`

    The status of the evaluation run.

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.evals.runs.output_items.list("run_id", eval_id: "eval_id")

puts(page)
```

#### Retrieve

`evals.runs.output_items.retrieve(output_item_id, **kwargs) -> OutputItemRetrieveResponse`

**get** `/evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}`

Get an evaluation run output item by ID.

##### Parameters

- `eval_id: String`

- `run_id: String`

- `output_item_id: String`

##### Returns

- `class OutputItemRetrieveResponse`

  A schema representing an evaluation run output item.

  - `id: String`

    Unique identifier for the evaluation run output item.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `datasource_item: Hash[Symbol, untyped]`

    Details of the input data source item.

  - `datasource_item_id: Integer`

    The identifier for the data source item.

  - `eval_id: String`

    The identifier of the evaluation group.

  - `object: :"eval.run.output_item"`

    The type of the object. Always "eval.run.output_item".

    - `:"eval.run.output_item"`

  - `results: Array[{ name, passed, score, 2 more}]`

    A list of grader results for this output item.

    - `name: String`

      The name of the grader.

    - `passed: bool`

      Whether the grader considered the output a pass.

    - `score: Float`

      The numeric score produced by the grader.

    - `sample: Hash[Symbol, untyped]`

      Optional sample or intermediate data produced by the grader.

    - `type: String`

      The grader type (for example, "string-check-grader").

  - `run_id: String`

    The identifier of the evaluation run associated with this output item.

  - `sample: { error, finish_reason, input, 7 more}`

    A sample containing the input and output of the evaluation run.

    - `error: EvalAPIError`

      An object representing an error response from the Eval API.

      - `code: String`

        The error code.

      - `message: String`

        The error message.

    - `finish_reason: String`

      The reason why the sample generation was finished.

    - `input: Array[{ content, role}]`

      An array of input messages.

      - `content: String`

        The content of the message.

      - `role: String`

        The role of the message sender (e.g., system, user, developer).

    - `max_completion_tokens: Integer`

      The maximum number of tokens allowed for completion.

    - `model: String`

      The model used for generating the sample.

    - `output: Array[{ content, role}]`

      An array of output messages.

      - `content: String`

        The content of the message.

      - `role: String`

        The role of the message (e.g. "system", "assistant", "user").

    - `seed: Integer`

      The seed used for generating the sample.

    - `temperature: Float`

      The sampling temperature used.

    - `top_p: Float`

      The top_p value used for sampling.

    - `usage: { cached_tokens, completion_tokens, prompt_tokens, total_tokens}`

      Token usage details for the sample.

      - `cached_tokens: Integer`

        The number of tokens retrieved from cache.

      - `completion_tokens: Integer`

        The number of completion tokens generated.

      - `prompt_tokens: Integer`

        The number of prompt tokens used.

      - `total_tokens: Integer`

        The total number of tokens used.

  - `status: String`

    The status of the evaluation run.

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

output_item = openai.evals.runs.output_items.retrieve("output_item_id", eval_id: "eval_id", run_id: "run_id")

puts(output_item)
```
