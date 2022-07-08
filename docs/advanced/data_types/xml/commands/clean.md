---
data_type: xml
commands:
  - name: Clean
    description: Command to start a cleaning.
    request:
      arguments:
        "[clean]":
          arguments:
            "[type]":
              description: clean mode
			  <<: &component_values
                data_values:
                  auto: auto clean
                  border: border clean [^1]
                  spot: spot clean [^1]
                  SpotArea: spot area and custom area clean [^2]
                  singleroom: single room clean [^3]
                  stop: stop
            "[act]":
              description: clean action
			  <<: &component_values
                data_values:
                  s: start
                  p: pause [^4]
                  r: resume
                  h: stop
            "[speed]":
              description: vacuum power
			  <<: &component_values
                data_values:
                  standard: standard
                  strong: max
      additional: >-
        !!! info

            `speed` is only necessary for a few models (e.g. Deebot 710 series)
---

{% include 'advanced/data_types/commands-template.jinja2' %}

[^1]: Models without mapping functionality only
[^2]: Models with mapping functionality only
[^3]: Models with single room cleaning mode only
[^4]: Spot and border modes cannot be paused, they can only be stopped.
