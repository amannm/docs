# GeneralLedgerFR

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/generalledgerfr
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / GeneralLedgerFR
> Canonical entity: `GeneralLedgerFR`

The information below provides a reference on how to access the General Ledger Detail report from the QuickBooks Report Service. For each specified account, the report shows all the transactions that occurred in that account over a period of time. It includes the beginning balance and total for each account. For France-based companies, use GeneralLedgerFR as the endpoint.

##### Note

The QuickBooks Reports API response for the General Ledger report hierarchy is broken in certain circumstances when there are sub accounts configured in the QuickBooks Online company. Invoke the report endpoint with the `minorversion=3` query parameter to get a well-formed, correct response.

## The general ledger report object

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
    "ReportName": "GeneralLedgerFR",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "StartPeriod": "2021-10-19",
    "Currency": "EUR",
    "EndPeriod": "2021-10-19",
    "Time": "2021-10-19T09:31:18-07:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "82",
              "value": "44566100 TVA d\u00e9ductible"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
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
                  "value": "2021-10-19"
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for 44566100 TVA d\u00e9ductible"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": "200.00"
            },
            {
              "value": ""
            },
            {
              "value": "200.00"
            }
          ]
        }
      },
      {
        "Header": {
          "ColData": [
            {
              "id": "65",
              "value": "51210100 Comptes en monnaie nationale"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
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
                  "value": "2021-10-19"
                },
                {
                  "value": "BQ"
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for 51210100 Comptes en monnaie nationale"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "Header": {
          "ColData": [
            {
              "id": "19",
              "value": "60710000 Achats de Marchandises (ou groupe) A"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
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
                  "value": "2021-10-19"
                },
                {
                  "value": "BQ"
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for 60710000 Achats de Marchandises (ou groupe) A"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "tx_date",
        "ColTitle": "Date"
      },
      {
        "ColType": "journal_code_name",
        "ColTitle": "Journal Code"
      },
      {
        "ColType": "doc_num",
        "ColTitle": "No."
      },
      {
        "ColType": "memo",
        "ColTitle": "Memo/Description"
      },
      {
        "ColType": "lettrage",
        "ColTitle": "Lettrage"
      },
      {
        "ColType": "debt_amt",
        "ColTitle": "Debit"
      },
      {
        "ColType": "credit_amt",
        "ColTitle": "Credit"
      },
      {
        "ColType": "subt_rbal_amount",
        "ColTitle": "Balance"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/GeneralLedgerFR?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `generalledgerqueryFR`

<details>
<summary>Show schema for `generalledgerqueryFR`</summary>

#### generalledgerqueryFR

Model type: `object`

##### `customer`

Required: Optional
Type: `String`
Default: Include data for all customers

Filters report contents to include information for specified customers.
Supported Values: One or more comma separated customer IDs as returned in the attribute, `Customer.Id`, of the Customer object response code.

##### `account`

Required: Optional
Type: `String`
Default: Data for all accounts

Filters report contents to include information for specified accounts.
Supported Values: One or more comma separated account IDs as returned in the attribute, `Account.Id`, of the Account object response code.

##### `accounting_method`

Required: Optional
Type: `String`
Default: Method defined in preferences by the <span class="literal">Preferences.ReportPrefs.ReportBasis</span> attribute

The accounting method used in the report. Supported Values:`Cash`, `Accrual`

##### `source_account`

Required: Optional
Type: `String`
Default: Data for all accounts

Filters report contents to include information for specified source accounts.
Supported Values: One or more comma separated account IDs as returned in the attribute, `Account.Id`, of the Account object response code.

##### `end_date`

Required: Optional
Type: `String`

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `account_type`

Required: Optional
Type: `String`
Default: All accounts

(source_account_type) Account type from which transactions are included in the report.
Supported Values: AccountsPayable, AccountsReceivable, Bank, CostOfGoodsSold, CreditCard, Equity, Expense, FixedAsset, Income, LongTermLiability, NonPosting, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome

<details>
<summary>Show child attributes</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **FOR ACCOUNT TYPE** | **SPECIFY THESE VALUES** |
| All Balance Sheet accounts | Bank, AccountsReceivable, OtherCurrentAsset, FixedAsset, OtherAsset, AccountsPayable, CreditCard, OtherCurrentLiability, LongTermLiability, Equity |
| All Asset Accounts | Bank, AccountsReceivable, OtherCurrentAsset, FixedAsset, OtherAsset |
| All Current Asset Accounts | Bank, AccountsReceivable, OtherCurrentAsset |
| All Bank Accounts | Bank |
| All Accounts receivable (A/R) Accounts | AccountsReceivable |
| All Other Current Assets Accounts | OtherCurrentAsset |
| All Fixed Assets Accounts | FixedAsset |
| All Other Assets Accounts | OtherAsset |
| All Liability Accounts | AccountsPayable, CreditCard, OtherCurrentLiability, LongTermLiability |
| All Current Liability Accounts | AccountsPayable, CreditCard, OtherCurrentLiability |
| All Accounts payable (A/P) Accounts | AccountsPayable |
| All Credit Card Accounts | CreditCard |
| All Other Current Liabilities Accounts | OtherCurrentLiability |
| All Long Term Liabilities Accounts | LongTermLiability |
| xls | application/vnd/ms-excel |
| All Equity Accounts | Equity |
| All Income/Expense Accounts | Income, CostOfGoodsSold, Expense, OtherIncome, OtherExpense |
| All Income Accounts | Income |
| All Cost of Goods Sold Accounts | CostOfGoodsSold |
| All Expenses Accounts | Expense |
| All Other Income Accounts | OtherIncome |

</details>

##### `sort_by`

Required: Optional
Type: `String`
Default: <span class="literal">txn_type</span>

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order.
Supported Values: `ascend`, `descend`

##### `start_date`

Required: Optional
Type: `String`

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `summarize_column_by`

Required: Optional
Type: `String`
Default: Total*

The criteria by which to group the report results.
Supported Values: Total, Month, Week, Days, Quarter, Year, Customers, Vendors, Classes, Departments, Employees, ProductsAndServices

##### `department`

Required: Optional
Type: `String`
Default: Include data for all departments

Filters report contents to include information for specified departments if so configured in the company file.
Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

##### `vendor`

Required: Optional
Type: `String`
Default: To return data for all vendors

Filters report contents to include information for specified vendors.
Supported Values: One or more comma separated vendor IDs as returned in the attribute, `Vendor.Id`, of the Vendor object response code.

##### `class`

Required: Optional
Type: `String`
Default: Include data for all classes

Filters report contents to include information for specified classes if so configured in the company file.
Supported Values: One or more comma separated class IDs as returned in the attribute, `Class.Id`, of the Class entity response code.

</details>

### Sample Query

This query returns the general ledger report for bank accounts between Jan 1, 2021 and October 18 2021.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/GeneralLedgerFR?start_date=2021-01-01&end_date=2015-10-18&source_account_type=Bank\r\n"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "GeneralLedgerFR",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "StartPeriod": "2021-10-19",
    "Currency": "EUR",
    "EndPeriod": "2021-10-19",
    "Time": "2021-10-19T09:31:18-07:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "82",
              "value": "44566100 TVA d\u00e9ductible"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
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
                  "value": "2021-10-19"
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for 44566100 TVA d\u00e9ductible"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": "200.00"
            },
            {
              "value": ""
            },
            {
              "value": "200.00"
            }
          ]
        }
      },
      {
        "Header": {
          "ColData": [
            {
              "id": "65",
              "value": "51210100 Comptes en monnaie nationale"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
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
                  "value": "2021-10-19"
                },
                {
                  "value": "BQ"
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for 51210100 Comptes en monnaie nationale"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "Header": {
          "ColData": [
            {
              "id": "19",
              "value": "60710000 Achats de Marchandises (ou groupe) A"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
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
                  "value": "2021-10-19"
                },
                {
                  "value": "BQ"
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                },
                {
                  "value": ""
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for 60710000 Achats de Marchandises (ou groupe) A"
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            },
            {
              "value": ""
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "tx_date",
        "ColTitle": "Date"
      },
      {
        "ColType": "journal_code_name",
        "ColTitle": "Journal Code"
      },
      {
        "ColType": "doc_num",
        "ColTitle": "No."
      },
      {
        "ColType": "memo",
        "ColTitle": "Memo/Description"
      },
      {
        "ColType": "lettrage",
        "ColTitle": "Lettrage"
      },
      {
        "ColType": "debt_amt",
        "ColTitle": "Debit"
      },
      {
        "ColType": "credit_amt",
        "ColTitle": "Credit"
      },
      {
        "ColType": "subt_rbal_amount",
        "ColTitle": "Balance"
      }
    ]
  }
}
```
