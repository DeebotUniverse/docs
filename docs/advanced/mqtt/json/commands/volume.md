# Volume commands

## `getVolume`

Command to get information about the volume

### Request

{%
   include-markdown "../../../../../include/advanced/mqtt/json/commands/request.md"
%}

- Name: `getVolume`
- Arguments: None

### Response

{%
   include-markdown "../../../../../include/advanced/mqtt/json/commands/response.md"
%}

```json
{
  "total": 10,
  "volume": 10
}
```

- `total`: The maximum supported level
- `volume`: The current set level

## `setVolume`

Command to set volume

### Request

{%
   include-markdown "../../../../../include/advanced/mqtt/json/commands/request.md"
%}

- Name: `setVolume`
- Arguments:
  - `volume`: The level to set the volume

{%
    include-markdown "../../../../../include/advanced/mqtt/json/commands/execute/response.md"
    heading-offset=2
%}
