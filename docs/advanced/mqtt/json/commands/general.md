# Commands

This pages describes the general part of the commands.

## Request

A command request look in general like:

```json
{
  "cmdName": "[commandName]",
  "payload": {
    "header": {
      "pri": "1",
      "ts": 1635497684.660167,
      "tzm": 480,
      "ver": "0.0.50"
    },
    "body": {
      "data": "[args]"
    }
  },
  "payloadType": "j",
  "td": "q",
  "toId": "[REMOVED]",
  "toRes": "[REMOVED]",
  "toType": "[REMOVED]"
}
```

### Request description

- `cmdName`: command name
- `header`: header object, values are constant except `ts`
  - `ts`: current timestamp
- `body.data`: object with the command arguments. `body` object is missing, when command has no args.
- `payloadType`:
  - `j` stands for json
- `td`: Specifier if request or response
  - `q`: Request
  - `p`: Response
- `toId`: Did of vacuum
- `toRes`: Resource of vacuum
- `toType`: class (model) of vacuum

## Response

In general a response looks like:

```json
{
  "id": "IGoc",
  "ret": "ok",
  "resp": {
    "header": {
      "pri": 1,
      "tzm": 480,
      "ts": "1297469931855",
      "ver": "0.0.1",
      "fwVer": "1.8.2",
      "hwVer": "0.1.1"
    },
    "body": {
      "data": "[Command respone]",
      "code": 0,
      "msg": "ok"
    }
  }
}
```

### Response description

- `id`: Request id
- `ret`:
  - `ok`: command was retrieved successfully from vacuum
  - `fail`: some error happen. e.g. vacuum did not respond
- `resp`: response object from the vacuum
  - `header`
    - `ts`: timestamp
    - `ver`: protocol version
    - `fwVer`: firmware version
    - `hwVer`: hardware version
  - `body`
    - `data`: Holding the actual response from the command. See specific command
  - `code`: Error code; `0` means no error, command was executed successfully
  - `msg`: Description for the error code
