# APAgingDetail

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/apagingdetail
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / APAgingDetail
> Canonical entity: `APAgingDetail`

The information below provides a reference on how to access the AP Aging Detail report from the QuickBooks Online Report Service.

## The ap aging detail report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### reporttoplevel

Model type: `object`

#### `Header`

The report header.

<details>
<summary>Child attributes for `Header`</summary>

##### reportheader

Model type: `object`

###### `Customer`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `ReportName`

Type: `String`

Name of the report.

###### `Vendor`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `Option`

Container for one or more name/value pairs that return additional information about the report contents.

<details>
<summary>Child attributes for `Option`</summary>

###### reportoption

Model type: `object`

###### `name`

Type: `String`

Supported Names: `AccountingStandard`—Indicates the accounting standard being used for this report. Returned with ProfitAndLoss and BalanceSheet reports, only. `NoReportData`—Used to signal whether report contains data. If `true`, report contains no data. If `false`, report contains data. Returned for every report type.

###### `value`

Type: `String`

The value of the parameter, as passed in with the report endpoint URL.

</details>

###### `Item`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `Employee`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `ReportBasis`

Type: `ReportBasisEnum`

Accounting method. Possible values include `Cash` and `Accrual`.

###### `StartPeriod`

Type: `String`

The date specified by the start_date query parameter submitted with the request. Format is `yyyy-mm-dd`.

###### `Class`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `Currency`

Type: `String`

A string containing the currency code associated with the report.

###### `EndPeriod`

Type: `String`

The date specified by the end_date query parameter submitted with the request. Format is `yyyy-mm-dd`.

###### `Time`

Type: `DateTime`

Date and timestamp of the report.

###### `Department`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `SummarizeColumnsBy`

Type: `SummarizeColumnsByEnum`

The method by which report columns are organized. This contains the value specified by the `summarize_column_by` query parameter submitted with the request.

</details>

#### `Rows`

Top level container holding information for report rows.

<details>
<summary>Child attributes for `Rows`</summary>

##### reportrows

Model type: `object`

###### `Row [0..n]`

Represents a row in a report. A group of rows is enclosed in a `Rows` container. Rows may be nested either as a single row or in sets, based on the accounts represented in the report and query parameters specified in the request. Parameters:

`type`—As an enclosing section of sub-rows, this is always the string, `Section`. As a leaf row, this is always the string, `Data`.

`group`—The group name, valid when `type=Section`. Possible values include: `Income`, `COGS`, `GrossProfit`, `Expenses`, `NetOperatingIncome`, `OtherIncome`, `OtherExpenses`, `NetOtherIncome`, `NetIncome`

<details>
<summary>Child attributes for `Row [0..n]`</summary>

###### reportrow

Model type: `object`

###### `ColData`

Information for each column of a leaf row `Row type=Data`. There must be a `ColData` definition for each column defined in the `Columns` section. Parameters:

`id`—The reference id of the entity as returned in the Identity field. Returned where applicable.

`value`—The value for column. The type of value is based on the column type.

`href`—The link to the quick zoom data for this cell, available when the report endpoint specifies the `qzurl` query parameter. The `qzurl` query parameter is supported on a report by report basis; check the list of query parameters for the specific report to determine support.

The value of the parameter is localized.

###### `Summary`

Summary row for a report section. It is the cumulative total amount of money in the account, including the sub accounts.

###### `Rows`

Container for one or more leaf rows.

###### `Header`

Header row for the report section.

</details>

</details>

#### `Columns`

Top level container holding information for report columns or subcolumns.

<details>
<summary>Child attributes for `Columns`</summary>

##### reportcolumns

Model type: `object`

###### `Column [0..n]`

Container for an individual report column definition.

<details>
<summary>Child attributes for `Column [0..n]`</summary>

###### reportcolumn

Model type: `object`

###### `ColType`

Type: `ColumnTypeEnum`

The type of information found in the column. Possible values include:

`Account`—This column in the row represents an account for the row item. The row further defines the specific account.

`Money`—This column in the row represents an amount for the row item.

###### `ColTitle`

Type: `String`

The column label. This string appears at the top of the column. If not defined, the column does not have a label. The value of this attribute is localized.

</details>

</details>

#### Example

```json
{
  "Header": {
    "ReportName": "AgedPayableDetail",
    "Currency": "USD",
    "EndPeriod": "2015-06-30",
    "Option": [
      {
        "Name": "report_date",
        "Value": "2015-06-30"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "Time": "2016-03-08T14:34:28-08:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "value": "31 - 60 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "id": "32",
                  "value": "Cal Telephone"
                },
                {
                  "value": "2015-05-24"
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section"
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "Total for 31 - 60 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {},
        "type": "Section"
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "1 - 30 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "id": "48",
                  "value": "PG&E"
                },
                {
                  "value": "2015-06-24"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "id": "51",
                  "value": "Tim Philip Masonry"
                },
                {
                  "value": "2015-06-24"
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section"
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "Total for 1 - 30 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "type": "Section"
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "vend_name",
        "ColTitle": "Vendor"
      },
      {
        "ColType": "due_date",
        "ColTitle": "Due Date"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/AgedPayableDetail?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `agedpayabledetailquery`

<details>
<summary>Show schema for `agedpayabledetailquery`</summary>

#### agedpayabledetailquery

Model type: `object`

##### `shipvia`

Required: Optional
Type: `String`
Default: To include data for all shipping methods

Filter by the shipping method as stored in `Invoice.ShipMethodRef.Name`.
Supported Values: Any shipping method as sent in the `Invoice.ShipMethodRef.Name` attribute at Invoice create- or update-time.

##### `term`

Required: Optional
Type: `String`
Default: to return data for all terms

Filters report contents based on term or terms supplied.
Supported Values: One or more comma separated term IDs as returned in the attribute, `Term.Id` of the Term object response code.

##### `end_duedate`

Required: Optional
Type: `String`
Default: To return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `accounting_method`

Required: Optional
Type: `String`
Default: Preferences.ReportPrefs.ReportBasis

The accounting method used in the report. Supported Values:`Cash`, `Accrual`

##### `start_duedate`

Required: Optional
Type: `String`
Default: To return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `custom1`

Required: Optional
Type: `String`
Default: to include data for all fields

Filter by the specified custom field as defined by the `CustomField` attribute in transaction entities where supported.
Supported Values: Name of custom field.

##### `custom2`

Required: Optional
Type: `String`
Default: to include data for all fields

Filter by the specified custom field as defined by the `CustomField` attribute in transaction entities where supported.
Supported Values: Name of custom field.

##### `custom3`

Required: Optional
Type: `String`
Default: to include data for all fields

Filter by the specified custom field as defined by the `CustomField` attribute in transaction entities where supported.
Supported Values: Name of custom field.

##### `report_date`

Required: Optional
Type: `String`
Default: Today's date

Start date to use for the report, in the format `YYYY-MM-DD`.

##### `num_periods`

Required: Optional
Type: `Integer`
Default: 4

The number of periods to be shown in the report.
Supported Values: A numeric value.

##### `vendor`

Required: Optional
Type: `String`
Default: to return data for all vendors

Filters report contents to include information for specified vendors.
Supported Values: One or more comma separated vendor IDs as returned in the attribute, `Vendor.Id`, of the Vendor object response code.

##### `past_due`

Required: Optional
Type: `Integer`

Filters report contents based on minimum days past due.
Supported Values: Integer number of days. no filtering

##### `aging_period`

Required: Optional
Type: `Decimal`
Default: 30

The number of days in the aging period.
Supported Values: A numeric value.

##### `columns`

Required: Optional
Type: `String`
Default: columns denoted with *

Column types to be shown in the report.
Supported Values: create_by, create_date, doc_num*, due_date*, last_mod_by, last_mod_date, memo*, past_due*, term_name, tx_date*, txn_type*, vend_bill_addr, vend_comp_name, vend_name*, vend_pri_cont, vend_pri_email, vend_pri_tel
 Additional columns with location tracking enabled: dept_name*

<details>
<summary>Show additional values supported based on multicurrency settings for the company.</summary>

#### MULTICURRENCY DISABLED

| Name | Description |
| --- | --- |
| currency | N/A |
| exchange rate | N/A |
| open balance | subt_neg_open_bal* |
| amount | subt_neg_amount* |

#### MULTICURRENCY ENABLED

| Name | Description |
| --- | --- |
| currency | currency |
| exchange rate | exch_rate |
| open balance | neg_foreign_open_bal <br> subt_neg_home_open_bal* |
| amount | neg_foreign_amount <br> subt_neg_home_amount* |

</details>

</details>

### Sample Query

This query returns details of aged payables from first half of 2015.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/AgedPayableDetail?report_date=2015-06-30&start_duedate=2015-01-01&end_duedate=2015-06-30&columns=due_date,vend_name"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "AgedPayableDetail",
    "Currency": "USD",
    "EndPeriod": "2015-06-30",
    "Option": [
      {
        "Name": "report_date",
        "Value": "2015-06-30"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "Time": "2016-03-08T14:34:28-08:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "value": "31 - 60 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "id": "32",
                  "value": "Cal Telephone"
                },
                {
                  "value": "2015-05-24"
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section"
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "Total for 31 - 60 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {},
        "type": "Section"
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "1 - 30 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "id": "48",
                  "value": "PG&E"
                },
                {
                  "value": "2015-06-24"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "id": "51",
                  "value": "Tim Philip Masonry"
                },
                {
                  "value": "2015-06-24"
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section"
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "Total for 1 - 30 days past due"
            },
            {
              "value": ""
            }
          ]
        },
        "type": "Section"
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "vend_name",
        "ColTitle": "Vendor"
      },
      {
        "ColType": "due_date",
        "ColTitle": "Due Date"
      }
    ]
  }
}
```
