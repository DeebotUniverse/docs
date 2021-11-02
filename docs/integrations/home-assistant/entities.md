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

!!! info

    The entities are split by their domains. In other words the domain is the header name :wink:

## Binary sensor

| Name           | Description                      |
| -------------- | -------------------------------- |
| `mop_attached` | Specifies if the mop is attached |

## Camera

| Name       | Description                       |
| ---------- | --------------------------------- |
| `live_map` | The live map (similar to the App) |

## Number

| Name     | Description    |
| -------- | -------------- |
| `volume` | Set the volume |

## Select

| Name           | Description                               |
| -------------- | ----------------------------------------- |
| `water_amount` | Set the water amount used during cleaning |

## Sensor

| Name                    | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| `last_cleaning_job`     | Information about the last cleaning. Details [below](#last-cleaning) |
| `last_error`            | Last error Details [below](#last-error)                              |
| `life_span_brush`       | % left of main brush                                                 |
| `life_span_filter`      | % left of filter                                                     |
| `life_span_side_brush`  | % left of side brushes                                               |
| `stats_area`            | cleaned area of last/current cleaning job                            |
| `stats_time`            | elapsed time of last/current cleaning job                            |
| `stats_type`            | type of last/current cleaning job                                    |
| `stats_total_area`      | total cleaned area                                                   |
| `stats_total_time`      | total cleaning time                                                  |
| `stats_total_cleanings` | total cleanings                                                      |

### Last cleaning

- `state`: Holding the status/stop reason
- `attributes`
  - `timestamp`: Timestamp, when the job was started
  - `image_url`: Url to the map image. Hosted on the servers
  - `type`: cleaning type
  - `area`: cleaned area
  - `duration`: duration in minutes

### Last error

- `state`: error code
- `attributes.description`: Description for the error code, if available
