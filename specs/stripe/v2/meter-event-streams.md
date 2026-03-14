# Meter Event Streams

You can send a higher-throughput of meter events using meter event streams. For this flow, you must first create a meter event session, which will provide you with a session token. You can then create meter events through the meter event stream endpoint, using the session token for authentication. The session tokens are short-lived and you will need to create a new meter event session when the token expires.

## Endpoints

### Create a Meter Event Stream Authentication Session

- [POST /v2/billing/meter_event_session](meter-event-streams/meter-event-sessions/create.md)

### Create a Meter Event with asynchronous validation

- [POST /v2/billing/meter_event_stream](billing/meter-event-sessions/create-async.md)
