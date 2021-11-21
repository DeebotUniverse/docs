---
data_type: json
commands:
  - name: getBreakPoint
    description: Check if continuous cleaning is activated.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setBreakPoint
    description: Command to enable/disabled continuous cleaning.
    request:
      arguments:
        enable: "`1` to enable; `0` to disable"
      <<: *example
---

{% include 'advanced/data_types/commands-template.jinja2' %}
