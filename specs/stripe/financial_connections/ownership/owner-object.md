# The Account Owner object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `email` (string, nullable)
  The email address of the owner.

- `name` (string)
  The full name of the owner.

- `ownership` (string)
  The ownership object that this owner belongs to.

- `phone` (string, nullable)
  The raw phone number of the owner.

- `raw_address` (string, nullable)
  The raw physical address of the owner.

- `refreshed_at` (timestamp, nullable)
  The timestamp of the refresh that updated this owner.

### The Account Owner object

```json
{
  "id": "fcaown_1NtI9uBHO5VeT9SUKLJU5suZ",
  "object": "financial_connections.account_owner",
  "email": "nobody+janesmith@stripe.com",
  "name": "Jane Smith",
  "ownership": "fcaowns_1NtI9uBHO5VeT9SUSRe21lqt",
  "phone": "+1 555-555-5555",
  "raw_address": "123 Main Street, Everytown USA",
  "refreshed_at": null
}
```
