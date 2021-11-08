# Water level commands

## `GetWaterPermeability`

Command to get water level

### Request

{%
   include-markdown "../../../../../include/advanced/data_types/xml/commands/request.md"
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
       include-markdown "../../../../../include/advanced/data_types/xml/commands/waterlevel.md"
    %}

## `SetWaterPermeability`

Command to set the water amount

### Request

{%
   include-markdown "../../../../../include/advanced/data_types/xml/commands/request.md"
%}

- Name: `SetWaterPermeability`
- Arguments:

  - `v`: The water amount

    {%
       include-markdown "../../../../../include/advanced/data_types/xml/commands/waterlevel.md"
    %}
