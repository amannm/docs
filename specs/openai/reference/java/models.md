# Models

## List

`ModelListPage models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/models`

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Parameters

- `ModelListParams params`

### Returns

- `class Model:`

  Describes an OpenAI model offering that can be used with the API.

  - `String id`

    The model identifier, which can be referenced in the API endpoints.

  - `long created`

    The Unix timestamp (in seconds) when the model was created.

  - `JsonValue; object_ "model"constant`

    The object type, which is always "model".

    - `MODEL("model")`

  - `String ownedBy`

    The organization that owns the model.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.models.ModelListPage;
import com.openai.models.models.ModelListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ModelListPage page = client.models().list();
    }
}
```

## Retrieve

`Model models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/models/{model}`

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Parameters

- `ModelRetrieveParams params`

  - `Optional<String> model`

### Returns

- `class Model:`

  Describes an OpenAI model offering that can be used with the API.

  - `String id`

    The model identifier, which can be referenced in the API endpoints.

  - `long created`

    The Unix timestamp (in seconds) when the model was created.

  - `JsonValue; object_ "model"constant`

    The object type, which is always "model".

    - `MODEL("model")`

  - `String ownedBy`

    The organization that owns the model.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.models.Model;
import com.openai.models.models.ModelRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Model model = client.models().retrieve("gpt-4o-mini");
    }
}
```

## Delete

`ModelDeleted models().delete(ModelDeleteParamsparams = ModelDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/models/{model}`

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

### Parameters

- `ModelDeleteParams params`

  - `Optional<String> model`

### Returns

- `class ModelDeleted:`

  - `String id`

  - `boolean deleted`

  - `String object_`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.models.ModelDeleteParams;
import com.openai.models.models.ModelDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ModelDeleted modelDeleted = client.models().delete("ft:gpt-4o-mini:acemeco:suffix:abc123");
    }
}
```

### Domain Types

### Model

- `class Model:`

  Describes an OpenAI model offering that can be used with the API.

  - `String id`

    The model identifier, which can be referenced in the API endpoints.

  - `long created`

    The Unix timestamp (in seconds) when the model was created.

  - `JsonValue; object_ "model"constant`

    The object type, which is always "model".

    - `MODEL("model")`

  - `String ownedBy`

    The organization that owns the model.

### Model Deleted

- `class ModelDeleted:`

  - `String id`

  - `boolean deleted`

  - `String object_`
