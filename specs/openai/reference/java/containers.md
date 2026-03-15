# Containers

## List

`ContainerListPage containers().list(ContainerListParamsparams = ContainerListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/containers`

List Containers

### Parameters

- `ContainerListParams params`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<String> name`

    Filter results by container name.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

### Returns

- `class ContainerListResponse:`

  - `String id`

    Unique identifier for the container.

  - `long createdAt`

    Unix timestamp (in seconds) when the container was created.

  - `String name`

    Name of the container.

  - `String object_`

    The type of this object.

  - `String status`

    Status of the container (e.g., active, deleted).

  - `Optional<ExpiresAfter> expiresAfter`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `Optional<Anchor> anchor`

      The reference point for the expiration.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `Optional<Long> minutes`

      The number of minutes after the anchor before the container expires.

  - `Optional<Long> lastActiveAt`

    Unix timestamp (in seconds) when the container was last active.

  - `Optional<MemoryLimit> memoryLimit`

    The memory limit configured for the container.

    - `_1G("1g")`

    - `_4G("4g")`

    - `_16G("16g")`

    - `_64G("64g")`

  - `Optional<NetworkPolicy> networkPolicy`

    Network access policy for the container.

    - `Type type`

      The network policy mode.

      - `ALLOWLIST("allowlist")`

      - `DISABLED("disabled")`

    - `Optional<List<String>> allowedDomains`

      Allowed outbound domains when `type` is `allowlist`.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.ContainerListPage;
import com.openai.models.containers.ContainerListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContainerListPage page = client.containers().list();
    }
}
```

## Create

`ContainerCreateResponse containers().create(ContainerCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/containers`

Create Container

### Parameters

- `ContainerCreateParams params`

  - `String name`

    Name of the container to create.

  - `Optional<ExpiresAfter> expiresAfter`

    Container expiration time in seconds relative to the 'anchor' time.

    - `Anchor anchor`

      Time anchor for the expiration time. Currently only 'last_active_at' is supported.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `long minutes`

  - `Optional<List<String>> fileIds`

    IDs of files to copy to the container.

  - `Optional<MemoryLimit> memoryLimit`

    Optional memory limit for the container. Defaults to "1g".

    - `_1G("1g")`

    - `_4G("4g")`

    - `_16G("16g")`

    - `_64G("64g")`

  - `Optional<NetworkPolicy> networkPolicy`

    Network access policy for the container.

    - `class ContainerNetworkPolicyDisabled:`

      - `JsonValue; type "disabled"constant`

        Disable outbound network access. Always `disabled`.

        - `DISABLED("disabled")`

    - `class ContainerNetworkPolicyAllowlist:`

      - `List<String> allowedDomains`

        A list of allowed domains when type is `allowlist`.

      - `JsonValue; type "allowlist"constant`

        Allow outbound network access only to specified domains. Always `allowlist`.

        - `ALLOWLIST("allowlist")`

      - `Optional<List<ContainerNetworkPolicyDomainSecret>> domainSecrets`

        Optional domain-scoped secrets for allowlisted domains.

        - `String domain`

          The domain associated with the secret.

        - `String name`

          The name of the secret to inject for the domain.

        - `String value`

          The secret value to inject for the domain.

  - `Optional<List<Skill>> skills`

    An optional list of skills referenced by id or inline data.

    - `class SkillReference:`

      - `String skillId`

        The ID of the referenced skill.

      - `JsonValue; type "skill_reference"constant`

        References a skill created with the /v1/skills endpoint.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        Optional skill version. Use a positive integer or 'latest'. Omit for default.

    - `class InlineSkill:`

      - `String description`

        The description of the skill.

      - `String name`

        The name of the skill.

      - `InlineSkillSource source`

        Inline skill payload

        - `String data`

          Base64-encoded skill zip bundle.

        - `JsonValue; mediaType "application/zip"constant`

          The media type of the inline skill payload. Must be `application/zip`.

          - `APPLICATION_ZIP("application/zip")`

        - `JsonValue; type "base64"constant`

          The type of the inline skill source. Must be `base64`.

          - `BASE64("base64")`

      - `JsonValue; type "inline"constant`

        Defines an inline skill for this request.

        - `INLINE("inline")`

### Returns

- `class ContainerCreateResponse:`

  - `String id`

    Unique identifier for the container.

  - `long createdAt`

    Unix timestamp (in seconds) when the container was created.

  - `String name`

    Name of the container.

  - `String object_`

    The type of this object.

  - `String status`

    Status of the container (e.g., active, deleted).

  - `Optional<ExpiresAfter> expiresAfter`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `Optional<Anchor> anchor`

      The reference point for the expiration.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `Optional<Long> minutes`

      The number of minutes after the anchor before the container expires.

  - `Optional<Long> lastActiveAt`

    Unix timestamp (in seconds) when the container was last active.

  - `Optional<MemoryLimit> memoryLimit`

    The memory limit configured for the container.

    - `_1G("1g")`

    - `_4G("4g")`

    - `_16G("16g")`

    - `_64G("64g")`

  - `Optional<NetworkPolicy> networkPolicy`

    Network access policy for the container.

    - `Type type`

      The network policy mode.

      - `ALLOWLIST("allowlist")`

      - `DISABLED("disabled")`

    - `Optional<List<String>> allowedDomains`

      Allowed outbound domains when `type` is `allowlist`.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.ContainerCreateParams;
import com.openai.models.containers.ContainerCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContainerCreateParams params = ContainerCreateParams.builder()
            .name("name")
            .build();
        ContainerCreateResponse container = client.containers().create(params);
    }
}
```

## Retrieve

`ContainerRetrieveResponse containers().retrieve(ContainerRetrieveParamsparams = ContainerRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/containers/{container_id}`

Retrieve Container

### Parameters

- `ContainerRetrieveParams params`

  - `Optional<String> containerId`

### Returns

- `class ContainerRetrieveResponse:`

  - `String id`

    Unique identifier for the container.

  - `long createdAt`

    Unix timestamp (in seconds) when the container was created.

  - `String name`

    Name of the container.

  - `String object_`

    The type of this object.

  - `String status`

    Status of the container (e.g., active, deleted).

  - `Optional<ExpiresAfter> expiresAfter`

    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.

    - `Optional<Anchor> anchor`

      The reference point for the expiration.

      - `LAST_ACTIVE_AT("last_active_at")`

    - `Optional<Long> minutes`

      The number of minutes after the anchor before the container expires.

  - `Optional<Long> lastActiveAt`

    Unix timestamp (in seconds) when the container was last active.

  - `Optional<MemoryLimit> memoryLimit`

    The memory limit configured for the container.

    - `_1G("1g")`

    - `_4G("4g")`

    - `_16G("16g")`

    - `_64G("64g")`

  - `Optional<NetworkPolicy> networkPolicy`

    Network access policy for the container.

    - `Type type`

      The network policy mode.

      - `ALLOWLIST("allowlist")`

      - `DISABLED("disabled")`

    - `Optional<List<String>> allowedDomains`

      Allowed outbound domains when `type` is `allowlist`.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.ContainerRetrieveParams;
import com.openai.models.containers.ContainerRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContainerRetrieveResponse container = client.containers().retrieve("container_id");
    }
}
```

## Delete

`containers().delete(ContainerDeleteParamsparams = ContainerDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/containers/{container_id}`

Delete Container

### Parameters

- `ContainerDeleteParams params`

  - `Optional<String> containerId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.ContainerDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.containers().delete("container_id");
    }
}
```

## Files

### List

`FileListPage containers().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/containers/{container_id}/files`

List Container files

#### Parameters

- `FileListParams params`

  - `Optional<String> containerId`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

#### Returns

- `class FileListResponse:`

  - `String id`

    Unique identifier for the file.

  - `long bytes`

    Size of the file in bytes.

  - `String containerId`

    The container this file belongs to.

  - `long createdAt`

    Unix timestamp (in seconds) when the file was created.

  - `JsonValue; object_ "container.file"constant`

    The type of this object (`container.file`).

    - `CONTAINER_FILE("container.file")`

  - `String path`

    Path of the file in the container.

  - `String source`

    Source of the file (e.g., `user`, `assistant`).

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.files.FileListPage;
import com.openai.models.containers.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileListPage page = client.containers().files().list("container_id");
    }
}
```

### Create

`FileCreateResponse containers().files().create(FileCreateParamsparams = FileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/containers/{container_id}/files`

Create a Container File

You can send either a multipart/form-data request with the raw file content, or a JSON request with a file ID.

#### Parameters

- `FileCreateParams params`

  - `Optional<String> containerId`

  - `Optional<String> file`

    The File object (not file name) to be uploaded.

  - `Optional<String> fileId`

    Name of the file to create.

#### Returns

- `class FileCreateResponse:`

  - `String id`

    Unique identifier for the file.

  - `long bytes`

    Size of the file in bytes.

  - `String containerId`

    The container this file belongs to.

  - `long createdAt`

    Unix timestamp (in seconds) when the file was created.

  - `JsonValue; object_ "container.file"constant`

    The type of this object (`container.file`).

    - `CONTAINER_FILE("container.file")`

  - `String path`

    Path of the file in the container.

  - `String source`

    Source of the file (e.g., `user`, `assistant`).

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.files.FileCreateParams;
import com.openai.models.containers.files.FileCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileCreateResponse file = client.containers().files().create("container_id");
    }
}
```

### Retrieve

`FileRetrieveResponse containers().files().retrieve(FileRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/containers/{container_id}/files/{file_id}`

Retrieve Container File

#### Parameters

- `FileRetrieveParams params`

  - `String containerId`

  - `Optional<String> fileId`

#### Returns

- `class FileRetrieveResponse:`

  - `String id`

    Unique identifier for the file.

  - `long bytes`

    Size of the file in bytes.

  - `String containerId`

    The container this file belongs to.

  - `long createdAt`

    Unix timestamp (in seconds) when the file was created.

  - `JsonValue; object_ "container.file"constant`

    The type of this object (`container.file`).

    - `CONTAINER_FILE("container.file")`

  - `String path`

    Path of the file in the container.

  - `String source`

    Source of the file (e.g., `user`, `assistant`).

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.files.FileRetrieveParams;
import com.openai.models.containers.files.FileRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileRetrieveParams params = FileRetrieveParams.builder()
            .containerId("container_id")
            .fileId("file_id")
            .build();
        FileRetrieveResponse file = client.containers().files().retrieve(params);
    }
}
```

### Delete

`containers().files().delete(FileDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/containers/{container_id}/files/{file_id}`

Delete Container File

#### Parameters

- `FileDeleteParams params`

  - `String containerId`

  - `Optional<String> fileId`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.containers.files.FileDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileDeleteParams params = FileDeleteParams.builder()
            .containerId("container_id")
            .fileId("file_id")
            .build();
        client.containers().files().delete(params);
    }
}
```

### Content

#### Retrieve

`HttpResponse containers().files().content().retrieve(ContentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/containers/{container_id}/files/{file_id}/content`

Retrieve Container File Content

##### Parameters

- `ContentRetrieveParams params`

  - `String containerId`

  - `Optional<String> fileId`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.containers.files.content.ContentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ContentRetrieveParams params = ContentRetrieveParams.builder()
            .containerId("container_id")
            .fileId("file_id")
            .build();
        HttpResponse content = client.containers().files().content().retrieve(params);
    }
}
```
