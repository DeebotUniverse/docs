---
data_type: xml
commands:
  - name: GetBatteryInfo
    description: Command to obtain battery state.
    response:
      arguments:
        "[battery]":
          arguments:
            "[power]":
              description: battery level
              <<: &component_values
                data_values:
                  000-100: percentage of battery remaining
      example: <ctl ret='ok'><battery power='078'/></ctl>
---

{% include 'advanced/data_types/commands-template.jinja2' %}
