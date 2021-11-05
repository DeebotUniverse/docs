# Map commands

## `getCachedMapInfo`

Command to get information about the maps.

### Request

Only the name and the arguments will be described. General information can be found under [Command General](general.md#request)

- Name: `getCachedMapInfo`
- Arguments: None

### Response

Only the `data` object will be described here.
To get information about the whole response, please refer to [Command General](general.md#response)

```json
{
  "enable": 1,
  "info": [
    {
      "mid": "199390082",
      "index": 0,
      "status": 1,
      "using": 1,
      "built": 1,
      "name": "Erdgeschoss"
    },
    {
      "mid": "722607162",
      "index": 3,
      "status": 0,
      "using": 0,
      "built": 0,
      "name": ""
    }
  ]
}
```

- `info`: A list of map objects
  - `mid`: Map id
  - `index`: internal index
  - `using`: `1` means currently used map. Otherwise `0`
  - `built`: `1` means map is built; Complete clean was done and bot returned successfully to charging station
  - `name`: Name of map set by the user
