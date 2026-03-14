# TaxSummary

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxsummary
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TaxSummary
> Canonical entity: `TaxSummary`

Applicable for non-US locale companies only. The information below provides a reference on how to access the Tax Summary report from the QuickBooks Online Report Service.

## The tax Summary report object

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
    "ReportName": "TaxSummary",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "StartPeriod": "2015-04-26",
    "Currency": "EUR",
    "EndPeriod": "2015-04-26",
    "Time": "2015-04-26T22:23:51-07:00",
    "SummarizeColumnsBy": "Total"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "Case 01 Vente, prestations de services"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 01"
      },
      {
        "ColData": [
          {
            "value": "Case 02 Autres operations imposables"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 02"
      },
      {
        "ColData": [
          {
            "value": "Case 22 2 Report du cr\u00c3\u00a9dit apparaissant ligne 27 de la pr\u00c3\u00a9c\u00c3\u00a9dente d\u00c3\u00a9claration"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 22"
      },
      {
        "group": "Case 23",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 23 Total TVA d\u00c3\u00a9ductible (lignes 19 \u00c3  22)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "group": "Case 25",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 25 Cr\u00c3\u00a9dit de TVA (ligne 23 \u00e2\u20ac\u201c ligne 16)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "group": "Case 27",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 27 Cr\u00c3\u00a9dit \u00c3  reporter (ligne 25 \u00e2\u20ac\u201c ligne 26 \u00e2\u20ac\u201c ligne AA) (Cette somme est \u00c3  reporter ligne 22 de la prochaine d\u00c3\u00a9claration)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "group": "Case 28",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 28 TVA nette due (ligne 16 \u00e2\u20ac\u201c ligne 23)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "ColData": [
          {
            "value": "Case 29 Taxes assimil\u00c3\u00a9es calcul\u00c3\u00a9es sur annexe no 3310 A"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 29"
      },
      {
        "ColData": [
          {
            "value": "Case 30 Sommes \u00c3  imputer, y compris acompte cong\u00c3\u00a9s"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 30"
      },
      {
        "ColData": [
          {
            "value": "Case 31 Sommes \u00c3  ajouter, y compris acompte cong\u00c3\u00a9s"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 31"
      },
      {
        "group": "Case 32",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 32 Total \u00c3  payer (lignes 28 + 29 - 30 + 31 \u00e2\u20ac\u201c AB)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "String",
        "ColTitle": ""
      },
      {
        "ColType": "Money",
        "ColTitle": "Total"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/TaxSummary?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `taxsummaryquery`

<details>
<summary>Show schema for `taxsummaryquery`</summary>

#### taxsummaryquery

Model type: `object`

##### `agency_id`

Required: Required
Type: `String`
Default: <span class="literal">Report_Date</span>

The ID of the Tax Agency for which to generate the report. Read the TaxAgency object to get all valid values for this field.

##### `accounting_method`

Required: Optional
Type: `String`
Default: Method defined in preferences by the <span class="literal">Preferences.ReportPrefs.ReportBasis</span> attribute

The accounting method used in the report. Supported Values:`Cash`, `Accrual`

##### `end_date`

Required: Optional
Type: `String`

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range. Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order. Supported Values: `ascend`, `descend`

##### `start_date`

Required: Optional
Type: `String`

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

</details>

### Sample Query

This query returns the tax summary report.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/TaxSummary?agency_id=1&start_date=2015-04-26&end_date=2015-04-26"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "TaxSummary",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "StartPeriod": "2015-04-26",
    "Currency": "EUR",
    "EndPeriod": "2015-04-26",
    "Time": "2015-04-26T22:23:51-07:00",
    "SummarizeColumnsBy": "Total"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "Case 01 Vente, prestations de services"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 01"
      },
      {
        "ColData": [
          {
            "value": "Case 02 Autres operations imposables"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 02"
      },
      {
        "ColData": [
          {
            "value": "Case 22 2 Report du cr\u00c3\u00a9dit apparaissant ligne 27 de la pr\u00c3\u00a9c\u00c3\u00a9dente d\u00c3\u00a9claration"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 22"
      },
      {
        "group": "Case 23",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 23 Total TVA d\u00c3\u00a9ductible (lignes 19 \u00c3  22)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "group": "Case 25",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 25 Cr\u00c3\u00a9dit de TVA (ligne 23 \u00e2\u20ac\u201c ligne 16)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "group": "Case 27",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 27 Cr\u00c3\u00a9dit \u00c3  reporter (ligne 25 \u00e2\u20ac\u201c ligne 26 \u00e2\u20ac\u201c ligne AA) (Cette somme est \u00c3  reporter ligne 22 de la prochaine d\u00c3\u00a9claration)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "group": "Case 28",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 28 TVA nette due (ligne 16 \u00e2\u20ac\u201c ligne 23)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      },
      {
        "ColData": [
          {
            "value": "Case 29 Taxes assimil\u00c3\u00a9es calcul\u00c3\u00a9es sur annexe no 3310 A"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 29"
      },
      {
        "ColData": [
          {
            "value": "Case 30 Sommes \u00c3  imputer, y compris acompte cong\u00c3\u00a9s"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 30"
      },
      {
        "ColData": [
          {
            "value": "Case 31 Sommes \u00c3  ajouter, y compris acompte cong\u00c3\u00a9s"
          },
          {
            "value": ""
          }
        ],
        "group": "Case 31"
      },
      {
        "group": "Case 32",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Case 32 Total \u00c3  payer (lignes 28 + 29 - 30 + 31 \u00e2\u20ac\u201c AB)"
            },
            {
              "value": "0.00"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "String",
        "ColTitle": ""
      },
      {
        "ColType": "Money",
        "ColTitle": "Total"
      }
    ]
  }
}
```
