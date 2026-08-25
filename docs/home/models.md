# Model support

!!! attention "Important notice"

    We do not provide support that is the same, equal, or similar to manufacturer support
    because we are in no way affiliated with ECOVACS nor is it sponsored or endorsed by ECOVACS

## :material-language-python: deebot-client

Used by [Deebot for Home Assistant](https://github.com/DeebotUniverse/Deebot-4-Home-Assistant)

### Vacuum cleaners

| Model                   |              status              | Protocol  | Data type |
| ----------------------- | :------------------------------: | --------- | --------- |
| Deebot OZMO 920         |         :material-check:         | REST/MQTT | JSON      |
| Deebot OZMO 950         | :fontawesome-solid-check-double: | REST/MQTT | JSON      |
| Deebot OZMO T5          |         :material-check:         | REST/MQTT | JSON      |
| Deebot (OZMO) T8 series |         :material-check:         | REST/MQTT | JSON      |
| Deebot T9 series        |         :material-check:         | REST/MQTT | JSON      |
| Deebot N8 series        |         :material-check:         | REST/MQTT | JSON      |
| Deebot U2 series        |                                  | REST/MQTT | JSON      |
| Deebot X1 Omni          |    :material-progress-check:     | REST/MQTT | JSON      |

### ECOVACS GOAT mowers

The following mower entries have dedicated upstream `deebot-client` hardware profiles. They are listed without a status icon because the existing status legend does not describe mower feature coverage precisely. The hardware profiles verify JSON as the data type.

| Model                         | Hardware ID | Device type        | Data type |
| ----------------------------- | ----------- | ------------------ | --------- |
| ECOVACS GOAT G1               | `5xu9h3`    | `DeviceType.MOWER` | JSON      |
| ECOVACS GOAT A1600 RTK        | `xmp9ds`    | `DeviceType.MOWER` | JSON      |
| ECOVACS GOAT A3000 LiDAR Pro  | `51rcxt`    | `DeviceType.MOWER` | JSON      |
| ECOVACS GOAT O500 Panorama    | `300lc5`    | `DeviceType.MOWER` | JSON      |
| ECOVACS GOAT O1200 LiDAR      | `2i0fns`    | `DeviceType.MOWER` | JSON      |

See [GOAT mower support](../goat/index.md) for the conservative mower capability notes.

## :material-language-javascript: ecovacs-deebot.js

Used by [Ecovacs Deebot adapter](https://github.com/mrbungle64/ioBroker.ecovacs-deebot) and [various others](projects.md#ecovacs-deebotjs)

| Model                   |              status              | Protocol  | Data type |
| ----------------------- | :------------------------------: | --------- | --------- |
| Deebot 500/501          |         :material-check:         |           |           |
| Deebot 600/601/605      |         :material-check:         | REST/MQTT | XML       |
| Deebot 710/711/711s     |         :material-check:         | REST/MQTT | XML       |
| Deebot 900/901          | :fontawesome-solid-check-double: | REST/MQTT | XML       |
| Deebot OZMO Slim 10/11  |         :material-check:         | REST/MQTT | XML       |
| Deebot OZMO 610         |         :material-check:         | XMPP      | XML       |
| Deebot OZMO 900/905     |         :material-check:         | REST/MQTT | XML       |
| Deebot OZMO 920         | :fontawesome-solid-check-double: | REST/MQTT | JSON      |
| Deebot OZMO 930         | :fontawesome-solid-check-double: | XMPP      | XML       |
| Deebot OZMO 950         | :fontawesome-solid-check-double: | REST/MQTT | JSON      |
| Deebot OZMO T5          |         :material-check:         | REST/MQTT | JSON      |
| Deebot (OZMO) T8 series |         :material-check:         | REST/MQTT | JSON      |
| Deebot T9 series        |         :material-check:         | REST/MQTT | JSON      |
| Deebot M88              |         :material-check:         | XMPP      | XML       |
| Deebot N8 series        |         :material-check:         | REST/MQTT | JSON      |
| Deebot N79 series       |         :material-check:         | XMPP      | XML       |
| Deebot U2 series        |    :material-progress-check:     | REST/MQTT | JSON      |
| Deebot Slim 2           | :fontawesome-solid-check-double: | XMPP      | XML       |
| Deebot X1 Omni          |         :material-check:         | REST/MQTT | JSON      |

## Legend

| Icon                             | Description                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| :fontawesome-solid-check-double: | Confirmed to work flawlessly and at least one of the main developers owns such a device |
| :material-check:                 | Confirmed to work properly                                                              |
| :material-progress-check:        | Confirmed to work partially                                                             |
| :material-close:                 | Currently no support                                                                    |
|                                  | No status or info available. Feedback is welcome                                        |
