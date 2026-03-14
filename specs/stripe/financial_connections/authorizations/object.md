# The Authorization object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `institution_name` (string)
  The name of the institution that this authorization belongs to.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `status` (enum)
  The status of the connection to the Authorization.
Possible enum values:
  - `active`
    Stripe is able to retrieve data from the Authorization without issues.

  - `inactive`
    Stripe cannot retrieve data from the Authorization.

- `status_details` (object)
  Details on the status of this Authorization.

  - `status_details.inactive` (object, nullable)
    Details related to the inactive status of this Authorization.

    - `status_details.inactive.action` (enum)
      The action (if any) to relink the inactive Authorization.
Possible enum values:
      - `none`
        There is no action recommended at this time to resolve the inactive Authorization.

      - `relink_required`
        You may relink the inactive Authorization by having your end user complete the streamlined relink flow.

### The Authorization object

```json
{
  "id": "fcauth_1NSlnc2eZvKYlo2CoamIONix",
  "object": "financial_connections.authorization",
  "institution_name": "StripeBank",
  "livemode": false,
  "status": "active",
  "status_details": {}
}
```
