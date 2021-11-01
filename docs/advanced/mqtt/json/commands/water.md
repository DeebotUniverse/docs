# Water commands

## `getWaterInfo`

Command to get water information

### Request

Only the name and the arguments will be described. General information can be found under [Command General](general.md#request)

- Name: `getWaterInfo`
- Arguments: None

### Response

Only the `data` object will be described here.
To get information about the whole response, please refer to [Command General](general.md#response)

```json
{
  "enable": 0,
  "amount": 4
}
```

- `enable`: Indicates if mop is attached. Should be interpreted as boolean.
- `amount`: The amount, which is currently set.
  - `1`: low
  - `2`: medium
  - `3`: high
  - `4`: ultra high

## `setWaterInfo`

Command to set the water amount

### Request

Only the name and the arguments will be described. General information can be found under [Command General](general.md#request)

- Name: `setWaterInfo`
- Arguments:
  - `amount`: The water amount. Available values are specified in [getWaterInfo](#getwaterinfo).

### Response

Please refer to [set commands](general.md#set-commands).
