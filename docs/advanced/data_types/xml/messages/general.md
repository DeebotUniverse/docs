# Messages

A message looks like:

```xml
<ctl ts='[timestamp]' td='[command]'>
    <playload sampleAttribute='value'/>
</ctl>
```

??? example "XML example with `CleanReport` message"

    This example message was published on `iot/atr/CleanReport/[did]/[class]/[resource]/x` for a Deebot 901 device.

    ```xml
    <ctl ts='1647080016429' td='CleanReport'>
        <clean type='auto' speed='standard' st='h' rsn='a' a='' l='' sts=''/>
    </ctl>
    ```
