# Attachable

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/attachable
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Attachable
> Canonical entity: `Attachable`

This page covers the Attachable, Upload, and Download resources used for attachment management. Attachments are supplemental information linked to a transaction or Item object. They can be files, notes, or a combination of both.

- In the case of file attachments, use an upload endpoint multipart request to upload the files to the QuickBooks attachment list and, optionally, to supply metadata for each via an attachable object. If meta data is not supplied with the upload request, the system creates it.
- In the case of a note, use the create attachable endpoint.

### Business Rules

An upload request may contain as many files as possible in a request, but the overall request size must not exceed 100 MB.

An attachable record can either contain a note only, a file attachment only, or both.
When using file `FileName` and `Note` attributes together, it's up to the app to manage how the note relates to the file name.

<details>
<summary>Show types approved for uploading</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **FILE TYPE** | **CONTENT TYPE** |
| ai | application/postscript |
| csv | text/csv |
| doc | application/msword |
| docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| eps | application/postscript |
| gif | image/gif |
| jpeg | image/jpeg |
| jpg | image/jpg |
| ods | application/vnd.oasis.opendocument.spreadsheet |
| pdf | application/pdf |
| png | image/png |
| rtf | text/rtf |
| tif | image/tif |
| txt | text/plain |
| xls | application/vnd/ms-excel |
| xlsx | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet |
| xml | text/xml |

</details>

## The attachable object

### attachableresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `IdType`
Traits: read only, system defined, filterable, sortable

Unique Identifier for an Intuit entity (object). Required for the update operation.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `FileName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum 1000 chars

FileName of the attachment. Required for file attachments.

#### `Note`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: max 2000 chars

This note is either related to the attachment specified by `FileName` or is a standalone note. Required for standalone notes.

#### `FileAccessUri`

Type: `String`
Traits: read only, system defined

FullPath FileAccess URI of the attachment. Returned for file attachments.

#### `Size`

Type: `Decimal`
Traits: read only, system defined, filterable, sortable

Size of the attachment. Returned for file attachments.

#### `ThumbnailFileAccessUri`

Type: `String`
Traits: read only, system defined

FullPath FileAccess URI of the attachment thumbnail if the attachment file is of a content type with thumbnail support. Returned for file attachments.

#### `TempDownloadUri`

Type: `String`
Traits: read only, system defined

TempDownload URI which can be directly downloaded by clients. Returned for file attachments.

#### `ThumbnailTempDownloadUri`

Type: `String`
Traits: read only, system defined, filterable, sortable

Thumbnail TempDownload URI which can be directly downloaded by clients. This is only available if the attachment file is of a content type with thumbnail support. Returned for file attachments.

#### `Category`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: max 100 chars

Category of the attachment. Valid values include (case sensitive): `Contact Photo`, `Document`, `Image`, `Receipt`, `Signature`, `Sound`, `Other`.

#### `ContentType`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: max 100 chars

ContentType of the attachment. Returned for file attachments.

#### `PlaceName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: max 2000 chars

PlaceName from where the attachment was requested.

#### `AttachableRef`

Required: Optional
Type: `AttachableRef`

Specifies the transaction object to which this attachable file is to be linked.

<details>
<summary>Child attributes for `AttachableRef`</summary>

##### attachableref

Model type: `object`

###### `IncludeOnSend`

Required: Optional
Type: `Boolean`
Traits: filterable

Used when `EntityRef.type` references a transaction object. This field indicates whether or not the attachment is sent with the transaction when **Save and Send** button is clicked in the QuickBooks UI or when the Send endpoint (send email) is invoked for the object.

###### `LineInfo`

Required: Optional
Type: `String`
Traits: filterable

For transaction objects, used to reference a transaction detail line.

###### `NoRefOnly`

Required: Optional
Type: `Boolean`
Traits: filterable

Indicates whether or not to find attachable records that have no references to any entity. Combine with `AttachableRef.Inactive`to return hidden references.

###### `CustomField[0..n]`

Required: Optional
Type: `CustomField`

If the user tries to fetch a record without permission, the permission denied message is conveyed through this field.

<details>
<summary>Child attributes for `CustomField[0..n]`</summary>

###### customfield

Model type: `object`

###### `DefinitionId`

Required: Required
Type: `String`
Traits: read only, system defined

Unique identifier of the CustomFieldDefinition that corresponds to this CustomField.

###### `Type`

Type: `CustomFieldTypeEnum`
Traits: read only

Data type of custom field. Only one type is currently supported: `StringType`.

###### `StringValue`

Required: Optional
Type: `String`

The value for the `StringType`custom field.

###### `Name`

Required: Optional
Type: `String`
Traits: read only

Name of the custom field.

</details>

###### `Inactive`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: false

Indicates whether or not to include references to hidden entities when filtering. When set to `true` , hidden references are returned in the result set. For filtering results, it works with `AttachableRef.EntityRef.Type` , `AttachableRef.EntityRef.Value` and `AttachableRef.NoRefOnly` filters in combination.

###### `EntityRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable

Object reference to which this attachment is linked.

Set `EntityRef.value` with the `Id` of the target object as returned in its response body when queried.

Set `EntityRef.type` with the specific type of the target object. For example, `invoice`, `bill`, `item`, etc.

<details>
<summary>Child attributes for `EntityRef`</summary>

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

#### `Long`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: max 100 chars

Longitude from where the attachment was requested.

#### `Tag`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: max 2000 chars

Tag name for the requested attachment.

#### `Lat`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: max 100 chars

Latitude from where the attachment was requested.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the entity. The MetaData values are set by Data Services and are read only for all applications.

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
  "Attachable": {
    "SyncToken": "0",
    "domain": "QBO",
    "AttachableRef": [
      {
        "IncludeOnSend": false,
        "EntityRef": {
          "type": "Invoice",
          "value": "95"
        }
      }
    ],
    "Note": "This is an attached note.",
    "sparse": false,
    "Id": "200900000000000008541",
    "MetaData": {
      "CreateTime": "2015-11-17T11:05:15-08:00",
      "LastUpdatedTime": "2015-11-17T11:05:15-08:00"
    }
  },
  "time": "2015-11-17T11:05:15.797-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-09-05T14:02:42.078-07:00">
  <Attachable domain="QBO" sparse="false">
    <Id>100000000000376715</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2013-09-05T14:02:42-07:00</CreateTime>
      <LastUpdatedTime>2013-09-05T14:02:42-07:00</LastUpdatedTime>
    </MetaData>
    <AttachableRef>
      <EntityRef type="Invoice">671</EntityRef>
      <IncludeOnSend>false</IncludeOnSend>
    </AttachableRef>
    <Lat>25.293112341223</Lat>
    <Long>-21.3253249834</Long>
    <PlaceName>Mountain View</PlaceName>
    <Note>This is an attached note.</Note>
    <Tag>Create Attachable with Note</Tag>
  </Attachable>
</IntuitResponse>
```

## Create a note attachment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/attachable`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this endpoint to attach a note to the an object. Adjust values in the `AttachableRef` element for your specific target object. The value for `AttachableRef.EntityRef.value` is the `Id` of the target object as returned in its response body when queried.

### Request Body

The minimum elements to create an attachable are listed here.

Schema: `attachablerequest`

<details>
<summary>Show schema for `attachablerequest`</summary>

#### attachablerequest

Model type: `object`

##### `Note`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: max 2000 chars

The note is either related to the attachment specified with the `FileName` attribute, or as a standalone note. Required for note attachments.

##### `FileName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum 1000 chars

FileName of the attachment. Required for file attachments.

##### `AttachableRef`

Required: Optional
Type: `AttachableRef`

Specifies the transaction object to which this attachable file is to be linked.

<details>
<summary>Child attributes for `AttachableRef`</summary>

###### attachableref

Model type: `object`

###### `IncludeOnSend`

Required: Optional
Type: `Boolean`
Traits: filterable

Used when `EntityRef.type` references a transaction object. This field indicates whether or not the attachment is sent with the transaction when **Save and Send** button is clicked in the QuickBooks UI or when the Send endpoint (send email) is invoked for the object.

###### `LineInfo`

Required: Optional
Type: `String`
Traits: filterable

For transaction objects, used to reference a transaction detail line.

###### `NoRefOnly`

Required: Optional
Type: `Boolean`
Traits: filterable

Indicates whether or not to find attachable records that have no references to any entity. Combine with `AttachableRef.Inactive`to return hidden references.

###### `CustomField[0..n]`

Required: Optional
Type: `CustomField`

If the user tries to fetch a record without permission, the permission denied message is conveyed through this field.

<details>
<summary>Child attributes for `CustomField[0..n]`</summary>

###### customfield

Model type: `object`

###### `DefinitionId`

Required: Required
Type: `String`
Traits: read only, system defined

Unique identifier of the CustomFieldDefinition that corresponds to this CustomField.

###### `Type`

Type: `CustomFieldTypeEnum`
Traits: read only

Data type of custom field. Only one type is currently supported: `StringType`.

###### `StringValue`

Required: Optional
Type: `String`

The value for the `StringType`custom field.

###### `Name`

Required: Optional
Type: `String`
Traits: read only

Name of the custom field.

</details>

###### `Inactive`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: false

Indicates whether or not to include references to hidden entities when filtering. When set to `true` , hidden references are returned in the result set. For filtering results, it works with `AttachableRef.EntityRef.Type` , `AttachableRef.EntityRef.Value` and `AttachableRef.NoRefOnly` filters in combination.

###### `EntityRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable

Object reference to which this attachment is linked.

Set `EntityRef.value` with the `Id` of the target object as returned in its response body when queried.

Set `EntityRef.type` with the specific type of the target object. For example, `invoice`, `bill`, `item`, etc.

<details>
<summary>Child attributes for `EntityRef`</summary>

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

</details>

#### Example

```json
{
  "Note": "This is an attached note.",
  "AttachableRef": [
    {
      "IncludeOnSend": "false",
      "EntityRef": {
        "type": "Invoice",
        "value": "95"
      }
    }
  ]
}
```

#### XML example

```xml
<Attachable xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <Lat>25.293112341223</Lat>
   <Long>-21.3253249834</Long>
   <Note>This is an attached note.</Note>
   <Tag>Create Attachable with Note</Tag>
   <PlaceName>Mountain View</PlaceName>
   <AttachableRef>
      <EntityRef type="Invoice">671</EntityRef>
   </AttachableRef>
</Attachable>
```

### Returns

The attachable response body.

#### Example

```json
{
  "Attachable": {
    "SyncToken": "0",
    "domain": "QBO",
    "AttachableRef": [
      {
        "IncludeOnSend": false,
        "EntityRef": {
          "type": "Invoice",
          "value": "95"
        }
      }
    ],
    "Note": "This is an attached note.",
    "sparse": false,
    "Id": "200900000000000008541",
    "MetaData": {
      "CreateTime": "2015-11-17T11:05:15-08:00",
      "LastUpdatedTime": "2015-11-17T11:05:15-08:00"
    }
  },
  "time": "2015-11-17T11:05:15.797-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-09-05T14:02:42.078-07:00">
  <Attachable domain="QBO" sparse="false">
    <Id>100000000000376715</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2013-09-05T14:02:42-07:00</CreateTime>
      <LastUpdatedTime>2013-09-05T14:02:42-07:00</LastUpdatedTime>
    </MetaData>
    <AttachableRef>
      <EntityRef type="Invoice">671</EntityRef>
      <IncludeOnSend>false</IncludeOnSend>
    </AttachableRef>
    <Lat>25.293112341223</Lat>
    <Long>-21.3253249834</Long>
    <PlaceName>Mountain View</PlaceName>
    <Note>This is an attached note.</Note>
    <Tag>Create Attachable with Note</Tag>
  </Attachable>
</IntuitResponse>
```

## Delete an attachable

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/attachable?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the attachable object specified in the request body. The request body must include the full payload of the attachable as returned in a read response.

### Request Body

Schema: `attachableresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "AttachableRef": [
    {
      "IncludeOnSend": false,
      "EntityRef": {
        "type": "Invoice",
        "value": "95"
      }
    }
  ],
  "Note": "This is an attached note.",
  "sparse": false,
  "Id": "200900000000000008541",
  "MetaData": {
    "CreateTime": "2015-11-17T11:05:15-08:00",
    "LastUpdatedTime": "2015-11-17T11:05:15-08:00"
  }
}
```

#### XML example

```xml
<Attachable xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
  <Id>100100000000000494787</Id>
  <SyncToken>0</SyncToken>
  <MetaData>
    <CreateTime>2013-04-23T08:56:37-07:00</CreateTime>
    <LastUpdatedTime>2013-04-23T08:56:37-07:00</LastUpdatedTime>
  </MetaData>
  <FileName>hello.txt</FileName>
  <FileAccessUri>/v3/company/220157472/download/100100000000000494787</FileAccessUri>
  <TempDownloadUri>d</TempDownloadUri>
  <Size>13</Size>
  <ContentType>text/plain</ContentType>
</Attachable>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Attachable": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "200900000000000008541"
  },
  "time": "2015-03-15T11:27:41.514-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:56:59.994-07:00">
  <Attachable domain="QBO" status="Deleted">
    <Id>100100000000000494787</Id>
  </Attachable>
</IntuitResponse>
```

## Download an attachment

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/download/<attachableId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves a temporary download URL to the specified `attchableID` as returned in the `attachable.Id` attribute from a read response. The application uses this URL to then download the file as a separate step. The URL expires after 15 minutes, after which time the app may obtain another.

### Returns

#### Example

```text
"https://intuit-.../attachments/receipt_june10.pdf?Expires=...&AWSAccessKeyId=...&Signature=..."
```

#### XML example

```text
https://intuit-.../attachments/receipt_june10.pdf?Expires=...&AWSAccessKeyId=...&Signature=...
```

## Query an attachable

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

The sample query on the right returns the attachable ids for all attachments linked to the purchase object whose Id is 611. To formulate this query, you must first know the type of object and its object Id using the query endpoint for that resource.

- Set `AttachableRef.EntityRef.type` with the specific type of the target object. For this example, `purchase` is used.
- Set `AttachableRef.EntityRef.value` with the `Id` of the target object as returned in its response body when queried. For this example, `611` is used.

### Sample Query

The sample query on the right returns the attachable ids for all attachments linked to the purchase object whose Id is 611. To formulate this query, you must first know the type of object and its object Id using the query endpoint for that resource.
For your own request:

- Set `AttachableRef.EntityRef.type` with the specific type of the target object. For this example, `purchase` is used.
- Set `AttachableRef.EntityRef.value` with the `Id` of the target object as returned in its response body when queried. For this example, `611` is used.

#### Example

```sql
"select Id from attachable where AttachableRef.EntityRef.Type = 'purchase' and AttachableRef.EntityRef.value = '611'"
```

#### XML example

```sql
select Id from attachable where AttachableRef.EntityRef.Type = 'purchase' and AttachableRef.EntityRef.value = '611'
```

### Returns

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Attachable": [
      {
        "Id": "100000000004062174",
        "sparse": true
      },
      {
        "Id": "100000000004158481",
        "sparse": true
      }
    ],
    "maxResults": 2
  },
  "time": "2015-11-24T10:18:31.289-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-11-24T10:19:22.019-08:00">
  <QueryResponse startPosition="1" maxResults="2">
    <Attachable sparse="true">
      <Id>100000000004062174</Id>
    </Attachable>
    <Attachable sparse="true">
      <Id>100000000004158481</Id>
    </Attachable>
  </QueryResponse>
</IntuitResponse>
```

## Read an attachable

### Definition

- **Operation:** `GET /v3/company/<realmID>/attachable/<attachableId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of an attachable item that has been previously created.

### Returns

The attachable response body.

#### Example

```json
{
  "Attachable": {
    "SyncToken": "0",
    "domain": "QBO",
    "AttachableRef": [
      {
        "IncludeOnSend": false,
        "EntityRef": {
          "type": "Invoice",
          "value": "95"
        }
      }
    ],
    "Note": "This is an attached note.",
    "sparse": false,
    "Id": "5000000000000010341",
    "MetaData": {
      "CreateTime": "2015-11-17T11:05:15-08:00",
      "LastUpdatedTime": "2015-11-17T11:05:15-08:00"
    }
  },
  "time": "2015-11-17T11:09:34.216-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-07-11T17:49:59.087-07:00">
<Attachable domain="QBO" sparse="false">
  <Id>100100000000000002117</Id>
  <SyncToken>0</SyncToken>
  <MetaData>
     <CreateTime>2012-05-10T11:53:14-07:00</CreateTime>
     <LastUpdatedTime>2012-05-10T11:53:16-07:00</LastUpdatedTime>
  </MetaData>
  <Lat>25.293112341223</Lat>
  <Long>-21.3253249834</Long>
  <Note>This is an attached note.</Note>
  <Tag>Create Attachable with Note</Tag>
  <PlaceName>Mountain View</PlaceName>
  <AttachableRef>
      <EntityReftype="Vendor">10576</EntityRef>
  </AttachableRef>
</Attachable>
</IntuitResponse>
```

## Full update an attachable

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/attachable`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing attachable object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `attachableresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "AttachableRef": [
    {
      "IncludeOnSend": false,
      "EntityRef": {
        "type": "Invoice",
        "value": "95"
      }
    }
  ],
  "Note": "This is an updated attached note.",
  "sparse": false,
  "Id": "5000000000000010341",
  "MetaData": {
    "CreateTime": "2015-11-17T11:05:15-08:00",
    "LastUpdatedTime": "2015-11-17T11:05:15-08:00"
  }
}
```

#### XML example

```xml
<Attachable xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
  <Id>100100000000000002117</Id>
  <SyncToken>0</SyncToken>
  <MetaData>
     <CreateTime>2012-05-10T11:53:14-07:00</CreateTime>
     <LastUpdatedTime>2012-05-10T11:53:16-07:00</LastUpdatedTime>
  </MetaData>
  <Lat>25.293112341223</Lat>
  <Long>-21.3253249834</Long>
  <Note>This is an attached note.</Note>
  <Tag>Create Attachable with Note with update.</Tag>
  <PlaceName>Mountain View</PlaceName>
  <AttachableRef>
      <EntityRef type="Vendor">10576</EntityRef>
  </AttachableRef>
</Attachable>
```

### Returns

The attachable response body.

#### Example

```json
{
  "Attachable": {
    "SyncToken": "1",
    "domain": "QBO",
    "AttachableRef": [
      {
        "IncludeOnSend": false,
        "EntityRef": {
          "type": "Invoice",
          "value": "95"
        }
      }
    ],
    "Note": "This is an updated attached note.",
    "sparse": false,
    "Id": "5000000000000010341",
    "MetaData": {
      "CreateTime": "2015-11-17T11:05:15-08:00",
      "LastUpdatedTime": "2015-11-17T11:11:04-08:00"
    }
  },
  "time": "2015-11-17T11:11:21.679-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-07-11T17:49:56.807-07:00">
<Attachable domain="QBO" sparse="false">
<Id>100100000000000002117</Id>
  <SyncToken>1</SyncToken>
  <MetaData>
     <CreateTime>2012-05-10T11:53:14-07:00</CreateTime>
     <LastUpdatedTime>2012-05-10T11:55:16-07:00</LastUpdatedTime>
  </MetaData>
  <Lat>25.293112341223</Lat>
  <Long>-21.3253249834</Long>
  <Note>This is an attached note.</Note>
  <Tag>Create Attachable with Note with update.</Tag>
  <PlaceName>Mountain View</PlaceName>
  <AttachableRef>
      <EntityRef type="Vendor">10576</EntityRef>
  </AttachableRef>
</IntuitResponse>
```

## Upload attachments

### Definition

- **Content type:** `multipart/form-data`
- **Operation:** `POST /v3/company/<realmID>/upload`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The upload endpoint allows the app to upload one or more attachments, with or without associated metadata, via a multipart/form-data request. The particular sample shown on the right is a two-part multipart request to upload an image and its associated Attachable metadata, linking the image to a target invoice object. Each part has its own header that contains:

- A boundary separator.
- A header specifying content disposition and content type. See sample request body on the right pane.

For your own request, adjust values in the `AttachableRef` element of the `Attachable` metadata part for your specific target object.

- Set `AttachableRef.EntityRef.value` with the `Id` of the target object as returned in its response body when queried.
- Set `AttachableRef.EntityRef.type` with the specific type of the target object. For example, `invoice`, `bill`, etc.

The minimum elements to create an attachable object are listed here.

Schema: `attachablerequest`

<details>
<summary>Show schema for `attachablerequest`</summary>

#### attachablerequest

Model type: `object`

##### `Note`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: max 2000 chars

The note is either related to the attachment specified with the `FileName` attribute, or as a standalone note. Required for note attachments.

##### `FileName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum 1000 chars

FileName of the attachment. Required for file attachments.

##### `AttachableRef`

Required: Optional
Type: `AttachableRef`

Specifies the transaction object to which this attachable file is to be linked.

<details>
<summary>Child attributes for `AttachableRef`</summary>

###### attachableref

Model type: `object`

###### `IncludeOnSend`

Required: Optional
Type: `Boolean`
Traits: filterable

Used when `EntityRef.type` references a transaction object. This field indicates whether or not the attachment is sent with the transaction when **Save and Send** button is clicked in the QuickBooks UI or when the Send endpoint (send email) is invoked for the object.

###### `LineInfo`

Required: Optional
Type: `String`
Traits: filterable

For transaction objects, used to reference a transaction detail line.

###### `NoRefOnly`

Required: Optional
Type: `Boolean`
Traits: filterable

Indicates whether or not to find attachable records that have no references to any entity. Combine with `AttachableRef.Inactive`to return hidden references.

###### `CustomField[0..n]`

Required: Optional
Type: `CustomField`

If the user tries to fetch a record without permission, the permission denied message is conveyed through this field.

<details>
<summary>Child attributes for `CustomField[0..n]`</summary>

###### customfield

Model type: `object`

###### `DefinitionId`

Required: Required
Type: `String`
Traits: read only, system defined

Unique identifier of the CustomFieldDefinition that corresponds to this CustomField.

###### `Type`

Type: `CustomFieldTypeEnum`
Traits: read only

Data type of custom field. Only one type is currently supported: `StringType`.

###### `StringValue`

Required: Optional
Type: `String`

The value for the `StringType`custom field.

###### `Name`

Required: Optional
Type: `String`
Traits: read only

Name of the custom field.

</details>

###### `Inactive`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: false

Indicates whether or not to include references to hidden entities when filtering. When set to `true` , hidden references are returned in the result set. For filtering results, it works with `AttachableRef.EntityRef.Type` , `AttachableRef.EntityRef.Value` and `AttachableRef.NoRefOnly` filters in combination.

###### `EntityRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable

Object reference to which this attachment is linked.

Set `EntityRef.value` with the `Id` of the target object as returned in its response body when queried.

Set `EntityRef.type` with the specific type of the target object. For example, `invoice`, `bill`, `item`, etc.

<details>
<summary>Child attributes for `EntityRef`</summary>

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

</details>

#### Example

```json
{
  "AttachableRef": [
    {
      "EntityRef": {
        "type": "Invoice",
        "value": "95"
      }
    }
  ],
  "ContentType": "image/jpg",
  "FileName": "receipt_nov15.jpg"
}
```

#### XML example

```text
Not available.
```

### Returns

The attachable response body.

#### Example

```json
{
  "AttachableResponse": [
    {
      "Attachable": {
        "SyncToken": "0",
        "domain": "QBO",
        "FileAccessUri": "...",
        "ThumbnailFileAccessUri": "...",
        "AttachableRef": [
          {
            "IncludeOnSend": false,
            "EntityRef": {
              "type": "Invoice",
              "value": "95"
            }
          }
        ],
        "TempDownloadUri": "https://...",
        "MetaData": {
          "CreateTime": "2015-11-16T10:59:02-08:00",
          "LastUpdatedTime": "2015-11-16T10:59:02-08:00"
        },
        "sparse": false,
        "ContentType": "image/jpeg",
        "FileName": "receipt_nov15.jpg",
        "Id": "100000000004190865",
        "Size": 1594261
      }
    }
  ],
  "time": "2015-11-16T10:58:58.100-08:00"
}
```

#### XML example

```text
Not available.
```
