# Scheduled Queries

If you have [scheduled a Sigma query](https://docs.stripe.com/docs/sigma/scheduled-queries.md), you’ll receive a `sigma.scheduled_query_run.created` webhook each time the query runs. The webhook contains a `ScheduledQueryRun` object, which you can use to retrieve the query results.

## Endpoints

### Retrieve a scheduled query run

- [GET /v1/sigma/scheduled_query_runs/:id](scheduled_queries/retrieve.md)

### List all scheduled query runs

- [GET /v1/sigma/scheduled_query_runs](scheduled_queries/list.md)
