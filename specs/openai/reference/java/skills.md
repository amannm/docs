# Skills

## Create

`Skill skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/skills`

Create a new skill.

### Parameters

- `SkillCreateParams params`

  - `Optional<Files> files`

    Skill files to upload (directory upload) or a single zip file.

    - `List<String>`

    - `String`

### Returns

- `class Skill:`

  - `String id`

    Unique identifier for the skill.

  - `long createdAt`

    Unix timestamp (seconds) for when the skill was created.

  - `String defaultVersion`

    Default version for the skill.

  - `String description`

    Description of the skill.

  - `String latestVersion`

    Latest version for the skill.

  - `String name`

    Name of the skill.

  - `JsonValue; object_ "skill"constant`

    The object type, which is `skill`.

    - `SKILL("skill")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.Skill;
import com.openai.models.skills.SkillCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Skill skill = client.skills().create();
    }
}
```

## List

`SkillListPage skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/skills`

List all skills for the current project.

### Parameters

- `SkillListParams params`

  - `Optional<String> after`

    Identifier for the last item from the previous pagination request

  - `Optional<Long> limit`

    Number of items to retrieve

  - `Optional<Order> order`

    Sort order of results by timestamp. Use `asc` for ascending order or `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

### Returns

- `class Skill:`

  - `String id`

    Unique identifier for the skill.

  - `long createdAt`

    Unix timestamp (seconds) for when the skill was created.

  - `String defaultVersion`

    Default version for the skill.

  - `String description`

    Description of the skill.

  - `String latestVersion`

    Latest version for the skill.

  - `String name`

    Name of the skill.

  - `JsonValue; object_ "skill"constant`

    The object type, which is `skill`.

    - `SKILL("skill")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.SkillListPage;
import com.openai.models.skills.SkillListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SkillListPage page = client.skills().list();
    }
}
```

## Retrieve

`Skill skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/skills/{skill_id}`

Get a skill by its ID.

### Parameters

- `SkillRetrieveParams params`

  - `Optional<String> skillId`

### Returns

- `class Skill:`

  - `String id`

    Unique identifier for the skill.

  - `long createdAt`

    Unix timestamp (seconds) for when the skill was created.

  - `String defaultVersion`

    Default version for the skill.

  - `String description`

    Description of the skill.

  - `String latestVersion`

    Latest version for the skill.

  - `String name`

    Name of the skill.

  - `JsonValue; object_ "skill"constant`

    The object type, which is `skill`.

    - `SKILL("skill")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.Skill;
import com.openai.models.skills.SkillRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Skill skill = client.skills().retrieve("skill_123");
    }
}
```

## Update

`Skill skills().update(SkillUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/skills/{skill_id}`

Update the default version pointer for a skill.

### Parameters

- `SkillUpdateParams params`

  - `Optional<String> skillId`

  - `String defaultVersion`

    The skill version number to set as default.

### Returns

- `class Skill:`

  - `String id`

    Unique identifier for the skill.

  - `long createdAt`

    Unix timestamp (seconds) for when the skill was created.

  - `String defaultVersion`

    Default version for the skill.

  - `String description`

    Description of the skill.

  - `String latestVersion`

    Latest version for the skill.

  - `String name`

    Name of the skill.

  - `JsonValue; object_ "skill"constant`

    The object type, which is `skill`.

    - `SKILL("skill")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.Skill;
import com.openai.models.skills.SkillUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SkillUpdateParams params = SkillUpdateParams.builder()
            .skillId("skill_123")
            .defaultVersion("default_version")
            .build();
        Skill skill = client.skills().update(params);
    }
}
```

## Delete

`DeletedSkill skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/skills/{skill_id}`

Delete a skill by its ID.

### Parameters

- `SkillDeleteParams params`

  - `Optional<String> skillId`

### Returns

- `class DeletedSkill:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "skill.deleted"constant`

    - `SKILL_DELETED("skill.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.DeletedSkill;
import com.openai.models.skills.SkillDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        DeletedSkill deletedSkill = client.skills().delete("skill_123");
    }
}
```

### Domain Types

### Deleted Skill

- `class DeletedSkill:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "skill.deleted"constant`

    - `SKILL_DELETED("skill.deleted")`

### Skill

- `class Skill:`

  - `String id`

    Unique identifier for the skill.

  - `long createdAt`

    Unix timestamp (seconds) for when the skill was created.

  - `String defaultVersion`

    Default version for the skill.

  - `String description`

    Description of the skill.

  - `String latestVersion`

    Latest version for the skill.

  - `String name`

    Name of the skill.

  - `JsonValue; object_ "skill"constant`

    The object type, which is `skill`.

    - `SKILL("skill")`

### Skill List

- `class SkillList:`

  - `List<Skill> data`

    A list of items

    - `String id`

      Unique identifier for the skill.

    - `long createdAt`

      Unix timestamp (seconds) for when the skill was created.

    - `String defaultVersion`

      Default version for the skill.

    - `String description`

      Description of the skill.

    - `String latestVersion`

      Latest version for the skill.

    - `String name`

      Name of the skill.

    - `JsonValue; object_ "skill"constant`

      The object type, which is `skill`.

      - `SKILL("skill")`

  - `Optional<String> firstId`

    The ID of the first item in the list.

  - `boolean hasMore`

    Whether there are more items available.

  - `Optional<String> lastId`

    The ID of the last item in the list.

  - `JsonValue; object_ "list"constant`

    The type of object returned, must be `list`.

    - `LIST("list")`

## Content

### Retrieve

`HttpResponse skills().content().retrieve(ContentRetrieveParamsparams = ContentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/skills/{skill_id}/content`

Download a skill zip bundle by its ID.

#### Parameters

- `ContentRetrieveParams params`

  - `Optional<String> skillId`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.skills.content.ContentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse content = client.skills().content().retrieve("skill_123");
    }
}
```

## Versions

### Create

`SkillVersion skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/skills/{skill_id}/versions`

Create a new immutable skill version.

#### Parameters

- `VersionCreateParams params`

  - `Optional<String> skillId`

  - `Optional<Boolean> default_`

    Whether to set this version as the default.

  - `Optional<Files> files`

    Skill files to upload (directory upload) or a single zip file.

    - `List<String>`

    - `String`

#### Returns

- `class SkillVersion:`

  - `String id`

    Unique identifier for the skill version.

  - `long createdAt`

    Unix timestamp (seconds) for when the version was created.

  - `String description`

    Description of the skill version.

  - `String name`

    Name of the skill version.

  - `JsonValue; object_ "skill.version"constant`

    The object type, which is `skill.version`.

    - `SKILL_VERSION("skill.version")`

  - `String skillId`

    Identifier of the skill for this version.

  - `String version`

    Version number for this skill.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.versions.SkillVersion;
import com.openai.models.skills.versions.VersionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SkillVersion skillVersion = client.skills().versions().create("skill_123");
    }
}
```

### List

`VersionListPage skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/skills/{skill_id}/versions`

List skill versions for a skill.

#### Parameters

- `VersionListParams params`

  - `Optional<String> skillId`

  - `Optional<String> after`

    The skill version ID to start after.

  - `Optional<Long> limit`

    Number of versions to retrieve.

  - `Optional<Order> order`

    Sort order of results by version number.

    - `ASC("asc")`

    - `DESC("desc")`

#### Returns

- `class SkillVersion:`

  - `String id`

    Unique identifier for the skill version.

  - `long createdAt`

    Unix timestamp (seconds) for when the version was created.

  - `String description`

    Description of the skill version.

  - `String name`

    Name of the skill version.

  - `JsonValue; object_ "skill.version"constant`

    The object type, which is `skill.version`.

    - `SKILL_VERSION("skill.version")`

  - `String skillId`

    Identifier of the skill for this version.

  - `String version`

    Version number for this skill.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.versions.VersionListPage;
import com.openai.models.skills.versions.VersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VersionListPage page = client.skills().versions().list("skill_123");
    }
}
```

### Retrieve

`SkillVersion skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/skills/{skill_id}/versions/{version}`

Get a specific skill version.

#### Parameters

- `VersionRetrieveParams params`

  - `String skillId`

  - `Optional<String> version`

    The version number to retrieve.

#### Returns

- `class SkillVersion:`

  - `String id`

    Unique identifier for the skill version.

  - `long createdAt`

    Unix timestamp (seconds) for when the version was created.

  - `String description`

    Description of the skill version.

  - `String name`

    Name of the skill version.

  - `JsonValue; object_ "skill.version"constant`

    The object type, which is `skill.version`.

    - `SKILL_VERSION("skill.version")`

  - `String skillId`

    Identifier of the skill for this version.

  - `String version`

    Version number for this skill.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.versions.SkillVersion;
import com.openai.models.skills.versions.VersionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VersionRetrieveParams params = VersionRetrieveParams.builder()
            .skillId("skill_123")
            .version("version")
            .build();
        SkillVersion skillVersion = client.skills().versions().retrieve(params);
    }
}
```

### Delete

`DeletedSkillVersion skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/skills/{skill_id}/versions/{version}`

Delete a skill version.

#### Parameters

- `VersionDeleteParams params`

  - `String skillId`

  - `Optional<String> version`

    The skill version number.

#### Returns

- `class DeletedSkillVersion:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "skill.version.deleted"constant`

    - `SKILL_VERSION_DELETED("skill.version.deleted")`

  - `String version`

    The deleted skill version.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.skills.versions.DeletedSkillVersion;
import com.openai.models.skills.versions.VersionDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VersionDeleteParams params = VersionDeleteParams.builder()
            .skillId("skill_123")
            .version("version")
            .build();
        DeletedSkillVersion deletedSkillVersion = client.skills().versions().delete(params);
    }
}
```

#### Domain Types

#### Deleted Skill Version

- `class DeletedSkillVersion:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "skill.version.deleted"constant`

    - `SKILL_VERSION_DELETED("skill.version.deleted")`

  - `String version`

    The deleted skill version.

#### Skill Version

- `class SkillVersion:`

  - `String id`

    Unique identifier for the skill version.

  - `long createdAt`

    Unix timestamp (seconds) for when the version was created.

  - `String description`

    Description of the skill version.

  - `String name`

    Name of the skill version.

  - `JsonValue; object_ "skill.version"constant`

    The object type, which is `skill.version`.

    - `SKILL_VERSION("skill.version")`

  - `String skillId`

    Identifier of the skill for this version.

  - `String version`

    Version number for this skill.

#### Skill Version List

- `class SkillVersionList:`

  - `List<SkillVersion> data`

    A list of items

    - `String id`

      Unique identifier for the skill version.

    - `long createdAt`

      Unix timestamp (seconds) for when the version was created.

    - `String description`

      Description of the skill version.

    - `String name`

      Name of the skill version.

    - `JsonValue; object_ "skill.version"constant`

      The object type, which is `skill.version`.

      - `SKILL_VERSION("skill.version")`

    - `String skillId`

      Identifier of the skill for this version.

    - `String version`

      Version number for this skill.

  - `Optional<String> firstId`

    The ID of the first item in the list.

  - `boolean hasMore`

    Whether there are more items available.

  - `Optional<String> lastId`

    The ID of the last item in the list.

  - `JsonValue; object_ "list"constant`

    The type of object returned, must be `list`.

    - `LIST("list")`

### Content

#### Retrieve

`HttpResponse skills().versions().content().retrieve(ContentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/skills/{skill_id}/versions/{version}/content`

Download a skill version zip bundle.

##### Parameters

- `ContentRetrieveParams params`

  - `String skillId`

  - `Optional<String> version`

    The skill version number.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.skills.versions.content.ContentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContentRetrieveParams params = ContentRetrieveParams.builder()
            .skillId("skill_123")
            .version("version")
            .build();
        HttpResponse content = client.skills().versions().content().retrieve(params);
    }
}
```
