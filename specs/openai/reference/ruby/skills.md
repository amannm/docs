# Skills

## Create

`skills.create(**kwargs) -> Skill`

**post** `/skills`

Create a new skill.

### Parameters

- `files: Array[String] | String`

  Skill files to upload (directory upload) or a single zip file.

  - `Array[String]`

    Skill files to upload (directory upload) or a single zip file.

  - `String`

    Skill zip file to upload.

### Returns

- `class Skill`

  - `id: String`

    Unique identifier for the skill.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the skill was created.

  - `default_version: String`

    Default version for the skill.

  - `description: String`

    Description of the skill.

  - `latest_version: String`

    Latest version for the skill.

  - `name: String`

    Name of the skill.

  - `object: :skill`

    The object type, which is `skill`.

    - `:skill`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

skill = openai.skills.create

puts(skill)
```

## List

`skills.list(**kwargs) -> CursorPage<Skill>`

**get** `/skills`

List all skills for the current project.

### Parameters

- `after: String`

  Identifier for the last item from the previous pagination request

- `limit: Integer`

  Number of items to retrieve

- `order: :asc | :desc`

  Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

  - `:asc`

  - `:desc`

### Returns

- `class Skill`

  - `id: String`

    Unique identifier for the skill.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the skill was created.

  - `default_version: String`

    Default version for the skill.

  - `description: String`

    Description of the skill.

  - `latest_version: String`

    Latest version for the skill.

  - `name: String`

    Name of the skill.

  - `object: :skill`

    The object type, which is `skill`.

    - `:skill`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.skills.list

puts(page)
```

## Retrieve

`skills.retrieve(skill_id) -> Skill`

**get** `/skills/{skill_id}`

Get a skill by its ID.

### Parameters

- `skill_id: String`

### Returns

- `class Skill`

  - `id: String`

    Unique identifier for the skill.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the skill was created.

  - `default_version: String`

    Default version for the skill.

  - `description: String`

    Description of the skill.

  - `latest_version: String`

    Latest version for the skill.

  - `name: String`

    Name of the skill.

  - `object: :skill`

    The object type, which is `skill`.

    - `:skill`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

skill = openai.skills.retrieve("skill_123")

puts(skill)
```

## Update

`skills.update(skill_id, **kwargs) -> Skill`

**post** `/skills/{skill_id}`

Update the default version pointer for a skill.

### Parameters

- `skill_id: String`

- `default_version: String`

  The skill version number to set as default.

### Returns

- `class Skill`

  - `id: String`

    Unique identifier for the skill.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the skill was created.

  - `default_version: String`

    Default version for the skill.

  - `description: String`

    Description of the skill.

  - `latest_version: String`

    Latest version for the skill.

  - `name: String`

    Name of the skill.

  - `object: :skill`

    The object type, which is `skill`.

    - `:skill`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

skill = openai.skills.update("skill_123", default_version: "default_version")

puts(skill)
```

## Delete

`skills.delete(skill_id) -> DeletedSkill`

**delete** `/skills/{skill_id}`

Delete a skill by its ID.

### Parameters

- `skill_id: String`

### Returns

- `class DeletedSkill`

  - `id: String`

  - `deleted: bool`

  - `object: :"skill.deleted"`

    - `:"skill.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

deleted_skill = openai.skills.delete("skill_123")

puts(deleted_skill)
```

### Domain Types

### Deleted Skill

- `class DeletedSkill`

  - `id: String`

  - `deleted: bool`

  - `object: :"skill.deleted"`

    - `:"skill.deleted"`

### Skill

- `class Skill`

  - `id: String`

    Unique identifier for the skill.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the skill was created.

  - `default_version: String`

    Default version for the skill.

  - `description: String`

    Description of the skill.

  - `latest_version: String`

    Latest version for the skill.

  - `name: String`

    Name of the skill.

  - `object: :skill`

    The object type, which is `skill`.

    - `:skill`

### Skill List

- `class SkillList`

  - `data: Array[Skill]`

    A list of items

    - `id: String`

      Unique identifier for the skill.

    - `created_at: Integer`

      Unix timestamp (seconds) for when the skill was created.

    - `default_version: String`

      Default version for the skill.

    - `description: String`

      Description of the skill.

    - `latest_version: String`

      Latest version for the skill.

    - `name: String`

      Name of the skill.

    - `object: :skill`

      The object type, which is `skill`.

      - `:skill`

  - `first_id: String`

    The ID of the first item in the list.

  - `has_more: bool`

    Whether there are more items available.

  - `last_id: String`

    The ID of the last item in the list.

  - `object: :list`

    The type of object returned, must be `list`.

    - `:list`

## Content

### Retrieve

`skills.content.retrieve(skill_id) -> StringIO`

**get** `/skills/{skill_id}/content`

Download a skill zip bundle by its ID.

#### Parameters

- `skill_id: String`

#### Returns

- `StringIO`

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

content = openai.skills.content.retrieve("skill_123")

puts(content)
```

## Versions

### Create

`skills.versions.create(skill_id, **kwargs) -> SkillVersion`

**post** `/skills/{skill_id}/versions`

Create a new immutable skill version.

#### Parameters

- `skill_id: String`

- `default: bool`

  Whether to set this version as the default.

- `files: Array[String] | String`

  Skill files to upload (directory upload) or a single zip file.

  - `Array[String]`

    Skill files to upload (directory upload) or a single zip file.

  - `String`

    Skill zip file to upload.

#### Returns

- `class SkillVersion`

  - `id: String`

    Unique identifier for the skill version.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the version was created.

  - `description: String`

    Description of the skill version.

  - `name: String`

    Name of the skill version.

  - `object: :"skill.version"`

    The object type, which is `skill.version`.

    - `:"skill.version"`

  - `skill_id: String`

    Identifier of the skill for this version.

  - `version: String`

    Version number for this skill.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

skill_version = openai.skills.versions.create("skill_123")

puts(skill_version)
```

### List

`skills.versions.list(skill_id, **kwargs) -> CursorPage<SkillVersion>`

**get** `/skills/{skill_id}/versions`

List skill versions for a skill.

#### Parameters

- `skill_id: String`

- `after: String`

  The skill version ID to start after.

- `limit: Integer`

  Number of versions to retrieve.

- `order: :asc | :desc`

  Sort order of results by version number.

  - `:asc`

  - `:desc`

#### Returns

- `class SkillVersion`

  - `id: String`

    Unique identifier for the skill version.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the version was created.

  - `description: String`

    Description of the skill version.

  - `name: String`

    Name of the skill version.

  - `object: :"skill.version"`

    The object type, which is `skill.version`.

    - `:"skill.version"`

  - `skill_id: String`

    Identifier of the skill for this version.

  - `version: String`

    Version number for this skill.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.skills.versions.list("skill_123")

puts(page)
```

### Retrieve

`skills.versions.retrieve(version, **kwargs) -> SkillVersion`

**get** `/skills/{skill_id}/versions/{version}`

Get a specific skill version.

#### Parameters

- `skill_id: String`

- `version: String`

  The version number to retrieve.

#### Returns

- `class SkillVersion`

  - `id: String`

    Unique identifier for the skill version.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the version was created.

  - `description: String`

    Description of the skill version.

  - `name: String`

    Name of the skill version.

  - `object: :"skill.version"`

    The object type, which is `skill.version`.

    - `:"skill.version"`

  - `skill_id: String`

    Identifier of the skill for this version.

  - `version: String`

    Version number for this skill.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

skill_version = openai.skills.versions.retrieve("version", skill_id: "skill_123")

puts(skill_version)
```

### Delete

`skills.versions.delete(version, **kwargs) -> DeletedSkillVersion`

**delete** `/skills/{skill_id}/versions/{version}`

Delete a skill version.

#### Parameters

- `skill_id: String`

- `version: String`

  The skill version number.

#### Returns

- `class DeletedSkillVersion`

  - `id: String`

  - `deleted: bool`

  - `object: :"skill.version.deleted"`

    - `:"skill.version.deleted"`

  - `version: String`

    The deleted skill version.

#### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

deleted_skill_version = openai.skills.versions.delete("version", skill_id: "skill_123")

puts(deleted_skill_version)
```

#### Domain Types

#### Deleted Skill Version

- `class DeletedSkillVersion`

  - `id: String`

  - `deleted: bool`

  - `object: :"skill.version.deleted"`

    - `:"skill.version.deleted"`

  - `version: String`

    The deleted skill version.

#### Skill Version

- `class SkillVersion`

  - `id: String`

    Unique identifier for the skill version.

  - `created_at: Integer`

    Unix timestamp (seconds) for when the version was created.

  - `description: String`

    Description of the skill version.

  - `name: String`

    Name of the skill version.

  - `object: :"skill.version"`

    The object type, which is `skill.version`.

    - `:"skill.version"`

  - `skill_id: String`

    Identifier of the skill for this version.

  - `version: String`

    Version number for this skill.

#### Skill Version List

- `class SkillVersionList`

  - `data: Array[SkillVersion]`

    A list of items

    - `id: String`

      Unique identifier for the skill version.

    - `created_at: Integer`

      Unix timestamp (seconds) for when the version was created.

    - `description: String`

      Description of the skill version.

    - `name: String`

      Name of the skill version.

    - `object: :"skill.version"`

      The object type, which is `skill.version`.

      - `:"skill.version"`

    - `skill_id: String`

      Identifier of the skill for this version.

    - `version: String`

      Version number for this skill.

  - `first_id: String`

    The ID of the first item in the list.

  - `has_more: bool`

    Whether there are more items available.

  - `last_id: String`

    The ID of the last item in the list.

  - `object: :list`

    The type of object returned, must be `list`.

    - `:list`

### Content

#### Retrieve

`skills.versions.content.retrieve(version, **kwargs) -> StringIO`

**get** `/skills/{skill_id}/versions/{version}/content`

Download a skill version zip bundle.

##### Parameters

- `skill_id: String`

- `version: String`

  The skill version number.

##### Returns

- `StringIO`

##### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

content = openai.skills.versions.content.retrieve("version", skill_id: "skill_123")

puts(content)
```
