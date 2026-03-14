# Department

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/department
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Department
> Canonical entity: `Department`

The Department resource provides a way to track transactions based on physical locations such as stores, sales regions, or countries. As you create sales and expense transactions, consistently designate the department to which they belong.
Delete is achieved by setting the `Active` attribute to `false` in an entity update request; thus, making it inactive. In this type of delete, the record is not permanently deleted, but is hidden for display purposes. References to inactive objects are left intact.

## The department object

### departmentresponse

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

User recognizable name for the Department.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `ParentRef`

Required: Conditionally required
Type: `ReferenceType`

The immediate parent of the SubDepartment. Required for the create operation if this object is a SubDepartment. Required if this object is a subdepartment.

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

Fully qualified name of the entity. The fully qualified name prepends the topmost parent, followed by each sub element separated by colons. Takes the form of `Parent:Department1:SubDepartment1:SubDepartment2`. Limited to 5 levels.

#### `SubDepartment`

Type: `Boolean`
Traits: read only, system defined, sortable
Default: false

Specifies whether this Department object is a SubDepartment. `true`--SubDepartment. `false` or null--top-level Department.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

If true, this entity is currently enabled for use by QuickBooks. If set to false, this entity is not available.

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
  "Department": {
    "FullyQualifiedName": "Marketing Department",
    "domain": "QBO",
    "Name": "Marketing Department",
    "SyncToken": "0",
    "SubDepartment": false,
    "sparse": false,
    "Active": true,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2013-08-13T11:52:48-07:00",
      "LastUpdatedTime": "2013-08-13T11:52:48-07:00"
    }
  },
  "time": "2013-08-13T11:54:48.026-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-08-13T11:54:13.371-07:00">
    <Department domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2013-08-13T11:52:48-07:00</CreateTime>
            <LastUpdatedTime>2013-08-13T11:52:48-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Marketing Department</Name>
        <SubDepartment>false</SubDepartment>
        <FullyQualifiedName>Marketing Department</FullyQualifiedName>
        <Active>true</Active>
    </Department>
</IntuitResponse>
```

## Create a department

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/department`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create a Department object are listed here.

Schema: `departmentrequest`

<details>
<summary>Show schema for `departmentrequest`</summary>

#### departmentrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`
Max length: maximum of 100 chars

User recognizable name for the department.

##### `ParentRef`

Required: Conditionally required
Type: `ReferenceType`

The immediate parent of the SubDepartment. Required for the create operation if this object is a SubDepartment. Required if this object is a subdepartment

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
  "Name": "Marketing Department"
}
```

#### XML example

```xml
<Department xmlns="http://schema.intuit.com/finance/v3">
   <Name>Sales Department</Name>
</Department>
```

### Returns

Returns the newly created Department object.

#### Example

```json
{
  "Department": {
    "FullyQualifiedName": "Marketing Department",
    "domain": "QBO",
    "Name": "Marketing Department",
    "SyncToken": "0",
    "SubDepartment": false,
    "sparse": false,
    "Active": true,
    "Id": "3",
    "MetaData": {
      "CreateTime": "2015-07-23T12:54:44-07:00",
      "LastUpdatedTime": "2015-07-23T12:54:44-07:00"
    }
  },
  "time": "2015-07-23T12:54:44.248-07:00"
}
```

#### XML example

```xml
<<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T12:53:47.547-07:00">
    <Department domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-23T12:53:47-07:00</CreateTime>
            <LastUpdatedTime>2015-07-23T12:53:47-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Sales Department</Name>
        <SubDepartment>false</SubDepartment>
        <FullyQualifiedName>Sales Department</FullyQualifiedName>
        <Active>true</Active>
    </Department>
    </IntuitResponse>
```

## Query a department

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Department"
```

#### XML example

```sql
select * from Department
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "Department": [
      {
        "FullyQualifiedName": "Sales Department",
        "domain": "QBO",
        "Name": "Sales Department",
        "SyncToken": "0",
        "SubDepartment": false,
        "sparse": false,
        "Active": false,
        "Id": "1",
        "MetaData": {
          "CreateTime": "2013-08-13T11:49:31-07:00",
          "LastUpdatedTime": "2013-08-13T11:49:31-07:00"
        }
      },
      {
        "FullyQualifiedName": "Support Department",
        "domain": "QBO",
        "Name": "Support Department",
        "SyncToken": "2",
        "SubDepartment": false,
        "sparse": false,
        "Active": false,
        "Id": "2",
        "MetaData": {
          "CreateTime": "2013-08-13T11:52:48-07:00",
          "LastUpdatedTime": "2013-08-13T11:58:58-07:00"
        }
      }
    ],
    "startPosition": 1,
    "maxResults": 2
  },
  "time": "2013-08-13T12:04:05.965-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-08-13T12:03:21.548-07:00">
    <QueryResponse startPosition="1" maxResults="2">
        <Department domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2013-08-13T11:49:31-07:00</CreateTime>
                <LastUpdatedTime>2013-08-13T11:49:31-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Sales Department</Name>
            <SubDepartment>false</SubDepartment>
            <FullyQualifiedName>Sales Department</FullyQualifiedName>
            <Active>false</Active>
        </Department>
        <Department domain="QBO" sparse="false">
            <Id>2</Id>
            <SyncToken>2</SyncToken>
            <MetaData>
                <CreateTime>2013-08-13T11:52:48-07:00</CreateTime>
                <LastUpdatedTime>2013-08-13T11:58:58-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Support Department</Name>
            <SubDepartment>false</SubDepartment>
            <FullyQualifiedName>Support Department</FullyQualifiedName>
            <Active>false</Active>
        </Department>
    </QueryResponse>
</IntuitResponse>
```

## Read a department

### Definition

- **Operation:** `GET /v3/company/<realmID>/department/<departmentId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Department object that has been previously created.

### Returns

Returns the Department object.

#### Example

```json
{
  "Department": {
    "FullyQualifiedName": "Marketing Department",
    "domain": "QBO",
    "Name": "Marketing Department",
    "SyncToken": "0",
    "SubDepartment": false,
    "sparse": false,
    "Active": true,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2013-08-13T11:52:48-07:00",
      "LastUpdatedTime": "2013-08-13T11:52:48-07:00"
    }
  },
  "time": "2013-08-13T11:54:48.026-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-08-13T11:54:13.371-07:00">
    <Department domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2013-08-13T11:52:48-07:00</CreateTime>
            <LastUpdatedTime>2013-08-13T11:52:48-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Marketing Department</Name>
        <SubDepartment>false</SubDepartment>
        <FullyQualifiedName>Marketing Department</FullyQualifiedName>
        <Active>true</Active>
    </Department>
</IntuitResponse>
```

## Full update a department

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/department`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing Department object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `departmentresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "FullyQualifiedName": "Marketing Department",
  "domain": "QBO",
  "Name": "Support Department",
  "SyncToken": "1",
  "SubDepartment": false,
  "sparse": false,
  "Active": true,
  "Id": "2",
  "MetaData": {
    "CreateTime": "2013-08-13T11:52:48-07:00",
    "LastUpdatedTime": "2013-08-13T11:52:48-07:00"
  }
}
```

#### XML example

```xml
<Department xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2013-08-13T11:52:48-07:00</CreateTime>
            <LastUpdatedTime>2013-08-13T11:52:48-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Accounting Department</Name>
        <SubDepartment>false</SubDepartment>
        <FullyQualifiedName>Marketing Department</FullyQualifiedName>
        <Active>true</Active>
    </Department>
```

### Returns

The Department object response body.

#### Example

```json
{
  "Department": {
    "FullyQualifiedName": "Support Department",
    "domain": "QBO",
    "Name": "Support Department",
    "SyncToken": "2",
    "SubDepartment": false,
    "sparse": false,
    "Active": true,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2013-08-13T11:52:48-07:00",
      "LastUpdatedTime": "2013-08-13T11:58:58-07:00"
    }
  },
  "time": "2013-08-13T11:58:58.925-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-08-13T11:56:27.351-07:00">
    <Department domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2013-08-13T11:52:48-07:00</CreateTime>
            <LastUpdatedTime>2013-08-13T11:56:27-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Accounting Department</Name>
        <SubDepartment>false</SubDepartment>
        <FullyQualifiedName>Accounting Department</FullyQualifiedName>
        <Active>true</Active>
    </Department>
</IntuitResponse>
```
