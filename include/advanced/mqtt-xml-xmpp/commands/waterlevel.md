# Water level commands

## `GetWaterPermeability`

Command to get water level

### Request

{%
   include-markdown "./request.md"
%}

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

{%
include-markdown "../reference/waterlevel-modes.md"
%}

## `SetWaterPermeability`

Command to set the water amount

### Request

{%
include-markdown "./request.md"
%}

- Name: `SetWaterPermeability`
- Arguments:
  - `v`: The water amount

{%
include-markdown "../reference/waterlevel-modes.md"
%}
