---
data_type: json
commands:
  - name: getSpeed
    description: Command to get vacuum power level.
    response:
      arguments:
        speed:
          description: The current vacuum power level.
          <<: &amount_values
            data_values:
              1000: quiet
              0: standard
              1: max
              2: max+
      example: >-
        {
          "speed": 1
        }
  - name: setSpeed
    description: Command to set the vacuum power level.
    request:
      arguments:
        speed:
          description: The vacuum power level
          <<: *amount_values
      example: >-
        {
          "speed": 1
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
