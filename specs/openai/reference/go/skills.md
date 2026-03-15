# Skills

## Create

`client.Skills.New(ctx, body) (*Skill, error)`

**post** `/skills`

Create a new skill.

### Parameters

- `body SkillNewParams`

  - `Files param.Field[SkillNewParamsFilesUnion]`

    Skill files to upload (directory upload) or a single zip file.

    - `type SkillNewParamsFilesArray []Reader`

      Skill files to upload (directory upload) or a single zip file.

    - `Reader`

### Returns

- `type Skill struct{…}`

  - `ID string`

    Unique identifier for the skill.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the skill was created.

  - `DefaultVersion string`

    Default version for the skill.

  - `Description string`

    Description of the skill.

  - `LatestVersion string`

    Latest version for the skill.

  - `Name string`

    Name of the skill.

  - `Object Skill`

    The object type, which is `skill`.

    - `const SkillSkill Skill = "skill"`

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
  skill, err := client.Skills.New(context.TODO(), openai.SkillNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
}
```

## List

`client.Skills.List(ctx, query) (*CursorPage[Skill], error)`

**get** `/skills`

List all skills for the current project.

### Parameters

- `query SkillListParams`

  - `After param.Field[string]`

    Identifier for the last item from the previous pagination request

  - `Limit param.Field[int64]`

    Number of items to retrieve

  - `Order param.Field[SkillListParamsOrder]`

    Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

    - `const SkillListParamsOrderAsc SkillListParamsOrder = "asc"`

    - `const SkillListParamsOrderDesc SkillListParamsOrder = "desc"`

### Returns

- `type Skill struct{…}`

  - `ID string`

    Unique identifier for the skill.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the skill was created.

  - `DefaultVersion string`

    Default version for the skill.

  - `Description string`

    Description of the skill.

  - `LatestVersion string`

    Latest version for the skill.

  - `Name string`

    Name of the skill.

  - `Object Skill`

    The object type, which is `skill`.

    - `const SkillSkill Skill = "skill"`

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
  page, err := client.Skills.List(context.TODO(), openai.SkillListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

## Retrieve

`client.Skills.Get(ctx, skillID) (*Skill, error)`

**get** `/skills/{skill_id}`

Get a skill by its ID.

### Parameters

- `skillID string`

### Returns

- `type Skill struct{…}`

  - `ID string`

    Unique identifier for the skill.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the skill was created.

  - `DefaultVersion string`

    Default version for the skill.

  - `Description string`

    Description of the skill.

  - `LatestVersion string`

    Latest version for the skill.

  - `Name string`

    Name of the skill.

  - `Object Skill`

    The object type, which is `skill`.

    - `const SkillSkill Skill = "skill"`

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
  skill, err := client.Skills.Get(context.TODO(), "skill_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
}
```

## Update

`client.Skills.Update(ctx, skillID, body) (*Skill, error)`

**post** `/skills/{skill_id}`

Update the default version pointer for a skill.

### Parameters

- `skillID string`

- `body SkillUpdateParams`

  - `DefaultVersion param.Field[string]`

    The skill version number to set as default.

### Returns

- `type Skill struct{…}`

  - `ID string`

    Unique identifier for the skill.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the skill was created.

  - `DefaultVersion string`

    Default version for the skill.

  - `Description string`

    Description of the skill.

  - `LatestVersion string`

    Latest version for the skill.

  - `Name string`

    Name of the skill.

  - `Object Skill`

    The object type, which is `skill`.

    - `const SkillSkill Skill = "skill"`

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
  skill, err := client.Skills.Update(
    context.TODO(),
    "skill_123",
    openai.SkillUpdateParams{
      DefaultVersion: "default_version",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
}
```

## Delete

`client.Skills.Delete(ctx, skillID) (*DeletedSkill, error)`

**delete** `/skills/{skill_id}`

Delete a skill by its ID.

### Parameters

- `skillID string`

### Returns

- `type DeletedSkill struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object SkillDeleted`

    - `const SkillDeletedSkillDeleted SkillDeleted = "skill.deleted"`

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
  deletedSkill, err := client.Skills.Delete(context.TODO(), "skill_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", deletedSkill.ID)
}
```

### Domain Types

### Deleted Skill

- `type DeletedSkill struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object SkillDeleted`

    - `const SkillDeletedSkillDeleted SkillDeleted = "skill.deleted"`

### Skill

- `type Skill struct{…}`

  - `ID string`

    Unique identifier for the skill.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the skill was created.

  - `DefaultVersion string`

    Default version for the skill.

  - `Description string`

    Description of the skill.

  - `LatestVersion string`

    Latest version for the skill.

  - `Name string`

    Name of the skill.

  - `Object Skill`

    The object type, which is `skill`.

    - `const SkillSkill Skill = "skill"`

### Skill List

- `type SkillList struct{…}`

  - `Data []Skill`

    A list of items

    - `ID string`

      Unique identifier for the skill.

    - `CreatedAt int64`

      Unix timestamp (seconds) for when the skill was created.

    - `DefaultVersion string`

      Default version for the skill.

    - `Description string`

      Description of the skill.

    - `LatestVersion string`

      Latest version for the skill.

    - `Name string`

      Name of the skill.

    - `Object Skill`

      The object type, which is `skill`.

      - `const SkillSkill Skill = "skill"`

  - `FirstID string`

    The ID of the first item in the list.

  - `HasMore bool`

    Whether there are more items available.

  - `LastID string`

    The ID of the last item in the list.

  - `Object List`

    The type of object returned, must be `list`.

    - `const ListList List = "list"`

## Content

### Retrieve

`client.Skills.Content.Get(ctx, skillID) (*Response, error)`

**get** `/skills/{skill_id}/content`

Download a skill zip bundle by its ID.

#### Parameters

- `skillID string`

#### Returns

- `type SkillContentGetResponse interface{…}`

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
  content, err := client.Skills.Content.Get(context.TODO(), "skill_123")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", content)
}
```

## Versions

### Create

`client.Skills.Versions.New(ctx, skillID, body) (*SkillVersion, error)`

**post** `/skills/{skill_id}/versions`

Create a new immutable skill version.

#### Parameters

- `skillID string`

- `body SkillVersionNewParams`

  - `Default param.Field[bool]`

    Whether to set this version as the default.

  - `Files param.Field[SkillVersionNewParamsFilesUnion]`

    Skill files to upload (directory upload) or a single zip file.

    - `type SkillVersionNewParamsFilesArray []Reader`

      Skill files to upload (directory upload) or a single zip file.

    - `Reader`

#### Returns

- `type SkillVersion struct{…}`

  - `ID string`

    Unique identifier for the skill version.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the version was created.

  - `Description string`

    Description of the skill version.

  - `Name string`

    Name of the skill version.

  - `Object SkillVersion`

    The object type, which is `skill.version`.

    - `const SkillVersionSkillVersion SkillVersion = "skill.version"`

  - `SkillID string`

    Identifier of the skill for this version.

  - `Version string`

    Version number for this skill.

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
  skillVersion, err := client.Skills.Versions.New(
    context.TODO(),
    "skill_123",
    openai.SkillVersionNewParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skillVersion.ID)
}
```

### List

`client.Skills.Versions.List(ctx, skillID, query) (*CursorPage[SkillVersion], error)`

**get** `/skills/{skill_id}/versions`

List skill versions for a skill.

#### Parameters

- `skillID string`

- `query SkillVersionListParams`

  - `After param.Field[string]`

    The skill version ID to start after.

  - `Limit param.Field[int64]`

    Number of versions to retrieve.

  - `Order param.Field[SkillVersionListParamsOrder]`

    Sort order of results by version number.

    - `const SkillVersionListParamsOrderAsc SkillVersionListParamsOrder = "asc"`

    - `const SkillVersionListParamsOrderDesc SkillVersionListParamsOrder = "desc"`

#### Returns

- `type SkillVersion struct{…}`

  - `ID string`

    Unique identifier for the skill version.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the version was created.

  - `Description string`

    Description of the skill version.

  - `Name string`

    Name of the skill version.

  - `Object SkillVersion`

    The object type, which is `skill.version`.

    - `const SkillVersionSkillVersion SkillVersion = "skill.version"`

  - `SkillID string`

    Identifier of the skill for this version.

  - `Version string`

    Version number for this skill.

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
  page, err := client.Skills.Versions.List(
    context.TODO(),
    "skill_123",
    openai.SkillVersionListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

### Retrieve

`client.Skills.Versions.Get(ctx, skillID, version) (*SkillVersion, error)`

**get** `/skills/{skill_id}/versions/{version}`

Get a specific skill version.

#### Parameters

- `skillID string`

- `version string`

  The version number to retrieve.

#### Returns

- `type SkillVersion struct{…}`

  - `ID string`

    Unique identifier for the skill version.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the version was created.

  - `Description string`

    Description of the skill version.

  - `Name string`

    Name of the skill version.

  - `Object SkillVersion`

    The object type, which is `skill.version`.

    - `const SkillVersionSkillVersion SkillVersion = "skill.version"`

  - `SkillID string`

    Identifier of the skill for this version.

  - `Version string`

    Version number for this skill.

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
  skillVersion, err := client.Skills.Versions.Get(
    context.TODO(),
    "skill_123",
    "version",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skillVersion.ID)
}
```

### Delete

`client.Skills.Versions.Delete(ctx, skillID, version) (*DeletedSkillVersion, error)`

**delete** `/skills/{skill_id}/versions/{version}`

Delete a skill version.

#### Parameters

- `skillID string`

- `version string`

  The skill version number.

#### Returns

- `type DeletedSkillVersion struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object SkillVersionDeleted`

    - `const SkillVersionDeletedSkillVersionDeleted SkillVersionDeleted = "skill.version.deleted"`

  - `Version string`

    The deleted skill version.

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
  deletedSkillVersion, err := client.Skills.Versions.Delete(
    context.TODO(),
    "skill_123",
    "version",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", deletedSkillVersion.ID)
}
```

#### Domain Types

#### Deleted Skill Version

- `type DeletedSkillVersion struct{…}`

  - `ID string`

  - `Deleted bool`

  - `Object SkillVersionDeleted`

    - `const SkillVersionDeletedSkillVersionDeleted SkillVersionDeleted = "skill.version.deleted"`

  - `Version string`

    The deleted skill version.

#### Skill Version

- `type SkillVersion struct{…}`

  - `ID string`

    Unique identifier for the skill version.

  - `CreatedAt int64`

    Unix timestamp (seconds) for when the version was created.

  - `Description string`

    Description of the skill version.

  - `Name string`

    Name of the skill version.

  - `Object SkillVersion`

    The object type, which is `skill.version`.

    - `const SkillVersionSkillVersion SkillVersion = "skill.version"`

  - `SkillID string`

    Identifier of the skill for this version.

  - `Version string`

    Version number for this skill.

#### Skill Version List

- `type SkillVersionList struct{…}`

  - `Data []SkillVersion`

    A list of items

    - `ID string`

      Unique identifier for the skill version.

    - `CreatedAt int64`

      Unix timestamp (seconds) for when the version was created.

    - `Description string`

      Description of the skill version.

    - `Name string`

      Name of the skill version.

    - `Object SkillVersion`

      The object type, which is `skill.version`.

      - `const SkillVersionSkillVersion SkillVersion = "skill.version"`

    - `SkillID string`

      Identifier of the skill for this version.

    - `Version string`

      Version number for this skill.

  - `FirstID string`

    The ID of the first item in the list.

  - `HasMore bool`

    Whether there are more items available.

  - `LastID string`

    The ID of the last item in the list.

  - `Object List`

    The type of object returned, must be `list`.

    - `const ListList List = "list"`

### Content

#### Retrieve

`client.Skills.Versions.Content.Get(ctx, skillID, version) (*Response, error)`

**get** `/skills/{skill_id}/versions/{version}/content`

Download a skill version zip bundle.

##### Parameters

- `skillID string`

- `version string`

  The skill version number.

##### Returns

- `type SkillVersionContentGetResponse interface{…}`

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
  content, err := client.Skills.Versions.Content.Get(
    context.TODO(),
    "skill_123",
    "version",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", content)
}
```
