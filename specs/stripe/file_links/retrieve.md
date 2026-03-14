# Retrieve a file link

Retrieves the file link with the given ID.

## Returns

If the identifier you provide is valid, a file link object returns. If not, Stripe raises [an error](retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "link_1Mr23jLkdIwHu7ix65betcoo",
  "object": "file_link",
  "created": 1680108075,
  "expired": false,
  "expires_at": null,
  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",
  "livemode": false,
  "metadata": {},
  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"
}
```
