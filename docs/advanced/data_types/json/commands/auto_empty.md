---
data_type: json
commands:
  - name: getAutoEmpty
    description: Check if the auto empty mode is activated.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setAutoEmpty
    description: Command to set the auto empty mode (permanently stored).
    request:
      arguments:
        enable: "`1` to enable; `0` to disable"
      <<: *example
  - name: setAutoEmpty
    description: Command to directly empty the dustbin to the Auto-Empty Station.
    request:
      arguments:
        act: "`start` for directly empty the dustbin"
      example: >-
        {
          "act": "start"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
