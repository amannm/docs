# Retrieve a file

Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to [access file contents](https://docs.stripe.com/docs/file-upload.md#download-file-contents).

## Returns

If the identifier you provide is valid, a file object returns. If not, Stripe raises [an error](retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "file_1Mr4LDLkdIwHu7ixFCz0dZiH",
  "object": "file",
  "created": 1680116847,
  "expires_at": 1703444847,
  "filename": "file.png",
  "links": {
    "object": "list",
    "data": [],
    "has_more": false,
    "url": "/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"
  },
  "purpose": "dispute_evidence",
  "size": 8429,
  "title": null,
  "type": "png",
  "url": "https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"
}
```
