# Events

The integration currently fires the following events:

## `deebot_cleaning_job`

Will be fired on start and end of a cleaning job and has the following structure:

- `cleaning_id`: cleaning id
- `status`: status of job
- `type`: cleaning type

The following keys are only available at the end of a cleaning:

- `area`: cleaned area
- `content`: Depends on the `type`
  - Ids of the rooms, when `type=spotArea`
  - Coordinates when `type=customArea`
- `time`: duration in seconds

!!! note

    When `status=finished` than the content can be trusted to be cleaned. Otherwise we cannot be sure.
    The vacuum unfortunately only sends this inaccurate status.

## `deebot_custom_command`

!!! warning "Only for advanced users"

    The reason for this event is only to give advanced users the possibility to
    try/use a command, which is not implemented yet.

Will be fired on a response of a [custom command](misc.md#custom-commands).
The event data depends on which command was send. Some commands are documented under advanced.

!!! tip

    The interesting part is normally inside `response->body->data`.
    In the example below it means I have enabled the advanced mode.

??? example "Example with the command `getAdvancedMode`"

    ```yaml
    service: vacuum.send_command
    target:
      entity_id: vacuum.YOUR_ROBOT_NAME
    data:
      command: getAdvancedMode
    ```

    When calling the above example you will get the event `deebot_custom_command` similar to:

    ```json
    {
      "event_type": "deebot_custom_command",
      "data": {
        "name": "getAdvancedMode",
        "response": {
          "header": {
            "pri": 1,
            "tzm": 480,
            "ts": "1295442034442",
            "ver": "0.0.1",
            "fwVer": "1.8.2",
            "hwVer": "0.1.1"
          },
          "body": {
            "code": 0,
            "msg": "ok",
            "data": {
              "enable": 1
            }
          }
        }
      },
      "origin": "LOCAL",
      "time_fired": "2021-10-05T21:45:40.294958+00:00",
      "context": {
        "id": "[REMOVED]",
        "parent_id": null,
        "user_id": null
      }
    }
    ```
