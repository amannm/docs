# Files

This object represents files hosted on Stripe’s servers. You can upload files with the [create file](files.md#create_file) request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a [Sigma scheduled query](files.md#scheduled_queries)).

Related guide: [File upload guide](https://docs.stripe.com/docs/file-upload.md)

## Endpoints

### Create a file

- [POST /v1/files](files/create.md)

### Retrieve a file

- [GET /v1/files/:id](files/retrieve.md)

### List all files

- [GET /v1/files](files/list.md)
