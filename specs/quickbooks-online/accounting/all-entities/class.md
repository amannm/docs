# Class

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/class
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Class
> Canonical entity: `Class`

Class objects provide a way to track different segments of the business so they're not tied to a particular client or project. For example, you can define classes to break down the income and expenses for each business segment. Classes are available to the entire transaction or to individual detail lines of a transaction.

## The class object

### classresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Name`

Required: Required
Type: `String`
Max length: maximum of 100 chars

User recognizable name for the Class.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `ParentRef`

Required: Conditionally required
Type: `ReferenceType`

The immediate parent of the SubClass. Required if this object is a subclass.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

#### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined, filterable, sortable

Fully qualified name of the entity. The fully qualified name prepends the topmost parent, followed by each sub class separated by colons. Takes the form of `Parent:Class1:SubClass1:SubClass2`. Limited to 5 levels.

#### `SubClass`

Required: Optional
Type: `Boolean`
Traits: system defined

Specifies whether this object is a subclass. `true`--this object represents a subclass. `false` or null--this object represents a top-level class.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

If true, this entity is currently enabled for use by QuickBooks.

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
  "Class": {
    "FullyQualifiedName": "France",
    "domain": "QBO",
    "Name": "France",
    "SyncToken": "0",
    "SubClass": false,
    "sparse": false,
    "Active": true,
    "Id": "5000000000000007280",
    "MetaData": {
      "CreateTime": "2015-07-22T13:57:27-07:00",
      "LastUpdatedTime": "2015-07-22T13:57:27-07:00"
    }
  },
  "time": "2015-07-22T13:57:27.84-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-22T13:58:40.998-07:00">
    <Class domain="QBO" sparse="false">
        <Id>5000000000000007281</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-22T13:58:41-07:00</CreateTime>
            <LastUpdatedTime>2015-07-22T13:58:41-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Spain</Name>
        <SubClass>false</SubClass>
        <FullyQualifiedName>Spain</FullyQualifiedName>
        <Active>true</Active>
    </Class>
</IntuitResponse>
```

## Create a class

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/class`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create a class are listed here.

Schema: `classrequest`

<details>
<summary>Show schema for `classrequest`</summary>

#### classrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`
Max length: maximum of 100 chars

User recognizable name for the Class.

##### `ParentRef`

Required: Conditionally required
Type: `ReferenceType`

For class objects that are sub-classes: the immediate parent of this object. Required if this object is a subclass.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

#### Example

```json
{
  "Name": "France"
}
```

#### XML example

```xml
<Class xmlns="http://schema.intuit.com/finance/v3">
   <Name>Spain</Name>
</Class>
```

### Returns

Returns the newly created class object.

#### Example

```json
{
  "Class": {
    "FullyQualifiedName": "France",
    "domain": "QBO",
    "Name": "France",
    "SyncToken": "0",
    "SubClass": false,
    "sparse": false,
    "Active": true,
    "Id": "5000000000000007280",
    "MetaData": {
      "CreateTime": "2015-07-22T13:57:27-07:00",
      "LastUpdatedTime": "2015-07-22T13:57:27-07:00"
    }
  },
  "time": "2015-07-22T13:57:27.84-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-22T13:58:40.998-07:00">
    <Class domain="QBO" sparse="false">
        <Id>5000000000000007281</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-22T13:58:41-07:00</CreateTime>
            <LastUpdatedTime>2015-07-22T13:58:41-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Spain</Name>
        <SubClass>false</SubClass>
        <FullyQualifiedName>Spain</FullyQualifiedName>
        <Active>true</Active>
    </Class>
</IntuitResponse>
```

## Query a class

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select  * from Class"
```

#### XML example

```sql
select  * from Class where name like 'France'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 5,
    "Class": [
      {
        "FullyQualifiedName": "Europe",
        "domain": "QBO",
        "Name": "Europe",
        "SyncToken": "0",
        "SubClass": false,
        "sparse": false,
        "Active": true,
        "Id": "5000000000000007195",
        "MetaData": {
          "CreateTime": "2015-07-14T14:25:49-07:00",
          "LastUpdatedTime": "2015-07-14T14:25:49-07:00"
        }
      },
      {
        "FullyQualifiedName": "InternalCafe",
        "domain": "QBO",
        "Name": "InternalCafe",
        "SyncToken": "2",
        "SubClass": false,
        "sparse": false,
        "Active": true,
        "Id": "5000000000000005251",
        "MetaData": {
          "CreateTime": "2015-06-30T15:38:56-07:00",
          "LastUpdatedTime": "2015-06-30T15:51:07-07:00"
        }
      },
      {
        "FullyQualifiedName": "InternalCafe:InternalParts",
        "domain": "QBO",
        "Name": "InternalParts",
        "SyncToken": "0",
        "sparse": false,
        "SubClass": true,
        "ParentRef": {
          "value": "5000000000000005251"
        },
        "Active": true,
        "Id": "5000000000000005252",
        "MetaData": {
          "CreateTime": "2015-06-30T15:41:51-07:00",
          "LastUpdatedTime": "2015-06-30T15:51:07-07:00"
        }
      },
      {
        "FullyQualifiedName": "North America",
        "domain": "QBO",
        "Name": "North America",
        "SyncToken": "0",
        "SubClass": false,
        "sparse": false,
        "Active": true,
        "Id": "5000000000000007194",
        "MetaData": {
          "CreateTime": "2015-07-14T14:24:49-07:00",
          "LastUpdatedTime": "2015-07-14T14:24:49-07:00"
        }
      },
      {
        "FullyQualifiedName": "Sales Dept",
        "domain": "QBO",
        "Name": "Sales Dept",
        "SyncToken": "0",
        "SubClass": false,
        "sparse": false,
        "Active": true,
        "Id": "5000000000000005250",
        "MetaData": {
          "CreateTime": "2015-06-30T15:37:54-07:00",
          "LastUpdatedTime": "2015-06-30T15:37:54-07:00"
        }
      }
    ],
    "maxResults": 5
  },
  "time": "2015-07-22T13:55:26.286-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-22T14:26:30.863-07:00">
  <QueryResponse startPosition="1" maxResults="1" totalCount="1">
    <Class domain="QBO" sparse="false">
      <Id>5000000000000007280</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-07-22T13:57:27-07:00</CreateTime>
        <LastUpdatedTime>2015-07-22T13:57:27-07:00</LastUpdatedTime>
      </MetaData>
      <Name>France</Name>
      <SubClass>false</SubClass>
      <FullyQualifiedName>France</FullyQualifiedName>
      <Active>true</Active>
    </Class>
  </QueryResponse>
</IntuitResponse>
```

## Read a class

### Definition

- **Operation:** `GET /v3/company/<realmID>/class/<classId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a class object that has been previously created.

### Returns

Returns the class object.

#### Example

```json
{
  "FullyQualifiedName": "France",
  "domain": "QBO",
  "Name": "France",
  "SyncToken": "0",
  "SubClass": false,
  "sparse": false,
  "Active": true,
  "Id": "5000000000000007280",
  "MetaData": {
    "CreateTime": "2015-07-22T13:57:27-07:00",
    "LastUpdatedTime": "2015-07-22T13:57:27-07:00"
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-22T15:07:06.896-07:00">
    <Class domain="QBO" sparse="false">
        <Id>5000000000000007280</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-22T13:57:27-07:00</CreateTime>
            <LastUpdatedTime>2015-07-22T13:57:27-07:00</LastUpdatedTime>
        </MetaData>
        <Name>France</Name>
        <SubClass>false</SubClass>
        <FullyQualifiedName>France</FullyQualifiedName>
        <Active>true</Active>
    </Class>
</IntuitResponse>
```

## Full update a class

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/class`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing class object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `classresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "FullyQualifiedName": "France",
  "domain": "QBO",
  "Name": "France",
  "SyncToken": "1",
  "SubClass": false,
  "sparse": false,
  "Active": true,
  "Id": "5000000000000007280",
  "MetaData": {
    "CreateTime": "2015-07-22T13:57:27-07:00",
    "LastUpdatedTime": "2015-07-22T13:57:27-07:00"
  }
}
```

#### XML example

```xml
<Class xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>5000000000000007280</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
        <CreateTime>2015-07-22T13:57:27-07:00</CreateTime>
        <LastUpdatedTime>2015-07-22T13:57:27-07:00</LastUpdatedTime>
    </MetaData>
    <Name>South France</Name>
    <SubClass>false</SubClass>
    <FullyQualifiedName>France</FullyQualifiedName>
    <Active>true</Active>
</Class>
```

### Returns

The class response body.

#### Example

```json
{
  "Class": {
    "FullyQualifiedName": "France",
    "domain": "QBO",
    "Name": "France",
    "SyncToken": "2",
    "SubClass": false,
    "sparse": false,
    "Active": true,
    "Id": "5000000000000007280",
    "MetaData": {
      "CreateTime": "2015-07-22T13:57:27-07:00",
      "LastUpdatedTime": "2015-07-22T15:13:03-07:00"
    }
  },
  "time": "2015-07-22T15:13:03.963-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-22T15:10:22.576-07:00">
    <Class domain="QBO" sparse="false">
        <Id>5000000000000007280</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2015-07-22T13:57:27-07:00</CreateTime>
            <LastUpdatedTime>2015-07-22T15:10:22-07:00</LastUpdatedTime>
        </MetaData>
        <Name>South France</Name>
        <SubClass>false</SubClass>
        <FullyQualifiedName>South France</FullyQualifiedName>
        <Active>true</Active>
    </Class>
</IntuitResponse>
```
