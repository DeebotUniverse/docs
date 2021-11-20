---
data_type: json
commands:
  - name: resetLifeSpan
    description: Command to reset an accessories component.
    request:
      arguments:
        type:
          description: The corresponding value for the component.
          <<: &component_values
            data_values:
              brush: main brush
              sideBrush: side brush
              filter: filter
      example: >-
        {
          "type": "sideBrush"
        }
---

{% include 'advanced/data_types/commands-template.jinja' %}
