# TaxPayment

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxpayment
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TaxPayment
> Canonical entity: `TaxPayment`

Tax Payment/Refund made against filed taxReturn. Applicable for AU, CA and UK locales only.

### Business Rules

## The taxpayment object

### taxpaymentresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `Refund`

Type: `Boolean`
Minor version: 47

Indicate if this transaction is a refund. Returns false for the payment.

#### `TxnDate`

Type: `Date`
Traits: read only
Default: current server date
Minor version: 47

Indicates the tax payment date

#### `PaymentAccountRef`

Type: `ReferenceType`
Traits: read only, system defined
Minor version: 47

Indicates the Account ID from which the payment was made (or refund was moved to).

<details>
<summary>Child attributes for `PaymentAccountRef`</summary>

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

#### `Description`

Type: `String`
Traits: read only, system defined
Minor version: 47

Specifies the Memo/Description added for this payment.

#### `PaymentAmount`

Type: `Decimal`
Traits: read only
Minor version: 47

Specifies the tax payment amount paid towards a filed tax return.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`
Traits: filterable, sortable

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
  "TaxPayment": {
    "Refund": "false",
    "SyncToken": "0",
    "domain": "QBO",
    "PaymentAccountRef": {
      "name": "Cash and cash equivalents-BAS Payment",
      "value": "57"
    },
    "PaymentAmount": "10.00",
    "PaymentDate": "2019-08-30",
    "sparse": "false",
    "Id": "8",
    "MetaData": {
      "CreateTime": "2019-08-30T06:00:26-07:00",
      "LastUpdatedTime": "2019-08-30T06:00:26-07:00"
    }
  },
  "time": "2020-02-03T11:05:54.491-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-02-03T11:05:54.491-08:00">
    <TaxPayment domain="QBO" sparse="false">
        <Id>8</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2019-08-30T06:00:26-07:00</CreateTime>
            <LastUpdatedTime>2019-08-30T06:00:26-07:00</LastUpdatedTime>
        </MetaData>
        <PaymentDate>2019-08-30</PaymentDate>
        <PaymentAccountRef name="Cash and cash equivalents-BAS Payment">57</PaymentAccountRef>
        <PaymentAmount>10.00</PaymentAmount>
        <Refund>false</Refund>
    </TaxPayment>
</IntuitResponse>
```

## Query taxpayment

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * From TaxPayment"
```

#### XML example

```sql
select * from TaxPayment
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "TaxPayment": [
      {
        "Refund": "false",
        "SyncToken": "0",
        "domain": "QBO",
        "PaymentAccountRef": {
          "name": "Cash and cash equivalents-BAS Payment",
          "value": "57"
        },
        "PaymentAmount": "10.00",
        "PaymentDate": "2019-08-30",
        "sparse": "false",
        "Id": "8",
        "MetaData": {
          "CreateTime": "2019-08-30T06:00:26-07:00",
          "LastUpdatedTime": "2019-08-30T06:00:26-07:00"
        }
      },
      {
        "Refund": "false",
        "SyncToken": "0",
        "domain": "QBO",
        "PaymentAccountRef": {
          "name": "Cash and cash equivalents-BAS Payment",
          "value": "57"
        },
        "Description": "testing VAT Payment",
        "PaymentAmount": "10.00",
        "PaymentDate": "2019-08-30",
        "sparse": "false",
        "Id": "9",
        "MetaData": {
          "CreateTime": "2019-08-30T06:02:40-07:00",
          "LastUpdatedTime": "2019-08-30T06:02:40-07:00"
        }
      },
      {
        "Refund": "false",
        "SyncToken": "0",
        "domain": "QBO",
        "PaymentAccountRef": {
          "name": "Cash and cash equivalents-BAS Payment",
          "value": "57"
        },
        "Description": "test the id",
        "PaymentAmount": "10.00",
        "PaymentDate": "2019-09-01",
        "sparse": "false",
        "Id": "10",
        "MetaData": {
          "CreateTime": "2019-09-01T01:48:39-07:00",
          "LastUpdatedTime": "2019-09-01T01:48:39-07:00"
        }
      },
      {
        "Refund": "false",
        "SyncToken": "0",
        "domain": "QBO",
        "PaymentAccountRef": {
          "name": "Cash and cash equivalents-BAS Payment",
          "value": "57"
        },
        "Description": "qwerty",
        "PaymentAmount": "15.00",
        "PaymentDate": "2019-09-01",
        "sparse": "false",
        "Id": "11",
        "MetaData": {
          "CreateTime": "2019-09-01T01:50:30-07:00",
          "LastUpdatedTime": "2019-09-01T01:50:30-07:00"
        }
      }
    ],
    "maxResults": 5,
    "totalCount": 5
  },
  "time": "2020-02-03T15:59:25.586-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-02-03T15:59:25.586-08:00">
    <QueryResponse startPosition="1" maxResults="4">
        <TaxPayment domain="QBO" sparse="false">
            <Id>8</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2019-08-30T06:00:26-07:00</CreateTime>
                <LastUpdatedTime>2019-08-30T06:00:26-07:00</LastUpdatedTime>
            </MetaData>
            <PaymentDate>2019-08-30</PaymentDate>
            <PaymentAccountRef name="Cash and cash equivalents-BAS Payment">57</PaymentAccountRef>
            <PaymentAmount>10.00</PaymentAmount>
            <Refund>false</Refund>
        </TaxPayment>
        <TaxPayment domain="QBO" sparse="false">
            <Id>9</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2019-08-30T06:02:40-07:00</CreateTime>
                <LastUpdatedTime>2019-08-30T06:02:40-07:00</LastUpdatedTime>
            </MetaData>
            <PaymentDate>2019-08-30</PaymentDate>
            <PaymentAccountRef name="Cash and cash equivalents-BAS Payment">57</PaymentAccountRef>
            <PaymentAmount>10.00</PaymentAmount>
            <Description>testing VAT Payment</Description>
            <Refund>false</Refund>
        </TaxPayment>
        <TaxPayment domain="QBO" sparse="false">
            <Id>10</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2019-09-01T01:48:39-07:00</CreateTime>
                <LastUpdatedTime>2019-09-01T01:48:39-07:00</LastUpdatedTime>
            </MetaData>
            <PaymentDate>2019-09-01</PaymentDate>
            <PaymentAccountRef name="Cash and cash equivalents-BAS Payment">57</PaymentAccountRef>
            <PaymentAmount>10.00</PaymentAmount>
            <Description>test the id</Description>
            <Refund>false</Refund>
        </TaxPayment>
        <TaxPayment domain="QBO" sparse="false">
            <Id>11</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2019-09-01T01:50:30-07:00</CreateTime>
                <LastUpdatedTime>2019-09-01T01:50:30-07:00</LastUpdatedTime>
            </MetaData>
            <PaymentDate>2019-09-01</PaymentDate>
            <PaymentAccountRef name="Cash and cash equivalents-BAS Payment">57</PaymentAccountRef>
            <PaymentAmount>15.00</PaymentAmount>
            <Description>qwerty</Description>
            <Refund>false</Refund>
        </TaxPayment>
    </QueryResponse>
</IntuitResponse>
```

## Read taxpayment

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxpayment/<taxPaymentId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the tax payment/refund made against filed tax return

### Returns

Returns the taxpayment object.

#### Example

```json
{
  "TaxPayment": {
    "Refund": "false",
    "SyncToken": "0",
    "domain": "QBO",
    "PaymentAccountRef": {
      "name": "Cash and cash equivalents-BAS Payment",
      "value": "57"
    },
    "PaymentAmount": "10.00",
    "PaymentDate": "2019-08-30",
    "sparse": "false",
    "Id": "8",
    "MetaData": {
      "CreateTime": "2019-08-30T06:00:26-07:00",
      "LastUpdatedTime": "2019-08-30T06:00:26-07:00"
    }
  },
  "time": "2020-02-03T11:05:54.491-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-02-03T11:05:54.491-08:00">
    <TaxPayment domain="QBO" sparse="false">
        <Id>8</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2019-08-30T06:00:26-07:00</CreateTime>
            <LastUpdatedTime>2019-08-30T06:00:26-07:00</LastUpdatedTime>
        </MetaData>
        <PaymentDate>2019-08-30</PaymentDate>
        <PaymentAccountRef name="Cash and cash equivalents-BAS Payment">57</PaymentAccountRef>
        <PaymentAmount>10.00</PaymentAmount>
        <Refund>false</Refund>
    </TaxPayment>
</IntuitResponse>
```
