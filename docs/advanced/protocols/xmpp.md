# Commands

This pages describes the general part of the commands.

## Request

A command request look in general like:

```xml
<iq id="[id]" to="[toId]@[toType].ecorobot.net/atom" from="[user]@ecouser.net/[toRes]" type="set">
    <query xmlns="com:ctl">
        <ctl td="[cmdName]" sampleAttribute="value" id="[randomid]"/>
    </query>
</iq>
```

### Request description

- `id`: id
- `toId`: did of the vacuum
- `toType`: class (model) of vacuum (e.g. `115`)
- `user`: user id given by Ecovacs API
- `toRes`: resource of the vacuum
- `type`: `set`
- `ctl`:
  - `cmdName`: command name
  - `randomid`: somewhat random string with 8 chars
