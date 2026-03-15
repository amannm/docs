# Moderations

## Create

`ModerationCreateResponse moderations().create(ModerationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/moderations`

Classifies if text and/or image inputs are potentially harmful. Learn
more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

### Parameters

- `ModerationCreateParams params`

  - `Input input`

    Input (or inputs) to classify. Can be a single string, an array of strings, or
    an array of multi-modal input objects similar to other models.

    - `String`

    - `List<String>`

    - `List<ModerationMultiModalInput>`

      - `class ModerationImageUrlInput:`

        An object describing an image to classify.

        - `ImageUrl imageUrl`

          Contains either an image URL or a data URL for a base64 encoded image.

          - `String url`

            Either a URL of the image or the base64 encoded image data.

        - `JsonValue; type "image_url"constant`

          Always `image_url`.

          - `IMAGE_URL("image_url")`

      - `class ModerationTextInput:`

        An object describing text to classify.

        - `String text`

          A string of text to classify.

        - `JsonValue; type "text"constant`

          Always `text`.

          - `TEXT("text")`

  - `Optional<ModerationModel> model`

    The content moderation model you would like to use. Learn more in
    [the moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about
    available models [here](https://platform.openai.com/docs/models#moderation).

    - `OMNI_MODERATION_LATEST("omni-moderation-latest")`

    - `OMNI_MODERATION_2024_09_26("omni-moderation-2024-09-26")`

    - `TEXT_MODERATION_LATEST("text-moderation-latest")`

    - `TEXT_MODERATION_STABLE("text-moderation-stable")`

### Returns

- `class ModerationCreateResponse:`

  Represents if a given text input is potentially harmful.

  - `String id`

    The unique identifier for the moderation request.

  - `String model`

    The model used to generate the moderation results.

  - `List<Moderation> results`

    A list of moderation objects.

    - `Categories categories`

      A list of the categories, and whether they are flagged or not.

      - `boolean harassment`

        Content that expresses, incites, or promotes harassing language towards any target.

      - `boolean harassmentThreatening`

        Harassment content that also includes violence or serious harm towards any target.

      - `boolean hate`

        Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

      - `boolean hateThreatening`

        Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

      - `Optional<Boolean> illicit`

        Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, "how to shoplift" would fit this category.

      - `Optional<Boolean> illicitViolent`

        Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

      - `boolean selfHarm`

        Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

      - `boolean selfHarmInstructions`

        Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

      - `boolean selfHarmIntent`

        Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

      - `boolean sexual`

        Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

      - `boolean sexualMinors`

        Sexual content that includes an individual who is under 18 years old.

      - `boolean violence`

        Content that depicts death, violence, or physical injury.

      - `boolean violenceGraphic`

        Content that depicts death, violence, or physical injury in graphic detail.

    - `CategoryAppliedInputTypes categoryAppliedInputTypes`

      A list of the categories along with the input type(s) that the score applies to.

      - `List<Harassment> harassment`

        The applied input type(s) for the category 'harassment'.

        - `TEXT("text")`

      - `List<HarassmentThreatening> harassmentThreatening`

        The applied input type(s) for the category 'harassment/threatening'.

        - `TEXT("text")`

      - `List<Hate> hate`

        The applied input type(s) for the category 'hate'.

        - `TEXT("text")`

      - `List<HateThreatening> hateThreatening`

        The applied input type(s) for the category 'hate/threatening'.

        - `TEXT("text")`

      - `List<Illicit> illicit`

        The applied input type(s) for the category 'illicit'.

        - `TEXT("text")`

      - `List<IllicitViolent> illicitViolent`

        The applied input type(s) for the category 'illicit/violent'.

        - `TEXT("text")`

      - `List<SelfHarm> selfHarm`

        The applied input type(s) for the category 'self-harm'.

        - `TEXT("text")`

        - `IMAGE("image")`

      - `List<SelfHarmInstruction> selfHarmInstructions`

        The applied input type(s) for the category 'self-harm/instructions'.

        - `TEXT("text")`

        - `IMAGE("image")`

      - `List<SelfHarmIntent> selfHarmIntent`

        The applied input type(s) for the category 'self-harm/intent'.

        - `TEXT("text")`

        - `IMAGE("image")`

      - `List<Sexual> sexual`

        The applied input type(s) for the category 'sexual'.

        - `TEXT("text")`

        - `IMAGE("image")`

      - `List<SexualMinor> sexualMinors`

        The applied input type(s) for the category 'sexual/minors'.

        - `TEXT("text")`

      - `List<Violence> violence`

        The applied input type(s) for the category 'violence'.

        - `TEXT("text")`

        - `IMAGE("image")`

      - `List<ViolenceGraphic> violenceGraphic`

        The applied input type(s) for the category 'violence/graphic'.

        - `TEXT("text")`

        - `IMAGE("image")`

    - `CategoryScores categoryScores`

      A list of the categories along with their scores as predicted by model.

      - `double harassment`

        The score for the category 'harassment'.

      - `double harassmentThreatening`

        The score for the category 'harassment/threatening'.

      - `double hate`

        The score for the category 'hate'.

      - `double hateThreatening`

        The score for the category 'hate/threatening'.

      - `double illicit`

        The score for the category 'illicit'.

      - `double illicitViolent`

        The score for the category 'illicit/violent'.

      - `double selfHarm`

        The score for the category 'self-harm'.

      - `double selfHarmInstructions`

        The score for the category 'self-harm/instructions'.

      - `double selfHarmIntent`

        The score for the category 'self-harm/intent'.

      - `double sexual`

        The score for the category 'sexual'.

      - `double sexualMinors`

        The score for the category 'sexual/minors'.

      - `double violence`

        The score for the category 'violence'.

      - `double violenceGraphic`

        The score for the category 'violence/graphic'.

    - `boolean flagged`

      Whether any of the below categories are flagged.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.moderations.ModerationCreateParams;
import com.openai.models.moderations.ModerationCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ModerationCreateParams params = ModerationCreateParams.builder()
            .input("I want to kill them.")
            .build();
        ModerationCreateResponse moderation = client.moderations().create(params);
    }
}
```

### Domain Types

### Moderation

- `class Moderation:`

  - `Categories categories`

    A list of the categories, and whether they are flagged or not.

    - `boolean harassment`

      Content that expresses, incites, or promotes harassing language towards any target.

    - `boolean harassmentThreatening`

      Harassment content that also includes violence or serious harm towards any target.

    - `boolean hate`

      Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste. Hateful content aimed at non-protected groups (e.g., chess players) is harassment.

    - `boolean hateThreatening`

      Hateful content that also includes violence or serious harm towards the targeted group based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.

    - `Optional<Boolean> illicit`

      Content that includes instructions or advice that facilitate the planning or execution of wrongdoing, or that gives advice or instruction on how to commit illicit acts. For example, "how to shoplift" would fit this category.

    - `Optional<Boolean> illicitViolent`

      Content that includes instructions or advice that facilitate the planning or execution of wrongdoing that also includes violence, or that gives advice or instruction on the procurement of any weapon.

    - `boolean selfHarm`

      Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.

    - `boolean selfHarmInstructions`

      Content that encourages performing acts of self-harm, such as suicide, cutting, and eating disorders, or that gives instructions or advice on how to commit such acts.

    - `boolean selfHarmIntent`

      Content where the speaker expresses that they are engaging or intend to engage in acts of self-harm, such as suicide, cutting, and eating disorders.

    - `boolean sexual`

      Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).

    - `boolean sexualMinors`

      Sexual content that includes an individual who is under 18 years old.

    - `boolean violence`

      Content that depicts death, violence, or physical injury.

    - `boolean violenceGraphic`

      Content that depicts death, violence, or physical injury in graphic detail.

  - `CategoryAppliedInputTypes categoryAppliedInputTypes`

    A list of the categories along with the input type(s) that the score applies to.

    - `List<Harassment> harassment`

      The applied input type(s) for the category 'harassment'.

      - `TEXT("text")`

    - `List<HarassmentThreatening> harassmentThreatening`

      The applied input type(s) for the category 'harassment/threatening'.

      - `TEXT("text")`

    - `List<Hate> hate`

      The applied input type(s) for the category 'hate'.

      - `TEXT("text")`

    - `List<HateThreatening> hateThreatening`

      The applied input type(s) for the category 'hate/threatening'.

      - `TEXT("text")`

    - `List<Illicit> illicit`

      The applied input type(s) for the category 'illicit'.

      - `TEXT("text")`

    - `List<IllicitViolent> illicitViolent`

      The applied input type(s) for the category 'illicit/violent'.

      - `TEXT("text")`

    - `List<SelfHarm> selfHarm`

      The applied input type(s) for the category 'self-harm'.

      - `TEXT("text")`

      - `IMAGE("image")`

    - `List<SelfHarmInstruction> selfHarmInstructions`

      The applied input type(s) for the category 'self-harm/instructions'.

      - `TEXT("text")`

      - `IMAGE("image")`

    - `List<SelfHarmIntent> selfHarmIntent`

      The applied input type(s) for the category 'self-harm/intent'.

      - `TEXT("text")`

      - `IMAGE("image")`

    - `List<Sexual> sexual`

      The applied input type(s) for the category 'sexual'.

      - `TEXT("text")`

      - `IMAGE("image")`

    - `List<SexualMinor> sexualMinors`

      The applied input type(s) for the category 'sexual/minors'.

      - `TEXT("text")`

    - `List<Violence> violence`

      The applied input type(s) for the category 'violence'.

      - `TEXT("text")`

      - `IMAGE("image")`

    - `List<ViolenceGraphic> violenceGraphic`

      The applied input type(s) for the category 'violence/graphic'.

      - `TEXT("text")`

      - `IMAGE("image")`

  - `CategoryScores categoryScores`

    A list of the categories along with their scores as predicted by model.

    - `double harassment`

      The score for the category 'harassment'.

    - `double harassmentThreatening`

      The score for the category 'harassment/threatening'.

    - `double hate`

      The score for the category 'hate'.

    - `double hateThreatening`

      The score for the category 'hate/threatening'.

    - `double illicit`

      The score for the category 'illicit'.

    - `double illicitViolent`

      The score for the category 'illicit/violent'.

    - `double selfHarm`

      The score for the category 'self-harm'.

    - `double selfHarmInstructions`

      The score for the category 'self-harm/instructions'.

    - `double selfHarmIntent`

      The score for the category 'self-harm/intent'.

    - `double sexual`

      The score for the category 'sexual'.

    - `double sexualMinors`

      The score for the category 'sexual/minors'.

    - `double violence`

      The score for the category 'violence'.

    - `double violenceGraphic`

      The score for the category 'violence/graphic'.

  - `boolean flagged`

    Whether any of the below categories are flagged.

### Moderation Image URL Input

- `class ModerationImageUrlInput:`

  An object describing an image to classify.

  - `ImageUrl imageUrl`

    Contains either an image URL or a data URL for a base64 encoded image.

    - `String url`

      Either a URL of the image or the base64 encoded image data.

  - `JsonValue; type "image_url"constant`

    Always `image_url`.

    - `IMAGE_URL("image_url")`

### Moderation Model

- `enum ModerationModel:`

  - `OMNI_MODERATION_LATEST("omni-moderation-latest")`

  - `OMNI_MODERATION_2024_09_26("omni-moderation-2024-09-26")`

  - `TEXT_MODERATION_LATEST("text-moderation-latest")`

  - `TEXT_MODERATION_STABLE("text-moderation-stable")`

### Moderation Multi Modal Input

- `class ModerationMultiModalInput: A class that can be one of several variants.union`

  An object describing an image to classify.

  - `class ModerationImageUrlInput:`

    An object describing an image to classify.

    - `ImageUrl imageUrl`

      Contains either an image URL or a data URL for a base64 encoded image.

      - `String url`

        Either a URL of the image or the base64 encoded image data.

    - `JsonValue; type "image_url"constant`

      Always `image_url`.

      - `IMAGE_URL("image_url")`

  - `class ModerationTextInput:`

    An object describing text to classify.

    - `String text`

      A string of text to classify.

    - `JsonValue; type "text"constant`

      Always `text`.

      - `TEXT("text")`

### Moderation Text Input

- `class ModerationTextInput:`

  An object describing text to classify.

  - `String text`

    A string of text to classify.

  - `JsonValue; type "text"constant`

    Always `text`.

    - `TEXT("text")`
