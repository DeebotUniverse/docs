---
data_type: xml
commands:
  - name: GetCleanSpeed
    description: Command to get vacuum power.
    response:
      arguments:
        speed:
          description: The vacuum power, which is currently set.
          <<: &amount_values
            data_values:
              standard: standard
              strong: max
  - name: SetCleanSpeed
    description: Command to set the vacuum power.
    request:
      arguments:
        speed:
          description: The vacuum power
          <<: *amount_values
---

{% include 'advanced/data_types/commands-template.jinja2' %}
