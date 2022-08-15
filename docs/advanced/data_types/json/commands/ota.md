---
data_type: json
commands:
  - name: getOta
    description: Command to get information about the over the air update.
    response:
      arguments:
        status:
          description: The status
          data_values:
            idle: Idle
        ver: Firmware version
      example: >-
        {
          "isForce": 0,
          "progress": 0,
          "result": 0,
          "status": "idle",
          "ver": "1.8.2"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
