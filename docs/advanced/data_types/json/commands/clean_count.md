---
data_type: json
commands:
  - name: getCleanCount
    description: Get the permanently stored setting for number of cleaning cycles for auto clean.
    response:
      arguments:
        count: the number of cleanings
      <<: &example
        example: >-
          {
            "count": 2
          }
  - name: setCleanCount
    description: Command to set the number of cleaning cycles for auto clean (permanently stored).
    request:
      arguments:
        count: the number of cleanings
      <<: *example
---

{% include 'advanced/data_types/commands-template.jinja2' %}
