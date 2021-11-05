# Stats commands

## `getStats`

Command to get information about the last or ongoing cleaning job

### Request

{%
   include-markdown "../../../../../include/advanced/mqtt/json/commands/request.md"
%}

- Name: `getStats`
- Arguments: None

### Response

{%
   include-markdown "../../../../../include/advanced/mqtt/json/commands/response.md"
%}

```json
{
  "area": 36,
  "time": 2063,
  "cid": "111",
  "start": "1297462509",
  "type": "spotArea",
  "content": "7,12,11,14"
}
```

#### Description

- `area`: The cleaned area in m²
- `time`: The elapsed time since starting this job in seconds
- `cid`: Cleaning id
- `start`: datetime, when clean job was started
- `type`: The cleaning type
- `content`: The map-sub-set (room) ids, which should be cleaned by this job
