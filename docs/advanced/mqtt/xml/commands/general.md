# Commands

This pages describes the general part of the commands.

## Request

A command request look in general like:

```json
{
  "cmdName": "[commandName]",
  "payload": "[playload]",
  "payloadType": "x",
  "auth": {
    "realm": "ecouser.net",
    "resource": "[REMOVED]",
    "token": "[REMOVED]",
    "userid": "[REMOVED]",
    "with": "users"
  },
  "td": "q",
  "toId": "[REMOVED]",
  "toRes": "[REMOVED]",
  "toType": "[REMOVED]"
}
```

### Request description

- `cmdName`: command name
- `playload`: xml with the command arguments
- `payloadType`:
  - `x`: xml
- `td`: Specifier if request or response
  - `q`: Request
- `toId`: Did of vacuum
- `toRes`: Resource of vacuum
- `toType`: class (model) of vacuum

## Response

In general a response looks like:

```json
{
  "ret": "ok",
  "resp": "[Command respone]",
  "id": "AwGB"
}
```

### Response description

- `ret`:
  - `ok`: command was retrieved successfully from vacuum
  - `fail`: some error happen. e.g. vacuum did not respond
- `resp`: response from the vacuum in XML format
- `id`: Request id