# Example commands

## Clean all

```yaml
service: vacuum.start
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
```

## Relocate Robot

```yaml
# Relocate Robot
service: vacuum.send_command
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
data:
  command: relocate
```

## Set fan speed

You can set the value of fan speed with the [generic Vacuum integrations](https://www.home-assistant.io/integrations/vacuum/#service-vacuumset_fan_speed). The available values for fan_speed are: quiet, normal, max, max+.

```yaml
# Set fan speed
service: vacuum.set_fan_speed
data:
  entity_id: vacuum.YOUR_ROBOT_NAME
  fan_speed: quiet
```

## Clean only certain rooms

You can clean certain area by specify it in rooms params, you can find room number under vacuum attributes

```yaml
# Clean Area
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
# Customize Clean
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

## Empty dustbin with auto-empty station

Manually start empting the dustbin, when the robot is docked on a auto-empty station.

```yaml
service: vacuum.send_command
target:
  entity_id: vacuum.YOUR_ROBOT_NAME
data:
  command: setAutoEmpty
  params:
    act: start
```
