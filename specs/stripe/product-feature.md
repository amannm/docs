# Product Feature

A product_feature represents an attachment between a feature and a product. When a product is purchased that has a feature attached, Stripe will create an entitlement to the feature for the purchasing customer.

## Endpoints

### List all features attached to a product

- [GET /v1/products/:id/features](product-feature/list.md)

### Attach a feature to a product

- [POST /v1/products/:id/features](product-feature/attach.md)

### Remove a feature from a product

- [DELETE /v1/products/:id/features/:id](product-feature/remove.md)
