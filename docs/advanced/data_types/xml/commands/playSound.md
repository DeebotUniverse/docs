---
data_type: xml
commands:
  - name: playSound
    description: Command to play a sound or voice report.
    request:
      arguments:
        sid: The ID of the sound
      additional: >-
        !!! info "Available sound IDs"

            For a list of available sound IDs see
            [here](https://github.com/mrbungle64/ecovacs-deebot.js/wiki/playSound#available-sound-ids)
---

{% include 'advanced/data_types/commands-template.jinja2' %}
