# Stats commands

## `getStats`

Command to get information about the last or ongoing cleaning job

### Request

Only the name and the arguments will be described. General information can be found under [Command General](general.md#request)

- Name: `getStats`
- Arguments: None

### Response

Only the `data` object will be described here.
To get information about the whole response, please refer to [Command General](general.md#response)

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

#### Response description

- `area`: The cleaned area in m²
- `time`: The elapsed time since starting this job in seconds
- `cid`: Cleaning id
- `start`: datetime, when clean job was started
- `type`: The cleaning type
- `content`: The map-sub-set (room) ids, which should be cleaned by this job
