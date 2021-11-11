---
data_type: json
commands:
  - name: getWaterInfo
    description: Command to get water information.
    response:
      arguments:
        enable: Indicates if mop is attached. Should be interpreted as boolean.
        amount:
          description: The amount, which is currently set.
          <<: &amount_values
            data_values:
              1: low
              2: medium
              3: high
              4: ultra high
      example: >-
        {
          "enable": 0,
          "amount": 4
        }
  - name: setWaterInfo
    description: Command to set the water amount.
    request:
      arguments:
        amount:
          description: The water amount
          <<: *amount_values
      example: >-
        {
          "amount": 4
        }
---

{% include 'advanced/data_types/commands-template.jinja' %}
