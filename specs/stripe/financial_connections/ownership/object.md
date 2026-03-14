# The Account Ownership object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `owners` (object)
  A paginated list of owners for this account.

  - `owners.object` (string)
    String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

  - `owners.data` (array of objects)
    Details about each object.

    - `owners.data.id` (string)
      Unique identifier for the object.

    - `owners.data.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `owners.data.email` (string, nullable)
      The email address of the owner.

    - `owners.data.name` (string)
      The full name of the owner.

    - `owners.data.ownership` (string)
      The ownership object that this owner belongs to.

    - `owners.data.phone` (string, nullable)
      The raw phone number of the owner.

    - `owners.data.raw_address` (string, nullable)
      The raw physical address of the owner.

    - `owners.data.refreshed_at` (timestamp, nullable)
      The timestamp of the refresh that updated this owner.

  - `owners.has_more` (boolean)
    True if this list has another page of items after this one that can be fetched.

  - `owners.url` (string)
    The URL where this list can be accessed.

### The Account Ownership object

```json
{
  "id": "fcaowns_1MwVKR2eZvKYlo2CGV7Mmt6s",
  "object": "linked_account_ownership",
  "created": 1681412227,
  "owners": {
    "object": "list",
    "data": [],
    "has_more": false,
    "url": "/v1/linked_accounts/fca_1MwVKR2eZvKYlo2CoMV2L3PV/owners?ownership=fcaowns_1MwVKR2eZvKYlo2CGV7Mmt6s"
  }
}
```
