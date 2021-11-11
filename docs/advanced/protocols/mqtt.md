# MQTT

It is possible to subscribe for "broadcast" messages sent out asynchronous from the bot
on the channel `iot/atr`.
The advantage for these messages is, that the robot is informing us, when some data
changed, instead that we need to poll the data continuously.

The schema is the following:

`iot/atr/[command name]/[did]/[class]/[resource]/[data type]`

- `command name`: the command name
- `did`: the id of the vacuum
- `class`: the class (model) of the vacuum
- `resource`: the resource of the vacuum
- `data type`: data type

  {% include 'advanced/protocols/data_type.md' %}

More information can be found under the respective data type:

- [json](../data_types/json/messages/index.md)
- [xml](../data_types/xml/messages/index.md)

??? example "Json-example with `reportStats` message"

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
