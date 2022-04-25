---
data_type: json
commands:
  - name: getAutoEmpty
    description: Check if the auto empty mode for the Auto Empty Station is activated.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
  - name: setAutoEmpty
    description: Command to set the auto empty mode (permanently stored) or to manually empty dust bin.
    request:
      arguments:
        enable: "`1` to enable; `0` to disable emptying dustbin after a cleaning job" 
        act: "`start` for manual emptying the dust bin"
      example: >-
        {
          "act": "start"
        }
      additional: >-
        !!! warning

          The arguments are exclusive, meaning you can only specify one at the time!
---

{% include 'advanced/data_types/commands-template.jinja2' %}
