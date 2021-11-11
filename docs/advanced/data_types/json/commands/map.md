---
data_type: json
commands:
  - name: getCachedMapInfo
    description: Command to get information about all maps.
    response:
      arguments:
        info:
          description: A list of map objects
          arguments:
            mid: Map id
            index: internal index
            using: "`1` means currently used map. Otherwise `0`"
            built: "`1` means map is built; Complete clean was done and bot returned successfully to charging station"
            name: Name of map set by the user
      example: >-
        {
          "enable": 1,
          "info": [
            {
              "mid": "199390082",
              "index": 0,
              "status": 1,
              "using": 1,
              "built": 1,
              "name": "Erdgeschoss"
            },
            {
              "mid": "722607162",
              "index": 3,
              "status": 0,
              "using": 0,
              "built": 0,
              "name": ""
            }
          ]
        }
---

{% include 'advanced/data_types/commands-template-jinja.md' %}
