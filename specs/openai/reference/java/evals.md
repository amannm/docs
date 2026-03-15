# Evals

## List

`EvalListPage evals().list(EvalListParamsparams = EvalListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/evals`

List evaluations for a project.

### Parameters

- `EvalListParams params`

  - `Optional<String> after`

    Identifier for the last eval from the previous pagination request.

  - `Optional<Long> limit`

    Number of evals to retrieve.

  - `Optional<Order> order`

    Sort order for evals by timestamp. Use `asc` for ascending order or `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<OrderBy> orderBy`

    Evals can be ordered by creation time or last updated time. Use
    `created_at` for creation time or `updated_at` for last updated time.

    - `CREATED_AT("created_at")`

    - `UPDATED_AT("updated_at")`

### Returns

- `class EvalListResponse:`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `String id`

    Unique identifier for the evaluation.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the eval was created.

  - `DataSourceConfig dataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig:`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "custom"constant`

        The type of data source. Always `custom`.

        - `CUSTOM("custom")`

    - `class Logs:`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "logs"constant`

        The type of data source. Always `logs`.

        - `LOGS("logs")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig:`

      Deprecated in favor of LogsDataSourceConfig.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "stored_completions"constant`

        The type of data source. Always `stored_completions`.

        - `STORED_COMPLETIONS("stored_completions")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the evaluation.

  - `JsonValue; object_ "eval"constant`

    The object type.

    - `EVAL("eval")`

  - `List<TestingCriterion> testingCriteria`

    A list of testing criteria.

    - `class LabelModelGrader:`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `List<Input> input`

        - `Content content`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

          - `class ResponseInputText:`

            A text input to the model.

            - `String text`

              The text input to the model.

            - `JsonValue; type "input_text"constant`

              The type of the input item. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `class OutputText:`

            A text output from the model.

            - `String text`

              The text output from the model.

            - `JsonValue; type "output_text"constant`

              The type of the output text. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

          - `class InputImage:`

            An image input block used within EvalItem content arrays.

            - `String imageUrl`

              The URL of the image input.

            - `JsonValue; type "input_image"constant`

              The type of the image input. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

            - `Optional<String> detail`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio:`

            An audio input to the model.

            - `InputAudio inputAudio`

              - `String data`

                Base64-encoded audio data.

              - `Format format`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `MP3("mp3")`

                - `WAV("wav")`

            - `JsonValue; type "input_audio"constant`

              The type of the input item. Always `input_audio`.

              - `INPUT_AUDIO("input_audio")`

          - `List<EvalContentItem>`

            - `String`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `OutputText`

              - `String text`

                The text output from the model.

              - `JsonValue; type "output_text"constant`

                The type of the output text. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image input.

              - `JsonValue; type "input_image"constant`

                The type of the image input. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio:`

              An audio input to the model.

              - `InputAudio inputAudio`

                - `String data`

                  Base64-encoded audio data.

                - `Format format`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `MP3("mp3")`

                  - `WAV("wav")`

              - `JsonValue; type "input_audio"constant`

                The type of the input item. Always `input_audio`.

                - `INPUT_AUDIO("input_audio")`

        - `Role role`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Type> type`

          The type of the message input. Always `message`.

          - `MESSAGE("message")`

      - `List<String> labels`

        The labels to assign to each item in the evaluation.

      - `String model`

        The model to use for the evaluation. Must support structured outputs.

      - `String name`

        The name of the grader.

      - `List<String> passingLabels`

        The labels that indicate a passing result. Must be a subset of labels.

      - `JsonValue; type "label_model"constant`

        The object type, which is always `label_model`.

        - `LABEL_MODEL("label_model")`

    - `class StringCheckGrader:`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `String input`

        The input text. This may include template strings.

      - `String name`

        The name of the grader.

      - `Operation operation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `EQ("eq")`

        - `NE("ne")`

        - `LIKE("like")`

        - `ILIKE("ilike")`

      - `String reference`

        The reference text. This may include template strings.

      - `JsonValue; type "string_check"constant`

        The object type, which is always `string_check`.

        - `STRING_CHECK("string_check")`

    - `class EvalGraderTextSimilarity:`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `double passThreshold`

        The threshold for the score.

    - `class EvalGraderPython:`

      A PythonGrader object that runs a python script on the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

    - `class EvalGraderScoreModel:`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.EvalListPage;
import com.openai.models.evals.EvalListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalListPage page = client.evals().list();
    }
}
```

## Create

`EvalCreateResponse evals().create(EvalCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/evals`

Create the structure of an evaluation that can be used to test a model's performance.
An evaluation is a set of testing criteria and the config for a data source, which dictates the schema of the data used in the evaluation. After creating an evaluation, you can run it on different models and model parameters. We support several types of graders and datasources.
For more information, see the [Evals guide](https://platform.openai.com/docs/guides/evals).

### Parameters

- `EvalCreateParams params`

  - `DataSourceConfig dataSourceConfig`

    The configuration for the data source used for the evaluation runs. Dictates the schema of the data used in the evaluation.

    - `class Custom:`

      A CustomDataSourceConfig object that defines the schema for the data source used for the evaluation runs.
      This schema is used to define the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `ItemSchema itemSchema`

        The json schema for each row in the data source.

      - `JsonValue; type "custom"constant`

        The type of data source. Always `custom`.

        - `CUSTOM("custom")`

      - `Optional<Boolean> includeSampleSchema`

        Whether the eval should expect you to populate the sample namespace (ie, by generating responses off of your data source)

    - `class Logs:`

      A data source config which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.

      - `JsonValue; type "logs"constant`

        The type of data source. Always `logs`.

        - `LOGS("logs")`

      - `Optional<Metadata> metadata`

        Metadata filters for the logs data source.

    - `class StoredCompletions:`

      Deprecated in favor of LogsDataSourceConfig.

      - `JsonValue; type "stored_completions"constant`

        The type of data source. Always `stored_completions`.

        - `STORED_COMPLETIONS("stored_completions")`

      - `Optional<Metadata> metadata`

        Metadata filters for the stored completions data source.

  - `List<TestingCriterion> testingCriteria`

    A list of graders for all eval runs in this group. Graders can reference variables in the data source using double curly braces notation, like `{{item.variable_name}}`. To reference the model's output, use the `sample` namespace (ie, `{{sample.output_text}}`).

    - `class LabelModel:`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `List<Input> input`

        A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

        - `class SimpleInputMessage:`

          - `String content`

            The content of the message.

          - `String role`

            The role of the message (e.g. "system", "assistant", "user").

        - `class EvalItem:`

          A message input to the model with a role indicating instruction following
          hierarchy. Instructions given with the `developer` or `system` role take
          precedence over instructions given with the `user` role. Messages with the
          `assistant` role are presumed to have been generated by the model in previous
          interactions.

          - `Content content`

            Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

            - `String`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `class OutputText:`

              A text output from the model.

              - `String text`

                The text output from the model.

              - `JsonValue; type "output_text"constant`

                The type of the output text. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

            - `class InputImage:`

              An image input block used within EvalItem content arrays.

              - `String imageUrl`

                The URL of the image input.

              - `JsonValue; type "input_image"constant`

                The type of the image input. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio:`

              An audio input to the model.

              - `InputAudio inputAudio`

                - `String data`

                  Base64-encoded audio data.

                - `Format format`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `MP3("mp3")`

                  - `WAV("wav")`

              - `JsonValue; type "input_audio"constant`

                The type of the input item. Always `input_audio`.

                - `INPUT_AUDIO("input_audio")`

            - `List<EvalContentItem>`

              - `String`

              - `class ResponseInputText:`

                A text input to the model.

                - `String text`

                  The text input to the model.

                - `JsonValue; type "input_text"constant`

                  The type of the input item. Always `input_text`.

                  - `INPUT_TEXT("input_text")`

              - `OutputText`

                - `String text`

                  The text output from the model.

                - `JsonValue; type "output_text"constant`

                  The type of the output text. Always `output_text`.

                  - `OUTPUT_TEXT("output_text")`

              - `InputImage`

                - `String imageUrl`

                  The URL of the image input.

                - `JsonValue; type "input_image"constant`

                  The type of the image input. Always `input_image`.

                  - `INPUT_IMAGE("input_image")`

                - `Optional<String> detail`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `class ResponseInputAudio:`

                An audio input to the model.

                - `InputAudio inputAudio`

                  - `String data`

                    Base64-encoded audio data.

                  - `Format format`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `MP3("mp3")`

                    - `WAV("wav")`

                - `JsonValue; type "input_audio"constant`

                  The type of the input item. Always `input_audio`.

                  - `INPUT_AUDIO("input_audio")`

          - `Role role`

            The role of the message input. One of `user`, `assistant`, `system`, or
            `developer`.

            - `USER("user")`

            - `ASSISTANT("assistant")`

            - `SYSTEM("system")`

            - `DEVELOPER("developer")`

          - `Optional<Type> type`

            The type of the message input. Always `message`.

            - `MESSAGE("message")`

      - `List<String> labels`

        The labels to classify to each item in the evaluation.

      - `String model`

        The model to use for the evaluation. Must support structured outputs.

      - `String name`

        The name of the grader.

      - `List<String> passingLabels`

        The labels that indicate a passing result. Must be a subset of labels.

      - `JsonValue; type "label_model"constant`

        The object type, which is always `label_model`.

        - `LABEL_MODEL("label_model")`

    - `class StringCheckGrader:`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `String input`

        The input text. This may include template strings.

      - `String name`

        The name of the grader.

      - `Operation operation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `EQ("eq")`

        - `NE("ne")`

        - `LIKE("like")`

        - `ILIKE("ilike")`

      - `String reference`

        The reference text. This may include template strings.

      - `JsonValue; type "string_check"constant`

        The object type, which is always `string_check`.

        - `STRING_CHECK("string_check")`

    - `class TextSimilarity:`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `double passThreshold`

        The threshold for the score.

    - `class Python:`

      A PythonGrader object that runs a python script on the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

    - `class ScoreModel:`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> name`

    The name of the evaluation.

### Returns

- `class EvalCreateResponse:`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `String id`

    Unique identifier for the evaluation.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the eval was created.

  - `DataSourceConfig dataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig:`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "custom"constant`

        The type of data source. Always `custom`.

        - `CUSTOM("custom")`

    - `class Logs:`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "logs"constant`

        The type of data source. Always `logs`.

        - `LOGS("logs")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig:`

      Deprecated in favor of LogsDataSourceConfig.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "stored_completions"constant`

        The type of data source. Always `stored_completions`.

        - `STORED_COMPLETIONS("stored_completions")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the evaluation.

  - `JsonValue; object_ "eval"constant`

    The object type.

    - `EVAL("eval")`

  - `List<TestingCriterion> testingCriteria`

    A list of testing criteria.

    - `class LabelModelGrader:`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `List<Input> input`

        - `Content content`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

          - `class ResponseInputText:`

            A text input to the model.

            - `String text`

              The text input to the model.

            - `JsonValue; type "input_text"constant`

              The type of the input item. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `class OutputText:`

            A text output from the model.

            - `String text`

              The text output from the model.

            - `JsonValue; type "output_text"constant`

              The type of the output text. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

          - `class InputImage:`

            An image input block used within EvalItem content arrays.

            - `String imageUrl`

              The URL of the image input.

            - `JsonValue; type "input_image"constant`

              The type of the image input. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

            - `Optional<String> detail`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio:`

            An audio input to the model.

            - `InputAudio inputAudio`

              - `String data`

                Base64-encoded audio data.

              - `Format format`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `MP3("mp3")`

                - `WAV("wav")`

            - `JsonValue; type "input_audio"constant`

              The type of the input item. Always `input_audio`.

              - `INPUT_AUDIO("input_audio")`

          - `List<EvalContentItem>`

            - `String`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `OutputText`

              - `String text`

                The text output from the model.

              - `JsonValue; type "output_text"constant`

                The type of the output text. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image input.

              - `JsonValue; type "input_image"constant`

                The type of the image input. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio:`

              An audio input to the model.

              - `InputAudio inputAudio`

                - `String data`

                  Base64-encoded audio data.

                - `Format format`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `MP3("mp3")`

                  - `WAV("wav")`

              - `JsonValue; type "input_audio"constant`

                The type of the input item. Always `input_audio`.

                - `INPUT_AUDIO("input_audio")`

        - `Role role`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Type> type`

          The type of the message input. Always `message`.

          - `MESSAGE("message")`

      - `List<String> labels`

        The labels to assign to each item in the evaluation.

      - `String model`

        The model to use for the evaluation. Must support structured outputs.

      - `String name`

        The name of the grader.

      - `List<String> passingLabels`

        The labels that indicate a passing result. Must be a subset of labels.

      - `JsonValue; type "label_model"constant`

        The object type, which is always `label_model`.

        - `LABEL_MODEL("label_model")`

    - `class StringCheckGrader:`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `String input`

        The input text. This may include template strings.

      - `String name`

        The name of the grader.

      - `Operation operation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `EQ("eq")`

        - `NE("ne")`

        - `LIKE("like")`

        - `ILIKE("ilike")`

      - `String reference`

        The reference text. This may include template strings.

      - `JsonValue; type "string_check"constant`

        The object type, which is always `string_check`.

        - `STRING_CHECK("string_check")`

    - `class EvalGraderTextSimilarity:`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `double passThreshold`

        The threshold for the score.

    - `class EvalGraderPython:`

      A PythonGrader object that runs a python script on the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

    - `class EvalGraderScoreModel:`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.evals.EvalCreateParams;
import com.openai.models.evals.EvalCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalCreateParams params = EvalCreateParams.builder()
            .customDataSourceConfig(EvalCreateParams.DataSourceConfig.Custom.ItemSchema.builder()
                .putAdditionalProperty("foo", JsonValue.from("bar"))
                .build())
            .addTestingCriterion(EvalCreateParams.TestingCriterion.LabelModel.builder()
                .addInput(EvalCreateParams.TestingCriterion.LabelModel.Input.SimpleInputMessage.builder()
                    .content("content")
                    .role("role")
                    .build())
                .addLabel("string")
                .model("model")
                .name("name")
                .addPassingLabel("string")
                .build())
            .build();
        EvalCreateResponse eval = client.evals().create(params);
    }
}
```

## Retrieve

`EvalRetrieveResponse evals().retrieve(EvalRetrieveParamsparams = EvalRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/evals/{eval_id}`

Get an evaluation by ID.

### Parameters

- `EvalRetrieveParams params`

  - `Optional<String> evalId`

### Returns

- `class EvalRetrieveResponse:`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `String id`

    Unique identifier for the evaluation.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the eval was created.

  - `DataSourceConfig dataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig:`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "custom"constant`

        The type of data source. Always `custom`.

        - `CUSTOM("custom")`

    - `class Logs:`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "logs"constant`

        The type of data source. Always `logs`.

        - `LOGS("logs")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig:`

      Deprecated in favor of LogsDataSourceConfig.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "stored_completions"constant`

        The type of data source. Always `stored_completions`.

        - `STORED_COMPLETIONS("stored_completions")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the evaluation.

  - `JsonValue; object_ "eval"constant`

    The object type.

    - `EVAL("eval")`

  - `List<TestingCriterion> testingCriteria`

    A list of testing criteria.

    - `class LabelModelGrader:`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `List<Input> input`

        - `Content content`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

          - `class ResponseInputText:`

            A text input to the model.

            - `String text`

              The text input to the model.

            - `JsonValue; type "input_text"constant`

              The type of the input item. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `class OutputText:`

            A text output from the model.

            - `String text`

              The text output from the model.

            - `JsonValue; type "output_text"constant`

              The type of the output text. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

          - `class InputImage:`

            An image input block used within EvalItem content arrays.

            - `String imageUrl`

              The URL of the image input.

            - `JsonValue; type "input_image"constant`

              The type of the image input. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

            - `Optional<String> detail`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio:`

            An audio input to the model.

            - `InputAudio inputAudio`

              - `String data`

                Base64-encoded audio data.

              - `Format format`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `MP3("mp3")`

                - `WAV("wav")`

            - `JsonValue; type "input_audio"constant`

              The type of the input item. Always `input_audio`.

              - `INPUT_AUDIO("input_audio")`

          - `List<EvalContentItem>`

            - `String`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `OutputText`

              - `String text`

                The text output from the model.

              - `JsonValue; type "output_text"constant`

                The type of the output text. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image input.

              - `JsonValue; type "input_image"constant`

                The type of the image input. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio:`

              An audio input to the model.

              - `InputAudio inputAudio`

                - `String data`

                  Base64-encoded audio data.

                - `Format format`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `MP3("mp3")`

                  - `WAV("wav")`

              - `JsonValue; type "input_audio"constant`

                The type of the input item. Always `input_audio`.

                - `INPUT_AUDIO("input_audio")`

        - `Role role`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Type> type`

          The type of the message input. Always `message`.

          - `MESSAGE("message")`

      - `List<String> labels`

        The labels to assign to each item in the evaluation.

      - `String model`

        The model to use for the evaluation. Must support structured outputs.

      - `String name`

        The name of the grader.

      - `List<String> passingLabels`

        The labels that indicate a passing result. Must be a subset of labels.

      - `JsonValue; type "label_model"constant`

        The object type, which is always `label_model`.

        - `LABEL_MODEL("label_model")`

    - `class StringCheckGrader:`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `String input`

        The input text. This may include template strings.

      - `String name`

        The name of the grader.

      - `Operation operation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `EQ("eq")`

        - `NE("ne")`

        - `LIKE("like")`

        - `ILIKE("ilike")`

      - `String reference`

        The reference text. This may include template strings.

      - `JsonValue; type "string_check"constant`

        The object type, which is always `string_check`.

        - `STRING_CHECK("string_check")`

    - `class EvalGraderTextSimilarity:`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `double passThreshold`

        The threshold for the score.

    - `class EvalGraderPython:`

      A PythonGrader object that runs a python script on the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

    - `class EvalGraderScoreModel:`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.EvalRetrieveParams;
import com.openai.models.evals.EvalRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalRetrieveResponse eval = client.evals().retrieve("eval_id");
    }
}
```

## Update

`EvalUpdateResponse evals().update(EvalUpdateParamsparams = EvalUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/evals/{eval_id}`

Update certain properties of an evaluation.

### Parameters

- `EvalUpdateParams params`

  - `Optional<String> evalId`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> name`

    Rename the evaluation.

### Returns

- `class EvalUpdateResponse:`

  An Eval object with a data source config and testing criteria.
  An Eval represents a task to be done for your LLM integration.
  Like:

  - Improve the quality of my chatbot
  - See how well my chatbot handles customer support
  - Check if o4-mini is better at my usecase than gpt-4o

  - `String id`

    Unique identifier for the evaluation.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the eval was created.

  - `DataSourceConfig dataSourceConfig`

    Configuration of data sources used in runs of the evaluation.

    - `class EvalCustomDataSourceConfig:`

      A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
      The response schema defines the shape of the data that will be:

      - Used to define your testing criteria and
      - What data is required when creating a run

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "custom"constant`

        The type of data source. Always `custom`.

        - `CUSTOM("custom")`

    - `class Logs:`

      A LogsDataSourceConfig which specifies the metadata property of your logs query.
      This is usually metadata like `usecase=chatbot` or `prompt-version=v2`, etc.
      The schema returned by this data source config is used to defined what variables are available in your evals.
      `item` and `sample` are both defined when using this data source config.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "logs"constant`

        The type of data source. Always `logs`.

        - `LOGS("logs")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `class EvalStoredCompletionsDataSourceConfig:`

      Deprecated in favor of LogsDataSourceConfig.

      - `Schema schema`

        The json schema for the run data source items.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `JsonValue; type "stored_completions"constant`

        The type of data source. Always `stored_completions`.

        - `STORED_COMPLETIONS("stored_completions")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String name`

    The name of the evaluation.

  - `JsonValue; object_ "eval"constant`

    The object type.

    - `EVAL("eval")`

  - `List<TestingCriterion> testingCriteria`

    A list of testing criteria.

    - `class LabelModelGrader:`

      A LabelModelGrader object which uses a model to assign labels to each item
      in the evaluation.

      - `List<Input> input`

        - `Content content`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `String`

          - `class ResponseInputText:`

            A text input to the model.

            - `String text`

              The text input to the model.

            - `JsonValue; type "input_text"constant`

              The type of the input item. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `class OutputText:`

            A text output from the model.

            - `String text`

              The text output from the model.

            - `JsonValue; type "output_text"constant`

              The type of the output text. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

          - `class InputImage:`

            An image input block used within EvalItem content arrays.

            - `String imageUrl`

              The URL of the image input.

            - `JsonValue; type "input_image"constant`

              The type of the image input. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

            - `Optional<String> detail`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `class ResponseInputAudio:`

            An audio input to the model.

            - `InputAudio inputAudio`

              - `String data`

                Base64-encoded audio data.

              - `Format format`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `MP3("mp3")`

                - `WAV("wav")`

            - `JsonValue; type "input_audio"constant`

              The type of the input item. Always `input_audio`.

              - `INPUT_AUDIO("input_audio")`

          - `List<EvalContentItem>`

            - `String`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `OutputText`

              - `String text`

                The text output from the model.

              - `JsonValue; type "output_text"constant`

                The type of the output text. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image input.

              - `JsonValue; type "input_image"constant`

                The type of the image input. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio:`

              An audio input to the model.

              - `InputAudio inputAudio`

                - `String data`

                  Base64-encoded audio data.

                - `Format format`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `MP3("mp3")`

                  - `WAV("wav")`

              - `JsonValue; type "input_audio"constant`

                The type of the input item. Always `input_audio`.

                - `INPUT_AUDIO("input_audio")`

        - `Role role`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

          - `DEVELOPER("developer")`

        - `Optional<Type> type`

          The type of the message input. Always `message`.

          - `MESSAGE("message")`

      - `List<String> labels`

        The labels to assign to each item in the evaluation.

      - `String model`

        The model to use for the evaluation. Must support structured outputs.

      - `String name`

        The name of the grader.

      - `List<String> passingLabels`

        The labels that indicate a passing result. Must be a subset of labels.

      - `JsonValue; type "label_model"constant`

        The object type, which is always `label_model`.

        - `LABEL_MODEL("label_model")`

    - `class StringCheckGrader:`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `String input`

        The input text. This may include template strings.

      - `String name`

        The name of the grader.

      - `Operation operation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `EQ("eq")`

        - `NE("ne")`

        - `LIKE("like")`

        - `ILIKE("ilike")`

      - `String reference`

        The reference text. This may include template strings.

      - `JsonValue; type "string_check"constant`

        The object type, which is always `string_check`.

        - `STRING_CHECK("string_check")`

    - `class EvalGraderTextSimilarity:`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `double passThreshold`

        The threshold for the score.

    - `class EvalGraderPython:`

      A PythonGrader object that runs a python script on the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

    - `class EvalGraderScoreModel:`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Optional<Double> passThreshold`

        The threshold for the score.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.EvalUpdateParams;
import com.openai.models.evals.EvalUpdateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalUpdateResponse eval = client.evals().update("eval_id");
    }
}
```

## Delete

`EvalDeleteResponse evals().delete(EvalDeleteParamsparams = EvalDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/evals/{eval_id}`

Delete an evaluation.

### Parameters

- `EvalDeleteParams params`

  - `Optional<String> evalId`

### Returns

- `class EvalDeleteResponse:`

  - `boolean deleted`

  - `String evalId`

  - `String object_`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.EvalDeleteParams;
import com.openai.models.evals.EvalDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EvalDeleteResponse eval = client.evals().delete("eval_id");
    }
}
```

### Domain Types

### Eval Custom Data Source Config

- `class EvalCustomDataSourceConfig:`

  A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
  The response schema defines the shape of the data that will be:

  - Used to define your testing criteria and
  - What data is required when creating a run

  - `Schema schema`

    The json schema for the run data source items.
    Learn how to build JSON schemas [here](https://json-schema.org/).

  - `JsonValue; type "custom"constant`

    The type of data source. Always `custom`.

    - `CUSTOM("custom")`

### Eval Stored Completions Data Source Config

- `class EvalStoredCompletionsDataSourceConfig:`

  Deprecated in favor of LogsDataSourceConfig.

  - `Schema schema`

    The json schema for the run data source items.
    Learn how to build JSON schemas [here](https://json-schema.org/).

  - `JsonValue; type "stored_completions"constant`

    The type of data source. Always `stored_completions`.

    - `STORED_COMPLETIONS("stored_completions")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

## Runs

### List

`RunListPage evals().runs().list(RunListParamsparams = RunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/evals/{eval_id}/runs`

Get a list of runs for an evaluation.

#### Parameters

- `RunListParams params`

  - `Optional<String> evalId`

  - `Optional<String> after`

    Identifier for the last run from the previous pagination request.

  - `Optional<Long> limit`

    Number of runs to retrieve.

  - `Optional<Order> order`

    Sort order for runs by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<Status> status`

    Filter runs by status. One of `queued` | `in_progress` | `failed` | `completed` | `canceled`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `COMPLETED("completed")`

    - `CANCELED("canceled")`

    - `FAILED("failed")`

#### Returns

- `class RunListResponse:`

  A schema representing an evaluation run.

  - `String id`

    Unique identifier for the evaluation run.

  - `long createdAt`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `DataSource dataSource`

    Information about the run's data source.

    - `class CreateEvalJsonlRunDataSource:`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `Source source`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

      - `JsonValue; type "jsonl"constant`

        The type of data source. Always `jsonl`.

        - `JSONL("jsonl")`

    - `class CreateEvalCompletionsRunDataSource:`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class StoredCompletions:`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `JsonValue; type "stored_completions"constant`

            The type of source. Always `stored_completions`.

            - `STORED_COMPLETIONS("stored_completions")`

          - `Optional<Long> createdAfter`

            An optional Unix timestamp to filter items created after this time.

          - `Optional<Long> createdBefore`

            An optional Unix timestamp to filter items created before this time.

          - `Optional<Long> limit`

            An optional maximum number of items to return.

          - `Optional<Metadata> metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `Optional<String> model`

            An optional model to filter by (e.g., 'gpt-4o').

      - `Type type`

        The type of run data source. Always `completions`.

        - `COMPLETIONS("completions")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                - `List<ResponseInputContent>`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `class ResponseInputImage:`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `Detail detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `LOW("low")`

                      - `HIGH("high")`

                      - `AUTO("auto")`

                      - `ORIGINAL("original")`

                    - `JsonValue; type "input_image"constant`

                      The type of the input item. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> imageUrl`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile:`

                    A file input to the model.

                    - `JsonValue; type "input_file"constant`

                      The type of the input item. Always `input_file`.

                      - `INPUT_FILE("input_file")`

                    - `Optional<String> fileData`

                      The content of the file to be sent to the model.

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> fileUrl`

                      The URL of the file to be sent to the model.

                    - `Optional<String> filename`

                      The name of the file to be sent to the model.

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Phase> phase`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `COMMENTARY("commentary")`

                - `FINAL_ANSWER("final_answer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

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

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<List<ChatCompletionFunctionTool>> tools`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses:`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class InnerResponses:`

          A EvalResponsesSource object describing a run data source configuration.

          - `JsonValue; type "responses"constant`

            The type of run data source. Always `responses`.

            - `RESPONSES("responses")`

          - `Optional<Long> createdAfter`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<Long> createdBefore`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<String> instructionsSearch`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `Optional<JsonValue> metadata`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `Optional<String> model`

            The name of the model to find responses for. This is a query parameter used to select responses.

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

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Double> temperature`

            Sampling temperature. This is a query parameter used to select responses.

          - `Optional<List<String>> tools`

            List of tool names. This is a query parameter used to select responses.

          - `Optional<Double> topP`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `Optional<List<String>> users`

            List of user identifiers. This is a query parameter used to select responses.

      - `JsonValue; type "responses"constant`

        The type of run data source. Always `responses`.

        - `RESPONSES("responses")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage:`

              - `String content`

                The content of the message.

              - `String role`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<Text> text`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `Optional<ResponseFormatTextConfig> format`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText:`

              Default response format. Used to generate text responses.

              - `JsonValue; type "text"constant`

                The type of response format being defined. Always `text`.

                - `TEXT("text")`

            - `class ResponseFormatTextJsonSchemaConfig:`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `String name`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `Schema schema`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `JsonValue; type "json_schema"constant`

                The type of response format being defined. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

              - `Optional<String> description`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `Optional<Boolean> strict`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJsonObject:`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `JsonValue; type "json_object"constant`

                The type of response format being defined. Always `json_object`.

                - `JSON_OBJECT("json_object")`

        - `Optional<List<Tool>> tools`

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

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether to enforce strict parameter validation. Default `true`.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `String key`

                      The key to compare against the value.

                    - `Type type`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `EQ("eq")`

                      - `NE("ne")`

                      - `GT("gt")`

                      - `GTE("gte")`

                      - `LT("lt")`

                      - `LTE("lte")`

                    - `Value value`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `double`

                      - `boolean`

                      - `List<ComparisonFilterValueItem>`

                        - `String`

                        - `double`

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. Default: `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `String name`

                  The name of the custom tool, used to identify it in tool calls.

                - `JsonValue; type "custom"constant`

                  The type of the custom tool. Always `custom`.

                  - `CUSTOM("custom")`

                - `Optional<Boolean> deferLoading`

                  Whether this tool should be deferred and discovered via tool search.

                - `Optional<String> description`

                  Optional description of the custom tool, used to provide more context.

                - `Optional<CustomToolInputFormat> format`

                  The input format for the custom tool. Default is unconstrained text.

                  - `JsonValue;`

                    - `JsonValue; type "text"constant`

                      Unconstrained text format. Always `text`.

                      - `TEXT("text")`

                  - `Grammar`

                    - `String definition`

                      The grammar definition.

                    - `Syntax syntax`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `LARK("lark")`

                      - `REGEX("regex")`

                    - `JsonValue; type "grammar"constant`

                      Grammar format. Always `grammar`.

                      - `GRAMMAR("grammar")`

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The user's location.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `EvalApiError error`

    An object representing an error response from the Eval API.

    - `String code`

      The error code.

    - `String message`

      The error message.

  - `String evalId`

    The identifier of the associated evaluation.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that is evaluated, if applicable.

  - `String name`

    The name of the evaluation run.

  - `JsonValue; object_ "eval.run"constant`

    The type of the object. Always "eval.run".

    - `EVAL_RUN("eval.run")`

  - `List<PerModelUsage> perModelUsage`

    Usage statistics for each model during the evaluation run.

    - `long cachedTokens`

      The number of tokens retrieved from cache.

    - `long completionTokens`

      The number of completion tokens generated.

    - `long invocationCount`

      The number of invocations.

    - `String modelName`

      The name of the model.

    - `long promptTokens`

      The number of prompt tokens used.

    - `long totalTokens`

      The total number of tokens used.

  - `List<PerTestingCriteriaResult> perTestingCriteriaResults`

    Results per testing criteria applied during the evaluation run.

    - `long failed`

      Number of tests failed for this criteria.

    - `long passed`

      Number of tests passed for this criteria.

    - `String testingCriteria`

      A description of the testing criteria.

  - `String reportUrl`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `ResultCounts resultCounts`

    Counters summarizing the outcomes of the evaluation run.

    - `long errored`

      Number of output items that resulted in an error.

    - `long failed`

      Number of output items that failed to pass the evaluation.

    - `long passed`

      Number of output items that passed the evaluation.

    - `long total`

      Total number of executed output items.

  - `String status`

    The status of the evaluation run.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.runs.RunListPage;
import com.openai.models.evals.runs.RunListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunListPage page = client.evals().runs().list("eval_id");
    }
}
```

### Create

`RunCreateResponse evals().runs().create(RunCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/evals/{eval_id}/runs`

Kicks off a new run for a given evaluation, specifying the data source, and what model configuration to use to test. The datasource will be validated against the schema specified in the config of the evaluation.

#### Parameters

- `RunCreateParams params`

  - `Optional<String> evalId`

  - `DataSource dataSource`

    Details about the run's data source.

    - `class CreateEvalJsonlRunDataSource:`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `Source source`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

      - `JsonValue; type "jsonl"constant`

        The type of data source. Always `jsonl`.

        - `JSONL("jsonl")`

    - `class CreateEvalCompletionsRunDataSource:`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class StoredCompletions:`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `JsonValue; type "stored_completions"constant`

            The type of source. Always `stored_completions`.

            - `STORED_COMPLETIONS("stored_completions")`

          - `Optional<Long> createdAfter`

            An optional Unix timestamp to filter items created after this time.

          - `Optional<Long> createdBefore`

            An optional Unix timestamp to filter items created before this time.

          - `Optional<Long> limit`

            An optional maximum number of items to return.

          - `Optional<Metadata> metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `Optional<String> model`

            An optional model to filter by (e.g., 'gpt-4o').

      - `Type type`

        The type of run data source. Always `completions`.

        - `COMPLETIONS("completions")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                - `List<ResponseInputContent>`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `class ResponseInputImage:`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `Detail detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `LOW("low")`

                      - `HIGH("high")`

                      - `AUTO("auto")`

                      - `ORIGINAL("original")`

                    - `JsonValue; type "input_image"constant`

                      The type of the input item. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> imageUrl`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile:`

                    A file input to the model.

                    - `JsonValue; type "input_file"constant`

                      The type of the input item. Always `input_file`.

                      - `INPUT_FILE("input_file")`

                    - `Optional<String> fileData`

                      The content of the file to be sent to the model.

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> fileUrl`

                      The URL of the file to be sent to the model.

                    - `Optional<String> filename`

                      The name of the file to be sent to the model.

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Phase> phase`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `COMMENTARY("commentary")`

                - `FINAL_ANSWER("final_answer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

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

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<List<ChatCompletionFunctionTool>> tools`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class CreateEvalResponsesRunDataSource:`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class Responses:`

          A EvalResponsesSource object describing a run data source configuration.

          - `JsonValue; type "responses"constant`

            The type of run data source. Always `responses`.

            - `RESPONSES("responses")`

          - `Optional<Long> createdAfter`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<Long> createdBefore`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<String> instructionsSearch`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `Optional<JsonValue> metadata`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `Optional<String> model`

            The name of the model to find responses for. This is a query parameter used to select responses.

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

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Double> temperature`

            Sampling temperature. This is a query parameter used to select responses.

          - `Optional<List<String>> tools`

            List of tool names. This is a query parameter used to select responses.

          - `Optional<Double> topP`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `Optional<List<String>> users`

            List of user identifiers. This is a query parameter used to select responses.

      - `Type type`

        The type of run data source. Always `responses`.

        - `RESPONSES("responses")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage:`

              - `String content`

                The content of the message.

              - `String role`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<Text> text`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `Optional<ResponseFormatTextConfig> format`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText:`

              Default response format. Used to generate text responses.

              - `JsonValue; type "text"constant`

                The type of response format being defined. Always `text`.

                - `TEXT("text")`

            - `class ResponseFormatTextJsonSchemaConfig:`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `String name`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `Schema schema`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `JsonValue; type "json_schema"constant`

                The type of response format being defined. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

              - `Optional<String> description`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `Optional<Boolean> strict`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJsonObject:`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `JsonValue; type "json_object"constant`

                The type of response format being defined. Always `json_object`.

                - `JSON_OBJECT("json_object")`

        - `Optional<List<Tool>> tools`

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

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether to enforce strict parameter validation. Default `true`.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `String key`

                      The key to compare against the value.

                    - `Type type`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `EQ("eq")`

                      - `NE("ne")`

                      - `GT("gt")`

                      - `GTE("gte")`

                      - `LT("lt")`

                      - `LTE("lte")`

                    - `Value value`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `double`

                      - `boolean`

                      - `List<ComparisonFilterValueItem>`

                        - `String`

                        - `double`

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. Default: `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `String name`

                  The name of the custom tool, used to identify it in tool calls.

                - `JsonValue; type "custom"constant`

                  The type of the custom tool. Always `custom`.

                  - `CUSTOM("custom")`

                - `Optional<Boolean> deferLoading`

                  Whether this tool should be deferred and discovered via tool search.

                - `Optional<String> description`

                  Optional description of the custom tool, used to provide more context.

                - `Optional<CustomToolInputFormat> format`

                  The input format for the custom tool. Default is unconstrained text.

                  - `JsonValue;`

                    - `JsonValue; type "text"constant`

                      Unconstrained text format. Always `text`.

                      - `TEXT("text")`

                  - `Grammar`

                    - `String definition`

                      The grammar definition.

                    - `Syntax syntax`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `LARK("lark")`

                      - `REGEX("regex")`

                    - `JsonValue; type "grammar"constant`

                      Grammar format. Always `grammar`.

                      - `GRAMMAR("grammar")`

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The user's location.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> name`

    The name of the run.

#### Returns

- `class RunCreateResponse:`

  A schema representing an evaluation run.

  - `String id`

    Unique identifier for the evaluation run.

  - `long createdAt`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `DataSource dataSource`

    Information about the run's data source.

    - `class CreateEvalJsonlRunDataSource:`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `Source source`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

      - `JsonValue; type "jsonl"constant`

        The type of data source. Always `jsonl`.

        - `JSONL("jsonl")`

    - `class CreateEvalCompletionsRunDataSource:`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class StoredCompletions:`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `JsonValue; type "stored_completions"constant`

            The type of source. Always `stored_completions`.

            - `STORED_COMPLETIONS("stored_completions")`

          - `Optional<Long> createdAfter`

            An optional Unix timestamp to filter items created after this time.

          - `Optional<Long> createdBefore`

            An optional Unix timestamp to filter items created before this time.

          - `Optional<Long> limit`

            An optional maximum number of items to return.

          - `Optional<Metadata> metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `Optional<String> model`

            An optional model to filter by (e.g., 'gpt-4o').

      - `Type type`

        The type of run data source. Always `completions`.

        - `COMPLETIONS("completions")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                - `List<ResponseInputContent>`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `class ResponseInputImage:`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `Detail detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `LOW("low")`

                      - `HIGH("high")`

                      - `AUTO("auto")`

                      - `ORIGINAL("original")`

                    - `JsonValue; type "input_image"constant`

                      The type of the input item. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> imageUrl`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile:`

                    A file input to the model.

                    - `JsonValue; type "input_file"constant`

                      The type of the input item. Always `input_file`.

                      - `INPUT_FILE("input_file")`

                    - `Optional<String> fileData`

                      The content of the file to be sent to the model.

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> fileUrl`

                      The URL of the file to be sent to the model.

                    - `Optional<String> filename`

                      The name of the file to be sent to the model.

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Phase> phase`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `COMMENTARY("commentary")`

                - `FINAL_ANSWER("final_answer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

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

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<List<ChatCompletionFunctionTool>> tools`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses:`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class InnerResponses:`

          A EvalResponsesSource object describing a run data source configuration.

          - `JsonValue; type "responses"constant`

            The type of run data source. Always `responses`.

            - `RESPONSES("responses")`

          - `Optional<Long> createdAfter`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<Long> createdBefore`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<String> instructionsSearch`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `Optional<JsonValue> metadata`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `Optional<String> model`

            The name of the model to find responses for. This is a query parameter used to select responses.

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

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Double> temperature`

            Sampling temperature. This is a query parameter used to select responses.

          - `Optional<List<String>> tools`

            List of tool names. This is a query parameter used to select responses.

          - `Optional<Double> topP`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `Optional<List<String>> users`

            List of user identifiers. This is a query parameter used to select responses.

      - `JsonValue; type "responses"constant`

        The type of run data source. Always `responses`.

        - `RESPONSES("responses")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage:`

              - `String content`

                The content of the message.

              - `String role`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<Text> text`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `Optional<ResponseFormatTextConfig> format`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText:`

              Default response format. Used to generate text responses.

              - `JsonValue; type "text"constant`

                The type of response format being defined. Always `text`.

                - `TEXT("text")`

            - `class ResponseFormatTextJsonSchemaConfig:`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `String name`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `Schema schema`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `JsonValue; type "json_schema"constant`

                The type of response format being defined. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

              - `Optional<String> description`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `Optional<Boolean> strict`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJsonObject:`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `JsonValue; type "json_object"constant`

                The type of response format being defined. Always `json_object`.

                - `JSON_OBJECT("json_object")`

        - `Optional<List<Tool>> tools`

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

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether to enforce strict parameter validation. Default `true`.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `String key`

                      The key to compare against the value.

                    - `Type type`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `EQ("eq")`

                      - `NE("ne")`

                      - `GT("gt")`

                      - `GTE("gte")`

                      - `LT("lt")`

                      - `LTE("lte")`

                    - `Value value`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `double`

                      - `boolean`

                      - `List<ComparisonFilterValueItem>`

                        - `String`

                        - `double`

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. Default: `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `String name`

                  The name of the custom tool, used to identify it in tool calls.

                - `JsonValue; type "custom"constant`

                  The type of the custom tool. Always `custom`.

                  - `CUSTOM("custom")`

                - `Optional<Boolean> deferLoading`

                  Whether this tool should be deferred and discovered via tool search.

                - `Optional<String> description`

                  Optional description of the custom tool, used to provide more context.

                - `Optional<CustomToolInputFormat> format`

                  The input format for the custom tool. Default is unconstrained text.

                  - `JsonValue;`

                    - `JsonValue; type "text"constant`

                      Unconstrained text format. Always `text`.

                      - `TEXT("text")`

                  - `Grammar`

                    - `String definition`

                      The grammar definition.

                    - `Syntax syntax`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `LARK("lark")`

                      - `REGEX("regex")`

                    - `JsonValue; type "grammar"constant`

                      Grammar format. Always `grammar`.

                      - `GRAMMAR("grammar")`

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The user's location.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `EvalApiError error`

    An object representing an error response from the Eval API.

    - `String code`

      The error code.

    - `String message`

      The error message.

  - `String evalId`

    The identifier of the associated evaluation.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that is evaluated, if applicable.

  - `String name`

    The name of the evaluation run.

  - `JsonValue; object_ "eval.run"constant`

    The type of the object. Always "eval.run".

    - `EVAL_RUN("eval.run")`

  - `List<PerModelUsage> perModelUsage`

    Usage statistics for each model during the evaluation run.

    - `long cachedTokens`

      The number of tokens retrieved from cache.

    - `long completionTokens`

      The number of completion tokens generated.

    - `long invocationCount`

      The number of invocations.

    - `String modelName`

      The name of the model.

    - `long promptTokens`

      The number of prompt tokens used.

    - `long totalTokens`

      The total number of tokens used.

  - `List<PerTestingCriteriaResult> perTestingCriteriaResults`

    Results per testing criteria applied during the evaluation run.

    - `long failed`

      Number of tests failed for this criteria.

    - `long passed`

      Number of tests passed for this criteria.

    - `String testingCriteria`

      A description of the testing criteria.

  - `String reportUrl`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `ResultCounts resultCounts`

    Counters summarizing the outcomes of the evaluation run.

    - `long errored`

      Number of output items that resulted in an error.

    - `long failed`

      Number of output items that failed to pass the evaluation.

    - `long passed`

      Number of output items that passed the evaluation.

    - `long total`

      Total number of executed output items.

  - `String status`

    The status of the evaluation run.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.evals.runs.CreateEvalJsonlRunDataSource;
import com.openai.models.evals.runs.RunCreateParams;
import com.openai.models.evals.runs.RunCreateResponse;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunCreateParams params = RunCreateParams.builder()
            .evalId("eval_id")
            .dataSource(CreateEvalJsonlRunDataSource.builder()
                .fileContentSource(List.of(CreateEvalJsonlRunDataSource.Source.FileContent.Content.builder()
                    .item(CreateEvalJsonlRunDataSource.Source.FileContent.Content.Item.builder()
                        .putAdditionalProperty("foo", JsonValue.from("bar"))
                        .build())
                    .build()))
                .build())
            .build();
        RunCreateResponse run = client.evals().runs().create(params);
    }
}
```

### Retrieve

`RunRetrieveResponse evals().runs().retrieve(RunRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/evals/{eval_id}/runs/{run_id}`

Get an evaluation run by ID.

#### Parameters

- `RunRetrieveParams params`

  - `String evalId`

  - `Optional<String> runId`

#### Returns

- `class RunRetrieveResponse:`

  A schema representing an evaluation run.

  - `String id`

    Unique identifier for the evaluation run.

  - `long createdAt`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `DataSource dataSource`

    Information about the run's data source.

    - `class CreateEvalJsonlRunDataSource:`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `Source source`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

      - `JsonValue; type "jsonl"constant`

        The type of data source. Always `jsonl`.

        - `JSONL("jsonl")`

    - `class CreateEvalCompletionsRunDataSource:`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class StoredCompletions:`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `JsonValue; type "stored_completions"constant`

            The type of source. Always `stored_completions`.

            - `STORED_COMPLETIONS("stored_completions")`

          - `Optional<Long> createdAfter`

            An optional Unix timestamp to filter items created after this time.

          - `Optional<Long> createdBefore`

            An optional Unix timestamp to filter items created before this time.

          - `Optional<Long> limit`

            An optional maximum number of items to return.

          - `Optional<Metadata> metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `Optional<String> model`

            An optional model to filter by (e.g., 'gpt-4o').

      - `Type type`

        The type of run data source. Always `completions`.

        - `COMPLETIONS("completions")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                - `List<ResponseInputContent>`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `class ResponseInputImage:`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `Detail detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `LOW("low")`

                      - `HIGH("high")`

                      - `AUTO("auto")`

                      - `ORIGINAL("original")`

                    - `JsonValue; type "input_image"constant`

                      The type of the input item. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> imageUrl`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile:`

                    A file input to the model.

                    - `JsonValue; type "input_file"constant`

                      The type of the input item. Always `input_file`.

                      - `INPUT_FILE("input_file")`

                    - `Optional<String> fileData`

                      The content of the file to be sent to the model.

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> fileUrl`

                      The URL of the file to be sent to the model.

                    - `Optional<String> filename`

                      The name of the file to be sent to the model.

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Phase> phase`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `COMMENTARY("commentary")`

                - `FINAL_ANSWER("final_answer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

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

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<List<ChatCompletionFunctionTool>> tools`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses:`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class InnerResponses:`

          A EvalResponsesSource object describing a run data source configuration.

          - `JsonValue; type "responses"constant`

            The type of run data source. Always `responses`.

            - `RESPONSES("responses")`

          - `Optional<Long> createdAfter`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<Long> createdBefore`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<String> instructionsSearch`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `Optional<JsonValue> metadata`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `Optional<String> model`

            The name of the model to find responses for. This is a query parameter used to select responses.

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

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Double> temperature`

            Sampling temperature. This is a query parameter used to select responses.

          - `Optional<List<String>> tools`

            List of tool names. This is a query parameter used to select responses.

          - `Optional<Double> topP`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `Optional<List<String>> users`

            List of user identifiers. This is a query parameter used to select responses.

      - `JsonValue; type "responses"constant`

        The type of run data source. Always `responses`.

        - `RESPONSES("responses")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage:`

              - `String content`

                The content of the message.

              - `String role`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<Text> text`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `Optional<ResponseFormatTextConfig> format`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText:`

              Default response format. Used to generate text responses.

              - `JsonValue; type "text"constant`

                The type of response format being defined. Always `text`.

                - `TEXT("text")`

            - `class ResponseFormatTextJsonSchemaConfig:`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `String name`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `Schema schema`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `JsonValue; type "json_schema"constant`

                The type of response format being defined. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

              - `Optional<String> description`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `Optional<Boolean> strict`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJsonObject:`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `JsonValue; type "json_object"constant`

                The type of response format being defined. Always `json_object`.

                - `JSON_OBJECT("json_object")`

        - `Optional<List<Tool>> tools`

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

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether to enforce strict parameter validation. Default `true`.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `String key`

                      The key to compare against the value.

                    - `Type type`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `EQ("eq")`

                      - `NE("ne")`

                      - `GT("gt")`

                      - `GTE("gte")`

                      - `LT("lt")`

                      - `LTE("lte")`

                    - `Value value`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `double`

                      - `boolean`

                      - `List<ComparisonFilterValueItem>`

                        - `String`

                        - `double`

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. Default: `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `String name`

                  The name of the custom tool, used to identify it in tool calls.

                - `JsonValue; type "custom"constant`

                  The type of the custom tool. Always `custom`.

                  - `CUSTOM("custom")`

                - `Optional<Boolean> deferLoading`

                  Whether this tool should be deferred and discovered via tool search.

                - `Optional<String> description`

                  Optional description of the custom tool, used to provide more context.

                - `Optional<CustomToolInputFormat> format`

                  The input format for the custom tool. Default is unconstrained text.

                  - `JsonValue;`

                    - `JsonValue; type "text"constant`

                      Unconstrained text format. Always `text`.

                      - `TEXT("text")`

                  - `Grammar`

                    - `String definition`

                      The grammar definition.

                    - `Syntax syntax`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `LARK("lark")`

                      - `REGEX("regex")`

                    - `JsonValue; type "grammar"constant`

                      Grammar format. Always `grammar`.

                      - `GRAMMAR("grammar")`

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The user's location.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `EvalApiError error`

    An object representing an error response from the Eval API.

    - `String code`

      The error code.

    - `String message`

      The error message.

  - `String evalId`

    The identifier of the associated evaluation.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that is evaluated, if applicable.

  - `String name`

    The name of the evaluation run.

  - `JsonValue; object_ "eval.run"constant`

    The type of the object. Always "eval.run".

    - `EVAL_RUN("eval.run")`

  - `List<PerModelUsage> perModelUsage`

    Usage statistics for each model during the evaluation run.

    - `long cachedTokens`

      The number of tokens retrieved from cache.

    - `long completionTokens`

      The number of completion tokens generated.

    - `long invocationCount`

      The number of invocations.

    - `String modelName`

      The name of the model.

    - `long promptTokens`

      The number of prompt tokens used.

    - `long totalTokens`

      The total number of tokens used.

  - `List<PerTestingCriteriaResult> perTestingCriteriaResults`

    Results per testing criteria applied during the evaluation run.

    - `long failed`

      Number of tests failed for this criteria.

    - `long passed`

      Number of tests passed for this criteria.

    - `String testingCriteria`

      A description of the testing criteria.

  - `String reportUrl`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `ResultCounts resultCounts`

    Counters summarizing the outcomes of the evaluation run.

    - `long errored`

      Number of output items that resulted in an error.

    - `long failed`

      Number of output items that failed to pass the evaluation.

    - `long passed`

      Number of output items that passed the evaluation.

    - `long total`

      Total number of executed output items.

  - `String status`

    The status of the evaluation run.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.runs.RunRetrieveParams;
import com.openai.models.evals.runs.RunRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunRetrieveParams params = RunRetrieveParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .build();
        RunRetrieveResponse run = client.evals().runs().retrieve(params);
    }
}
```

### Cancel

`RunCancelResponse evals().runs().cancel(RunCancelParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/evals/{eval_id}/runs/{run_id}`

Cancel an ongoing evaluation run.

#### Parameters

- `RunCancelParams params`

  - `String evalId`

  - `Optional<String> runId`

#### Returns

- `class RunCancelResponse:`

  A schema representing an evaluation run.

  - `String id`

    Unique identifier for the evaluation run.

  - `long createdAt`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `DataSource dataSource`

    Information about the run's data source.

    - `class CreateEvalJsonlRunDataSource:`

      A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

      - `Source source`

        Determines what populates the `item` namespace in the data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

      - `JsonValue; type "jsonl"constant`

        The type of data source. Always `jsonl`.

        - `JSONL("jsonl")`

    - `class CreateEvalCompletionsRunDataSource:`

      A CompletionsRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class StoredCompletions:`

          A StoredCompletionsRunDataSource configuration describing a set of filters

          - `JsonValue; type "stored_completions"constant`

            The type of source. Always `stored_completions`.

            - `STORED_COMPLETIONS("stored_completions")`

          - `Optional<Long> createdAfter`

            An optional Unix timestamp to filter items created after this time.

          - `Optional<Long> createdBefore`

            An optional Unix timestamp to filter items created before this time.

          - `Optional<Long> limit`

            An optional maximum number of items to return.

          - `Optional<Metadata> metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

          - `Optional<String> model`

            An optional model to filter by (e.g., 'gpt-4o').

      - `Type type`

        The type of run data source. Always `completions`.

        - `COMPLETIONS("completions")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class EasyInputMessage:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Text, image, or audio input to the model, used to generate a response.
                Can also contain previous assistant responses.

                - `String`

                - `List<ResponseInputContent>`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `class ResponseInputImage:`

                    An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                    - `Detail detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                      - `LOW("low")`

                      - `HIGH("high")`

                      - `AUTO("auto")`

                      - `ORIGINAL("original")`

                    - `JsonValue; type "input_image"constant`

                      The type of the input item. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> imageUrl`

                      The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

                  - `class ResponseInputFile:`

                    A file input to the model.

                    - `JsonValue; type "input_file"constant`

                      The type of the input item. Always `input_file`.

                      - `INPUT_FILE("input_file")`

                    - `Optional<String> fileData`

                      The content of the file to be sent to the model.

                    - `Optional<String> fileId`

                      The ID of the file to be sent to the model.

                    - `Optional<String> fileUrl`

                      The URL of the file to be sent to the model.

                    - `Optional<String> filename`

                      The name of the file to be sent to the model.

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Phase> phase`

                Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
                For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
                phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

                - `COMMENTARY("commentary")`

                - `FINAL_ANSWER("final_answer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

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

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<List<ChatCompletionFunctionTool>> tools`

          A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class Responses:`

      A ResponsesRunDataSource object describing a model sampling configuration.

      - `Source source`

        Determines what populates the `item` namespace in this run's data source.

        - `class FileContent:`

          - `List<Content> content`

            The content of the jsonl file.

            - `Item item`

            - `Optional<Sample> sample`

          - `JsonValue; type "file_content"constant`

            The type of jsonl source. Always `file_content`.

            - `FILE_CONTENT("file_content")`

        - `class FileId:`

          - `String id`

            The identifier of the file.

          - `JsonValue; type "file_id"constant`

            The type of jsonl source. Always `file_id`.

            - `FILE_ID("file_id")`

        - `class InnerResponses:`

          A EvalResponsesSource object describing a run data source configuration.

          - `JsonValue; type "responses"constant`

            The type of run data source. Always `responses`.

            - `RESPONSES("responses")`

          - `Optional<Long> createdAfter`

            Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<Long> createdBefore`

            Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

          - `Optional<String> instructionsSearch`

            Optional string to search the 'instructions' field. This is a query parameter used to select responses.

          - `Optional<JsonValue> metadata`

            Metadata filter for the responses. This is a query parameter used to select responses.

          - `Optional<String> model`

            The name of the model to find responses for. This is a query parameter used to select responses.

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

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

          - `Optional<Double> temperature`

            Sampling temperature. This is a query parameter used to select responses.

          - `Optional<List<String>> tools`

            List of tool names. This is a query parameter used to select responses.

          - `Optional<Double> topP`

            Nucleus sampling parameter. This is a query parameter used to select responses.

          - `Optional<List<String>> users`

            List of user identifiers. This is a query parameter used to select responses.

      - `JsonValue; type "responses"constant`

        The type of run data source. Always `responses`.

        - `RESPONSES("responses")`

      - `Optional<InputMessages> inputMessages`

        Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

        - `class Template:`

          - `List<InnerTemplate> template`

            A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

            - `class ChatMessage:`

              - `String content`

                The content of the message.

              - `String role`

                The role of the message (e.g. "system", "assistant", "user").

            - `class EvalItem:`

              A message input to the model with a role indicating instruction following
              hierarchy. Instructions given with the `developer` or `system` role take
              precedence over instructions given with the `user` role. Messages with the
              `assistant` role are presumed to have been generated by the model in previous
              interactions.

              - `Content content`

                Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                - `String`

                - `class ResponseInputText:`

                  A text input to the model.

                  - `String text`

                    The text input to the model.

                  - `JsonValue; type "input_text"constant`

                    The type of the input item. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `class OutputText:`

                  A text output from the model.

                  - `String text`

                    The text output from the model.

                  - `JsonValue; type "output_text"constant`

                    The type of the output text. Always `output_text`.

                    - `OUTPUT_TEXT("output_text")`

                - `class InputImage:`

                  An image input block used within EvalItem content arrays.

                  - `String imageUrl`

                    The URL of the image input.

                  - `JsonValue; type "input_image"constant`

                    The type of the image input. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

                  - `Optional<String> detail`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `class ResponseInputAudio:`

                  An audio input to the model.

                  - `InputAudio inputAudio`

                    - `String data`

                      Base64-encoded audio data.

                    - `Format format`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `MP3("mp3")`

                      - `WAV("wav")`

                  - `JsonValue; type "input_audio"constant`

                    The type of the input item. Always `input_audio`.

                    - `INPUT_AUDIO("input_audio")`

                - `List<EvalContentItem>`

                  - `String`

                  - `class ResponseInputText:`

                    A text input to the model.

                    - `String text`

                      The text input to the model.

                    - `JsonValue; type "input_text"constant`

                      The type of the input item. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `OutputText`

                    - `String text`

                      The text output from the model.

                    - `JsonValue; type "output_text"constant`

                      The type of the output text. Always `output_text`.

                      - `OUTPUT_TEXT("output_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image input.

                    - `JsonValue; type "input_image"constant`

                      The type of the image input. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                    - `Optional<String> detail`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `class ResponseInputAudio:`

                    An audio input to the model.

                    - `InputAudio inputAudio`

                      - `String data`

                        Base64-encoded audio data.

                      - `Format format`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `MP3("mp3")`

                        - `WAV("wav")`

                    - `JsonValue; type "input_audio"constant`

                      The type of the input item. Always `input_audio`.

                      - `INPUT_AUDIO("input_audio")`

              - `Role role`

                The role of the message input. One of `user`, `assistant`, `system`, or
                `developer`.

                - `USER("user")`

                - `ASSISTANT("assistant")`

                - `SYSTEM("system")`

                - `DEVELOPER("developer")`

              - `Optional<Type> type`

                The type of the message input. Always `message`.

                - `MESSAGE("message")`

          - `JsonValue; type "template"constant`

            The type of input messages. Always `template`.

            - `TEMPLATE("template")`

        - `class ItemReference:`

          - `String itemReference`

            A reference to a variable in the `item` namespace. Ie, "item.name"

          - `JsonValue; type "item_reference"constant`

            The type of input messages. Always `item_reference`.

            - `ITEM_REFERENCE("item_reference")`

      - `Optional<String> model`

        The name of the model to use for generating completions (e.g. "o3-mini").

      - `Optional<SamplingParams> samplingParams`

        - `Optional<Long> maxCompletionTokens`

          The maximum number of tokens in the generated output.

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

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

        - `Optional<Long> seed`

          A seed value to initialize the randomness, during sampling.

        - `Optional<Double> temperature`

          A higher temperature increases randomness in the outputs.

        - `Optional<Text> text`

          Configuration options for a text response from the model. Can be plain
          text or structured JSON data. Learn more:

          - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
          - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          - `Optional<ResponseFormatTextConfig> format`

            An object specifying the format that the model must output.

            Configuring `{ "type": "json_schema" }` enables Structured Outputs,
            which ensures the model will match your supplied JSON schema. Learn more in the
            [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

            The default format is `{ "type": "text" }` with no additional options.

            **Not recommended for gpt-4o and newer models:**

            Setting to `{ "type": "json_object" }` enables the older JSON mode, which
            ensures the message the model generates is valid JSON. Using `json_schema`
            is preferred for models that support it.

            - `class ResponseFormatText:`

              Default response format. Used to generate text responses.

              - `JsonValue; type "text"constant`

                The type of response format being defined. Always `text`.

                - `TEXT("text")`

            - `class ResponseFormatTextJsonSchemaConfig:`

              JSON Schema response format. Used to generate structured JSON responses.
              Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

              - `String name`

                The name of the response format. Must be a-z, A-Z, 0-9, or contain
                underscores and dashes, with a maximum length of 64.

              - `Schema schema`

                The schema for the response format, described as a JSON Schema object.
                Learn how to build JSON schemas [here](https://json-schema.org/).

              - `JsonValue; type "json_schema"constant`

                The type of response format being defined. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

              - `Optional<String> description`

                A description of what the response format is for, used by the model to
                determine how to respond in the format.

              - `Optional<Boolean> strict`

                Whether to enable strict schema adherence when generating the output.
                If set to true, the model will always follow the exact schema defined
                in the `schema` field. Only a subset of JSON Schema is supported when
                `strict` is `true`. To learn more, read the [Structured Outputs
                guide](https://platform.openai.com/docs/guides/structured-outputs).

            - `class ResponseFormatJsonObject:`

              JSON object response format. An older method of generating JSON responses.
              Using `json_schema` is recommended for models that support it. Note that the
              model will not generate JSON without a system or user message instructing it
              to do so.

              - `JsonValue; type "json_object"constant`

                The type of response format being defined. Always `json_object`.

                - `JSON_OBJECT("json_object")`

        - `Optional<List<Tool>> tools`

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

          - `class FunctionTool:`

            Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

            - `String name`

              The name of the function to call.

            - `Optional<Parameters> parameters`

              A JSON schema object describing the parameters of the function.

            - `Optional<Boolean> strict`

              Whether to enforce strict parameter validation. Default `true`.

            - `JsonValue; type "function"constant`

              The type of the function tool. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> deferLoading`

              Whether this function is deferred and loaded via tool search.

            - `Optional<String> description`

              A description of the function. Used by the model to determine whether or not to call the function.

          - `class FileSearchTool:`

            A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

            - `JsonValue; type "file_search"constant`

              The type of the file search tool. Always `file_search`.

              - `FILE_SEARCH("file_search")`

            - `List<String> vectorStoreIds`

              The IDs of the vector stores to search.

            - `Optional<Filters> filters`

              A filter to apply.

              - `class ComparisonFilter:`

                A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                - `String key`

                  The key to compare against the value.

                - `Type type`

                  Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                  - `eq`: equals
                  - `ne`: not equal
                  - `gt`: greater than
                  - `gte`: greater than or equal
                  - `lt`: less than
                  - `lte`: less than or equal
                  - `in`: in
                  - `nin`: not in

                  - `EQ("eq")`

                  - `NE("ne")`

                  - `GT("gt")`

                  - `GTE("gte")`

                  - `LT("lt")`

                  - `LTE("lte")`

                - `Value value`

                  The value to compare against the attribute key; supports string, number, or boolean types.

                  - `String`

                  - `double`

                  - `boolean`

                  - `List<ComparisonFilterValueItem>`

                    - `String`

                    - `double`

              - `class CompoundFilter:`

                Combine multiple filters using `and` or `or`.

                - `List<Filter> filters`

                  Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

                  - `class ComparisonFilter:`

                    A filter used to compare a specified attribute key to a given value using a defined comparison operation.

                    - `String key`

                      The key to compare against the value.

                    - `Type type`

                      Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

                      - `eq`: equals
                      - `ne`: not equal
                      - `gt`: greater than
                      - `gte`: greater than or equal
                      - `lt`: less than
                      - `lte`: less than or equal
                      - `in`: in
                      - `nin`: not in

                      - `EQ("eq")`

                      - `NE("ne")`

                      - `GT("gt")`

                      - `GTE("gte")`

                      - `LT("lt")`

                      - `LTE("lte")`

                    - `Value value`

                      The value to compare against the attribute key; supports string, number, or boolean types.

                      - `String`

                      - `double`

                      - `boolean`

                      - `List<ComparisonFilterValueItem>`

                        - `String`

                        - `double`

                  - `JsonValue`

                - `Type type`

                  Type of operation: `and` or `or`.

                  - `AND("and")`

                  - `OR("or")`

            - `Optional<Long> maxNumResults`

              The maximum number of results to return. This number should be between 1 and 50 inclusive.

            - `Optional<RankingOptions> rankingOptions`

              Ranking options for search.

              - `Optional<HybridSearch> hybridSearch`

                Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

                - `double embeddingWeight`

                  The weight of the embedding in the reciprocal ranking fusion.

                - `double textWeight`

                  The weight of the text in the reciprocal ranking fusion.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search.

                - `AUTO("auto")`

                - `DEFAULT_2024_11_15("default-2024-11-15")`

              - `Optional<Double> scoreThreshold`

                The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

          - `class ComputerTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `JsonValue; type "computer"constant`

              The type of the computer tool. Always `computer`.

              - `COMPUTER("computer")`

          - `class ComputerUsePreviewTool:`

            A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

            - `long displayHeight`

              The height of the computer display.

            - `long displayWidth`

              The width of the computer display.

            - `Environment environment`

              The type of computer environment to control.

              - `WINDOWS("windows")`

              - `MAC("mac")`

              - `LINUX("linux")`

              - `UBUNTU("ubuntu")`

              - `BROWSER("browser")`

            - `JsonValue; type "computer_use_preview"constant`

              The type of the computer use tool. Always `computer_use_preview`.

              - `COMPUTER_USE_PREVIEW("computer_use_preview")`

          - `class WebSearchTool:`

            Search the Internet for sources related to the prompt. Learn more about the
            [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

              - `WEB_SEARCH("web_search")`

              - `WEB_SEARCH_2025_08_26("web_search_2025_08_26")`

            - `Optional<Filters> filters`

              Filters for the search.

              - `Optional<List<String>> allowedDomains`

                Allowed domains for the search. If not provided, all domains are allowed.
                Subdomains of the provided domains are allowed as well.

                Example: `["pubmed.ncbi.nlm.nih.gov"]`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The approximate location of the user.

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

              - `Optional<Type> type`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

          - `Mcp`

            - `String serverLabel`

              A label for this MCP server, used to identify it in tool calls.

            - `JsonValue; type "mcp"constant`

              The type of the MCP tool. Always `mcp`.

              - `MCP("mcp")`

            - `Optional<AllowedTools> allowedTools`

              List of allowed tool names or a filter object.

              - `List<String>`

              - `class McpToolFilter:`

                A filter object to specify which tools are allowed.

                - `Optional<Boolean> readOnly`

                  Indicates whether or not a tool modifies data or is read-only. If an
                  MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                  it will match this filter.

                - `Optional<List<String>> toolNames`

                  List of allowed tool names.

            - `Optional<String> authorization`

              An OAuth access token that can be used with a remote MCP server, either
              with a custom MCP server URL or a service connector. Your application
              must handle the OAuth authorization flow and provide the token here.

            - `Optional<ConnectorId> connectorId`

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

              - `CONNECTOR_DROPBOX("connector_dropbox")`

              - `CONNECTOR_GMAIL("connector_gmail")`

              - `CONNECTOR_GOOGLECALENDAR("connector_googlecalendar")`

              - `CONNECTOR_GOOGLEDRIVE("connector_googledrive")`

              - `CONNECTOR_MICROSOFTTEAMS("connector_microsoftteams")`

              - `CONNECTOR_OUTLOOKCALENDAR("connector_outlookcalendar")`

              - `CONNECTOR_OUTLOOKEMAIL("connector_outlookemail")`

              - `CONNECTOR_SHAREPOINT("connector_sharepoint")`

            - `Optional<Boolean> deferLoading`

              Whether this MCP tool is deferred and discovered via tool search.

            - `Optional<Headers> headers`

              Optional HTTP headers to send to the MCP server. Use for authentication
              or other purposes.

            - `Optional<RequireApproval> requireApproval`

              Specify which of the MCP server's tools require approval.

              - `class McpToolApprovalFilter:`

                Specify which of the MCP server's tools require approval. Can be
                `always`, `never`, or a filter object associated with tools
                that require approval.

                - `Optional<Always> always`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

                - `Optional<Never> never`

                  A filter object to specify which tools are allowed.

                  - `Optional<Boolean> readOnly`

                    Indicates whether or not a tool modifies data or is read-only. If an
                    MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
                    it will match this filter.

                  - `Optional<List<String>> toolNames`

                    List of allowed tool names.

              - `enum McpToolApprovalSetting:`

                Specify a single approval policy for all tools. One of `always` or
                `never`. When set to `always`, all tools will require approval. When
                set to `never`, all tools will not require approval.

                - `ALWAYS("always")`

                - `NEVER("never")`

            - `Optional<String> serverDescription`

              Optional description of the MCP server, used to provide more context.

            - `Optional<String> serverUrl`

              The URL for the MCP server. One of `server_url` or `connector_id` must be
              provided.

          - `CodeInterpreter`

            - `Container container`

              The code interpreter container. Can be a container ID or an object that
              specifies uploaded file IDs to make available to your code, along with an
              optional `memory_limit` setting.

              - `String`

              - `class CodeInterpreterToolAuto:`

                Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

                - `JsonValue; type "auto"constant`

                  Always `auto`.

                  - `AUTO("auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the code interpreter container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

            - `JsonValue; type "code_interpreter"constant`

              The type of the code interpreter tool. Always `code_interpreter`.

              - `CODE_INTERPRETER("code_interpreter")`

          - `ImageGeneration`

            - `JsonValue; type "image_generation"constant`

              The type of the image generation tool. Always `image_generation`.

              - `IMAGE_GENERATION("image_generation")`

            - `Optional<Action> action`

              Whether to generate a new image or edit an existing image. Default: `auto`.

              - `GENERATE("generate")`

              - `EDIT("edit")`

              - `AUTO("auto")`

            - `Optional<Background> background`

              Background type for the generated image. One of `transparent`,
              `opaque`, or `auto`. Default: `auto`.

              - `TRANSPARENT("transparent")`

              - `OPAQUE("opaque")`

              - `AUTO("auto")`

            - `Optional<InputFidelity> inputFidelity`

              Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

              - `HIGH("high")`

              - `LOW("low")`

            - `Optional<InputImageMask> inputImageMask`

              Optional mask for inpainting. Contains `image_url`
              (string, optional) and `file_id` (string, optional).

              - `Optional<String> fileId`

                File ID for the mask image.

              - `Optional<String> imageUrl`

                Base64-encoded mask image.

            - `Optional<Model> model`

              The image generation model to use. Default: `gpt-image-1`.

              - `GPT_IMAGE_1("gpt-image-1")`

              - `GPT_IMAGE_1_MINI("gpt-image-1-mini")`

              - `GPT_IMAGE_1_5("gpt-image-1.5")`

            - `Optional<Moderation> moderation`

              Moderation level for the generated image. Default: `auto`.

              - `AUTO("auto")`

              - `LOW("low")`

            - `Optional<Long> outputCompression`

              Compression level for the output image. Default: 100.

            - `Optional<OutputFormat> outputFormat`

              The output format of the generated image. One of `png`, `webp`, or
              `jpeg`. Default: `png`.

              - `PNG("png")`

              - `WEBP("webp")`

              - `JPEG("jpeg")`

            - `Optional<Long> partialImages`

              Number of partial images to generate in streaming mode, from 0 (default value) to 3.

            - `Optional<Quality> quality`

              The quality of the generated image. One of `low`, `medium`, `high`,
              or `auto`. Default: `auto`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `AUTO("auto")`

            - `Optional<Size> size`

              The size of the generated image. One of `1024x1024`, `1024x1536`,
              `1536x1024`, or `auto`. Default: `auto`.

              - `_1024X1024("1024x1024")`

              - `_1024X1536("1024x1536")`

              - `_1536X1024("1536x1024")`

              - `AUTO("auto")`

          - `JsonValue;`

            - `JsonValue; type "local_shell"constant`

              The type of the local shell tool. Always `local_shell`.

              - `LOCAL_SHELL("local_shell")`

          - `class FunctionShellTool:`

            A tool that allows the model to execute shell commands.

            - `JsonValue; type "shell"constant`

              The type of the shell tool. Always `shell`.

              - `SHELL("shell")`

            - `Optional<Environment> environment`

              - `class ContainerAuto:`

                - `JsonValue; type "container_auto"constant`

                  Automatically creates a container for this request

                  - `CONTAINER_AUTO("container_auto")`

                - `Optional<List<String>> fileIds`

                  An optional list of uploaded files to make available to your code.

                - `Optional<MemoryLimit> memoryLimit`

                  The memory limit for the container.

                  - `_1G("1g")`

                  - `_4G("4g")`

                  - `_16G("16g")`

                  - `_64G("64g")`

                - `Optional<NetworkPolicy> networkPolicy`

                  Network access policy for the container.

                  - `class ContainerNetworkPolicyDisabled:`

                    - `JsonValue; type "disabled"constant`

                      Disable outbound network access. Always `disabled`.

                      - `DISABLED("disabled")`

                  - `class ContainerNetworkPolicyAllowlist:`

                    - `List<String> allowedDomains`

                      A list of allowed domains when type is `allowlist`.

                    - `JsonValue; type "allowlist"constant`

                      Allow outbound network access only to specified domains. Always `allowlist`.

                      - `ALLOWLIST("allowlist")`

                    - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

                      Optional domain-scoped secrets for allowlisted domains.

                      - `String domain`

                        The domain associated with the secret.

                      - `String name`

                        The name of the secret to inject for the domain.

                      - `String value`

                        The secret value to inject for the domain.

                - `Optional<List<Skill>> skills`

                  An optional list of skills referenced by id or inline data.

                  - `class SkillReference:`

                    - `String skillId`

                      The ID of the referenced skill.

                    - `JsonValue; type "skill_reference"constant`

                      References a skill created with the /v1/skills endpoint.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      Optional skill version. Use a positive integer or 'latest'. Omit for default.

                  - `class InlineSkill:`

                    - `String description`

                      The description of the skill.

                    - `String name`

                      The name of the skill.

                    - `InlineSkillSource source`

                      Inline skill payload

                      - `String data`

                        Base64-encoded skill zip bundle.

                      - `JsonValue; mediaType "application/zip"constant`

                        The media type of the inline skill payload. Must be `application/zip`.

                        - `APPLICATION_ZIP("application/zip")`

                      - `JsonValue; type "base64"constant`

                        The type of the inline skill source. Must be `base64`.

                        - `BASE64("base64")`

                    - `JsonValue; type "inline"constant`

                      Defines an inline skill for this request.

                      - `INLINE("inline")`

              - `class LocalEnvironment:`

                - `JsonValue; type "local"constant`

                  Use a local computer environment.

                  - `LOCAL("local")`

                - `Optional<List<LocalSkill>> skills`

                  An optional list of skills.

                  - `String description`

                    The description of the skill.

                  - `String name`

                    The name of the skill.

                  - `String path`

                    The path to the directory containing the skill.

              - `class ContainerReference:`

                - `String containerId`

                  The ID of the referenced container.

                - `JsonValue; type "container_reference"constant`

                  References a container created with the /v1/containers endpoint

                  - `CONTAINER_REFERENCE("container_reference")`

          - `class CustomTool:`

            A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

            - `String name`

              The name of the custom tool, used to identify it in tool calls.

            - `JsonValue; type "custom"constant`

              The type of the custom tool. Always `custom`.

              - `CUSTOM("custom")`

            - `Optional<Boolean> deferLoading`

              Whether this tool should be deferred and discovered via tool search.

            - `Optional<String> description`

              Optional description of the custom tool, used to provide more context.

            - `Optional<CustomToolInputFormat> format`

              The input format for the custom tool. Default is unconstrained text.

              - `JsonValue;`

                - `JsonValue; type "text"constant`

                  Unconstrained text format. Always `text`.

                  - `TEXT("text")`

              - `Grammar`

                - `String definition`

                  The grammar definition.

                - `Syntax syntax`

                  The syntax of the grammar definition. One of `lark` or `regex`.

                  - `LARK("lark")`

                  - `REGEX("regex")`

                - `JsonValue; type "grammar"constant`

                  Grammar format. Always `grammar`.

                  - `GRAMMAR("grammar")`

          - `class NamespaceTool:`

            Groups function/custom tools under a shared namespace.

            - `String description`

              A description of the namespace shown to the model.

            - `String name`

              The namespace name used in tool calls (for example, `crm`).

            - `List<Tool> tools`

              The function/custom tools available inside this namespace.

              - `class Function:`

                - `String name`

                - `JsonValue; type "function"constant`

                  - `FUNCTION("function")`

                - `Optional<Boolean> deferLoading`

                  Whether this function should be deferred and discovered via tool search.

                - `Optional<String> description`

                - `Optional<JsonValue> parameters`

                - `Optional<Boolean> strict`

              - `class CustomTool:`

                A custom tool that processes input using a specified format. Learn more about   [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

                - `String name`

                  The name of the custom tool, used to identify it in tool calls.

                - `JsonValue; type "custom"constant`

                  The type of the custom tool. Always `custom`.

                  - `CUSTOM("custom")`

                - `Optional<Boolean> deferLoading`

                  Whether this tool should be deferred and discovered via tool search.

                - `Optional<String> description`

                  Optional description of the custom tool, used to provide more context.

                - `Optional<CustomToolInputFormat> format`

                  The input format for the custom tool. Default is unconstrained text.

                  - `JsonValue;`

                    - `JsonValue; type "text"constant`

                      Unconstrained text format. Always `text`.

                      - `TEXT("text")`

                  - `Grammar`

                    - `String definition`

                      The grammar definition.

                    - `Syntax syntax`

                      The syntax of the grammar definition. One of `lark` or `regex`.

                      - `LARK("lark")`

                      - `REGEX("regex")`

                    - `JsonValue; type "grammar"constant`

                      Grammar format. Always `grammar`.

                      - `GRAMMAR("grammar")`

            - `JsonValue; type "namespace"constant`

              The type of the tool. Always `namespace`.

              - `NAMESPACE("namespace")`

          - `class ToolSearchTool:`

            Hosted or BYOT tool search configuration for deferred tools.

            - `JsonValue; type "tool_search"constant`

              The type of the tool. Always `tool_search`.

              - `TOOL_SEARCH("tool_search")`

            - `Optional<String> description`

              Description shown to the model for a client-executed tool search tool.

            - `Optional<Execution> execution`

              Whether tool search is executed by the server or by the client.

              - `SERVER("server")`

              - `CLIENT("client")`

            - `Optional<JsonValue> parameters`

              Parameter schema for a client-executed tool search tool.

          - `class WebSearchPreviewTool:`

            This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

            - `Type type`

              The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

              - `WEB_SEARCH_PREVIEW("web_search_preview")`

              - `WEB_SEARCH_PREVIEW_2025_03_11("web_search_preview_2025_03_11")`

            - `Optional<List<SearchContentType>> searchContentTypes`

              - `TEXT("text")`

              - `IMAGE("image")`

            - `Optional<SearchContextSize> searchContextSize`

              High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<UserLocation> userLocation`

              The user's location.

              - `JsonValue; type "approximate"constant`

                The type of location approximation. Always `approximate`.

                - `APPROXIMATE("approximate")`

              - `Optional<String> city`

                Free text input for the city of the user, e.g. `San Francisco`.

              - `Optional<String> country`

                The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

              - `Optional<String> region`

                Free text input for the region of the user, e.g. `California`.

              - `Optional<String> timezone`

                The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

          - `class ApplyPatchTool:`

            Allows the assistant to create, delete, or update files using unified diffs.

            - `JsonValue; type "apply_patch"constant`

              The type of the tool. Always `apply_patch`.

              - `APPLY_PATCH("apply_patch")`

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `EvalApiError error`

    An object representing an error response from the Eval API.

    - `String code`

      The error code.

    - `String message`

      The error message.

  - `String evalId`

    The identifier of the associated evaluation.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that is evaluated, if applicable.

  - `String name`

    The name of the evaluation run.

  - `JsonValue; object_ "eval.run"constant`

    The type of the object. Always "eval.run".

    - `EVAL_RUN("eval.run")`

  - `List<PerModelUsage> perModelUsage`

    Usage statistics for each model during the evaluation run.

    - `long cachedTokens`

      The number of tokens retrieved from cache.

    - `long completionTokens`

      The number of completion tokens generated.

    - `long invocationCount`

      The number of invocations.

    - `String modelName`

      The name of the model.

    - `long promptTokens`

      The number of prompt tokens used.

    - `long totalTokens`

      The total number of tokens used.

  - `List<PerTestingCriteriaResult> perTestingCriteriaResults`

    Results per testing criteria applied during the evaluation run.

    - `long failed`

      Number of tests failed for this criteria.

    - `long passed`

      Number of tests passed for this criteria.

    - `String testingCriteria`

      A description of the testing criteria.

  - `String reportUrl`

    The URL to the rendered evaluation run report on the UI dashboard.

  - `ResultCounts resultCounts`

    Counters summarizing the outcomes of the evaluation run.

    - `long errored`

      Number of output items that resulted in an error.

    - `long failed`

      Number of output items that failed to pass the evaluation.

    - `long passed`

      Number of output items that passed the evaluation.

    - `long total`

      Total number of executed output items.

  - `String status`

    The status of the evaluation run.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.runs.RunCancelParams;
import com.openai.models.evals.runs.RunCancelResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunCancelParams params = RunCancelParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .build();
        RunCancelResponse response = client.evals().runs().cancel(params);
    }
}
```

### Delete

`RunDeleteResponse evals().runs().delete(RunDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/evals/{eval_id}/runs/{run_id}`

Delete an eval run.

#### Parameters

- `RunDeleteParams params`

  - `String evalId`

  - `Optional<String> runId`

#### Returns

- `class RunDeleteResponse:`

  - `Optional<Boolean> deleted`

  - `Optional<String> object_`

  - `Optional<String> runId`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.runs.RunDeleteParams;
import com.openai.models.evals.runs.RunDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunDeleteParams params = RunDeleteParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .build();
        RunDeleteResponse run = client.evals().runs().delete(params);
    }
}
```

#### Domain Types

#### Create Eval Completions Run Data Source

- `class CreateEvalCompletionsRunDataSource:`

  A CompletionsRunDataSource object describing a model sampling configuration.

  - `Source source`

    Determines what populates the `item` namespace in this run's data source.

    - `class FileContent:`

      - `List<Content> content`

        The content of the jsonl file.

        - `Item item`

        - `Optional<Sample> sample`

      - `JsonValue; type "file_content"constant`

        The type of jsonl source. Always `file_content`.

        - `FILE_CONTENT("file_content")`

    - `class FileId:`

      - `String id`

        The identifier of the file.

      - `JsonValue; type "file_id"constant`

        The type of jsonl source. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class StoredCompletions:`

      A StoredCompletionsRunDataSource configuration describing a set of filters

      - `JsonValue; type "stored_completions"constant`

        The type of source. Always `stored_completions`.

        - `STORED_COMPLETIONS("stored_completions")`

      - `Optional<Long> createdAfter`

        An optional Unix timestamp to filter items created after this time.

      - `Optional<Long> createdBefore`

        An optional Unix timestamp to filter items created before this time.

      - `Optional<Long> limit`

        An optional maximum number of items to return.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `Optional<String> model`

        An optional model to filter by (e.g., 'gpt-4o').

  - `Type type`

    The type of run data source. Always `completions`.

    - `COMPLETIONS("completions")`

  - `Optional<InputMessages> inputMessages`

    Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

    - `class Template:`

      - `List<InnerTemplate> template`

        A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

        - `class EasyInputMessage:`

          A message input to the model with a role indicating instruction following
          hierarchy. Instructions given with the `developer` or `system` role take
          precedence over instructions given with the `user` role. Messages with the
          `assistant` role are presumed to have been generated by the model in previous
          interactions.

          - `Content content`

            Text, image, or audio input to the model, used to generate a response.
            Can also contain previous assistant responses.

            - `String`

            - `List<ResponseInputContent>`

              - `class ResponseInputText:`

                A text input to the model.

                - `String text`

                  The text input to the model.

                - `JsonValue; type "input_text"constant`

                  The type of the input item. Always `input_text`.

                  - `INPUT_TEXT("input_text")`

              - `class ResponseInputImage:`

                An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

                - `Detail detail`

                  The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

                  - `LOW("low")`

                  - `HIGH("high")`

                  - `AUTO("auto")`

                  - `ORIGINAL("original")`

                - `JsonValue; type "input_image"constant`

                  The type of the input item. Always `input_image`.

                  - `INPUT_IMAGE("input_image")`

                - `Optional<String> fileId`

                  The ID of the file to be sent to the model.

                - `Optional<String> imageUrl`

                  The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

              - `class ResponseInputFile:`

                A file input to the model.

                - `JsonValue; type "input_file"constant`

                  The type of the input item. Always `input_file`.

                  - `INPUT_FILE("input_file")`

                - `Optional<String> fileData`

                  The content of the file to be sent to the model.

                - `Optional<String> fileId`

                  The ID of the file to be sent to the model.

                - `Optional<String> fileUrl`

                  The URL of the file to be sent to the model.

                - `Optional<String> filename`

                  The name of the file to be sent to the model.

          - `Role role`

            The role of the message input. One of `user`, `assistant`, `system`, or
            `developer`.

            - `USER("user")`

            - `ASSISTANT("assistant")`

            - `SYSTEM("system")`

            - `DEVELOPER("developer")`

          - `Optional<Phase> phase`

            Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
            For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
            phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

            - `COMMENTARY("commentary")`

            - `FINAL_ANSWER("final_answer")`

          - `Optional<Type> type`

            The type of the message input. Always `message`.

            - `MESSAGE("message")`

        - `class EvalItem:`

          A message input to the model with a role indicating instruction following
          hierarchy. Instructions given with the `developer` or `system` role take
          precedence over instructions given with the `user` role. Messages with the
          `assistant` role are presumed to have been generated by the model in previous
          interactions.

          - `Content content`

            Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

            - `String`

            - `class ResponseInputText:`

              A text input to the model.

              - `String text`

                The text input to the model.

              - `JsonValue; type "input_text"constant`

                The type of the input item. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `class OutputText:`

              A text output from the model.

              - `String text`

                The text output from the model.

              - `JsonValue; type "output_text"constant`

                The type of the output text. Always `output_text`.

                - `OUTPUT_TEXT("output_text")`

            - `class InputImage:`

              An image input block used within EvalItem content arrays.

              - `String imageUrl`

                The URL of the image input.

              - `JsonValue; type "input_image"constant`

                The type of the image input. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

              - `Optional<String> detail`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `class ResponseInputAudio:`

              An audio input to the model.

              - `InputAudio inputAudio`

                - `String data`

                  Base64-encoded audio data.

                - `Format format`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `MP3("mp3")`

                  - `WAV("wav")`

              - `JsonValue; type "input_audio"constant`

                The type of the input item. Always `input_audio`.

                - `INPUT_AUDIO("input_audio")`

            - `List<EvalContentItem>`

              - `String`

              - `class ResponseInputText:`

                A text input to the model.

                - `String text`

                  The text input to the model.

                - `JsonValue; type "input_text"constant`

                  The type of the input item. Always `input_text`.

                  - `INPUT_TEXT("input_text")`

              - `OutputText`

                - `String text`

                  The text output from the model.

                - `JsonValue; type "output_text"constant`

                  The type of the output text. Always `output_text`.

                  - `OUTPUT_TEXT("output_text")`

              - `InputImage`

                - `String imageUrl`

                  The URL of the image input.

                - `JsonValue; type "input_image"constant`

                  The type of the image input. Always `input_image`.

                  - `INPUT_IMAGE("input_image")`

                - `Optional<String> detail`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `class ResponseInputAudio:`

                An audio input to the model.

                - `InputAudio inputAudio`

                  - `String data`

                    Base64-encoded audio data.

                  - `Format format`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `MP3("mp3")`

                    - `WAV("wav")`

                - `JsonValue; type "input_audio"constant`

                  The type of the input item. Always `input_audio`.

                  - `INPUT_AUDIO("input_audio")`

          - `Role role`

            The role of the message input. One of `user`, `assistant`, `system`, or
            `developer`.

            - `USER("user")`

            - `ASSISTANT("assistant")`

            - `SYSTEM("system")`

            - `DEVELOPER("developer")`

          - `Optional<Type> type`

            The type of the message input. Always `message`.

            - `MESSAGE("message")`

      - `JsonValue; type "template"constant`

        The type of input messages. Always `template`.

        - `TEMPLATE("template")`

    - `class ItemReference:`

      - `String itemReference`

        A reference to a variable in the `item` namespace. Ie, "item.input_trajectory"

      - `JsonValue; type "item_reference"constant`

        The type of input messages. Always `item_reference`.

        - `ITEM_REFERENCE("item_reference")`

  - `Optional<String> model`

    The name of the model to use for generating completions (e.g. "o3-mini").

  - `Optional<SamplingParams> samplingParams`

    - `Optional<Long> maxCompletionTokens`

      The maximum number of tokens in the generated output.

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

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

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

    - `Optional<Long> seed`

      A seed value to initialize the randomness, during sampling.

    - `Optional<Double> temperature`

      A higher temperature increases randomness in the outputs.

    - `Optional<List<ChatCompletionFunctionTool>> tools`

      A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

    - `Optional<Double> topP`

      An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

#### Create Eval JSONL Run Data Source

- `class CreateEvalJsonlRunDataSource:`

  A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

  - `Source source`

    Determines what populates the `item` namespace in the data source.

    - `class FileContent:`

      - `List<Content> content`

        The content of the jsonl file.

        - `Item item`

        - `Optional<Sample> sample`

      - `JsonValue; type "file_content"constant`

        The type of jsonl source. Always `file_content`.

        - `FILE_CONTENT("file_content")`

    - `class FileId:`

      - `String id`

        The identifier of the file.

      - `JsonValue; type "file_id"constant`

        The type of jsonl source. Always `file_id`.

        - `FILE_ID("file_id")`

  - `JsonValue; type "jsonl"constant`

    The type of data source. Always `jsonl`.

    - `JSONL("jsonl")`

#### Eval API Error

- `class EvalApiError:`

  An object representing an error response from the Eval API.

  - `String code`

    The error code.

  - `String message`

    The error message.

### Output Items

#### List

`OutputItemListPage evals().runs().outputItems().list(OutputItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/evals/{eval_id}/runs/{run_id}/output_items`

Get a list of output items for an evaluation run.

##### Parameters

- `OutputItemListParams params`

  - `String evalId`

  - `Optional<String> runId`

  - `Optional<String> after`

    Identifier for the last output item from the previous pagination request.

  - `Optional<Long> limit`

    Number of output items to retrieve.

  - `Optional<Order> order`

    Sort order for output items by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<Status> status`

    Filter output items by status. Use `failed` to filter by failed output
    items or `pass` to filter by passed output items.

    - `FAIL("fail")`

    - `PASS("pass")`

##### Returns

- `class OutputItemListResponse:`

  A schema representing an evaluation run output item.

  - `String id`

    Unique identifier for the evaluation run output item.

  - `long createdAt`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `DatasourceItem datasourceItem`

    Details of the input data source item.

  - `long datasourceItemId`

    The identifier for the data source item.

  - `String evalId`

    The identifier of the evaluation group.

  - `JsonValue; object_ "eval.run.output_item"constant`

    The type of the object. Always "eval.run.output_item".

    - `EVAL_RUN_OUTPUT_ITEM("eval.run.output_item")`

  - `List<Result> results`

    A list of grader results for this output item.

    - `String name`

      The name of the grader.

    - `boolean passed`

      Whether the grader considered the output a pass.

    - `double score`

      The numeric score produced by the grader.

    - `Optional<Sample> sample`

      Optional sample or intermediate data produced by the grader.

    - `Optional<String> type`

      The grader type (for example, "string-check-grader").

  - `String runId`

    The identifier of the evaluation run associated with this output item.

  - `Sample sample`

    A sample containing the input and output of the evaluation run.

    - `EvalApiError error`

      An object representing an error response from the Eval API.

      - `String code`

        The error code.

      - `String message`

        The error message.

    - `String finishReason`

      The reason why the sample generation was finished.

    - `List<Input> input`

      An array of input messages.

      - `String content`

        The content of the message.

      - `String role`

        The role of the message sender (e.g., system, user, developer).

    - `long maxCompletionTokens`

      The maximum number of tokens allowed for completion.

    - `String model`

      The model used for generating the sample.

    - `List<Output> output`

      An array of output messages.

      - `Optional<String> content`

        The content of the message.

      - `Optional<String> role`

        The role of the message (e.g. "system", "assistant", "user").

    - `long seed`

      The seed used for generating the sample.

    - `double temperature`

      The sampling temperature used.

    - `double topP`

      The top_p value used for sampling.

    - `Usage usage`

      Token usage details for the sample.

      - `long cachedTokens`

        The number of tokens retrieved from cache.

      - `long completionTokens`

        The number of completion tokens generated.

      - `long promptTokens`

        The number of prompt tokens used.

      - `long totalTokens`

        The total number of tokens used.

  - `String status`

    The status of the evaluation run.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.runs.outputitems.OutputItemListPage;
import com.openai.models.evals.runs.outputitems.OutputItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        OutputItemListParams params = OutputItemListParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .build();
        OutputItemListPage page = client.evals().runs().outputItems().list(params);
    }
}
```

#### Retrieve

`OutputItemRetrieveResponse evals().runs().outputItems().retrieve(OutputItemRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}`

Get an evaluation run output item by ID.

##### Parameters

- `OutputItemRetrieveParams params`

  - `String evalId`

  - `String runId`

  - `Optional<String> outputItemId`

##### Returns

- `class OutputItemRetrieveResponse:`

  A schema representing an evaluation run output item.

  - `String id`

    Unique identifier for the evaluation run output item.

  - `long createdAt`

    Unix timestamp (in seconds) when the evaluation run was created.

  - `DatasourceItem datasourceItem`

    Details of the input data source item.

  - `long datasourceItemId`

    The identifier for the data source item.

  - `String evalId`

    The identifier of the evaluation group.

  - `JsonValue; object_ "eval.run.output_item"constant`

    The type of the object. Always "eval.run.output_item".

    - `EVAL_RUN_OUTPUT_ITEM("eval.run.output_item")`

  - `List<Result> results`

    A list of grader results for this output item.

    - `String name`

      The name of the grader.

    - `boolean passed`

      Whether the grader considered the output a pass.

    - `double score`

      The numeric score produced by the grader.

    - `Optional<Sample> sample`

      Optional sample or intermediate data produced by the grader.

    - `Optional<String> type`

      The grader type (for example, "string-check-grader").

  - `String runId`

    The identifier of the evaluation run associated with this output item.

  - `Sample sample`

    A sample containing the input and output of the evaluation run.

    - `EvalApiError error`

      An object representing an error response from the Eval API.

      - `String code`

        The error code.

      - `String message`

        The error message.

    - `String finishReason`

      The reason why the sample generation was finished.

    - `List<Input> input`

      An array of input messages.

      - `String content`

        The content of the message.

      - `String role`

        The role of the message sender (e.g., system, user, developer).

    - `long maxCompletionTokens`

      The maximum number of tokens allowed for completion.

    - `String model`

      The model used for generating the sample.

    - `List<Output> output`

      An array of output messages.

      - `Optional<String> content`

        The content of the message.

      - `Optional<String> role`

        The role of the message (e.g. "system", "assistant", "user").

    - `long seed`

      The seed used for generating the sample.

    - `double temperature`

      The sampling temperature used.

    - `double topP`

      The top_p value used for sampling.

    - `Usage usage`

      Token usage details for the sample.

      - `long cachedTokens`

        The number of tokens retrieved from cache.

      - `long completionTokens`

        The number of completion tokens generated.

      - `long promptTokens`

        The number of prompt tokens used.

      - `long totalTokens`

        The total number of tokens used.

  - `String status`

    The status of the evaluation run.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.evals.runs.outputitems.OutputItemRetrieveParams;
import com.openai.models.evals.runs.outputitems.OutputItemRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        OutputItemRetrieveParams params = OutputItemRetrieveParams.builder()
            .evalId("eval_id")
            .runId("run_id")
            .outputItemId("output_item_id")
            .build();
        OutputItemRetrieveResponse outputItem = client.evals().runs().outputItems().retrieve(params);
    }
}
```
