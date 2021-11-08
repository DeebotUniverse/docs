# Stats messages

## `onStats`

{%
   include-markdown "../../../../../include/advanced/data_types/json/messages/receive.md"
%}

- during a cleaning job on each cleaned m²

{%
   include-markdown "../../../../../include/advanced/data_types/json/messages/general.md"
%}

<!--onStats-->

```json
{
  "area": 36,
  "time": 2063,
  "cid": "111",
  "start": "1297462509",
  "type": "spotArea"
}
```

### Description

- `area`: The cleaned area in m²
- `time`: The elapsed time since starting this job in seconds
- `cid`: Cleaning id
- `start`: Datetime, when clean job was started
- `type`: The cleaning type

<!--onStats-end-->

## `reportStats`

{%
   include-markdown "../../../../../include/advanced/data_types/json/messages/receive.md"
%}

- on the start of a cleaning job
- on the end (stop) of a cleaning job

{%
   include-markdown "../../../../../include/advanced/data_types/json/messages/general.md"
%}

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
- `stop`:

  | Values | Description  |
  | ------ | ------------ |
  | 0      | Job started  |
  | 1      | Job finished |

The following parameters are only present at the end of the cleaning job:

- `area`: The cleaned area in m²
- `time`: The cleaning time in seconds
- `start`: datetime, when clean job was started
- `content`: The map-sub-set (room) ids, which should be cleaned by this job
- `stopReason`: The stop reason

  | Values | Description                                                          |
  | ------ | -------------------------------------------------------------------- |
  | 1      | finished normally                                                    |
  | 2      | stopped manually                                                     |
  | 3      | finished with warnings (e.g. one room not cleaned as it was blocked) |
