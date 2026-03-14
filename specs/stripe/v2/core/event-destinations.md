# Event Destinations

Set up an event destination to receive events from Stripe across multiple destination types, including [webhook endpoints](https://docs.stripe.com/webhooks.md) and [Amazon EventBridge](https://docs.stripe.com/event-destinations/eventbridge.md). Event destinations support receiving [thin events](../events.md) and [snapshot events](../../events.md).

## Endpoints

### Create an Event Destination

- [POST /v2/core/event_destinations](event-destinations/create.md)

### Update an Event Destination

- [POST /v2/core/event_destinations/:id](event-destinations/update.md)

### Retrieve an Event Destination

- [GET /v2/core/event_destinations/:id](event-destinations/retrieve.md)

### List Event Destinations

- [GET /v2/core/event_destinations](event-destinations/list.md)

### Delete an Event Destination

- [DELETE /v2/core/event_destinations/:id](event-destinations/delete.md)

### Disable an Event Destination

- [POST /v2/core/event_destinations/:id/disable](event-destinations/disable.md)

### Enable an Event Destination

- [POST /v2/core/event_destinations/:id/enable](event-destinations/enable.md)
