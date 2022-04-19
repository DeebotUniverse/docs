---
data_type: json
commands:
  - name: getLifeSpan
    description: Command to get information about accessories components.
    request:
      arguments:
        "[component]":
          description: A list with corresponding value for the components. Multiple values possible
          <<: &component_values
            data_values:
              brush: main brush
              sideBrush: side brush
              heap: filter
              unitCare: other components [^1]
              dModule: unknown [^1]
      example: >-
        [
          "sideBrush",
          "brush",
          "heap"
        ]
    response:
      arguments:
        "[result]":
          description: A list with a result object for each requested component.
          arguments:
            <<: &component_type
              type:
                description: The corresponding value for the component.
                <<: *component_values
            left: Remaining lifetime in minutes
            total: Total lifetime in minutes
      example: >-
        [
          { "type": "sideBrush", "left": 0, "total": 9000 },
          { "type": "brush", "left": 10873, "total": 18000 },
          { "type": "heap", "left": 73, "total": 7200 }
        ]
      additional: >-
        !!! hint

            To calculate the percentage use `left/total`.

  - name: resetLifeSpan
    description: Command to reset an accessories component.
    request:
      arguments:
        <<: *component_type
      example: >-
        {
          "type": "sideBrush"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}

[^1]: Only available for some newer models (e.g. T8/T9 series)
