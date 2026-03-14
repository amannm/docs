# Report Runs

The `ReportRun` object represents an instance of a `Report` generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to the results.

## Endpoints

### Create a Report Run

- [POST /v2/reporting/report_runs](report-runs/create.md)

### Retrieve a Report Run

- [GET /v2/reporting/report_runs/:id](report-runs/retrieve.md)
