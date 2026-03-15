# Beta

## ChatKit

### Domain Types

### ChatKit Workflow

- `class ChatKitWorkflow:`

  Workflow metadata and state returned for the session.

  - `String id`

    Identifier of the workflow backing the session.

  - `Optional<StateVariables> stateVariables`

    State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

    - `String`

    - `boolean`

    - `double`

  - `Tracing tracing`

    Tracing settings applied to the workflow.

    - `boolean enabled`

      Indicates whether tracing is enabled.

  - `Optional<String> version`

    Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Sessions

#### Cancel

`ChatSession beta().chatkit().sessions().cancel(SessionCancelParamsparams = SessionCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/chatkit/sessions/{session_id}/cancel`

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### Parameters

- `SessionCancelParams params`

  - `Optional<String> sessionId`

##### Returns

- `class ChatSession:`

  Represents a ChatKit session and its resolved configuration.

  - `String id`

    Identifier for the ChatKit session.

  - `ChatSessionChatKitConfiguration chatkitConfiguration`

    Resolved ChatKit feature configuration for the session.

    - `ChatSessionAutomaticThreadTitling automaticThreadTitling`

      Automatic thread titling preferences.

      - `boolean enabled`

        Whether automatic thread titling is enabled.

    - `ChatSessionFileUpload fileUpload`

      Upload settings for the session.

      - `boolean enabled`

        Indicates if uploads are enabled for the session.

      - `Optional<Long> maxFileSize`

        Maximum upload size in megabytes.

      - `Optional<Long> maxFiles`

        Maximum number of uploads allowed during the session.

    - `ChatSessionHistory history`

      History retention configuration.

      - `boolean enabled`

        Indicates if chat history is persisted for the session.

      - `Optional<Long> recentThreads`

        Number of prior threads surfaced in history views. Defaults to null when all history is retained.

  - `String clientSecret`

    Ephemeral client secret that authenticates session requests.

  - `long expiresAt`

    Unix timestamp (in seconds) for when the session expires.

  - `long maxRequestsPer1Minute`

    Convenience copy of the per-minute request limit.

  - `JsonValue; object_ "chatkit.session"constant`

    Type discriminator that is always `chatkit.session`.

    - `CHATKIT_SESSION("chatkit.session")`

  - `ChatSessionRateLimits rateLimits`

    Resolved rate limit values.

    - `long maxRequestsPer1Minute`

      Maximum allowed requests per one-minute window.

  - `ChatSessionStatus status`

    Current lifecycle state of the session.

    - `ACTIVE("active")`

    - `EXPIRED("expired")`

    - `CANCELLED("cancelled")`

  - `String user`

    User identifier associated with the session.

  - `ChatKitWorkflow workflow`

    Workflow metadata for the session.

    - `String id`

      Identifier of the workflow backing the session.

    - `Optional<StateVariables> stateVariables`

      State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

      - `String`

      - `boolean`

      - `double`

    - `Tracing tracing`

      Tracing settings applied to the workflow.

      - `boolean enabled`

        Indicates whether tracing is enabled.

    - `Optional<String> version`

      Specific workflow version used for the session. Defaults to null when using the latest deployment.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.sessions.SessionCancelParams;
import com.openai.models.beta.chatkit.threads.ChatSession;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatSession chatSession = client.beta().chatkit().sessions().cancel("cksess_123");
    }
}
```

#### Create

`ChatSession beta().chatkit().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/chatkit/sessions`

Create a ChatKit session.

##### Parameters

- `SessionCreateParams params`

  - `String user`

    A free-form string that identifies your end user; ensures this Session can access other objects that have the same `user` scope.

  - `ChatSessionWorkflowParam workflow`

    Workflow that powers the session.

  - `Optional<ChatSessionChatKitConfigurationParam> chatkitConfiguration`

    Optional overrides for ChatKit runtime configuration features

  - `Optional<ChatSessionExpiresAfterParam> expiresAfter`

    Optional override for session expiration timing in seconds from creation. Defaults to 10 minutes.

  - `Optional<ChatSessionRateLimitsParam> rateLimits`

    Optional override for per-minute request limits. When omitted, defaults to 10.

##### Returns

- `class ChatSession:`

  Represents a ChatKit session and its resolved configuration.

  - `String id`

    Identifier for the ChatKit session.

  - `ChatSessionChatKitConfiguration chatkitConfiguration`

    Resolved ChatKit feature configuration for the session.

    - `ChatSessionAutomaticThreadTitling automaticThreadTitling`

      Automatic thread titling preferences.

      - `boolean enabled`

        Whether automatic thread titling is enabled.

    - `ChatSessionFileUpload fileUpload`

      Upload settings for the session.

      - `boolean enabled`

        Indicates if uploads are enabled for the session.

      - `Optional<Long> maxFileSize`

        Maximum upload size in megabytes.

      - `Optional<Long> maxFiles`

        Maximum number of uploads allowed during the session.

    - `ChatSessionHistory history`

      History retention configuration.

      - `boolean enabled`

        Indicates if chat history is persisted for the session.

      - `Optional<Long> recentThreads`

        Number of prior threads surfaced in history views. Defaults to null when all history is retained.

  - `String clientSecret`

    Ephemeral client secret that authenticates session requests.

  - `long expiresAt`

    Unix timestamp (in seconds) for when the session expires.

  - `long maxRequestsPer1Minute`

    Convenience copy of the per-minute request limit.

  - `JsonValue; object_ "chatkit.session"constant`

    Type discriminator that is always `chatkit.session`.

    - `CHATKIT_SESSION("chatkit.session")`

  - `ChatSessionRateLimits rateLimits`

    Resolved rate limit values.

    - `long maxRequestsPer1Minute`

      Maximum allowed requests per one-minute window.

  - `ChatSessionStatus status`

    Current lifecycle state of the session.

    - `ACTIVE("active")`

    - `EXPIRED("expired")`

    - `CANCELLED("cancelled")`

  - `String user`

    User identifier associated with the session.

  - `ChatKitWorkflow workflow`

    Workflow metadata for the session.

    - `String id`

      Identifier of the workflow backing the session.

    - `Optional<StateVariables> stateVariables`

      State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

      - `String`

      - `boolean`

      - `double`

    - `Tracing tracing`

      Tracing settings applied to the workflow.

      - `boolean enabled`

        Indicates whether tracing is enabled.

    - `Optional<String> version`

      Specific workflow version used for the session. Defaults to null when using the latest deployment.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.sessions.SessionCreateParams;
import com.openai.models.beta.chatkit.threads.ChatSession;
import com.openai.models.beta.chatkit.threads.ChatSessionWorkflowParam;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionCreateParams params = SessionCreateParams.builder()
            .user("x")
            .workflow(ChatSessionWorkflowParam.builder()
                .id("id")
                .build())
            .build();
        ChatSession chatSession = client.beta().chatkit().sessions().create(params);
    }
}
```

### Threads

#### List Items

`ThreadListItemsPage beta().chatkit().threads().listItems(ThreadListItemsParamsparams = ThreadListItemsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/chatkit/threads/{thread_id}/items`

List items that belong to a ChatKit thread.

##### Parameters

- `ThreadListItemsParams params`

  - `Optional<String> threadId`

  - `Optional<String> after`

    List items created after this thread item ID. Defaults to null for the first page.

  - `Optional<String> before`

    List items created before this thread item ID. Defaults to null for the newest results.

  - `Optional<Long> limit`

    Maximum number of thread items to return. Defaults to 20.

  - `Optional<Order> order`

    Sort order for results by creation time. Defaults to `desc`.

    - `ASC("asc")`

    - `DESC("desc")`

##### Returns

- `class Data: A class that can be one of several variants.union`

  User-authored messages within a thread.

  - `class ChatKitThreadUserMessageItem:`

    User-authored messages within a thread.

    - `String id`

      Identifier of the thread item.

    - `List<ChatKitAttachment> attachments`

      Attachments associated with the user message. Defaults to an empty list.

      - `String id`

        Identifier for the attachment.

      - `String mimeType`

        MIME type of the attachment.

      - `String name`

        Original display name for the attachment.

      - `Optional<String> previewUrl`

        Preview URL for rendering the attachment inline.

      - `Type type`

        Attachment discriminator.

        - `IMAGE("image")`

        - `FILE("file")`

    - `List<Content> content`

      Ordered content elements supplied by the user.

      - `class InputText:`

        Text block that a user contributed to the thread.

        - `String text`

          Plain-text content supplied by the user.

        - `JsonValue; type "input_text"constant`

          Type discriminator that is always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `class QuotedText:`

        Quoted snippet that the user referenced in their message.

        - `String text`

          Quoted text content.

        - `JsonValue; type "quoted_text"constant`

          Type discriminator that is always `quoted_text`.

          - `QUOTED_TEXT("quoted_text")`

    - `long createdAt`

      Unix timestamp (in seconds) for when the item was created.

    - `Optional<InferenceOptions> inferenceOptions`

      Inference overrides applied to the message. Defaults to null when unset.

      - `Optional<String> model`

        Model name that generated the response. Defaults to null when using the session default.

      - `Optional<ToolChoice> toolChoice`

        Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

        - `String id`

          Identifier of the requested tool.

    - `JsonValue; object_ "chatkit.thread_item"constant`

      Type discriminator that is always `chatkit.thread_item`.

      - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

    - `String threadId`

      Identifier of the parent thread.

    - `JsonValue; type "chatkit.user_message"constant`

      - `CHATKIT_USER_MESSAGE("chatkit.user_message")`

  - `class ChatKitThreadAssistantMessageItem:`

    Assistant-authored message within a thread.

    - `String id`

      Identifier of the thread item.

    - `List<ChatKitResponseOutputText> content`

      Ordered assistant response segments.

      - `List<Annotation> annotations`

        Ordered list of annotations attached to the response text.

        - `class File:`

          Annotation that references an uploaded file.

          - `Source source`

            File attachment referenced by the annotation.

            - `String filename`

              Filename referenced by the annotation.

            - `JsonValue; type "file"constant`

              Type discriminator that is always `file`.

              - `FILE("file")`

          - `JsonValue; type "file"constant`

            Type discriminator that is always `file` for this annotation.

            - `FILE("file")`

        - `class Url:`

          Annotation that references a URL.

          - `Source source`

            URL referenced by the annotation.

            - `JsonValue; type "url"constant`

              Type discriminator that is always `url`.

              - `URL("url")`

            - `String url`

              URL referenced by the annotation.

          - `JsonValue; type "url"constant`

            Type discriminator that is always `url` for this annotation.

            - `URL("url")`

      - `String text`

        Assistant generated text.

      - `JsonValue; type "output_text"constant`

        Type discriminator that is always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `long createdAt`

      Unix timestamp (in seconds) for when the item was created.

    - `JsonValue; object_ "chatkit.thread_item"constant`

      Type discriminator that is always `chatkit.thread_item`.

      - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

    - `String threadId`

      Identifier of the parent thread.

    - `JsonValue; type "chatkit.assistant_message"constant`

      Type discriminator that is always `chatkit.assistant_message`.

      - `CHATKIT_ASSISTANT_MESSAGE("chatkit.assistant_message")`

  - `class ChatKitWidgetItem:`

    Thread item that renders a widget payload.

    - `String id`

      Identifier of the thread item.

    - `long createdAt`

      Unix timestamp (in seconds) for when the item was created.

    - `JsonValue; object_ "chatkit.thread_item"constant`

      Type discriminator that is always `chatkit.thread_item`.

      - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

    - `String threadId`

      Identifier of the parent thread.

    - `JsonValue; type "chatkit.widget"constant`

      Type discriminator that is always `chatkit.widget`.

      - `CHATKIT_WIDGET("chatkit.widget")`

    - `String widget`

      Serialized widget payload rendered in the UI.

  - `class ChatKitClientToolCall:`

    Record of a client side tool invocation initiated by the assistant.

    - `String id`

      Identifier of the thread item.

    - `String arguments`

      JSON-encoded arguments that were sent to the tool.

    - `String callId`

      Identifier for the client tool call.

    - `long createdAt`

      Unix timestamp (in seconds) for when the item was created.

    - `String name`

      Tool name that was invoked.

    - `JsonValue; object_ "chatkit.thread_item"constant`

      Type discriminator that is always `chatkit.thread_item`.

      - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

    - `Optional<String> output`

      JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

    - `Status status`

      Execution status for the tool call.

      - `IN_PROGRESS("in_progress")`

      - `COMPLETED("completed")`

    - `String threadId`

      Identifier of the parent thread.

    - `JsonValue; type "chatkit.client_tool_call"constant`

      Type discriminator that is always `chatkit.client_tool_call`.

      - `CHATKIT_CLIENT_TOOL_CALL("chatkit.client_tool_call")`

  - `class ChatKitTask:`

    Task emitted by the workflow to show progress and status updates.

    - `String id`

      Identifier of the thread item.

    - `long createdAt`

      Unix timestamp (in seconds) for when the item was created.

    - `Optional<String> heading`

      Optional heading for the task. Defaults to null when not provided.

    - `JsonValue; object_ "chatkit.thread_item"constant`

      Type discriminator that is always `chatkit.thread_item`.

      - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

    - `Optional<String> summary`

      Optional summary that describes the task. Defaults to null when omitted.

    - `TaskType taskType`

      Subtype for the task.

      - `CUSTOM("custom")`

      - `THOUGHT("thought")`

    - `String threadId`

      Identifier of the parent thread.

    - `JsonValue; type "chatkit.task"constant`

      Type discriminator that is always `chatkit.task`.

      - `CHATKIT_TASK("chatkit.task")`

  - `class ChatKitTaskGroup:`

    Collection of workflow tasks grouped together in the thread.

    - `String id`

      Identifier of the thread item.

    - `long createdAt`

      Unix timestamp (in seconds) for when the item was created.

    - `JsonValue; object_ "chatkit.thread_item"constant`

      Type discriminator that is always `chatkit.thread_item`.

      - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

    - `List<Task> tasks`

      Tasks included in the group.

      - `Optional<String> heading`

        Optional heading for the grouped task. Defaults to null when not provided.

      - `Optional<String> summary`

        Optional summary that describes the grouped task. Defaults to null when omitted.

      - `Type type`

        Subtype for the grouped task.

        - `CUSTOM("custom")`

        - `THOUGHT("thought")`

    - `String threadId`

      Identifier of the parent thread.

    - `JsonValue; type "chatkit.task_group"constant`

      Type discriminator that is always `chatkit.task_group`.

      - `CHATKIT_TASK_GROUP("chatkit.task_group")`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.threads.ThreadListItemsPage;
import com.openai.models.beta.chatkit.threads.ThreadListItemsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadListItemsPage page = client.beta().chatkit().threads().listItems("cthr_123");
    }
}
```

#### Retrieve

`ChatKitThread beta().chatkit().threads().retrieve(ThreadRetrieveParamsparams = ThreadRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/chatkit/threads/{thread_id}`

Retrieve a ChatKit thread by its identifier.

##### Parameters

- `ThreadRetrieveParams params`

  - `Optional<String> threadId`

##### Returns

- `class ChatKitThread:`

  Represents a ChatKit thread and its current status.

  - `String id`

    Identifier of the thread.

  - `long createdAt`

    Unix timestamp (in seconds) for when the thread was created.

  - `JsonValue; object_ "chatkit.thread"constant`

    Type discriminator that is always `chatkit.thread`.

    - `CHATKIT_THREAD("chatkit.thread")`

  - `Status status`

    Current status for the thread. Defaults to `active` for newly created threads.

    - `JsonValue;`

      - `JsonValue; type "active"constant`

        Status discriminator that is always `active`.

        - `ACTIVE("active")`

    - `class Locked:`

      Indicates that a thread is locked and cannot accept new input.

      - `Optional<String> reason`

        Reason that the thread was locked. Defaults to null when no reason is recorded.

      - `JsonValue; type "locked"constant`

        Status discriminator that is always `locked`.

        - `LOCKED("locked")`

    - `class Closed:`

      Indicates that a thread has been closed.

      - `Optional<String> reason`

        Reason that the thread was closed. Defaults to null when no reason is recorded.

      - `JsonValue; type "closed"constant`

        Status discriminator that is always `closed`.

        - `CLOSED("closed")`

  - `Optional<String> title`

    Optional human-readable title for the thread. Defaults to null when no title has been generated.

  - `String user`

    Free-form string that identifies your end user who owns the thread.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.threads.ChatKitThread;
import com.openai.models.beta.chatkit.threads.ThreadRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatKitThread chatkitThread = client.beta().chatkit().threads().retrieve("cthr_123");
    }
}
```

#### Delete

`ThreadDeleteResponse beta().chatkit().threads().delete(ThreadDeleteParamsparams = ThreadDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/chatkit/threads/{thread_id}`

Delete a ChatKit thread along with its items and stored attachments.

##### Parameters

- `ThreadDeleteParams params`

  - `Optional<String> threadId`

##### Returns

- `class ThreadDeleteResponse:`

  Confirmation payload returned after deleting a thread.

  - `String id`

    Identifier of the deleted thread.

  - `boolean deleted`

    Indicates that the thread has been deleted.

  - `JsonValue; object_ "chatkit.thread.deleted"constant`

    Type discriminator that is always `chatkit.thread.deleted`.

    - `CHATKIT_THREAD_DELETED("chatkit.thread.deleted")`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.threads.ThreadDeleteParams;
import com.openai.models.beta.chatkit.threads.ThreadDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadDeleteResponse thread = client.beta().chatkit().threads().delete("cthr_123");
    }
}
```

#### List

`ThreadListPage beta().chatkit().threads().list(ThreadListParamsparams = ThreadListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/chatkit/threads`

List ChatKit threads with optional pagination and user filters.

##### Parameters

- `ThreadListParams params`

  - `Optional<String> after`

    List items created after this thread item ID. Defaults to null for the first page.

  - `Optional<String> before`

    List items created before this thread item ID. Defaults to null for the newest results.

  - `Optional<Long> limit`

    Maximum number of thread items to return. Defaults to 20.

  - `Optional<Order> order`

    Sort order for results by creation time. Defaults to `desc`.

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> user`

    Filter threads that belong to this user identifier. Defaults to null to return all users.

##### Returns

- `class ChatKitThread:`

  Represents a ChatKit thread and its current status.

  - `String id`

    Identifier of the thread.

  - `long createdAt`

    Unix timestamp (in seconds) for when the thread was created.

  - `JsonValue; object_ "chatkit.thread"constant`

    Type discriminator that is always `chatkit.thread`.

    - `CHATKIT_THREAD("chatkit.thread")`

  - `Status status`

    Current status for the thread. Defaults to `active` for newly created threads.

    - `JsonValue;`

      - `JsonValue; type "active"constant`

        Status discriminator that is always `active`.

        - `ACTIVE("active")`

    - `class Locked:`

      Indicates that a thread is locked and cannot accept new input.

      - `Optional<String> reason`

        Reason that the thread was locked. Defaults to null when no reason is recorded.

      - `JsonValue; type "locked"constant`

        Status discriminator that is always `locked`.

        - `LOCKED("locked")`

    - `class Closed:`

      Indicates that a thread has been closed.

      - `Optional<String> reason`

        Reason that the thread was closed. Defaults to null when no reason is recorded.

      - `JsonValue; type "closed"constant`

        Status discriminator that is always `closed`.

        - `CLOSED("closed")`

  - `Optional<String> title`

    Optional human-readable title for the thread. Defaults to null when no title has been generated.

  - `String user`

    Free-form string that identifies your end user who owns the thread.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.threads.ThreadListPage;
import com.openai.models.beta.chatkit.threads.ThreadListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadListPage page = client.beta().chatkit().threads().list();
    }
}
```

##### Domain Types

##### Chat Session

- `class ChatSession:`

  Represents a ChatKit session and its resolved configuration.

  - `String id`

    Identifier for the ChatKit session.

  - `ChatSessionChatKitConfiguration chatkitConfiguration`

    Resolved ChatKit feature configuration for the session.

    - `ChatSessionAutomaticThreadTitling automaticThreadTitling`

      Automatic thread titling preferences.

      - `boolean enabled`

        Whether automatic thread titling is enabled.

    - `ChatSessionFileUpload fileUpload`

      Upload settings for the session.

      - `boolean enabled`

        Indicates if uploads are enabled for the session.

      - `Optional<Long> maxFileSize`

        Maximum upload size in megabytes.

      - `Optional<Long> maxFiles`

        Maximum number of uploads allowed during the session.

    - `ChatSessionHistory history`

      History retention configuration.

      - `boolean enabled`

        Indicates if chat history is persisted for the session.

      - `Optional<Long> recentThreads`

        Number of prior threads surfaced in history views. Defaults to null when all history is retained.

  - `String clientSecret`

    Ephemeral client secret that authenticates session requests.

  - `long expiresAt`

    Unix timestamp (in seconds) for when the session expires.

  - `long maxRequestsPer1Minute`

    Convenience copy of the per-minute request limit.

  - `JsonValue; object_ "chatkit.session"constant`

    Type discriminator that is always `chatkit.session`.

    - `CHATKIT_SESSION("chatkit.session")`

  - `ChatSessionRateLimits rateLimits`

    Resolved rate limit values.

    - `long maxRequestsPer1Minute`

      Maximum allowed requests per one-minute window.

  - `ChatSessionStatus status`

    Current lifecycle state of the session.

    - `ACTIVE("active")`

    - `EXPIRED("expired")`

    - `CANCELLED("cancelled")`

  - `String user`

    User identifier associated with the session.

  - `ChatKitWorkflow workflow`

    Workflow metadata for the session.

    - `String id`

      Identifier of the workflow backing the session.

    - `Optional<StateVariables> stateVariables`

      State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

      - `String`

      - `boolean`

      - `double`

    - `Tracing tracing`

      Tracing settings applied to the workflow.

      - `boolean enabled`

        Indicates whether tracing is enabled.

    - `Optional<String> version`

      Specific workflow version used for the session. Defaults to null when using the latest deployment.

##### Chat Session Automatic Thread Titling

- `class ChatSessionAutomaticThreadTitling:`

  Automatic thread title preferences for the session.

  - `boolean enabled`

    Whether automatic thread titling is enabled.

##### Chat Session ChatKit Configuration

- `class ChatSessionChatKitConfiguration:`

  ChatKit configuration for the session.

  - `ChatSessionAutomaticThreadTitling automaticThreadTitling`

    Automatic thread titling preferences.

    - `boolean enabled`

      Whether automatic thread titling is enabled.

  - `ChatSessionFileUpload fileUpload`

    Upload settings for the session.

    - `boolean enabled`

      Indicates if uploads are enabled for the session.

    - `Optional<Long> maxFileSize`

      Maximum upload size in megabytes.

    - `Optional<Long> maxFiles`

      Maximum number of uploads allowed during the session.

  - `ChatSessionHistory history`

    History retention configuration.

    - `boolean enabled`

      Indicates if chat history is persisted for the session.

    - `Optional<Long> recentThreads`

      Number of prior threads surfaced in history views. Defaults to null when all history is retained.

##### Chat Session ChatKit Configuration Param

- `class ChatSessionChatKitConfigurationParam:`

  Optional per-session configuration settings for ChatKit behavior.

  - `Optional<AutomaticThreadTitling> automaticThreadTitling`

    Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

    - `Optional<Boolean> enabled`

      Enable automatic thread title generation. Defaults to true.

  - `Optional<FileUpload> fileUpload`

    Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max_files 10, max_file_size 512 MB).

    - `Optional<Boolean> enabled`

      Enable uploads for this session. Defaults to false.

    - `Optional<Long> maxFileSize`

      Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

    - `Optional<Long> maxFiles`

      Maximum number of files that can be uploaded to the session. Defaults to 10.

  - `Optional<History> history`

    Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent_threads (null).

    - `Optional<Boolean> enabled`

      Enables chat users to access previous ChatKit threads. Defaults to true.

    - `Optional<Long> recentThreads`

      Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

##### Chat Session Expires After Param

- `class ChatSessionExpiresAfterParam:`

  Controls when the session expires relative to an anchor timestamp.

  - `JsonValue; anchor "created_at"constant`

    Base timestamp used to calculate expiration. Currently fixed to `created_at`.

    - `CREATED_AT("created_at")`

  - `long seconds`

    Number of seconds after the anchor when the session expires.

##### Chat Session File Upload

- `class ChatSessionFileUpload:`

  Upload permissions and limits applied to the session.

  - `boolean enabled`

    Indicates if uploads are enabled for the session.

  - `Optional<Long> maxFileSize`

    Maximum upload size in megabytes.

  - `Optional<Long> maxFiles`

    Maximum number of uploads allowed during the session.

##### Chat Session History

- `class ChatSessionHistory:`

  History retention preferences returned for the session.

  - `boolean enabled`

    Indicates if chat history is persisted for the session.

  - `Optional<Long> recentThreads`

    Number of prior threads surfaced in history views. Defaults to null when all history is retained.

##### Chat Session Rate Limits

- `class ChatSessionRateLimits:`

  Active per-minute request limit for the session.

  - `long maxRequestsPer1Minute`

    Maximum allowed requests per one-minute window.

##### Chat Session Rate Limits Param

- `class ChatSessionRateLimitsParam:`

  Controls request rate limits for the session.

  - `Optional<Long> maxRequestsPer1Minute`

    Maximum number of requests allowed per minute for the session. Defaults to 10.

##### Chat Session Status

- `enum ChatSessionStatus:`

  - `ACTIVE("active")`

  - `EXPIRED("expired")`

  - `CANCELLED("cancelled")`

##### Chat Session Workflow Param

- `class ChatSessionWorkflowParam:`

  Workflow reference and overrides applied to the chat session.

  - `String id`

    Identifier for the workflow invoked by the session.

  - `Optional<StateVariables> stateVariables`

    State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

    - `String`

    - `boolean`

    - `double`

  - `Optional<Tracing> tracing`

    Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

    - `Optional<Boolean> enabled`

      Whether tracing is enabled during the session. Defaults to true.

  - `Optional<String> version`

    Specific workflow version to run. Defaults to the latest deployed version.

##### ChatKit Attachment

- `class ChatKitAttachment:`

  Attachment metadata included on thread items.

  - `String id`

    Identifier for the attachment.

  - `String mimeType`

    MIME type of the attachment.

  - `String name`

    Original display name for the attachment.

  - `Optional<String> previewUrl`

    Preview URL for rendering the attachment inline.

  - `Type type`

    Attachment discriminator.

    - `IMAGE("image")`

    - `FILE("file")`

##### ChatKit Response Output Text

- `class ChatKitResponseOutputText:`

  Assistant response text accompanied by optional annotations.

  - `List<Annotation> annotations`

    Ordered list of annotations attached to the response text.

    - `class File:`

      Annotation that references an uploaded file.

      - `Source source`

        File attachment referenced by the annotation.

        - `String filename`

          Filename referenced by the annotation.

        - `JsonValue; type "file"constant`

          Type discriminator that is always `file`.

          - `FILE("file")`

      - `JsonValue; type "file"constant`

        Type discriminator that is always `file` for this annotation.

        - `FILE("file")`

    - `class Url:`

      Annotation that references a URL.

      - `Source source`

        URL referenced by the annotation.

        - `JsonValue; type "url"constant`

          Type discriminator that is always `url`.

          - `URL("url")`

        - `String url`

          URL referenced by the annotation.

      - `JsonValue; type "url"constant`

        Type discriminator that is always `url` for this annotation.

        - `URL("url")`

  - `String text`

    Assistant generated text.

  - `JsonValue; type "output_text"constant`

    Type discriminator that is always `output_text`.

    - `OUTPUT_TEXT("output_text")`

##### ChatKit Thread

- `class ChatKitThread:`

  Represents a ChatKit thread and its current status.

  - `String id`

    Identifier of the thread.

  - `long createdAt`

    Unix timestamp (in seconds) for when the thread was created.

  - `JsonValue; object_ "chatkit.thread"constant`

    Type discriminator that is always `chatkit.thread`.

    - `CHATKIT_THREAD("chatkit.thread")`

  - `Status status`

    Current status for the thread. Defaults to `active` for newly created threads.

    - `JsonValue;`

      - `JsonValue; type "active"constant`

        Status discriminator that is always `active`.

        - `ACTIVE("active")`

    - `class Locked:`

      Indicates that a thread is locked and cannot accept new input.

      - `Optional<String> reason`

        Reason that the thread was locked. Defaults to null when no reason is recorded.

      - `JsonValue; type "locked"constant`

        Status discriminator that is always `locked`.

        - `LOCKED("locked")`

    - `class Closed:`

      Indicates that a thread has been closed.

      - `Optional<String> reason`

        Reason that the thread was closed. Defaults to null when no reason is recorded.

      - `JsonValue; type "closed"constant`

        Status discriminator that is always `closed`.

        - `CLOSED("closed")`

  - `Optional<String> title`

    Optional human-readable title for the thread. Defaults to null when no title has been generated.

  - `String user`

    Free-form string that identifies your end user who owns the thread.

##### ChatKit Thread Assistant Message Item

- `class ChatKitThreadAssistantMessageItem:`

  Assistant-authored message within a thread.

  - `String id`

    Identifier of the thread item.

  - `List<ChatKitResponseOutputText> content`

    Ordered assistant response segments.

    - `List<Annotation> annotations`

      Ordered list of annotations attached to the response text.

      - `class File:`

        Annotation that references an uploaded file.

        - `Source source`

          File attachment referenced by the annotation.

          - `String filename`

            Filename referenced by the annotation.

          - `JsonValue; type "file"constant`

            Type discriminator that is always `file`.

            - `FILE("file")`

        - `JsonValue; type "file"constant`

          Type discriminator that is always `file` for this annotation.

          - `FILE("file")`

      - `class Url:`

        Annotation that references a URL.

        - `Source source`

          URL referenced by the annotation.

          - `JsonValue; type "url"constant`

            Type discriminator that is always `url`.

            - `URL("url")`

          - `String url`

            URL referenced by the annotation.

        - `JsonValue; type "url"constant`

          Type discriminator that is always `url` for this annotation.

          - `URL("url")`

    - `String text`

      Assistant generated text.

    - `JsonValue; type "output_text"constant`

      Type discriminator that is always `output_text`.

      - `OUTPUT_TEXT("output_text")`

  - `long createdAt`

    Unix timestamp (in seconds) for when the item was created.

  - `JsonValue; object_ "chatkit.thread_item"constant`

    Type discriminator that is always `chatkit.thread_item`.

    - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

  - `String threadId`

    Identifier of the parent thread.

  - `JsonValue; type "chatkit.assistant_message"constant`

    Type discriminator that is always `chatkit.assistant_message`.

    - `CHATKIT_ASSISTANT_MESSAGE("chatkit.assistant_message")`

##### ChatKit Thread Item List

- `class ChatKitThreadItemList:`

  A paginated list of thread items rendered for the ChatKit API.

  - `List<Data> data`

    A list of items

    - `class ChatKitThreadUserMessageItem:`

      User-authored messages within a thread.

      - `String id`

        Identifier of the thread item.

      - `List<ChatKitAttachment> attachments`

        Attachments associated with the user message. Defaults to an empty list.

        - `String id`

          Identifier for the attachment.

        - `String mimeType`

          MIME type of the attachment.

        - `String name`

          Original display name for the attachment.

        - `Optional<String> previewUrl`

          Preview URL for rendering the attachment inline.

        - `Type type`

          Attachment discriminator.

          - `IMAGE("image")`

          - `FILE("file")`

      - `List<Content> content`

        Ordered content elements supplied by the user.

        - `class InputText:`

          Text block that a user contributed to the thread.

          - `String text`

            Plain-text content supplied by the user.

          - `JsonValue; type "input_text"constant`

            Type discriminator that is always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `class QuotedText:`

          Quoted snippet that the user referenced in their message.

          - `String text`

            Quoted text content.

          - `JsonValue; type "quoted_text"constant`

            Type discriminator that is always `quoted_text`.

            - `QUOTED_TEXT("quoted_text")`

      - `long createdAt`

        Unix timestamp (in seconds) for when the item was created.

      - `Optional<InferenceOptions> inferenceOptions`

        Inference overrides applied to the message. Defaults to null when unset.

        - `Optional<String> model`

          Model name that generated the response. Defaults to null when using the session default.

        - `Optional<ToolChoice> toolChoice`

          Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

          - `String id`

            Identifier of the requested tool.

      - `JsonValue; object_ "chatkit.thread_item"constant`

        Type discriminator that is always `chatkit.thread_item`.

        - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

      - `String threadId`

        Identifier of the parent thread.

      - `JsonValue; type "chatkit.user_message"constant`

        - `CHATKIT_USER_MESSAGE("chatkit.user_message")`

    - `class ChatKitThreadAssistantMessageItem:`

      Assistant-authored message within a thread.

      - `String id`

        Identifier of the thread item.

      - `List<ChatKitResponseOutputText> content`

        Ordered assistant response segments.

        - `List<Annotation> annotations`

          Ordered list of annotations attached to the response text.

          - `class File:`

            Annotation that references an uploaded file.

            - `Source source`

              File attachment referenced by the annotation.

              - `String filename`

                Filename referenced by the annotation.

              - `JsonValue; type "file"constant`

                Type discriminator that is always `file`.

                - `FILE("file")`

            - `JsonValue; type "file"constant`

              Type discriminator that is always `file` for this annotation.

              - `FILE("file")`

          - `class Url:`

            Annotation that references a URL.

            - `Source source`

              URL referenced by the annotation.

              - `JsonValue; type "url"constant`

                Type discriminator that is always `url`.

                - `URL("url")`

              - `String url`

                URL referenced by the annotation.

            - `JsonValue; type "url"constant`

              Type discriminator that is always `url` for this annotation.

              - `URL("url")`

        - `String text`

          Assistant generated text.

        - `JsonValue; type "output_text"constant`

          Type discriminator that is always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `long createdAt`

        Unix timestamp (in seconds) for when the item was created.

      - `JsonValue; object_ "chatkit.thread_item"constant`

        Type discriminator that is always `chatkit.thread_item`.

        - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

      - `String threadId`

        Identifier of the parent thread.

      - `JsonValue; type "chatkit.assistant_message"constant`

        Type discriminator that is always `chatkit.assistant_message`.

        - `CHATKIT_ASSISTANT_MESSAGE("chatkit.assistant_message")`

    - `class ChatKitWidgetItem:`

      Thread item that renders a widget payload.

      - `String id`

        Identifier of the thread item.

      - `long createdAt`

        Unix timestamp (in seconds) for when the item was created.

      - `JsonValue; object_ "chatkit.thread_item"constant`

        Type discriminator that is always `chatkit.thread_item`.

        - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

      - `String threadId`

        Identifier of the parent thread.

      - `JsonValue; type "chatkit.widget"constant`

        Type discriminator that is always `chatkit.widget`.

        - `CHATKIT_WIDGET("chatkit.widget")`

      - `String widget`

        Serialized widget payload rendered in the UI.

    - `class ChatKitClientToolCall:`

      Record of a client side tool invocation initiated by the assistant.

      - `String id`

        Identifier of the thread item.

      - `String arguments`

        JSON-encoded arguments that were sent to the tool.

      - `String callId`

        Identifier for the client tool call.

      - `long createdAt`

        Unix timestamp (in seconds) for when the item was created.

      - `String name`

        Tool name that was invoked.

      - `JsonValue; object_ "chatkit.thread_item"constant`

        Type discriminator that is always `chatkit.thread_item`.

        - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

      - `Optional<String> output`

        JSON-encoded output captured from the tool. Defaults to null while execution is in progress.

      - `Status status`

        Execution status for the tool call.

        - `IN_PROGRESS("in_progress")`

        - `COMPLETED("completed")`

      - `String threadId`

        Identifier of the parent thread.

      - `JsonValue; type "chatkit.client_tool_call"constant`

        Type discriminator that is always `chatkit.client_tool_call`.

        - `CHATKIT_CLIENT_TOOL_CALL("chatkit.client_tool_call")`

    - `class ChatKitTask:`

      Task emitted by the workflow to show progress and status updates.

      - `String id`

        Identifier of the thread item.

      - `long createdAt`

        Unix timestamp (in seconds) for when the item was created.

      - `Optional<String> heading`

        Optional heading for the task. Defaults to null when not provided.

      - `JsonValue; object_ "chatkit.thread_item"constant`

        Type discriminator that is always `chatkit.thread_item`.

        - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

      - `Optional<String> summary`

        Optional summary that describes the task. Defaults to null when omitted.

      - `TaskType taskType`

        Subtype for the task.

        - `CUSTOM("custom")`

        - `THOUGHT("thought")`

      - `String threadId`

        Identifier of the parent thread.

      - `JsonValue; type "chatkit.task"constant`

        Type discriminator that is always `chatkit.task`.

        - `CHATKIT_TASK("chatkit.task")`

    - `class ChatKitTaskGroup:`

      Collection of workflow tasks grouped together in the thread.

      - `String id`

        Identifier of the thread item.

      - `long createdAt`

        Unix timestamp (in seconds) for when the item was created.

      - `JsonValue; object_ "chatkit.thread_item"constant`

        Type discriminator that is always `chatkit.thread_item`.

        - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

      - `List<Task> tasks`

        Tasks included in the group.

        - `Optional<String> heading`

          Optional heading for the grouped task. Defaults to null when not provided.

        - `Optional<String> summary`

          Optional summary that describes the grouped task. Defaults to null when omitted.

        - `Type type`

          Subtype for the grouped task.

          - `CUSTOM("custom")`

          - `THOUGHT("thought")`

      - `String threadId`

        Identifier of the parent thread.

      - `JsonValue; type "chatkit.task_group"constant`

        Type discriminator that is always `chatkit.task_group`.

        - `CHATKIT_TASK_GROUP("chatkit.task_group")`

  - `Optional<String> firstId`

    The ID of the first item in the list.

  - `boolean hasMore`

    Whether there are more items available.

  - `Optional<String> lastId`

    The ID of the last item in the list.

  - `JsonValue; object_ "list"constant`

    The type of object returned, must be `list`.

    - `LIST("list")`

##### ChatKit Thread User Message Item

- `class ChatKitThreadUserMessageItem:`

  User-authored messages within a thread.

  - `String id`

    Identifier of the thread item.

  - `List<ChatKitAttachment> attachments`

    Attachments associated with the user message. Defaults to an empty list.

    - `String id`

      Identifier for the attachment.

    - `String mimeType`

      MIME type of the attachment.

    - `String name`

      Original display name for the attachment.

    - `Optional<String> previewUrl`

      Preview URL for rendering the attachment inline.

    - `Type type`

      Attachment discriminator.

      - `IMAGE("image")`

      - `FILE("file")`

  - `List<Content> content`

    Ordered content elements supplied by the user.

    - `class InputText:`

      Text block that a user contributed to the thread.

      - `String text`

        Plain-text content supplied by the user.

      - `JsonValue; type "input_text"constant`

        Type discriminator that is always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `class QuotedText:`

      Quoted snippet that the user referenced in their message.

      - `String text`

        Quoted text content.

      - `JsonValue; type "quoted_text"constant`

        Type discriminator that is always `quoted_text`.

        - `QUOTED_TEXT("quoted_text")`

  - `long createdAt`

    Unix timestamp (in seconds) for when the item was created.

  - `Optional<InferenceOptions> inferenceOptions`

    Inference overrides applied to the message. Defaults to null when unset.

    - `Optional<String> model`

      Model name that generated the response. Defaults to null when using the session default.

    - `Optional<ToolChoice> toolChoice`

      Preferred tool to invoke. Defaults to null when ChatKit should auto-select.

      - `String id`

        Identifier of the requested tool.

  - `JsonValue; object_ "chatkit.thread_item"constant`

    Type discriminator that is always `chatkit.thread_item`.

    - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

  - `String threadId`

    Identifier of the parent thread.

  - `JsonValue; type "chatkit.user_message"constant`

    - `CHATKIT_USER_MESSAGE("chatkit.user_message")`

##### ChatKit Widget Item

- `class ChatKitWidgetItem:`

  Thread item that renders a widget payload.

  - `String id`

    Identifier of the thread item.

  - `long createdAt`

    Unix timestamp (in seconds) for when the item was created.

  - `JsonValue; object_ "chatkit.thread_item"constant`

    Type discriminator that is always `chatkit.thread_item`.

    - `CHATKIT_THREAD_ITEM("chatkit.thread_item")`

  - `String threadId`

    Identifier of the parent thread.

  - `JsonValue; type "chatkit.widget"constant`

    Type discriminator that is always `chatkit.widget`.

    - `CHATKIT_WIDGET("chatkit.widget")`

  - `String widget`

    Serialized widget payload rendered in the UI.

## Assistants

### List

`AssistantListPage beta().assistants().list(AssistantListParamsparams = AssistantListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/assistants`

Returns a list of assistants.

#### Parameters

- `AssistantListParams params`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

#### Returns

- `class Assistant:`

  Represents an `assistant` that can call the model and use tools.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the assistant was created.

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `JsonValue; object_ "assistant"constant`

    The object type, which is always `assistant`.

    - `ASSISTANT("assistant")`

  - `List<AssistantTool> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.assistants.AssistantListPage;
import com.openai.models.beta.assistants.AssistantListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AssistantListPage page = client.beta().assistants().list();
    }
}
```

### Create

`Assistant beta().assistants().create(AssistantCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/assistants`

Create an assistant with a model and instructions.

#### Parameters

- `AssistantCreateParams params`

  - `ChatModel model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

    - `GPT_5_4("gpt-5.4")`

    - `GPT_5_3_CHAT_LATEST("gpt-5.3-chat-latest")`

    - `GPT_5_2("gpt-5.2")`

    - `GPT_5_2_2025_12_11("gpt-5.2-2025-12-11")`

    - `GPT_5_2_CHAT_LATEST("gpt-5.2-chat-latest")`

    - `GPT_5_2_PRO("gpt-5.2-pro")`

    - `GPT_5_2_PRO_2025_12_11("gpt-5.2-pro-2025-12-11")`

    - `GPT_5_1("gpt-5.1")`

    - `GPT_5_1_2025_11_13("gpt-5.1-2025-11-13")`

    - `GPT_5_1_CODEX("gpt-5.1-codex")`

    - `GPT_5_1_MINI("gpt-5.1-mini")`

    - `GPT_5_1_CHAT_LATEST("gpt-5.1-chat-latest")`

    - `GPT_5("gpt-5")`

    - `GPT_5_MINI("gpt-5-mini")`

    - `GPT_5_NANO("gpt-5-nano")`

    - `GPT_5_2025_08_07("gpt-5-2025-08-07")`

    - `GPT_5_MINI_2025_08_07("gpt-5-mini-2025-08-07")`

    - `GPT_5_NANO_2025_08_07("gpt-5-nano-2025-08-07")`

    - `GPT_5_CHAT_LATEST("gpt-5-chat-latest")`

    - `GPT_4_1("gpt-4.1")`

    - `GPT_4_1_MINI("gpt-4.1-mini")`

    - `GPT_4_1_NANO("gpt-4.1-nano")`

    - `GPT_4_1_2025_04_14("gpt-4.1-2025-04-14")`

    - `GPT_4_1_MINI_2025_04_14("gpt-4.1-mini-2025-04-14")`

    - `GPT_4_1_NANO_2025_04_14("gpt-4.1-nano-2025-04-14")`

    - `O4_MINI("o4-mini")`

    - `O4_MINI_2025_04_16("o4-mini-2025-04-16")`

    - `O3("o3")`

    - `O3_2025_04_16("o3-2025-04-16")`

    - `O3_MINI("o3-mini")`

    - `O3_MINI_2025_01_31("o3-mini-2025-01-31")`

    - `O1("o1")`

    - `O1_2024_12_17("o1-2024-12-17")`

    - `O1_PREVIEW("o1-preview")`

    - `O1_PREVIEW_2024_09_12("o1-preview-2024-09-12")`

    - `O1_MINI("o1-mini")`

    - `O1_MINI_2024_09_12("o1-mini-2024-09-12")`

    - `GPT_4O("gpt-4o")`

    - `GPT_4O_2024_11_20("gpt-4o-2024-11-20")`

    - `GPT_4O_2024_08_06("gpt-4o-2024-08-06")`

    - `GPT_4O_2024_05_13("gpt-4o-2024-05-13")`

    - `GPT_4O_AUDIO_PREVIEW("gpt-4o-audio-preview")`

    - `GPT_4O_AUDIO_PREVIEW_2024_10_01("gpt-4o-audio-preview-2024-10-01")`

    - `GPT_4O_AUDIO_PREVIEW_2024_12_17("gpt-4o-audio-preview-2024-12-17")`

    - `GPT_4O_AUDIO_PREVIEW_2025_06_03("gpt-4o-audio-preview-2025-06-03")`

    - `GPT_4O_MINI_AUDIO_PREVIEW("gpt-4o-mini-audio-preview")`

    - `GPT_4O_MINI_AUDIO_PREVIEW_2024_12_17("gpt-4o-mini-audio-preview-2024-12-17")`

    - `GPT_4O_SEARCH_PREVIEW("gpt-4o-search-preview")`

    - `GPT_4O_MINI_SEARCH_PREVIEW("gpt-4o-mini-search-preview")`

    - `GPT_4O_SEARCH_PREVIEW_2025_03_11("gpt-4o-search-preview-2025-03-11")`

    - `GPT_4O_MINI_SEARCH_PREVIEW_2025_03_11("gpt-4o-mini-search-preview-2025-03-11")`

    - `CHATGPT_4O_LATEST("chatgpt-4o-latest")`

    - `CODEX_MINI_LATEST("codex-mini-latest")`

    - `GPT_4O_MINI("gpt-4o-mini")`

    - `GPT_4O_MINI_2024_07_18("gpt-4o-mini-2024-07-18")`

    - `GPT_4_TURBO("gpt-4-turbo")`

    - `GPT_4_TURBO_2024_04_09("gpt-4-turbo-2024-04-09")`

    - `GPT_4_0125_PREVIEW("gpt-4-0125-preview")`

    - `GPT_4_TURBO_PREVIEW("gpt-4-turbo-preview")`

    - `GPT_4_1106_PREVIEW("gpt-4-1106-preview")`

    - `GPT_4_VISION_PREVIEW("gpt-4-vision-preview")`

    - `GPT_4("gpt-4")`

    - `GPT_4_0314("gpt-4-0314")`

    - `GPT_4_0613("gpt-4-0613")`

    - `GPT_4_32K("gpt-4-32k")`

    - `GPT_4_32K_0314("gpt-4-32k-0314")`

    - `GPT_4_32K_0613("gpt-4-32k-0613")`

    - `GPT_3_5_TURBO("gpt-3.5-turbo")`

    - `GPT_3_5_TURBO_16K("gpt-3.5-turbo-16k")`

    - `GPT_3_5_TURBO_0301("gpt-3.5-turbo-0301")`

    - `GPT_3_5_TURBO_0613("gpt-3.5-turbo-0613")`

    - `GPT_3_5_TURBO_1106("gpt-3.5-turbo-1106")`

    - `GPT_3_5_TURBO_0125("gpt-3.5-turbo-0125")`

    - `GPT_3_5_TURBO_16K_0613("gpt-3.5-turbo-16k-0613")`

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `Optional<ReasoningEffort> reasoningEffort`

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
    reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.

    - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
    - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
    - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
    - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

      - `Optional<List<VectorStore>> vectorStores`

        A helper to create a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) with file_ids and attach it to this assistant. There can be a maximum of 1 vector store attached to the assistant.

        - `Optional<ChunkingStrategy> chunkingStrategy`

          The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

          - `JsonValue;`

            - `JsonValue; type "auto"constant`

              Always `auto`.

              - `AUTO("auto")`

          - `class Static:`

            - `InnerStatic static_`

              - `long chunkOverlapTokens`

                The number of tokens that overlap between chunks. The default value is `400`.

                Note that the overlap must not exceed half of `max_chunk_size_tokens`.

              - `long maxChunkSizeTokens`

                The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

            - `JsonValue; type "static"constant`

              Always `static`.

              - `STATIC("static")`

        - `Optional<List<String>> fileIds`

          A list of [file](https://platform.openai.com/docs/api-reference/files) IDs to add to the vector store. For vector stores created before Nov 2025, there can be a maximum of 10,000 files in a vector store. For vector stores created starting in Nov 2025, the limit is 100,000,000 files.

        - `Optional<Metadata> metadata`

          Set of 16 key-value pairs that can be attached to an object. This can be
          useful for storing additional information about the object in a structured
          format, and querying for objects via API or the dashboard.

          Keys are strings with a maximum length of 64 characters. Values are strings
          with a maximum length of 512 characters.

  - `Optional<List<AssistantTool>> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Returns

- `class Assistant:`

  Represents an `assistant` that can call the model and use tools.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the assistant was created.

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `JsonValue; object_ "assistant"constant`

    The object type, which is always `assistant`.

    - `ASSISTANT("assistant")`

  - `List<AssistantTool> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatModel;
import com.openai.models.beta.assistants.Assistant;
import com.openai.models.beta.assistants.AssistantCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AssistantCreateParams params = AssistantCreateParams.builder()
            .model(ChatModel.GPT_4O)
            .build();
        Assistant assistant = client.beta().assistants().create(params);
    }
}
```

### Retrieve

`Assistant beta().assistants().retrieve(AssistantRetrieveParamsparams = AssistantRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/assistants/{assistant_id}`

Retrieves an assistant.

#### Parameters

- `AssistantRetrieveParams params`

  - `Optional<String> assistantId`

#### Returns

- `class Assistant:`

  Represents an `assistant` that can call the model and use tools.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the assistant was created.

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `JsonValue; object_ "assistant"constant`

    The object type, which is always `assistant`.

    - `ASSISTANT("assistant")`

  - `List<AssistantTool> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.assistants.Assistant;
import com.openai.models.beta.assistants.AssistantRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Assistant assistant = client.beta().assistants().retrieve("assistant_id");
    }
}
```

### Update

`Assistant beta().assistants().update(AssistantUpdateParamsparams = AssistantUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/assistants/{assistant_id}`

Modifies an assistant.

#### Parameters

- `AssistantUpdateParams params`

  - `Optional<String> assistantId`

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<Model> model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

    - `GPT_5("gpt-5")`

    - `GPT_5_MINI("gpt-5-mini")`

    - `GPT_5_NANO("gpt-5-nano")`

    - `GPT_5_2025_08_07("gpt-5-2025-08-07")`

    - `GPT_5_MINI_2025_08_07("gpt-5-mini-2025-08-07")`

    - `GPT_5_NANO_2025_08_07("gpt-5-nano-2025-08-07")`

    - `GPT_4_1("gpt-4.1")`

    - `GPT_4_1_MINI("gpt-4.1-mini")`

    - `GPT_4_1_NANO("gpt-4.1-nano")`

    - `GPT_4_1_2025_04_14("gpt-4.1-2025-04-14")`

    - `GPT_4_1_MINI_2025_04_14("gpt-4.1-mini-2025-04-14")`

    - `GPT_4_1_NANO_2025_04_14("gpt-4.1-nano-2025-04-14")`

    - `O3_MINI("o3-mini")`

    - `O3_MINI_2025_01_31("o3-mini-2025-01-31")`

    - `O1("o1")`

    - `O1_2024_12_17("o1-2024-12-17")`

    - `GPT_4O("gpt-4o")`

    - `GPT_4O_2024_11_20("gpt-4o-2024-11-20")`

    - `GPT_4O_2024_08_06("gpt-4o-2024-08-06")`

    - `GPT_4O_2024_05_13("gpt-4o-2024-05-13")`

    - `GPT_4O_MINI("gpt-4o-mini")`

    - `GPT_4O_MINI_2024_07_18("gpt-4o-mini-2024-07-18")`

    - `GPT_4_5_PREVIEW("gpt-4.5-preview")`

    - `GPT_4_5_PREVIEW_2025_02_27("gpt-4.5-preview-2025-02-27")`

    - `GPT_4_TURBO("gpt-4-turbo")`

    - `GPT_4_TURBO_2024_04_09("gpt-4-turbo-2024-04-09")`

    - `GPT_4_0125_PREVIEW("gpt-4-0125-preview")`

    - `GPT_4_TURBO_PREVIEW("gpt-4-turbo-preview")`

    - `GPT_4_1106_PREVIEW("gpt-4-1106-preview")`

    - `GPT_4_VISION_PREVIEW("gpt-4-vision-preview")`

    - `GPT_4("gpt-4")`

    - `GPT_4_0314("gpt-4-0314")`

    - `GPT_4_0613("gpt-4-0613")`

    - `GPT_4_32K("gpt-4-32k")`

    - `GPT_4_32K_0314("gpt-4-32k-0314")`

    - `GPT_4_32K_0613("gpt-4-32k-0613")`

    - `GPT_3_5_TURBO("gpt-3.5-turbo")`

    - `GPT_3_5_TURBO_16K("gpt-3.5-turbo-16k")`

    - `GPT_3_5_TURBO_0613("gpt-3.5-turbo-0613")`

    - `GPT_3_5_TURBO_1106("gpt-3.5-turbo-1106")`

    - `GPT_3_5_TURBO_0125("gpt-3.5-turbo-0125")`

    - `GPT_3_5_TURBO_16K_0613("gpt-3.5-turbo-16k-0613")`

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `Optional<ReasoningEffort> reasoningEffort`

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
    reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.

    - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
    - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
    - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
    - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        Overrides the list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        Overrides the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<List<AssistantTool>> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Returns

- `class Assistant:`

  Represents an `assistant` that can call the model and use tools.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the assistant was created.

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `JsonValue; object_ "assistant"constant`

    The object type, which is always `assistant`.

    - `ASSISTANT("assistant")`

  - `List<AssistantTool> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.assistants.Assistant;
import com.openai.models.beta.assistants.AssistantUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Assistant assistant = client.beta().assistants().update("assistant_id");
    }
}
```

### Delete

`AssistantDeleted beta().assistants().delete(AssistantDeleteParamsparams = AssistantDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/assistants/{assistant_id}`

Delete an assistant.

#### Parameters

- `AssistantDeleteParams params`

  - `Optional<String> assistantId`

#### Returns

- `class AssistantDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "assistant.deleted"constant`

    - `ASSISTANT_DELETED("assistant.deleted")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.assistants.AssistantDeleteParams;
import com.openai.models.beta.assistants.AssistantDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AssistantDeleted assistantDeleted = client.beta().assistants().delete("assistant_id");
    }
}
```

#### Domain Types

#### Assistant

- `class Assistant:`

  Represents an `assistant` that can call the model and use tools.

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the assistant was created.

  - `Optional<String> description`

    The description of the assistant. The maximum length is 512 characters.

  - `Optional<String> instructions`

    The system instructions that the assistant uses. The maximum length is 256,000 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

  - `Optional<String> name`

    The name of the assistant. The maximum length is 256 characters.

  - `JsonValue; object_ "assistant"constant`

    The object type, which is always `assistant`.

    - `ASSISTANT("assistant")`

  - `List<AssistantTool> tools`

    A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

#### Assistant Deleted

- `class AssistantDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "assistant.deleted"constant`

    - `ASSISTANT_DELETED("assistant.deleted")`

#### Assistant Stream Event

- `class AssistantStreamEvent: A class that can be one of several variants.union`

  Represents an event emitted when streaming a Run.

  Each event in a server-sent events stream has an `event` and `data` property:

  ```
  event: thread.created
  data: {"id": "thread_123", "object": "thread", ...}
  ```

  We emit events whenever a new object is created, transitions to a new state, or is being
  streamed in parts (deltas). For example, we emit `thread.run.created` when a new run
  is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses
  to create a message during a run, we emit a `thread.message.created event`, a
  `thread.message.in_progress` event, many `thread.message.delta` events, and finally a
  `thread.message.completed` event.

  We may add additional events over time, so we recommend handling unknown events gracefully
  in your code. See the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn how to
  integrate the Assistants API with streaming.

  - `ThreadCreated`

    - `Thread data`

      Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the thread was created.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread"constant`

        The object type, which is always `thread`.

        - `THREAD("thread")`

      - `Optional<ToolResources> toolResources`

        A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

        - `Optional<CodeInterpreter> codeInterpreter`

          - `Optional<List<String>> fileIds`

            A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

        - `Optional<FileSearch> fileSearch`

          - `Optional<List<String>> vectorStoreIds`

            The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

    - `JsonValue; event "thread.created"constant`

      - `THREAD_CREATED("thread.created")`

    - `Optional<Boolean> enabled`

      Whether to enable input audio transcription.

  - `ThreadRunCreated`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.created"constant`

      - `THREAD_RUN_CREATED("thread.run.created")`

  - `ThreadRunQueued`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.queued"constant`

      - `THREAD_RUN_QUEUED("thread.run.queued")`

  - `ThreadRunInProgress`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.in_progress"constant`

      - `THREAD_RUN_IN_PROGRESS("thread.run.in_progress")`

  - `ThreadRunRequiresAction`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.requires_action"constant`

      - `THREAD_RUN_REQUIRES_ACTION("thread.run.requires_action")`

  - `ThreadRunCompleted`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.completed"constant`

      - `THREAD_RUN_COMPLETED("thread.run.completed")`

  - `ThreadRunIncomplete`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.incomplete"constant`

      - `THREAD_RUN_INCOMPLETE("thread.run.incomplete")`

  - `ThreadRunFailed`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.failed"constant`

      - `THREAD_RUN_FAILED("thread.run.failed")`

  - `ThreadRunCancelling`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.cancelling"constant`

      - `THREAD_RUN_CANCELLING("thread.run.cancelling")`

  - `ThreadRunCancelled`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.cancelled"constant`

      - `THREAD_RUN_CANCELLED("thread.run.cancelled")`

  - `ThreadRunExpired`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.expired"constant`

      - `THREAD_RUN_EXPIRED("thread.run.expired")`

  - `ThreadRunStepCreated`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.created"constant`

      - `THREAD_RUN_STEP_CREATED("thread.run.step.created")`

  - `ThreadRunStepInProgress`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.in_progress"constant`

      - `THREAD_RUN_STEP_IN_PROGRESS("thread.run.step.in_progress")`

  - `ThreadRunStepDelta`

    - `RunStepDeltaEvent data`

      Represents a run step delta i.e. any changed fields on a run step during streaming.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `RunStepDelta delta`

        The delta containing the fields that have changed on the run step.

        - `Optional<StepDetails> stepDetails`

          The details of the run step.

          - `class RunStepDeltaMessageDelta:`

            Details of the message creation by the run step.

            - `JsonValue; type "message_creation"constant`

              Always `message_creation`.

              - `MESSAGE_CREATION("message_creation")`

            - `Optional<MessageCreation> messageCreation`

              - `Optional<String> messageId`

                The ID of the message that was created by this run step.

          - `class ToolCallDeltaObject:`

            Details of the tool call.

            - `JsonValue; type "tool_calls"constant`

              Always `tool_calls`.

              - `TOOL_CALLS("tool_calls")`

            - `Optional<List<ToolCallDelta>> toolCalls`

              An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

              - `class CodeInterpreterToolCallDelta:`

                Details of the Code Interpreter tool call the run step was involved in.

                - `long index`

                  The index of the tool call in the tool calls array.

                - `JsonValue; type "code_interpreter"constant`

                  The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                  - `CODE_INTERPRETER("code_interpreter")`

                - `Optional<String> id`

                  The ID of the tool call.

                - `Optional<CodeInterpreter> codeInterpreter`

                  The Code Interpreter tool call definition.

                  - `Optional<String> input`

                    The input to the Code Interpreter tool call.

                  - `Optional<List<Output>> outputs`

                    The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                    - `class CodeInterpreterLogs:`

                      Text output from the Code Interpreter tool call as part of a run step.

                      - `long index`

                        The index of the output in the outputs array.

                      - `JsonValue; type "logs"constant`

                        Always `logs`.

                        - `LOGS("logs")`

                      - `Optional<String> logs`

                        The text output from the Code Interpreter tool call.

                    - `class CodeInterpreterOutputImage:`

                      - `long index`

                        The index of the output in the outputs array.

                      - `JsonValue; type "image"constant`

                        Always `image`.

                        - `IMAGE("image")`

                      - `Optional<Image> image`

                        - `Optional<String> fileId`

                          The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

              - `class FileSearchToolCallDelta:`

                - `JsonValue fileSearch`

                  For now, this is always going to be an empty object.

                - `long index`

                  The index of the tool call in the tool calls array.

                - `JsonValue; type "file_search"constant`

                  The type of tool call. This is always going to be `file_search` for this type of tool call.

                  - `FILE_SEARCH("file_search")`

                - `Optional<String> id`

                  The ID of the tool call object.

              - `class FunctionToolCallDelta:`

                - `long index`

                  The index of the tool call in the tool calls array.

                - `JsonValue; type "function"constant`

                  The type of tool call. This is always going to be `function` for this type of tool call.

                  - `FUNCTION("function")`

                - `Optional<String> id`

                  The ID of the tool call object.

                - `Optional<Function> function`

                  The definition of the function that was called.

                  - `Optional<String> arguments`

                    The arguments passed to the function.

                  - `Optional<String> name`

                    The name of the function.

                  - `Optional<String> output`

                    The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

      - `JsonValue; object_ "thread.run.step.delta"constant`

        The object type, which is always `thread.run.step.delta`.

        - `THREAD_RUN_STEP_DELTA("thread.run.step.delta")`

    - `JsonValue; event "thread.run.step.delta"constant`

      - `THREAD_RUN_STEP_DELTA("thread.run.step.delta")`

  - `ThreadRunStepCompleted`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.completed"constant`

      - `THREAD_RUN_STEP_COMPLETED("thread.run.step.completed")`

  - `ThreadRunStepFailed`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.failed"constant`

      - `THREAD_RUN_STEP_FAILED("thread.run.step.failed")`

  - `ThreadRunStepCancelled`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.cancelled"constant`

      - `THREAD_RUN_STEP_CANCELLED("thread.run.step.cancelled")`

  - `ThreadRunStepExpired`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.expired"constant`

      - `THREAD_RUN_STEP_EXPIRED("thread.run.step.expired")`

  - `ThreadMessageCreated`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.created"constant`

      - `THREAD_MESSAGE_CREATED("thread.message.created")`

  - `ThreadMessageInProgress`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.in_progress"constant`

      - `THREAD_MESSAGE_IN_PROGRESS("thread.message.in_progress")`

  - `ThreadMessageDelta`

    - `MessageDeltaEvent data`

      Represents a message delta i.e. any changed fields on a message during streaming.

      - `String id`

        The identifier of the message, which can be referenced in API endpoints.

      - `MessageDelta delta`

        The delta containing the fields that have changed on the Message.

        - `Optional<List<MessageContentDelta>> content`

          The content of the message in array of text and/or images.

          - `class ImageFileDeltaBlock:`

            References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

            - `long index`

              The index of the content part in the message.

            - `JsonValue; type "image_file"constant`

              Always `image_file`.

              - `IMAGE_FILE("image_file")`

            - `Optional<ImageFileDelta> imageFile`

              - `Optional<Detail> detail`

                Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> fileId`

                The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

          - `class TextDeltaBlock:`

            The text content that is part of a message.

            - `long index`

              The index of the content part in the message.

            - `JsonValue; type "text"constant`

              Always `text`.

              - `TEXT("text")`

            - `Optional<TextDelta> text`

              - `Optional<List<AnnotationDelta>> annotations`

                - `class FileCitationDeltaAnnotation:`

                  A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                  - `long index`

                    The index of the annotation in the text content part.

                  - `JsonValue; type "file_citation"constant`

                    Always `file_citation`.

                    - `FILE_CITATION("file_citation")`

                  - `Optional<Long> endIndex`

                  - `Optional<FileCitation> fileCitation`

                    - `Optional<String> fileId`

                      The ID of the specific File the citation is from.

                    - `Optional<String> quote`

                      The specific quote in the file.

                  - `Optional<Long> startIndex`

                  - `Optional<String> text`

                    The text in the message content that needs to be replaced.

                - `class FilePathDeltaAnnotation:`

                  A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                  - `long index`

                    The index of the annotation in the text content part.

                  - `JsonValue; type "file_path"constant`

                    Always `file_path`.

                    - `FILE_PATH("file_path")`

                  - `Optional<Long> endIndex`

                  - `Optional<FilePath> filePath`

                    - `Optional<String> fileId`

                      The ID of the file that was generated.

                  - `Optional<Long> startIndex`

                  - `Optional<String> text`

                    The text in the message content that needs to be replaced.

              - `Optional<String> value`

                The data that makes up the text.

          - `class RefusalDeltaBlock:`

            The refusal content that is part of a message.

            - `long index`

              The index of the refusal part in the message.

            - `JsonValue; type "refusal"constant`

              Always `refusal`.

              - `REFUSAL("refusal")`

            - `Optional<String> refusal`

          - `class ImageUrlDeltaBlock:`

            References an image URL in the content of a message.

            - `long index`

              The index of the content part in the message.

            - `JsonValue; type "image_url"constant`

              Always `image_url`.

              - `IMAGE_URL("image_url")`

            - `Optional<ImageUrlDelta> imageUrl`

              - `Optional<Detail> detail`

                Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> url`

                The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Role> role`

          The entity that produced the message. One of `user` or `assistant`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

      - `JsonValue; object_ "thread.message.delta"constant`

        The object type, which is always `thread.message.delta`.

        - `THREAD_MESSAGE_DELTA("thread.message.delta")`

    - `JsonValue; event "thread.message.delta"constant`

      - `THREAD_MESSAGE_DELTA("thread.message.delta")`

  - `ThreadMessageCompleted`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.completed"constant`

      - `THREAD_MESSAGE_COMPLETED("thread.message.completed")`

  - `ThreadMessageIncomplete`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.incomplete"constant`

      - `THREAD_MESSAGE_INCOMPLETE("thread.message.incomplete")`

  - `ErrorEvent`

    - `ErrorObject data`

      - `Optional<String> code`

      - `String message`

      - `Optional<String> param`

      - `String type`

    - `JsonValue; event "error"constant`

      - `ERROR("error")`

#### Assistant Tool

- `class AssistantTool: A class that can be one of several variants.union`

  - `class CodeInterpreterTool:`

    - `JsonValue; type "code_interpreter"constant`

      The type of tool being defined: `code_interpreter`

      - `CODE_INTERPRETER("code_interpreter")`

  - `class FileSearchTool:`

    - `JsonValue; type "file_search"constant`

      The type of tool being defined: `file_search`

      - `FILE_SEARCH("file_search")`

    - `Optional<FileSearch> fileSearch`

      Overrides for the file search tool.

      - `Optional<Long> maxNumResults`

        The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

        Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

      - `Optional<RankingOptions> rankingOptions`

        The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

        See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `double scoreThreshold`

          The score threshold for the file search. All values must be a floating point number between 0 and 1.

        - `Optional<Ranker> ranker`

          The ranker to use for the file search. If not specified will use the `auto` ranker.

          - `AUTO("auto")`

          - `DEFAULT_2024_08_21("default_2024_08_21")`

  - `class FunctionTool:`

    - `FunctionDefinition function`

      - `String name`

        The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

      - `Optional<String> description`

        A description of what the function does, used by the model to choose when and how to call the function.

      - `Optional<FunctionParameters> parameters`

        The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

        Omitting `parameters` defines a function with an empty parameter list.

      - `Optional<Boolean> strict`

        Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

    - `JsonValue; type "function"constant`

      The type of tool being defined: `function`

      - `FUNCTION("function")`

#### Code Interpreter Tool

- `class CodeInterpreterTool:`

  - `JsonValue; type "code_interpreter"constant`

    The type of tool being defined: `code_interpreter`

    - `CODE_INTERPRETER("code_interpreter")`

#### File Search Tool

- `class FileSearchTool:`

  - `JsonValue; type "file_search"constant`

    The type of tool being defined: `file_search`

    - `FILE_SEARCH("file_search")`

  - `Optional<FileSearch> fileSearch`

    Overrides for the file search tool.

    - `Optional<Long> maxNumResults`

      The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

      Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

    - `Optional<RankingOptions> rankingOptions`

      The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

      See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

      - `double scoreThreshold`

        The score threshold for the file search. All values must be a floating point number between 0 and 1.

      - `Optional<Ranker> ranker`

        The ranker to use for the file search. If not specified will use the `auto` ranker.

        - `AUTO("auto")`

        - `DEFAULT_2024_08_21("default_2024_08_21")`

#### Function Tool

- `class FunctionTool:`

  - `FunctionDefinition function`

    - `String name`

      The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

    - `Optional<String> description`

      A description of what the function does, used by the model to choose when and how to call the function.

    - `Optional<FunctionParameters> parameters`

      The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

      Omitting `parameters` defines a function with an empty parameter list.

    - `Optional<Boolean> strict`

      Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

  - `JsonValue; type "function"constant`

    The type of tool being defined: `function`

    - `FUNCTION("function")`

#### Message Stream Event

- `class MessageStreamEvent: A class that can be one of several variants.union`

  Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

  - `ThreadMessageCreated`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.created"constant`

      - `THREAD_MESSAGE_CREATED("thread.message.created")`

  - `ThreadMessageInProgress`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.in_progress"constant`

      - `THREAD_MESSAGE_IN_PROGRESS("thread.message.in_progress")`

  - `ThreadMessageDelta`

    - `MessageDeltaEvent data`

      Represents a message delta i.e. any changed fields on a message during streaming.

      - `String id`

        The identifier of the message, which can be referenced in API endpoints.

      - `MessageDelta delta`

        The delta containing the fields that have changed on the Message.

        - `Optional<List<MessageContentDelta>> content`

          The content of the message in array of text and/or images.

          - `class ImageFileDeltaBlock:`

            References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

            - `long index`

              The index of the content part in the message.

            - `JsonValue; type "image_file"constant`

              Always `image_file`.

              - `IMAGE_FILE("image_file")`

            - `Optional<ImageFileDelta> imageFile`

              - `Optional<Detail> detail`

                Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> fileId`

                The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

          - `class TextDeltaBlock:`

            The text content that is part of a message.

            - `long index`

              The index of the content part in the message.

            - `JsonValue; type "text"constant`

              Always `text`.

              - `TEXT("text")`

            - `Optional<TextDelta> text`

              - `Optional<List<AnnotationDelta>> annotations`

                - `class FileCitationDeltaAnnotation:`

                  A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                  - `long index`

                    The index of the annotation in the text content part.

                  - `JsonValue; type "file_citation"constant`

                    Always `file_citation`.

                    - `FILE_CITATION("file_citation")`

                  - `Optional<Long> endIndex`

                  - `Optional<FileCitation> fileCitation`

                    - `Optional<String> fileId`

                      The ID of the specific File the citation is from.

                    - `Optional<String> quote`

                      The specific quote in the file.

                  - `Optional<Long> startIndex`

                  - `Optional<String> text`

                    The text in the message content that needs to be replaced.

                - `class FilePathDeltaAnnotation:`

                  A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                  - `long index`

                    The index of the annotation in the text content part.

                  - `JsonValue; type "file_path"constant`

                    Always `file_path`.

                    - `FILE_PATH("file_path")`

                  - `Optional<Long> endIndex`

                  - `Optional<FilePath> filePath`

                    - `Optional<String> fileId`

                      The ID of the file that was generated.

                  - `Optional<Long> startIndex`

                  - `Optional<String> text`

                    The text in the message content that needs to be replaced.

              - `Optional<String> value`

                The data that makes up the text.

          - `class RefusalDeltaBlock:`

            The refusal content that is part of a message.

            - `long index`

              The index of the refusal part in the message.

            - `JsonValue; type "refusal"constant`

              Always `refusal`.

              - `REFUSAL("refusal")`

            - `Optional<String> refusal`

          - `class ImageUrlDeltaBlock:`

            References an image URL in the content of a message.

            - `long index`

              The index of the content part in the message.

            - `JsonValue; type "image_url"constant`

              Always `image_url`.

              - `IMAGE_URL("image_url")`

            - `Optional<ImageUrlDelta> imageUrl`

              - `Optional<Detail> detail`

                Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

              - `Optional<String> url`

                The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Role> role`

          The entity that produced the message. One of `user` or `assistant`.

          - `USER("user")`

          - `ASSISTANT("assistant")`

      - `JsonValue; object_ "thread.message.delta"constant`

        The object type, which is always `thread.message.delta`.

        - `THREAD_MESSAGE_DELTA("thread.message.delta")`

    - `JsonValue; event "thread.message.delta"constant`

      - `THREAD_MESSAGE_DELTA("thread.message.delta")`

  - `ThreadMessageCompleted`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.completed"constant`

      - `THREAD_MESSAGE_COMPLETED("thread.message.completed")`

  - `ThreadMessageIncomplete`

    - `Message data`

      Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `Optional<String> assistantId`

        If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they were added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the message was completed.

      - `List<MessageContent> content`

        The content of the message in array of text and/or images.

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlock:`

          The text content that is part of a message.

          - `Text text`

            - `List<Annotation> annotations`

              - `class FileCitationAnnotation:`

                A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

                - `long endIndex`

                - `FileCitation fileCitation`

                  - `String fileId`

                    The ID of the specific File the citation is from.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_citation"constant`

                  Always `file_citation`.

                  - `FILE_CITATION("file_citation")`

              - `class FilePathAnnotation:`

                A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

                - `long endIndex`

                - `FilePath filePath`

                  - `String fileId`

                    The ID of the file that was generated.

                - `long startIndex`

                - `String text`

                  The text in the message content that needs to be replaced.

                - `JsonValue; type "file_path"constant`

                  Always `file_path`.

                  - `FILE_PATH("file_path")`

            - `String value`

              The data that makes up the text.

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

        - `class RefusalContentBlock:`

          The refusal content generated by the assistant.

          - `String refusal`

          - `JsonValue; type "refusal"constant`

            Always `refusal`.

            - `REFUSAL("refusal")`

      - `long createdAt`

        The Unix timestamp (in seconds) for when the message was created.

      - `Optional<Long> incompleteAt`

        The Unix timestamp (in seconds) for when the message was marked as incomplete.

      - `Optional<IncompleteDetails> incompleteDetails`

        On an incomplete message, details about why the message is incomplete.

        - `Reason reason`

          The reason the message is incomplete.

          - `CONTENT_FILTER("content_filter")`

          - `MAX_TOKENS("max_tokens")`

          - `RUN_CANCELLED("run_cancelled")`

          - `RUN_EXPIRED("run_expired")`

          - `RUN_FAILED("run_failed")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.message"constant`

        The object type, which is always `thread.message`.

        - `THREAD_MESSAGE("thread.message")`

      - `Role role`

        The entity that produced the message. One of `user` or `assistant`.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<String> runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

      - `Status status`

        The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

        - `IN_PROGRESS("in_progress")`

        - `INCOMPLETE("incomplete")`

        - `COMPLETED("completed")`

      - `String threadId`

        The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

    - `JsonValue; event "thread.message.incomplete"constant`

      - `THREAD_MESSAGE_INCOMPLETE("thread.message.incomplete")`

#### Run Step Stream Event

- `class RunStepStreamEvent: A class that can be one of several variants.union`

  Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

  - `ThreadRunStepCreated`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.created"constant`

      - `THREAD_RUN_STEP_CREATED("thread.run.step.created")`

  - `ThreadRunStepInProgress`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.in_progress"constant`

      - `THREAD_RUN_STEP_IN_PROGRESS("thread.run.step.in_progress")`

  - `ThreadRunStepDelta`

    - `RunStepDeltaEvent data`

      Represents a run step delta i.e. any changed fields on a run step during streaming.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `RunStepDelta delta`

        The delta containing the fields that have changed on the run step.

        - `Optional<StepDetails> stepDetails`

          The details of the run step.

          - `class RunStepDeltaMessageDelta:`

            Details of the message creation by the run step.

            - `JsonValue; type "message_creation"constant`

              Always `message_creation`.

              - `MESSAGE_CREATION("message_creation")`

            - `Optional<MessageCreation> messageCreation`

              - `Optional<String> messageId`

                The ID of the message that was created by this run step.

          - `class ToolCallDeltaObject:`

            Details of the tool call.

            - `JsonValue; type "tool_calls"constant`

              Always `tool_calls`.

              - `TOOL_CALLS("tool_calls")`

            - `Optional<List<ToolCallDelta>> toolCalls`

              An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

              - `class CodeInterpreterToolCallDelta:`

                Details of the Code Interpreter tool call the run step was involved in.

                - `long index`

                  The index of the tool call in the tool calls array.

                - `JsonValue; type "code_interpreter"constant`

                  The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                  - `CODE_INTERPRETER("code_interpreter")`

                - `Optional<String> id`

                  The ID of the tool call.

                - `Optional<CodeInterpreter> codeInterpreter`

                  The Code Interpreter tool call definition.

                  - `Optional<String> input`

                    The input to the Code Interpreter tool call.

                  - `Optional<List<Output>> outputs`

                    The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                    - `class CodeInterpreterLogs:`

                      Text output from the Code Interpreter tool call as part of a run step.

                      - `long index`

                        The index of the output in the outputs array.

                      - `JsonValue; type "logs"constant`

                        Always `logs`.

                        - `LOGS("logs")`

                      - `Optional<String> logs`

                        The text output from the Code Interpreter tool call.

                    - `class CodeInterpreterOutputImage:`

                      - `long index`

                        The index of the output in the outputs array.

                      - `JsonValue; type "image"constant`

                        Always `image`.

                        - `IMAGE("image")`

                      - `Optional<Image> image`

                        - `Optional<String> fileId`

                          The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

              - `class FileSearchToolCallDelta:`

                - `JsonValue fileSearch`

                  For now, this is always going to be an empty object.

                - `long index`

                  The index of the tool call in the tool calls array.

                - `JsonValue; type "file_search"constant`

                  The type of tool call. This is always going to be `file_search` for this type of tool call.

                  - `FILE_SEARCH("file_search")`

                - `Optional<String> id`

                  The ID of the tool call object.

              - `class FunctionToolCallDelta:`

                - `long index`

                  The index of the tool call in the tool calls array.

                - `JsonValue; type "function"constant`

                  The type of tool call. This is always going to be `function` for this type of tool call.

                  - `FUNCTION("function")`

                - `Optional<String> id`

                  The ID of the tool call object.

                - `Optional<Function> function`

                  The definition of the function that was called.

                  - `Optional<String> arguments`

                    The arguments passed to the function.

                  - `Optional<String> name`

                    The name of the function.

                  - `Optional<String> output`

                    The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

      - `JsonValue; object_ "thread.run.step.delta"constant`

        The object type, which is always `thread.run.step.delta`.

        - `THREAD_RUN_STEP_DELTA("thread.run.step.delta")`

    - `JsonValue; event "thread.run.step.delta"constant`

      - `THREAD_RUN_STEP_DELTA("thread.run.step.delta")`

  - `ThreadRunStepCompleted`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.completed"constant`

      - `THREAD_RUN_STEP_COMPLETED("thread.run.step.completed")`

  - `ThreadRunStepFailed`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.failed"constant`

      - `THREAD_RUN_STEP_FAILED("thread.run.step.failed")`

  - `ThreadRunStepCancelled`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.cancelled"constant`

      - `THREAD_RUN_STEP_CANCELLED("thread.run.step.cancelled")`

  - `ThreadRunStepExpired`

    - `RunStep data`

      Represents a step in execution of a run.

      - `String id`

        The identifier of the run step, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run step was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run step completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run step was created.

      - `Optional<Long> expiredAt`

        The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run step failed.

      - `Optional<LastError> lastError`

        The last error associated with this run step. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error` or `rate_limit_exceeded`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `JsonValue; object_ "thread.run.step"constant`

        The object type, which is always `thread.run.step`.

        - `THREAD_RUN_STEP("thread.run.step")`

      - `String runId`

        The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

      - `Status status`

        The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

        - `IN_PROGRESS("in_progress")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `EXPIRED("expired")`

      - `StepDetails stepDetails`

        The details of the run step.

        - `class MessageCreationStepDetails:`

          Details of the message creation by the run step.

          - `MessageCreation messageCreation`

            - `String messageId`

              The ID of the message that was created by this run step.

          - `JsonValue; type "message_creation"constant`

            Always `message_creation`.

            - `MESSAGE_CREATION("message_creation")`

        - `class ToolCallsStepDetails:`

          Details of the tool call.

          - `List<ToolCall> toolCalls`

            An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

            - `class CodeInterpreterToolCall:`

              Details of the Code Interpreter tool call the run step was involved in.

              - `String id`

                The ID of the tool call.

              - `CodeInterpreter codeInterpreter`

                The Code Interpreter tool call definition.

                - `String input`

                  The input to the Code Interpreter tool call.

                - `List<Output> outputs`

                  The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                  - `class LogsOutput:`

                    Text output from the Code Interpreter tool call as part of a run step.

                    - `String logs`

                      The text output from the Code Interpreter tool call.

                    - `JsonValue; type "logs"constant`

                      Always `logs`.

                      - `LOGS("logs")`

                  - `class ImageOutput:`

                    - `Image image`

                      - `String fileId`

                        The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                    - `JsonValue; type "image"constant`

                      Always `image`.

                      - `IMAGE("image")`

              - `JsonValue; type "code_interpreter"constant`

                The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

                - `CODE_INTERPRETER("code_interpreter")`

            - `class FileSearchToolCall:`

              - `String id`

                The ID of the tool call object.

              - `FileSearch fileSearch`

                For now, this is always going to be an empty object.

                - `Optional<RankingOptions> rankingOptions`

                  The ranking options for the file search.

                  - `Ranker ranker`

                    The ranker to use for the file search. If not specified will use the `auto` ranker.

                    - `AUTO("auto")`

                    - `DEFAULT_2024_08_21("default_2024_08_21")`

                  - `double scoreThreshold`

                    The score threshold for the file search. All values must be a floating point number between 0 and 1.

                - `Optional<List<Result>> results`

                  The results of the file search.

                  - `String fileId`

                    The ID of the file that result was found in.

                  - `String fileName`

                    The name of the file that result was found in.

                  - `double score`

                    The score of the result. All values must be a floating point number between 0 and 1.

                  - `Optional<List<Content>> content`

                    The content of the result that was found. The content is only included if requested via the include query parameter.

                    - `Optional<String> text`

                      The text content of the file.

                    - `Optional<Type> type`

                      The type of the content.

                      - `TEXT("text")`

              - `JsonValue; type "file_search"constant`

                The type of tool call. This is always going to be `file_search` for this type of tool call.

                - `FILE_SEARCH("file_search")`

            - `class FunctionToolCall:`

              - `String id`

                The ID of the tool call object.

              - `Function function`

                The definition of the function that was called.

                - `String arguments`

                  The arguments passed to the function.

                - `String name`

                  The name of the function.

                - `Optional<String> output`

                  The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

              - `JsonValue; type "function"constant`

                The type of tool call. This is always going to be `function` for this type of tool call.

                - `FUNCTION("function")`

          - `JsonValue; type "tool_calls"constant`

            Always `tool_calls`.

            - `TOOL_CALLS("tool_calls")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

      - `Type type`

        The type of run step, which can be either `message_creation` or `tool_calls`.

        - `MESSAGE_CREATION("message_creation")`

        - `TOOL_CALLS("tool_calls")`

      - `Optional<Usage> usage`

        Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

        - `long completionTokens`

          Number of completion tokens used over the course of the run step.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run step.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

    - `JsonValue; event "thread.run.step.expired"constant`

      - `THREAD_RUN_STEP_EXPIRED("thread.run.step.expired")`

#### Run Stream Event

- `class RunStreamEvent: A class that can be one of several variants.union`

  Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

  - `ThreadRunCreated`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.created"constant`

      - `THREAD_RUN_CREATED("thread.run.created")`

  - `ThreadRunQueued`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.queued"constant`

      - `THREAD_RUN_QUEUED("thread.run.queued")`

  - `ThreadRunInProgress`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.in_progress"constant`

      - `THREAD_RUN_IN_PROGRESS("thread.run.in_progress")`

  - `ThreadRunRequiresAction`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.requires_action"constant`

      - `THREAD_RUN_REQUIRES_ACTION("thread.run.requires_action")`

  - `ThreadRunCompleted`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.completed"constant`

      - `THREAD_RUN_COMPLETED("thread.run.completed")`

  - `ThreadRunIncomplete`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.incomplete"constant`

      - `THREAD_RUN_INCOMPLETE("thread.run.incomplete")`

  - `ThreadRunFailed`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.failed"constant`

      - `THREAD_RUN_FAILED("thread.run.failed")`

  - `ThreadRunCancelling`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.cancelling"constant`

      - `THREAD_RUN_CANCELLING("thread.run.cancelling")`

  - `ThreadRunCancelled`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.cancelled"constant`

      - `THREAD_RUN_CANCELLED("thread.run.cancelled")`

  - `ThreadRunExpired`

    - `Run data`

      Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

      - `String id`

        The identifier, which can be referenced in API endpoints.

      - `String assistantId`

        The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

      - `Optional<Long> cancelledAt`

        The Unix timestamp (in seconds) for when the run was cancelled.

      - `Optional<Long> completedAt`

        The Unix timestamp (in seconds) for when the run was completed.

      - `long createdAt`

        The Unix timestamp (in seconds) for when the run was created.

      - `Optional<Long> expiresAt`

        The Unix timestamp (in seconds) for when the run will expire.

      - `Optional<Long> failedAt`

        The Unix timestamp (in seconds) for when the run failed.

      - `Optional<IncompleteDetails> incompleteDetails`

        Details on why the run is incomplete. Will be `null` if the run is not incomplete.

        - `Optional<Reason> reason`

          The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

          - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

          - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

      - `String instructions`

        The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `Optional<LastError> lastError`

        The last error associated with this run. Will be `null` if there are no errors.

        - `Code code`

          One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

          - `SERVER_ERROR("server_error")`

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          - `INVALID_PROMPT("invalid_prompt")`

        - `String message`

          A human-readable description of the error.

      - `Optional<Long> maxCompletionTokens`

        The maximum number of completion tokens specified to have been used over the course of the run.

      - `Optional<Long> maxPromptTokens`

        The maximum number of prompt tokens specified to have been used over the course of the run.

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

      - `String model`

        The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

      - `JsonValue; object_ "thread.run"constant`

        The object type, which is always `thread.run`.

        - `THREAD_RUN("thread.run")`

      - `boolean parallelToolCalls`

        Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

      - `Optional<RequiredAction> requiredAction`

        Details on the action required to continue the run. Will be `null` if no action is required.

        - `SubmitToolOutputs submitToolOutputs`

          Details on the tool outputs needed for this run to continue.

          - `List<RequiredActionFunctionToolCall> toolCalls`

            A list of the relevant tool calls.

            - `String id`

              The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

            - `Function function`

              The function definition.

              - `String arguments`

                The arguments that the model expects you to pass to the function.

              - `String name`

                The name of the function.

            - `JsonValue; type "function"constant`

              The type of tool call the output is required for. For now, this is always `function`.

              - `FUNCTION("function")`

        - `JsonValue; type "submit_tool_outputs"constant`

          For now, this is always `submit_tool_outputs`.

          - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

      - `Optional<AssistantResponseFormatOption> responseFormat`

        Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

        Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

        Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

        **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

        - `JsonValue;`

          - `AUTO("auto")`

        - `class ResponseFormatText:`

          Default response format. Used to generate text responses.

          - `JsonValue; type "text"constant`

            The type of response format being defined. Always `text`.

            - `TEXT("text")`

        - `class ResponseFormatJsonObject:`

          JSON object response format. An older method of generating JSON responses.
          Using `json_schema` is recommended for models that support it. Note that the
          model will not generate JSON without a system or user message instructing it
          to do so.

          - `JsonValue; type "json_object"constant`

            The type of response format being defined. Always `json_object`.

            - `JSON_OBJECT("json_object")`

        - `class ResponseFormatJsonSchema:`

          JSON Schema response format. Used to generate structured JSON responses.
          Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonSchema jsonSchema`

            Structured Outputs configuration options, including a JSON Schema.

            - `String name`

              The name of the response format. Must be a-z, A-Z, 0-9, or contain
              underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the response format is for, used by the model to
              determine how to respond in the format.

            - `Optional<Schema> schema`

              The schema for the response format, described as a JSON Schema object.
              Learn how to build JSON schemas [here](https://json-schema.org/).

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the output.
              If set to true, the model will always follow the exact schema defined
              in the `schema` field. Only a subset of JSON Schema is supported when
              `strict` is `true`. To learn more, read the [Structured Outputs
              guide](https://platform.openai.com/docs/guides/structured-outputs).

          - `JsonValue; type "json_schema"constant`

            The type of response format being defined. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Long> startedAt`

        The Unix timestamp (in seconds) for when the run was started.

      - `RunStatus status`

        The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

        - `QUEUED("queued")`

        - `IN_PROGRESS("in_progress")`

        - `REQUIRES_ACTION("requires_action")`

        - `CANCELLING("cancelling")`

        - `CANCELLED("cancelled")`

        - `FAILED("failed")`

        - `COMPLETED("completed")`

        - `INCOMPLETE("incomplete")`

        - `EXPIRED("expired")`

      - `String threadId`

        The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

      - `Optional<AssistantToolChoiceOption> toolChoice`

        Controls which (if any) tool is called by the model.
        `none` means the model will not call any tools and instead generates a message.
        `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
        `required` means the model must call one or more tools before responding to the user.
        Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

        - `Auto`

          - `NONE("none")`

          - `AUTO("auto")`

          - `REQUIRED("required")`

        - `class AssistantToolChoice:`

          Specifies a tool the model should use. Use to force the model to call a specific tool.

          - `Type type`

            The type of the tool. If type is `function`, the function name must be set

            - `FUNCTION("function")`

            - `CODE_INTERPRETER("code_interpreter")`

            - `FILE_SEARCH("file_search")`

          - `Optional<AssistantToolChoiceFunction> function`

            - `String name`

              The name of the function to call.

      - `List<AssistantTool> tools`

        The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchTool:`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

          - `Optional<FileSearch> fileSearch`

            Overrides for the file search tool.

            - `Optional<Long> maxNumResults`

              The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

              Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

              See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

              - `Optional<Ranker> ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `class FunctionTool:`

          - `FunctionDefinition function`

            - `String name`

              The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

            - `Optional<String> description`

              A description of what the function does, used by the model to choose when and how to call the function.

            - `Optional<FunctionParameters> parameters`

              The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

              Omitting `parameters` defines a function with an empty parameter list.

            - `Optional<Boolean> strict`

              Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

          - `JsonValue; type "function"constant`

            The type of tool being defined: `function`

            - `FUNCTION("function")`

      - `Optional<TruncationStrategy> truncationStrategy`

        Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

        - `Type type`

          The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

          - `AUTO("auto")`

          - `LAST_MESSAGES("last_messages")`

        - `Optional<Long> lastMessages`

          The number of most recent messages from the thread when constructing the context for the run.

      - `Optional<Usage> usage`

        Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

        - `long completionTokens`

          Number of completion tokens used over the course of the run.

        - `long promptTokens`

          Number of prompt tokens used over the course of the run.

        - `long totalTokens`

          Total number of tokens used (prompt + completion).

      - `Optional<Double> temperature`

        The sampling temperature used for this run. If not set, defaults to 1.

      - `Optional<Double> topP`

        The nucleus sampling value used for this run. If not set, defaults to 1.

    - `JsonValue; event "thread.run.expired"constant`

      - `THREAD_RUN_EXPIRED("thread.run.expired")`

#### Thread Stream Event

- `class ThreadStreamEvent:`

  Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

  - `Thread data`

    Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

    - `String id`

      The identifier, which can be referenced in API endpoints.

    - `long createdAt`

      The Unix timestamp (in seconds) for when the thread was created.

    - `Optional<Metadata> metadata`

      Set of 16 key-value pairs that can be attached to an object. This can be
      useful for storing additional information about the object in a structured
      format, and querying for objects via API or the dashboard.

      Keys are strings with a maximum length of 64 characters. Values are strings
      with a maximum length of 512 characters.

    - `JsonValue; object_ "thread"constant`

      The object type, which is always `thread`.

      - `THREAD("thread")`

    - `Optional<ToolResources> toolResources`

      A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

      - `Optional<CodeInterpreter> codeInterpreter`

        - `Optional<List<String>> fileIds`

          A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

      - `Optional<FileSearch> fileSearch`

        - `Optional<List<String>> vectorStoreIds`

          The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

  - `JsonValue; event "thread.created"constant`

    - `THREAD_CREATED("thread.created")`

  - `Optional<Boolean> enabled`

    Whether to enable input audio transcription.

## Threads

### Create

`Thread beta().threads().create(ThreadCreateParamsparams = ThreadCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads`

Create a thread.

#### Parameters

- `ThreadCreateParams params`

  - `Optional<List<Message>> messages`

    A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.

    - `Content content`

      The text contents of the message.

      - `String`

      - `List<MessageContentPartParam>`

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlockParam:`

          The text content that is part of a message.

          - `String text`

            Text content to be sent to the model

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

    - `Role role`

      The role of the entity that is creating the message. Allowed values include:

      - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
      - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

      - `USER("user")`

      - `ASSISTANT("assistant")`

    - `Optional<List<Attachment>> attachments`

      A list of files attached to the message, and the tools they should be added to.

      - `Optional<String> fileId`

        The ID of the file to attach to the message.

      - `Optional<List<Tool>> tools`

        The tools to add this file to.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `JsonValue;`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

    - `Optional<Metadata> metadata`

      Set of 16 key-value pairs that can be attached to an object. This can be
      useful for storing additional information about the object in a structured
      format, and querying for objects via API or the dashboard.

      Keys are strings with a maximum length of 64 characters. Values are strings
      with a maximum length of 512 characters.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<ToolResources> toolResources`

    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

      - `Optional<List<VectorStore>> vectorStores`

        A helper to create a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread.

        - `Optional<ChunkingStrategy> chunkingStrategy`

          The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

          - `JsonValue;`

            - `JsonValue; type "auto"constant`

              Always `auto`.

              - `AUTO("auto")`

          - `class Static:`

            - `InnerStatic static_`

              - `long chunkOverlapTokens`

                The number of tokens that overlap between chunks. The default value is `400`.

                Note that the overlap must not exceed half of `max_chunk_size_tokens`.

              - `long maxChunkSizeTokens`

                The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

            - `JsonValue; type "static"constant`

              Always `static`.

              - `STATIC("static")`

        - `Optional<List<String>> fileIds`

          A list of [file](https://platform.openai.com/docs/api-reference/files) IDs to add to the vector store. For vector stores created before Nov 2025, there can be a maximum of 10,000 files in a vector store. For vector stores created starting in Nov 2025, the limit is 100,000,000 files.

        - `Optional<Metadata> metadata`

          Set of 16 key-value pairs that can be attached to an object. This can be
          useful for storing additional information about the object in a structured
          format, and querying for objects via API or the dashboard.

          Keys are strings with a maximum length of 64 characters. Values are strings
          with a maximum length of 512 characters.

#### Returns

- `class Thread:`

  Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the thread was created.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread"constant`

    The object type, which is always `thread`.

    - `THREAD("thread")`

  - `Optional<ToolResources> toolResources`

    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.Thread;
import com.openai.models.beta.threads.ThreadCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Thread thread = client.beta().threads().create();
    }
}
```

### Create And Run

`Run beta().threads().createAndRun(ThreadCreateAndRunParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/runs`

Create a thread and run it in one request.

#### Parameters

- `ThreadCreateAndRunParams params`

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

  - `Optional<String> instructions`

    Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<ChatModel> model`

    The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

    - `GPT_5_4("gpt-5.4")`

    - `GPT_5_3_CHAT_LATEST("gpt-5.3-chat-latest")`

    - `GPT_5_2("gpt-5.2")`

    - `GPT_5_2_2025_12_11("gpt-5.2-2025-12-11")`

    - `GPT_5_2_CHAT_LATEST("gpt-5.2-chat-latest")`

    - `GPT_5_2_PRO("gpt-5.2-pro")`

    - `GPT_5_2_PRO_2025_12_11("gpt-5.2-pro-2025-12-11")`

    - `GPT_5_1("gpt-5.1")`

    - `GPT_5_1_2025_11_13("gpt-5.1-2025-11-13")`

    - `GPT_5_1_CODEX("gpt-5.1-codex")`

    - `GPT_5_1_MINI("gpt-5.1-mini")`

    - `GPT_5_1_CHAT_LATEST("gpt-5.1-chat-latest")`

    - `GPT_5("gpt-5")`

    - `GPT_5_MINI("gpt-5-mini")`

    - `GPT_5_NANO("gpt-5-nano")`

    - `GPT_5_2025_08_07("gpt-5-2025-08-07")`

    - `GPT_5_MINI_2025_08_07("gpt-5-mini-2025-08-07")`

    - `GPT_5_NANO_2025_08_07("gpt-5-nano-2025-08-07")`

    - `GPT_5_CHAT_LATEST("gpt-5-chat-latest")`

    - `GPT_4_1("gpt-4.1")`

    - `GPT_4_1_MINI("gpt-4.1-mini")`

    - `GPT_4_1_NANO("gpt-4.1-nano")`

    - `GPT_4_1_2025_04_14("gpt-4.1-2025-04-14")`

    - `GPT_4_1_MINI_2025_04_14("gpt-4.1-mini-2025-04-14")`

    - `GPT_4_1_NANO_2025_04_14("gpt-4.1-nano-2025-04-14")`

    - `O4_MINI("o4-mini")`

    - `O4_MINI_2025_04_16("o4-mini-2025-04-16")`

    - `O3("o3")`

    - `O3_2025_04_16("o3-2025-04-16")`

    - `O3_MINI("o3-mini")`

    - `O3_MINI_2025_01_31("o3-mini-2025-01-31")`

    - `O1("o1")`

    - `O1_2024_12_17("o1-2024-12-17")`

    - `O1_PREVIEW("o1-preview")`

    - `O1_PREVIEW_2024_09_12("o1-preview-2024-09-12")`

    - `O1_MINI("o1-mini")`

    - `O1_MINI_2024_09_12("o1-mini-2024-09-12")`

    - `GPT_4O("gpt-4o")`

    - `GPT_4O_2024_11_20("gpt-4o-2024-11-20")`

    - `GPT_4O_2024_08_06("gpt-4o-2024-08-06")`

    - `GPT_4O_2024_05_13("gpt-4o-2024-05-13")`

    - `GPT_4O_AUDIO_PREVIEW("gpt-4o-audio-preview")`

    - `GPT_4O_AUDIO_PREVIEW_2024_10_01("gpt-4o-audio-preview-2024-10-01")`

    - `GPT_4O_AUDIO_PREVIEW_2024_12_17("gpt-4o-audio-preview-2024-12-17")`

    - `GPT_4O_AUDIO_PREVIEW_2025_06_03("gpt-4o-audio-preview-2025-06-03")`

    - `GPT_4O_MINI_AUDIO_PREVIEW("gpt-4o-mini-audio-preview")`

    - `GPT_4O_MINI_AUDIO_PREVIEW_2024_12_17("gpt-4o-mini-audio-preview-2024-12-17")`

    - `GPT_4O_SEARCH_PREVIEW("gpt-4o-search-preview")`

    - `GPT_4O_MINI_SEARCH_PREVIEW("gpt-4o-mini-search-preview")`

    - `GPT_4O_SEARCH_PREVIEW_2025_03_11("gpt-4o-search-preview-2025-03-11")`

    - `GPT_4O_MINI_SEARCH_PREVIEW_2025_03_11("gpt-4o-mini-search-preview-2025-03-11")`

    - `CHATGPT_4O_LATEST("chatgpt-4o-latest")`

    - `CODEX_MINI_LATEST("codex-mini-latest")`

    - `GPT_4O_MINI("gpt-4o-mini")`

    - `GPT_4O_MINI_2024_07_18("gpt-4o-mini-2024-07-18")`

    - `GPT_4_TURBO("gpt-4-turbo")`

    - `GPT_4_TURBO_2024_04_09("gpt-4-turbo-2024-04-09")`

    - `GPT_4_0125_PREVIEW("gpt-4-0125-preview")`

    - `GPT_4_TURBO_PREVIEW("gpt-4-turbo-preview")`

    - `GPT_4_1106_PREVIEW("gpt-4-1106-preview")`

    - `GPT_4_VISION_PREVIEW("gpt-4-vision-preview")`

    - `GPT_4("gpt-4")`

    - `GPT_4_0314("gpt-4-0314")`

    - `GPT_4_0613("gpt-4-0613")`

    - `GPT_4_32K("gpt-4-32k")`

    - `GPT_4_32K_0314("gpt-4-32k-0314")`

    - `GPT_4_32K_0613("gpt-4-32k-0613")`

    - `GPT_3_5_TURBO("gpt-3.5-turbo")`

    - `GPT_3_5_TURBO_16K("gpt-3.5-turbo-16k")`

    - `GPT_3_5_TURBO_0301("gpt-3.5-turbo-0301")`

    - `GPT_3_5_TURBO_0613("gpt-3.5-turbo-0613")`

    - `GPT_3_5_TURBO_1106("gpt-3.5-turbo-1106")`

    - `GPT_3_5_TURBO_0125("gpt-3.5-turbo-0125")`

    - `GPT_3_5_TURBO_16K_0613("gpt-3.5-turbo-16k-0613")`

  - `Optional<Boolean> parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<Thread> thread`

    Options to create a new thread. If no thread is provided when running a
    request, an empty thread will be created.

    - `Optional<List<Message>> messages`

      A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.

      - `Content content`

        The text contents of the message.

        - `String`

        - `List<MessageContentPartParam>`

          - `class ImageFileContentBlock:`

            References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

            - `ImageFile imageFile`

              - `String fileId`

                The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

              - `Optional<Detail> detail`

                Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

            - `JsonValue; type "image_file"constant`

              Always `image_file`.

              - `IMAGE_FILE("image_file")`

          - `class ImageUrlContentBlock:`

            References an image URL in the content of a message.

            - `ImageUrl imageUrl`

              - `String url`

                The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

              - `Optional<Detail> detail`

                Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

                - `AUTO("auto")`

                - `LOW("low")`

                - `HIGH("high")`

            - `JsonValue; type "image_url"constant`

              The type of the content part.

              - `IMAGE_URL("image_url")`

          - `class TextContentBlockParam:`

            The text content that is part of a message.

            - `String text`

              Text content to be sent to the model

            - `JsonValue; type "text"constant`

              Always `text`.

              - `TEXT("text")`

      - `Role role`

        The role of the entity that is creating the message. Allowed values include:

        - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
        - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `Optional<List<Attachment>> attachments`

        A list of files attached to the message, and the tools they should be added to.

        - `Optional<String> fileId`

          The ID of the file to attach to the message.

        - `Optional<List<Tool>> tools`

          The tools to add this file to.

          - `class CodeInterpreterTool:`

            - `JsonValue; type "code_interpreter"constant`

              The type of tool being defined: `code_interpreter`

              - `CODE_INTERPRETER("code_interpreter")`

          - `JsonValue;`

            - `JsonValue; type "file_search"constant`

              The type of tool being defined: `file_search`

              - `FILE_SEARCH("file_search")`

      - `Optional<Metadata> metadata`

        Set of 16 key-value pairs that can be attached to an object. This can be
        useful for storing additional information about the object in a structured
        format, and querying for objects via API or the dashboard.

        Keys are strings with a maximum length of 64 characters. Values are strings
        with a maximum length of 512 characters.

    - `Optional<Metadata> metadata`

      Set of 16 key-value pairs that can be attached to an object. This can be
      useful for storing additional information about the object in a structured
      format, and querying for objects via API or the dashboard.

      Keys are strings with a maximum length of 64 characters. Values are strings
      with a maximum length of 512 characters.

    - `Optional<ToolResources> toolResources`

      A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

      - `Optional<CodeInterpreter> codeInterpreter`

        - `Optional<List<String>> fileIds`

          A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

      - `Optional<FileSearch> fileSearch`

        - `Optional<List<String>> vectorStoreIds`

          The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

        - `Optional<List<VectorStore>> vectorStores`

          A helper to create a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) with file_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread.

          - `Optional<ChunkingStrategy> chunkingStrategy`

            The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

            - `JsonValue;`

              - `JsonValue; type "auto"constant`

                Always `auto`.

                - `AUTO("auto")`

            - `class Static:`

              - `InnerStatic static_`

                - `long chunkOverlapTokens`

                  The number of tokens that overlap between chunks. The default value is `400`.

                  Note that the overlap must not exceed half of `max_chunk_size_tokens`.

                - `long maxChunkSizeTokens`

                  The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

              - `JsonValue; type "static"constant`

                Always `static`.

                - `STATIC("static")`

          - `Optional<List<String>> fileIds`

            A list of [file](https://platform.openai.com/docs/api-reference/files) IDs to add to the vector store. For vector stores created before Nov 2025, there can be a maximum of 10,000 files in a vector store. For vector stores created starting in Nov 2025, the limit is 100,000,000 files.

          - `Optional<Metadata> metadata`

            Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured
            format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings
            with a maximum length of 512 characters.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

  - `Optional<ToolResources> toolResources`

    A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

  - `Optional<List<AssistantTool>> tools`

    Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

#### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.ThreadCreateAndRunParams;
import com.openai.models.beta.threads.runs.Run;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadCreateAndRunParams params = ThreadCreateAndRunParams.builder()
            .assistantId("assistant_id")
            .build();
        Run run = client.beta().threads().createAndRun(params);
    }
}
```

### Retrieve

`Thread beta().threads().retrieve(ThreadRetrieveParamsparams = ThreadRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}`

Retrieves a thread.

#### Parameters

- `ThreadRetrieveParams params`

  - `Optional<String> threadId`

#### Returns

- `class Thread:`

  Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the thread was created.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread"constant`

    The object type, which is always `thread`.

    - `THREAD("thread")`

  - `Optional<ToolResources> toolResources`

    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.Thread;
import com.openai.models.beta.threads.ThreadRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Thread thread = client.beta().threads().retrieve("thread_id");
    }
}
```

### Update

`Thread beta().threads().update(ThreadUpdateParamsparams = ThreadUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}`

Modifies a thread.

#### Parameters

- `ThreadUpdateParams params`

  - `Optional<String> threadId`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<ToolResources> toolResources`

    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

#### Returns

- `class Thread:`

  Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the thread was created.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread"constant`

    The object type, which is always `thread`.

    - `THREAD("thread")`

  - `Optional<ToolResources> toolResources`

    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.Thread;
import com.openai.models.beta.threads.ThreadUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Thread thread = client.beta().threads().update("thread_id");
    }
}
```

### Delete

`ThreadDeleted beta().threads().delete(ThreadDeleteParamsparams = ThreadDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/threads/{thread_id}`

Delete a thread.

#### Parameters

- `ThreadDeleteParams params`

  - `Optional<String> threadId`

#### Returns

- `class ThreadDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "thread.deleted"constant`

    - `THREAD_DELETED("thread.deleted")`

#### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.ThreadDeleteParams;
import com.openai.models.beta.threads.ThreadDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ThreadDeleted threadDeleted = client.beta().threads().delete("thread_id");
    }
}
```

#### Domain Types

#### Assistant Response Format Option

- `class AssistantResponseFormatOption: A class that can be one of several variants.union`

  Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

  Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

  Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

  **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

  - `JsonValue;`

    - `AUTO("auto")`

  - `class ResponseFormatText:`

    Default response format. Used to generate text responses.

    - `JsonValue; type "text"constant`

      The type of response format being defined. Always `text`.

      - `TEXT("text")`

  - `class ResponseFormatJsonObject:`

    JSON object response format. An older method of generating JSON responses.
    Using `json_schema` is recommended for models that support it. Note that the
    model will not generate JSON without a system or user message instructing it
    to do so.

    - `JsonValue; type "json_object"constant`

      The type of response format being defined. Always `json_object`.

      - `JSON_OBJECT("json_object")`

  - `class ResponseFormatJsonSchema:`

    JSON Schema response format. Used to generate structured JSON responses.
    Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

    - `JsonSchema jsonSchema`

      Structured Outputs configuration options, including a JSON Schema.

      - `String name`

        The name of the response format. Must be a-z, A-Z, 0-9, or contain
        underscores and dashes, with a maximum length of 64.

      - `Optional<String> description`

        A description of what the response format is for, used by the model to
        determine how to respond in the format.

      - `Optional<Schema> schema`

        The schema for the response format, described as a JSON Schema object.
        Learn how to build JSON schemas [here](https://json-schema.org/).

      - `Optional<Boolean> strict`

        Whether to enable strict schema adherence when generating the output.
        If set to true, the model will always follow the exact schema defined
        in the `schema` field. Only a subset of JSON Schema is supported when
        `strict` is `true`. To learn more, read the [Structured Outputs
        guide](https://platform.openai.com/docs/guides/structured-outputs).

    - `JsonValue; type "json_schema"constant`

      The type of response format being defined. Always `json_schema`.

      - `JSON_SCHEMA("json_schema")`

#### Assistant Tool Choice

- `class AssistantToolChoice:`

  Specifies a tool the model should use. Use to force the model to call a specific tool.

  - `Type type`

    The type of the tool. If type is `function`, the function name must be set

    - `FUNCTION("function")`

    - `CODE_INTERPRETER("code_interpreter")`

    - `FILE_SEARCH("file_search")`

  - `Optional<AssistantToolChoiceFunction> function`

    - `String name`

      The name of the function to call.

#### Assistant Tool Choice Function

- `class AssistantToolChoiceFunction:`

  - `String name`

    The name of the function to call.

#### Assistant Tool Choice Option

- `class AssistantToolChoiceOption: A class that can be one of several variants.union`

  Controls which (if any) tool is called by the model.
  `none` means the model will not call any tools and instead generates a message.
  `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
  `required` means the model must call one or more tools before responding to the user.
  Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

  - `Auto`

    - `NONE("none")`

    - `AUTO("auto")`

    - `REQUIRED("required")`

  - `class AssistantToolChoice:`

    Specifies a tool the model should use. Use to force the model to call a specific tool.

    - `Type type`

      The type of the tool. If type is `function`, the function name must be set

      - `FUNCTION("function")`

      - `CODE_INTERPRETER("code_interpreter")`

      - `FILE_SEARCH("file_search")`

    - `Optional<AssistantToolChoiceFunction> function`

      - `String name`

        The name of the function to call.

#### Thread

- `class Thread:`

  Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the thread was created.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread"constant`

    The object type, which is always `thread`.

    - `THREAD("thread")`

  - `Optional<ToolResources> toolResources`

    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

    - `Optional<CodeInterpreter> codeInterpreter`

      - `Optional<List<String>> fileIds`

        A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

    - `Optional<FileSearch> fileSearch`

      - `Optional<List<String>> vectorStoreIds`

        The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

#### Thread Deleted

- `class ThreadDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "thread.deleted"constant`

    - `THREAD_DELETED("thread.deleted")`

### Runs

#### List

`RunListPage beta().threads().runs().list(RunListParamsparams = RunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}/runs`

Returns a list of runs belonging to a thread.

##### Parameters

- `RunListParams params`

  - `Optional<String> threadId`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

##### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.RunListPage;
import com.openai.models.beta.threads.runs.RunListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunListPage page = client.beta().threads().runs().list("thread_id");
    }
}
```

#### Create

`Run beta().threads().runs().create(RunCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}/runs`

Create a run.

##### Parameters

- `RunCreateParams params`

  - `Optional<String> threadId`

  - `Optional<List<RunStepInclude>> include`

    A list of additional fields to include in the response. Currently the only supported value is `step_details.tool_calls[*].file_search.results[*].content` to fetch the file search result content.

    See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

    - `STEP_DETAILS_TOOL_CALLS_FILE_SEARCH_RESULTS_CONTENT("step_details.tool_calls[*].file_search.results[*].content")`

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

  - `Optional<String> additionalInstructions`

    Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

  - `Optional<List<AdditionalMessage>> additionalMessages`

    Adds additional messages to the thread before creating the run.

    - `Content content`

      The text contents of the message.

      - `String`

      - `List<MessageContentPartParam>`

        - `class ImageFileContentBlock:`

          References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

          - `ImageFile imageFile`

            - `String fileId`

              The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

            - `Optional<Detail> detail`

              Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_file"constant`

            Always `image_file`.

            - `IMAGE_FILE("image_file")`

        - `class ImageUrlContentBlock:`

          References an image URL in the content of a message.

          - `ImageUrl imageUrl`

            - `String url`

              The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

            - `Optional<Detail> detail`

              Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

              - `AUTO("auto")`

              - `LOW("low")`

              - `HIGH("high")`

          - `JsonValue; type "image_url"constant`

            The type of the content part.

            - `IMAGE_URL("image_url")`

        - `class TextContentBlockParam:`

          The text content that is part of a message.

          - `String text`

            Text content to be sent to the model

          - `JsonValue; type "text"constant`

            Always `text`.

            - `TEXT("text")`

    - `Role role`

      The role of the entity that is creating the message. Allowed values include:

      - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
      - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

      - `USER("user")`

      - `ASSISTANT("assistant")`

    - `Optional<List<Attachment>> attachments`

      A list of files attached to the message, and the tools they should be added to.

      - `Optional<String> fileId`

        The ID of the file to attach to the message.

      - `Optional<List<Tool>> tools`

        The tools to add this file to.

        - `class CodeInterpreterTool:`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool being defined: `code_interpreter`

            - `CODE_INTERPRETER("code_interpreter")`

        - `JsonValue;`

          - `JsonValue; type "file_search"constant`

            The type of tool being defined: `file_search`

            - `FILE_SEARCH("file_search")`

    - `Optional<Metadata> metadata`

      Set of 16 key-value pairs that can be attached to an object. This can be
      useful for storing additional information about the object in a structured
      format, and querying for objects via API or the dashboard.

      Keys are strings with a maximum length of 64 characters. Values are strings
      with a maximum length of 512 characters.

  - `Optional<String> instructions`

    Overrides the [instructions](https://platform.openai.com/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `Optional<ChatModel> model`

    The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

    - `GPT_5_4("gpt-5.4")`

    - `GPT_5_3_CHAT_LATEST("gpt-5.3-chat-latest")`

    - `GPT_5_2("gpt-5.2")`

    - `GPT_5_2_2025_12_11("gpt-5.2-2025-12-11")`

    - `GPT_5_2_CHAT_LATEST("gpt-5.2-chat-latest")`

    - `GPT_5_2_PRO("gpt-5.2-pro")`

    - `GPT_5_2_PRO_2025_12_11("gpt-5.2-pro-2025-12-11")`

    - `GPT_5_1("gpt-5.1")`

    - `GPT_5_1_2025_11_13("gpt-5.1-2025-11-13")`

    - `GPT_5_1_CODEX("gpt-5.1-codex")`

    - `GPT_5_1_MINI("gpt-5.1-mini")`

    - `GPT_5_1_CHAT_LATEST("gpt-5.1-chat-latest")`

    - `GPT_5("gpt-5")`

    - `GPT_5_MINI("gpt-5-mini")`

    - `GPT_5_NANO("gpt-5-nano")`

    - `GPT_5_2025_08_07("gpt-5-2025-08-07")`

    - `GPT_5_MINI_2025_08_07("gpt-5-mini-2025-08-07")`

    - `GPT_5_NANO_2025_08_07("gpt-5-nano-2025-08-07")`

    - `GPT_5_CHAT_LATEST("gpt-5-chat-latest")`

    - `GPT_4_1("gpt-4.1")`

    - `GPT_4_1_MINI("gpt-4.1-mini")`

    - `GPT_4_1_NANO("gpt-4.1-nano")`

    - `GPT_4_1_2025_04_14("gpt-4.1-2025-04-14")`

    - `GPT_4_1_MINI_2025_04_14("gpt-4.1-mini-2025-04-14")`

    - `GPT_4_1_NANO_2025_04_14("gpt-4.1-nano-2025-04-14")`

    - `O4_MINI("o4-mini")`

    - `O4_MINI_2025_04_16("o4-mini-2025-04-16")`

    - `O3("o3")`

    - `O3_2025_04_16("o3-2025-04-16")`

    - `O3_MINI("o3-mini")`

    - `O3_MINI_2025_01_31("o3-mini-2025-01-31")`

    - `O1("o1")`

    - `O1_2024_12_17("o1-2024-12-17")`

    - `O1_PREVIEW("o1-preview")`

    - `O1_PREVIEW_2024_09_12("o1-preview-2024-09-12")`

    - `O1_MINI("o1-mini")`

    - `O1_MINI_2024_09_12("o1-mini-2024-09-12")`

    - `GPT_4O("gpt-4o")`

    - `GPT_4O_2024_11_20("gpt-4o-2024-11-20")`

    - `GPT_4O_2024_08_06("gpt-4o-2024-08-06")`

    - `GPT_4O_2024_05_13("gpt-4o-2024-05-13")`

    - `GPT_4O_AUDIO_PREVIEW("gpt-4o-audio-preview")`

    - `GPT_4O_AUDIO_PREVIEW_2024_10_01("gpt-4o-audio-preview-2024-10-01")`

    - `GPT_4O_AUDIO_PREVIEW_2024_12_17("gpt-4o-audio-preview-2024-12-17")`

    - `GPT_4O_AUDIO_PREVIEW_2025_06_03("gpt-4o-audio-preview-2025-06-03")`

    - `GPT_4O_MINI_AUDIO_PREVIEW("gpt-4o-mini-audio-preview")`

    - `GPT_4O_MINI_AUDIO_PREVIEW_2024_12_17("gpt-4o-mini-audio-preview-2024-12-17")`

    - `GPT_4O_SEARCH_PREVIEW("gpt-4o-search-preview")`

    - `GPT_4O_MINI_SEARCH_PREVIEW("gpt-4o-mini-search-preview")`

    - `GPT_4O_SEARCH_PREVIEW_2025_03_11("gpt-4o-search-preview-2025-03-11")`

    - `GPT_4O_MINI_SEARCH_PREVIEW_2025_03_11("gpt-4o-mini-search-preview-2025-03-11")`

    - `CHATGPT_4O_LATEST("chatgpt-4o-latest")`

    - `CODEX_MINI_LATEST("codex-mini-latest")`

    - `GPT_4O_MINI("gpt-4o-mini")`

    - `GPT_4O_MINI_2024_07_18("gpt-4o-mini-2024-07-18")`

    - `GPT_4_TURBO("gpt-4-turbo")`

    - `GPT_4_TURBO_2024_04_09("gpt-4-turbo-2024-04-09")`

    - `GPT_4_0125_PREVIEW("gpt-4-0125-preview")`

    - `GPT_4_TURBO_PREVIEW("gpt-4-turbo-preview")`

    - `GPT_4_1106_PREVIEW("gpt-4-1106-preview")`

    - `GPT_4_VISION_PREVIEW("gpt-4-vision-preview")`

    - `GPT_4("gpt-4")`

    - `GPT_4_0314("gpt-4-0314")`

    - `GPT_4_0613("gpt-4-0613")`

    - `GPT_4_32K("gpt-4-32k")`

    - `GPT_4_32K_0314("gpt-4-32k-0314")`

    - `GPT_4_32K_0613("gpt-4-32k-0613")`

    - `GPT_3_5_TURBO("gpt-3.5-turbo")`

    - `GPT_3_5_TURBO_16K("gpt-3.5-turbo-16k")`

    - `GPT_3_5_TURBO_0301("gpt-3.5-turbo-0301")`

    - `GPT_3_5_TURBO_0613("gpt-3.5-turbo-0613")`

    - `GPT_3_5_TURBO_1106("gpt-3.5-turbo-1106")`

    - `GPT_3_5_TURBO_0125("gpt-3.5-turbo-0125")`

    - `GPT_3_5_TURBO_16K_0613("gpt-3.5-turbo-16k-0613")`

  - `Optional<Boolean> parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<ReasoningEffort> reasoningEffort`

    Constrains effort on reasoning for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
    reasoning effort can result in faster responses and fewer tokens used
    on reasoning in a response.

    - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
    - All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
    - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
    - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

  - `Optional<Double> temperature`

    What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

  - `Optional<List<AssistantTool>> tools`

    Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<Double> topP`

    An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

##### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.Run;
import com.openai.models.beta.threads.runs.RunCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunCreateParams params = RunCreateParams.builder()
            .threadId("thread_id")
            .assistantId("assistant_id")
            .build();
        Run run = client.beta().threads().runs().create(params);
    }
}
```

#### Retrieve

`Run beta().threads().runs().retrieve(RunRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}/runs/{run_id}`

Retrieves a run.

##### Parameters

- `RunRetrieveParams params`

  - `String threadId`

  - `Optional<String> runId`

##### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.Run;
import com.openai.models.beta.threads.runs.RunRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunRetrieveParams params = RunRetrieveParams.builder()
            .threadId("thread_id")
            .runId("run_id")
            .build();
        Run run = client.beta().threads().runs().retrieve(params);
    }
}
```

#### Update

`Run beta().threads().runs().update(RunUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}/runs/{run_id}`

Modifies a run.

##### Parameters

- `RunUpdateParams params`

  - `String threadId`

  - `Optional<String> runId`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

##### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.Run;
import com.openai.models.beta.threads.runs.RunUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunUpdateParams params = RunUpdateParams.builder()
            .threadId("thread_id")
            .runId("run_id")
            .build();
        Run run = client.beta().threads().runs().update(params);
    }
}
```

#### Submit Tool Outputs

`Run beta().threads().runs().submitToolOutputs(RunSubmitToolOutputsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}/runs/{run_id}/submit_tool_outputs`

When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.

##### Parameters

- `RunSubmitToolOutputsParams params`

  - `String threadId`

  - `Optional<String> runId`

  - `List<ToolOutput> toolOutputs`

    A list of tools for which the outputs are being submitted.

    - `Optional<String> output`

      The output of the tool call to be submitted to continue the run.

    - `Optional<String> toolCallId`

      The ID of the tool call in the `required_action` object within the run object the output is being submitted for.

##### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.Run;
import com.openai.models.beta.threads.runs.RunSubmitToolOutputsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunSubmitToolOutputsParams params = RunSubmitToolOutputsParams.builder()
            .threadId("thread_id")
            .runId("run_id")
            .addToolOutput(RunSubmitToolOutputsParams.ToolOutput.builder().build())
            .build();
        Run run = client.beta().threads().runs().submitToolOutputs(params);
    }
}
```

#### Cancel

`Run beta().threads().runs().cancel(RunCancelParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}/runs/{run_id}/cancel`

Cancels a run that is `in_progress`.

##### Parameters

- `RunCancelParams params`

  - `String threadId`

  - `Optional<String> runId`

##### Returns

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.Run;
import com.openai.models.beta.threads.runs.RunCancelParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunCancelParams params = RunCancelParams.builder()
            .threadId("thread_id")
            .runId("run_id")
            .build();
        Run run = client.beta().threads().runs().cancel(params);
    }
}
```

##### Domain Types

##### Required Action Function Tool Call

- `class RequiredActionFunctionToolCall:`

  Tool call objects

  - `String id`

    The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

  - `Function function`

    The function definition.

    - `String arguments`

      The arguments that the model expects you to pass to the function.

    - `String name`

      The name of the function.

  - `JsonValue; type "function"constant`

    The type of tool call the output is required for. For now, this is always `function`.

    - `FUNCTION("function")`

##### Run

- `class Run:`

  Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run was completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run was created.

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) for when the run will expire.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run failed.

  - `Optional<IncompleteDetails> incompleteDetails`

    Details on why the run is incomplete. Will be `null` if the run is not incomplete.

    - `Optional<Reason> reason`

      The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

      - `MAX_COMPLETION_TOKENS("max_completion_tokens")`

      - `MAX_PROMPT_TOKENS("max_prompt_tokens")`

  - `String instructions`

    The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `Optional<LastError> lastError`

    The last error associated with this run. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      - `INVALID_PROMPT("invalid_prompt")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Long> maxCompletionTokens`

    The maximum number of completion tokens specified to have been used over the course of the run.

  - `Optional<Long> maxPromptTokens`

    The maximum number of prompt tokens specified to have been used over the course of the run.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `String model`

    The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

  - `JsonValue; object_ "thread.run"constant`

    The object type, which is always `thread.run`.

    - `THREAD_RUN("thread.run")`

  - `boolean parallelToolCalls`

    Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

  - `Optional<RequiredAction> requiredAction`

    Details on the action required to continue the run. Will be `null` if no action is required.

    - `SubmitToolOutputs submitToolOutputs`

      Details on the tool outputs needed for this run to continue.

      - `List<RequiredActionFunctionToolCall> toolCalls`

        A list of the relevant tool calls.

        - `String id`

          The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

        - `Function function`

          The function definition.

          - `String arguments`

            The arguments that the model expects you to pass to the function.

          - `String name`

            The name of the function.

        - `JsonValue; type "function"constant`

          The type of tool call the output is required for. For now, this is always `function`.

          - `FUNCTION("function")`

    - `JsonValue; type "submit_tool_outputs"constant`

      For now, this is always `submit_tool_outputs`.

      - `SUBMIT_TOOL_OUTPUTS("submit_tool_outputs")`

  - `Optional<AssistantResponseFormatOption> responseFormat`

    Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

    - `JsonValue;`

      - `AUTO("auto")`

    - `class ResponseFormatText:`

      Default response format. Used to generate text responses.

      - `JsonValue; type "text"constant`

        The type of response format being defined. Always `text`.

        - `TEXT("text")`

    - `class ResponseFormatJsonObject:`

      JSON object response format. An older method of generating JSON responses.
      Using `json_schema` is recommended for models that support it. Note that the
      model will not generate JSON without a system or user message instructing it
      to do so.

      - `JsonValue; type "json_object"constant`

        The type of response format being defined. Always `json_object`.

        - `JSON_OBJECT("json_object")`

    - `class ResponseFormatJsonSchema:`

      JSON Schema response format. Used to generate structured JSON responses.
      Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonSchema jsonSchema`

        Structured Outputs configuration options, including a JSON Schema.

        - `String name`

          The name of the response format. Must be a-z, A-Z, 0-9, or contain
          underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the response format is for, used by the model to
          determine how to respond in the format.

        - `Optional<Schema> schema`

          The schema for the response format, described as a JSON Schema object.
          Learn how to build JSON schemas [here](https://json-schema.org/).

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the output.
          If set to true, the model will always follow the exact schema defined
          in the `schema` field. Only a subset of JSON Schema is supported when
          `strict` is `true`. To learn more, read the [Structured Outputs
          guide](https://platform.openai.com/docs/guides/structured-outputs).

      - `JsonValue; type "json_schema"constant`

        The type of response format being defined. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Long> startedAt`

    The Unix timestamp (in seconds) for when the run was started.

  - `RunStatus status`

    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

    - `QUEUED("queued")`

    - `IN_PROGRESS("in_progress")`

    - `REQUIRES_ACTION("requires_action")`

    - `CANCELLING("cancelling")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `INCOMPLETE("incomplete")`

    - `EXPIRED("expired")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

  - `Optional<AssistantToolChoiceOption> toolChoice`

    Controls which (if any) tool is called by the model.
    `none` means the model will not call any tools and instead generates a message.
    `auto` is the default value and means the model can pick between generating a message or calling one or more tools.
    `required` means the model must call one or more tools before responding to the user.
    Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

    - `Auto`

      - `NONE("none")`

      - `AUTO("auto")`

      - `REQUIRED("required")`

    - `class AssistantToolChoice:`

      Specifies a tool the model should use. Use to force the model to call a specific tool.

      - `Type type`

        The type of the tool. If type is `function`, the function name must be set

        - `FUNCTION("function")`

        - `CODE_INTERPRETER("code_interpreter")`

        - `FILE_SEARCH("file_search")`

      - `Optional<AssistantToolChoiceFunction> function`

        - `String name`

          The name of the function to call.

  - `List<AssistantTool> tools`

    The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

    - `class CodeInterpreterTool:`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool being defined: `code_interpreter`

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchTool:`

      - `JsonValue; type "file_search"constant`

        The type of tool being defined: `file_search`

        - `FILE_SEARCH("file_search")`

      - `Optional<FileSearch> fileSearch`

        Overrides for the file search tool.

        - `Optional<Long> maxNumResults`

          The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

          Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.

          See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

          - `Optional<Ranker> ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

    - `class FunctionTool:`

      - `FunctionDefinition function`

        - `String name`

          The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

        - `Optional<String> description`

          A description of what the function does, used by the model to choose when and how to call the function.

        - `Optional<FunctionParameters> parameters`

          The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

          Omitting `parameters` defines a function with an empty parameter list.

        - `Optional<Boolean> strict`

          Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

      - `JsonValue; type "function"constant`

        The type of tool being defined: `function`

        - `FUNCTION("function")`

  - `Optional<TruncationStrategy> truncationStrategy`

    Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

    - `Type type`

      The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

      - `AUTO("auto")`

      - `LAST_MESSAGES("last_messages")`

    - `Optional<Long> lastMessages`

      The number of most recent messages from the thread when constructing the context for the run.

  - `Optional<Usage> usage`

    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

    - `long completionTokens`

      Number of completion tokens used over the course of the run.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

  - `Optional<Double> temperature`

    The sampling temperature used for this run. If not set, defaults to 1.

  - `Optional<Double> topP`

    The nucleus sampling value used for this run. If not set, defaults to 1.

##### Run Status

- `enum RunStatus:`

  The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

  - `QUEUED("queued")`

  - `IN_PROGRESS("in_progress")`

  - `REQUIRES_ACTION("requires_action")`

  - `CANCELLING("cancelling")`

  - `CANCELLED("cancelled")`

  - `FAILED("failed")`

  - `COMPLETED("completed")`

  - `INCOMPLETE("incomplete")`

  - `EXPIRED("expired")`

#### Steps

##### List

`StepListPage beta().threads().runs().steps().list(StepListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}/runs/{run_id}/steps`

Returns a list of run steps belonging to a run.

###### Parameters

- `StepListParams params`

  - `String threadId`

  - `Optional<String> runId`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<List<RunStepInclude>> include`

    A list of additional fields to include in the response. Currently the only supported value is `step_details.tool_calls[*].file_search.results[*].content` to fetch the file search result content.

    See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

    - `STEP_DETAILS_TOOL_CALLS_FILE_SEARCH_RESULTS_CONTENT("step_details.tool_calls[*].file_search.results[*].content")`

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

###### Returns

- `class RunStep:`

  Represents a step in execution of a run.

  - `String id`

    The identifier of the run step, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run step was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run step completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run step was created.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run step failed.

  - `Optional<LastError> lastError`

    The last error associated with this run step. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error` or `rate_limit_exceeded`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.run.step"constant`

    The object type, which is always `thread.run.step`.

    - `THREAD_RUN_STEP("thread.run.step")`

  - `String runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

  - `Status status`

    The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

    - `IN_PROGRESS("in_progress")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

  - `StepDetails stepDetails`

    The details of the run step.

    - `class MessageCreationStepDetails:`

      Details of the message creation by the run step.

      - `MessageCreation messageCreation`

        - `String messageId`

          The ID of the message that was created by this run step.

      - `JsonValue; type "message_creation"constant`

        Always `message_creation`.

        - `MESSAGE_CREATION("message_creation")`

    - `class ToolCallsStepDetails:`

      Details of the tool call.

      - `List<ToolCall> toolCalls`

        An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

        - `class CodeInterpreterToolCall:`

          Details of the Code Interpreter tool call the run step was involved in.

          - `String id`

            The ID of the tool call.

          - `CodeInterpreter codeInterpreter`

            The Code Interpreter tool call definition.

            - `String input`

              The input to the Code Interpreter tool call.

            - `List<Output> outputs`

              The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

              - `class LogsOutput:`

                Text output from the Code Interpreter tool call as part of a run step.

                - `String logs`

                  The text output from the Code Interpreter tool call.

                - `JsonValue; type "logs"constant`

                  Always `logs`.

                  - `LOGS("logs")`

              - `class ImageOutput:`

                - `Image image`

                  - `String fileId`

                    The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                - `JsonValue; type "image"constant`

                  Always `image`.

                  - `IMAGE("image")`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchToolCall:`

          - `String id`

            The ID of the tool call object.

          - `FileSearch fileSearch`

            For now, this is always going to be an empty object.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search.

              - `Ranker ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

            - `Optional<List<Result>> results`

              The results of the file search.

              - `String fileId`

                The ID of the file that result was found in.

              - `String fileName`

                The name of the file that result was found in.

              - `double score`

                The score of the result. All values must be a floating point number between 0 and 1.

              - `Optional<List<Content>> content`

                The content of the result that was found. The content is only included if requested via the include query parameter.

                - `Optional<String> text`

                  The text content of the file.

                - `Optional<Type> type`

                  The type of the content.

                  - `TEXT("text")`

          - `JsonValue; type "file_search"constant`

            The type of tool call. This is always going to be `file_search` for this type of tool call.

            - `FILE_SEARCH("file_search")`

        - `class FunctionToolCall:`

          - `String id`

            The ID of the tool call object.

          - `Function function`

            The definition of the function that was called.

            - `String arguments`

              The arguments passed to the function.

            - `String name`

              The name of the function.

            - `Optional<String> output`

              The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

          - `JsonValue; type "function"constant`

            The type of tool call. This is always going to be `function` for this type of tool call.

            - `FUNCTION("function")`

      - `JsonValue; type "tool_calls"constant`

        Always `tool_calls`.

        - `TOOL_CALLS("tool_calls")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

  - `Type type`

    The type of run step, which can be either `message_creation` or `tool_calls`.

    - `MESSAGE_CREATION("message_creation")`

    - `TOOL_CALLS("tool_calls")`

  - `Optional<Usage> usage`

    Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

    - `long completionTokens`

      Number of completion tokens used over the course of the run step.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run step.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

###### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.steps.StepListPage;
import com.openai.models.beta.threads.runs.steps.StepListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        StepListParams params = StepListParams.builder()
            .threadId("thread_id")
            .runId("run_id")
            .build();
        StepListPage page = client.beta().threads().runs().steps().list(params);
    }
}
```

##### Retrieve

`RunStep beta().threads().runs().steps().retrieve(StepRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}/runs/{run_id}/steps/{step_id}`

Retrieves a run step.

###### Parameters

- `StepRetrieveParams params`

  - `String threadId`

  - `String runId`

  - `Optional<String> stepId`

  - `Optional<List<RunStepInclude>> include`

    A list of additional fields to include in the response. Currently the only supported value is `step_details.tool_calls[*].file_search.results[*].content` to fetch the file search result content.

    See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

    - `STEP_DETAILS_TOOL_CALLS_FILE_SEARCH_RESULTS_CONTENT("step_details.tool_calls[*].file_search.results[*].content")`

###### Returns

- `class RunStep:`

  Represents a step in execution of a run.

  - `String id`

    The identifier of the run step, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run step was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run step completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run step was created.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run step failed.

  - `Optional<LastError> lastError`

    The last error associated with this run step. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error` or `rate_limit_exceeded`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.run.step"constant`

    The object type, which is always `thread.run.step`.

    - `THREAD_RUN_STEP("thread.run.step")`

  - `String runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

  - `Status status`

    The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

    - `IN_PROGRESS("in_progress")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

  - `StepDetails stepDetails`

    The details of the run step.

    - `class MessageCreationStepDetails:`

      Details of the message creation by the run step.

      - `MessageCreation messageCreation`

        - `String messageId`

          The ID of the message that was created by this run step.

      - `JsonValue; type "message_creation"constant`

        Always `message_creation`.

        - `MESSAGE_CREATION("message_creation")`

    - `class ToolCallsStepDetails:`

      Details of the tool call.

      - `List<ToolCall> toolCalls`

        An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

        - `class CodeInterpreterToolCall:`

          Details of the Code Interpreter tool call the run step was involved in.

          - `String id`

            The ID of the tool call.

          - `CodeInterpreter codeInterpreter`

            The Code Interpreter tool call definition.

            - `String input`

              The input to the Code Interpreter tool call.

            - `List<Output> outputs`

              The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

              - `class LogsOutput:`

                Text output from the Code Interpreter tool call as part of a run step.

                - `String logs`

                  The text output from the Code Interpreter tool call.

                - `JsonValue; type "logs"constant`

                  Always `logs`.

                  - `LOGS("logs")`

              - `class ImageOutput:`

                - `Image image`

                  - `String fileId`

                    The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                - `JsonValue; type "image"constant`

                  Always `image`.

                  - `IMAGE("image")`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchToolCall:`

          - `String id`

            The ID of the tool call object.

          - `FileSearch fileSearch`

            For now, this is always going to be an empty object.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search.

              - `Ranker ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

            - `Optional<List<Result>> results`

              The results of the file search.

              - `String fileId`

                The ID of the file that result was found in.

              - `String fileName`

                The name of the file that result was found in.

              - `double score`

                The score of the result. All values must be a floating point number between 0 and 1.

              - `Optional<List<Content>> content`

                The content of the result that was found. The content is only included if requested via the include query parameter.

                - `Optional<String> text`

                  The text content of the file.

                - `Optional<Type> type`

                  The type of the content.

                  - `TEXT("text")`

          - `JsonValue; type "file_search"constant`

            The type of tool call. This is always going to be `file_search` for this type of tool call.

            - `FILE_SEARCH("file_search")`

        - `class FunctionToolCall:`

          - `String id`

            The ID of the tool call object.

          - `Function function`

            The definition of the function that was called.

            - `String arguments`

              The arguments passed to the function.

            - `String name`

              The name of the function.

            - `Optional<String> output`

              The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

          - `JsonValue; type "function"constant`

            The type of tool call. This is always going to be `function` for this type of tool call.

            - `FUNCTION("function")`

      - `JsonValue; type "tool_calls"constant`

        Always `tool_calls`.

        - `TOOL_CALLS("tool_calls")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

  - `Type type`

    The type of run step, which can be either `message_creation` or `tool_calls`.

    - `MESSAGE_CREATION("message_creation")`

    - `TOOL_CALLS("tool_calls")`

  - `Optional<Usage> usage`

    Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

    - `long completionTokens`

      Number of completion tokens used over the course of the run step.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run step.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

###### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.steps.RunStep;
import com.openai.models.beta.threads.runs.steps.StepRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        StepRetrieveParams params = StepRetrieveParams.builder()
            .threadId("thread_id")
            .runId("run_id")
            .stepId("step_id")
            .build();
        RunStep runStep = client.beta().threads().runs().steps().retrieve(params);
    }
}
```

###### Domain Types

###### Code Interpreter Logs

- `class CodeInterpreterLogs:`

  Text output from the Code Interpreter tool call as part of a run step.

  - `long index`

    The index of the output in the outputs array.

  - `JsonValue; type "logs"constant`

    Always `logs`.

    - `LOGS("logs")`

  - `Optional<String> logs`

    The text output from the Code Interpreter tool call.

###### Code Interpreter Output Image

- `class CodeInterpreterOutputImage:`

  - `long index`

    The index of the output in the outputs array.

  - `JsonValue; type "image"constant`

    Always `image`.

    - `IMAGE("image")`

  - `Optional<Image> image`

    - `Optional<String> fileId`

      The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

###### Code Interpreter Tool Call

- `class CodeInterpreterToolCall:`

  Details of the Code Interpreter tool call the run step was involved in.

  - `String id`

    The ID of the tool call.

  - `CodeInterpreter codeInterpreter`

    The Code Interpreter tool call definition.

    - `String input`

      The input to the Code Interpreter tool call.

    - `List<Output> outputs`

      The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

      - `class LogsOutput:`

        Text output from the Code Interpreter tool call as part of a run step.

        - `String logs`

          The text output from the Code Interpreter tool call.

        - `JsonValue; type "logs"constant`

          Always `logs`.

          - `LOGS("logs")`

      - `class ImageOutput:`

        - `Image image`

          - `String fileId`

            The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

        - `JsonValue; type "image"constant`

          Always `image`.

          - `IMAGE("image")`

  - `JsonValue; type "code_interpreter"constant`

    The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

    - `CODE_INTERPRETER("code_interpreter")`

###### Code Interpreter Tool Call Delta

- `class CodeInterpreterToolCallDelta:`

  Details of the Code Interpreter tool call the run step was involved in.

  - `long index`

    The index of the tool call in the tool calls array.

  - `JsonValue; type "code_interpreter"constant`

    The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

    - `CODE_INTERPRETER("code_interpreter")`

  - `Optional<String> id`

    The ID of the tool call.

  - `Optional<CodeInterpreter> codeInterpreter`

    The Code Interpreter tool call definition.

    - `Optional<String> input`

      The input to the Code Interpreter tool call.

    - `Optional<List<Output>> outputs`

      The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

      - `class CodeInterpreterLogs:`

        Text output from the Code Interpreter tool call as part of a run step.

        - `long index`

          The index of the output in the outputs array.

        - `JsonValue; type "logs"constant`

          Always `logs`.

          - `LOGS("logs")`

        - `Optional<String> logs`

          The text output from the Code Interpreter tool call.

      - `class CodeInterpreterOutputImage:`

        - `long index`

          The index of the output in the outputs array.

        - `JsonValue; type "image"constant`

          Always `image`.

          - `IMAGE("image")`

        - `Optional<Image> image`

          - `Optional<String> fileId`

            The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

###### File Search Tool Call

- `class FileSearchToolCall:`

  - `String id`

    The ID of the tool call object.

  - `FileSearch fileSearch`

    For now, this is always going to be an empty object.

    - `Optional<RankingOptions> rankingOptions`

      The ranking options for the file search.

      - `Ranker ranker`

        The ranker to use for the file search. If not specified will use the `auto` ranker.

        - `AUTO("auto")`

        - `DEFAULT_2024_08_21("default_2024_08_21")`

      - `double scoreThreshold`

        The score threshold for the file search. All values must be a floating point number between 0 and 1.

    - `Optional<List<Result>> results`

      The results of the file search.

      - `String fileId`

        The ID of the file that result was found in.

      - `String fileName`

        The name of the file that result was found in.

      - `double score`

        The score of the result. All values must be a floating point number between 0 and 1.

      - `Optional<List<Content>> content`

        The content of the result that was found. The content is only included if requested via the include query parameter.

        - `Optional<String> text`

          The text content of the file.

        - `Optional<Type> type`

          The type of the content.

          - `TEXT("text")`

  - `JsonValue; type "file_search"constant`

    The type of tool call. This is always going to be `file_search` for this type of tool call.

    - `FILE_SEARCH("file_search")`

###### File Search Tool Call Delta

- `class FileSearchToolCallDelta:`

  - `JsonValue fileSearch`

    For now, this is always going to be an empty object.

  - `long index`

    The index of the tool call in the tool calls array.

  - `JsonValue; type "file_search"constant`

    The type of tool call. This is always going to be `file_search` for this type of tool call.

    - `FILE_SEARCH("file_search")`

  - `Optional<String> id`

    The ID of the tool call object.

###### Function Tool Call

- `class FunctionToolCall:`

  - `String id`

    The ID of the tool call object.

  - `Function function`

    The definition of the function that was called.

    - `String arguments`

      The arguments passed to the function.

    - `String name`

      The name of the function.

    - `Optional<String> output`

      The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

  - `JsonValue; type "function"constant`

    The type of tool call. This is always going to be `function` for this type of tool call.

    - `FUNCTION("function")`

###### Function Tool Call Delta

- `class FunctionToolCallDelta:`

  - `long index`

    The index of the tool call in the tool calls array.

  - `JsonValue; type "function"constant`

    The type of tool call. This is always going to be `function` for this type of tool call.

    - `FUNCTION("function")`

  - `Optional<String> id`

    The ID of the tool call object.

  - `Optional<Function> function`

    The definition of the function that was called.

    - `Optional<String> arguments`

      The arguments passed to the function.

    - `Optional<String> name`

      The name of the function.

    - `Optional<String> output`

      The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

###### Message Creation Step Details

- `class MessageCreationStepDetails:`

  Details of the message creation by the run step.

  - `MessageCreation messageCreation`

    - `String messageId`

      The ID of the message that was created by this run step.

  - `JsonValue; type "message_creation"constant`

    Always `message_creation`.

    - `MESSAGE_CREATION("message_creation")`

###### Run Step

- `class RunStep:`

  Represents a step in execution of a run.

  - `String id`

    The identifier of the run step, which can be referenced in API endpoints.

  - `String assistantId`

    The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

  - `Optional<Long> cancelledAt`

    The Unix timestamp (in seconds) for when the run step was cancelled.

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the run step completed.

  - `long createdAt`

    The Unix timestamp (in seconds) for when the run step was created.

  - `Optional<Long> expiredAt`

    The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

  - `Optional<Long> failedAt`

    The Unix timestamp (in seconds) for when the run step failed.

  - `Optional<LastError> lastError`

    The last error associated with this run step. Will be `null` if there are no errors.

    - `Code code`

      One of `server_error` or `rate_limit_exceeded`.

      - `SERVER_ERROR("server_error")`

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

    - `String message`

      A human-readable description of the error.

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.run.step"constant`

    The object type, which is always `thread.run.step`.

    - `THREAD_RUN_STEP("thread.run.step")`

  - `String runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

  - `Status status`

    The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

    - `IN_PROGRESS("in_progress")`

    - `CANCELLED("cancelled")`

    - `FAILED("failed")`

    - `COMPLETED("completed")`

    - `EXPIRED("expired")`

  - `StepDetails stepDetails`

    The details of the run step.

    - `class MessageCreationStepDetails:`

      Details of the message creation by the run step.

      - `MessageCreation messageCreation`

        - `String messageId`

          The ID of the message that was created by this run step.

      - `JsonValue; type "message_creation"constant`

        Always `message_creation`.

        - `MESSAGE_CREATION("message_creation")`

    - `class ToolCallsStepDetails:`

      Details of the tool call.

      - `List<ToolCall> toolCalls`

        An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

        - `class CodeInterpreterToolCall:`

          Details of the Code Interpreter tool call the run step was involved in.

          - `String id`

            The ID of the tool call.

          - `CodeInterpreter codeInterpreter`

            The Code Interpreter tool call definition.

            - `String input`

              The input to the Code Interpreter tool call.

            - `List<Output> outputs`

              The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

              - `class LogsOutput:`

                Text output from the Code Interpreter tool call as part of a run step.

                - `String logs`

                  The text output from the Code Interpreter tool call.

                - `JsonValue; type "logs"constant`

                  Always `logs`.

                  - `LOGS("logs")`

              - `class ImageOutput:`

                - `Image image`

                  - `String fileId`

                    The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

                - `JsonValue; type "image"constant`

                  Always `image`.

                  - `IMAGE("image")`

          - `JsonValue; type "code_interpreter"constant`

            The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

            - `CODE_INTERPRETER("code_interpreter")`

        - `class FileSearchToolCall:`

          - `String id`

            The ID of the tool call object.

          - `FileSearch fileSearch`

            For now, this is always going to be an empty object.

            - `Optional<RankingOptions> rankingOptions`

              The ranking options for the file search.

              - `Ranker ranker`

                The ranker to use for the file search. If not specified will use the `auto` ranker.

                - `AUTO("auto")`

                - `DEFAULT_2024_08_21("default_2024_08_21")`

              - `double scoreThreshold`

                The score threshold for the file search. All values must be a floating point number between 0 and 1.

            - `Optional<List<Result>> results`

              The results of the file search.

              - `String fileId`

                The ID of the file that result was found in.

              - `String fileName`

                The name of the file that result was found in.

              - `double score`

                The score of the result. All values must be a floating point number between 0 and 1.

              - `Optional<List<Content>> content`

                The content of the result that was found. The content is only included if requested via the include query parameter.

                - `Optional<String> text`

                  The text content of the file.

                - `Optional<Type> type`

                  The type of the content.

                  - `TEXT("text")`

          - `JsonValue; type "file_search"constant`

            The type of tool call. This is always going to be `file_search` for this type of tool call.

            - `FILE_SEARCH("file_search")`

        - `class FunctionToolCall:`

          - `String id`

            The ID of the tool call object.

          - `Function function`

            The definition of the function that was called.

            - `String arguments`

              The arguments passed to the function.

            - `String name`

              The name of the function.

            - `Optional<String> output`

              The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

          - `JsonValue; type "function"constant`

            The type of tool call. This is always going to be `function` for this type of tool call.

            - `FUNCTION("function")`

      - `JsonValue; type "tool_calls"constant`

        Always `tool_calls`.

        - `TOOL_CALLS("tool_calls")`

  - `String threadId`

    The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

  - `Type type`

    The type of run step, which can be either `message_creation` or `tool_calls`.

    - `MESSAGE_CREATION("message_creation")`

    - `TOOL_CALLS("tool_calls")`

  - `Optional<Usage> usage`

    Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

    - `long completionTokens`

      Number of completion tokens used over the course of the run step.

    - `long promptTokens`

      Number of prompt tokens used over the course of the run step.

    - `long totalTokens`

      Total number of tokens used (prompt + completion).

###### Run Step Delta

- `class RunStepDelta:`

  The delta containing the fields that have changed on the run step.

  - `Optional<StepDetails> stepDetails`

    The details of the run step.

    - `class RunStepDeltaMessageDelta:`

      Details of the message creation by the run step.

      - `JsonValue; type "message_creation"constant`

        Always `message_creation`.

        - `MESSAGE_CREATION("message_creation")`

      - `Optional<MessageCreation> messageCreation`

        - `Optional<String> messageId`

          The ID of the message that was created by this run step.

    - `class ToolCallDeltaObject:`

      Details of the tool call.

      - `JsonValue; type "tool_calls"constant`

        Always `tool_calls`.

        - `TOOL_CALLS("tool_calls")`

      - `Optional<List<ToolCallDelta>> toolCalls`

        An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

        - `class CodeInterpreterToolCallDelta:`

          Details of the Code Interpreter tool call the run step was involved in.

          - `long index`

            The index of the tool call in the tool calls array.

          - `JsonValue; type "code_interpreter"constant`

            The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

            - `CODE_INTERPRETER("code_interpreter")`

          - `Optional<String> id`

            The ID of the tool call.

          - `Optional<CodeInterpreter> codeInterpreter`

            The Code Interpreter tool call definition.

            - `Optional<String> input`

              The input to the Code Interpreter tool call.

            - `Optional<List<Output>> outputs`

              The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

              - `class CodeInterpreterLogs:`

                Text output from the Code Interpreter tool call as part of a run step.

                - `long index`

                  The index of the output in the outputs array.

                - `JsonValue; type "logs"constant`

                  Always `logs`.

                  - `LOGS("logs")`

                - `Optional<String> logs`

                  The text output from the Code Interpreter tool call.

              - `class CodeInterpreterOutputImage:`

                - `long index`

                  The index of the output in the outputs array.

                - `JsonValue; type "image"constant`

                  Always `image`.

                  - `IMAGE("image")`

                - `Optional<Image> image`

                  - `Optional<String> fileId`

                    The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

        - `class FileSearchToolCallDelta:`

          - `JsonValue fileSearch`

            For now, this is always going to be an empty object.

          - `long index`

            The index of the tool call in the tool calls array.

          - `JsonValue; type "file_search"constant`

            The type of tool call. This is always going to be `file_search` for this type of tool call.

            - `FILE_SEARCH("file_search")`

          - `Optional<String> id`

            The ID of the tool call object.

        - `class FunctionToolCallDelta:`

          - `long index`

            The index of the tool call in the tool calls array.

          - `JsonValue; type "function"constant`

            The type of tool call. This is always going to be `function` for this type of tool call.

            - `FUNCTION("function")`

          - `Optional<String> id`

            The ID of the tool call object.

          - `Optional<Function> function`

            The definition of the function that was called.

            - `Optional<String> arguments`

              The arguments passed to the function.

            - `Optional<String> name`

              The name of the function.

            - `Optional<String> output`

              The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

###### Run Step Delta Event

- `class RunStepDeltaEvent:`

  Represents a run step delta i.e. any changed fields on a run step during streaming.

  - `String id`

    The identifier of the run step, which can be referenced in API endpoints.

  - `RunStepDelta delta`

    The delta containing the fields that have changed on the run step.

    - `Optional<StepDetails> stepDetails`

      The details of the run step.

      - `class RunStepDeltaMessageDelta:`

        Details of the message creation by the run step.

        - `JsonValue; type "message_creation"constant`

          Always `message_creation`.

          - `MESSAGE_CREATION("message_creation")`

        - `Optional<MessageCreation> messageCreation`

          - `Optional<String> messageId`

            The ID of the message that was created by this run step.

      - `class ToolCallDeltaObject:`

        Details of the tool call.

        - `JsonValue; type "tool_calls"constant`

          Always `tool_calls`.

          - `TOOL_CALLS("tool_calls")`

        - `Optional<List<ToolCallDelta>> toolCalls`

          An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

          - `class CodeInterpreterToolCallDelta:`

            Details of the Code Interpreter tool call the run step was involved in.

            - `long index`

              The index of the tool call in the tool calls array.

            - `JsonValue; type "code_interpreter"constant`

              The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

              - `CODE_INTERPRETER("code_interpreter")`

            - `Optional<String> id`

              The ID of the tool call.

            - `Optional<CodeInterpreter> codeInterpreter`

              The Code Interpreter tool call definition.

              - `Optional<String> input`

                The input to the Code Interpreter tool call.

              - `Optional<List<Output>> outputs`

                The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

                - `class CodeInterpreterLogs:`

                  Text output from the Code Interpreter tool call as part of a run step.

                  - `long index`

                    The index of the output in the outputs array.

                  - `JsonValue; type "logs"constant`

                    Always `logs`.

                    - `LOGS("logs")`

                  - `Optional<String> logs`

                    The text output from the Code Interpreter tool call.

                - `class CodeInterpreterOutputImage:`

                  - `long index`

                    The index of the output in the outputs array.

                  - `JsonValue; type "image"constant`

                    Always `image`.

                    - `IMAGE("image")`

                  - `Optional<Image> image`

                    - `Optional<String> fileId`

                      The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

          - `class FileSearchToolCallDelta:`

            - `JsonValue fileSearch`

              For now, this is always going to be an empty object.

            - `long index`

              The index of the tool call in the tool calls array.

            - `JsonValue; type "file_search"constant`

              The type of tool call. This is always going to be `file_search` for this type of tool call.

              - `FILE_SEARCH("file_search")`

            - `Optional<String> id`

              The ID of the tool call object.

          - `class FunctionToolCallDelta:`

            - `long index`

              The index of the tool call in the tool calls array.

            - `JsonValue; type "function"constant`

              The type of tool call. This is always going to be `function` for this type of tool call.

              - `FUNCTION("function")`

            - `Optional<String> id`

              The ID of the tool call object.

            - `Optional<Function> function`

              The definition of the function that was called.

              - `Optional<String> arguments`

                The arguments passed to the function.

              - `Optional<String> name`

                The name of the function.

              - `Optional<String> output`

                The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

  - `JsonValue; object_ "thread.run.step.delta"constant`

    The object type, which is always `thread.run.step.delta`.

    - `THREAD_RUN_STEP_DELTA("thread.run.step.delta")`

###### Run Step Delta Message Delta

- `class RunStepDeltaMessageDelta:`

  Details of the message creation by the run step.

  - `JsonValue; type "message_creation"constant`

    Always `message_creation`.

    - `MESSAGE_CREATION("message_creation")`

  - `Optional<MessageCreation> messageCreation`

    - `Optional<String> messageId`

      The ID of the message that was created by this run step.

###### Run Step Include

- `enum RunStepInclude:`

  - `STEP_DETAILS_TOOL_CALLS_FILE_SEARCH_RESULTS_CONTENT("step_details.tool_calls[*].file_search.results[*].content")`

###### Tool Call

- `class ToolCall: A class that can be one of several variants.union`

  Details of the Code Interpreter tool call the run step was involved in.

  - `class CodeInterpreterToolCall:`

    Details of the Code Interpreter tool call the run step was involved in.

    - `String id`

      The ID of the tool call.

    - `CodeInterpreter codeInterpreter`

      The Code Interpreter tool call definition.

      - `String input`

        The input to the Code Interpreter tool call.

      - `List<Output> outputs`

        The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

        - `class LogsOutput:`

          Text output from the Code Interpreter tool call as part of a run step.

          - `String logs`

            The text output from the Code Interpreter tool call.

          - `JsonValue; type "logs"constant`

            Always `logs`.

            - `LOGS("logs")`

        - `class ImageOutput:`

          - `Image image`

            - `String fileId`

              The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

          - `JsonValue; type "image"constant`

            Always `image`.

            - `IMAGE("image")`

    - `JsonValue; type "code_interpreter"constant`

      The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

      - `CODE_INTERPRETER("code_interpreter")`

  - `class FileSearchToolCall:`

    - `String id`

      The ID of the tool call object.

    - `FileSearch fileSearch`

      For now, this is always going to be an empty object.

      - `Optional<RankingOptions> rankingOptions`

        The ranking options for the file search.

        - `Ranker ranker`

          The ranker to use for the file search. If not specified will use the `auto` ranker.

          - `AUTO("auto")`

          - `DEFAULT_2024_08_21("default_2024_08_21")`

        - `double scoreThreshold`

          The score threshold for the file search. All values must be a floating point number between 0 and 1.

      - `Optional<List<Result>> results`

        The results of the file search.

        - `String fileId`

          The ID of the file that result was found in.

        - `String fileName`

          The name of the file that result was found in.

        - `double score`

          The score of the result. All values must be a floating point number between 0 and 1.

        - `Optional<List<Content>> content`

          The content of the result that was found. The content is only included if requested via the include query parameter.

          - `Optional<String> text`

            The text content of the file.

          - `Optional<Type> type`

            The type of the content.

            - `TEXT("text")`

    - `JsonValue; type "file_search"constant`

      The type of tool call. This is always going to be `file_search` for this type of tool call.

      - `FILE_SEARCH("file_search")`

  - `class FunctionToolCall:`

    - `String id`

      The ID of the tool call object.

    - `Function function`

      The definition of the function that was called.

      - `String arguments`

        The arguments passed to the function.

      - `String name`

        The name of the function.

      - `Optional<String> output`

        The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

    - `JsonValue; type "function"constant`

      The type of tool call. This is always going to be `function` for this type of tool call.

      - `FUNCTION("function")`

###### Tool Call Delta

- `class ToolCallDelta: A class that can be one of several variants.union`

  Details of the Code Interpreter tool call the run step was involved in.

  - `class CodeInterpreterToolCallDelta:`

    Details of the Code Interpreter tool call the run step was involved in.

    - `long index`

      The index of the tool call in the tool calls array.

    - `JsonValue; type "code_interpreter"constant`

      The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

      - `CODE_INTERPRETER("code_interpreter")`

    - `Optional<String> id`

      The ID of the tool call.

    - `Optional<CodeInterpreter> codeInterpreter`

      The Code Interpreter tool call definition.

      - `Optional<String> input`

        The input to the Code Interpreter tool call.

      - `Optional<List<Output>> outputs`

        The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

        - `class CodeInterpreterLogs:`

          Text output from the Code Interpreter tool call as part of a run step.

          - `long index`

            The index of the output in the outputs array.

          - `JsonValue; type "logs"constant`

            Always `logs`.

            - `LOGS("logs")`

          - `Optional<String> logs`

            The text output from the Code Interpreter tool call.

        - `class CodeInterpreterOutputImage:`

          - `long index`

            The index of the output in the outputs array.

          - `JsonValue; type "image"constant`

            Always `image`.

            - `IMAGE("image")`

          - `Optional<Image> image`

            - `Optional<String> fileId`

              The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

  - `class FileSearchToolCallDelta:`

    - `JsonValue fileSearch`

      For now, this is always going to be an empty object.

    - `long index`

      The index of the tool call in the tool calls array.

    - `JsonValue; type "file_search"constant`

      The type of tool call. This is always going to be `file_search` for this type of tool call.

      - `FILE_SEARCH("file_search")`

    - `Optional<String> id`

      The ID of the tool call object.

  - `class FunctionToolCallDelta:`

    - `long index`

      The index of the tool call in the tool calls array.

    - `JsonValue; type "function"constant`

      The type of tool call. This is always going to be `function` for this type of tool call.

      - `FUNCTION("function")`

    - `Optional<String> id`

      The ID of the tool call object.

    - `Optional<Function> function`

      The definition of the function that was called.

      - `Optional<String> arguments`

        The arguments passed to the function.

      - `Optional<String> name`

        The name of the function.

      - `Optional<String> output`

        The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

###### Tool Call Delta Object

- `class ToolCallDeltaObject:`

  Details of the tool call.

  - `JsonValue; type "tool_calls"constant`

    Always `tool_calls`.

    - `TOOL_CALLS("tool_calls")`

  - `Optional<List<ToolCallDelta>> toolCalls`

    An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterToolCallDelta:`

      Details of the Code Interpreter tool call the run step was involved in.

      - `long index`

        The index of the tool call in the tool calls array.

      - `JsonValue; type "code_interpreter"constant`

        The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

        - `CODE_INTERPRETER("code_interpreter")`

      - `Optional<String> id`

        The ID of the tool call.

      - `Optional<CodeInterpreter> codeInterpreter`

        The Code Interpreter tool call definition.

        - `Optional<String> input`

          The input to the Code Interpreter tool call.

        - `Optional<List<Output>> outputs`

          The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

          - `class CodeInterpreterLogs:`

            Text output from the Code Interpreter tool call as part of a run step.

            - `long index`

              The index of the output in the outputs array.

            - `JsonValue; type "logs"constant`

              Always `logs`.

              - `LOGS("logs")`

            - `Optional<String> logs`

              The text output from the Code Interpreter tool call.

          - `class CodeInterpreterOutputImage:`

            - `long index`

              The index of the output in the outputs array.

            - `JsonValue; type "image"constant`

              Always `image`.

              - `IMAGE("image")`

            - `Optional<Image> image`

              - `Optional<String> fileId`

                The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

    - `class FileSearchToolCallDelta:`

      - `JsonValue fileSearch`

        For now, this is always going to be an empty object.

      - `long index`

        The index of the tool call in the tool calls array.

      - `JsonValue; type "file_search"constant`

        The type of tool call. This is always going to be `file_search` for this type of tool call.

        - `FILE_SEARCH("file_search")`

      - `Optional<String> id`

        The ID of the tool call object.

    - `class FunctionToolCallDelta:`

      - `long index`

        The index of the tool call in the tool calls array.

      - `JsonValue; type "function"constant`

        The type of tool call. This is always going to be `function` for this type of tool call.

        - `FUNCTION("function")`

      - `Optional<String> id`

        The ID of the tool call object.

      - `Optional<Function> function`

        The definition of the function that was called.

        - `Optional<String> arguments`

          The arguments passed to the function.

        - `Optional<String> name`

          The name of the function.

        - `Optional<String> output`

          The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

###### Tool Calls Step Details

- `class ToolCallsStepDetails:`

  Details of the tool call.

  - `List<ToolCall> toolCalls`

    An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

    - `class CodeInterpreterToolCall:`

      Details of the Code Interpreter tool call the run step was involved in.

      - `String id`

        The ID of the tool call.

      - `CodeInterpreter codeInterpreter`

        The Code Interpreter tool call definition.

        - `String input`

          The input to the Code Interpreter tool call.

        - `List<Output> outputs`

          The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

          - `class LogsOutput:`

            Text output from the Code Interpreter tool call as part of a run step.

            - `String logs`

              The text output from the Code Interpreter tool call.

            - `JsonValue; type "logs"constant`

              Always `logs`.

              - `LOGS("logs")`

          - `class ImageOutput:`

            - `Image image`

              - `String fileId`

                The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

            - `JsonValue; type "image"constant`

              Always `image`.

              - `IMAGE("image")`

      - `JsonValue; type "code_interpreter"constant`

        The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

        - `CODE_INTERPRETER("code_interpreter")`

    - `class FileSearchToolCall:`

      - `String id`

        The ID of the tool call object.

      - `FileSearch fileSearch`

        For now, this is always going to be an empty object.

        - `Optional<RankingOptions> rankingOptions`

          The ranking options for the file search.

          - `Ranker ranker`

            The ranker to use for the file search. If not specified will use the `auto` ranker.

            - `AUTO("auto")`

            - `DEFAULT_2024_08_21("default_2024_08_21")`

          - `double scoreThreshold`

            The score threshold for the file search. All values must be a floating point number between 0 and 1.

        - `Optional<List<Result>> results`

          The results of the file search.

          - `String fileId`

            The ID of the file that result was found in.

          - `String fileName`

            The name of the file that result was found in.

          - `double score`

            The score of the result. All values must be a floating point number between 0 and 1.

          - `Optional<List<Content>> content`

            The content of the result that was found. The content is only included if requested via the include query parameter.

            - `Optional<String> text`

              The text content of the file.

            - `Optional<Type> type`

              The type of the content.

              - `TEXT("text")`

      - `JsonValue; type "file_search"constant`

        The type of tool call. This is always going to be `file_search` for this type of tool call.

        - `FILE_SEARCH("file_search")`

    - `class FunctionToolCall:`

      - `String id`

        The ID of the tool call object.

      - `Function function`

        The definition of the function that was called.

        - `String arguments`

          The arguments passed to the function.

        - `String name`

          The name of the function.

        - `Optional<String> output`

          The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

      - `JsonValue; type "function"constant`

        The type of tool call. This is always going to be `function` for this type of tool call.

        - `FUNCTION("function")`

  - `JsonValue; type "tool_calls"constant`

    Always `tool_calls`.

    - `TOOL_CALLS("tool_calls")`

### Messages

#### List

`MessageListPage beta().threads().messages().list(MessageListParamsparams = MessageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}/messages`

Returns a list of messages for a given thread.

##### Parameters

- `MessageListParams params`

  - `Optional<String> threadId`

  - `Optional<String> after`

    A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

  - `Optional<String> before`

    A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

  - `Optional<Long> limit`

    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> runId`

    Filter messages by the run ID that generated them.

##### Returns

- `class Message:`

  Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `Optional<String> assistantId`

    If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

  - `Optional<List<Attachment>> attachments`

    A list of files attached to the message, and the tools they were added to.

    - `Optional<String> fileId`

      The ID of the file to attach to the message.

    - `Optional<List<Tool>> tools`

      The tools to add this file to.

      - `class CodeInterpreterTool:`

        - `JsonValue; type "code_interpreter"constant`

          The type of tool being defined: `code_interpreter`

          - `CODE_INTERPRETER("code_interpreter")`

      - `JsonValue;`

        - `JsonValue; type "file_search"constant`

          The type of tool being defined: `file_search`

          - `FILE_SEARCH("file_search")`

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the message was completed.

  - `List<MessageContent> content`

    The content of the message in array of text and/or images.

    - `class ImageFileContentBlock:`

      References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

      - `ImageFile imageFile`

        - `String fileId`

          The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

        - `Optional<Detail> detail`

          Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_file"constant`

        Always `image_file`.

        - `IMAGE_FILE("image_file")`

    - `class ImageUrlContentBlock:`

      References an image URL in the content of a message.

      - `ImageUrl imageUrl`

        - `String url`

          The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

    - `class TextContentBlock:`

      The text content that is part of a message.

      - `Text text`

        - `List<Annotation> annotations`

          - `class FileCitationAnnotation:`

            A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

            - `long endIndex`

            - `FileCitation fileCitation`

              - `String fileId`

                The ID of the specific File the citation is from.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_citation"constant`

              Always `file_citation`.

              - `FILE_CITATION("file_citation")`

          - `class FilePathAnnotation:`

            A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

            - `long endIndex`

            - `FilePath filePath`

              - `String fileId`

                The ID of the file that was generated.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_path"constant`

              Always `file_path`.

              - `FILE_PATH("file_path")`

        - `String value`

          The data that makes up the text.

      - `JsonValue; type "text"constant`

        Always `text`.

        - `TEXT("text")`

    - `class RefusalContentBlock:`

      The refusal content generated by the assistant.

      - `String refusal`

      - `JsonValue; type "refusal"constant`

        Always `refusal`.

        - `REFUSAL("refusal")`

  - `long createdAt`

    The Unix timestamp (in seconds) for when the message was created.

  - `Optional<Long> incompleteAt`

    The Unix timestamp (in seconds) for when the message was marked as incomplete.

  - `Optional<IncompleteDetails> incompleteDetails`

    On an incomplete message, details about why the message is incomplete.

    - `Reason reason`

      The reason the message is incomplete.

      - `CONTENT_FILTER("content_filter")`

      - `MAX_TOKENS("max_tokens")`

      - `RUN_CANCELLED("run_cancelled")`

      - `RUN_EXPIRED("run_expired")`

      - `RUN_FAILED("run_failed")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.message"constant`

    The object type, which is always `thread.message`.

    - `THREAD_MESSAGE("thread.message")`

  - `Role role`

    The entity that produced the message. One of `user` or `assistant`.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `Optional<String> runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

  - `Status status`

    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

    - `IN_PROGRESS("in_progress")`

    - `INCOMPLETE("incomplete")`

    - `COMPLETED("completed")`

  - `String threadId`

    The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.messages.MessageListPage;
import com.openai.models.beta.threads.messages.MessageListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageListPage page = client.beta().threads().messages().list("thread_id");
    }
}
```

#### Create

`Message beta().threads().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}/messages`

Create a message.

##### Parameters

- `MessageCreateParams params`

  - `Optional<String> threadId`

  - `Content content`

    The text contents of the message.

    - `String`

    - `List<MessageContentPartParam>`

      - `class ImageFileContentBlock:`

        References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

        - `ImageFile imageFile`

          - `String fileId`

            The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

          - `Optional<Detail> detail`

            Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

            - `AUTO("auto")`

            - `LOW("low")`

            - `HIGH("high")`

        - `JsonValue; type "image_file"constant`

          Always `image_file`.

          - `IMAGE_FILE("image_file")`

      - `class ImageUrlContentBlock:`

        References an image URL in the content of a message.

        - `ImageUrl imageUrl`

          - `String url`

            The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

          - `Optional<Detail> detail`

            Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

            - `AUTO("auto")`

            - `LOW("low")`

            - `HIGH("high")`

        - `JsonValue; type "image_url"constant`

          The type of the content part.

          - `IMAGE_URL("image_url")`

      - `class TextContentBlockParam:`

        The text content that is part of a message.

        - `String text`

          Text content to be sent to the model

        - `JsonValue; type "text"constant`

          Always `text`.

          - `TEXT("text")`

  - `Role role`

    The role of the entity that is creating the message. Allowed values include:

    - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
    - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `Optional<List<Attachment>> attachments`

    A list of files attached to the message, and the tools they should be added to.

    - `Optional<String> fileId`

      The ID of the file to attach to the message.

    - `Optional<List<Tool>> tools`

      The tools to add this file to.

      - `class CodeInterpreterTool:`

        - `JsonValue; type "code_interpreter"constant`

          The type of tool being defined: `code_interpreter`

          - `CODE_INTERPRETER("code_interpreter")`

      - `JsonValue;`

        - `JsonValue; type "file_search"constant`

          The type of tool being defined: `file_search`

          - `FILE_SEARCH("file_search")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

##### Returns

- `class Message:`

  Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `Optional<String> assistantId`

    If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

  - `Optional<List<Attachment>> attachments`

    A list of files attached to the message, and the tools they were added to.

    - `Optional<String> fileId`

      The ID of the file to attach to the message.

    - `Optional<List<Tool>> tools`

      The tools to add this file to.

      - `class CodeInterpreterTool:`

        - `JsonValue; type "code_interpreter"constant`

          The type of tool being defined: `code_interpreter`

          - `CODE_INTERPRETER("code_interpreter")`

      - `JsonValue;`

        - `JsonValue; type "file_search"constant`

          The type of tool being defined: `file_search`

          - `FILE_SEARCH("file_search")`

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the message was completed.

  - `List<MessageContent> content`

    The content of the message in array of text and/or images.

    - `class ImageFileContentBlock:`

      References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

      - `ImageFile imageFile`

        - `String fileId`

          The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

        - `Optional<Detail> detail`

          Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_file"constant`

        Always `image_file`.

        - `IMAGE_FILE("image_file")`

    - `class ImageUrlContentBlock:`

      References an image URL in the content of a message.

      - `ImageUrl imageUrl`

        - `String url`

          The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

    - `class TextContentBlock:`

      The text content that is part of a message.

      - `Text text`

        - `List<Annotation> annotations`

          - `class FileCitationAnnotation:`

            A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

            - `long endIndex`

            - `FileCitation fileCitation`

              - `String fileId`

                The ID of the specific File the citation is from.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_citation"constant`

              Always `file_citation`.

              - `FILE_CITATION("file_citation")`

          - `class FilePathAnnotation:`

            A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

            - `long endIndex`

            - `FilePath filePath`

              - `String fileId`

                The ID of the file that was generated.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_path"constant`

              Always `file_path`.

              - `FILE_PATH("file_path")`

        - `String value`

          The data that makes up the text.

      - `JsonValue; type "text"constant`

        Always `text`.

        - `TEXT("text")`

    - `class RefusalContentBlock:`

      The refusal content generated by the assistant.

      - `String refusal`

      - `JsonValue; type "refusal"constant`

        Always `refusal`.

        - `REFUSAL("refusal")`

  - `long createdAt`

    The Unix timestamp (in seconds) for when the message was created.

  - `Optional<Long> incompleteAt`

    The Unix timestamp (in seconds) for when the message was marked as incomplete.

  - `Optional<IncompleteDetails> incompleteDetails`

    On an incomplete message, details about why the message is incomplete.

    - `Reason reason`

      The reason the message is incomplete.

      - `CONTENT_FILTER("content_filter")`

      - `MAX_TOKENS("max_tokens")`

      - `RUN_CANCELLED("run_cancelled")`

      - `RUN_EXPIRED("run_expired")`

      - `RUN_FAILED("run_failed")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.message"constant`

    The object type, which is always `thread.message`.

    - `THREAD_MESSAGE("thread.message")`

  - `Role role`

    The entity that produced the message. One of `user` or `assistant`.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `Optional<String> runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

  - `Status status`

    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

    - `IN_PROGRESS("in_progress")`

    - `INCOMPLETE("incomplete")`

    - `COMPLETED("completed")`

  - `String threadId`

    The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.messages.Message;
import com.openai.models.beta.threads.messages.MessageCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .threadId("thread_id")
            .content("string")
            .role(MessageCreateParams.Role.USER)
            .build();
        Message message = client.beta().threads().messages().create(params);
    }
}
```

#### Update

`Message beta().threads().messages().update(MessageUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/threads/{thread_id}/messages/{message_id}`

Modifies a message.

##### Parameters

- `MessageUpdateParams params`

  - `String threadId`

  - `Optional<String> messageId`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

##### Returns

- `class Message:`

  Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `Optional<String> assistantId`

    If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

  - `Optional<List<Attachment>> attachments`

    A list of files attached to the message, and the tools they were added to.

    - `Optional<String> fileId`

      The ID of the file to attach to the message.

    - `Optional<List<Tool>> tools`

      The tools to add this file to.

      - `class CodeInterpreterTool:`

        - `JsonValue; type "code_interpreter"constant`

          The type of tool being defined: `code_interpreter`

          - `CODE_INTERPRETER("code_interpreter")`

      - `JsonValue;`

        - `JsonValue; type "file_search"constant`

          The type of tool being defined: `file_search`

          - `FILE_SEARCH("file_search")`

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the message was completed.

  - `List<MessageContent> content`

    The content of the message in array of text and/or images.

    - `class ImageFileContentBlock:`

      References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

      - `ImageFile imageFile`

        - `String fileId`

          The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

        - `Optional<Detail> detail`

          Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_file"constant`

        Always `image_file`.

        - `IMAGE_FILE("image_file")`

    - `class ImageUrlContentBlock:`

      References an image URL in the content of a message.

      - `ImageUrl imageUrl`

        - `String url`

          The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

    - `class TextContentBlock:`

      The text content that is part of a message.

      - `Text text`

        - `List<Annotation> annotations`

          - `class FileCitationAnnotation:`

            A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

            - `long endIndex`

            - `FileCitation fileCitation`

              - `String fileId`

                The ID of the specific File the citation is from.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_citation"constant`

              Always `file_citation`.

              - `FILE_CITATION("file_citation")`

          - `class FilePathAnnotation:`

            A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

            - `long endIndex`

            - `FilePath filePath`

              - `String fileId`

                The ID of the file that was generated.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_path"constant`

              Always `file_path`.

              - `FILE_PATH("file_path")`

        - `String value`

          The data that makes up the text.

      - `JsonValue; type "text"constant`

        Always `text`.

        - `TEXT("text")`

    - `class RefusalContentBlock:`

      The refusal content generated by the assistant.

      - `String refusal`

      - `JsonValue; type "refusal"constant`

        Always `refusal`.

        - `REFUSAL("refusal")`

  - `long createdAt`

    The Unix timestamp (in seconds) for when the message was created.

  - `Optional<Long> incompleteAt`

    The Unix timestamp (in seconds) for when the message was marked as incomplete.

  - `Optional<IncompleteDetails> incompleteDetails`

    On an incomplete message, details about why the message is incomplete.

    - `Reason reason`

      The reason the message is incomplete.

      - `CONTENT_FILTER("content_filter")`

      - `MAX_TOKENS("max_tokens")`

      - `RUN_CANCELLED("run_cancelled")`

      - `RUN_EXPIRED("run_expired")`

      - `RUN_FAILED("run_failed")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.message"constant`

    The object type, which is always `thread.message`.

    - `THREAD_MESSAGE("thread.message")`

  - `Role role`

    The entity that produced the message. One of `user` or `assistant`.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `Optional<String> runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

  - `Status status`

    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

    - `IN_PROGRESS("in_progress")`

    - `INCOMPLETE("incomplete")`

    - `COMPLETED("completed")`

  - `String threadId`

    The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.messages.Message;
import com.openai.models.beta.threads.messages.MessageUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageUpdateParams params = MessageUpdateParams.builder()
            .threadId("thread_id")
            .messageId("message_id")
            .build();
        Message message = client.beta().threads().messages().update(params);
    }
}
```

#### Retrieve

`Message beta().threads().messages().retrieve(MessageRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/threads/{thread_id}/messages/{message_id}`

Retrieve a message.

##### Parameters

- `MessageRetrieveParams params`

  - `String threadId`

  - `Optional<String> messageId`

##### Returns

- `class Message:`

  Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `Optional<String> assistantId`

    If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

  - `Optional<List<Attachment>> attachments`

    A list of files attached to the message, and the tools they were added to.

    - `Optional<String> fileId`

      The ID of the file to attach to the message.

    - `Optional<List<Tool>> tools`

      The tools to add this file to.

      - `class CodeInterpreterTool:`

        - `JsonValue; type "code_interpreter"constant`

          The type of tool being defined: `code_interpreter`

          - `CODE_INTERPRETER("code_interpreter")`

      - `JsonValue;`

        - `JsonValue; type "file_search"constant`

          The type of tool being defined: `file_search`

          - `FILE_SEARCH("file_search")`

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the message was completed.

  - `List<MessageContent> content`

    The content of the message in array of text and/or images.

    - `class ImageFileContentBlock:`

      References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

      - `ImageFile imageFile`

        - `String fileId`

          The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

        - `Optional<Detail> detail`

          Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_file"constant`

        Always `image_file`.

        - `IMAGE_FILE("image_file")`

    - `class ImageUrlContentBlock:`

      References an image URL in the content of a message.

      - `ImageUrl imageUrl`

        - `String url`

          The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

    - `class TextContentBlock:`

      The text content that is part of a message.

      - `Text text`

        - `List<Annotation> annotations`

          - `class FileCitationAnnotation:`

            A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

            - `long endIndex`

            - `FileCitation fileCitation`

              - `String fileId`

                The ID of the specific File the citation is from.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_citation"constant`

              Always `file_citation`.

              - `FILE_CITATION("file_citation")`

          - `class FilePathAnnotation:`

            A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

            - `long endIndex`

            - `FilePath filePath`

              - `String fileId`

                The ID of the file that was generated.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_path"constant`

              Always `file_path`.

              - `FILE_PATH("file_path")`

        - `String value`

          The data that makes up the text.

      - `JsonValue; type "text"constant`

        Always `text`.

        - `TEXT("text")`

    - `class RefusalContentBlock:`

      The refusal content generated by the assistant.

      - `String refusal`

      - `JsonValue; type "refusal"constant`

        Always `refusal`.

        - `REFUSAL("refusal")`

  - `long createdAt`

    The Unix timestamp (in seconds) for when the message was created.

  - `Optional<Long> incompleteAt`

    The Unix timestamp (in seconds) for when the message was marked as incomplete.

  - `Optional<IncompleteDetails> incompleteDetails`

    On an incomplete message, details about why the message is incomplete.

    - `Reason reason`

      The reason the message is incomplete.

      - `CONTENT_FILTER("content_filter")`

      - `MAX_TOKENS("max_tokens")`

      - `RUN_CANCELLED("run_cancelled")`

      - `RUN_EXPIRED("run_expired")`

      - `RUN_FAILED("run_failed")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.message"constant`

    The object type, which is always `thread.message`.

    - `THREAD_MESSAGE("thread.message")`

  - `Role role`

    The entity that produced the message. One of `user` or `assistant`.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `Optional<String> runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

  - `Status status`

    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

    - `IN_PROGRESS("in_progress")`

    - `INCOMPLETE("incomplete")`

    - `COMPLETED("completed")`

  - `String threadId`

    The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.messages.Message;
import com.openai.models.beta.threads.messages.MessageRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageRetrieveParams params = MessageRetrieveParams.builder()
            .threadId("thread_id")
            .messageId("message_id")
            .build();
        Message message = client.beta().threads().messages().retrieve(params);
    }
}
```

#### Delete

`MessageDeleted beta().threads().messages().delete(MessageDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/threads/{thread_id}/messages/{message_id}`

Deletes a message.

##### Parameters

- `MessageDeleteParams params`

  - `String threadId`

  - `Optional<String> messageId`

##### Returns

- `class MessageDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "thread.message.deleted"constant`

    - `THREAD_MESSAGE_DELETED("thread.message.deleted")`

##### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.messages.MessageDeleteParams;
import com.openai.models.beta.threads.messages.MessageDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        MessageDeleteParams params = MessageDeleteParams.builder()
            .threadId("thread_id")
            .messageId("message_id")
            .build();
        MessageDeleted messageDeleted = client.beta().threads().messages().delete(params);
    }
}
```

##### Domain Types

##### Annotation

- `class Annotation: A class that can be one of several variants.union`

  A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

  - `class FileCitationAnnotation:`

    A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

    - `long endIndex`

    - `FileCitation fileCitation`

      - `String fileId`

        The ID of the specific File the citation is from.

    - `long startIndex`

    - `String text`

      The text in the message content that needs to be replaced.

    - `JsonValue; type "file_citation"constant`

      Always `file_citation`.

      - `FILE_CITATION("file_citation")`

  - `class FilePathAnnotation:`

    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

    - `long endIndex`

    - `FilePath filePath`

      - `String fileId`

        The ID of the file that was generated.

    - `long startIndex`

    - `String text`

      The text in the message content that needs to be replaced.

    - `JsonValue; type "file_path"constant`

      Always `file_path`.

      - `FILE_PATH("file_path")`

##### Annotation Delta

- `class AnnotationDelta: A class that can be one of several variants.union`

  A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

  - `class FileCitationDeltaAnnotation:`

    A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

    - `long index`

      The index of the annotation in the text content part.

    - `JsonValue; type "file_citation"constant`

      Always `file_citation`.

      - `FILE_CITATION("file_citation")`

    - `Optional<Long> endIndex`

    - `Optional<FileCitation> fileCitation`

      - `Optional<String> fileId`

        The ID of the specific File the citation is from.

      - `Optional<String> quote`

        The specific quote in the file.

    - `Optional<Long> startIndex`

    - `Optional<String> text`

      The text in the message content that needs to be replaced.

  - `class FilePathDeltaAnnotation:`

    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

    - `long index`

      The index of the annotation in the text content part.

    - `JsonValue; type "file_path"constant`

      Always `file_path`.

      - `FILE_PATH("file_path")`

    - `Optional<Long> endIndex`

    - `Optional<FilePath> filePath`

      - `Optional<String> fileId`

        The ID of the file that was generated.

    - `Optional<Long> startIndex`

    - `Optional<String> text`

      The text in the message content that needs to be replaced.

##### File Citation Annotation

- `class FileCitationAnnotation:`

  A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

  - `long endIndex`

  - `FileCitation fileCitation`

    - `String fileId`

      The ID of the specific File the citation is from.

  - `long startIndex`

  - `String text`

    The text in the message content that needs to be replaced.

  - `JsonValue; type "file_citation"constant`

    Always `file_citation`.

    - `FILE_CITATION("file_citation")`

##### File Citation Delta Annotation

- `class FileCitationDeltaAnnotation:`

  A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

  - `long index`

    The index of the annotation in the text content part.

  - `JsonValue; type "file_citation"constant`

    Always `file_citation`.

    - `FILE_CITATION("file_citation")`

  - `Optional<Long> endIndex`

  - `Optional<FileCitation> fileCitation`

    - `Optional<String> fileId`

      The ID of the specific File the citation is from.

    - `Optional<String> quote`

      The specific quote in the file.

  - `Optional<Long> startIndex`

  - `Optional<String> text`

    The text in the message content that needs to be replaced.

##### File Path Annotation

- `class FilePathAnnotation:`

  A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

  - `long endIndex`

  - `FilePath filePath`

    - `String fileId`

      The ID of the file that was generated.

  - `long startIndex`

  - `String text`

    The text in the message content that needs to be replaced.

  - `JsonValue; type "file_path"constant`

    Always `file_path`.

    - `FILE_PATH("file_path")`

##### File Path Delta Annotation

- `class FilePathDeltaAnnotation:`

  A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

  - `long index`

    The index of the annotation in the text content part.

  - `JsonValue; type "file_path"constant`

    Always `file_path`.

    - `FILE_PATH("file_path")`

  - `Optional<Long> endIndex`

  - `Optional<FilePath> filePath`

    - `Optional<String> fileId`

      The ID of the file that was generated.

  - `Optional<Long> startIndex`

  - `Optional<String> text`

    The text in the message content that needs to be replaced.

##### Image File

- `class ImageFile:`

  - `String fileId`

    The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

  - `Optional<Detail> detail`

    Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

    - `AUTO("auto")`

    - `LOW("low")`

    - `HIGH("high")`

##### Image File Content Block

- `class ImageFileContentBlock:`

  References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

  - `ImageFile imageFile`

    - `String fileId`

      The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

    - `Optional<Detail> detail`

      Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

      - `AUTO("auto")`

      - `LOW("low")`

      - `HIGH("high")`

  - `JsonValue; type "image_file"constant`

    Always `image_file`.

    - `IMAGE_FILE("image_file")`

##### Image File Delta

- `class ImageFileDelta:`

  - `Optional<Detail> detail`

    Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

    - `AUTO("auto")`

    - `LOW("low")`

    - `HIGH("high")`

  - `Optional<String> fileId`

    The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

##### Image File Delta Block

- `class ImageFileDeltaBlock:`

  References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

  - `long index`

    The index of the content part in the message.

  - `JsonValue; type "image_file"constant`

    Always `image_file`.

    - `IMAGE_FILE("image_file")`

  - `Optional<ImageFileDelta> imageFile`

    - `Optional<Detail> detail`

      Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

      - `AUTO("auto")`

      - `LOW("low")`

      - `HIGH("high")`

    - `Optional<String> fileId`

      The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

##### Image URL

- `class ImageUrl:`

  - `String url`

    The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

  - `Optional<Detail> detail`

    Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

    - `AUTO("auto")`

    - `LOW("low")`

    - `HIGH("high")`

##### Image URL Content Block

- `class ImageUrlContentBlock:`

  References an image URL in the content of a message.

  - `ImageUrl imageUrl`

    - `String url`

      The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

    - `Optional<Detail> detail`

      Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

      - `AUTO("auto")`

      - `LOW("low")`

      - `HIGH("high")`

  - `JsonValue; type "image_url"constant`

    The type of the content part.

    - `IMAGE_URL("image_url")`

##### Image URL Delta

- `class ImageUrlDelta:`

  - `Optional<Detail> detail`

    Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

    - `AUTO("auto")`

    - `LOW("low")`

    - `HIGH("high")`

  - `Optional<String> url`

    The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

##### Image URL Delta Block

- `class ImageUrlDeltaBlock:`

  References an image URL in the content of a message.

  - `long index`

    The index of the content part in the message.

  - `JsonValue; type "image_url"constant`

    Always `image_url`.

    - `IMAGE_URL("image_url")`

  - `Optional<ImageUrlDelta> imageUrl`

    - `Optional<Detail> detail`

      Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

      - `AUTO("auto")`

      - `LOW("low")`

      - `HIGH("high")`

    - `Optional<String> url`

      The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

##### Message

- `class Message:`

  Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

  - `String id`

    The identifier, which can be referenced in API endpoints.

  - `Optional<String> assistantId`

    If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

  - `Optional<List<Attachment>> attachments`

    A list of files attached to the message, and the tools they were added to.

    - `Optional<String> fileId`

      The ID of the file to attach to the message.

    - `Optional<List<Tool>> tools`

      The tools to add this file to.

      - `class CodeInterpreterTool:`

        - `JsonValue; type "code_interpreter"constant`

          The type of tool being defined: `code_interpreter`

          - `CODE_INTERPRETER("code_interpreter")`

      - `JsonValue;`

        - `JsonValue; type "file_search"constant`

          The type of tool being defined: `file_search`

          - `FILE_SEARCH("file_search")`

  - `Optional<Long> completedAt`

    The Unix timestamp (in seconds) for when the message was completed.

  - `List<MessageContent> content`

    The content of the message in array of text and/or images.

    - `class ImageFileContentBlock:`

      References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

      - `ImageFile imageFile`

        - `String fileId`

          The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

        - `Optional<Detail> detail`

          Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_file"constant`

        Always `image_file`.

        - `IMAGE_FILE("image_file")`

    - `class ImageUrlContentBlock:`

      References an image URL in the content of a message.

      - `ImageUrl imageUrl`

        - `String url`

          The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

        - `Optional<Detail> detail`

          Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

      - `JsonValue; type "image_url"constant`

        The type of the content part.

        - `IMAGE_URL("image_url")`

    - `class TextContentBlock:`

      The text content that is part of a message.

      - `Text text`

        - `List<Annotation> annotations`

          - `class FileCitationAnnotation:`

            A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

            - `long endIndex`

            - `FileCitation fileCitation`

              - `String fileId`

                The ID of the specific File the citation is from.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_citation"constant`

              Always `file_citation`.

              - `FILE_CITATION("file_citation")`

          - `class FilePathAnnotation:`

            A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

            - `long endIndex`

            - `FilePath filePath`

              - `String fileId`

                The ID of the file that was generated.

            - `long startIndex`

            - `String text`

              The text in the message content that needs to be replaced.

            - `JsonValue; type "file_path"constant`

              Always `file_path`.

              - `FILE_PATH("file_path")`

        - `String value`

          The data that makes up the text.

      - `JsonValue; type "text"constant`

        Always `text`.

        - `TEXT("text")`

    - `class RefusalContentBlock:`

      The refusal content generated by the assistant.

      - `String refusal`

      - `JsonValue; type "refusal"constant`

        Always `refusal`.

        - `REFUSAL("refusal")`

  - `long createdAt`

    The Unix timestamp (in seconds) for when the message was created.

  - `Optional<Long> incompleteAt`

    The Unix timestamp (in seconds) for when the message was marked as incomplete.

  - `Optional<IncompleteDetails> incompleteDetails`

    On an incomplete message, details about why the message is incomplete.

    - `Reason reason`

      The reason the message is incomplete.

      - `CONTENT_FILTER("content_filter")`

      - `MAX_TOKENS("max_tokens")`

      - `RUN_CANCELLED("run_cancelled")`

      - `RUN_EXPIRED("run_expired")`

      - `RUN_FAILED("run_failed")`

  - `Optional<Metadata> metadata`

    Set of 16 key-value pairs that can be attached to an object. This can be
    useful for storing additional information about the object in a structured
    format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings
    with a maximum length of 512 characters.

  - `JsonValue; object_ "thread.message"constant`

    The object type, which is always `thread.message`.

    - `THREAD_MESSAGE("thread.message")`

  - `Role role`

    The entity that produced the message. One of `user` or `assistant`.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `Optional<String> runId`

    The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

  - `Status status`

    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

    - `IN_PROGRESS("in_progress")`

    - `INCOMPLETE("incomplete")`

    - `COMPLETED("completed")`

  - `String threadId`

    The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

##### Message Content

- `class MessageContent: A class that can be one of several variants.union`

  References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

  - `class ImageFileContentBlock:`

    References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

    - `ImageFile imageFile`

      - `String fileId`

        The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

      - `Optional<Detail> detail`

        Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

    - `JsonValue; type "image_file"constant`

      Always `image_file`.

      - `IMAGE_FILE("image_file")`

  - `class ImageUrlContentBlock:`

    References an image URL in the content of a message.

    - `ImageUrl imageUrl`

      - `String url`

        The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

      - `Optional<Detail> detail`

        Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

    - `JsonValue; type "image_url"constant`

      The type of the content part.

      - `IMAGE_URL("image_url")`

  - `class TextContentBlock:`

    The text content that is part of a message.

    - `Text text`

      - `List<Annotation> annotations`

        - `class FileCitationAnnotation:`

          A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

          - `long endIndex`

          - `FileCitation fileCitation`

            - `String fileId`

              The ID of the specific File the citation is from.

          - `long startIndex`

          - `String text`

            The text in the message content that needs to be replaced.

          - `JsonValue; type "file_citation"constant`

            Always `file_citation`.

            - `FILE_CITATION("file_citation")`

        - `class FilePathAnnotation:`

          A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

          - `long endIndex`

          - `FilePath filePath`

            - `String fileId`

              The ID of the file that was generated.

          - `long startIndex`

          - `String text`

            The text in the message content that needs to be replaced.

          - `JsonValue; type "file_path"constant`

            Always `file_path`.

            - `FILE_PATH("file_path")`

      - `String value`

        The data that makes up the text.

    - `JsonValue; type "text"constant`

      Always `text`.

      - `TEXT("text")`

  - `class RefusalContentBlock:`

    The refusal content generated by the assistant.

    - `String refusal`

    - `JsonValue; type "refusal"constant`

      Always `refusal`.

      - `REFUSAL("refusal")`

##### Message Content Delta

- `class MessageContentDelta: A class that can be one of several variants.union`

  References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

  - `class ImageFileDeltaBlock:`

    References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

    - `long index`

      The index of the content part in the message.

    - `JsonValue; type "image_file"constant`

      Always `image_file`.

      - `IMAGE_FILE("image_file")`

    - `Optional<ImageFileDelta> imageFile`

      - `Optional<Detail> detail`

        Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

      - `Optional<String> fileId`

        The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

  - `class TextDeltaBlock:`

    The text content that is part of a message.

    - `long index`

      The index of the content part in the message.

    - `JsonValue; type "text"constant`

      Always `text`.

      - `TEXT("text")`

    - `Optional<TextDelta> text`

      - `Optional<List<AnnotationDelta>> annotations`

        - `class FileCitationDeltaAnnotation:`

          A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

          - `long index`

            The index of the annotation in the text content part.

          - `JsonValue; type "file_citation"constant`

            Always `file_citation`.

            - `FILE_CITATION("file_citation")`

          - `Optional<Long> endIndex`

          - `Optional<FileCitation> fileCitation`

            - `Optional<String> fileId`

              The ID of the specific File the citation is from.

            - `Optional<String> quote`

              The specific quote in the file.

          - `Optional<Long> startIndex`

          - `Optional<String> text`

            The text in the message content that needs to be replaced.

        - `class FilePathDeltaAnnotation:`

          A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

          - `long index`

            The index of the annotation in the text content part.

          - `JsonValue; type "file_path"constant`

            Always `file_path`.

            - `FILE_PATH("file_path")`

          - `Optional<Long> endIndex`

          - `Optional<FilePath> filePath`

            - `Optional<String> fileId`

              The ID of the file that was generated.

          - `Optional<Long> startIndex`

          - `Optional<String> text`

            The text in the message content that needs to be replaced.

      - `Optional<String> value`

        The data that makes up the text.

  - `class RefusalDeltaBlock:`

    The refusal content that is part of a message.

    - `long index`

      The index of the refusal part in the message.

    - `JsonValue; type "refusal"constant`

      Always `refusal`.

      - `REFUSAL("refusal")`

    - `Optional<String> refusal`

  - `class ImageUrlDeltaBlock:`

    References an image URL in the content of a message.

    - `long index`

      The index of the content part in the message.

    - `JsonValue; type "image_url"constant`

      Always `image_url`.

      - `IMAGE_URL("image_url")`

    - `Optional<ImageUrlDelta> imageUrl`

      - `Optional<Detail> detail`

        Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

      - `Optional<String> url`

        The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

##### Message Content Part Param

- `class MessageContentPartParam: A class that can be one of several variants.union`

  References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

  - `class ImageFileContentBlock:`

    References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

    - `ImageFile imageFile`

      - `String fileId`

        The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

      - `Optional<Detail> detail`

        Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

    - `JsonValue; type "image_file"constant`

      Always `image_file`.

      - `IMAGE_FILE("image_file")`

  - `class ImageUrlContentBlock:`

    References an image URL in the content of a message.

    - `ImageUrl imageUrl`

      - `String url`

        The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

      - `Optional<Detail> detail`

        Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

        - `AUTO("auto")`

        - `LOW("low")`

        - `HIGH("high")`

    - `JsonValue; type "image_url"constant`

      The type of the content part.

      - `IMAGE_URL("image_url")`

  - `class TextContentBlockParam:`

    The text content that is part of a message.

    - `String text`

      Text content to be sent to the model

    - `JsonValue; type "text"constant`

      Always `text`.

      - `TEXT("text")`

##### Message Deleted

- `class MessageDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "thread.message.deleted"constant`

    - `THREAD_MESSAGE_DELETED("thread.message.deleted")`

##### Message Delta

- `class MessageDelta:`

  The delta containing the fields that have changed on the Message.

  - `Optional<List<MessageContentDelta>> content`

    The content of the message in array of text and/or images.

    - `class ImageFileDeltaBlock:`

      References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

      - `long index`

        The index of the content part in the message.

      - `JsonValue; type "image_file"constant`

        Always `image_file`.

        - `IMAGE_FILE("image_file")`

      - `Optional<ImageFileDelta> imageFile`

        - `Optional<Detail> detail`

          Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

        - `Optional<String> fileId`

          The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

    - `class TextDeltaBlock:`

      The text content that is part of a message.

      - `long index`

        The index of the content part in the message.

      - `JsonValue; type "text"constant`

        Always `text`.

        - `TEXT("text")`

      - `Optional<TextDelta> text`

        - `Optional<List<AnnotationDelta>> annotations`

          - `class FileCitationDeltaAnnotation:`

            A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

            - `long index`

              The index of the annotation in the text content part.

            - `JsonValue; type "file_citation"constant`

              Always `file_citation`.

              - `FILE_CITATION("file_citation")`

            - `Optional<Long> endIndex`

            - `Optional<FileCitation> fileCitation`

              - `Optional<String> fileId`

                The ID of the specific File the citation is from.

              - `Optional<String> quote`

                The specific quote in the file.

            - `Optional<Long> startIndex`

            - `Optional<String> text`

              The text in the message content that needs to be replaced.

          - `class FilePathDeltaAnnotation:`

            A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

            - `long index`

              The index of the annotation in the text content part.

            - `JsonValue; type "file_path"constant`

              Always `file_path`.

              - `FILE_PATH("file_path")`

            - `Optional<Long> endIndex`

            - `Optional<FilePath> filePath`

              - `Optional<String> fileId`

                The ID of the file that was generated.

            - `Optional<Long> startIndex`

            - `Optional<String> text`

              The text in the message content that needs to be replaced.

        - `Optional<String> value`

          The data that makes up the text.

    - `class RefusalDeltaBlock:`

      The refusal content that is part of a message.

      - `long index`

        The index of the refusal part in the message.

      - `JsonValue; type "refusal"constant`

        Always `refusal`.

        - `REFUSAL("refusal")`

      - `Optional<String> refusal`

    - `class ImageUrlDeltaBlock:`

      References an image URL in the content of a message.

      - `long index`

        The index of the content part in the message.

      - `JsonValue; type "image_url"constant`

        Always `image_url`.

        - `IMAGE_URL("image_url")`

      - `Optional<ImageUrlDelta> imageUrl`

        - `Optional<Detail> detail`

          Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

          - `AUTO("auto")`

          - `LOW("low")`

          - `HIGH("high")`

        - `Optional<String> url`

          The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

  - `Optional<Role> role`

    The entity that produced the message. One of `user` or `assistant`.

    - `USER("user")`

    - `ASSISTANT("assistant")`

##### Message Delta Event

- `class MessageDeltaEvent:`

  Represents a message delta i.e. any changed fields on a message during streaming.

  - `String id`

    The identifier of the message, which can be referenced in API endpoints.

  - `MessageDelta delta`

    The delta containing the fields that have changed on the Message.

    - `Optional<List<MessageContentDelta>> content`

      The content of the message in array of text and/or images.

      - `class ImageFileDeltaBlock:`

        References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

        - `long index`

          The index of the content part in the message.

        - `JsonValue; type "image_file"constant`

          Always `image_file`.

          - `IMAGE_FILE("image_file")`

        - `Optional<ImageFileDelta> imageFile`

          - `Optional<Detail> detail`

            Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

            - `AUTO("auto")`

            - `LOW("low")`

            - `HIGH("high")`

          - `Optional<String> fileId`

            The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

      - `class TextDeltaBlock:`

        The text content that is part of a message.

        - `long index`

          The index of the content part in the message.

        - `JsonValue; type "text"constant`

          Always `text`.

          - `TEXT("text")`

        - `Optional<TextDelta> text`

          - `Optional<List<AnnotationDelta>> annotations`

            - `class FileCitationDeltaAnnotation:`

              A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

              - `long index`

                The index of the annotation in the text content part.

              - `JsonValue; type "file_citation"constant`

                Always `file_citation`.

                - `FILE_CITATION("file_citation")`

              - `Optional<Long> endIndex`

              - `Optional<FileCitation> fileCitation`

                - `Optional<String> fileId`

                  The ID of the specific File the citation is from.

                - `Optional<String> quote`

                  The specific quote in the file.

              - `Optional<Long> startIndex`

              - `Optional<String> text`

                The text in the message content that needs to be replaced.

            - `class FilePathDeltaAnnotation:`

              A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

              - `long index`

                The index of the annotation in the text content part.

              - `JsonValue; type "file_path"constant`

                Always `file_path`.

                - `FILE_PATH("file_path")`

              - `Optional<Long> endIndex`

              - `Optional<FilePath> filePath`

                - `Optional<String> fileId`

                  The ID of the file that was generated.

              - `Optional<Long> startIndex`

              - `Optional<String> text`

                The text in the message content that needs to be replaced.

          - `Optional<String> value`

            The data that makes up the text.

      - `class RefusalDeltaBlock:`

        The refusal content that is part of a message.

        - `long index`

          The index of the refusal part in the message.

        - `JsonValue; type "refusal"constant`

          Always `refusal`.

          - `REFUSAL("refusal")`

        - `Optional<String> refusal`

      - `class ImageUrlDeltaBlock:`

        References an image URL in the content of a message.

        - `long index`

          The index of the content part in the message.

        - `JsonValue; type "image_url"constant`

          Always `image_url`.

          - `IMAGE_URL("image_url")`

        - `Optional<ImageUrlDelta> imageUrl`

          - `Optional<Detail> detail`

            Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

            - `AUTO("auto")`

            - `LOW("low")`

            - `HIGH("high")`

          - `Optional<String> url`

            The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

    - `Optional<Role> role`

      The entity that produced the message. One of `user` or `assistant`.

      - `USER("user")`

      - `ASSISTANT("assistant")`

  - `JsonValue; object_ "thread.message.delta"constant`

    The object type, which is always `thread.message.delta`.

    - `THREAD_MESSAGE_DELTA("thread.message.delta")`

##### Refusal Content Block

- `class RefusalContentBlock:`

  The refusal content generated by the assistant.

  - `String refusal`

  - `JsonValue; type "refusal"constant`

    Always `refusal`.

    - `REFUSAL("refusal")`

##### Refusal Delta Block

- `class RefusalDeltaBlock:`

  The refusal content that is part of a message.

  - `long index`

    The index of the refusal part in the message.

  - `JsonValue; type "refusal"constant`

    Always `refusal`.

    - `REFUSAL("refusal")`

  - `Optional<String> refusal`

##### Text

- `class Text:`

  - `List<Annotation> annotations`

    - `class FileCitationAnnotation:`

      A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

      - `long endIndex`

      - `FileCitation fileCitation`

        - `String fileId`

          The ID of the specific File the citation is from.

      - `long startIndex`

      - `String text`

        The text in the message content that needs to be replaced.

      - `JsonValue; type "file_citation"constant`

        Always `file_citation`.

        - `FILE_CITATION("file_citation")`

    - `class FilePathAnnotation:`

      A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

      - `long endIndex`

      - `FilePath filePath`

        - `String fileId`

          The ID of the file that was generated.

      - `long startIndex`

      - `String text`

        The text in the message content that needs to be replaced.

      - `JsonValue; type "file_path"constant`

        Always `file_path`.

        - `FILE_PATH("file_path")`

  - `String value`

    The data that makes up the text.

##### Text Content Block

- `class TextContentBlock:`

  The text content that is part of a message.

  - `Text text`

    - `List<Annotation> annotations`

      - `class FileCitationAnnotation:`

        A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

        - `long endIndex`

        - `FileCitation fileCitation`

          - `String fileId`

            The ID of the specific File the citation is from.

        - `long startIndex`

        - `String text`

          The text in the message content that needs to be replaced.

        - `JsonValue; type "file_citation"constant`

          Always `file_citation`.

          - `FILE_CITATION("file_citation")`

      - `class FilePathAnnotation:`

        A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

        - `long endIndex`

        - `FilePath filePath`

          - `String fileId`

            The ID of the file that was generated.

        - `long startIndex`

        - `String text`

          The text in the message content that needs to be replaced.

        - `JsonValue; type "file_path"constant`

          Always `file_path`.

          - `FILE_PATH("file_path")`

    - `String value`

      The data that makes up the text.

  - `JsonValue; type "text"constant`

    Always `text`.

    - `TEXT("text")`

##### Text Content Block Param

- `class TextContentBlockParam:`

  The text content that is part of a message.

  - `String text`

    Text content to be sent to the model

  - `JsonValue; type "text"constant`

    Always `text`.

    - `TEXT("text")`

##### Text Delta

- `class TextDelta:`

  - `Optional<List<AnnotationDelta>> annotations`

    - `class FileCitationDeltaAnnotation:`

      A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

      - `long index`

        The index of the annotation in the text content part.

      - `JsonValue; type "file_citation"constant`

        Always `file_citation`.

        - `FILE_CITATION("file_citation")`

      - `Optional<Long> endIndex`

      - `Optional<FileCitation> fileCitation`

        - `Optional<String> fileId`

          The ID of the specific File the citation is from.

        - `Optional<String> quote`

          The specific quote in the file.

      - `Optional<Long> startIndex`

      - `Optional<String> text`

        The text in the message content that needs to be replaced.

    - `class FilePathDeltaAnnotation:`

      A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

      - `long index`

        The index of the annotation in the text content part.

      - `JsonValue; type "file_path"constant`

        Always `file_path`.

        - `FILE_PATH("file_path")`

      - `Optional<Long> endIndex`

      - `Optional<FilePath> filePath`

        - `Optional<String> fileId`

          The ID of the file that was generated.

      - `Optional<Long> startIndex`

      - `Optional<String> text`

        The text in the message content that needs to be replaced.

  - `Optional<String> value`

    The data that makes up the text.

##### Text Delta Block

- `class TextDeltaBlock:`

  The text content that is part of a message.

  - `long index`

    The index of the content part in the message.

  - `JsonValue; type "text"constant`

    Always `text`.

    - `TEXT("text")`

  - `Optional<TextDelta> text`

    - `Optional<List<AnnotationDelta>> annotations`

      - `class FileCitationDeltaAnnotation:`

        A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

        - `long index`

          The index of the annotation in the text content part.

        - `JsonValue; type "file_citation"constant`

          Always `file_citation`.

          - `FILE_CITATION("file_citation")`

        - `Optional<Long> endIndex`

        - `Optional<FileCitation> fileCitation`

          - `Optional<String> fileId`

            The ID of the specific File the citation is from.

          - `Optional<String> quote`

            The specific quote in the file.

        - `Optional<Long> startIndex`

        - `Optional<String> text`

          The text in the message content that needs to be replaced.

      - `class FilePathDeltaAnnotation:`

        A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

        - `long index`

          The index of the annotation in the text content part.

        - `JsonValue; type "file_path"constant`

          Always `file_path`.

          - `FILE_PATH("file_path")`

        - `Optional<Long> endIndex`

        - `Optional<FilePath> filePath`

          - `Optional<String> fileId`

            The ID of the file that was generated.

        - `Optional<Long> startIndex`

        - `Optional<String> text`

          The text in the message content that needs to be replaced.

    - `Optional<String> value`

      The data that makes up the text.
