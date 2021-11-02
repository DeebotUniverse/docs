# Stats messages

## `reportStats`

This message will be sent out on the start and on the end (stop) of a cleaning job.

Only the `data` object will be described here.
To get information about the whole message, please refer to [Messages](index.md#messages)

```json
{
  "cid": "1319392469",
  "type": "spotArea",
  "stop": 1,
  "mapCount": 15,
  "area": 0,
  "time": 7,
  "start": "1297811709",
  "content": "7,12,11,14",
  "stopReason": 2
}
```

### Description

- `cid`: Cleaning job id
- `type`: Cleaning type
- `stop`: Indicates if the job has started (`0`) or finished (`1`)

The following parameters are only present at the end of the cleaning job:

- `area`: The cleaned area in m²
- `time`: The cleaning time in seconds
- `start`: datetime, when clean job was started
- `content`: The map-sub-set (room) ids, which should be cleaned by this job
- `stopReason`: The stop reason
  - `1`: finished normally
  - `2`: stopped manually
  - `3`: finished with warnings (e.g. one room not cleaned as it was blocked)
