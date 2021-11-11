# REST

This pages describes the general part of the used rest api.

## Request

A command request look in general like:

```json
{
  "cmdName": "[commandName]",
  "payload": "[playload]",
  "payloadType": "[payloadType]",
  "auth": {
    "realm": "ecouser.net",
    "resource": "[resource]",
    "token": "[token]",
    "userid": "[userid]",
    "with": "users"
  },
  "td": "q",
  "toId": "[toId]",
  "toRes": "[toRes]",
  "toType": "[toType]"
}
```

### Description

- `cmdName`: command name
- `playload`: command request object. Will be described in the respective payload type
  - [json commands](../data_types/json/commands/index.md)
  - [xml commands](../data_types/xml/commands/index.md)
- `payloadType`:

  {% include 'advanced/protocols/data_type.md' %}

- `auth`: the authentication object
- `td`: Specifier if request or response

  | Value | Description |
  | ----- | ----------- |
  | q     | request     |

- `toId`: Did of vacuum
- `toRes`: Resource of vacuum
- `toType`: class (model) of vacuum (e.g. `ls1ok3`)

## Response

In general a response looks like:

```json
{
  "id": "[id]",
  "ret": "ok",
  "resp": "[Command response]"
}
```

### Description

- `id`: Request id
- `ret`: status

  | Value | Description                                             |
  | ----- | ------------------------------------------------------- |
  | ok    | command response was retrieved successfully from vacuum |
  | fail  | some error happen. e.g. vacuum did not respond          |

- `resp`: command response. Can be missing if the command is only executing something.
  Will be described in the respective payload type
