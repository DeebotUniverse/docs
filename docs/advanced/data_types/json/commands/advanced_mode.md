---
data_type: json
commands:
  - name: getAdvancedMode
    description: Check if the advanced mode is activated.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setAdvancedMode
    description: Command to enable/disabled the advanced mode.
    request:
      arguments:
        enable: "`1` to enable; `0` to disable"
      <<: *example
---

{% include 'advanced/data_types/commands-template.jinja' %}
