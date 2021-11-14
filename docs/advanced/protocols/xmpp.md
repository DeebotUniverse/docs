# XMPP

## Request

A command request look in general like:

```xml
<iq id="[id]" to="[toId]@[toType].ecorobot.net/atom" from="[user]@ecouser.net/[toRes]" type="set">
    <query xmlns="com:ctl">
        <ctl td="[cmdName]" sampleAttribute="[value]" id="[randomid]"/>
    </query>
</iq>
```

### Request description

- `id`: id
- `toId`: did of the vacuum
- `toType`: class (model) of vacuum (e.g. `115`)
- `user`: user id given by Ecovacs API
- `toRes`: resource of the vacuum
- `type`: always `set`
- payload (see also data type [XML](../data_types/xml/commands/general.md#request-and-response-description)):
  - `cmdName`: command name
  - `randomid`: somewhat random string with 8 chars

## Response

In general a response looks like:

```xml
<iq from="[toId]@[toType].ecorobot.net/atom" id="[id]" to="[user]@ecouser.net/[resource]" type="set" xmlns:stream="http://etherx.jabber.org/streams">
 <query xmlns="com:ctl">
  <ctl id="[randomid]" ret="ok">
   <cmdName sampleAttribute="[value]"/>
  </ctl>
 </query>
</iq>
```

### Response description

- `toId`: did of the vacuum
- `toType`: class (model) of vacuum (e.g. `115`)
- `user`: user id given by Ecovacs API
- `toRes`: resource of the vacuum
- `type`: always `set`
- `id`: id
- `ret`: status
- `randomid`: random id that was sent (see [Request description](#request-description))
- payload (see also data type [XML](../data_types/xml/commands/general.md#request-and-response-description)):
  - `cmdName`: command that was sent
  - `sampleAttribute`: a sample attribute (e.g. `act`)
