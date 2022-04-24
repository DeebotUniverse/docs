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

This integration supports also sending "raw" commands to the vacuum.
If your model supports the command and a response will be received, it will be fired with this event.
The event data depends on which command was send.

Some commands are documented under [advanced](../../advanced/data_types/json/commands/).

### Example `getLifeSpan`

To send a custom command, we use the service [`vacuum.send_command`](https://www.home-assistant.io/integrations/vacuum/#service-vacuumsend_command).
From the [`getLifeSpan` documentation](../../advanced/data_types/json/commands/life_span#getlifespan), we get the following information:

- command name is `getLifeSpan`
- the arguments is a list of components from which we want to get the life span.

With the above information, we can write a similar service call:
My vacuum only supports a subset of the documented components.

```yaml
service: vacuum.send_command
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
data:
  command: getLifeSpan
  params:
    - sideBrush
    - brush
    - heap
```

After executing the command the event `deebot_custom_command` is fired will a similar response:

!!! tip

    The interesting part is normally inside `response->body->data`, if data present.

```json
{
  "event_type": "deebot_custom_command",
  "data": {
    "name": "getLifeSpan",
    "response": {
      "header": {
        "pri": 1,
        "tzm": 480,
        "ts": "1312811509056",
        "ver": "0.0.1",
        "fwVer": "1.8.2",
        "hwVer": "0.1.1"
      },
      "body": {
        "code": 0,
        "msg": "ok",
        "data": [
          {
            "type": "sideBrush",
            "left": 2378,
            "total": 9000
          },
          {
            "type": "brush",
            "left": 6569,
            "total": 18000
          },
          {
            "type": "heap",
            "left": 3348,
            "total": 7200
          }
        ]
      }
    }
  },
  "origin": "LOCAL",
  "time_fired": "2022-04-24T22:30:57.187634+00:00",
  "context": {
    "id": "[REMOVED]",
    "parent_id": null,
    "user_id": null
  }
}
```

As specified in the docs, the unit of `left` is minutes, meaning e.g. I can use the brush for another 6569 minutes.
