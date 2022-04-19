---
data_type: json
commands:
  - name: getTrueDetect
    description: Check if "TrueDetect 3D" is activated.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setTrueDetect
    description: Command to enable/disable the "TrueDetect 3D" mode.
    request:
      arguments:
        enable: "`1` to enable; `0` to disable"
      <<: *example
---

{% include 'advanced/data_types/commands-template.jinja2' %}
