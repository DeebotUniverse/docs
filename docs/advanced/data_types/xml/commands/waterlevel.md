---
data_type: xml
commands:
  - name: GetWaterPermeability
    description: Command to get water level.
    response:
      arguments:
        v:
          description: The amount, which is currently set.
          <<: &amount_values
            data_values:
              1: low
              2: medium
              3: high
              4: ultra high
  - name: SetWaterPermeability
    description: Command to set the water level.
    request:
      arguments:
        v:
          description: The water amount
          <<: *amount_values
---

{% include 'advanced/data_types/commands-template.jinja2' %}
