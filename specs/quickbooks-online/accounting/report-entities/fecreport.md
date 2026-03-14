# FECReport

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/fecreport
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / FECReport
> Canonical entity: `FECReport`

The information below provides a reference on how to access the **Fichier des Ecritures Comptables (FEC)** report from the QuickBooks Online Report Service. This report is available for FR locale only.

## The FEC report object

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
    "ReportName": "FECReport",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "ReportBasis": "Accrual",
    "StartPeriod": "2021-07-01",
    "Currency": "EUR",
    "EndPeriod": "2021-07-28",
    "Time": "2021-07-28T04:37:20-07:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "41100001"
          },
          {
            "value": "Clients"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1001"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - F1001"
          },
          {
            "value": "800.00"
          },
          {
            "value": ".00"
          },
          {
            "value": "AA"
          },
          {
            "value": "20210719"
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
            "value": "[{\"filename\":\"Invoice F1001.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-30.s3.amazonaws.com/9130355064301256/attachments/15e85a6e-bc14-4340-a8ed-36ca44d96384Invoice%20F1001.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=GdV0t2vNhRI7pMtjuoDkM3CiFaA%3D\",\"attachableId\":\"100100000000000001601\"},{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-1.s3.amazonaws.com/9130355064301256/attachments/8ec5b9e6-9ff0-41ea-b36d-bafb866eb488Credit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=lIsb3k7BSGG%2FgrTzgaGLocBDmLY%3D\",\"attachableId\":\"100100000000000001623\"},{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-15.s3.amazonaws.com/9130355064301256/attachments/c893ffc1-5c54-4501-854d-0b67a8b53a25Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=tUHcOoAjCcJ3ptI%2Feo9aZVfCS8c%3D\",\"attachableId\":\"100100000000000001624\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/7d3bdb3b-1c5c-46a9-9b9d-dff04a532b62Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=%2Fa7T1yjK3Vn8nIN3fhrAxm6BRHs%3D\",\"attachableId\":\"100100000000000001625\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "70710000"
          },
          {
            "value": "Ventes de Marchandises (ou groupe) A 0%"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1001"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - F1001 - Sale of Products"
          },
          {
            "value": ".00"
          },
          {
            "value": "800.00"
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
            "value": "[{\"filename\":\"Invoice F1001.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-30.s3.amazonaws.com/9130355064301256/attachments/15e85a6e-bc14-4340-a8ed-36ca44d96384Invoice%20F1001.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=GdV0t2vNhRI7pMtjuoDkM3CiFaA%3D\",\"attachableId\":\"100100000000000001601\"},{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-1.s3.amazonaws.com/9130355064301256/attachments/8ec5b9e6-9ff0-41ea-b36d-bafb866eb488Credit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=lIsb3k7BSGG%2FgrTzgaGLocBDmLY%3D\",\"attachableId\":\"100100000000000001623\"},{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-15.s3.amazonaws.com/9130355064301256/attachments/c893ffc1-5c54-4501-854d-0b67a8b53a25Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=tUHcOoAjCcJ3ptI%2Feo9aZVfCS8c%3D\",\"attachableId\":\"100100000000000001624\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/7d3bdb3b-1c5c-46a9-9b9d-dff04a532b62Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=%2Fa7T1yjK3Vn8nIN3fhrAxm6BRHs%3D\",\"attachableId\":\"100100000000000001625\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "Sale of Products"
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "41100001"
          },
          {
            "value": "Clients"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "A01"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - A01"
          },
          {
            "value": ".00"
          },
          {
            "value": "800.00"
          },
          {
            "value": "AA"
          },
          {
            "value": "20210719"
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
            "value": "[{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-20.s3.amazonaws.com/9130355064301256/attachments/060de78e-4c72-455d-8a72-33ac3dbe36ebCredit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=m%2Fde74p4khfgDDC%2F%2BfZIq%2BVHnuQ%3D\",\"attachableId\":\"100100000000000001627\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-23.s3.amazonaws.com/9130355064301256/attachments/f6b9744f-1497-473f-ac96-ad1622021915Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=uhqIKmnR9AFtzk737uscBGXVtb4%3D\",\"attachableId\":\"100100000000000001621\"}]"
          },
          {
            "value": ""
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "70710000"
          },
          {
            "value": "Ventes de Marchandises (ou groupe) A 0%"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "A01"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - A01 - Sale of Products"
          },
          {
            "value": "800.00"
          },
          {
            "value": ".00"
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
            "value": "[{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-20.s3.amazonaws.com/9130355064301256/attachments/060de78e-4c72-455d-8a72-33ac3dbe36ebCredit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=m%2Fde74p4khfgDDC%2F%2BfZIq%2BVHnuQ%3D\",\"attachableId\":\"100100000000000001627\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-23.s3.amazonaws.com/9130355064301256/attachments/f6b9744f-1497-473f-ac96-ad1622021915Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=uhqIKmnR9AFtzk737uscBGXVtb4%3D\",\"attachableId\":\"100100000000000001621\"}]"
          },
          {
            "value": ""
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "Sale of Products"
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "41100001"
          },
          {
            "value": "Clients"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1002"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - qwqwe - F1002"
          },
          {
            "value": "900.00"
          },
          {
            "value": ".00"
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
            "value": "[{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/5f1d37a4-6195-4134-9bf9-88823c7231b2Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=1Uo1JcpwSR6YP%2BKxWhKRsZtSVxA%3D\",\"attachableId\":\"100100000000000001641\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-19.s3.amazonaws.com/9130355064301256/attachments/ce144cb4-0f98-4327-895e-92f0db836d44Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=F0qyBGpWAwEkUwBKE6VWbkITWTE%3D\",\"attachableId\":\"100100000000000001622\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "70710000"
          },
          {
            "value": "Ventes de Marchandises (ou groupe) A 0%"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1002"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - F1002 - Sale of Products"
          },
          {
            "value": ".00"
          },
          {
            "value": "900.00"
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
            "value": "[{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/5f1d37a4-6195-4134-9bf9-88823c7231b2Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=1Uo1JcpwSR6YP%2BKxWhKRsZtSVxA%3D\",\"attachableId\":\"100100000000000001641\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-19.s3.amazonaws.com/9130355064301256/attachments/ce144cb4-0f98-4327-895e-92f0db836d44Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=F0qyBGpWAwEkUwBKE6VWbkITWTE%3D\",\"attachableId\":\"100100000000000001622\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "Sale of Products"
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "String",
        "ColTitle": "JournalCode",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "journal_code_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "JournalLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "journal_code_description"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureNum",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "txn_num"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureDate",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "create_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompteNum",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "acct_num_with_extn"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompteLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "account_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompAuxNum",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "aux_account"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompAuxLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "aux_account_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "PieceRef",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "doc_num"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "PieceDate",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "tx_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "memo"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Debit",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "debt_amt"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Credit",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "credit_amt"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureLet",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "lettrage"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "DateLet",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "paid_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "ValidDate",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "region_tx_validation_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Montantdevise",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "multicurrency_amount"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Idevise",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "multicurrency_symbol"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "AttachmentsInfo",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "attachments"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Due Date",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "due_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Journal Code type",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$journal_code_type"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Supplier",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$vend_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Total {0}",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$item_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Customer",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$cust_name"
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
- **Operation:** `GET /v3/company/<realmID>/reports/FECReport?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `fecreportquery`

<details>
<summary>Show schema for `fecreportquery`</summary>

#### fecreportquery

Model type: `object`

##### `attachmentType`

Required: Optional
Type: `String`
Default: The Attachment type

The parameter attachment type is a string value, and can accept one of the values : `TEMPORARY_LINKS` or `NONE` only.

##### `withQboIdentifier`

Required: Optional
Type: `Boolean`
Default: <span class="literal">withQboIdentifier</span>

The parameter `withQboIdentifier` is a boolean value, in the format `true` or `false`. This parameter can be used to add the columns transaction id and sequence in the response of the query

##### `start_date`

Required: Optional
Type: `String`
Default: <span class="literal">start_date</span>

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `end_date`

Required: Optional
Type: `String`
Default: <span class="literal">end_date</span>

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `add_due_date`

Required: Optional
Type: `Boolean`
Default: <span class="literal">add_due_date</span>

The parameter add_due_date is a boolean value, in the format `true`. `false`

</details>

### Sample Query

This query for Fichier des Ecritures Comptables(FEC) returns detailed information about all the data related to the bookkeeping and all the entries which are booked during a fiscal year.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/FECReport?start_date=2019-11-01&end_date=2021-11-06&attachmentType=TEMPORARY_LINKS&add_due_date=true"
```

### Returns

Returns the FEC report object.

#### Example

```json
{
  "Header": {
    "ReportName": "FECReport",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "ReportBasis": "Accrual",
    "StartPeriod": "2021-07-01",
    "Currency": "EUR",
    "EndPeriod": "2021-07-28",
    "Time": "2021-07-28T04:37:20-07:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "41100001"
          },
          {
            "value": "Clients"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1001"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - F1001"
          },
          {
            "value": "800.00"
          },
          {
            "value": ".00"
          },
          {
            "value": "AA"
          },
          {
            "value": "20210719"
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
            "value": "[{\"filename\":\"Invoice F1001.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-30.s3.amazonaws.com/9130355064301256/attachments/15e85a6e-bc14-4340-a8ed-36ca44d96384Invoice%20F1001.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=GdV0t2vNhRI7pMtjuoDkM3CiFaA%3D\",\"attachableId\":\"100100000000000001601\"},{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-1.s3.amazonaws.com/9130355064301256/attachments/8ec5b9e6-9ff0-41ea-b36d-bafb866eb488Credit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=lIsb3k7BSGG%2FgrTzgaGLocBDmLY%3D\",\"attachableId\":\"100100000000000001623\"},{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-15.s3.amazonaws.com/9130355064301256/attachments/c893ffc1-5c54-4501-854d-0b67a8b53a25Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=tUHcOoAjCcJ3ptI%2Feo9aZVfCS8c%3D\",\"attachableId\":\"100100000000000001624\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/7d3bdb3b-1c5c-46a9-9b9d-dff04a532b62Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=%2Fa7T1yjK3Vn8nIN3fhrAxm6BRHs%3D\",\"attachableId\":\"100100000000000001625\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "70710000"
          },
          {
            "value": "Ventes de Marchandises (ou groupe) A 0%"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1001"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - F1001 - Sale of Products"
          },
          {
            "value": ".00"
          },
          {
            "value": "800.00"
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
            "value": "[{\"filename\":\"Invoice F1001.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-30.s3.amazonaws.com/9130355064301256/attachments/15e85a6e-bc14-4340-a8ed-36ca44d96384Invoice%20F1001.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=GdV0t2vNhRI7pMtjuoDkM3CiFaA%3D\",\"attachableId\":\"100100000000000001601\"},{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-1.s3.amazonaws.com/9130355064301256/attachments/8ec5b9e6-9ff0-41ea-b36d-bafb866eb488Credit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=lIsb3k7BSGG%2FgrTzgaGLocBDmLY%3D\",\"attachableId\":\"100100000000000001623\"},{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-15.s3.amazonaws.com/9130355064301256/attachments/c893ffc1-5c54-4501-854d-0b67a8b53a25Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=tUHcOoAjCcJ3ptI%2Feo9aZVfCS8c%3D\",\"attachableId\":\"100100000000000001624\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/7d3bdb3b-1c5c-46a9-9b9d-dff04a532b62Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=%2Fa7T1yjK3Vn8nIN3fhrAxm6BRHs%3D\",\"attachableId\":\"100100000000000001625\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "Sale of Products"
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "41100001"
          },
          {
            "value": "Clients"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "A01"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - A01"
          },
          {
            "value": ".00"
          },
          {
            "value": "800.00"
          },
          {
            "value": "AA"
          },
          {
            "value": "20210719"
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
            "value": "[{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-20.s3.amazonaws.com/9130355064301256/attachments/060de78e-4c72-455d-8a72-33ac3dbe36ebCredit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=m%2Fde74p4khfgDDC%2F%2BfZIq%2BVHnuQ%3D\",\"attachableId\":\"100100000000000001627\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-23.s3.amazonaws.com/9130355064301256/attachments/f6b9744f-1497-473f-ac96-ad1622021915Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=uhqIKmnR9AFtzk737uscBGXVtb4%3D\",\"attachableId\":\"100100000000000001621\"}]"
          },
          {
            "value": ""
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "70710000"
          },
          {
            "value": "Ventes de Marchandises (ou groupe) A 0%"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "A01"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - A01 - Sale of Products"
          },
          {
            "value": "800.00"
          },
          {
            "value": ".00"
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
            "value": "[{\"filename\":\"Credit Note A01.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-20.s3.amazonaws.com/9130355064301256/attachments/060de78e-4c72-455d-8a72-33ac3dbe36ebCredit%20Note%20A01.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=m%2Fde74p4khfgDDC%2F%2BfZIq%2BVHnuQ%3D\",\"attachableId\":\"100100000000000001627\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-23.s3.amazonaws.com/9130355064301256/attachments/f6b9744f-1497-473f-ac96-ad1622021915Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=uhqIKmnR9AFtzk737uscBGXVtb4%3D\",\"attachableId\":\"100100000000000001621\"}]"
          },
          {
            "value": ""
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "Sale of Products"
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "41100001"
          },
          {
            "value": "Clients"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1002"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - qwqwe - F1002"
          },
          {
            "value": "900.00"
          },
          {
            "value": ".00"
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
            "value": "[{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/5f1d37a4-6195-4134-9bf9-88823c7231b2Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=1Uo1JcpwSR6YP%2BKxWhKRsZtSVxA%3D\",\"attachableId\":\"100100000000000001641\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-19.s3.amazonaws.com/9130355064301256/attachments/ce144cb4-0f98-4327-895e-92f0db836d44Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=F0qyBGpWAwEkUwBKE6VWbkITWTE%3D\",\"attachableId\":\"100100000000000001622\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "VT"
          },
          {
            "value": "Sales"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "20210719"
          },
          {
            "value": "70710000"
          },
          {
            "value": "Ventes de Marchandises (ou groupe) A 0%"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "F1002"
          },
          {
            "value": "20210719"
          },
          {
            "value": "Customer - F1002 - Sale of Products"
          },
          {
            "value": ".00"
          },
          {
            "value": "900.00"
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
            "value": "[{\"filename\":\"Invoice F1002.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-22.s3.amazonaws.com/9130355064301256/attachments/5f1d37a4-6195-4134-9bf9-88823c7231b2Invoice%20F1002.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=1Uo1JcpwSR6YP%2BKxWhKRsZtSVxA%3D\",\"attachableId\":\"100100000000000001641\"},{\"filename\":\"Invoice F1001 voided.pdf\",\"tempURI\":\"https://intuit-qbo-preprod-19.s3.amazonaws.com/9130355064301256/attachments/ce144cb4-0f98-4327-895e-92f0db836d44Invoice%20F1001%20voided.pdf?AWSAccessKeyId=AKIAZYPU4D4LSQ626GRN&Expires=1627473140&Signature=F0qyBGpWAwEkUwBKE6VWbkITWTE%3D\",\"attachableId\":\"100100000000000001622\"}]"
          },
          {
            "value": "20210818"
          },
          {
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "Sale of Products"
          },
          {
            "value": "Customer"
          }
        ],
        "type": "Data"
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "String",
        "ColTitle": "JournalCode",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "journal_code_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "JournalLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "journal_code_description"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureNum",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "txn_num"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureDate",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "create_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompteNum",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "acct_num_with_extn"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompteLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "account_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompAuxNum",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "aux_account"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "CompAuxLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "aux_account_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "PieceRef",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "doc_num"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "PieceDate",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "tx_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureLib",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "memo"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Debit",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "debt_amt"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Credit",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "credit_amt"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "EcritureLet",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "lettrage"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "DateLet",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "paid_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "ValidDate",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "region_tx_validation_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Montantdevise",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "multicurrency_amount"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Idevise",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "multicurrency_symbol"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "AttachmentsInfo",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "attachments"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Due Date",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "due_date"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Journal Code type",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$journal_code_type"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Supplier",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$vend_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Total {0}",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$item_name"
          }
        ]
      },
      {
        "ColType": "String",
        "ColTitle": "Customer",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "$TECHNICAL$cust_name"
          }
        ]
      }
    ]
  }
}
```
