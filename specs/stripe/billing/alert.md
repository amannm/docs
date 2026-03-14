# Alerts

A billing alert is a resource that notifies you when a certain usage threshold on a meter is crossed. For example, you might create a billing alert to notify you when a certain user made 100 API requests.

## Endpoints

### Create a billing alert

- [POST /v1/billing/alerts](alert/create.md)

### Retrieve a billing alert

- [GET /v1/billing/alerts/:id](alert/retrieve.md)

### List billing alerts

- [GET /v1/billing/alerts](alert/list.md)

### Activate a billing alert

- [POST /v1/billing/alerts/:id/activate](alert/activate.md)

### Archive a billing alert

- [POST /v1/billing/alerts/:id/archive](alert/archive.md)

### Deactivate a billing alert

- [POST /v1/billing/alerts/:id/deactivate](alert/deactivate.md)
