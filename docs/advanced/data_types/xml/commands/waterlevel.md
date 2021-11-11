# Water level commands

## `GetWaterPermeability`

Command to get water level

### Request

Only the name and the arguments will be described.

- Name: `GetWaterPermeability`
- Arguments: None

### Response

Only the payload will be described here

```json
{
  "v": 4
}
```

- `v`: The amount, which is currently set

  | Value | Description |
  | ----- | ----------- |
  | 1     | low         |
  | 2     | medium      |
  | 3     | high        |
  | 4     | ultra high  |

## `SetWaterPermeability`

Command to set the water amount

### Request

Only the name and the arguments will be described.

- Name: `SetWaterPermeability`
- Arguments:

  - `v`: The water amount

    | Value | Description |
    | ----- | ----------- |
    | 1     | low         |
    | 2     | medium      |
    | 3     | high        |
    | 4     | ultra high  |
