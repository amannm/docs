# Models

## List

`models.list() -> Page<Model>`

**get** `/models`

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Returns

- `class Model`

  Describes an OpenAI model offering that can be used with the API.

  - `id: String`

    The model identifier, which can be referenced in the API endpoints.

  - `created: Integer`

    The Unix timestamp (in seconds) when the model was created.

  - `object: :model`

    The object type, which is always "model".

    - `:model`

  - `owned_by: String`

    The organization that owns the model.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.models.list

puts(page)
```

## Retrieve

`models.retrieve(model) -> Model`

**get** `/models/{model}`

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Parameters

- `model: String`

### Returns

- `class Model`

  Describes an OpenAI model offering that can be used with the API.

  - `id: String`

    The model identifier, which can be referenced in the API endpoints.

  - `created: Integer`

    The Unix timestamp (in seconds) when the model was created.

  - `object: :model`

    The object type, which is always "model".

    - `:model`

  - `owned_by: String`

    The organization that owns the model.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

model = openai.models.retrieve("gpt-4o-mini")

puts(model)
```

## Delete

`models.delete(model) -> ModelDeleted`

**delete** `/models/{model}`

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

### Parameters

- `model: String`

### Returns

- `class ModelDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

model_deleted = openai.models.delete("ft:gpt-4o-mini:acemeco:suffix:abc123")

puts(model_deleted)
```

### Domain Types

### Model

- `class Model`

  Describes an OpenAI model offering that can be used with the API.

  - `id: String`

    The model identifier, which can be referenced in the API endpoints.

  - `created: Integer`

    The Unix timestamp (in seconds) when the model was created.

  - `object: :model`

    The object type, which is always "model".

    - `:model`

  - `owned_by: String`

    The organization that owns the model.

### Model Deleted

- `class ModelDeleted`

  - `id: String`

  - `deleted: bool`

  - `object: String`
