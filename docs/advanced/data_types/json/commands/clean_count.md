---
data_type: json
commands:
  - name: getCleanCount
    description: Get the persistent value for clean count.
    response:
      arguments:
        count: the number of cleanings
      <<: &example
        example: >-
          {
            "count": 2
          }
  - name: setCleanCount
    description: Command to set the persistent value for clean count.
    request:
      arguments:
        count: the number of cleanings
      <<: *example
---

{% include 'advanced/data_types/commands-template.jinja2' %}
