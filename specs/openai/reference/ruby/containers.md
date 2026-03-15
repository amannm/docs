# Containers

## List

`containers.list(**kwargs) -> CursorPage<ContainerListResponse>`

**get** `/containers`

List Containers

### Parameters

- `after: String`

  A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- `limit: Integer`

  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- `name: String`

  Filter results by container name.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

  - `:asc`

  - `:desc`

### Returns

- `class ContainerListResponse`

  - `id: String`

    Unique identifier for the container.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the container was created.

  - `name: String`

    Name of the container.

  - `object: String`

    The type of this object.

  - `status: String`

    Status of the container (e.g., active, deleted).

  - `expires_after: { anchor, minutes}`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `anchor: :last_active_at`

      The reference point for the expiration.

      - `:last_active_at`

    - `minutes: Integer`

      The number of minutes after the anchor before the container expires.

  - `last_active_at: Integer`

    Unix timestamp (in seconds) when the container was last active.

  - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

    The memory limit configured for the container.

    - `:"1g"`

    - `:"4g"`

    - `:"16g"`

    - `:"64g"`

  - `network_policy: { type, allowed_domains}`

    Network access policy for the container.

    - `type: :allowlist | :disabled`

      The network policy mode.

      - `:allowlist`

      - `:disabled`

    - `allowed_domains: Array[String]`

      Allowed outbound domains when `type` is `allowlist`.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.containers.list

puts(page)
```

## Create

`containers.create(**kwargs) -> ContainerCreateResponse`

**post** `/containers`

Create Container

### Parameters

- `name: String`

  Name of the container to create.

- `expires_after: { anchor, minutes}`

  Container expiration time in seconds relative to the 'anchor' time.

  - `anchor: :last_active_at`

    Time anchor for the expiration time. Currently only 'last_active_at' is supported.

    - `:last_active_at`

  - `minutes: Integer`

- `file_ids: Array[String]`

  IDs of files to copy to the container.

- `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

  Optional memory limit for the container. Defaults to "1g".

  - `:"1g"`

  - `:"4g"`

  - `:"16g"`

  - `:"64g"`

- `network_policy: ContainerNetworkPolicyDisabled | ContainerNetworkPolicyAllowlist`

  Network access policy for the container.

  - `class ContainerNetworkPolicyDisabled`

    - `type: :disabled`

      Disable outbound network access. Always `disabled`.

      - `:disabled`

  - `class ContainerNetworkPolicyAllowlist`

    - `allowed_domains: Array[String]`

      A list of allowed domains when type is `allowlist`.

    - `type: :allowlist`

      Allow outbound network access only to specified domains. Always `allowlist`.

      - `:allowlist`

    - `domain_secrets: Array[ContainerNetworkPolicyDomainSecret]`

      Optional domain-scoped secrets for allowlisted domains.

      - `domain: String`

        The domain associated with the secret.

      - `name: String`

        The name of the secret to inject for the domain.

      - `value: String`

        The secret value to inject for the domain.

- `skills: Array[SkillReference | InlineSkill]`

  An optional list of skills referenced by id or inline data.

  - `class SkillReference`

    - `skill_id: String`

      The ID of the referenced skill.

    - `type: :skill_reference`

      References a skill created with the /v1/skills endpoint.

      - `:skill_reference`

    - `version: String`

      Optional skill version. Use a positive integer or 'latest'. Omit for default.

  - `class InlineSkill`

    - `description: String`

      The description of the skill.

    - `name: String`

      The name of the skill.

    - `source: InlineSkillSource`

      Inline skill payload

      - `data: String`

        Base64-encoded skill zip bundle.

      - `media_type: :"application/zip"`

        The media type of the inline skill payload. Must be `application/zip`.

        - `:"application/zip"`

      - `type: :base64`

        The type of the inline skill source. Must be `base64`.

        - `:base64`

    - `type: :inline`

      Defines an inline skill for this request.

      - `:inline`

### Returns

- `class ContainerCreateResponse`

  - `id: String`

    Unique identifier for the container.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the container was created.

  - `name: String`

    Name of the container.

  - `object: String`

    The type of this object.

  - `status: String`

    Status of the container (e.g., active, deleted).

  - `expires_after: { anchor, minutes}`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `anchor: :last_active_at`

      The reference point for the expiration.

      - `:last_active_at`

    - `minutes: Integer`

      The number of minutes after the anchor before the container expires.

  - `last_active_at: Integer`

    Unix timestamp (in seconds) when the container was last active.

  - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

    The memory limit configured for the container.

    - `:"1g"`

    - `:"4g"`

    - `:"16g"`

    - `:"64g"`

  - `network_policy: { type, allowed_domains}`

    Network access policy for the container.

    - `type: :allowlist | :disabled`

      The network policy mode.

      - `:allowlist`

      - `:disabled`

    - `allowed_domains: Array[String]`

      Allowed outbound domains when `type` is `allowlist`.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

container = openai.containers.create(name: "name")

puts(container)
```

## Retrieve

`containers.retrieve(container_id) -> ContainerRetrieveResponse`

**get** `/containers/{container_id}`

Retrieve Container

### Parameters

- `container_id: String`

### Returns

- `class ContainerRetrieveResponse`

  - `id: String`

    Unique identifier for the container.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the container was created.

  - `name: String`

    Name of the container.

  - `object: String`

    The type of this object.

  - `status: String`

    Status of the container (e.g., active, deleted).

  - `expires_after: { anchor, minutes}`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `anchor: :last_active_at`

      The reference point for the expiration.

      - `:last_active_at`

    - `minutes: Integer`

      The number of minutes after the anchor before the container expires.

  - `last_active_at: Integer`

    Unix timestamp (in seconds) when the container was last active.

  - `memory_limit: :"1g" | :"4g" | :"16g" | :"64g"`

    The memory limit configured for the container.

    - `:"1g"`

    - `:"4g"`

    - `:"16g"`

    - `:"64g"`

  - `network_policy: { type, allowed_domains}`

    Network access policy for the container.

    - `type: :allowlist | :disabled`

      The network policy mode.

      - `:allowlist`

      - `:disabled`

    - `allowed_domains: Array[String]`

      Allowed outbound domains when `type` is `allowlist`.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

container = openai.containers.retrieve("container_id")

puts(container)
```

## Delete

`containers.delete(container_id) -> void`

**delete** `/containers/{container_id}`

Delete Container

### Parameters

- `container_id: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.containers.delete("container_id")

puts(result)
```

## Files

### List

`containers.files.list(container_id, **kwargs) -> CursorPage<FileListResponse>`

**get** `/containers/{container_id}/files`

List Container files

#### Parameters

- `container_id: String`

- `after: String`

  A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

- `limit: Integer`

  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

  - `:asc`

  - `:desc`

#### Returns

- `class FileListResponse`

  - `id: String`

    Unique identifier for the file.

  - `bytes: Integer`

    Size of the file in bytes.

  - `container_id: String`

    The container this file belongs to.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the file was created.

  - `object: :"container.file"`

    The type of this object (`container.file`).

    - `:"container.file"`

  - `path: String`

    Path of the file in the container.

  - `source: String`

    Source of the file (e.g., `user`, `assistant`).

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.containers.files.list("container_id")

puts(page)
```

### Create

`containers.files.create(container_id, **kwargs) -> FileCreateResponse`

**post** `/containers/{container_id}/files`

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

#### Parameters

- `container_id: String`

- `file: String`

  The File object (not file name) to be uploaded.

- `file_id: String`

  Name of the file to create.

#### Returns

- `class FileCreateResponse`

  - `id: String`

    Unique identifier for the file.

  - `bytes: Integer`

    Size of the file in bytes.

  - `container_id: String`

    The container this file belongs to.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the file was created.

  - `object: :"container.file"`

    The type of this object (`container.file`).

    - `:"container.file"`

  - `path: String`

    Path of the file in the container.

  - `source: String`

    Source of the file (e.g., `user`, `assistant`).

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

file = openai.containers.files.create("container_id")

puts(file)
```

### Retrieve

`containers.files.retrieve(file_id, **kwargs) -> FileRetrieveResponse`

**get** `/containers/{container_id}/files/{file_id}`

Retrieve Container File

#### Parameters

- `container_id: String`

- `file_id: String`

#### Returns

- `class FileRetrieveResponse`

  - `id: String`

    Unique identifier for the file.

  - `bytes: Integer`

    Size of the file in bytes.

  - `container_id: String`

    The container this file belongs to.

  - `created_at: Integer`

    Unix timestamp (in seconds) when the file was created.

  - `object: :"container.file"`

    The type of this object (`container.file`).

    - `:"container.file"`

  - `path: String`

    Path of the file in the container.

  - `source: String`

    Source of the file (e.g., `user`, `assistant`).

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

file = openai.containers.files.retrieve("file_id", container_id: "container_id")

puts(file)
```

### Delete

`containers.files.delete(file_id, **kwargs) -> void`

**delete** `/containers/{container_id}/files/{file_id}`

Delete Container File

#### Parameters

- `container_id: String`

- `file_id: String`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.containers.files.delete("file_id", container_id: "container_id")

puts(result)
```

### Content

#### Retrieve

`containers.files.content.retrieve(file_id, **kwargs) -> StringIO`

**get** `/containers/{container_id}/files/{file_id}/content`

Retrieve Container File Content

##### Parameters

- `container_id: String`

- `file_id: String`

##### Returns

- `StringIO`

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

content = openai.containers.files.content.retrieve("file_id", container_id: "container_id")

puts(content)
```
