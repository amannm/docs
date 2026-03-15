# Models

## List

`client.Models.List(ctx) (*Page[Model], error)`

**get** `/models`

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Returns

- `type Model struct{…}`

  Describes an OpenAI model offering that can be used with the API.

  - `ID string`

    The model identifier, which can be referenced in the API endpoints.

  - `Created int64`

    The Unix timestamp (in seconds) when the model was created.

  - `Object Model`

    The object type, which is always "model".

    - `const ModelModel Model = "model"`

  - `OwnedBy string`

    The organization that owns the model.

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
  page, err := client.Models.List(context.TODO())
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Models.Get(ctx, model) (*Model, error)`

**get** `/models/{model}`

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Parameters

- `model string`

### Returns

- `type Model struct{…}`

  Describes an OpenAI model offering that can be used with the API.

  - `ID string`

    The model identifier, which can be referenced in the API endpoints.

  - `Created int64`

    The Unix timestamp (in seconds) when the model was created.

  - `Object Model`

    The object type, which is always "model".

    - `const ModelModel Model = "model"`

  - `OwnedBy string`

    The organization that owns the model.

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
  model, err := client.Models.Get(context.TODO(), "gpt-4o-mini")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", model.ID)
}
```

## Delete

`client.Models.Delete(ctx, model) (*ModelDeleted, error)`

**delete** `/models/{model}`

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

### Parameters

- `model string`

### Returns

- `type ModelDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object string`

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
  modelDeleted, err := client.Models.Delete(context.TODO(), "ft:gpt-4o-mini:acemeco:suffix:abc123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", modelDeleted.ID)
}
```

### Domain Types

### Model

- `type Model struct{…}`

  Describes an OpenAI model offering that can be used with the API.

  - `ID string`

    The model identifier, which can be referenced in the API endpoints.

  - `Created int64`

    The Unix timestamp (in seconds) when the model was created.

  - `Object Model`

    The object type, which is always "model".

    - `const ModelModel Model = "model"`

  - `OwnedBy string`

    The organization that owns the model.

### Model Deleted

- `type ModelDeleted struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object string`
