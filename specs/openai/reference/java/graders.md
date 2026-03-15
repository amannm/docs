# Graders

## Grader Models

### Domain Types

### Eval Content Item

- `class EvalContentItem: A class that can be one of several variants.union`

  A single content item: input text, output text, input image, or input audio.

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

### Label Model Grader

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

### Multi Grader

- `class MultiGrader:`

  A MultiGrader object combines the output of multiple graders to produce a single score.

  - `String calculateOutput`

    A formula to calculate the output based on grader results.

  - `Graders graders`

    A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

    - `class TextSimilarityGrader:`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `EvaluationMetric evaluationMetric`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `COSINE("cosine")`

        - `FUZZY_MATCH("fuzzy_match")`

        - `BLEU("bleu")`

        - `GLEU("gleu")`

        - `METEOR("meteor")`

        - `ROUGE_1("rouge_1")`

        - `ROUGE_2("rouge_2")`

        - `ROUGE_3("rouge_3")`

        - `ROUGE_4("rouge_4")`

        - `ROUGE_5("rouge_5")`

        - `ROUGE_L("rouge_l")`

      - `String input`

        The text being graded.

      - `String name`

        The name of the grader.

      - `String reference`

        The text being graded against.

      - `JsonValue; type "text_similarity"constant`

        The type of grader.

        - `TEXT_SIMILARITY("text_similarity")`

    - `class PythonGrader:`

      A PythonGrader object that runs a python script on the input.

      - `String name`

        The name of the grader.

      - `String source`

        The source code of the python script.

      - `JsonValue; type "python"constant`

        The object type, which is always `python`.

        - `PYTHON("python")`

      - `Optional<String> imageTag`

        The image tag to use for the python script.

    - `class ScoreModelGrader:`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `List<Input> input`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

      - `String model`

        The model to use for the evaluation.

      - `String name`

        The name of the grader.

      - `JsonValue; type "score_model"constant`

        The object type, which is always `score_model`.

        - `SCORE_MODEL("score_model")`

      - `Optional<List<Double>> range`

        The range of the score. Defaults to `[0, 1]`.

      - `Optional<SamplingParams> samplingParams`

        The sampling parameters for the model.

        - `Optional<Long> maxCompletionsTokens`

          The maximum number of tokens the grader model may generate in its response.

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

        - `Optional<Double> topP`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

  - `String name`

    The name of the grader.

  - `JsonValue; type "multi"constant`

    The object type, which is always `multi`.

    - `MULTI("multi")`

### Python Grader

- `class PythonGrader:`

  A PythonGrader object that runs a python script on the input.

  - `String name`

    The name of the grader.

  - `String source`

    The source code of the python script.

  - `JsonValue; type "python"constant`

    The object type, which is always `python`.

    - `PYTHON("python")`

  - `Optional<String> imageTag`

    The image tag to use for the python script.

### Score Model Grader

- `class ScoreModelGrader:`

  A ScoreModelGrader object that uses a model to assign a score to the input.

  - `List<Input> input`

    The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

  - `String model`

    The model to use for the evaluation.

  - `String name`

    The name of the grader.

  - `JsonValue; type "score_model"constant`

    The object type, which is always `score_model`.

    - `SCORE_MODEL("score_model")`

  - `Optional<List<Double>> range`

    The range of the score. Defaults to `[0, 1]`.

  - `Optional<SamplingParams> samplingParams`

    The sampling parameters for the model.

    - `Optional<Long> maxCompletionsTokens`

      The maximum number of tokens the grader model may generate in its response.

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

    - `Optional<Double> topP`

      An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

### String Check Grader

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

### Text Similarity Grader

- `class TextSimilarityGrader:`

  A TextSimilarityGrader object which grades text based on similarity metrics.

  - `EvaluationMetric evaluationMetric`

    The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
    `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
    or `rouge_l`.

    - `COSINE("cosine")`

    - `FUZZY_MATCH("fuzzy_match")`

    - `BLEU("bleu")`

    - `GLEU("gleu")`

    - `METEOR("meteor")`

    - `ROUGE_1("rouge_1")`

    - `ROUGE_2("rouge_2")`

    - `ROUGE_3("rouge_3")`

    - `ROUGE_4("rouge_4")`

    - `ROUGE_5("rouge_5")`

    - `ROUGE_L("rouge_l")`

  - `String input`

    The text being graded.

  - `String name`

    The name of the grader.

  - `String reference`

    The text being graded against.

  - `JsonValue; type "text_similarity"constant`

    The type of grader.

    - `TEXT_SIMILARITY("text_similarity")`
