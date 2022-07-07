---
data_type: xml
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
              dustcaseheap: filter
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
        <ctl ret='ok' type='SideBrush' left='04858' total='9000'/>
        <ctl ret='ok' type='DustCaseHeap' left='03058' total='7200'/>
      additional: >-
        !!! hint

            To calculate the percentage use `left/total`.

{% include 'advanced/data_types/commands-template.jinja2' %}
