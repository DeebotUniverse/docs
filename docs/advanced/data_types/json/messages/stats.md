---
data_type: json
messages:
  - name: onStats
    receive:
      - during a cleaning job on each cleaned m²
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
  - name: reportStats
    receive:
      - on the start of a cleaning job
      - on the end (stop) of a cleaning job
    arguments:
      cid: Cleaning job id
      type: Cleaning type
      stop:
        data_values:
          0: Job started
          1: Job finished
      area: The cleaned area in m² [^1]
      time: The cleaning time in seconds [^1]
      start: datetime, when clean job was started [^1]
      content: The map-sub-set (room) ids, which should be cleaned by this job [^1]
      stopReason:
        description: The stop reason [^1]
        data_values:
          1: finished normally
          2: stopped manually
          3: finished with warnings (e.g. one room not cleaned as it was blocked)
    example: >-
      {
        "cid": "1319392469",
        "type": "spotArea",
        "stop": 1,
        "mapCount": 15,
        "area": 0,
        "time": 7,
        "start": "1297811709",
        "content": "7,12,11,14",
        "stopReason": 2
      }
---

{% include 'advanced/data_types/messages-template.jinja2' %}

[^1]: Only present at the end of the cleaning job.
