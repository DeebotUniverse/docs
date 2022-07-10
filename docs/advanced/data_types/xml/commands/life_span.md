---
data_type: XML
commands:
  - name: GetLifeSpan
    description: Command to get information about accessories components.
    request:
      arguments:
        "[type]":
          description: A list with corresponding value for the components.
          <<: &component_values
            data_values:
              Brush: main brush
              SideBrush: side brush
              DustCaseHeap: filter

      example: >-
        <ctl type="Brush" />
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

        <ctl ret='ok' type='Brush' left='13858' total='18000'/>

      additional: >-
        !!! hint

            To calculate the percentage use `left/total`.
---

{% include 'advanced/data_types/commands-template.jinja2' %}
