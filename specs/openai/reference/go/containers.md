# Containers

## List

`client.Containers.List(ctx, query) (*CursorPage[ContainerListResponse], error)`

**get** `/containers`

List Containers

### Parameters

- `query ContainerListParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Name param.Field[string]`

    Filter results by container name.

  - `Order param.Field[ContainerListParamsOrder]`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `const ContainerListParamsOrderAsc ContainerListParamsOrder = "asc"`

    - `const ContainerListParamsOrderDesc ContainerListParamsOrder = "desc"`

### Returns

- `type ContainerListResponse struct{…}`

  - `ID string`

    Unique identifier for the container.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the container was created.

  - `Name string`

    Name of the container.

  - `Object string`

    The type of this object.

  - `Status string`

    Status of the container (e.g., active, deleted).

  - `ExpiresAfter ContainerListResponseExpiresAfter`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `Anchor string`

      The reference point for the expiration.

      - `const ContainerListResponseExpiresAfterAnchorLastActiveAt ContainerListResponseExpiresAfterAnchor = "last_active_at"`

    - `Minutes int64`

      The number of minutes after the anchor before the container expires.

  - `LastActiveAt int64`

    Unix timestamp (in seconds) when the container was last active.

  - `MemoryLimit ContainerListResponseMemoryLimit`

    The memory limit configured for the container.

    - `const ContainerListResponseMemoryLimit1g ContainerListResponseMemoryLimit = "1g"`

    - `const ContainerListResponseMemoryLimit4g ContainerListResponseMemoryLimit = "4g"`

    - `const ContainerListResponseMemoryLimit16g ContainerListResponseMemoryLimit = "16g"`

    - `const ContainerListResponseMemoryLimit64g ContainerListResponseMemoryLimit = "64g"`

  - `NetworkPolicy ContainerListResponseNetworkPolicy`

    Network access policy for the container.

    - `Type string`

      The network policy mode.

      - `const ContainerListResponseNetworkPolicyTypeAllowlist ContainerListResponseNetworkPolicyType = "allowlist"`

      - `const ContainerListResponseNetworkPolicyTypeDisabled ContainerListResponseNetworkPolicyType = "disabled"`

    - `AllowedDomains []string`

      Allowed outbound domains when `type` is `allowlist`.

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
  page, err := client.Containers.List(context.TODO(), openai.ContainerListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Create

`client.Containers.New(ctx, body) (*ContainerNewResponse, error)`

**post** `/containers`

Create Container

### Parameters

- `body ContainerNewParams`

  - `Name param.Field[string]`

    Name of the container to create.

  - `ExpiresAfter param.Field[ContainerNewParamsExpiresAfter]`

    Container expiration time in seconds relative to the 'anchor' time.

    - `Anchor string`

      Time anchor for the expiration time. Currently only 'last_active_at' is supported.

      - `const ContainerNewParamsExpiresAfterAnchorLastActiveAt ContainerNewParamsExpiresAfterAnchor = "last_active_at"`

    - `Minutes int64`

  - `FileIDs param.Field[[]string]`

    IDs of files to copy to the container.

  - `MemoryLimit param.Field[ContainerNewParamsMemoryLimit]`

    Optional memory limit for the container. Defaults to "1g".

    - `const ContainerNewParamsMemoryLimit1g ContainerNewParamsMemoryLimit = "1g"`

    - `const ContainerNewParamsMemoryLimit4g ContainerNewParamsMemoryLimit = "4g"`

    - `const ContainerNewParamsMemoryLimit16g ContainerNewParamsMemoryLimit = "16g"`

    - `const ContainerNewParamsMemoryLimit64g ContainerNewParamsMemoryLimit = "64g"`

  - `NetworkPolicy param.Field[ContainerNewParamsNetworkPolicyUnion]`

    Network access policy for the container.

    - `type ContainerNetworkPolicyDisabled struct{…}`

      - `Type Disabled`

        Disable outbound network access. Always `disabled`.

        - `const DisabledDisabled Disabled = "disabled"`

    - `type ContainerNetworkPolicyAllowlist struct{…}`

      - `AllowedDomains []string`

        A list of allowed domains when type is `allowlist`.

      - `Type Allowlist`

        Allow outbound network access only to specified domains. Always `allowlist`.

        - `const AllowlistAllowlist Allowlist = "allowlist"`

      - `DomainSecrets []ContainerNetworkPolicyDomainSecret`

        Optional domain-scoped secrets for allowlisted domains.

        - `Domain string`

          The domain associated with the secret.

        - `Name string`

          The name of the secret to inject for the domain.

        - `Value string`

          The secret value to inject for the domain.

  - `Skills param.Field[[]ContainerNewParamsSkillUnion]`

    An optional list of skills referenced by id or inline data.

    - `type SkillReference struct{…}`

      - `SkillID string`

        The ID of the referenced skill.

      - `Type SkillReference`

        References a skill created with the /v1/skills endpoint.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        Optional skill version. Use a positive integer or 'latest'. Omit for default.

    - `type InlineSkill struct{…}`

      - `Description string`

        The description of the skill.

      - `Name string`

        The name of the skill.

      - `Source InlineSkillSource`

        Inline skill payload

        - `Data string`

          Base64-encoded skill zip bundle.

        - `MediaType ApplicationZip`

          The media type of the inline skill payload. Must be `application/zip`.

          - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

        - `Type Base64`

          The type of the inline skill source. Must be `base64`.

          - `const Base64Base64 Base64 = "base64"`

      - `Type Inline`

        Defines an inline skill for this request.

        - `const InlineInline Inline = "inline"`

### Returns

- `type ContainerNewResponse struct{…}`

  - `ID string`

    Unique identifier for the container.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the container was created.

  - `Name string`

    Name of the container.

  - `Object string`

    The type of this object.

  - `Status string`

    Status of the container (e.g., active, deleted).

  - `ExpiresAfter ContainerNewResponseExpiresAfter`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `Anchor string`

      The reference point for the expiration.

      - `const ContainerNewResponseExpiresAfterAnchorLastActiveAt ContainerNewResponseExpiresAfterAnchor = "last_active_at"`

    - `Minutes int64`

      The number of minutes after the anchor before the container expires.

  - `LastActiveAt int64`

    Unix timestamp (in seconds) when the container was last active.

  - `MemoryLimit ContainerNewResponseMemoryLimit`

    The memory limit configured for the container.

    - `const ContainerNewResponseMemoryLimit1g ContainerNewResponseMemoryLimit = "1g"`

    - `const ContainerNewResponseMemoryLimit4g ContainerNewResponseMemoryLimit = "4g"`

    - `const ContainerNewResponseMemoryLimit16g ContainerNewResponseMemoryLimit = "16g"`

    - `const ContainerNewResponseMemoryLimit64g ContainerNewResponseMemoryLimit = "64g"`

  - `NetworkPolicy ContainerNewResponseNetworkPolicy`

    Network access policy for the container.

    - `Type string`

      The network policy mode.

      - `const ContainerNewResponseNetworkPolicyTypeAllowlist ContainerNewResponseNetworkPolicyType = "allowlist"`

      - `const ContainerNewResponseNetworkPolicyTypeDisabled ContainerNewResponseNetworkPolicyType = "disabled"`

    - `AllowedDomains []string`

      Allowed outbound domains when `type` is `allowlist`.

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
  container, err := client.Containers.New(context.TODO(), openai.ContainerNewParams{
    Name: "name",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", container.ID)
}
```

## Retrieve

`client.Containers.Get(ctx, containerID) (*ContainerGetResponse, error)`

**get** `/containers/{container_id}`

Retrieve Container

### Parameters

- `containerID string`

### Returns

- `type ContainerGetResponse struct{…}`

  - `ID string`

    Unique identifier for the container.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the container was created.

  - `Name string`

    Name of the container.

  - `Object string`

    The type of this object.

  - `Status string`

    Status of the container (e.g., active, deleted).

  - `ExpiresAfter ContainerGetResponseExpiresAfter`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `Anchor string`

      The reference point for the expiration.

      - `const ContainerGetResponseExpiresAfterAnchorLastActiveAt ContainerGetResponseExpiresAfterAnchor = "last_active_at"`

    - `Minutes int64`

      The number of minutes after the anchor before the container expires.

  - `LastActiveAt int64`

    Unix timestamp (in seconds) when the container was last active.

  - `MemoryLimit ContainerGetResponseMemoryLimit`

    The memory limit configured for the container.

    - `const ContainerGetResponseMemoryLimit1g ContainerGetResponseMemoryLimit = "1g"`

    - `const ContainerGetResponseMemoryLimit4g ContainerGetResponseMemoryLimit = "4g"`

    - `const ContainerGetResponseMemoryLimit16g ContainerGetResponseMemoryLimit = "16g"`

    - `const ContainerGetResponseMemoryLimit64g ContainerGetResponseMemoryLimit = "64g"`

  - `NetworkPolicy ContainerGetResponseNetworkPolicy`

    Network access policy for the container.

    - `Type string`

      The network policy mode.

      - `const ContainerGetResponseNetworkPolicyTypeAllowlist ContainerGetResponseNetworkPolicyType = "allowlist"`

      - `const ContainerGetResponseNetworkPolicyTypeDisabled ContainerGetResponseNetworkPolicyType = "disabled"`

    - `AllowedDomains []string`

      Allowed outbound domains when `type` is `allowlist`.

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
  container, err := client.Containers.Get(context.TODO(), "container_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", container.ID)
}
```

## Delete

`client.Containers.Delete(ctx, containerID) error`

**delete** `/containers/{container_id}`

Delete Container

### Parameters

- `containerID string`

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Containers.Delete(context.TODO(), "container_id")
  if err != nil {
    panic(err.Error())
  }
}
```

## Files

### List

`client.Containers.Files.List(ctx, containerID, query) (*CursorPage[ContainerFileListResponse], error)`

**get** `/containers/{container_id}/files`

List Container files

#### Parameters

- `containerID string`

- `query ContainerFileListParams`

  - `After param.Field[string]`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Limit param.Field[int64]`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Order param.Field[ContainerFileListParamsOrder]`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `const ContainerFileListParamsOrderAsc ContainerFileListParamsOrder = "asc"`

    - `const ContainerFileListParamsOrderDesc ContainerFileListParamsOrder = "desc"`

#### Returns

- `type ContainerFileListResponse struct{…}`

  - `ID string`

    Unique identifier for the file.

  - `Bytes int64`

    Size of the file in bytes.

  - `ContainerID string`

    The container this file belongs to.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the file was created.

  - `Object ContainerFile`

    The type of this object (`container.file`).

    - `const ContainerFileContainerFile ContainerFile = "container.file"`

  - `Path string`

    Path of the file in the container.

  - `Source string`

    Source of the file (e.g., `user`, `assistant`).

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
  page, err := client.Containers.Files.List(
    context.TODO(),
    "container_id",
    openai.ContainerFileListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Create

`client.Containers.Files.New(ctx, containerID, body) (*ContainerFileNewResponse, error)`

**post** `/containers/{container_id}/files`

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

#### Parameters

- `containerID string`

- `body ContainerFileNewParams`

  - `File param.Field[Reader]`

    The File object (not file name) to be uploaded.

  - `FileID param.Field[string]`

    Name of the file to create.

#### Returns

- `type ContainerFileNewResponse struct{…}`

  - `ID string`

    Unique identifier for the file.

  - `Bytes int64`

    Size of the file in bytes.

  - `ContainerID string`

    The container this file belongs to.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the file was created.

  - `Object ContainerFile`

    The type of this object (`container.file`).

    - `const ContainerFileContainerFile ContainerFile = "container.file"`

  - `Path string`

    Path of the file in the container.

  - `Source string`

    Source of the file (e.g., `user`, `assistant`).

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
  file, err := client.Containers.Files.New(
    context.TODO(),
    "container_id",
    openai.ContainerFileNewParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", file.ID)
}
```

### Retrieve

`client.Containers.Files.Get(ctx, containerID, fileID) (*ContainerFileGetResponse, error)`

**get** `/containers/{container_id}/files/{file_id}`

Retrieve Container File

#### Parameters

- `containerID string`

- `fileID string`

#### Returns

- `type ContainerFileGetResponse struct{…}`

  - `ID string`

    Unique identifier for the file.

  - `Bytes int64`

    Size of the file in bytes.

  - `ContainerID string`

    The container this file belongs to.

  - `CreatedAt int64`

    Unix timestamp (in seconds) when the file was created.

  - `Object ContainerFile`

    The type of this object (`container.file`).

    - `const ContainerFileContainerFile ContainerFile = "container.file"`

  - `Path string`

    Path of the file in the container.

  - `Source string`

    Source of the file (e.g., `user`, `assistant`).

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
  file, err := client.Containers.Files.Get(
    context.TODO(),
    "container_id",
    "file_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", file.ID)
}
```

### Delete

`client.Containers.Files.Delete(ctx, containerID, fileID) error`

**delete** `/containers/{container_id}/files/{file_id}`

Delete Container File

#### Parameters

- `containerID string`

- `fileID string`

#### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Containers.Files.Delete(
    context.TODO(),
    "container_id",
    "file_id",
  )
  if err != nil {
    panic(err.Error())
  }
}
```

### Content

#### Retrieve

`client.Containers.Files.Content.Get(ctx, containerID, fileID) (*Response, error)`

**get** `/containers/{container_id}/files/{file_id}/content`

Retrieve Container File Content

##### Parameters

- `containerID string`

- `fileID string`

##### Returns

- `type ContainerFileContentGetResponse interface{…}`

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
  content, err := client.Containers.Files.Content.Get(
    context.TODO(),
    "container_id",
    "file_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", content)
}
```
