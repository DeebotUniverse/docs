# Water commands

## `getWaterInfo`

Command to get water information

### Request

{%
   include-markdown "../../../../../include/advanced/data_types/json/commands/request.md"
%}

- Name: `getWaterInfo`
- Arguments: None

### Response

{%
   include-markdown "../../../../../include/advanced/data_types/json/commands/response.md"
%}

```json
{
  "enable": 0,
  "amount": 4
}
```

- `enable`: Indicates if mop is attached. Should be interpreted as boolean.
- `amount`: The amount, which is currently set.

  {% include-markdown "../../../../../include/advanced/data_types/json/commands/water.md" %}

## `setWaterInfo`

Command to set the water amount

### Request

{%
   include-markdown "../../../../../include/advanced/data_types/json/commands/request.md"
%}

- Name: `setWaterInfo`
- Arguments:

  - `amount`: The water amount. Available values are specified in
    [getWaterInfo](#getwaterinfo).

    {% include-markdown "../../../../../include/advanced/data_types/json/commands/water.md" %}

{%
    include-markdown "../../../../../include/advanced/data_types/execute_command.md"
    heading-offset=2
%}
