---
data_type: json
commands:
  - name: setRelocationState
    description: Locating the position of the bot.
    request:
      arguments:
        mode: "manu"
      example: >-
        {
          "mode": "manu"
        }
---

{% include 'advanced/data_types/commands-template.jinja' %}
