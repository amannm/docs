# InventoryAdjustment

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/inventoryadjustment
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / InventoryAdjustment
> Canonical entity: `InventoryAdjustment`

InventoryAdjustment provides a way for customers to change the quantity of inventory items for various reasons, such as damage, stock write-off, shrinkage, or expiration. The change in quantity automatically handles the underlying accounting and valuation. Customers can view and verify the inventory quantity and valuation using the Inventory Valuation Report in QuickBooks Online. This functionality is available for QuickBooks Online Plus and advanced SKUs in the US. To access this entity, invoke the endpoints with a `minorversion=70` or higher query parameter.

## The inventoryadjustment object

### inventoryadjustmentresponse

Model type: `object`

#### `TxnDate`

Required: Required
Type: `DateTime`

The date entered by the user when this transaction occurred.

yyyy/MM/dd is the valid date format.

For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.

Sort order is ASC by default.

<details>
<summary>Child attributes for `TxnDate`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of an inventory adjustment.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### itemadjustmentline

Model type: `object`

###### `Id`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

###### `ItemAdjustmentLineDetail`

Required: Required
Type: `Item Adjustment`

Details for the line in the inventory adjustment.

<details>
<summary>Child attributes for `ItemAdjustmentLineDetail`</summary>

###### itemadjustmentlinedetail

Model type: `object`

###### `QtyDiff`

Required: Required
Type: `Decimal`

Change in quantity. Set it to a positive number for incrementing and a negative number if for decrementing the quantity.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object. Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

<details>
<summary>Child attributes for `ItemRef`</summary>

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

</details>

###### `DetailType`

Required: Required for create
Type: `LineDetailTypeEnum`

Set to `ItemAdjustmentLineDetail`for this type of line.

</details>

#### `AdjustAccountRef`

Required: Required
Type: `ReferenceType`
Traits: read only, system defined

Specifies which account is debited. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AdjustAccountRef.value` and `AdjustAccountRef.name`, respectively.

<details>
<summary>Child attributes for `AdjustAccountRef`</summary>

##### referencetype

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

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object.

#### `DocNumber`

Required: Optional
Type: `String`
Max length: max 21 chars

Reference number for the transaction. If not explicitly provided at creation time, this field is auto populated by incrementing the last number by 1.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Statement Memo field on the Invoice form in the QuickBooks Online UI.

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
  "InventoryAdjustment": {
    "DocNumber": "27",
    "TxnDate": "2024-05-02",
    "PrivateNote": "",
    "SyncToken": "0",
    "domain": "QBO",
    "AdjustAccountRef": {
      "name": "Inventory Shrinkage",
      "value": "91"
    },
    "sparse": false,
    "Line": [
      {
        "ItemAdjustmentLineDetail": {
          "QtyDiff": -2,
          "ItemRef": {
            "value": "1010000001"
          }
        },
        "Id": "1"
      }
    ],
    "Id": "1455000081",
    "MetaData": {
      "LastUpdatedTime": "2024-05-07"
    }
  },
  "time": "2024-05-07T15:49:02.469-07:00"
}
```

## Create an inventory adjustment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/inventoryadjustment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Creates a new inventory adjustment

### Request Body

The minimum elements to create an inventoryadjustment object are listed here.

Schema: `inventoryadjustmentcreaterequest`

<details>
<summary>Show schema for `inventoryadjustmentcreaterequest`</summary>

#### inventoryadjustmentcreaterequest

Model type: `object`

##### `AdjustAccountRef`

Required: Required
Type: `ReferenceType`

Specifies which account is debited. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AdjustAccountRef.value` and `AdjustAccountRef.name`, respectively.

<details>
<summary>Child attributes for `AdjustAccountRef`</summary>

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

##### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of an inventory adjustment.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### itemadjustmentline

Model type: `object`

###### `Id`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

###### `ItemAdjustmentLineDetail`

Required: Required
Type: `Item Adjustment`

Details for the line in the inventory adjustment.

<details>
<summary>Child attributes for `ItemAdjustmentLineDetail`</summary>

###### itemadjustmentlinedetail

Model type: `object`

###### `QtyDiff`

Required: Required
Type: `Decimal`

Change in quantity. Set it to a positive number for incrementing and a negative number if for decrementing the quantity.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object. Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

<details>
<summary>Child attributes for `ItemRef`</summary>

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

</details>

###### `DetailType`

Required: Required for create
Type: `LineDetailTypeEnum`

Set to `ItemAdjustmentLineDetail`for this type of line.

</details>

##### `TxnDate`

Required: Required
Type: `DateTime`

The date entered by the user when this transaction occurred.

`yyyy/MM/dd` is the valid date format.

For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.

Sort order is ASC by default.

<details>
<summary>Child attributes for `TxnDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

##### `DocNumber`

Required: Optional
Type: `String`
Max length: max 21 chars

Reference number for the transaction. If not explicitly provided at creation time, this field is auto populated by incrementing the last number by 1.

##### `PrivateNote`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Statement Memo field on the Invoice form in the QuickBooks Online UI.

</details>

#### Example

```json
{
  "AdjustAccountRef": {
    "value": "91"
  },
  "PrivateNote": "Memo 1",
  "Line": [
    {
      "DetailType": "ItemAdjustmentLineDetail",
      "ItemAdjustmentLineDetail": {
        "QtyDiff": -2,
        "ItemRef": {
          "value": "1010000001"
        }
      }
    }
  ],
  "TxnDate": "2024-05-02"
}
```

### Returns

Returns the newly created inventoryadjustment object.

#### Example

```json
{
  "InventoryAdjustment": {
    "DocNumber": "27",
    "TxnDate": "2024-05-02",
    "PrivateNote": "",
    "SyncToken": "0",
    "domain": "QBO",
    "AdjustAccountRef": {
      "name": "Inventory Shrinkage",
      "value": "91"
    },
    "sparse": false,
    "Line": [
      {
        "ItemAdjustmentLineDetail": {
          "QtyDiff": -2,
          "ItemRef": {
            "value": "1010000001"
          }
        },
        "Id": "1"
      }
    ],
    "Id": "1455000081",
    "MetaData": {
      "LastUpdatedTime": "2024-05-07"
    }
  },
  "time": "2024-05-07T15:49:02.469-07:00"
}
```

## Delete an inventory adjustment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/inventoryadjustment?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Deletes the inventory adjustment object specified in the request body. Include a minimum of `InventoryAdjustment.Id` and `InventoryAdjustment.SyncToken` in the request body.

### Request Body

Schema: `inventoryadjustmentdeleterequest`

<details>
<summary>Show schema for `inventoryadjustmentdeleterequest`</summary>

#### inventoryadjustmentdeleterequest

Model type: `object`

##### `SyncToken`

Required: Required
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `id`

Required: Required
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object.

</details>

#### Example

```json
{
  "SyncToken": "0",
  "Id": "1455000086"
}
```

### Returns

Returns information for the deleted object.

#### Example

```json
{
  "InventoryAdjustment": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "1455000086"
  },
  "time": "2024-05-08T14:04:46.441-07:00"
}
```

## Read an inventory adjustment

### Definition

- **Operation:** `GET /v3/company/<realmID>/inventoryadjustment/<inventoryadjustmentId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of an inventoryadjustment object that has been previously created.

### Returns

Returns the inventoryadjustment object.

#### Example

```json
{
  "InventoryAdjustment": {
    "DocNumber": "3",
    "TxnDate": "2024-05-02",
    "PrivateNote": "",
    "SyncToken": "0",
    "domain": "QBO",
    "AdjustAccountRef": {
      "name": "Inventory Shrinkage",
      "value": "91"
    },
    "sparse": false,
    "Line": [
      {
        "ItemAdjustmentLineDetail": {
          "QtyDiff": -5,
          "ItemRef": {
            "value": "1010000001"
          }
        },
        "Id": "1"
      }
    ],
    "Id": "1455000036",
    "MetaData": {
      "LastUpdatedTime": "2024-05-03"
    }
  },
  "time": "2024-05-08T13:59:23.274-07:00"
}
```

## Update an inventory adjustment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/inventoryadjustment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation updates the inventoryadjustment object specified in the request body. Include a minimum of `InventoryAdjustment.Id` and `InventoryAdjustment.SyncToken` in the request body.

**Note:** The `sparse` attribute must be set to `true`.

### Request Body

Schema: `inventoryadjustmentrequest`

<details>
<summary>Show schema for `inventoryadjustmentrequest`</summary>

#### inventoryadjustmentrequest

Model type: `object`

##### `AdjustAccountRef`

Required: Required
Type: `ReferenceType`
Traits: read only, system defined

Specifies which account is debited. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AdjustAccountRef.value` and `AdjustAccountRef.name`, respectively.

<details>
<summary>Child attributes for `AdjustAccountRef`</summary>

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

##### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of an inventory adjustment.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### itemadjustmentline

Model type: `object`

###### `Id`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

###### `ItemAdjustmentLineDetail`

Required: Required
Type: `Item Adjustment`

Details for the line in the inventory adjustment.

<details>
<summary>Child attributes for `ItemAdjustmentLineDetail`</summary>

###### itemadjustmentlinedetail

Model type: `object`

###### `QtyDiff`

Required: Required
Type: `Decimal`

Change in quantity. Set it to a positive number for incrementing and a negative number if for decrementing the quantity.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object. Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

<details>
<summary>Child attributes for `ItemRef`</summary>

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

</details>

###### `DetailType`

Required: Required for create
Type: `LineDetailTypeEnum`

Set to `ItemAdjustmentLineDetail`for this type of line.

</details>

##### `TxnDate`

Required: Required
Type: `DateTime`

The date entered by the user when this transaction occurred.

`yyyy/MM/dd` is the valid date format.

For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.

Sort order is ASC by default.

<details>
<summary>Child attributes for `TxnDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

##### `DocNumber`

Required: Optional
Type: `String`
Max length: max 21 chars

Reference number for the transaction. If not explicitly provided at creation time, this field is auto populated by incrementing the last number by 1.

##### `PrivateNote`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Statement Memo field on the Invoice form in the QuickBooks Online UI.

</details>

#### Example

```json
{
  "SyncToken": "0",
  "PrivateNote": "Update 1",
  "TxnDate": "2024-06-17",
  "AdjustAccountRef": {
    "value": "91"
  },
  "sparse": true,
  "Line": [
    {
      "ItemAdjustmentLineDetail": {
        "QtyDiff": -3,
        "ItemRef": {
          "value": "1010000001"
        }
      },
      "Id": "1"
    }
  ],
  "Id": "1455000036"
}
```

### Returns

The inventoryadjustment response body.

#### Example

```json
{
  "InventoryAdjustment": {
    "DocNumber": "3",
    "TxnDate": "2024-06-17",
    "PrivateNote": "Update 1",
    "SyncToken": "1",
    "domain": "QBO",
    "AdjustAccountRef": {
      "name": "Inventory Shrinkage",
      "value": "91"
    },
    "sparse": false,
    "Line": [
      {
        "ItemAdjustmentLineDetail": {
          "QtyDiff": -3,
          "ItemRef": {
            "value": "1010000001"
          }
        },
        "Id": "1"
      }
    ],
    "Id": "1455000036",
    "MetaData": {
      "LastUpdatedTime": "2024-06-17"
    }
  },
  "time": "2024-06-17T14:25:11.880-07:00"
}
```
