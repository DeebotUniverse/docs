## Messages

A message looks like:

<!--message-object-->

```json
{
  "header": {
    "pri": 1,
    "tzm": 480,
    "ts": "1297811721698",
    "ver": "0.0.1",
    "fwVer": "1.8.2",
    "hwVer": "0.1.1"
  },
  "body": {
    "data": "[data]"
  }
}
```

## Description

- `header`
  - `ts`: timestamp
  - `ver`: protocol version
  - `fwVer`: firmware version
  - `hwVer`: hardware version
- `body`
  - `data`: Holding the actual data. See specific description

<!--message-object-end-->
