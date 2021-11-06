#### type (mode)

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

#### act (action)

| value | description |
| ----- | ----------- |
| `s`   | start       |
| `p`   | pause       |
| `r`   | resume      |
| `h`   | stop        |
