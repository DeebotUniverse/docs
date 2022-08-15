---
data_type: json
commands:
  - name: getMultiMapState
    description: Check if multiple maps are activated
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setMultiMapState
    description: Command to enable/disabled multiple maps.
    request:
      arguments:
        enable: "`1` to enable; `0` to disable"
      <<: *example
---

{% include 'advanced/data_types/commands-template.jinja2' %}
