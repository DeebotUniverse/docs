---
data_type: xml
commands:
  - name: getCleanSpeed
    description: Command to get vacuum power level.
    response:
      arguments:
        speed:
          description: The current vacuum power level.
          <<: data_values
            data_values:
              standart: standart
              strong: strong
      example: >-
        <ctl ret='ok' speed='standard'/>
  - name: setCleanSpeed
    description: Command to set the vacuum power level.
    request:
      arguments:
        speed:
          description: The vacuum power level
          <<: data_values
            data_values:
              standart: standart
              strong: strong
      example: >-
        <ctl speed="standard" />
---

{% include 'advanced/data_types/commands-template.jinja2' %}
