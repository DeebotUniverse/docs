# Commands

## Request

Here only the command request object will be described.
More information about sending commands can be found under [api](../../../protocols/rest.md#request).

```json
{
  "header": {
    "pri": "1",
    "ts": 1635497684,
    "tzm": 480,
    "ver": "0.0.50"
  },
  "body": {
    "data": "[args]"
  }
}
```

### Description

- `header`: header object, values are constant except `ts`
  - `ts`: current timestamp
  - `tz`: time zone
  - `ver`: version
- `body`: Missing, when command has no args
  - `data`: object with the command arguments.

## Response

Here only the command response object will be described.
More information about sending commands can be found under [api](../../../protocols/rest.md#response).

{% set description_header = "###" %}
{% include 'advanced/data_types/json/message.md' %}
