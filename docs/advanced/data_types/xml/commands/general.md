# Commands

Here only the payload will be described.
More information about sending commands can be found under the respective protocol:

- commands:
  - [REST](../../../protocols/rest.md#request)
  - [XMPP](../../../protocols/xmpp.md#request)
- "broadcast" messages (response only):
  - [MQTT](../../../protocols/mqtt.md#request)

## Request

```xml
<ctl td="[cmdName]" sampleAttribute="[value]" id="[randomid]"/>
```

## Response

```xml
<cmdName sampleAttribute='[value]'/>
```

### Request and response description

- `cmdName`: command name
- `sampleAttribute`: a sample attribute (e.g. `act`)
