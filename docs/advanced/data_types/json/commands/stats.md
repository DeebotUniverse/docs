---
data_type: json
commands:
  - name: getStats
    description: Command to get information about the last or ongoing cleaning job.
    response:
      arguments:
        area: The cleaned area in m²
        time: The elapsed time since starting this job in seconds
        cid: Cleaning id
        start: Datetime, when clean job was started
        type: The cleaning type
      example: >-
        {
          "area": 36,
          "time": 2063,
          "cid": "111",
          "start": "1297462509",
          "type": "spotArea"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
