# BalanceSheet

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/balancesheet
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / BalanceSheet
> Canonical entity: `BalanceSheet`

The information below provides a reference on how to query the Balance Sheet report from the QuickBooks Online Report Service.

## The balance sheet report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### balancesheetreporttoplevel

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

Top level container holding information for Profit and Loss report rows.

<details>
<summary>Child attributes for `Rows`</summary>

##### profitandlossreportrows

Model type: `object`

###### `Row [0..n]`

Represents a row in a report. A group of rows is enclosed in a `Rows` container. Rows may be nested either as a single row or in sets, based on the accounts represented in the report and query parameters specified in the request. Parameters:

`type`—As an enclosing section of sub-rows, this is always the string, `Section`. As a leaf row, this is always the string, `Data`.

`group`—The group name, valid when `type=Section`.

<details>
<summary>Show possible values for group</summary>

#### Values based on locales

| Name | Description |
| --- | --- |
| US | `Income` `COGS` `GrossProfit` `Expenses` `NetOperatingIncome` `OtherExpenses` `NetOtherIncome` `NetIncome` |
| CA | `Income` `COGS` `Expenses` `OtherIncome` `OtherExpenses` `NetIncome` |
| GB | `Income` `COGS` `GrossProfit` `Expenses` `NetOperatingIncome` `OtherIncome` `OtherExpenses` `NetOtherIncome` `NetIncome` |
| IN | `Income` `COGS` `GrossProfit` `OtherIncome` `Expenses` `OtherExpenses` `NetIncome` |
| FR | `DepreciationAndProvisions` `OperatingExpenses` `QuotasResultInJointOperations` `FinancialCharges` `ExceptionalCharges` `EmployeeParticipationResults` `IncomeTaxExpenses` `TotalExpenses` `ProfitOrLoss` `Including` `Revenue` `Export` `JointOperations` `FinancialProducts` `ExceptionalItems` `TotalIncome` |
| AU | `Income` `COGS` `GrossProfit` `OtherIncome` `Expenses` `OtherExpenses` `NetIncome` |

</details>

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
    "ReportName": "BalanceSheet",
    "Option": [
      {
        "Name": "AccountingStandard",
        "Value": "GAAP"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this calendar year-to-date",
    "ReportBasis": "Accrual",
    "StartPeriod": "2016-01-01",
    "Currency": "USD",
    "EndPeriod": "2016-10-31",
    "Time": "2016-10-31T09:42:21-07:00",
    "SummarizeColumnsBy": "Total"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "value": "ASSETS"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Current Assets"
                  },
                  {
                    "value": ""
                  }
                ]
              },
              "Rows": {
                "Row": [
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Bank Accounts"
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
                              "id": "35",
                              "value": "Checking"
                            },
                            {
                              "value": "1350.55"
                            }
                          ],
                          "type": "Data"
                        },
                        {
                          "ColData": [
                            {
                              "id": "36",
                              "value": "Savings"
                            },
                            {
                              "value": "800.00"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "BankAccounts",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Bank Accounts"
                        },
                        {
                          "value": "2150.55"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Accounts Receivable"
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
                              "id": "84",
                              "value": "Accounts Receivable (A/R)"
                            },
                            {
                              "value": "6383.12"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "AR",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Accounts Receivable"
                        },
                        {
                          "value": "6383.12"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Other current assets"
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
                              "id": "81",
                              "value": "Inventory Asset"
                            },
                            {
                              "value": "596.25"
                            }
                          ],
                          "type": "Data"
                        },
                        {
                          "ColData": [
                            {
                              "id": "4",
                              "value": "Undeposited Funds"
                            },
                            {
                              "value": "2117.52"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "OtherCurrentAssets",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Other current assets"
                        },
                        {
                          "value": "2713.77"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "group": "CurrentAssets",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Current Assets"
                  },
                  {
                    "value": "11247.44"
                  }
                ]
              }
            },
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Fixed Assets"
                  },
                  {
                    "value": ""
                  }
                ]
              },
              "Rows": {
                "Row": [
                  {
                    "Header": {
                      "ColData": [
                        {
                          "id": "37",
                          "value": "Truck"
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
                              "id": "38",
                              "value": "Original Cost"
                            },
                            {
                              "value": "13495.00"
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
                          "value": "Total Truck"
                        },
                        {
                          "value": "13495.00"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "group": "FixedAssets",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Fixed Assets"
                  },
                  {
                    "value": "13495.00"
                  }
                ]
              }
            }
          ]
        },
        "type": "Section",
        "group": "TotalAssets",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL ASSETS"
            },
            {
              "value": "24742.44"
            }
          ]
        }
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "LIABILITIES AND EQUITY"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Liabilities"
                  },
                  {
                    "value": ""
                  }
                ]
              },
              "Rows": {
                "Row": [
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Current Liabilities"
                        },
                        {
                          "value": ""
                        }
                      ]
                    },
                    "Rows": {
                      "Row": [
                        {
                          "Header": {
                            "ColData": [
                              {
                                "value": "Accounts Payable"
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
                                    "id": "33",
                                    "value": "Accounts Payable (A/P)"
                                  },
                                  {
                                    "value": "1984.17"
                                  }
                                ],
                                "type": "Data"
                              }
                            ]
                          },
                          "type": "Section",
                          "group": "AP",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total Accounts Payable"
                              },
                              {
                                "value": "1984.17"
                              }
                            ]
                          }
                        },
                        {
                          "Header": {
                            "ColData": [
                              {
                                "value": "Credit Cards"
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
                                    "id": "41",
                                    "value": "Mastercard"
                                  },
                                  {
                                    "value": "157.72"
                                  }
                                ],
                                "type": "Data"
                              }
                            ]
                          },
                          "type": "Section",
                          "group": "CreditCards",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total Credit Cards"
                              },
                              {
                                "value": "157.72"
                              }
                            ]
                          }
                        },
                        {
                          "Header": {
                            "ColData": [
                              {
                                "value": "Other Current Liabilities"
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
                                    "id": "89",
                                    "value": "Arizona Dept. of Revenue Payable"
                                  },
                                  {
                                    "value": "4.55"
                                  }
                                ],
                                "type": "Data"
                              },
                              {
                                "ColData": [
                                  {
                                    "id": "90",
                                    "value": "Board of Equalization Payable"
                                  },
                                  {
                                    "value": "401.98"
                                  }
                                ],
                                "type": "Data"
                              },
                              {
                                "ColData": [
                                  {
                                    "id": "43",
                                    "value": "Loan Payable"
                                  },
                                  {
                                    "value": "4000.00"
                                  }
                                ],
                                "type": "Data"
                              }
                            ]
                          },
                          "type": "Section",
                          "group": "OtherCurrentLiabilities",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total Other Current Liabilities"
                              },
                              {
                                "value": "4406.53"
                              }
                            ]
                          }
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "CurrentLiabilities",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Current Liabilities"
                        },
                        {
                          "value": "6548.42"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Long-Term Liabilities"
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
                              "id": "44",
                              "value": "Notes Payable"
                            },
                            {
                              "value": "25000.00"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "LongTermLiabilities",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Long-Term Liabilities"
                        },
                        {
                          "value": "25000.00"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "group": "Liabilities",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Liabilities"
                  },
                  {
                    "value": "31548.42"
                  }
                ]
              }
            },
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Equity"
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
                        "id": "34",
                        "value": "Opening Balance Equity"
                      },
                      {
                        "value": "-9337.50"
                      }
                    ],
                    "type": "Data"
                  },
                  {
                    "ColData": [
                      {
                        "id": "2",
                        "value": "Retained Earnings"
                      },
                      {
                        "value": "91.25"
                      }
                    ],
                    "type": "Data"
                  },
                  {
                    "ColData": [
                      {
                        "value": "Net Income"
                      },
                      {
                        "value": "2440.27"
                      }
                    ],
                    "type": "Data",
                    "group": "NetIncome"
                  }
                ]
              },
              "type": "Section",
              "group": "Equity",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Equity"
                  },
                  {
                    "value": "-6805.98"
                  }
                ]
              }
            }
          ]
        },
        "type": "Section",
        "group": "TotalLiabilitiesAndEquity",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL LIABILITIES AND EQUITY"
            },
            {
              "value": "24742.44"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "Account",
        "ColTitle": "",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "account"
          }
        ]
      },
      {
        "ColType": "Money",
        "ColTitle": "Total",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "total"
          }
        ]
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/BalanceSheet?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `balancesheetquery`

<details>
<summary>Show schema for `balancesheetquery`</summary>

#### balancesheetquery

Model type: `object`

##### `customer`

Required: Optional
Type: `String`
Default: to include data for all customers

Filters report contents to include information for specified customers. Supported Values: One or more comma separated customer IDs as returned in the attribute, `Customer.Id`, of the Customer object response code.

##### `qzurl`

Required: Optional
Type: `String`
Default: false

Specifies whether Quick Zoom URL information should be generated for rows in the report. Quick Zoom URL is a hyperlink to another report containing further details about the particular column of data. Supported Values: `true`, `false`

##### `accounting_method`

Required: Optional
Type: `String`
Default: Preferences.ReportPrefs.ReportBasis

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

##### `adjusted_gain_loss`

Required: Optional
Type: `String`
Default: false
Locales: CA

Specifies whether unrealized gain and losses are included in the report. Supported Values: `true`, `false`

##### `class`

Required: Optional
Type: `String`
Default: to include data for all classes

Filters report contents to include information for specified classes if so configured in the company file. Supported Values: One or more comma separated class IDs as returned in the attribute, `Class.Id`, of the Class entity response code.

##### `item`

Required: Optional
Type: `String`
Default: to include data for all items

Filters report contents to include information for specified items. Supported Values: One or more comma separated item IDs as returned in the attribute, `Item.Id`,of the Item entity response code.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order. Supported Values: `ascend`, `descend`

##### `summarize_column_by`

Required: Optional
Type: `String`
Default: Total*

The criteria by which to group the report results. Supported Values: Total, Month, Week, Days, Quarter, Year, Customers, Vendors, Classes, Departments, Employees, ProductsAndServices

##### `department`

Required: Optional
Type: `String`
Default: to include data for all departments

Filters report contents to include information for specified departments if so configured in the company file. Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

##### `vendor`

Required: Optional
Type: `String`
Default: to return data for all vendors

Filters report contents to include information for specified vendors. Supported Values: One or more comma separated vendor IDs as returned in the attribute, `Vendor.Id`, of the Vendor object response code.

##### `start_date`

Required: Optional
Type: `String`

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

</details>

### Sample Query

This query returns the balance sheet for the last fiscal year.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/BalanceSheet?date_macro=Last Fiscal Year-to-date"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "BalanceSheet",
    "Option": [
      {
        "Name": "AccountingStandard",
        "Value": "GAAP"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this calendar year-to-date",
    "ReportBasis": "Accrual",
    "StartPeriod": "2016-01-01",
    "Currency": "USD",
    "EndPeriod": "2016-10-31",
    "Time": "2016-10-31T09:42:21-07:00",
    "SummarizeColumnsBy": "Total"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "value": "ASSETS"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Current Assets"
                  },
                  {
                    "value": ""
                  }
                ]
              },
              "Rows": {
                "Row": [
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Bank Accounts"
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
                              "id": "35",
                              "value": "Checking"
                            },
                            {
                              "value": "1350.55"
                            }
                          ],
                          "type": "Data"
                        },
                        {
                          "ColData": [
                            {
                              "id": "36",
                              "value": "Savings"
                            },
                            {
                              "value": "800.00"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "BankAccounts",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Bank Accounts"
                        },
                        {
                          "value": "2150.55"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Accounts Receivable"
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
                              "id": "84",
                              "value": "Accounts Receivable (A/R)"
                            },
                            {
                              "value": "6383.12"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "AR",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Accounts Receivable"
                        },
                        {
                          "value": "6383.12"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Other current assets"
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
                              "id": "81",
                              "value": "Inventory Asset"
                            },
                            {
                              "value": "596.25"
                            }
                          ],
                          "type": "Data"
                        },
                        {
                          "ColData": [
                            {
                              "id": "4",
                              "value": "Undeposited Funds"
                            },
                            {
                              "value": "2117.52"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "OtherCurrentAssets",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Other current assets"
                        },
                        {
                          "value": "2713.77"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "group": "CurrentAssets",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Current Assets"
                  },
                  {
                    "value": "11247.44"
                  }
                ]
              }
            },
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Fixed Assets"
                  },
                  {
                    "value": ""
                  }
                ]
              },
              "Rows": {
                "Row": [
                  {
                    "Header": {
                      "ColData": [
                        {
                          "id": "37",
                          "value": "Truck"
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
                              "id": "38",
                              "value": "Original Cost"
                            },
                            {
                              "value": "13495.00"
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
                          "value": "Total Truck"
                        },
                        {
                          "value": "13495.00"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "group": "FixedAssets",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Fixed Assets"
                  },
                  {
                    "value": "13495.00"
                  }
                ]
              }
            }
          ]
        },
        "type": "Section",
        "group": "TotalAssets",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL ASSETS"
            },
            {
              "value": "24742.44"
            }
          ]
        }
      },
      {
        "Header": {
          "ColData": [
            {
              "value": "LIABILITIES AND EQUITY"
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Liabilities"
                  },
                  {
                    "value": ""
                  }
                ]
              },
              "Rows": {
                "Row": [
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Current Liabilities"
                        },
                        {
                          "value": ""
                        }
                      ]
                    },
                    "Rows": {
                      "Row": [
                        {
                          "Header": {
                            "ColData": [
                              {
                                "value": "Accounts Payable"
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
                                    "id": "33",
                                    "value": "Accounts Payable (A/P)"
                                  },
                                  {
                                    "value": "1984.17"
                                  }
                                ],
                                "type": "Data"
                              }
                            ]
                          },
                          "type": "Section",
                          "group": "AP",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total Accounts Payable"
                              },
                              {
                                "value": "1984.17"
                              }
                            ]
                          }
                        },
                        {
                          "Header": {
                            "ColData": [
                              {
                                "value": "Credit Cards"
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
                                    "id": "41",
                                    "value": "Mastercard"
                                  },
                                  {
                                    "value": "157.72"
                                  }
                                ],
                                "type": "Data"
                              }
                            ]
                          },
                          "type": "Section",
                          "group": "CreditCards",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total Credit Cards"
                              },
                              {
                                "value": "157.72"
                              }
                            ]
                          }
                        },
                        {
                          "Header": {
                            "ColData": [
                              {
                                "value": "Other Current Liabilities"
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
                                    "id": "89",
                                    "value": "Arizona Dept. of Revenue Payable"
                                  },
                                  {
                                    "value": "4.55"
                                  }
                                ],
                                "type": "Data"
                              },
                              {
                                "ColData": [
                                  {
                                    "id": "90",
                                    "value": "Board of Equalization Payable"
                                  },
                                  {
                                    "value": "401.98"
                                  }
                                ],
                                "type": "Data"
                              },
                              {
                                "ColData": [
                                  {
                                    "id": "43",
                                    "value": "Loan Payable"
                                  },
                                  {
                                    "value": "4000.00"
                                  }
                                ],
                                "type": "Data"
                              }
                            ]
                          },
                          "type": "Section",
                          "group": "OtherCurrentLiabilities",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total Other Current Liabilities"
                              },
                              {
                                "value": "4406.53"
                              }
                            ]
                          }
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "CurrentLiabilities",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Current Liabilities"
                        },
                        {
                          "value": "6548.42"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "value": "Long-Term Liabilities"
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
                              "id": "44",
                              "value": "Notes Payable"
                            },
                            {
                              "value": "25000.00"
                            }
                          ],
                          "type": "Data"
                        }
                      ]
                    },
                    "type": "Section",
                    "group": "LongTermLiabilities",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total Long-Term Liabilities"
                        },
                        {
                          "value": "25000.00"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "group": "Liabilities",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Liabilities"
                  },
                  {
                    "value": "31548.42"
                  }
                ]
              }
            },
            {
              "Header": {
                "ColData": [
                  {
                    "value": "Equity"
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
                        "id": "34",
                        "value": "Opening Balance Equity"
                      },
                      {
                        "value": "-9337.50"
                      }
                    ],
                    "type": "Data"
                  },
                  {
                    "ColData": [
                      {
                        "id": "2",
                        "value": "Retained Earnings"
                      },
                      {
                        "value": "91.25"
                      }
                    ],
                    "type": "Data"
                  },
                  {
                    "ColData": [
                      {
                        "value": "Net Income"
                      },
                      {
                        "value": "2440.27"
                      }
                    ],
                    "type": "Data",
                    "group": "NetIncome"
                  }
                ]
              },
              "type": "Section",
              "group": "Equity",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total Equity"
                  },
                  {
                    "value": "-6805.98"
                  }
                ]
              }
            }
          ]
        },
        "type": "Section",
        "group": "TotalLiabilitiesAndEquity",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL LIABILITIES AND EQUITY"
            },
            {
              "value": "24742.44"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "Account",
        "ColTitle": "",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "account"
          }
        ]
      },
      {
        "ColType": "Money",
        "ColTitle": "Total",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "total"
          }
        ]
      }
    ]
  }
}
```
