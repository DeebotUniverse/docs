# Example commands

All `vacuum` services offered by Home Assistant are described in their [docs](https://www.home-assistant.io/integrations/vacuum/#component-services).

Below some more advanced examples:

## Relocate Robot

```yaml
service: vacuum.send_command
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
data:
  command: relocate
```

## Clean only certain rooms

You can clean certain area by specify it in rooms params, you can find room number under vacuum attributes

```yaml
service: vacuum.send_command
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
data:
  command: spot_area
  params:
    rooms: 10,14
    cleanings: 1
```

## Clean custom area

```yaml
service: vacuum.send_command
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
data:
  command: custom_area
  params:
    coordinates: -1339,-1511,296,-2587
```

!!! tip

    To find out the correct coordinates use the following steps:

    1. Use the app to send the vacuum to a custom area
    2. Use the dev tools to listen for the event `deebot_cleaning_job`, which will be fired at the start/end of a cleaning job
    3. At the end of the job you can find your coordinates under `data->content`

    Also the coordinates will be logged on `debug`. After activating debug logs, you can search your logs for `Last custom area values (x1,y1,x2,y2):` to get the coordinates.

## Custom commands

!!! warning "Only for advanced users"

    The reason for this use case is only to give advanced users the possibility to
    try/use a command, which is not implemented yet.

More information can be found under [deebot_custom_command](../events.md#deebotcustomcommand)
