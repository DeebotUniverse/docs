---
data_type: json
commands:
  - name: getCarpertPressure
    description: Check if automatically increase fan speed to maximum if carpet is detected, is activated.
    request:
      <<: &typo
        additional: >-
          !!! warning

              The typo in the command is intended as ecovacs as done it, when specifying this command.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setCarpertPressure
    description: Command to enable/disabled to automatically increase fan speed to maximum if carpet is detected.
    request:
      arguments:
        enable: "`1` to enable; `0` to disable"
      <<: *example
      <<: *typo
---

{% include 'advanced/data_types/commands-template.jinja2' %}
