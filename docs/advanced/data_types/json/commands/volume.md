---
data_type: json
commands:
  - name: getVolume
    description: Command to get information about the volume.
    response:
      arguments:
        total: The maximum supported level
        volume: The current set level
      example: >-
        {
          "total": 10,
          "volume": 10
        }
  - name: setVolume
    description: Command to set the volume.
    request:
      arguments:
        volume: The level to set the volume to it
      example: >-
        {
          "volume": 10
        }
---

{% include 'advanced/data_types/commands-template-jinja.md' %}
