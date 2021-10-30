# Services

The integration adds the following services:

## `deebot.refresh`

Service to manually refresh parts of the vacuum.

Parameters:

- `service`: `deebot.refresh`
- `target.entity_id`: Entity id of vacuum
- `data.part`: Part, which should be refreshed. Following are supported:
  - Status
  - Error
  - Fan speed
  - Clean logs
  - Water
  - Battery
  - Stats
  - Life spans
  - Rooms
  - Map

??? example

    ```yaml
    service: deebot.refresh
    data:
      part: Status
    target:
      entity_id: vacuum.YOUR_ROBOT_NAME
    ```
