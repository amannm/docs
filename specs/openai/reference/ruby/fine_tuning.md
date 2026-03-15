# Fine Tuning

## Methods

### Domain Types

### Dpo Hyperparameters

- `class DpoHyperparameters`

  The hyperparameters used for the DPO fine-tuning job.

  - `batch_size: :auto | Integer`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `BatchSize = :auto`

      - `:auto`

    - `Integer`

  - `beta: :auto | Float`

    The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

    - `Beta = :auto`

      - `:auto`

    - `Float`

  - `learning_rate_multiplier: :auto | Float`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `LearningRateMultiplier = :auto`

      - `:auto`

    - `Float`

  - `n_epochs: :auto | Integer`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `NEpochs = :auto`

      - `:auto`

    - `Integer`

### Dpo Method

- `class DpoMethod`

  Configuration for the DPO fine-tuning method.

  - `hyperparameters: DpoHyperparameters`

    The hyperparameters used for the DPO fine-tuning job.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `beta: :auto | Float`

      The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

      - `Beta = :auto`

        - `:auto`

      - `Float`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

### Reinforcement Hyperparameters

- `class ReinforcementHyperparameters`

  The hyperparameters used for the reinforcement fine-tuning job.

  - `batch_size: :auto | Integer`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `BatchSize = :auto`

      - `:auto`

    - `Integer`

  - `compute_multiplier: :auto | Float`

    Multiplier on amount of compute used for exploring search space during training.

    - `ComputeMultiplier = :auto`

      - `:auto`

    - `Float`

  - `eval_interval: :auto | Integer`

    The number of training steps between evaluation runs.

    - `EvalInterval = :auto`

      - `:auto`

    - `Integer`

  - `eval_samples: :auto | Integer`

    Number of evaluation samples to generate per training step.

    - `EvalSamples = :auto`

      - `:auto`

    - `Integer`

  - `learning_rate_multiplier: :auto | Float`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `LearningRateMultiplier = :auto`

      - `:auto`

    - `Float`

  - `n_epochs: :auto | Integer`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `NEpochs = :auto`

      - `:auto`

    - `Integer`

  - `reasoning_effort: :default | :low | :medium | :high`

    Level of reasoning effort.

    - `:default`

    - `:low`

    - `:medium`

    - `:high`

### Reinforcement Method

- `class ReinforcementMethod`

  Configuration for the reinforcement fine-tuning method.

  - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

    The grader used for the fine-tuning job.

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

    - `class TextSimilarityGrader`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `:cosine`

        - `:fuzzy_match`

        - `:bleu`

        - `:gleu`

        - `:meteor`

        - `:rouge_1`

        - `:rouge_2`

        - `:rouge_3`

        - `:rouge_4`

        - `:rouge_5`

        - `:rouge_l`

      - `input: String`

        The text being graded.

      - `name: String`

        The name of the grader.

      - `reference: String`

        The text being graded against.

      - `type: :text_similarity`

        The type of grader.

        - `:text_similarity`

    - `class PythonGrader`

      A PythonGrader object that runs a python script on the input.

      - `name: String`

        The name of the grader.

      - `source: String`

        The source code of the python script.

      - `type: :python`

        The object type, which is always `python`.

        - `:python`

      - `image_tag: String`

        The image tag to use for the python script.

    - `class ScoreModelGrader`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `input: Array[{ content, role, type}]`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

      - `model: String`

        The model to use for the evaluation.

      - `name: String`

        The name of the grader.

      - `type: :score_model`

        The object type, which is always `score_model`.

        - `:score_model`

      - `range: Array[Float]`

        The range of the score. Defaults to `[0, 1]`.

      - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

        The sampling parameters for the model.

        - `max_completions_tokens: Integer`

          The maximum number of tokens the grader model may generate in its response.

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

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class MultiGrader`

      A MultiGrader object combines the output of multiple graders to produce a single score.

      - `calculate_output: String`

        A formula to calculate the output based on grader results.

      - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

      - `name: String`

        The name of the grader.

      - `type: :multi`

        The object type, which is always `multi`.

        - `:multi`

  - `hyperparameters: ReinforcementHyperparameters`

    The hyperparameters used for the reinforcement fine-tuning job.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `compute_multiplier: :auto | Float`

      Multiplier on amount of compute used for exploring search space during training.

      - `ComputeMultiplier = :auto`

        - `:auto`

      - `Float`

    - `eval_interval: :auto | Integer`

      The number of training steps between evaluation runs.

      - `EvalInterval = :auto`

        - `:auto`

      - `Integer`

    - `eval_samples: :auto | Integer`

      Number of evaluation samples to generate per training step.

      - `EvalSamples = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

    - `reasoning_effort: :default | :low | :medium | :high`

      Level of reasoning effort.

      - `:default`

      - `:low`

      - `:medium`

      - `:high`

### Supervised Hyperparameters

- `class SupervisedHyperparameters`

  The hyperparameters used for the fine-tuning job.

  - `batch_size: :auto | Integer`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `BatchSize = :auto`

      - `:auto`

    - `Integer`

  - `learning_rate_multiplier: :auto | Float`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `LearningRateMultiplier = :auto`

      - `:auto`

    - `Float`

  - `n_epochs: :auto | Integer`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `NEpochs = :auto`

      - `:auto`

    - `Integer`

### Supervised Method

- `class SupervisedMethod`

  Configuration for the supervised fine-tuning method.

  - `hyperparameters: SupervisedHyperparameters`

    The hyperparameters used for the fine-tuning job.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

## Jobs

### Create

`fine_tuning.jobs.create(**kwargs) -> FineTuningJob`

**post** `/fine_tuning/jobs`

Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

#### Parameters

- `model: String | :"babbage-002" | :"davinci-002" | :"gpt-3.5-turbo" | :"gpt-4o-mini"`

  The name of the model to fine-tune. You can select one of the
  [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

  - `String`

  - `:"babbage-002" | :"davinci-002" | :"gpt-3.5-turbo" | :"gpt-4o-mini"`

    The name of the model to fine-tune. You can select one of the
    [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

    - `:"babbage-002"`

    - `:"davinci-002"`

    - `:"gpt-3.5-turbo"`

    - `:"gpt-4o-mini"`

- `training_file: String`

  The ID of an uploaded file that contains training data.

  See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

  Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

  The contents of the file should differ depending on if the model uses the [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input), [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) format, or if the fine-tuning method uses the [preference](https://platform.openai.com/docs/api-reference/fine-tuning/preference-input) format.

  See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.

- `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

  The hyperparameters used for the fine-tuning job.
  This value is now deprecated in favor of `method`, and should be passed in under the `method` parameter.

  - `batch_size: :auto | Integer`

    Number of examples in each batch. A larger batch size means that model parameters
    are updated less frequently, but with lower variance.

    - `BatchSize = :auto`

      - `:auto`

    - `Integer`

  - `learning_rate_multiplier: :auto | Float`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
    overfitting.

    - `LearningRateMultiplier = :auto`

      - `:auto`

    - `Float`

  - `n_epochs: :auto | Integer`

    The number of epochs to train the model for. An epoch refers to one full cycle
    through the training dataset.

    - `NEpochs = :auto`

      - `:auto`

    - `Integer`

- `integrations: Array[{ type, wandb}]`

  A list of integrations to enable for your fine-tuning job.

  - `type: :wandb`

    The type of integration to enable. Currently, only "wandb" (Weights and Biases) is supported.

    - `:wandb`

  - `wandb: { project, entity, name, tags}`

    The settings for your integration with Weights and Biases. This payload specifies the project that
    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
    to your run, and set a default entity (team, username, etc) to be associated with your run.

    - `project: String`

      The name of the project that the new run will be created under.

    - `entity: String`

      The entity to use for the run. This allows you to set the team or username of the WandB user that you would
      like associated with the run. If not set, the default entity for the registered WandB API key is used.

    - `name: String`

      A display name to set for the run. If not set, we will use the Job ID as the name.

    - `tags: Array[String]`

      A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
      default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

- `metadata: Metadata`

  Set of 16 key-value pairs that can be attached to an object. This can be
  useful for storing additional information about the object in a structured
  format, and querying for objects via API or the dashboard.

  Keys are strings with a maximum length of 64 characters. Values are strings
  with a maximum length of 512 characters.

- `method_: { type, dpo, reinforcement, supervised}`

  The method used for fine-tuning.

  - `type: :supervised | :dpo | :reinforcement`

    The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

    - `:supervised`

    - `:dpo`

    - `:reinforcement`

  - `dpo: DpoMethod`

    Configuration for the DPO fine-tuning method.

    - `hyperparameters: DpoHyperparameters`

      The hyperparameters used for the DPO fine-tuning job.

      - `batch_size: :auto | Integer`

        Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

        - `BatchSize = :auto`

          - `:auto`

        - `Integer`

      - `beta: :auto | Float`

        The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

        - `Beta = :auto`

          - `:auto`

        - `Float`

      - `learning_rate_multiplier: :auto | Float`

        Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

        - `LearningRateMultiplier = :auto`

          - `:auto`

        - `Float`

      - `n_epochs: :auto | Integer`

        The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

        - `NEpochs = :auto`

          - `:auto`

        - `Integer`

  - `reinforcement: ReinforcementMethod`

    Configuration for the reinforcement fine-tuning method.

    - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

      The grader used for the fine-tuning job.

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

      - `class TextSimilarityGrader`

        A TextSimilarityGrader object which grades text based on similarity metrics.

        - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

          The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
          `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
          or `rouge_l`.

          - `:cosine`

          - `:fuzzy_match`

          - `:bleu`

          - `:gleu`

          - `:meteor`

          - `:rouge_1`

          - `:rouge_2`

          - `:rouge_3`

          - `:rouge_4`

          - `:rouge_5`

          - `:rouge_l`

        - `input: String`

          The text being graded.

        - `name: String`

          The name of the grader.

        - `reference: String`

          The text being graded against.

        - `type: :text_similarity`

          The type of grader.

          - `:text_similarity`

      - `class PythonGrader`

        A PythonGrader object that runs a python script on the input.

        - `name: String`

          The name of the grader.

        - `source: String`

          The source code of the python script.

        - `type: :python`

          The object type, which is always `python`.

          - `:python`

        - `image_tag: String`

          The image tag to use for the python script.

      - `class ScoreModelGrader`

        A ScoreModelGrader object that uses a model to assign a score to the input.

        - `input: Array[{ content, role, type}]`

          The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

        - `model: String`

          The model to use for the evaluation.

        - `name: String`

          The name of the grader.

        - `type: :score_model`

          The object type, which is always `score_model`.

          - `:score_model`

        - `range: Array[Float]`

          The range of the score. Defaults to `[0, 1]`.

        - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

          The sampling parameters for the model.

          - `max_completions_tokens: Integer`

            The maximum number of tokens the grader model may generate in its response.

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

          - `top_p: Float`

            An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

      - `class MultiGrader`

        A MultiGrader object combines the output of multiple graders to produce a single score.

        - `calculate_output: String`

          A formula to calculate the output based on grader results.

        - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

          - `class TextSimilarityGrader`

            A TextSimilarityGrader object which grades text based on similarity metrics.

            - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

              The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
              `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
              or `rouge_l`.

              - `:cosine`

              - `:fuzzy_match`

              - `:bleu`

              - `:gleu`

              - `:meteor`

              - `:rouge_1`

              - `:rouge_2`

              - `:rouge_3`

              - `:rouge_4`

              - `:rouge_5`

              - `:rouge_l`

            - `input: String`

              The text being graded.

            - `name: String`

              The name of the grader.

            - `reference: String`

              The text being graded against.

            - `type: :text_similarity`

              The type of grader.

              - `:text_similarity`

          - `class PythonGrader`

            A PythonGrader object that runs a python script on the input.

            - `name: String`

              The name of the grader.

            - `source: String`

              The source code of the python script.

            - `type: :python`

              The object type, which is always `python`.

              - `:python`

            - `image_tag: String`

              The image tag to use for the python script.

          - `class ScoreModelGrader`

            A ScoreModelGrader object that uses a model to assign a score to the input.

            - `input: Array[{ content, role, type}]`

              The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

            - `model: String`

              The model to use for the evaluation.

            - `name: String`

              The name of the grader.

            - `type: :score_model`

              The object type, which is always `score_model`.

              - `:score_model`

            - `range: Array[Float]`

              The range of the score. Defaults to `[0, 1]`.

            - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

              The sampling parameters for the model.

              - `max_completions_tokens: Integer`

                The maximum number of tokens the grader model may generate in its response.

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

              - `top_p: Float`

                An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

        - `name: String`

          The name of the grader.

        - `type: :multi`

          The object type, which is always `multi`.

          - `:multi`

    - `hyperparameters: ReinforcementHyperparameters`

      The hyperparameters used for the reinforcement fine-tuning job.

      - `batch_size: :auto | Integer`

        Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

        - `BatchSize = :auto`

          - `:auto`

        - `Integer`

      - `compute_multiplier: :auto | Float`

        Multiplier on amount of compute used for exploring search space during training.

        - `ComputeMultiplier = :auto`

          - `:auto`

        - `Float`

      - `eval_interval: :auto | Integer`

        The number of training steps between evaluation runs.

        - `EvalInterval = :auto`

          - `:auto`

        - `Integer`

      - `eval_samples: :auto | Integer`

        Number of evaluation samples to generate per training step.

        - `EvalSamples = :auto`

          - `:auto`

        - `Integer`

      - `learning_rate_multiplier: :auto | Float`

        Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

        - `LearningRateMultiplier = :auto`

          - `:auto`

        - `Float`

      - `n_epochs: :auto | Integer`

        The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

        - `NEpochs = :auto`

          - `:auto`

        - `Integer`

      - `reasoning_effort: :default | :low | :medium | :high`

        Level of reasoning effort.

        - `:default`

        - `:low`

        - `:medium`

        - `:high`

  - `supervised: SupervisedMethod`

    Configuration for the supervised fine-tuning method.

    - `hyperparameters: SupervisedHyperparameters`

      The hyperparameters used for the fine-tuning job.

      - `batch_size: :auto | Integer`

        Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

        - `BatchSize = :auto`

          - `:auto`

        - `Integer`

      - `learning_rate_multiplier: :auto | Float`

        Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

        - `LearningRateMultiplier = :auto`

          - `:auto`

        - `Float`

      - `n_epochs: :auto | Integer`

        The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

        - `NEpochs = :auto`

          - `:auto`

        - `Integer`

- `seed: Integer`

  The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
  If a seed is not specified, one will be generated for you.

- `suffix: String`

  A string of up to 64 characters that will be added to your fine-tuned model name.

  For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

- `validation_file: String`

  The ID of an uploaded file that contains validation data.

  If you provide this file, the data is used to generate validation
  metrics periodically during fine-tuning. These metrics can be viewed in
  the fine-tuning results file.
  The same data should not be present in both train and validation files.

  Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

  See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.

#### Returns

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

fine_tuning_job = openai.fine_tuning.jobs.create(model: :"gpt-4o-mini", training_file: "file-abc123")

puts(fine_tuning_job)
```

### List

`fine_tuning.jobs.list(**kwargs) -> CursorPage<FineTuningJob>`

**get** `/fine_tuning/jobs`

List your organization's fine-tuning jobs

#### Parameters

- `after: String`

  Identifier for the last job from the previous pagination request.

- `limit: Integer`

  Number of fine-tuning jobs to retrieve.

- `metadata: Hash[Symbol, String]`

  Optional metadata filter. To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to indicate no metadata.

#### Returns

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.fine_tuning.jobs.list

puts(page)
```

### Retrieve

`fine_tuning.jobs.retrieve(fine_tuning_job_id) -> FineTuningJob`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}`

Get info about a fine-tuning job.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

#### Parameters

- `fine_tuning_job_id: String`

#### Returns

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

fine_tuning_job = openai.fine_tuning.jobs.retrieve("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(fine_tuning_job)
```

### List Events

`fine_tuning.jobs.list_events(fine_tuning_job_id, **kwargs) -> CursorPage<FineTuningJobEvent>`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}/events`

Get status updates for a fine-tuning job.

#### Parameters

- `fine_tuning_job_id: String`

- `after: String`

  Identifier for the last event from the previous pagination request.

- `limit: Integer`

  Number of events to retrieve.

#### Returns

- `class FineTuningJobEvent`

  Fine-tuning job event object

  - `id: String`

    The object identifier.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `level: :info | :warn | :error`

    The log level of the event.

    - `:info`

    - `:warn`

    - `:error`

  - `message: String`

    The message of the event.

  - `object: :"fine_tuning.job.event"`

    The object type, which is always "fine_tuning.job.event".

    - `:"fine_tuning.job.event"`

  - `data: untyped`

    The data associated with the event.

  - `type: :message | :metrics`

    The type of event.

    - `:message`

    - `:metrics`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.fine_tuning.jobs.list_events("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(page)
```

### Cancel

`fine_tuning.jobs.cancel(fine_tuning_job_id) -> FineTuningJob`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/cancel`

Immediately cancel a fine-tune job.

#### Parameters

- `fine_tuning_job_id: String`

#### Returns

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

fine_tuning_job = openai.fine_tuning.jobs.cancel("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(fine_tuning_job)
```

### Pause

`fine_tuning.jobs.pause(fine_tuning_job_id) -> FineTuningJob`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/pause`

Pause a fine-tune job.

#### Parameters

- `fine_tuning_job_id: String`

#### Returns

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

fine_tuning_job = openai.fine_tuning.jobs.pause("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(fine_tuning_job)
```

### Resume

`fine_tuning.jobs.resume(fine_tuning_job_id) -> FineTuningJob`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/resume`

Resume a fine-tune job.

#### Parameters

- `fine_tuning_job_id: String`

#### Returns

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

fine_tuning_job = openai.fine_tuning.jobs.resume("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(fine_tuning_job)
```

#### Domain Types

#### Fine Tuning Job

- `class FineTuningJob`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `id: String`

    The object identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `error: { code, message, param}`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `param: String`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `fine_tuned_model: String`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `finished_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `hyperparameters: { batch_size, learning_rate_multiplier, n_epochs}`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `batch_size: :auto | Integer`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `BatchSize = :auto`

        - `:auto`

      - `Integer`

    - `learning_rate_multiplier: :auto | Float`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `LearningRateMultiplier = :auto`

        - `:auto`

      - `Float`

    - `n_epochs: :auto | Integer`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `NEpochs = :auto`

        - `:auto`

      - `Integer`

  - `model: String`

    The base model that is being fine-tuned.

  - `object: :"fine_tuning.job"`

    The object type, which is always "fine_tuning.job".

    - `:"fine_tuning.job"`

  - `organization_id: String`

    The organization that owns the fine-tuning job.

  - `result_files: Array[String]`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `seed: Integer`

    The seed used for the fine-tuning job.

  - `status: :validating_files | :queued | :running | 3 more`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `:validating_files`

    - `:queued`

    - `:running`

    - `:succeeded`

    - `:failed`

    - `:cancelled`

  - `trained_tokens: Integer`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `training_file: String`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `validation_file: String`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `estimated_finish: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `integrations: Array[FineTuningJobWandbIntegrationObject]`

    A list of integrations to enable for this fine-tuning job.

    - `type: :wandb`

      The type of the integration being enabled for the fine-tuning job

      - `:wandb`

    - `wandb: FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `project: String`

        The name of the project that the new run will be created under.

      - `entity: String`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `name: String`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `tags: Array[String]`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `metadata: Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `method_: { type, dpo, reinforcement, supervised}`

    The method used for fine-tuning.

    - `type: :supervised | :dpo | :reinforcement`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `:supervised`

      - `:dpo`

      - `:reinforcement`

    - `dpo: DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `hyperparameters: DpoHyperparameters`

        The hyperparameters used for the DPO fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `beta: :auto | Float`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `Beta = :auto`

            - `:auto`

          - `Float`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

    - `reinforcement: ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        The grader used for the fine-tuning job.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `class MultiGrader`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `calculate_output: String`

            A formula to calculate the output based on grader results.

          - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

            - `class TextSimilarityGrader`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `:cosine`

                - `:fuzzy_match`

                - `:bleu`

                - `:gleu`

                - `:meteor`

                - `:rouge_1`

                - `:rouge_2`

                - `:rouge_3`

                - `:rouge_4`

                - `:rouge_5`

                - `:rouge_l`

              - `input: String`

                The text being graded.

              - `name: String`

                The name of the grader.

              - `reference: String`

                The text being graded against.

              - `type: :text_similarity`

                The type of grader.

                - `:text_similarity`

            - `class PythonGrader`

              A PythonGrader object that runs a python script on the input.

              - `name: String`

                The name of the grader.

              - `source: String`

                The source code of the python script.

              - `type: :python`

                The object type, which is always `python`.

                - `:python`

              - `image_tag: String`

                The image tag to use for the python script.

            - `class ScoreModelGrader`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `input: Array[{ content, role, type}]`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

              - `model: String`

                The model to use for the evaluation.

              - `name: String`

                The name of the grader.

              - `type: :score_model`

                The object type, which is always `score_model`.

                - `:score_model`

              - `range: Array[Float]`

                The range of the score. Defaults to `[0, 1]`.

              - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

                The sampling parameters for the model.

                - `max_completions_tokens: Integer`

                  The maximum number of tokens the grader model may generate in its response.

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

                - `top_p: Float`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

          - `name: String`

            The name of the grader.

          - `type: :multi`

            The object type, which is always `multi`.

            - `:multi`

      - `hyperparameters: ReinforcementHyperparameters`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `compute_multiplier: :auto | Float`

          Multiplier on amount of compute used for exploring search space during training.

          - `ComputeMultiplier = :auto`

            - `:auto`

          - `Float`

        - `eval_interval: :auto | Integer`

          The number of training steps between evaluation runs.

          - `EvalInterval = :auto`

            - `:auto`

          - `Integer`

        - `eval_samples: :auto | Integer`

          Number of evaluation samples to generate per training step.

          - `EvalSamples = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

        - `reasoning_effort: :default | :low | :medium | :high`

          Level of reasoning effort.

          - `:default`

          - `:low`

          - `:medium`

          - `:high`

    - `supervised: SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `hyperparameters: SupervisedHyperparameters`

        The hyperparameters used for the fine-tuning job.

        - `batch_size: :auto | Integer`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `BatchSize = :auto`

            - `:auto`

          - `Integer`

        - `learning_rate_multiplier: :auto | Float`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `LearningRateMultiplier = :auto`

            - `:auto`

          - `Float`

        - `n_epochs: :auto | Integer`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `NEpochs = :auto`

            - `:auto`

          - `Integer`

#### Fine Tuning Job Event

- `class FineTuningJobEvent`

  Fine-tuning job event object

  - `id: String`

    The object identifier.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `level: :info | :warn | :error`

    The log level of the event.

    - `:info`

    - `:warn`

    - `:error`

  - `message: String`

    The message of the event.

  - `object: :"fine_tuning.job.event"`

    The object type, which is always "fine_tuning.job.event".

    - `:"fine_tuning.job.event"`

  - `data: untyped`

    The data associated with the event.

  - `type: :message | :metrics`

    The type of event.

    - `:message`

    - `:metrics`

#### Fine Tuning Job Wandb Integration

- `class FineTuningJobWandbIntegration`

  The settings for your integration with Weights and Biases. This payload specifies the project that
  metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
  to your run, and set a default entity (team, username, etc) to be associated with your run.

  - `project: String`

    The name of the project that the new run will be created under.

  - `entity: String`

    The entity to use for the run. This allows you to set the team or username of the WandB user that you would
    like associated with the run. If not set, the default entity for the registered WandB API key is used.

  - `name: String`

    A display name to set for the run. If not set, we will use the Job ID as the name.

  - `tags: Array[String]`

    A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
    default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

#### Fine Tuning Job Wandb Integration Object

- `class FineTuningJobWandbIntegrationObject`

  - `type: :wandb`

    The type of the integration being enabled for the fine-tuning job

    - `:wandb`

  - `wandb: FineTuningJobWandbIntegration`

    The settings for your integration with Weights and Biases. This payload specifies the project that
    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
    to your run, and set a default entity (team, username, etc) to be associated with your run.

    - `project: String`

      The name of the project that the new run will be created under.

    - `entity: String`

      The entity to use for the run. This allows you to set the team or username of the WandB user that you would
      like associated with the run. If not set, the default entity for the registered WandB API key is used.

    - `name: String`

      A display name to set for the run. If not set, we will use the Job ID as the name.

    - `tags: Array[String]`

      A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
      default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

### Checkpoints

#### List

`fine_tuning.jobs.checkpoints.list(fine_tuning_job_id, **kwargs) -> CursorPage<FineTuningJobCheckpoint>`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints`

List checkpoints for a fine-tuning job.

##### Parameters

- `fine_tuning_job_id: String`

- `after: String`

  Identifier for the last checkpoint ID from the previous pagination request.

- `limit: Integer`

  Number of checkpoints to retrieve.

##### Returns

- `class FineTuningJobCheckpoint`

  The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

  - `id: String`

    The checkpoint identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the checkpoint was created.

  - `fine_tuned_model_checkpoint: String`

    The name of the fine-tuned checkpoint model that is created.

  - `fine_tuning_job_id: String`

    The name of the fine-tuning job that this checkpoint was created from.

  - `metrics: { full_valid_loss, full_valid_mean_token_accuracy, step, 4 more}`

    Metrics at the step number during the fine-tuning job.

    - `full_valid_loss: Float`

    - `full_valid_mean_token_accuracy: Float`

    - `step: Float`

    - `train_loss: Float`

    - `train_mean_token_accuracy: Float`

    - `valid_loss: Float`

    - `valid_mean_token_accuracy: Float`

  - `object: :"fine_tuning.job.checkpoint"`

    The object type, which is always "fine_tuning.job.checkpoint".

    - `:"fine_tuning.job.checkpoint"`

  - `step_number: Integer`

    The step number that the checkpoint was created at.

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.fine_tuning.jobs.checkpoints.list("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(page)
```

##### Domain Types

##### Fine Tuning Job Checkpoint

- `class FineTuningJobCheckpoint`

  The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

  - `id: String`

    The checkpoint identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the checkpoint was created.

  - `fine_tuned_model_checkpoint: String`

    The name of the fine-tuned checkpoint model that is created.

  - `fine_tuning_job_id: String`

    The name of the fine-tuning job that this checkpoint was created from.

  - `metrics: { full_valid_loss, full_valid_mean_token_accuracy, step, 4 more}`

    Metrics at the step number during the fine-tuning job.

    - `full_valid_loss: Float`

    - `full_valid_mean_token_accuracy: Float`

    - `step: Float`

    - `train_loss: Float`

    - `train_mean_token_accuracy: Float`

    - `valid_loss: Float`

    - `valid_mean_token_accuracy: Float`

  - `object: :"fine_tuning.job.checkpoint"`

    The object type, which is always "fine_tuning.job.checkpoint".

    - `:"fine_tuning.job.checkpoint"`

  - `step_number: Integer`

    The step number that the checkpoint was created at.

## Checkpoints

### Permissions

#### Retrieve

`fine_tuning.checkpoints.permissions.retrieve(fine_tuned_model_checkpoint, **kwargs) -> PermissionRetrieveResponse`

**get** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### Parameters

- `fine_tuned_model_checkpoint: String`

- `after: String`

  Identifier for the last permission ID from the previous pagination request.

- `limit: Integer`

  Number of permissions to retrieve.

- `order: :ascending | :descending`

  The order in which to retrieve permissions.

  - `:ascending`

  - `:descending`

- `project_id: String`

  The ID of the project to get permissions for.

##### Returns

- `class PermissionRetrieveResponse`

  - `data: Array[{ id, created_at, object, project_id}]`

    - `id: String`

      The permission identifier, which can be referenced in the API endpoints.

    - `created_at: Integer`

      The Unix timestamp (in seconds) for when the permission was created.

    - `object: :"checkpoint.permission"`

      The object type, which is always "checkpoint.permission".

      - `:"checkpoint.permission"`

    - `project_id: String`

      The project identifier that the permission is for.

  - `has_more: bool`

  - `object: :list`

    - `:list`

  - `first_id: String`

  - `last_id: String`

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

permission = openai.fine_tuning.checkpoints.permissions.retrieve("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(permission)
```

#### List

`fine_tuning.checkpoints.permissions.list(fine_tuned_model_checkpoint, **kwargs) -> ConversationCursorPage<PermissionListResponse>`

**get** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### Parameters

- `fine_tuned_model_checkpoint: String`

- `after: String`

  Identifier for the last permission ID from the previous pagination request.

- `limit: Integer`

  Number of permissions to retrieve.

- `order: :ascending | :descending`

  The order in which to retrieve permissions.

  - `:ascending`

  - `:descending`

- `project_id: String`

  The ID of the project to get permissions for.

##### Returns

- `class PermissionListResponse`

  The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

  - `id: String`

    The permission identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the permission was created.

  - `object: :"checkpoint.permission"`

    The object type, which is always "checkpoint.permission".

    - `:"checkpoint.permission"`

  - `project_id: String`

    The project identifier that the permission is for.

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.fine_tuning.checkpoints.permissions.list("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(page)
```

#### Create

`fine_tuning.checkpoints.permissions.create(fine_tuned_model_checkpoint, **kwargs) -> Page<PermissionCreateResponse>`

**post** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### Parameters

- `fine_tuned_model_checkpoint: String`

- `project_ids: Array[String]`

  The project identifiers to grant access to.

##### Returns

- `class PermissionCreateResponse`

  The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

  - `id: String`

    The permission identifier, which can be referenced in the API endpoints.

  - `created_at: Integer`

    The Unix timestamp (in seconds) for when the permission was created.

  - `object: :"checkpoint.permission"`

    The object type, which is always "checkpoint.permission".

    - `:"checkpoint.permission"`

  - `project_id: String`

    The project identifier that the permission is for.

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.fine_tuning.checkpoints.permissions.create(
  "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
  project_ids: ["string"]
)

puts(page)
```

#### Delete

`fine_tuning.checkpoints.permissions.delete(permission_id, **kwargs) -> PermissionDeleteResponse`

**delete** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### Parameters

- `fine_tuned_model_checkpoint: String`

- `permission_id: String`

##### Returns

- `class PermissionDeleteResponse`

  - `id: String`

    The ID of the fine-tuned model checkpoint permission that was deleted.

  - `deleted: bool`

    Whether the fine-tuned model checkpoint permission was successfully deleted.

  - `object: :"checkpoint.permission"`

    The object type, which is always "checkpoint.permission".

    - `:"checkpoint.permission"`

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

permission = openai.fine_tuning.checkpoints.permissions.delete(
  "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  fine_tuned_model_checkpoint: "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd"
)

puts(permission)
```

## Alpha

### Graders

#### Run

`fine_tuning.alpha.graders.run(**kwargs) -> GraderRunResponse`

**post** `/fine_tuning/alpha/graders/run`

Run a grader.

##### Parameters

- `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

  The grader used for the fine-tuning job.

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

  - `class TextSimilarityGrader`

    A TextSimilarityGrader object which grades text based on similarity metrics.

    - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

      The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
      `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
      or `rouge_l`.

      - `:cosine`

      - `:fuzzy_match`

      - `:bleu`

      - `:gleu`

      - `:meteor`

      - `:rouge_1`

      - `:rouge_2`

      - `:rouge_3`

      - `:rouge_4`

      - `:rouge_5`

      - `:rouge_l`

    - `input: String`

      The text being graded.

    - `name: String`

      The name of the grader.

    - `reference: String`

      The text being graded against.

    - `type: :text_similarity`

      The type of grader.

      - `:text_similarity`

  - `class PythonGrader`

    A PythonGrader object that runs a python script on the input.

    - `name: String`

      The name of the grader.

    - `source: String`

      The source code of the python script.

    - `type: :python`

      The object type, which is always `python`.

      - `:python`

    - `image_tag: String`

      The image tag to use for the python script.

  - `class ScoreModelGrader`

    A ScoreModelGrader object that uses a model to assign a score to the input.

    - `input: Array[{ content, role, type}]`

      The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

    - `model: String`

      The model to use for the evaluation.

    - `name: String`

      The name of the grader.

    - `type: :score_model`

      The object type, which is always `score_model`.

      - `:score_model`

    - `range: Array[Float]`

      The range of the score. Defaults to `[0, 1]`.

    - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

      The sampling parameters for the model.

      - `max_completions_tokens: Integer`

        The maximum number of tokens the grader model may generate in its response.

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

      - `top_p: Float`

        An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `class MultiGrader`

    A MultiGrader object combines the output of multiple graders to produce a single score.

    - `calculate_output: String`

      A formula to calculate the output based on grader results.

    - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

      - `class TextSimilarityGrader`

        A TextSimilarityGrader object which grades text based on similarity metrics.

        - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

          The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
          `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
          or `rouge_l`.

          - `:cosine`

          - `:fuzzy_match`

          - `:bleu`

          - `:gleu`

          - `:meteor`

          - `:rouge_1`

          - `:rouge_2`

          - `:rouge_3`

          - `:rouge_4`

          - `:rouge_5`

          - `:rouge_l`

        - `input: String`

          The text being graded.

        - `name: String`

          The name of the grader.

        - `reference: String`

          The text being graded against.

        - `type: :text_similarity`

          The type of grader.

          - `:text_similarity`

      - `class PythonGrader`

        A PythonGrader object that runs a python script on the input.

        - `name: String`

          The name of the grader.

        - `source: String`

          The source code of the python script.

        - `type: :python`

          The object type, which is always `python`.

          - `:python`

        - `image_tag: String`

          The image tag to use for the python script.

      - `class ScoreModelGrader`

        A ScoreModelGrader object that uses a model to assign a score to the input.

        - `input: Array[{ content, role, type}]`

          The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

        - `model: String`

          The model to use for the evaluation.

        - `name: String`

          The name of the grader.

        - `type: :score_model`

          The object type, which is always `score_model`.

          - `:score_model`

        - `range: Array[Float]`

          The range of the score. Defaults to `[0, 1]`.

        - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

          The sampling parameters for the model.

          - `max_completions_tokens: Integer`

            The maximum number of tokens the grader model may generate in its response.

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

          - `top_p: Float`

            An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

    - `name: String`

      The name of the grader.

    - `type: :multi`

      The object type, which is always `multi`.

      - `:multi`

- `model_sample: String`

  The model sample to be evaluated. This value will be used to populate
  the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
  The `output_json` variable will be populated if the model sample is a
  valid JSON string.

- `item: untyped`

  The dataset item provided to the grader. This will be used to populate
  the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.

##### Returns

- `class GraderRunResponse`

  - `metadata: { errors, execution_time, name, 4 more}`

    - `errors: { formula_parse_error, invalid_variable_error, model_grader_parse_error, 11 more}`

      - `formula_parse_error: bool`

      - `invalid_variable_error: bool`

      - `model_grader_parse_error: bool`

      - `model_grader_refusal_error: bool`

      - `model_grader_server_error: bool`

      - `model_grader_server_error_details: String`

      - `other_error: bool`

      - `python_grader_runtime_error: bool`

      - `python_grader_runtime_error_details: String`

      - `python_grader_server_error: bool`

      - `python_grader_server_error_type: String`

      - `sample_parse_error: bool`

      - `truncated_observation_error: bool`

      - `unresponsive_reward_error: bool`

    - `execution_time: Float`

    - `name: String`

    - `sampled_model_name: String`

    - `scores: Hash[Symbol, untyped]`

    - `token_usage: Integer`

    - `type: String`

  - `model_grader_token_usage_per_model: Hash[Symbol, untyped]`

  - `reward: Float`

  - `sub_rewards: Hash[Symbol, untyped]`

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.fine_tuning.alpha.graders.run(
  grader: {input: "input", name: "name", operation: :eq, reference: "reference", type: :string_check},
  model_sample: "model_sample"
)

puts(response)
```

#### Validate

`fine_tuning.alpha.graders.validate(**kwargs) -> GraderValidateResponse`

**post** `/fine_tuning/alpha/graders/validate`

Validate a grader.

##### Parameters

- `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

  The grader used for the fine-tuning job.

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

  - `class TextSimilarityGrader`

    A TextSimilarityGrader object which grades text based on similarity metrics.

    - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

      The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
      `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
      or `rouge_l`.

      - `:cosine`

      - `:fuzzy_match`

      - `:bleu`

      - `:gleu`

      - `:meteor`

      - `:rouge_1`

      - `:rouge_2`

      - `:rouge_3`

      - `:rouge_4`

      - `:rouge_5`

      - `:rouge_l`

    - `input: String`

      The text being graded.

    - `name: String`

      The name of the grader.

    - `reference: String`

      The text being graded against.

    - `type: :text_similarity`

      The type of grader.

      - `:text_similarity`

  - `class PythonGrader`

    A PythonGrader object that runs a python script on the input.

    - `name: String`

      The name of the grader.

    - `source: String`

      The source code of the python script.

    - `type: :python`

      The object type, which is always `python`.

      - `:python`

    - `image_tag: String`

      The image tag to use for the python script.

  - `class ScoreModelGrader`

    A ScoreModelGrader object that uses a model to assign a score to the input.

    - `input: Array[{ content, role, type}]`

      The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

    - `model: String`

      The model to use for the evaluation.

    - `name: String`

      The name of the grader.

    - `type: :score_model`

      The object type, which is always `score_model`.

      - `:score_model`

    - `range: Array[Float]`

      The range of the score. Defaults to `[0, 1]`.

    - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

      The sampling parameters for the model.

      - `max_completions_tokens: Integer`

        The maximum number of tokens the grader model may generate in its response.

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

      - `top_p: Float`

        An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

  - `class MultiGrader`

    A MultiGrader object combines the output of multiple graders to produce a single score.

    - `calculate_output: String`

      A formula to calculate the output based on grader results.

    - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

      - `class TextSimilarityGrader`

        A TextSimilarityGrader object which grades text based on similarity metrics.

        - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

          The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
          `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
          or `rouge_l`.

          - `:cosine`

          - `:fuzzy_match`

          - `:bleu`

          - `:gleu`

          - `:meteor`

          - `:rouge_1`

          - `:rouge_2`

          - `:rouge_3`

          - `:rouge_4`

          - `:rouge_5`

          - `:rouge_l`

        - `input: String`

          The text being graded.

        - `name: String`

          The name of the grader.

        - `reference: String`

          The text being graded against.

        - `type: :text_similarity`

          The type of grader.

          - `:text_similarity`

      - `class PythonGrader`

        A PythonGrader object that runs a python script on the input.

        - `name: String`

          The name of the grader.

        - `source: String`

          The source code of the python script.

        - `type: :python`

          The object type, which is always `python`.

          - `:python`

        - `image_tag: String`

          The image tag to use for the python script.

      - `class ScoreModelGrader`

        A ScoreModelGrader object that uses a model to assign a score to the input.

        - `input: Array[{ content, role, type}]`

          The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

        - `model: String`

          The model to use for the evaluation.

        - `name: String`

          The name of the grader.

        - `type: :score_model`

          The object type, which is always `score_model`.

          - `:score_model`

        - `range: Array[Float]`

          The range of the score. Defaults to `[0, 1]`.

        - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

          The sampling parameters for the model.

          - `max_completions_tokens: Integer`

            The maximum number of tokens the grader model may generate in its response.

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

          - `top_p: Float`

            An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

    - `name: String`

      The name of the grader.

    - `type: :multi`

      The object type, which is always `multi`.

      - `:multi`

##### Returns

- `class GraderValidateResponse`

  - `grader: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

    The grader used for the fine-tuning job.

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

    - `class TextSimilarityGrader`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `:cosine`

        - `:fuzzy_match`

        - `:bleu`

        - `:gleu`

        - `:meteor`

        - `:rouge_1`

        - `:rouge_2`

        - `:rouge_3`

        - `:rouge_4`

        - `:rouge_5`

        - `:rouge_l`

      - `input: String`

        The text being graded.

      - `name: String`

        The name of the grader.

      - `reference: String`

        The text being graded against.

      - `type: :text_similarity`

        The type of grader.

        - `:text_similarity`

    - `class PythonGrader`

      A PythonGrader object that runs a python script on the input.

      - `name: String`

        The name of the grader.

      - `source: String`

        The source code of the python script.

      - `type: :python`

        The object type, which is always `python`.

        - `:python`

      - `image_tag: String`

        The image tag to use for the python script.

    - `class ScoreModelGrader`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `input: Array[{ content, role, type}]`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

      - `model: String`

        The model to use for the evaluation.

      - `name: String`

        The name of the grader.

      - `type: :score_model`

        The object type, which is always `score_model`.

        - `:score_model`

      - `range: Array[Float]`

        The range of the score. Defaults to `[0, 1]`.

      - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

        The sampling parameters for the model.

        - `max_completions_tokens: Integer`

          The maximum number of tokens the grader model may generate in its response.

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

        - `top_p: Float`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `class MultiGrader`

      A MultiGrader object combines the output of multiple graders to produce a single score.

      - `calculate_output: String`

        A formula to calculate the output based on grader results.

      - `graders: StringCheckGrader | TextSimilarityGrader | PythonGrader | 2 more`

        A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

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

        - `class TextSimilarityGrader`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `evaluation_metric: :cosine | :fuzzy_match | :bleu | 8 more`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `:cosine`

            - `:fuzzy_match`

            - `:bleu`

            - `:gleu`

            - `:meteor`

            - `:rouge_1`

            - `:rouge_2`

            - `:rouge_3`

            - `:rouge_4`

            - `:rouge_5`

            - `:rouge_l`

          - `input: String`

            The text being graded.

          - `name: String`

            The name of the grader.

          - `reference: String`

            The text being graded against.

          - `type: :text_similarity`

            The type of grader.

            - `:text_similarity`

        - `class PythonGrader`

          A PythonGrader object that runs a python script on the input.

          - `name: String`

            The name of the grader.

          - `source: String`

            The source code of the python script.

          - `type: :python`

            The object type, which is always `python`.

            - `:python`

          - `image_tag: String`

            The image tag to use for the python script.

        - `class ScoreModelGrader`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `input: Array[{ content, role, type}]`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

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

          - `model: String`

            The model to use for the evaluation.

          - `name: String`

            The name of the grader.

          - `type: :score_model`

            The object type, which is always `score_model`.

            - `:score_model`

          - `range: Array[Float]`

            The range of the score. Defaults to `[0, 1]`.

          - `sampling_params: { max_completions_tokens, reasoning_effort, seed, 2 more}`

            The sampling parameters for the model.

            - `max_completions_tokens: Integer`

              The maximum number of tokens the grader model may generate in its response.

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

            - `top_p: Float`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

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

      - `name: String`

        The name of the grader.

      - `type: :multi`

        The object type, which is always `multi`.

        - `:multi`

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.fine_tuning.alpha.graders.validate(
  grader: {input: "input", name: "name", operation: :eq, reference: "reference", type: :string_check}
)

puts(response)
```
