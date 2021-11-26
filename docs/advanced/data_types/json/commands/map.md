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
  - name: getMapSubSet
    description: Command to get map subset information.
    request:
      arguments:
        msid: Map set id
        <<: &arguments
          mid: Map id
          type:
            description: The type of map set
            data_values:
              ar: Rooms
              vw: Virtual walls
              mw: No mopping zones
          mssid: Map subset id [^1]
      example: >-
        {
          "mid": "199390082",
          "msid": "8",
          "type": "ar",
          "mssid": "17"
        }
    response:
      arguments:
        <<: *arguments
        value: List of coordinates
        subtype: Room type [^1]
        connections: Connections to other rooms [^1]
      example: >-
        {
          "type": "ar",
          "mssid": "12",
          "value": "-2700,-7450;-2700,-6750;-2550,-6650;...",
          "subtype": "12",
          "connections": "17,14,10,11,13,7",
          "mid": "199390082"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}

[^1]: Only present when `type` = `ar`
