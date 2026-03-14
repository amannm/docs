# TaxCode

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxcode
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TaxCode
> Canonical entity: `TaxCode`

A TaxCode object is used to track the taxable or non-taxable status of products, services, and customers. You can assign a sales tax code to each of your products, services, and customers based on their taxable or non-taxable status. You can then use these codes to generate reports that provide information to the tax agencies about the taxable or non-taxable status of certain sales. See [Global tax model](https://developer.intuit.com/app/developer/qbo/docs/workflows/calculate-sales-tax/automated-sales-tax-for-non-us-locales) for more information about using TaxCode objects and the tax model in general.

### Create a taxcode

Use the `taxservice` resource to create a tax code.

## The taxcode object

### taxcoderesponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Name`

Required: Required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

User recognizable name for the tax sales code.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `PurchaseTaxRateList`

Required: Conditionally required
Type: `TaxRateList`

List of references to tax rates that apply for purchase transactions when this tax code represents a group of tax rates. Required when `TaxGroup` is set to `true`

<details>
<summary>Child attributes for `PurchaseTaxRateList`</summary>

##### taxratelist

Model type: `object`

###### `TaxRateDetail [0..n]`

Required: Optional

TaxRateDetail that specifies qualified detail of TaxRate.

<details>
<summary>Child attributes for `TaxRateDetail [0..n]`</summary>

###### taxratedetail

Model type: `object`

###### `TaxRateRef`

Required: Required

Reference to the tax rate.

<details>
<summary>Child attributes for `TaxRateRef`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

###### `TaxTypeApplicable`

Required: Optional
Type: `String`

Applicable TaxType enum. Valid values: TaxOnAmount, TaxOnAmountPlusTax, TaxOnTax

###### `TaxOrder`

Required: Optional
Type: `Integer`

Applicable Tax Order.

</details>

</details>

#### `SalesTaxRateList`

Required: Conditionally required
Type: `TaxRateList`

List of references to tax rates that apply for sales transactions when this tax code represents a group of tax rates. Required when `TaxGroup` is set to `true`

<details>
<summary>Child attributes for `SalesTaxRateList`</summary>

##### taxratelist

Model type: `object`

###### `TaxRateDetail [0..n]`

Required: Optional

TaxRateDetail that specifies qualified detail of TaxRate.

<details>
<summary>Child attributes for `TaxRateDetail [0..n]`</summary>

###### taxratedetail

Model type: `object`

###### `TaxRateRef`

Required: Required

Reference to the tax rate.

<details>
<summary>Child attributes for `TaxRateRef`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

###### `TaxTypeApplicable`

Required: Optional
Type: `String`

Applicable TaxType enum. Valid values: TaxOnAmount, TaxOnAmountPlusTax, TaxOnTax

###### `TaxOrder`

Required: Optional
Type: `Integer`

Applicable Tax Order.

</details>

</details>

#### `TaxCodeConfigType`

Type: `String`
Traits: read only
Minor version: 51

Flag to identify whether the TaxCode is system defined by Automated Sales Tax engine or user generated. Valid values include `USER_DEFINED`, `SYSTEM_GENERATED`SYSTEM_GENERATED.

#### `TaxGroup`

Required: Optional
Type: `Boolean`
Traits: read only
Default: true

`true`—-this object represents a group of one or more tax rates. `false`—-this object represents pseudo-tax codes TAX and NON.

#### `Taxable`

Required: Optional
Type: `Boolean`
Traits: read only

False or null means meaning non-taxable. True means taxable. Always true, except for the pseudo taxcode NON.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: true

False if inactive. Inactive sales tax codes may be hidden from display and may not be used on financial transactions.

#### `Description`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

User entered description for the sales tax code.

#### `Hidden`

Required: Optional
Type: `Boolean`
Traits: read only
Minor version: 21

Read-only. Denotes whether active tax codes are displayed on transactions. `true`—-This tax code is hidden on transactions. `false`—-This tax code is displayed on transactions.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the object. The MetaData values are set by Data Services and are read only for all applications.

<details>
<summary>Child attributes for `MetaData`</summary>

##### modificationmetadata

Model type: `object`

###### `CreateTime`

Type: `DateTime`
Traits: read only, system defined, filterable, sortable

Time the entity was created in the source domain.

<details>
<summary>Child attributes for `CreateTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `LastUpdatedTime`

Type: `DateTime`
Traits: read only, system defined, filterable, sortable

Time the entity was last updated in the source domain.

<details>
<summary>Child attributes for `LastUpdatedTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

</details>

#### Example

```json
{
  "TaxCode": {
    "SyncToken": "0",
    "domain": "QBO",
    "TaxGroup": true,
    "Name": "California",
    "Taxable": true,
    "PurchaseTaxRateList": {
      "TaxRateDetail": []
    },
    "sparse": false,
    "Active": true,
    "Description": "California",
    "MetaData": {
      "CreateTime": "2014-09-18T12:17:04-07:00",
      "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
    },
    "Id": "2",
    "SalesTaxRateList": {
      "TaxRateDetail": [
        {
          "TaxTypeApplicable": "TaxOnAmount",
          "TaxRateRef": {
            "name": "California",
            "value": "3"
          },
          "TaxOrder": 0
        }
      ]
    }
  },
  "time": "2015-07-27T12:37:22.733-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T12:36:59.832-07:00">
  <TaxCode domain="QBO" sparse="false">
    <Id>2</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
      <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
    </MetaData>
    <Name>California</Name>
    <Description>California</Description>
    <Active>true</Active>
    <Taxable>true</Taxable>
    <TaxGroup>true</TaxGroup>
    <SalesTaxRateList>
      <TaxRateDetail>
        <TaxRateRef name="California">3</TaxRateRef>
        <TaxTypeApplicable>TaxOnAmount</TaxTypeApplicable>
        <TaxOrder>0</TaxOrder>
      </TaxRateDetail>
    </SalesTaxRateList>
    <PurchaseTaxRateList />
  </TaxCode>
</IntuitResponse>
```

## Query a taxcode

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * From TaxCode"
```

#### XML example

```sql
select * from TaxCode
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 5,
    "TaxCode": [
      {
        "TaxGroup": false,
        "Name": "TAX",
        "Taxable": true,
        "Description": "TAX",
        "Id": "TAX",
        "MetaData": {
          "CreateTime": "2014-10-15T11:28:33-07:00",
          "LastUpdatedTime": "2014-10-15T11:28:33-07:00"
        }
      },
      {
        "TaxGroup": false,
        "Name": "NON",
        "Taxable": false,
        "Description": "NON",
        "Id": "NON",
        "MetaData": {
          "CreateTime": "2014-10-15T11:28:33-07:00",
          "LastUpdatedTime": "2014-10-15T11:28:33-07:00"
        }
      },
      {
        "TaxGroup": true,
        "Name": "CustomSalesTax",
        "Taxable": true,
        "Description": "CustomSalesTax",
        "Id": "CustomSalesTax",
        "MetaData": {
          "CreateTime": "2014-10-15T11:28:33-07:00",
          "LastUpdatedTime": "2014-10-15T11:28:33-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "TaxGroup": true,
        "Name": "California",
        "Taxable": true,
        "PurchaseTaxRateList": {
          "TaxRateDetail": []
        },
        "sparse": false,
        "Active": true,
        "Description": "California",
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        },
        "Id": "2",
        "SalesTaxRateList": {
          "TaxRateDetail": [
            {
              "TaxTypeApplicable": "TaxOnAmount",
              "TaxRateRef": {
                "name": "California",
                "value": "3"
              },
              "TaxOrder": 0
            }
          ]
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "TaxGroup": true,
        "Name": "Tucson",
        "Taxable": true,
        "PurchaseTaxRateList": {
          "TaxRateDetail": []
        },
        "sparse": false,
        "Active": true,
        "Description": "Tucson",
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        },
        "Id": "3",
        "SalesTaxRateList": {
          "TaxRateDetail": [
            {
              "TaxTypeApplicable": "TaxOnAmount",
              "TaxRateRef": {
                "name": "AZ State tax",
                "value": "1"
              },
              "TaxOrder": 0
            },
            {
              "TaxTypeApplicable": "TaxOnAmount",
              "TaxRateRef": {
                "name": "Tucson City",
                "value": "2"
              },
              "TaxOrder": 0
            }
          ]
        }
      }
    ],
    "maxResults": 5
  },
  "time": "2015-07-27T11:44:00.125-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T11:43:27.268-07:00">
    <QueryResponse startPosition="1" maxResults="5" totalCount="5">
        <TaxCode>
            <Id>TAX</Id>
            <MetaData>
                <CreateTime>2014-10-15T11:28:33-07:00</CreateTime>
                <LastUpdatedTime>2014-10-15T11:28:33-07:00</LastUpdatedTime>
            </MetaData>
            <Name>TAX</Name>
            <Description>TAX</Description>
            <Taxable>true</Taxable>
            <TaxGroup>false</TaxGroup>
        </TaxCode>
        <TaxCode>
            <Id>NON</Id>
            <MetaData>
                <CreateTime>2014-10-15T11:28:33-07:00</CreateTime>
                <LastUpdatedTime>2014-10-15T11:28:33-07:00</LastUpdatedTime>
            </MetaData>
            <Name>NON</Name>
            <Description>NON</Description>
            <Taxable>false</Taxable>
            <TaxGroup>false</TaxGroup>
        </TaxCode>
        <TaxCode>
            <Id>CustomSalesTax</Id>
            <MetaData>
                <CreateTime>2014-10-15T11:28:33-07:00</CreateTime>
                <LastUpdatedTime>2014-10-15T11:28:33-07:00</LastUpdatedTime>
            </MetaData>
            <Name>CustomSalesTax</Name>
            <Description>CustomSalesTax</Description>
            <Taxable>true</Taxable>
            <TaxGroup>true</TaxGroup>
        </TaxCode>
        <TaxCode domain="QBO" sparse="false">
            <Id>2</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
            </MetaData>
            <Name>California</Name>
            <Description>California</Description>
            <Active>true</Active>
            <Taxable>true</Taxable>
            <TaxGroup>true</TaxGroup>
            <SalesTaxRateList>
                <TaxRateDetail>
                    <TaxRateRef name="California">3</TaxRateRef>
                    <TaxTypeApplicable>TaxOnAmount</TaxTypeApplicable>
                    <TaxOrder>0</TaxOrder>
                </TaxRateDetail>
            </SalesTaxRateList>
            <PurchaseTaxRateList />
        </TaxCode>
        <TaxCode domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Tucson</Name>
            <Description>Tucson</Description>
            <Active>true</Active>
            <Taxable>true</Taxable>
            <TaxGroup>true</TaxGroup>
            <SalesTaxRateList>
                <TaxRateDetail>
                    <TaxRateRef name="AZ State tax">1</TaxRateRef>
                    <TaxTypeApplicable>TaxOnAmount</TaxTypeApplicable>
                    <TaxOrder>0</TaxOrder>
                </TaxRateDetail>
                <TaxRateDetail>
                    <TaxRateRef name="Tucson City">2</TaxRateRef>
                    <TaxTypeApplicable>TaxOnAmount</TaxTypeApplicable>
                    <TaxOrder>0</TaxOrder>
                </TaxRateDetail>
            </SalesTaxRateList>
            <PurchaseTaxRateList />
        </TaxCode>
    </QueryResponse>
</IntuitResponse>
```

## Read a taxcode

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxcode/<taxcodeId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TaxCode object that has been previously created.

### Returns

Returns the TaxCode object.

#### Example

```json
{
  "TaxCode": {
    "SyncToken": "0",
    "domain": "QBO",
    "TaxGroup": true,
    "Name": "California",
    "Taxable": true,
    "PurchaseTaxRateList": {
      "TaxRateDetail": []
    },
    "sparse": false,
    "Active": true,
    "Description": "California",
    "MetaData": {
      "CreateTime": "2014-09-18T12:17:04-07:00",
      "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
    },
    "Id": "2",
    "SalesTaxRateList": {
      "TaxRateDetail": [
        {
          "TaxTypeApplicable": "TaxOnAmount",
          "TaxRateRef": {
            "name": "California",
            "value": "3"
          },
          "TaxOrder": 0
        }
      ]
    }
  },
  "time": "2015-07-27T12:37:22.733-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T12:36:59.832-07:00">
  <TaxCode domain="QBO" sparse="false">
    <Id>2</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
      <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
    </MetaData>
    <Name>California</Name>
    <Description>California</Description>
    <Active>true</Active>
    <Taxable>true</Taxable>
    <TaxGroup>true</TaxGroup>
    <SalesTaxRateList>
      <TaxRateDetail>
        <TaxRateRef name="California">3</TaxRateRef>
        <TaxTypeApplicable>TaxOnAmount</TaxTypeApplicable>
        <TaxOrder>0</TaxOrder>
      </TaxRateDetail>
    </SalesTaxRateList>
    <PurchaseTaxRateList />
  </TaxCode>
</IntuitResponse>
```
