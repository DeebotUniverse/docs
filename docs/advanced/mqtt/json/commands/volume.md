# Volume commands

## `getVolume`

Command to get information about the volume

### Request

Only the name and the arguments will be described. General information can be found under [Command General](general.md#request)

- Name: `getVolume`
- Arguments: None

### Response

Only the `data` object will be described here.
To get information about the whole response, please refer to [Command General](general.md#response)

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

Only the name and the arguments will be described. General information can be found under [Command General](general.md#request)

- Name: `setVolume`
- Arguments:
  - `volume`: The level to set the volume
  - `total`: The maximum supported level

!!! danger

    Only set the argument `total`to the value received from the command `getVolume`.

### Response

Please refer to [set commands](general.md#set-commands).
