---
data_type: json
commands:
  - name: getSleep
    description: Check if the sleep mode is activated.
    response:
      arguments:
        enable: "`1` if enabled otherwise `0`"
      <<: &example
        example: >-
          {
            "enable": 1
          }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
