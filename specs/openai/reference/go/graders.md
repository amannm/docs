# Graders

## Grader Models

### Domain Types

### Grader Inputs

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

### Label Model Grader

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

### Multi Grader

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

### Python Grader

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

### Score Model Grader

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

### String Check Grader

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

### Text Similarity Grader

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
