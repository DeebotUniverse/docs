# Messages

Messages are published asynchronous from the vacuum on the MQTT `iot/atr` channel.

The schema is the following: `iot/atr/[command name]/[did]/[class]/[resource]/j`

- `command name`: the command name
- `did`: the id of the vacuum
- `class`: the class (model) of the vacuum
- `resource`: the resource of the vacuum

The message looks similar to the [response of a command](../commands/general.md#response), except that it contains only the `resp` object of the command.

??? example "Example with `reportStats` message"

    The following message was published on `iot/atr/reportStats/[did]/[class]/[resource]/j`:

    ```json
    {
      "header": {
        "pri": 1,
        "tzm": 480,
        "ts": "1297811721698",
        "ver": "0.0.1",
        "fwVer": "1.8.2",
        "hwVer": "0.1.1"
      },
      "body": {
        "data": {
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
      }
    }
    ```

## Overview

| Command       | Refer to                                  |
| ------------- | ----------------------------------------- |
| `onStats`     | [getStats](../commands/stats.md#getstats) |
| `reportStats` | [reportStats](stats.md#reportstats)       |
