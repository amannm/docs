# Fine Tuning

## Methods

### Domain Types

### Dpo Hyperparameters

- `class DpoHyperparameters:`

  The hyperparameters used for the DPO fine-tuning job.

  - `Optional<BatchSize> batchSize`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

  - `Optional<Beta> beta`

    The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

    - `JsonValue;`

      - `AUTO("auto")`

    - `double`

  - `Optional<LearningRateMultiplier> learningRateMultiplier`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `JsonValue;`

      - `AUTO("auto")`

    - `double`

  - `Optional<NEpochs> nEpochs`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

### Dpo Method

- `class DpoMethod:`

  Configuration for the DPO fine-tuning method.

  - `Optional<DpoHyperparameters> hyperparameters`

    The hyperparameters used for the DPO fine-tuning job.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<Beta> beta`

      The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

### Reinforcement Hyperparameters

- `class ReinforcementHyperparameters:`

  The hyperparameters used for the reinforcement fine-tuning job.

  - `Optional<BatchSize> batchSize`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

  - `Optional<ComputeMultiplier> computeMultiplier`

    Multiplier on amount of compute used for exploring search space during training.

    - `JsonValue;`

      - `AUTO("auto")`

    - `double`

  - `Optional<EvalInterval> evalInterval`

    The number of training steps between evaluation runs.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

  - `Optional<EvalSamples> evalSamples`

    Number of evaluation samples to generate per training step.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

  - `Optional<LearningRateMultiplier> learningRateMultiplier`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `JsonValue;`

      - `AUTO("auto")`

    - `double`

  - `Optional<NEpochs> nEpochs`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

  - `Optional<ReasoningEffort> reasoningEffort`

    Level of reasoning effort.

    - `DEFAULT("default")`

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

### Reinforcement Method

- `class ReinforcementMethod:`

  Configuration for the reinforcement fine-tuning method.

  - `Grader grader`

    The grader used for the fine-tuning job.

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

  - `Optional<ReinforcementHyperparameters> hyperparameters`

    The hyperparameters used for the reinforcement fine-tuning job.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<ComputeMultiplier> computeMultiplier`

      Multiplier on amount of compute used for exploring search space during training.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<EvalInterval> evalInterval`

      The number of training steps between evaluation runs.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<EvalSamples> evalSamples`

      Number of evaluation samples to generate per training step.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<ReasoningEffort> reasoningEffort`

      Level of reasoning effort.

      - `DEFAULT("default")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

### Supervised Hyperparameters

- `class SupervisedHyperparameters:`

  The hyperparameters used for the fine-tuning job.

  - `Optional<BatchSize> batchSize`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

  - `Optional<LearningRateMultiplier> learningRateMultiplier`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `JsonValue;`

      - `AUTO("auto")`

    - `double`

  - `Optional<NEpochs> nEpochs`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `JsonValue;`

      - `AUTO("auto")`

    - `long`

### Supervised Method

- `class SupervisedMethod:`

  Configuration for the supervised fine-tuning method.

  - `Optional<SupervisedHyperparameters> hyperparameters`

    The hyperparameters used for the fine-tuning job.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

## Jobs

### Create

`FineTuningJob fineTuning().jobs().create(JobCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/jobs`

Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

#### Parameters

- `JobCreateParams params`

  - `Model model`

    The name of the model to fine-tune. You can select one of the
    [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

    - `BABBAGE_002("babbage-002")`

    - `DAVINCI_002("davinci-002")`

    - `GPT_3_5_TURBO("gpt-3.5-turbo")`

    - `GPT_4O_MINI("gpt-4o-mini")`

  - `String trainingFile`

    The ID of an uploaded file that contains training data.

    See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

    Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

    The contents of the file should differ depending on if the model uses the [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input), [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) format, or if the fine-tuning method uses the [preference](https://platform.openai.com/docs/api-reference/fine-tuning/preference-input) format.

    See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.

  - `Optional<Hyperparameters> hyperparameters`

    The hyperparameters used for the fine-tuning job.
    This value is now deprecated in favor of `method`, and should be passed in under the `method` parameter.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `Optional<List<Integration>> integrations`

    A list of integrations to enable for your fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of integration to enable. Currently, only "wandb" (Weights and Biases) is supported.

      - `WANDB("wandb")`

    - `Wandb wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

  - `Optional<Long> seed`

    The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
    If a seed is not specified, one will be generated for you.

  - `Optional<String> suffix`

    A string of up to 64 characters that will be added to your fine-tuned model name.

    For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

  - `Optional<String> validationFile`

    The ID of an uploaded file that contains validation data.

    If you provide this file, the data is used to generate validation
    metrics periodically during fine-tuning. These metrics can be viewed in
    the fine-tuning results file.
    The same data should not be present in both train and validation files.

    Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

    See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.

#### Returns

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.FineTuningJob;
import com.openai.models.finetuning.jobs.JobCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        JobCreateParams params = JobCreateParams.builder()
            .model(JobCreateParams.Model.GPT_4O_MINI)
            .trainingFile("file-abc123")
            .build();
        FineTuningJob fineTuningJob = client.fineTuning().jobs().create(params);
    }
}
```

### List

`JobListPage fineTuning().jobs().list(JobListParamsparams = JobListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/fine_tuning/jobs`

List your organization's fine-tuning jobs

#### Parameters

- `JobListParams params`

  - `Optional<String> after`

    Identifier for the last job from the previous pagination request.

  - `Optional<Long> limit`

    Number of fine-tuning jobs to retrieve.

  - `Optional<Metadata> metadata`

    Optional metadata filter. To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to indicate no metadata.

#### Returns

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.JobListPage;
import com.openai.models.finetuning.jobs.JobListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        JobListPage page = client.fineTuning().jobs().list();
    }
}
```

### Retrieve

`FineTuningJob fineTuning().jobs().retrieve(JobRetrieveParamsparams = JobRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}`

Get info about a fine-tuning job.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

#### Parameters

- `JobRetrieveParams params`

  - `Optional<String> fineTuningJobId`

#### Returns

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.FineTuningJob;
import com.openai.models.finetuning.jobs.JobRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FineTuningJob fineTuningJob = client.fineTuning().jobs().retrieve("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

### List Events

`JobListEventsPage fineTuning().jobs().listEvents(JobListEventsParamsparams = JobListEventsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}/events`

Get status updates for a fine-tuning job.

#### Parameters

- `JobListEventsParams params`

  - `Optional<String> fineTuningJobId`

  - `Optional<String> after`

    Identifier for the last event from the previous pagination request.

  - `Optional<Long> limit`

    Number of events to retrieve.

#### Returns

- `class FineTuningJobEvent:`

  Fine-tuning job event object

  - `String id`

    The object identifier.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Level level`

    The log level of the event.

    - `INFO("info")`

    - `WARN("warn")`

    - `ERROR("error")`

  - `String message`

    The message of the event.

  - `JsonValue; object_ "fine_tuning.job.event"constant`

    The object type, which is always "fine_tuning.job.event".

    - `FINE_TUNING_JOB_EVENT("fine_tuning.job.event")`

  - `Optional<JsonValue> data`

    The data associated with the event.

  - `Optional<Type> type`

    The type of event.

    - `MESSAGE("message")`

    - `METRICS("metrics")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.JobListEventsPage;
import com.openai.models.finetuning.jobs.JobListEventsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        JobListEventsPage page = client.fineTuning().jobs().listEvents("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

### Cancel

`FineTuningJob fineTuning().jobs().cancel(JobCancelParamsparams = JobCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/cancel`

Immediately cancel a fine-tune job.

#### Parameters

- `JobCancelParams params`

  - `Optional<String> fineTuningJobId`

#### Returns

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.FineTuningJob;
import com.openai.models.finetuning.jobs.JobCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FineTuningJob fineTuningJob = client.fineTuning().jobs().cancel("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

### Pause

`FineTuningJob fineTuning().jobs().pause(JobPauseParamsparams = JobPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/pause`

Pause a fine-tune job.

#### Parameters

- `JobPauseParams params`

  - `Optional<String> fineTuningJobId`

#### Returns

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.FineTuningJob;
import com.openai.models.finetuning.jobs.JobPauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FineTuningJob fineTuningJob = client.fineTuning().jobs().pause("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

### Resume

`FineTuningJob fineTuning().jobs().resume(JobResumeParamsparams = JobResumeParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/resume`

Resume a fine-tune job.

#### Parameters

- `JobResumeParams params`

  - `Optional<String> fineTuningJobId`

#### Returns

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.FineTuningJob;
import com.openai.models.finetuning.jobs.JobResumeParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FineTuningJob fineTuningJob = client.fineTuning().jobs().resume("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

#### Domain Types

#### Fine Tuning Job

- `class FineTuningJob:`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `String id`

    The object identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Optional<Error> error`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `Optional<String> param`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `Optional<String> fineTunedModel`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `Optional<Long> finishedAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters hyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `Optional<BatchSize> batchSize`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

    - `Optional<LearningRateMultiplier> learningRateMultiplier`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `JsonValue;`

        - `AUTO("auto")`

      - `double`

    - `Optional<NEpochs> nEpochs`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `JsonValue;`

        - `AUTO("auto")`

      - `long`

  - `String model`

    The base model that is being fine-tuned.

  - `JsonValue; object_ "fine_tuning.job"constant`

    The object type, which is always "fine_tuning.job".

    - `FINE_TUNING_JOB("fine_tuning.job")`

  - `String organizationId`

    The organization that owns the fine-tuning job.

  - `List<String> resultFiles`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `long seed`

    The seed used for the fine-tuning job.

  - `Status status`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `VALIDATING_FILES("validating_files")`

    - `QUEUED("queued")`

    - `RUNNING("running")`

    - `SUCCEEDED("succeeded")`

    - `FAILED("failed")`

    - `CANCELLED("cancelled")`

  - `Optional<Long> trainedTokens`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `String trainingFile`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<String> validationFile`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Optional<Long> estimatedFinish`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Optional<List<FineTuningJobWandbIntegrationObject>> integrations`

    A list of integrations to enable for this fine-tuning job.

    - `JsonValue; type "wandb"constant`

      The type of the integration being enabled for the fine-tuning job

      - `WANDB("wandb")`

    - `FineTuningJobWandbIntegration wandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `String project`

        The name of the project that the new run will be created under.

      - `Optional<String> entity`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Optional<String> name`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Optional<List<String>> tags`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Method> method`

    The method used for fine-tuning.

    - `Type type`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `SUPERVISED("supervised")`

      - `DPO("dpo")`

      - `REINFORCEMENT("reinforcement")`

    - `Optional<DpoMethod> dpo`

      Configuration for the DPO fine-tuning method.

      - `Optional<DpoHyperparameters> hyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<Beta> beta`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

    - `Optional<ReinforcementMethod> reinforcement`

      Configuration for the reinforcement fine-tuning method.

      - `Grader grader`

        The grader used for the fine-tuning job.

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

      - `Optional<ReinforcementHyperparameters> hyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ComputeMultiplier> computeMultiplier`

          Multiplier on amount of compute used for exploring search space during training.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<EvalInterval> evalInterval`

          The number of training steps between evaluation runs.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<EvalSamples> evalSamples`

          Number of evaluation samples to generate per training step.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<ReasoningEffort> reasoningEffort`

          Level of reasoning effort.

          - `DEFAULT("default")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

    - `Optional<SupervisedMethod> supervised`

      Configuration for the supervised fine-tuning method.

      - `Optional<SupervisedHyperparameters> hyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `Optional<BatchSize> batchSize`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

        - `Optional<LearningRateMultiplier> learningRateMultiplier`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `JsonValue;`

            - `AUTO("auto")`

          - `double`

        - `Optional<NEpochs> nEpochs`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `JsonValue;`

            - `AUTO("auto")`

          - `long`

#### Fine Tuning Job Event

- `class FineTuningJobEvent:`

  Fine-tuning job event object

  - `String id`

    The object identifier.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Level level`

    The log level of the event.

    - `INFO("info")`

    - `WARN("warn")`

    - `ERROR("error")`

  - `String message`

    The message of the event.

  - `JsonValue; object_ "fine_tuning.job.event"constant`

    The object type, which is always "fine_tuning.job.event".

    - `FINE_TUNING_JOB_EVENT("fine_tuning.job.event")`

  - `Optional<JsonValue> data`

    The data associated with the event.

  - `Optional<Type> type`

    The type of event.

    - `MESSAGE("message")`

    - `METRICS("metrics")`

#### Fine Tuning Job Wandb Integration

- `class FineTuningJobWandbIntegration:`

  The settings for your integration with Weights and Biases. This payload specifies the project that
  metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
  to your run, and set a default entity (team, username, etc) to be associated with your run.

  - `String project`

    The name of the project that the new run will be created under.

  - `Optional<String> entity`

    The entity to use for the run. This allows you to set the team or username of the WandB user that you would
    like associated with the run. If not set, the default entity for the registered WandB API key is used.

  - `Optional<String> name`

    A display name to set for the run. If not set, we will use the Job ID as the name.

  - `Optional<List<String>> tags`

    A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
    default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

#### Fine Tuning Job Wandb Integration Object

- `class FineTuningJobWandbIntegrationObject:`

  - `JsonValue; type "wandb"constant`

    The type of the integration being enabled for the fine-tuning job

    - `WANDB("wandb")`

  - `FineTuningJobWandbIntegration wandb`

    The settings for your integration with Weights and Biases. This payload specifies the project that
    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
    to your run, and set a default entity (team, username, etc) to be associated with your run.

    - `String project`

      The name of the project that the new run will be created under.

    - `Optional<String> entity`

      The entity to use for the run. This allows you to set the team or username of the WandB user that you would
      like associated with the run. If not set, the default entity for the registered WandB API key is used.

    - `Optional<String> name`

      A display name to set for the run. If not set, we will use the Job ID as the name.

    - `Optional<List<String>> tags`

      A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
      default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

### Checkpoints

#### List

`CheckpointListPage fineTuning().jobs().checkpoints().list(CheckpointListParamsparams = CheckpointListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints`

List checkpoints for a fine-tuning job.

##### Parameters

- `CheckpointListParams params`

  - `Optional<String> fineTuningJobId`

  - `Optional<String> after`

    Identifier for the last checkpoint ID from the previous pagination request.

  - `Optional<Long> limit`

    Number of checkpoints to retrieve.

##### Returns

- `class FineTuningJobCheckpoint:`

  The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

  - `String id`

    The checkpoint identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the checkpoint was created.

  - `String fineTunedModelCheckpoint`

    The name of the fine-tuned checkpoint model that is created.

  - `String fineTuningJobId`

    The name of the fine-tuning job that this checkpoint was created from.

  - `Metrics metrics`

    Metrics at the step number during the fine-tuning job.

    - `Optional<Double> fullValidLoss`

    - `Optional<Double> fullValidMeanTokenAccuracy`

    - `Optional<Double> step`

    - `Optional<Double> trainLoss`

    - `Optional<Double> trainMeanTokenAccuracy`

    - `Optional<Double> validLoss`

    - `Optional<Double> validMeanTokenAccuracy`

  - `JsonValue; object_ "fine_tuning.job.checkpoint"constant`

    The object type, which is always "fine_tuning.job.checkpoint".

    - `FINE_TUNING_JOB_CHECKPOINT("fine_tuning.job.checkpoint")`

  - `long stepNumber`

    The step number that the checkpoint was created at.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.checkpoints.CheckpointListPage;
import com.openai.models.finetuning.jobs.checkpoints.CheckpointListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CheckpointListPage page = client.fineTuning().jobs().checkpoints().list("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

##### Domain Types

##### Fine Tuning Job Checkpoint

- `class FineTuningJobCheckpoint:`

  The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

  - `String id`

    The checkpoint identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the checkpoint was created.

  - `String fineTunedModelCheckpoint`

    The name of the fine-tuned checkpoint model that is created.

  - `String fineTuningJobId`

    The name of the fine-tuning job that this checkpoint was created from.

  - `Metrics metrics`

    Metrics at the step number during the fine-tuning job.

    - `Optional<Double> fullValidLoss`

    - `Optional<Double> fullValidMeanTokenAccuracy`

    - `Optional<Double> step`

    - `Optional<Double> trainLoss`

    - `Optional<Double> trainMeanTokenAccuracy`

    - `Optional<Double> validLoss`

    - `Optional<Double> validMeanTokenAccuracy`

  - `JsonValue; object_ "fine_tuning.job.checkpoint"constant`

    The object type, which is always "fine_tuning.job.checkpoint".

    - `FINE_TUNING_JOB_CHECKPOINT("fine_tuning.job.checkpoint")`

  - `long stepNumber`

    The step number that the checkpoint was created at.

## Checkpoints

### Permissions

#### Retrieve

`PermissionRetrieveResponse fineTuning().checkpoints().permissions().retrieve(PermissionRetrieveParamsparams = PermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### Parameters

- `PermissionRetrieveParams params`

  - `Optional<String> fineTunedModelCheckpoint`

  - `Optional<String> after`

    Identifier for the last permission ID from the previous pagination request.

  - `Optional<Long> limit`

    Number of permissions to retrieve.

  - `Optional<Order> order`

    The order in which to retrieve permissions.

    - `ASCENDING("ascending")`

    - `DESCENDING("descending")`

  - `Optional<String> projectId`

    The ID of the project to get permissions for.

##### Returns

- `class PermissionRetrieveResponse:`

  - `List<Data> data`

    - `String id`

      The permission identifier, which can be referenced in the API endpoints.

    - `long createdAt`

      The Unix timestamp (in seconds) for when the permission was created.

    - `JsonValue; object_ "checkpoint.permission"constant`

      The object type, which is always "checkpoint.permission".

      - `CHECKPOINT_PERMISSION("checkpoint.permission")`

    - `String projectId`

      The project identifier that the permission is for.

  - `boolean hasMore`

  - `JsonValue; object_ "list"constant`

    - `LIST("list")`

  - `Optional<String> firstId`

  - `Optional<String> lastId`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.checkpoints.permissions.PermissionRetrieveParams;
import com.openai.models.finetuning.checkpoints.permissions.PermissionRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionRetrieveResponse permission = client.fineTuning().checkpoints().permissions().retrieve("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

#### List

`PermissionListPage fineTuning().checkpoints().permissions().list(PermissionListParamsparams = PermissionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### Parameters

- `PermissionListParams params`

  - `Optional<String> fineTunedModelCheckpoint`

  - `Optional<String> after`

    Identifier for the last permission ID from the previous pagination request.

  - `Optional<Long> limit`

    Number of permissions to retrieve.

  - `Optional<Order> order`

    The order in which to retrieve permissions.

    - `ASCENDING("ascending")`

    - `DESCENDING("descending")`

  - `Optional<String> projectId`

    The ID of the project to get permissions for.

##### Returns

- `class PermissionListResponse:`

  The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

  - `String id`

    The permission identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the permission was created.

  - `JsonValue; object_ "checkpoint.permission"constant`

    The object type, which is always "checkpoint.permission".

    - `CHECKPOINT_PERMISSION("checkpoint.permission")`

  - `String projectId`

    The project identifier that the permission is for.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.checkpoints.permissions.PermissionListPage;
import com.openai.models.finetuning.checkpoints.permissions.PermissionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionListPage page = client.fineTuning().checkpoints().permissions().list("ft-AF1WoRqd3aJAHsqc9NY7iL8F");
    }
}
```

#### Create

`PermissionCreatePage fineTuning().checkpoints().permissions().create(PermissionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### Parameters

- `PermissionCreateParams params`

  - `Optional<String> fineTunedModelCheckpoint`

  - `List<String> projectIds`

    The project identifiers to grant access to.

##### Returns

- `class PermissionCreateResponse:`

  The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

  - `String id`

    The permission identifier, which can be referenced in the API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the permission was created.

  - `JsonValue; object_ "checkpoint.permission"constant`

    The object type, which is always "checkpoint.permission".

    - `CHECKPOINT_PERMISSION("checkpoint.permission")`

  - `String projectId`

    The project identifier that the permission is for.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.checkpoints.permissions.PermissionCreatePage;
import com.openai.models.finetuning.checkpoints.permissions.PermissionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionCreateParams params = PermissionCreateParams.builder()
            .fineTunedModelCheckpoint("ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd")
            .addProjectId("string")
            .build();
        PermissionCreatePage page = client.fineTuning().checkpoints().permissions().create(params);
    }
}
```

#### Delete

`PermissionDeleteResponse fineTuning().checkpoints().permissions().delete(PermissionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### Parameters

- `PermissionDeleteParams params`

  - `String fineTunedModelCheckpoint`

  - `Optional<String> permissionId`

##### Returns

- `class PermissionDeleteResponse:`

  - `String id`

    The ID of the fine-tuned model checkpoint permission that was deleted.

  - `boolean deleted`

    Whether the fine-tuned model checkpoint permission was successfully deleted.

  - `JsonValue; object_ "checkpoint.permission"constant`

    The object type, which is always "checkpoint.permission".

    - `CHECKPOINT_PERMISSION("checkpoint.permission")`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.checkpoints.permissions.PermissionDeleteParams;
import com.openai.models.finetuning.checkpoints.permissions.PermissionDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        PermissionDeleteParams params = PermissionDeleteParams.builder()
            .fineTunedModelCheckpoint("ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd")
            .permissionId("cp_zc4Q7MP6XxulcVzj4MZdwsAB")
            .build();
        PermissionDeleteResponse permission = client.fineTuning().checkpoints().permissions().delete(params);
    }
}
```

## Alpha

### Graders

#### Run

`GraderRunResponse fineTuning().alpha().graders().run(GraderRunParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/alpha/graders/run`

Run a grader.

##### Parameters

- `GraderRunParams params`

  - `Grader grader`

    The grader used for the fine-tuning job.

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

  - `String modelSample`

    The model sample to be evaluated. This value will be used to populate
    the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
    The `output_json` variable will be populated if the model sample is a
    valid JSON string.

  - `Optional<JsonValue> item`

    The dataset item provided to the grader. This will be used to populate
    the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.

##### Returns

- `class GraderRunResponse:`

  - `Metadata metadata`

    - `Errors errors`

      - `boolean formulaParseError`

      - `boolean invalidVariableError`

      - `boolean modelGraderParseError`

      - `boolean modelGraderRefusalError`

      - `boolean modelGraderServerError`

      - `Optional<String> modelGraderServerErrorDetails`

      - `boolean otherError`

      - `boolean pythonGraderRuntimeError`

      - `Optional<String> pythonGraderRuntimeErrorDetails`

      - `boolean pythonGraderServerError`

      - `Optional<String> pythonGraderServerErrorType`

      - `boolean sampleParseError`

      - `boolean truncatedObservationError`

      - `boolean unresponsiveRewardError`

    - `double executionTime`

    - `String name`

    - `Optional<String> sampledModelName`

    - `Scores scores`

    - `Optional<Long> tokenUsage`

    - `String type`

  - `ModelGraderTokenUsagePerModel modelGraderTokenUsagePerModel`

  - `double reward`

  - `SubRewards subRewards`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.alpha.graders.GraderRunParams;
import com.openai.models.finetuning.alpha.graders.GraderRunResponse;
import com.openai.models.graders.gradermodels.StringCheckGrader;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GraderRunParams params = GraderRunParams.builder()
            .grader(StringCheckGrader.builder()
                .input("input")
                .name("name")
                .operation(StringCheckGrader.Operation.EQ)
                .reference("reference")
                .build())
            .modelSample("model_sample")
            .build();
        GraderRunResponse response = client.fineTuning().alpha().graders().run(params);
    }
}
```

#### Validate

`GraderValidateResponse fineTuning().alpha().graders().validate(GraderValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/fine_tuning/alpha/graders/validate`

Validate a grader.

##### Parameters

- `GraderValidateParams params`

  - `Grader grader`

    The grader used for the fine-tuning job.

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

##### Returns

- `class GraderValidateResponse:`

  - `Optional<Grader> grader`

    The grader used for the fine-tuning job.

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

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.alpha.graders.GraderValidateParams;
import com.openai.models.finetuning.alpha.graders.GraderValidateResponse;
import com.openai.models.graders.gradermodels.StringCheckGrader;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        GraderValidateParams params = GraderValidateParams.builder()
            .grader(StringCheckGrader.builder()
                .input("input")
                .name("name")
                .operation(StringCheckGrader.Operation.EQ)
                .reference("reference")
                .build())
            .build();
        GraderValidateResponse response = client.fineTuning().alpha().graders().validate(params);
    }
}
```
