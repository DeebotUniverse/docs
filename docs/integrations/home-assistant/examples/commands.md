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

    Use the app to send the vacuum to a custom area and afterwards search your logs for `Last custom area values (x1,y1,x2,y2):` entries to get the coordinates.
