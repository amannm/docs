# Terminal Hardware Order

A TerminalHardwareOrder represents an order for Terminal hardware, containing information such as the price, shipping information and the items ordered.

## Endpoints

### Create a Terminal Hardware Order

- [POST /v1/terminal/hardware_orders](hardware_orders/create.md)

### Retrieve a Terminal Hardware Order

- [GET /v1/terminal/hardware_orders/:id](hardware_orders/retrieve.md)

### List all Terminal Hardware Orders

- [GET /v1/terminal/hardware_orders](hardware_orders/list.md)

### Cancel a Terminal Hardware Order

- [POST /v1/terminal/hardware_orders/:id/cancel](hardware_orders/cancel.md)

### Preview a Terminal Hardware Order

- [GET /v1/terminal/hardware_orders/preview](hardware_orders/preview.md)

### Test mode: Mark a Terminal Hardware Order as Delivered

- [POST /v1/test_helpers/terminal/hardware_orders/:id/deliver](hardware_orders/test_mode_deliver.md)

### Test mode: Mark a Terminal Hardware Order as Ready To Ship

- [POST /v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship](hardware_orders/test_mode_mark_ready_to_ship.md)

### Test mode: Mark a Terminal Hardware Order as Shipped

- [POST /v1/test_helpers/terminal/hardware_orders/:id/ship](hardware_orders/test_mode_ship.md)

### Test mode: Mark a Terminal Hardware Order as Undeliverable

- [POST /v1/test_helpers/terminal/hardware_orders/:id/mark_undeliverable](hardware_orders/test_mode_mark_undeliverable.md)
