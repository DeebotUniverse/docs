# Entities

Here you can find a short description for all entities created by this component.
All exposed entities have the following naming schema:

`[domain].[robot name]_[entity name]`

E.g. `binary_sensor.susi_mop_attached`

!!! info

    Except the **vacuum**  entity, all others are disabled by default.
    You should only enable the required ones.

??? tip "Attributes as entities"

    With [templates](https://www.home-assistant.io/integrations/template/) any attributes can be made as entity.

    Example:

    ```yaml
    template:
      - sensor:
          - name: "Vacuum fan speed"
            state: {{ states.vacuum.YOUR_ROBOT_NAME.attributes['fan_speed'] }}
    ```

## Sensors

| Name                   | Description                               |
| ---------------------- | ----------------------------------------- |
| `last_clean_image`     | A URL to the last success clean           |
| `component_brush`      | % left of main brush                      |
| `component_filter`     | % left of filter                          |
| `component_side_brush` | % left of side brushes                    |
| `stats_area`           | cleaned area of last/current cleaning job |
| `stats_time`           | elapsed time of last/current cleaning job |
| `stats_type`           | type of last/current cleaning job         |
