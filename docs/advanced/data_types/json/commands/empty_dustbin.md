---
data_type: json
commands:
  - name: setAutoEmpty
    description: Command to control the Auto-Empty Station.
    request:
      arguments:
        act: The action
      example: >-
        {
          "act": "start"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
