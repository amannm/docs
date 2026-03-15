# Moderations

## Create

`client.Moderations.New(ctx, body) (*ModerationNewResponse, error)`

**post** `/moderations`

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

### Parameters

- `body ModerationNewParams`

  - `Input param.Field[ModerationNewParamsInputUnion]`

    Input (or inputs) to classify. Can be a single string, an array of strings, or
    an array of multi-modal input objects similar to other models.

    - `string`

    - `type ModerationNewParamsInputArray []string`

      An array of strings to classify for moderation.

    - `type ModerationNewParamsInputModerationMultiModalArray []ModerationMultiModalInputUnion`

      An array of multi-modal inputs to the moderation model.

      - `type ModerationImageURLInput struct{…}`

        An object describing an image to classify.

        - `ImageURL ModerationImageURLInputImageURL`

          Contains either an image URL or a data URL for a base64 encoded image.

          - `URL string`

            Either a URL of the image or the base64 encoded image data.

        - `Type ImageURL`

          Always `image_url`.

          - `const ImageURLImageURL ImageURL = "image_url"`

      - `type ModerationTextInput struct{…}`

        An object describing text to classify.

        - `Text string`

          A string of text to classify.

        - `Type Text`

          Always `text`.

          - `const TextText Text = "text"`

  - `Model param.Field[ModerationModel]`

    The content moderation model you would like to use. Learn more in
    [the moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about
    available models [here](https://platform.openai.com/docs/models#moderation).

    - `string`

    - `type ModerationModel string`

      - `const ModerationModelOmniModerationLatest ModerationModel = "omni-moderation-latest"`

      - `const ModerationModelOmniModeration2024_09_26 ModerationModel = "omni-moderation-2024-09-26"`

      - `const ModerationModelTextModerationLatest ModerationModel = "text-moderation-latest"`

      - `const ModerationModelTextModerationStable ModerationModel = "text-moderation-stable"`

### Returns

- `type ModerationNewResponse struct{…}`

  Represents if a given text input is potentially harmful.

  - `ID string`

    The unique identifier for the moderation request.

  - `Model string`

    The model used to generate the moderation results.

  - `Results []Moderation`

    A list of moderation objects.

    - `Categories ModerationCategories`

      A list of the categories, and whether they are flagged or not.

      - `Harassment bool`

        Content that expresses, incites, or promotes harassing language towards any target.

      - `HarassmentThreatening bool`

        Harassment content that also includes violence or serious harm towards any target.

      - `Hate bool`

        Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

      - `HateThreatening bool`

        Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

      - `Illicit bool`

        Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, "how to shoplift" would fit this category.

      - `IllicitViolent bool`

        Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

      - `SelfHarm bool`

        Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

      - `SelfHarmInstructions bool`

        Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

      - `SelfHarmIntent bool`

        Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

      - `Sexual bool`

        Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

      - `SexualMinors bool`

        Sexual content that includes an individual who is under 18 years old.

      - `Violence bool`

        Content that depicts death, violence, or physical injury.

      - `ViolenceGraphic bool`

        Content that depicts death, violence, or physical injury in graphic detail.

    - `CategoryAppliedInputTypes ModerationCategoryAppliedInputTypes`

      A list of the categories along with the input type(s) that the score applies to.

      - `Harassment []string`

        The applied input type(s) for the category 'harassment'.

        - `const ModerationCategoryAppliedInputTypesHarassmentText ModerationCategoryAppliedInputTypesHarassment = "text"`

      - `HarassmentThreatening []string`

        The applied input type(s) for the category 'harassment/threatening'.

        - `const ModerationCategoryAppliedInputTypesHarassmentThreateningText ModerationCategoryAppliedInputTypesHarassmentThreatening = "text"`

      - `Hate []string`

        The applied input type(s) for the category 'hate'.

        - `const ModerationCategoryAppliedInputTypesHateText ModerationCategoryAppliedInputTypesHate = "text"`

      - `HateThreatening []string`

        The applied input type(s) for the category 'hate/threatening'.

        - `const ModerationCategoryAppliedInputTypesHateThreateningText ModerationCategoryAppliedInputTypesHateThreatening = "text"`

      - `Illicit []string`

        The applied input type(s) for the category 'illicit'.

        - `const ModerationCategoryAppliedInputTypesIllicitText ModerationCategoryAppliedInputTypesIllicit = "text"`

      - `IllicitViolent []string`

        The applied input type(s) for the category 'illicit/violent'.

        - `const ModerationCategoryAppliedInputTypesIllicitViolentText ModerationCategoryAppliedInputTypesIllicitViolent = "text"`

      - `SelfHarm []string`

        The applied input type(s) for the category 'self-harm'.

        - `const ModerationCategoryAppliedInputTypesSelfHarmText ModerationCategoryAppliedInputTypesSelfHarm = "text"`

        - `const ModerationCategoryAppliedInputTypesSelfHarmImage ModerationCategoryAppliedInputTypesSelfHarm = "image"`

      - `SelfHarmInstructions []string`

        The applied input type(s) for the category 'self-harm/instructions'.

        - `const ModerationCategoryAppliedInputTypesSelfHarmInstructionText ModerationCategoryAppliedInputTypesSelfHarmInstruction = "text"`

        - `const ModerationCategoryAppliedInputTypesSelfHarmInstructionImage ModerationCategoryAppliedInputTypesSelfHarmInstruction = "image"`

      - `SelfHarmIntent []string`

        The applied input type(s) for the category 'self-harm/intent'.

        - `const ModerationCategoryAppliedInputTypesSelfHarmIntentText ModerationCategoryAppliedInputTypesSelfHarmIntent = "text"`

        - `const ModerationCategoryAppliedInputTypesSelfHarmIntentImage ModerationCategoryAppliedInputTypesSelfHarmIntent = "image"`

      - `Sexual []string`

        The applied input type(s) for the category 'sexual'.

        - `const ModerationCategoryAppliedInputTypesSexualText ModerationCategoryAppliedInputTypesSexual = "text"`

        - `const ModerationCategoryAppliedInputTypesSexualImage ModerationCategoryAppliedInputTypesSexual = "image"`

      - `SexualMinors []string`

        The applied input type(s) for the category 'sexual/minors'.

        - `const ModerationCategoryAppliedInputTypesSexualMinorText ModerationCategoryAppliedInputTypesSexualMinor = "text"`

      - `Violence []string`

        The applied input type(s) for the category 'violence'.

        - `const ModerationCategoryAppliedInputTypesViolenceText ModerationCategoryAppliedInputTypesViolence = "text"`

        - `const ModerationCategoryAppliedInputTypesViolenceImage ModerationCategoryAppliedInputTypesViolence = "image"`

      - `ViolenceGraphic []string`

        The applied input type(s) for the category 'violence/graphic'.

        - `const ModerationCategoryAppliedInputTypesViolenceGraphicText ModerationCategoryAppliedInputTypesViolenceGraphic = "text"`

        - `const ModerationCategoryAppliedInputTypesViolenceGraphicImage ModerationCategoryAppliedInputTypesViolenceGraphic = "image"`

    - `CategoryScores ModerationCategoryScores`

      A list of the categories along with their scores as predicted by model.

      - `Harassment float64`

        The score for the category 'harassment'.

      - `HarassmentThreatening float64`

        The score for the category 'harassment/threatening'.

      - `Hate float64`

        The score for the category 'hate'.

      - `HateThreatening float64`

        The score for the category 'hate/threatening'.

      - `Illicit float64`

        The score for the category 'illicit'.

      - `IllicitViolent float64`

        The score for the category 'illicit/violent'.

      - `SelfHarm float64`

        The score for the category 'self-harm'.

      - `SelfHarmInstructions float64`

        The score for the category 'self-harm/instructions'.

      - `SelfHarmIntent float64`

        The score for the category 'self-harm/intent'.

      - `Sexual float64`

        The score for the category 'sexual'.

      - `SexualMinors float64`

        The score for the category 'sexual/minors'.

      - `Violence float64`

        The score for the category 'violence'.

      - `ViolenceGraphic float64`

        The score for the category 'violence/graphic'.

    - `Flagged bool`

      Whether any of the below categories are flagged.

### Example

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
  moderation, err := client.Moderations.New(context.TODO(), openai.ModerationNewParams{
    Input: openai.ModerationNewParamsInputUnion{
      OfString: openai.String("I want to kill them."),
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", moderation.ID)
}
```

### Domain Types

### Moderation

- `type Moderation struct{…}`

  - `Categories ModerationCategories`

    A list of the categories, and whether they are flagged or not.

    - `Harassment bool`

      Content that expresses, incites, or promotes harassing language towards any target.

    - `HarassmentThreatening bool`

      Harassment content that also includes violence or serious harm towards any target.

    - `Hate bool`

      Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

    - `HateThreatening bool`

      Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

    - `Illicit bool`

      Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, "how to shoplift" would fit this category.

    - `IllicitViolent bool`

      Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

    - `SelfHarm bool`

      Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

    - `SelfHarmInstructions bool`

      Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

    - `SelfHarmIntent bool`

      Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

    - `Sexual bool`

      Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

    - `SexualMinors bool`

      Sexual content that includes an individual who is under 18 years old.

    - `Violence bool`

      Content that depicts death, violence, or physical injury.

    - `ViolenceGraphic bool`

      Content that depicts death, violence, or physical injury in graphic detail.

  - `CategoryAppliedInputTypes ModerationCategoryAppliedInputTypes`

    A list of the categories along with the input type(s) that the score applies to.

    - `Harassment []string`

      The applied input type(s) for the category 'harassment'.

      - `const ModerationCategoryAppliedInputTypesHarassmentText ModerationCategoryAppliedInputTypesHarassment = "text"`

    - `HarassmentThreatening []string`

      The applied input type(s) for the category 'harassment/threatening'.

      - `const ModerationCategoryAppliedInputTypesHarassmentThreateningText ModerationCategoryAppliedInputTypesHarassmentThreatening = "text"`

    - `Hate []string`

      The applied input type(s) for the category 'hate'.

      - `const ModerationCategoryAppliedInputTypesHateText ModerationCategoryAppliedInputTypesHate = "text"`

    - `HateThreatening []string`

      The applied input type(s) for the category 'hate/threatening'.

      - `const ModerationCategoryAppliedInputTypesHateThreateningText ModerationCategoryAppliedInputTypesHateThreatening = "text"`

    - `Illicit []string`

      The applied input type(s) for the category 'illicit'.

      - `const ModerationCategoryAppliedInputTypesIllicitText ModerationCategoryAppliedInputTypesIllicit = "text"`

    - `IllicitViolent []string`

      The applied input type(s) for the category 'illicit/violent'.

      - `const ModerationCategoryAppliedInputTypesIllicitViolentText ModerationCategoryAppliedInputTypesIllicitViolent = "text"`

    - `SelfHarm []string`

      The applied input type(s) for the category 'self-harm'.

      - `const ModerationCategoryAppliedInputTypesSelfHarmText ModerationCategoryAppliedInputTypesSelfHarm = "text"`

      - `const ModerationCategoryAppliedInputTypesSelfHarmImage ModerationCategoryAppliedInputTypesSelfHarm = "image"`

    - `SelfHarmInstructions []string`

      The applied input type(s) for the category 'self-harm/instructions'.

      - `const ModerationCategoryAppliedInputTypesSelfHarmInstructionText ModerationCategoryAppliedInputTypesSelfHarmInstruction = "text"`

      - `const ModerationCategoryAppliedInputTypesSelfHarmInstructionImage ModerationCategoryAppliedInputTypesSelfHarmInstruction = "image"`

    - `SelfHarmIntent []string`

      The applied input type(s) for the category 'self-harm/intent'.

      - `const ModerationCategoryAppliedInputTypesSelfHarmIntentText ModerationCategoryAppliedInputTypesSelfHarmIntent = "text"`

      - `const ModerationCategoryAppliedInputTypesSelfHarmIntentImage ModerationCategoryAppliedInputTypesSelfHarmIntent = "image"`

    - `Sexual []string`

      The applied input type(s) for the category 'sexual'.

      - `const ModerationCategoryAppliedInputTypesSexualText ModerationCategoryAppliedInputTypesSexual = "text"`

      - `const ModerationCategoryAppliedInputTypesSexualImage ModerationCategoryAppliedInputTypesSexual = "image"`

    - `SexualMinors []string`

      The applied input type(s) for the category 'sexual/minors'.

      - `const ModerationCategoryAppliedInputTypesSexualMinorText ModerationCategoryAppliedInputTypesSexualMinor = "text"`

    - `Violence []string`

      The applied input type(s) for the category 'violence'.

      - `const ModerationCategoryAppliedInputTypesViolenceText ModerationCategoryAppliedInputTypesViolence = "text"`

      - `const ModerationCategoryAppliedInputTypesViolenceImage ModerationCategoryAppliedInputTypesViolence = "image"`

    - `ViolenceGraphic []string`

      The applied input type(s) for the category 'violence/graphic'.

      - `const ModerationCategoryAppliedInputTypesViolenceGraphicText ModerationCategoryAppliedInputTypesViolenceGraphic = "text"`

      - `const ModerationCategoryAppliedInputTypesViolenceGraphicImage ModerationCategoryAppliedInputTypesViolenceGraphic = "image"`

  - `CategoryScores ModerationCategoryScores`

    A list of the categories along with their scores as predicted by model.

    - `Harassment float64`

      The score for the category 'harassment'.

    - `HarassmentThreatening float64`

      The score for the category 'harassment/threatening'.

    - `Hate float64`

      The score for the category 'hate'.

    - `HateThreatening float64`

      The score for the category 'hate/threatening'.

    - `Illicit float64`

      The score for the category 'illicit'.

    - `IllicitViolent float64`

      The score for the category 'illicit/violent'.

    - `SelfHarm float64`

      The score for the category 'self-harm'.

    - `SelfHarmInstructions float64`

      The score for the category 'self-harm/instructions'.

    - `SelfHarmIntent float64`

      The score for the category 'self-harm/intent'.

    - `Sexual float64`

      The score for the category 'sexual'.

    - `SexualMinors float64`

      The score for the category 'sexual/minors'.

    - `Violence float64`

      The score for the category 'violence'.

    - `ViolenceGraphic float64`

      The score for the category 'violence/graphic'.

  - `Flagged bool`

    Whether any of the below categories are flagged.

### Moderation Image URL Input

- `type ModerationImageURLInput struct{…}`

  An object describing an image to classify.

  - `ImageURL ModerationImageURLInputImageURL`

    Contains either an image URL or a data URL for a base64 encoded image.

    - `URL string`

      Either a URL of the image or the base64 encoded image data.

  - `Type ImageURL`

    Always `image_url`.

    - `const ImageURLImageURL ImageURL = "image_url"`

### Moderation Model

- `type ModerationModel string`

  - `const ModerationModelOmniModerationLatest ModerationModel = "omni-moderation-latest"`

  - `const ModerationModelOmniModeration2024_09_26 ModerationModel = "omni-moderation-2024-09-26"`

  - `const ModerationModelTextModerationLatest ModerationModel = "text-moderation-latest"`

  - `const ModerationModelTextModerationStable ModerationModel = "text-moderation-stable"`

### Moderation Multi Modal Input

- `type ModerationMultiModalInputUnion interface{…}`

  An object describing an image to classify.

  - `type ModerationImageURLInput struct{…}`

    An object describing an image to classify.

    - `ImageURL ModerationImageURLInputImageURL`

      Contains either an image URL or a data URL for a base64 encoded image.

      - `URL string`

        Either a URL of the image or the base64 encoded image data.

    - `Type ImageURL`

      Always `image_url`.

      - `const ImageURLImageURL ImageURL = "image_url"`

  - `type ModerationTextInput struct{…}`

    An object describing text to classify.

    - `Text string`

      A string of text to classify.

    - `Type Text`

      Always `text`.

      - `const TextText Text = "text"`

### Moderation Text Input

- `type ModerationTextInput struct{…}`

  An object describing text to classify.

  - `Text string`

    A string of text to classify.

  - `Type Text`

    Always `text`.

    - `const TextText Text = "text"`
