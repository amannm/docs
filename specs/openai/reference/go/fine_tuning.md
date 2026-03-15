# Fine Tuning

## Methods

### Domain Types

### Dpo Hyperparameters

- `type DpoHyperparametersResp struct{…}`

  The hyperparameters used for the DPO fine-tuning job.

  - `BatchSize DpoHyperparametersBatchSizeUnionResp`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

  - `Beta DpoHyperparametersBetaUnionResp`

    The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `float64`

  - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `float64`

  - `NEpochs DpoHyperparametersNEpochsUnionResp`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

### Dpo Method

- `type DpoMethod struct{…}`

  Configuration for the DPO fine-tuning method.

  - `Hyperparameters DpoHyperparametersResp`

    The hyperparameters used for the DPO fine-tuning job.

    - `BatchSize DpoHyperparametersBatchSizeUnionResp`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `Beta DpoHyperparametersBetaUnionResp`

      The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs DpoHyperparametersNEpochsUnionResp`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

### Reinforcement Hyperparameters

- `type ReinforcementHyperparametersResp struct{…}`

  The hyperparameters used for the reinforcement fine-tuning job.

  - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

  - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

    Multiplier on amount of compute used for exploring search space during training.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `float64`

  - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

    The number of training steps between evaluation runs.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

  - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

    Number of evaluation samples to generate per training step.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

  - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `float64`

  - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

  - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

    Level of reasoning effort.

    - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

    - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

    - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

    - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

### Reinforcement Method

- `type ReinforcementMethod struct{…}`

  Configuration for the reinforcement fine-tuning method.

  - `Grader ReinforcementMethodGraderUnion`

    The grader used for the fine-tuning job.

    - `type StringCheckGrader struct{…}`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `Input string`

        The input text. This may include template strings.

      - `Name string`

        The name of the grader.

      - `Operation StringCheckGraderOperation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

        - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

        - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

        - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

      - `Reference string`

        The reference text. This may include template strings.

      - `Type StringCheck`

        The object type, which is always `string_check`.

        - `const StringCheckStringCheck StringCheck = "string_check"`

    - `type TextSimilarityGrader struct{…}`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

        - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

        - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

        - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

        - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

        - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

        - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

        - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

        - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

        - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

        - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

      - `Input string`

        The text being graded.

      - `Name string`

        The name of the grader.

      - `Reference string`

        The text being graded against.

      - `Type TextSimilarity`

        The type of grader.

        - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

    - `type PythonGrader struct{…}`

      A PythonGrader object that runs a python script on the input.

      - `Name string`

        The name of the grader.

      - `Source string`

        The source code of the python script.

      - `Type Python`

        The object type, which is always `python`.

        - `const PythonPython Python = "python"`

      - `ImageTag string`

        The image tag to use for the python script.

    - `type ScoreModelGrader struct{…}`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Input []ScoreModelGraderInput`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

        - `Content ScoreModelGraderInputContentUnion`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `string`

          - `type ResponseInputText struct{…}`

            A text input to the model.

            - `Text string`

              The text input to the model.

            - `Type InputText`

              The type of the input item. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type ScoreModelGraderInputContentOutputText struct{…}`

            A text output from the model.

            - `Text string`

              The text output from the model.

            - `Type OutputText`

              The type of the output text. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

          - `type ScoreModelGraderInputContentInputImage struct{…}`

            An image input block used within EvalItem content arrays.

            - `ImageURL string`

              The URL of the image input.

            - `Type InputImage`

              The type of the image input. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

            - `Detail string`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `type ResponseInputAudio struct{…}`

            An audio input to the model.

            - `InputAudio ResponseInputAudioInputAudio`

              - `Data string`

                Base64-encoded audio data.

              - `Format string`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

            - `Type InputAudio`

              The type of the input item. Always `input_audio`.

              - `const InputAudioInputAudio InputAudio = "input_audio"`

          - `type GraderInputs []GraderInputUnion`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `string`

            - `type ResponseInputText struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type GraderInputOutputText struct{…}`

              A text output from the model.

              - `Text string`

                The text output from the model.

              - `Type OutputText`

                The type of the output text. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

            - `type GraderInputInputImage struct{…}`

              An image input block used within EvalItem content arrays.

              - `ImageURL string`

                The URL of the image input.

              - `Type InputImage`

                The type of the image input. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail string`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `type ResponseInputAudio struct{…}`

              An audio input to the model.

              - `InputAudio ResponseInputAudioInputAudio`

                - `Data string`

                  Base64-encoded audio data.

                - `Format string`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                  - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

              - `Type InputAudio`

                The type of the input item. Always `input_audio`.

                - `const InputAudioInputAudio InputAudio = "input_audio"`

        - `Role string`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

          - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

          - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

          - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

        - `Type string`

          The type of the message input. Always `message`.

          - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

      - `Model string`

        The model to use for the evaluation.

      - `Name string`

        The name of the grader.

      - `Type ScoreModel`

        The object type, which is always `score_model`.

        - `const ScoreModelScoreModel ScoreModel = "score_model"`

      - `Range []float64`

        The range of the score. Defaults to `[0, 1]`.

      - `SamplingParams ScoreModelGraderSamplingParams`

        The sampling parameters for the model.

        - `MaxCompletionsTokens int64`

          The maximum number of tokens the grader model may generate in its response.

        - `ReasoningEffort ReasoningEffort`

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

        - `Seed int64`

          A seed value to initialize the randomness, during sampling.

        - `Temperature float64`

          A higher temperature increases randomness in the outputs.

        - `TopP float64`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `type MultiGrader struct{…}`

      A MultiGrader object combines the output of multiple graders to produce a single score.

      - `CalculateOutput string`

        A formula to calculate the output based on grader results.

      - `Graders MultiGraderGradersUnion`

        A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type LabelModelGrader struct{…}`

          A LabelModelGrader object which uses a model to assign labels to each item
          in the evaluation.

          - `Input []LabelModelGraderInput`

            - `Content LabelModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type LabelModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type LabelModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

              - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

              - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

              - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

          - `Labels []string`

            The labels to assign to each item in the evaluation.

          - `Model string`

            The model to use for the evaluation. Must support structured outputs.

          - `Name string`

            The name of the grader.

          - `PassingLabels []string`

            The labels that indicate a passing result. Must be a subset of labels.

          - `Type LabelModel`

            The object type, which is always `label_model`.

            - `const LabelModelLabelModel LabelModel = "label_model"`

      - `Name string`

        The name of the grader.

      - `Type Multi`

        The object type, which is always `multi`.

        - `const MultiMulti Multi = "multi"`

  - `Hyperparameters ReinforcementHyperparametersResp`

    The hyperparameters used for the reinforcement fine-tuning job.

    - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

      Multiplier on amount of compute used for exploring search space during training.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

      The number of training steps between evaluation runs.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

      Number of evaluation samples to generate per training step.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

      Level of reasoning effort.

      - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

      - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

      - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

      - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

### Supervised Hyperparameters

- `type SupervisedHyperparametersResp struct{…}`

  The hyperparameters used for the fine-tuning job.

  - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

    Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

  - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `float64`

  - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

    - `type Auto string`

      - `const AutoAuto Auto = "auto"`

    - `int64`

### Supervised Method

- `type SupervisedMethod struct{…}`

  Configuration for the supervised fine-tuning method.

  - `Hyperparameters SupervisedHyperparametersResp`

    The hyperparameters used for the fine-tuning job.

    - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

      Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

      The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

## Jobs

### Create

`client.FineTuning.Jobs.New(ctx, body) (*FineTuningJob, error)`

**post** `/fine_tuning/jobs`

Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

#### Parameters

- `body FineTuningJobNewParams`

  - `Model param.Field[FineTuningJobNewParamsModel]`

    The name of the model to fine-tune. You can select one of the
    [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

    - `string`

    - `type FineTuningJobNewParamsModel string`

      The name of the model to fine-tune. You can select one of the
      [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

      - `const FineTuningJobNewParamsModelBabbage002 FineTuningJobNewParamsModel = "babbage-002"`

      - `const FineTuningJobNewParamsModelDavinci002 FineTuningJobNewParamsModel = "davinci-002"`

      - `const FineTuningJobNewParamsModelGPT3_5Turbo FineTuningJobNewParamsModel = "gpt-3.5-turbo"`

      - `const FineTuningJobNewParamsModelGPT4oMini FineTuningJobNewParamsModel = "gpt-4o-mini"`

  - `TrainingFile param.Field[string]`

    The ID of an uploaded file that contains training data.

    See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.

    Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

    The contents of the file should differ depending on if the model uses the [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input), [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) format, or if the fine-tuning method uses the [preference](https://platform.openai.com/docs/api-reference/fine-tuning/preference-input) format.

    See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.

  - `Hyperparameters param.Field[FineTuningJobNewParamsHyperparameters]`

    The hyperparameters used for the fine-tuning job.
    This value is now deprecated in favor of `method`, and should be passed in under the `method` parameter.

    - `BatchSize FineTuningJobNewParamsHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobNewParamsHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobNewParamsHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Integrations param.Field[[]FineTuningJobNewParamsIntegration]`

    A list of integrations to enable for your fine-tuning job.

    - `Type Wandb`

      The type of integration to enable. Currently, only "wandb" (Weights and Biases) is supported.

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobNewParamsIntegrationWandb`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata param.Field[Metadata]`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method param.Field[FineTuningJobNewParamsMethod]`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobNewParamsMethodTypeSupervised FineTuningJobNewParamsMethodType = "supervised"`

      - `const FineTuningJobNewParamsMethodTypeDpo FineTuningJobNewParamsMethodType = "dpo"`

      - `const FineTuningJobNewParamsMethodTypeReinforcement FineTuningJobNewParamsMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

  - `Seed param.Field[int64]`

    The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases.
    If a seed is not specified, one will be generated for you.

  - `Suffix param.Field[string]`

    A string of up to 64 characters that will be added to your fine-tuned model name.

    For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

  - `ValidationFile param.Field[string]`

    The ID of an uploaded file that contains validation data.

    If you provide this file, the data is used to generate validation
    metrics periodically during fine-tuning. These metrics can be viewed in
    the fine-tuning results file.
    The same data should not be present in both train and validation files.

    Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

    See the [fine-tuning guide](https://platform.openai.com/docs/guides/model-optimization) for more details.

#### Returns

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  fineTuningJob, err := client.FineTuning.Jobs.New(context.TODO(), openai.FineTuningJobNewParams{
    Model: openai.FineTuningJobNewParamsModelGPT4oMini,
    TrainingFile: "file-abc123",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fineTuningJob.ID)
}
```

### List

`client.FineTuning.Jobs.List(ctx, query) (*CursorPage[FineTuningJob], error)`

**get** `/fine_tuning/jobs`

List your organization's fine-tuning jobs

#### Parameters

- `query FineTuningJobListParams`

  - `After param.Field[string]`

    Identifier for the last job from the previous pagination request.

  - `Limit param.Field[int64]`

    Number of fine-tuning jobs to retrieve.

  - `Metadata param.Field[map[string, string]]`

    Optional metadata filter. To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to indicate no metadata.

#### Returns

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.FineTuning.Jobs.List(context.TODO(), openai.FineTuningJobListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Retrieve

`client.FineTuning.Jobs.Get(ctx, fineTuningJobID) (*FineTuningJob, error)`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}`

Get info about a fine-tuning job.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/model-optimization)

#### Parameters

- `fineTuningJobID string`

#### Returns

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  fineTuningJob, err := client.FineTuning.Jobs.Get(context.TODO(), "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fineTuningJob.ID)
}
```

### List Events

`client.FineTuning.Jobs.ListEvents(ctx, fineTuningJobID, query) (*CursorPage[FineTuningJobEvent], error)`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}/events`

Get status updates for a fine-tuning job.

#### Parameters

- `fineTuningJobID string`

- `query FineTuningJobListEventsParams`

  - `After param.Field[string]`

    Identifier for the last event from the previous pagination request.

  - `Limit param.Field[int64]`

    Number of events to retrieve.

#### Returns

- `type FineTuningJobEvent struct{…}`

  Fine-tuning job event object

  - `ID string`

    The object identifier.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Level FineTuningJobEventLevel`

    The log level of the event.

    - `const FineTuningJobEventLevelInfo FineTuningJobEventLevel = "info"`

    - `const FineTuningJobEventLevelWarn FineTuningJobEventLevel = "warn"`

    - `const FineTuningJobEventLevelError FineTuningJobEventLevel = "error"`

  - `Message string`

    The message of the event.

  - `Object FineTuningJobEvent`

    The object type, which is always "fine_tuning.job.event".

    - `const FineTuningJobEventFineTuningJobEvent FineTuningJobEvent = "fine_tuning.job.event"`

  - `Data any`

    The data associated with the event.

  - `Type FineTuningJobEventType`

    The type of event.

    - `const FineTuningJobEventTypeMessage FineTuningJobEventType = "message"`

    - `const FineTuningJobEventTypeMetrics FineTuningJobEventType = "metrics"`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.FineTuning.Jobs.ListEvents(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningJobListEventsParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Cancel

`client.FineTuning.Jobs.Cancel(ctx, fineTuningJobID) (*FineTuningJob, error)`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/cancel`

Immediately cancel a fine-tune job.

#### Parameters

- `fineTuningJobID string`

#### Returns

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  fineTuningJob, err := client.FineTuning.Jobs.Cancel(context.TODO(), "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fineTuningJob.ID)
}
```

### Pause

`client.FineTuning.Jobs.Pause(ctx, fineTuningJobID) (*FineTuningJob, error)`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/pause`

Pause a fine-tune job.

#### Parameters

- `fineTuningJobID string`

#### Returns

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  fineTuningJob, err := client.FineTuning.Jobs.Pause(context.TODO(), "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fineTuningJob.ID)
}
```

### Resume

`client.FineTuning.Jobs.Resume(ctx, fineTuningJobID) (*FineTuningJob, error)`

**post** `/fine_tuning/jobs/{fine_tuning_job_id}/resume`

Resume a fine-tune job.

#### Parameters

- `fineTuningJobID string`

#### Returns

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  fineTuningJob, err := client.FineTuning.Jobs.Resume(context.TODO(), "ft-AF1WoRqd3aJAHsqc9NY7iL8F")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fineTuningJob.ID)
}
```

#### Domain Types

#### Fine Tuning Job

- `type FineTuningJob struct{…}`

  The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

  - `ID string`

    The object identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Error FineTuningJobError`

    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Param string`

      The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

  - `FineTunedModel string`

    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

  - `FinishedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

  - `Hyperparameters FineTuningJobHyperparameters`

    The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

    - `BatchSize FineTuningJobHyperparametersBatchSizeUnion`

      Number of examples in each batch. A larger batch size means that model parameters
      are updated less frequently, but with lower variance.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

    - `LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnion`

      Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
      overfitting.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `float64`

    - `NEpochs FineTuningJobHyperparametersNEpochsUnion`

      The number of epochs to train the model for. An epoch refers to one full cycle
      through the training dataset.

      - `type Auto string`

        - `const AutoAuto Auto = "auto"`

      - `int64`

  - `Model string`

    The base model that is being fine-tuned.

  - `Object FineTuningJob`

    The object type, which is always "fine_tuning.job".

    - `const FineTuningJobFineTuningJob FineTuningJob = "fine_tuning.job"`

  - `OrganizationID string`

    The organization that owns the fine-tuning job.

  - `ResultFiles []string`

    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `Seed int64`

    The seed used for the fine-tuning job.

  - `Status FineTuningJobStatus`

    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

    - `const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating_files"`

    - `const FineTuningJobStatusQueued FineTuningJobStatus = "queued"`

    - `const FineTuningJobStatusRunning FineTuningJobStatus = "running"`

    - `const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"`

    - `const FineTuningJobStatusFailed FineTuningJobStatus = "failed"`

    - `const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"`

  - `TrainedTokens int64`

    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

  - `TrainingFile string`

    The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `ValidationFile string`

    The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

  - `EstimatedFinish int64`

    The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

  - `Integrations []FineTuningJobWandbIntegrationObject`

    A list of integrations to enable for this fine-tuning job.

    - `Type Wandb`

      The type of the integration being enabled for the fine-tuning job

      - `const WandbWandb Wandb = "wandb"`

    - `Wandb FineTuningJobWandbIntegration`

      The settings for your integration with Weights and Biases. This payload specifies the project that
      metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
      to your run, and set a default entity (team, username, etc) to be associated with your run.

      - `Project string`

        The name of the project that the new run will be created under.

      - `Entity string`

        The entity to use for the run. This allows you to set the team or username of the WandB user that you would
        like associated with the run. If not set, the default entity for the registered WandB API key is used.

      - `Name string`

        A display name to set for the run. If not set, we will use the Job ID as the name.

      - `Tags []string`

        A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
        default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

  - `Metadata Metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Method FineTuningJobMethod`

    The method used for fine-tuning.

    - `Type string`

      The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

      - `const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"`

      - `const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"`

      - `const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"`

    - `Dpo DpoMethod`

      Configuration for the DPO fine-tuning method.

      - `Hyperparameters DpoHyperparametersResp`

        The hyperparameters used for the DPO fine-tuning job.

        - `BatchSize DpoHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `Beta DpoHyperparametersBetaUnionResp`

          The beta value for the DPO method. A higher beta value will increase the weight of the penalty between the policy and reference model.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `LearningRateMultiplier DpoHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs DpoHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

    - `Reinforcement ReinforcementMethod`

      Configuration for the reinforcement fine-tuning method.

      - `Grader ReinforcementMethodGraderUnion`

        The grader used for the fine-tuning job.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type MultiGrader struct{…}`

          A MultiGrader object combines the output of multiple graders to produce a single score.

          - `CalculateOutput string`

            A formula to calculate the output based on grader results.

          - `Graders MultiGraderGradersUnion`

            A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

            - `type StringCheckGrader struct{…}`

              A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

              - `Input string`

                The input text. This may include template strings.

              - `Name string`

                The name of the grader.

              - `Operation StringCheckGraderOperation`

                The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

                - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

                - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

                - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

                - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

              - `Reference string`

                The reference text. This may include template strings.

              - `Type StringCheck`

                The object type, which is always `string_check`.

                - `const StringCheckStringCheck StringCheck = "string_check"`

            - `type TextSimilarityGrader struct{…}`

              A TextSimilarityGrader object which grades text based on similarity metrics.

              - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

                The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
                `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
                or `rouge_l`.

                - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

                - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

                - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

                - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

                - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

                - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

                - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

                - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

                - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

                - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

                - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

              - `Input string`

                The text being graded.

              - `Name string`

                The name of the grader.

              - `Reference string`

                The text being graded against.

              - `Type TextSimilarity`

                The type of grader.

                - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

            - `type PythonGrader struct{…}`

              A PythonGrader object that runs a python script on the input.

              - `Name string`

                The name of the grader.

              - `Source string`

                The source code of the python script.

              - `Type Python`

                The object type, which is always `python`.

                - `const PythonPython Python = "python"`

              - `ImageTag string`

                The image tag to use for the python script.

            - `type ScoreModelGrader struct{…}`

              A ScoreModelGrader object that uses a model to assign a score to the input.

              - `Input []ScoreModelGraderInput`

                The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

                - `Content ScoreModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type ScoreModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type ScoreModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

                  - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

                  - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

                  - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

              - `Model string`

                The model to use for the evaluation.

              - `Name string`

                The name of the grader.

              - `Type ScoreModel`

                The object type, which is always `score_model`.

                - `const ScoreModelScoreModel ScoreModel = "score_model"`

              - `Range []float64`

                The range of the score. Defaults to `[0, 1]`.

              - `SamplingParams ScoreModelGraderSamplingParams`

                The sampling parameters for the model.

                - `MaxCompletionsTokens int64`

                  The maximum number of tokens the grader model may generate in its response.

                - `ReasoningEffort ReasoningEffort`

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

                - `Seed int64`

                  A seed value to initialize the randomness, during sampling.

                - `Temperature float64`

                  A higher temperature increases randomness in the outputs.

                - `TopP float64`

                  An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

            - `type LabelModelGrader struct{…}`

              A LabelModelGrader object which uses a model to assign labels to each item
              in the evaluation.

              - `Input []LabelModelGraderInput`

                - `Content LabelModelGraderInputContentUnion`

                  Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

                  - `string`

                  - `type ResponseInputText struct{…}`

                    A text input to the model.

                    - `Text string`

                      The text input to the model.

                    - `Type InputText`

                      The type of the input item. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type LabelModelGraderInputContentOutputText struct{…}`

                    A text output from the model.

                    - `Text string`

                      The text output from the model.

                    - `Type OutputText`

                      The type of the output text. Always `output_text`.

                      - `const OutputTextOutputText OutputText = "output_text"`

                  - `type LabelModelGraderInputContentInputImage struct{…}`

                    An image input block used within EvalItem content arrays.

                    - `ImageURL string`

                      The URL of the image input.

                    - `Type InputImage`

                      The type of the image input. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                    - `Detail string`

                      The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                  - `type ResponseInputAudio struct{…}`

                    An audio input to the model.

                    - `InputAudio ResponseInputAudioInputAudio`

                      - `Data string`

                        Base64-encoded audio data.

                      - `Format string`

                        The format of the audio data. Currently supported formats are `mp3` and
                        `wav`.

                        - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                        - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                    - `Type InputAudio`

                      The type of the input item. Always `input_audio`.

                      - `const InputAudioInputAudio InputAudio = "input_audio"`

                  - `type GraderInputs []GraderInputUnion`

                    A list of inputs, each of which may be either an input text, output text, input
                    image, or input audio object.

                    - `string`

                    - `type ResponseInputText struct{…}`

                      A text input to the model.

                      - `Text string`

                        The text input to the model.

                      - `Type InputText`

                        The type of the input item. Always `input_text`.

                        - `const InputTextInputText InputText = "input_text"`

                    - `type GraderInputOutputText struct{…}`

                      A text output from the model.

                      - `Text string`

                        The text output from the model.

                      - `Type OutputText`

                        The type of the output text. Always `output_text`.

                        - `const OutputTextOutputText OutputText = "output_text"`

                    - `type GraderInputInputImage struct{…}`

                      An image input block used within EvalItem content arrays.

                      - `ImageURL string`

                        The URL of the image input.

                      - `Type InputImage`

                        The type of the image input. Always `input_image`.

                        - `const InputImageInputImage InputImage = "input_image"`

                      - `Detail string`

                        The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                    - `type ResponseInputAudio struct{…}`

                      An audio input to the model.

                      - `InputAudio ResponseInputAudioInputAudio`

                        - `Data string`

                          Base64-encoded audio data.

                        - `Format string`

                          The format of the audio data. Currently supported formats are `mp3` and
                          `wav`.

                          - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                          - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                      - `Type InputAudio`

                        The type of the input item. Always `input_audio`.

                        - `const InputAudioInputAudio InputAudio = "input_audio"`

                - `Role string`

                  The role of the message input. One of `user`, `assistant`, `system`, or
                  `developer`.

                  - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

                  - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

                  - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

                  - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

                - `Type string`

                  The type of the message input. Always `message`.

                  - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

              - `Labels []string`

                The labels to assign to each item in the evaluation.

              - `Model string`

                The model to use for the evaluation. Must support structured outputs.

              - `Name string`

                The name of the grader.

              - `PassingLabels []string`

                The labels that indicate a passing result. Must be a subset of labels.

              - `Type LabelModel`

                The object type, which is always `label_model`.

                - `const LabelModelLabelModel LabelModel = "label_model"`

          - `Name string`

            The name of the grader.

          - `Type Multi`

            The object type, which is always `multi`.

            - `const MultiMulti Multi = "multi"`

      - `Hyperparameters ReinforcementHyperparametersResp`

        The hyperparameters used for the reinforcement fine-tuning job.

        - `BatchSize ReinforcementHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ComputeMultiplier ReinforcementHyperparametersComputeMultiplierUnionResp`

          Multiplier on amount of compute used for exploring search space during training.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `EvalInterval ReinforcementHyperparametersEvalIntervalUnionResp`

          The number of training steps between evaluation runs.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `EvalSamples ReinforcementHyperparametersEvalSamplesUnionResp`

          Number of evaluation samples to generate per training step.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier ReinforcementHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs ReinforcementHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `ReasoningEffort ReinforcementHyperparametersReasoningEffort`

          Level of reasoning effort.

          - `const ReinforcementHyperparametersReasoningEffortDefault ReinforcementHyperparametersReasoningEffort = "default"`

          - `const ReinforcementHyperparametersReasoningEffortLow ReinforcementHyperparametersReasoningEffort = "low"`

          - `const ReinforcementHyperparametersReasoningEffortMedium ReinforcementHyperparametersReasoningEffort = "medium"`

          - `const ReinforcementHyperparametersReasoningEffortHigh ReinforcementHyperparametersReasoningEffort = "high"`

    - `Supervised SupervisedMethod`

      Configuration for the supervised fine-tuning method.

      - `Hyperparameters SupervisedHyperparametersResp`

        The hyperparameters used for the fine-tuning job.

        - `BatchSize SupervisedHyperparametersBatchSizeUnionResp`

          Number of examples in each batch. A larger batch size means that model parameters are updated less frequently, but with lower variance.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

        - `LearningRateMultiplier SupervisedHyperparametersLearningRateMultiplierUnionResp`

          Scaling factor for the learning rate. A smaller learning rate may be useful to avoid overfitting.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `float64`

        - `NEpochs SupervisedHyperparametersNEpochsUnionResp`

          The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.

          - `type Auto string`

            - `const AutoAuto Auto = "auto"`

          - `int64`

#### Fine Tuning Job Event

- `type FineTuningJobEvent struct{…}`

  Fine-tuning job event object

  - `ID string`

    The object identifier.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the fine-tuning job was created.

  - `Level FineTuningJobEventLevel`

    The log level of the event.

    - `const FineTuningJobEventLevelInfo FineTuningJobEventLevel = "info"`

    - `const FineTuningJobEventLevelWarn FineTuningJobEventLevel = "warn"`

    - `const FineTuningJobEventLevelError FineTuningJobEventLevel = "error"`

  - `Message string`

    The message of the event.

  - `Object FineTuningJobEvent`

    The object type, which is always "fine_tuning.job.event".

    - `const FineTuningJobEventFineTuningJobEvent FineTuningJobEvent = "fine_tuning.job.event"`

  - `Data any`

    The data associated with the event.

  - `Type FineTuningJobEventType`

    The type of event.

    - `const FineTuningJobEventTypeMessage FineTuningJobEventType = "message"`

    - `const FineTuningJobEventTypeMetrics FineTuningJobEventType = "metrics"`

#### Fine Tuning Job Wandb Integration

- `type FineTuningJobWandbIntegration struct{…}`

  The settings for your integration with Weights and Biases. This payload specifies the project that
  metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
  to your run, and set a default entity (team, username, etc) to be associated with your run.

  - `Project string`

    The name of the project that the new run will be created under.

  - `Entity string`

    The entity to use for the run. This allows you to set the team or username of the WandB user that you would
    like associated with the run. If not set, the default entity for the registered WandB API key is used.

  - `Name string`

    A display name to set for the run. If not set, we will use the Job ID as the name.

  - `Tags []string`

    A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
    default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

#### Fine Tuning Job Wandb Integration Object

- `type FineTuningJobWandbIntegrationObject struct{…}`

  - `Type Wandb`

    The type of the integration being enabled for the fine-tuning job

    - `const WandbWandb Wandb = "wandb"`

  - `Wandb FineTuningJobWandbIntegration`

    The settings for your integration with Weights and Biases. This payload specifies the project that
    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
    to your run, and set a default entity (team, username, etc) to be associated with your run.

    - `Project string`

      The name of the project that the new run will be created under.

    - `Entity string`

      The entity to use for the run. This allows you to set the team or username of the WandB user that you would
      like associated with the run. If not set, the default entity for the registered WandB API key is used.

    - `Name string`

      A display name to set for the run. If not set, we will use the Job ID as the name.

    - `Tags []string`

      A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
      default tags are generated by OpenAI: "openai/finetune", "openai/{base-model}", "openai/{ftjob-abcdef}".

### Checkpoints

#### List

`client.FineTuning.Jobs.Checkpoints.List(ctx, fineTuningJobID, query) (*CursorPage[FineTuningJobCheckpoint], error)`

**get** `/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints`

List checkpoints for a fine-tuning job.

##### Parameters

- `fineTuningJobID string`

- `query FineTuningJobCheckpointListParams`

  - `After param.Field[string]`

    Identifier for the last checkpoint ID from the previous pagination request.

  - `Limit param.Field[int64]`

    Number of checkpoints to retrieve.

##### Returns

- `type FineTuningJobCheckpoint struct{…}`

  The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

  - `ID string`

    The checkpoint identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the checkpoint was created.

  - `FineTunedModelCheckpoint string`

    The name of the fine-tuned checkpoint model that is created.

  - `FineTuningJobID string`

    The name of the fine-tuning job that this checkpoint was created from.

  - `Metrics FineTuningJobCheckpointMetrics`

    Metrics at the step number during the fine-tuning job.

    - `FullValidLoss float64`

    - `FullValidMeanTokenAccuracy float64`

    - `Step float64`

    - `TrainLoss float64`

    - `TrainMeanTokenAccuracy float64`

    - `ValidLoss float64`

    - `ValidMeanTokenAccuracy float64`

  - `Object FineTuningJobCheckpoint`

    The object type, which is always "fine_tuning.job.checkpoint".

    - `const FineTuningJobCheckpointFineTuningJobCheckpoint FineTuningJobCheckpoint = "fine_tuning.job.checkpoint"`

  - `StepNumber int64`

    The step number that the checkpoint was created at.

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.FineTuning.Jobs.Checkpoints.List(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningJobCheckpointListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

##### Domain Types

##### Fine Tuning Job Checkpoint

- `type FineTuningJobCheckpoint struct{…}`

  The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

  - `ID string`

    The checkpoint identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the checkpoint was created.

  - `FineTunedModelCheckpoint string`

    The name of the fine-tuned checkpoint model that is created.

  - `FineTuningJobID string`

    The name of the fine-tuning job that this checkpoint was created from.

  - `Metrics FineTuningJobCheckpointMetrics`

    Metrics at the step number during the fine-tuning job.

    - `FullValidLoss float64`

    - `FullValidMeanTokenAccuracy float64`

    - `Step float64`

    - `TrainLoss float64`

    - `TrainMeanTokenAccuracy float64`

    - `ValidLoss float64`

    - `ValidMeanTokenAccuracy float64`

  - `Object FineTuningJobCheckpoint`

    The object type, which is always "fine_tuning.job.checkpoint".

    - `const FineTuningJobCheckpointFineTuningJobCheckpoint FineTuningJobCheckpoint = "fine_tuning.job.checkpoint"`

  - `StepNumber int64`

    The step number that the checkpoint was created at.

## Checkpoints

### Permissions

#### Retrieve

`client.FineTuning.Checkpoints.Permissions.Get(ctx, fineTunedModelCheckpoint, query) (*FineTuningCheckpointPermissionGetResponse, error)`

**get** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### Parameters

- `fineTunedModelCheckpoint string`

- `query FineTuningCheckpointPermissionGetParams`

  - `After param.Field[string]`

    Identifier for the last permission ID from the previous pagination request.

  - `Limit param.Field[int64]`

    Number of permissions to retrieve.

  - `Order param.Field[FineTuningCheckpointPermissionGetParamsOrder]`

    The order in which to retrieve permissions.

    - `const FineTuningCheckpointPermissionGetParamsOrderAscending FineTuningCheckpointPermissionGetParamsOrder = "ascending"`

    - `const FineTuningCheckpointPermissionGetParamsOrderDescending FineTuningCheckpointPermissionGetParamsOrder = "descending"`

  - `ProjectID param.Field[string]`

    The ID of the project to get permissions for.

##### Returns

- `type FineTuningCheckpointPermissionGetResponse struct{…}`

  - `Data []FineTuningCheckpointPermissionGetResponseData`

    - `ID string`

      The permission identifier, which can be referenced in the API endpoints.

    - `CreatedAt int64`

      The Unix timestamp (in seconds) for when the permission was created.

    - `Object CheckpointPermission`

      The object type, which is always "checkpoint.permission".

      - `const CheckpointPermissionCheckpointPermission CheckpointPermission = "checkpoint.permission"`

    - `ProjectID string`

      The project identifier that the permission is for.

  - `HasMore bool`

  - `Object List`

    - `const ListList List = "list"`

  - `FirstID string`

  - `LastID string`

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  permission, err := client.FineTuning.Checkpoints.Permissions.Get(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningCheckpointPermissionGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", permission.FirstID)
}
```

#### List

`client.FineTuning.Checkpoints.Permissions.List(ctx, fineTunedModelCheckpoint, query) (*ConversationCursorPage[FineTuningCheckpointPermissionListResponse], error)`

**get** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to view all permissions for a fine-tuned model checkpoint.

##### Parameters

- `fineTunedModelCheckpoint string`

- `query FineTuningCheckpointPermissionListParams`

  - `After param.Field[string]`

    Identifier for the last permission ID from the previous pagination request.

  - `Limit param.Field[int64]`

    Number of permissions to retrieve.

  - `Order param.Field[FineTuningCheckpointPermissionListParamsOrder]`

    The order in which to retrieve permissions.

    - `const FineTuningCheckpointPermissionListParamsOrderAscending FineTuningCheckpointPermissionListParamsOrder = "ascending"`

    - `const FineTuningCheckpointPermissionListParamsOrderDescending FineTuningCheckpointPermissionListParamsOrder = "descending"`

  - `ProjectID param.Field[string]`

    The ID of the project to get permissions for.

##### Returns

- `type FineTuningCheckpointPermissionListResponse struct{…}`

  The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

  - `ID string`

    The permission identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the permission was created.

  - `Object CheckpointPermission`

    The object type, which is always "checkpoint.permission".

    - `const CheckpointPermissionCheckpointPermission CheckpointPermission = "checkpoint.permission"`

  - `ProjectID string`

    The project identifier that the permission is for.

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.FineTuning.Checkpoints.Permissions.List(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningCheckpointPermissionListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Create

`client.FineTuning.Checkpoints.Permissions.New(ctx, fineTunedModelCheckpoint, body) (*Page[FineTuningCheckpointPermissionNewResponse], error)`

**post** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions`

**NOTE:** Calling this endpoint requires an [admin API key](../admin-api-keys).

This enables organization owners to share fine-tuned models with other projects in their organization.

##### Parameters

- `fineTunedModelCheckpoint string`

- `body FineTuningCheckpointPermissionNewParams`

  - `ProjectIDs param.Field[[]string]`

    The project identifiers to grant access to.

##### Returns

- `type FineTuningCheckpointPermissionNewResponse struct{…}`

  The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.

  - `ID string`

    The permission identifier, which can be referenced in the API endpoints.

  - `CreatedAt int64`

    The Unix timestamp (in seconds) for when the permission was created.

  - `Object CheckpointPermission`

    The object type, which is always "checkpoint.permission".

    - `const CheckpointPermissionCheckpointPermission CheckpointPermission = "checkpoint.permission"`

  - `ProjectID string`

    The project identifier that the permission is for.

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.FineTuning.Checkpoints.Permissions.New(
    context.TODO(),
    "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
    openai.FineTuningCheckpointPermissionNewParams{
      ProjectIDs: []string{"string"},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

#### Delete

`client.FineTuning.Checkpoints.Permissions.Delete(ctx, fineTunedModelCheckpoint, permissionID) (*FineTuningCheckpointPermissionDeleteResponse, error)`

**delete** `/fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}`

**NOTE:** This endpoint requires an [admin API key](../admin-api-keys).

Organization owners can use this endpoint to delete a permission for a fine-tuned model checkpoint.

##### Parameters

- `fineTunedModelCheckpoint string`

- `permissionID string`

##### Returns

- `type FineTuningCheckpointPermissionDeleteResponse struct{…}`

  - `ID string`

    The ID of the fine-tuned model checkpoint permission that was deleted.

  - `Deleted bool`

    Whether the fine-tuned model checkpoint permission was successfully deleted.

  - `Object CheckpointPermission`

    The object type, which is always "checkpoint.permission".

    - `const CheckpointPermissionCheckpointPermission CheckpointPermission = "checkpoint.permission"`

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  permission, err := client.FineTuning.Checkpoints.Permissions.Delete(
    context.TODO(),
    "ft:gpt-4o-mini-2024-07-18:org:weather:B7R9VjQd",
    "cp_zc4Q7MP6XxulcVzj4MZdwsAB",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", permission.ID)
}
```

## Alpha

### Graders

#### Run

`client.FineTuning.Alpha.Graders.Run(ctx, body) (*FineTuningAlphaGraderRunResponse, error)`

**post** `/fine_tuning/alpha/graders/run`

Run a grader.

##### Parameters

- `body FineTuningAlphaGraderRunParams`

  - `Grader param.Field[FineTuningAlphaGraderRunParamsGraderUnion]`

    The grader used for the fine-tuning job.

    - `type StringCheckGrader struct{…}`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `Input string`

        The input text. This may include template strings.

      - `Name string`

        The name of the grader.

      - `Operation StringCheckGraderOperation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

        - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

        - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

        - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

      - `Reference string`

        The reference text. This may include template strings.

      - `Type StringCheck`

        The object type, which is always `string_check`.

        - `const StringCheckStringCheck StringCheck = "string_check"`

    - `type TextSimilarityGrader struct{…}`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

        - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

        - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

        - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

        - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

        - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

        - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

        - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

        - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

        - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

        - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

      - `Input string`

        The text being graded.

      - `Name string`

        The name of the grader.

      - `Reference string`

        The text being graded against.

      - `Type TextSimilarity`

        The type of grader.

        - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

    - `type PythonGrader struct{…}`

      A PythonGrader object that runs a python script on the input.

      - `Name string`

        The name of the grader.

      - `Source string`

        The source code of the python script.

      - `Type Python`

        The object type, which is always `python`.

        - `const PythonPython Python = "python"`

      - `ImageTag string`

        The image tag to use for the python script.

    - `type ScoreModelGrader struct{…}`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Input []ScoreModelGraderInput`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

        - `Content ScoreModelGraderInputContentUnion`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `string`

          - `type ResponseInputText struct{…}`

            A text input to the model.

            - `Text string`

              The text input to the model.

            - `Type InputText`

              The type of the input item. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type ScoreModelGraderInputContentOutputText struct{…}`

            A text output from the model.

            - `Text string`

              The text output from the model.

            - `Type OutputText`

              The type of the output text. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

          - `type ScoreModelGraderInputContentInputImage struct{…}`

            An image input block used within EvalItem content arrays.

            - `ImageURL string`

              The URL of the image input.

            - `Type InputImage`

              The type of the image input. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

            - `Detail string`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `type ResponseInputAudio struct{…}`

            An audio input to the model.

            - `InputAudio ResponseInputAudioInputAudio`

              - `Data string`

                Base64-encoded audio data.

              - `Format string`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

            - `Type InputAudio`

              The type of the input item. Always `input_audio`.

              - `const InputAudioInputAudio InputAudio = "input_audio"`

          - `type GraderInputs []GraderInputUnion`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `string`

            - `type ResponseInputText struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type GraderInputOutputText struct{…}`

              A text output from the model.

              - `Text string`

                The text output from the model.

              - `Type OutputText`

                The type of the output text. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

            - `type GraderInputInputImage struct{…}`

              An image input block used within EvalItem content arrays.

              - `ImageURL string`

                The URL of the image input.

              - `Type InputImage`

                The type of the image input. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail string`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `type ResponseInputAudio struct{…}`

              An audio input to the model.

              - `InputAudio ResponseInputAudioInputAudio`

                - `Data string`

                  Base64-encoded audio data.

                - `Format string`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                  - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

              - `Type InputAudio`

                The type of the input item. Always `input_audio`.

                - `const InputAudioInputAudio InputAudio = "input_audio"`

        - `Role string`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

          - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

          - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

          - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

        - `Type string`

          The type of the message input. Always `message`.

          - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

      - `Model string`

        The model to use for the evaluation.

      - `Name string`

        The name of the grader.

      - `Type ScoreModel`

        The object type, which is always `score_model`.

        - `const ScoreModelScoreModel ScoreModel = "score_model"`

      - `Range []float64`

        The range of the score. Defaults to `[0, 1]`.

      - `SamplingParams ScoreModelGraderSamplingParams`

        The sampling parameters for the model.

        - `MaxCompletionsTokens int64`

          The maximum number of tokens the grader model may generate in its response.

        - `ReasoningEffort ReasoningEffort`

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

        - `Seed int64`

          A seed value to initialize the randomness, during sampling.

        - `Temperature float64`

          A higher temperature increases randomness in the outputs.

        - `TopP float64`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `type MultiGrader struct{…}`

      A MultiGrader object combines the output of multiple graders to produce a single score.

      - `CalculateOutput string`

        A formula to calculate the output based on grader results.

      - `Graders MultiGraderGradersUnion`

        A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type LabelModelGrader struct{…}`

          A LabelModelGrader object which uses a model to assign labels to each item
          in the evaluation.

          - `Input []LabelModelGraderInput`

            - `Content LabelModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type LabelModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type LabelModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

              - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

              - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

              - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

          - `Labels []string`

            The labels to assign to each item in the evaluation.

          - `Model string`

            The model to use for the evaluation. Must support structured outputs.

          - `Name string`

            The name of the grader.

          - `PassingLabels []string`

            The labels that indicate a passing result. Must be a subset of labels.

          - `Type LabelModel`

            The object type, which is always `label_model`.

            - `const LabelModelLabelModel LabelModel = "label_model"`

      - `Name string`

        The name of the grader.

      - `Type Multi`

        The object type, which is always `multi`.

        - `const MultiMulti Multi = "multi"`

  - `ModelSample param.Field[string]`

    The model sample to be evaluated. This value will be used to populate
    the `sample` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.
    The `output_json` variable will be populated if the model sample is a
    valid JSON string.

  - `Item param.Field[any]`

    The dataset item provided to the grader. This will be used to populate
    the `item` namespace. See [the guide](https://platform.openai.com/docs/guides/graders) for more details.

##### Returns

- `type FineTuningAlphaGraderRunResponse struct{…}`

  - `Metadata FineTuningAlphaGraderRunResponseMetadata`

    - `Errors FineTuningAlphaGraderRunResponseMetadataErrors`

      - `FormulaParseError bool`

      - `InvalidVariableError bool`

      - `ModelGraderParseError bool`

      - `ModelGraderRefusalError bool`

      - `ModelGraderServerError bool`

      - `ModelGraderServerErrorDetails string`

      - `OtherError bool`

      - `PythonGraderRuntimeError bool`

      - `PythonGraderRuntimeErrorDetails string`

      - `PythonGraderServerError bool`

      - `PythonGraderServerErrorType string`

      - `SampleParseError bool`

      - `TruncatedObservationError bool`

      - `UnresponsiveRewardError bool`

    - `ExecutionTime float64`

    - `Name string`

    - `SampledModelName string`

    - `Scores map[string, any]`

    - `TokenUsage int64`

    - `Type string`

  - `ModelGraderTokenUsagePerModel map[string, any]`

  - `Reward float64`

  - `SubRewards map[string, any]`

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.FineTuning.Alpha.Graders.Run(context.TODO(), openai.FineTuningAlphaGraderRunParams{
    Grader: openai.FineTuningAlphaGraderRunParamsGraderUnion{
      OfStringCheck: &openai.StringCheckGraderParam{
        Input: "input",
        Name: "name",
        Operation: openai.StringCheckGraderOperationEq,
        Reference: "reference",
      },
    },
    ModelSample: "model_sample",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Metadata)
}
```

#### Validate

`client.FineTuning.Alpha.Graders.Validate(ctx, body) (*FineTuningAlphaGraderValidateResponse, error)`

**post** `/fine_tuning/alpha/graders/validate`

Validate a grader.

##### Parameters

- `body FineTuningAlphaGraderValidateParams`

  - `Grader param.Field[FineTuningAlphaGraderValidateParamsGraderUnion]`

    The grader used for the fine-tuning job.

    - `type StringCheckGrader struct{…}`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `Input string`

        The input text. This may include template strings.

      - `Name string`

        The name of the grader.

      - `Operation StringCheckGraderOperation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

        - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

        - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

        - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

      - `Reference string`

        The reference text. This may include template strings.

      - `Type StringCheck`

        The object type, which is always `string_check`.

        - `const StringCheckStringCheck StringCheck = "string_check"`

    - `type TextSimilarityGrader struct{…}`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

        - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

        - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

        - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

        - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

        - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

        - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

        - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

        - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

        - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

        - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

      - `Input string`

        The text being graded.

      - `Name string`

        The name of the grader.

      - `Reference string`

        The text being graded against.

      - `Type TextSimilarity`

        The type of grader.

        - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

    - `type PythonGrader struct{…}`

      A PythonGrader object that runs a python script on the input.

      - `Name string`

        The name of the grader.

      - `Source string`

        The source code of the python script.

      - `Type Python`

        The object type, which is always `python`.

        - `const PythonPython Python = "python"`

      - `ImageTag string`

        The image tag to use for the python script.

    - `type ScoreModelGrader struct{…}`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Input []ScoreModelGraderInput`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

        - `Content ScoreModelGraderInputContentUnion`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `string`

          - `type ResponseInputText struct{…}`

            A text input to the model.

            - `Text string`

              The text input to the model.

            - `Type InputText`

              The type of the input item. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type ScoreModelGraderInputContentOutputText struct{…}`

            A text output from the model.

            - `Text string`

              The text output from the model.

            - `Type OutputText`

              The type of the output text. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

          - `type ScoreModelGraderInputContentInputImage struct{…}`

            An image input block used within EvalItem content arrays.

            - `ImageURL string`

              The URL of the image input.

            - `Type InputImage`

              The type of the image input. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

            - `Detail string`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `type ResponseInputAudio struct{…}`

            An audio input to the model.

            - `InputAudio ResponseInputAudioInputAudio`

              - `Data string`

                Base64-encoded audio data.

              - `Format string`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

            - `Type InputAudio`

              The type of the input item. Always `input_audio`.

              - `const InputAudioInputAudio InputAudio = "input_audio"`

          - `type GraderInputs []GraderInputUnion`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `string`

            - `type ResponseInputText struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type GraderInputOutputText struct{…}`

              A text output from the model.

              - `Text string`

                The text output from the model.

              - `Type OutputText`

                The type of the output text. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

            - `type GraderInputInputImage struct{…}`

              An image input block used within EvalItem content arrays.

              - `ImageURL string`

                The URL of the image input.

              - `Type InputImage`

                The type of the image input. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail string`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `type ResponseInputAudio struct{…}`

              An audio input to the model.

              - `InputAudio ResponseInputAudioInputAudio`

                - `Data string`

                  Base64-encoded audio data.

                - `Format string`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                  - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

              - `Type InputAudio`

                The type of the input item. Always `input_audio`.

                - `const InputAudioInputAudio InputAudio = "input_audio"`

        - `Role string`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

          - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

          - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

          - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

        - `Type string`

          The type of the message input. Always `message`.

          - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

      - `Model string`

        The model to use for the evaluation.

      - `Name string`

        The name of the grader.

      - `Type ScoreModel`

        The object type, which is always `score_model`.

        - `const ScoreModelScoreModel ScoreModel = "score_model"`

      - `Range []float64`

        The range of the score. Defaults to `[0, 1]`.

      - `SamplingParams ScoreModelGraderSamplingParams`

        The sampling parameters for the model.

        - `MaxCompletionsTokens int64`

          The maximum number of tokens the grader model may generate in its response.

        - `ReasoningEffort ReasoningEffort`

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

        - `Seed int64`

          A seed value to initialize the randomness, during sampling.

        - `Temperature float64`

          A higher temperature increases randomness in the outputs.

        - `TopP float64`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `type MultiGrader struct{…}`

      A MultiGrader object combines the output of multiple graders to produce a single score.

      - `CalculateOutput string`

        A formula to calculate the output based on grader results.

      - `Graders MultiGraderGradersUnion`

        A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type LabelModelGrader struct{…}`

          A LabelModelGrader object which uses a model to assign labels to each item
          in the evaluation.

          - `Input []LabelModelGraderInput`

            - `Content LabelModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type LabelModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type LabelModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

              - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

              - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

              - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

          - `Labels []string`

            The labels to assign to each item in the evaluation.

          - `Model string`

            The model to use for the evaluation. Must support structured outputs.

          - `Name string`

            The name of the grader.

          - `PassingLabels []string`

            The labels that indicate a passing result. Must be a subset of labels.

          - `Type LabelModel`

            The object type, which is always `label_model`.

            - `const LabelModelLabelModel LabelModel = "label_model"`

      - `Name string`

        The name of the grader.

      - `Type Multi`

        The object type, which is always `multi`.

        - `const MultiMulti Multi = "multi"`

##### Returns

- `type FineTuningAlphaGraderValidateResponse struct{…}`

  - `Grader FineTuningAlphaGraderValidateResponseGraderUnion`

    The grader used for the fine-tuning job.

    - `type StringCheckGrader struct{…}`

      A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

      - `Input string`

        The input text. This may include template strings.

      - `Name string`

        The name of the grader.

      - `Operation StringCheckGraderOperation`

        The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

        - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

        - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

        - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

        - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

      - `Reference string`

        The reference text. This may include template strings.

      - `Type StringCheck`

        The object type, which is always `string_check`.

        - `const StringCheckStringCheck StringCheck = "string_check"`

    - `type TextSimilarityGrader struct{…}`

      A TextSimilarityGrader object which grades text based on similarity metrics.

      - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

        The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
        `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
        or `rouge_l`.

        - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

        - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

        - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

        - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

        - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

        - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

        - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

        - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

        - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

        - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

        - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

      - `Input string`

        The text being graded.

      - `Name string`

        The name of the grader.

      - `Reference string`

        The text being graded against.

      - `Type TextSimilarity`

        The type of grader.

        - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

    - `type PythonGrader struct{…}`

      A PythonGrader object that runs a python script on the input.

      - `Name string`

        The name of the grader.

      - `Source string`

        The source code of the python script.

      - `Type Python`

        The object type, which is always `python`.

        - `const PythonPython Python = "python"`

      - `ImageTag string`

        The image tag to use for the python script.

    - `type ScoreModelGrader struct{…}`

      A ScoreModelGrader object that uses a model to assign a score to the input.

      - `Input []ScoreModelGraderInput`

        The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

        - `Content ScoreModelGraderInputContentUnion`

          Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

          - `string`

          - `type ResponseInputText struct{…}`

            A text input to the model.

            - `Text string`

              The text input to the model.

            - `Type InputText`

              The type of the input item. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type ScoreModelGraderInputContentOutputText struct{…}`

            A text output from the model.

            - `Text string`

              The text output from the model.

            - `Type OutputText`

              The type of the output text. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

          - `type ScoreModelGraderInputContentInputImage struct{…}`

            An image input block used within EvalItem content arrays.

            - `ImageURL string`

              The URL of the image input.

            - `Type InputImage`

              The type of the image input. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

            - `Detail string`

              The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

          - `type ResponseInputAudio struct{…}`

            An audio input to the model.

            - `InputAudio ResponseInputAudioInputAudio`

              - `Data string`

                Base64-encoded audio data.

              - `Format string`

                The format of the audio data. Currently supported formats are `mp3` and
                `wav`.

                - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

            - `Type InputAudio`

              The type of the input item. Always `input_audio`.

              - `const InputAudioInputAudio InputAudio = "input_audio"`

          - `type GraderInputs []GraderInputUnion`

            A list of inputs, each of which may be either an input text, output text, input
            image, or input audio object.

            - `string`

            - `type ResponseInputText struct{…}`

              A text input to the model.

              - `Text string`

                The text input to the model.

              - `Type InputText`

                The type of the input item. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type GraderInputOutputText struct{…}`

              A text output from the model.

              - `Text string`

                The text output from the model.

              - `Type OutputText`

                The type of the output text. Always `output_text`.

                - `const OutputTextOutputText OutputText = "output_text"`

            - `type GraderInputInputImage struct{…}`

              An image input block used within EvalItem content arrays.

              - `ImageURL string`

                The URL of the image input.

              - `Type InputImage`

                The type of the image input. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

              - `Detail string`

                The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

            - `type ResponseInputAudio struct{…}`

              An audio input to the model.

              - `InputAudio ResponseInputAudioInputAudio`

                - `Data string`

                  Base64-encoded audio data.

                - `Format string`

                  The format of the audio data. Currently supported formats are `mp3` and
                  `wav`.

                  - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                  - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

              - `Type InputAudio`

                The type of the input item. Always `input_audio`.

                - `const InputAudioInputAudio InputAudio = "input_audio"`

        - `Role string`

          The role of the message input. One of `user`, `assistant`, `system`, or
          `developer`.

          - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

          - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

          - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

          - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

        - `Type string`

          The type of the message input. Always `message`.

          - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

      - `Model string`

        The model to use for the evaluation.

      - `Name string`

        The name of the grader.

      - `Type ScoreModel`

        The object type, which is always `score_model`.

        - `const ScoreModelScoreModel ScoreModel = "score_model"`

      - `Range []float64`

        The range of the score. Defaults to `[0, 1]`.

      - `SamplingParams ScoreModelGraderSamplingParams`

        The sampling parameters for the model.

        - `MaxCompletionsTokens int64`

          The maximum number of tokens the grader model may generate in its response.

        - `ReasoningEffort ReasoningEffort`

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

        - `Seed int64`

          A seed value to initialize the randomness, during sampling.

        - `Temperature float64`

          A higher temperature increases randomness in the outputs.

        - `TopP float64`

          An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

    - `type MultiGrader struct{…}`

      A MultiGrader object combines the output of multiple graders to produce a single score.

      - `CalculateOutput string`

        A formula to calculate the output based on grader results.

      - `Graders MultiGraderGradersUnion`

        A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

        - `type StringCheckGrader struct{…}`

          A StringCheckGrader object that performs a string comparison between input and reference using a specified operation.

          - `Input string`

            The input text. This may include template strings.

          - `Name string`

            The name of the grader.

          - `Operation StringCheckGraderOperation`

            The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`.

            - `const StringCheckGraderOperationEq StringCheckGraderOperation = "eq"`

            - `const StringCheckGraderOperationNe StringCheckGraderOperation = "ne"`

            - `const StringCheckGraderOperationLike StringCheckGraderOperation = "like"`

            - `const StringCheckGraderOperationIlike StringCheckGraderOperation = "ilike"`

          - `Reference string`

            The reference text. This may include template strings.

          - `Type StringCheck`

            The object type, which is always `string_check`.

            - `const StringCheckStringCheck StringCheck = "string_check"`

        - `type TextSimilarityGrader struct{…}`

          A TextSimilarityGrader object which grades text based on similarity metrics.

          - `EvaluationMetric TextSimilarityGraderEvaluationMetric`

            The evaluation metric to use. One of `cosine`, `fuzzy_match`, `bleu`,
            `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`, `rouge_4`, `rouge_5`,
            or `rouge_l`.

            - `const TextSimilarityGraderEvaluationMetricCosine TextSimilarityGraderEvaluationMetric = "cosine"`

            - `const TextSimilarityGraderEvaluationMetricFuzzyMatch TextSimilarityGraderEvaluationMetric = "fuzzy_match"`

            - `const TextSimilarityGraderEvaluationMetricBleu TextSimilarityGraderEvaluationMetric = "bleu"`

            - `const TextSimilarityGraderEvaluationMetricGleu TextSimilarityGraderEvaluationMetric = "gleu"`

            - `const TextSimilarityGraderEvaluationMetricMeteor TextSimilarityGraderEvaluationMetric = "meteor"`

            - `const TextSimilarityGraderEvaluationMetricRouge1 TextSimilarityGraderEvaluationMetric = "rouge_1"`

            - `const TextSimilarityGraderEvaluationMetricRouge2 TextSimilarityGraderEvaluationMetric = "rouge_2"`

            - `const TextSimilarityGraderEvaluationMetricRouge3 TextSimilarityGraderEvaluationMetric = "rouge_3"`

            - `const TextSimilarityGraderEvaluationMetricRouge4 TextSimilarityGraderEvaluationMetric = "rouge_4"`

            - `const TextSimilarityGraderEvaluationMetricRouge5 TextSimilarityGraderEvaluationMetric = "rouge_5"`

            - `const TextSimilarityGraderEvaluationMetricRougeL TextSimilarityGraderEvaluationMetric = "rouge_l"`

          - `Input string`

            The text being graded.

          - `Name string`

            The name of the grader.

          - `Reference string`

            The text being graded against.

          - `Type TextSimilarity`

            The type of grader.

            - `const TextSimilarityTextSimilarity TextSimilarity = "text_similarity"`

        - `type PythonGrader struct{…}`

          A PythonGrader object that runs a python script on the input.

          - `Name string`

            The name of the grader.

          - `Source string`

            The source code of the python script.

          - `Type Python`

            The object type, which is always `python`.

            - `const PythonPython Python = "python"`

          - `ImageTag string`

            The image tag to use for the python script.

        - `type ScoreModelGrader struct{…}`

          A ScoreModelGrader object that uses a model to assign a score to the input.

          - `Input []ScoreModelGraderInput`

            The input messages evaluated by the grader. Supports text, output text, input image, and input audio content blocks, and may include template strings.

            - `Content ScoreModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type ScoreModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type ScoreModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const ScoreModelGraderInputRoleUser ScoreModelGraderInputRole = "user"`

              - `const ScoreModelGraderInputRoleAssistant ScoreModelGraderInputRole = "assistant"`

              - `const ScoreModelGraderInputRoleSystem ScoreModelGraderInputRole = "system"`

              - `const ScoreModelGraderInputRoleDeveloper ScoreModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const ScoreModelGraderInputTypeMessage ScoreModelGraderInputType = "message"`

          - `Model string`

            The model to use for the evaluation.

          - `Name string`

            The name of the grader.

          - `Type ScoreModel`

            The object type, which is always `score_model`.

            - `const ScoreModelScoreModel ScoreModel = "score_model"`

          - `Range []float64`

            The range of the score. Defaults to `[0, 1]`.

          - `SamplingParams ScoreModelGraderSamplingParams`

            The sampling parameters for the model.

            - `MaxCompletionsTokens int64`

              The maximum number of tokens the grader model may generate in its response.

            - `ReasoningEffort ReasoningEffort`

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

            - `Seed int64`

              A seed value to initialize the randomness, during sampling.

            - `Temperature float64`

              A higher temperature increases randomness in the outputs.

            - `TopP float64`

              An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

        - `type LabelModelGrader struct{…}`

          A LabelModelGrader object which uses a model to assign labels to each item
          in the evaluation.

          - `Input []LabelModelGraderInput`

            - `Content LabelModelGraderInputContentUnion`

              Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

              - `string`

              - `type ResponseInputText struct{…}`

                A text input to the model.

                - `Text string`

                  The text input to the model.

                - `Type InputText`

                  The type of the input item. Always `input_text`.

                  - `const InputTextInputText InputText = "input_text"`

              - `type LabelModelGraderInputContentOutputText struct{…}`

                A text output from the model.

                - `Text string`

                  The text output from the model.

                - `Type OutputText`

                  The type of the output text. Always `output_text`.

                  - `const OutputTextOutputText OutputText = "output_text"`

              - `type LabelModelGraderInputContentInputImage struct{…}`

                An image input block used within EvalItem content arrays.

                - `ImageURL string`

                  The URL of the image input.

                - `Type InputImage`

                  The type of the image input. Always `input_image`.

                  - `const InputImageInputImage InputImage = "input_image"`

                - `Detail string`

                  The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

              - `type ResponseInputAudio struct{…}`

                An audio input to the model.

                - `InputAudio ResponseInputAudioInputAudio`

                  - `Data string`

                    Base64-encoded audio data.

                  - `Format string`

                    The format of the audio data. Currently supported formats are `mp3` and
                    `wav`.

                    - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                    - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                - `Type InputAudio`

                  The type of the input item. Always `input_audio`.

                  - `const InputAudioInputAudio InputAudio = "input_audio"`

              - `type GraderInputs []GraderInputUnion`

                A list of inputs, each of which may be either an input text, output text, input
                image, or input audio object.

                - `string`

                - `type ResponseInputText struct{…}`

                  A text input to the model.

                  - `Text string`

                    The text input to the model.

                  - `Type InputText`

                    The type of the input item. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type GraderInputOutputText struct{…}`

                  A text output from the model.

                  - `Text string`

                    The text output from the model.

                  - `Type OutputText`

                    The type of the output text. Always `output_text`.

                    - `const OutputTextOutputText OutputText = "output_text"`

                - `type GraderInputInputImage struct{…}`

                  An image input block used within EvalItem content arrays.

                  - `ImageURL string`

                    The URL of the image input.

                  - `Type InputImage`

                    The type of the image input. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

                  - `Detail string`

                    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

                - `type ResponseInputAudio struct{…}`

                  An audio input to the model.

                  - `InputAudio ResponseInputAudioInputAudio`

                    - `Data string`

                      Base64-encoded audio data.

                    - `Format string`

                      The format of the audio data. Currently supported formats are `mp3` and
                      `wav`.

                      - `const ResponseInputAudioInputAudioFormatMP3 ResponseInputAudioInputAudioFormat = "mp3"`

                      - `const ResponseInputAudioInputAudioFormatWAV ResponseInputAudioInputAudioFormat = "wav"`

                  - `Type InputAudio`

                    The type of the input item. Always `input_audio`.

                    - `const InputAudioInputAudio InputAudio = "input_audio"`

            - `Role string`

              The role of the message input. One of `user`, `assistant`, `system`, or
              `developer`.

              - `const LabelModelGraderInputRoleUser LabelModelGraderInputRole = "user"`

              - `const LabelModelGraderInputRoleAssistant LabelModelGraderInputRole = "assistant"`

              - `const LabelModelGraderInputRoleSystem LabelModelGraderInputRole = "system"`

              - `const LabelModelGraderInputRoleDeveloper LabelModelGraderInputRole = "developer"`

            - `Type string`

              The type of the message input. Always `message`.

              - `const LabelModelGraderInputTypeMessage LabelModelGraderInputType = "message"`

          - `Labels []string`

            The labels to assign to each item in the evaluation.

          - `Model string`

            The model to use for the evaluation. Must support structured outputs.

          - `Name string`

            The name of the grader.

          - `PassingLabels []string`

            The labels that indicate a passing result. Must be a subset of labels.

          - `Type LabelModel`

            The object type, which is always `label_model`.

            - `const LabelModelLabelModel LabelModel = "label_model"`

      - `Name string`

        The name of the grader.

      - `Type Multi`

        The object type, which is always `multi`.

        - `const MultiMulti Multi = "multi"`

##### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.FineTuning.Alpha.Graders.Validate(context.TODO(), openai.FineTuningAlphaGraderValidateParams{
    Grader: openai.FineTuningAlphaGraderValidateParamsGraderUnion{
      OfStringCheckGrader: &openai.StringCheckGraderParam{
        Input: "input",
        Name: "name",
        Operation: openai.StringCheckGraderOperationEq,
        Reference: "reference",
      },
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response.Grader)
}
```
