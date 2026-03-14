# Delete a plan

Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.

## Returns

An object with the deleted plan’s ID and a deleted flag upon success. Otherwise, this call raises [an error](delete.md#errors), such as if the plan has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "deleted": true
}
```
