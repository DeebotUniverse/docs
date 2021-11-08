# Clean command

## `Clean`

Command to start a cleaning

### Request

{%
   include-markdown "../../../../../include/advanced/data_types/xml/commands/request.md"
%}

- Name: `Clean`
- Arguments:
  - `clean`:
    - `type`: [clean mode](#clean-mode)
    - `act`: [clean action](#clean-action)

#### Clean mode

| value        | description                          |
| ------------ | ------------------------------------ |
| `auto`       | auto clean                           |
| `border`     | border clean [^1]                    |
| `spot`       | spot clean [^1]                      |
| `SpotArea`   | spot area and custom area clean [^2] |
| `singleroom` | single room clean [^3]               |
| `stop`       | stop                                 |

[^1]: Models without mapping functionality only
[^2]: Models with mapping functionality only
[^3]: Models with single room cleaning mode only

#### Clean action

| value | description |
| ----- | ----------- |
| `s`   | start       |
| `p`   | pause       |
| `r`   | resume      |
| `h`   | stop        |
