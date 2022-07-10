---
data_type: xml
commands:
  - name: GetChargeState
    description: Command to obtain charge state.
    response:
      arguments:
        "[type]":
          description: charging mode
          <<: &component_values
            data_values:
              SlotCharging: charging
              Going: returning
              Idle: cleaning
      example: <ctl ret='ok'><charge type='Idle'/>
---

{% include 'advanced/data_types/commands-template.jinja2' %}
