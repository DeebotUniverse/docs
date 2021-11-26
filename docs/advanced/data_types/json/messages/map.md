---
data_type: json
messages:
  - name: onMapSet
    receive:
      - on the start of a cleaning job, if there are map set changes
    arguments:
      mid: Map id
      type:
        description: The type of map set
        data_values:
          ar: Rooms
          vw: Virtual walls
          mw: No mopping zones
      msid: Map set id. Only present when `type` = `ar`
      subsets:
        arguments:
          "[subset]":
            description: List of subset
            arguments:
              mssid: Map subset id
    example: >-
      {
        "type": "ar",
        "mid": "199390082",
        "msid": "8",
        "subsets": [
          { "mssid": "7" },
          { "mssid": "12" },
          { "mssid": "17" },
          { "mssid": "14" },
          { "mssid": "10" },
          { "mssid": "11" },
          { "mssid": "13" }
        ]
      }
---

{% include 'advanced/data_types/messages-template.jinja2' %}
