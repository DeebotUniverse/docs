# UI advanced example

Main feature is ability to specify via UI the order of the cleaned rooms.
Thanks to @aidbish for the initial idea.

![Preview](../../../../assets/images/ui-advanced.gif)

## Setup

For this setup to work, you need some custom components (all available via HACS)

- [Variables](https://github.com/Wibias/hass-variables)
- [Vacuum-card](https://github.com/denysdovhan/vacuum-card)
- [Button-card](https://github.com/custom-cards/button-card)

## Configuration

This example needs also a backend configuration for the templates and scripts.
My vacuum has the name _"susi"_, please change it accordingly.

## Backend (configuration.yaml)

```yaml
script:
  deebot_clean:
    description: Start a deebot cleaning task
    variables:
      # The queue variable
      queue: variable.deebot_susi_queue
      vacuum_bot: vacuum.susi
    sequence:
      - alias: Get room numbers
        variables:
          # See for appending to list
          # https://github.com/home-assistant/core/issues/33678#issuecomment-609424851
          rooms: >-
            {%- set queue_split = states(queue).split(",") -%}
            {%- set rooms = state_attr(vacuum_bot, "rooms")-%}
            {%- set data = namespace(rooms=[]) -%}
            {%- for room_name in queue_split -%}
              {%- set data.rooms = data.rooms + [rooms[room_name]] -%}
            {%- endfor -%}
            {{ data.rooms | join(",") }}
      - alias: Send cleaning job to vacuum
        service: vacuum.send_command
        data:
          entity_id: "{{ vacuum_bot }}"
          command: spot_area
          params:
            rooms: "{{ rooms }}"
            cleanings: 1

  deebot_room_queue:
    description: Add/Remove a room from the queue
    fields:
      queue:
        description: The queue variable
        example: deebot_susi_queue
      room:
        description: Room, which should be removed or added
        example: kitchen
    sequence:
      - service: variable.set_variable
        data:
          variable: "{{ queue }}"
          value: >-
            {%- set queue = states("variable.deebot_susi_queue").split(",") -%}
            {%- if states("variable.deebot_susi_queue") | length == 0 -%}
              {{ room }}
            {%- elif room in queue -%}
              {{ queue | reject("eq", room) | list | join(",")}}
            {%- else -%}
              {{ (queue + [room]) | join(",") }}
            {%- endif -%}

recorder:
  exclude:
    entities:
      - variable.deebot_susi_queue
      - script.deebot_room_queue
    entity_globs:
      - sensor.deebot_susi_queue_*

variable:
  deebot_susi_queue:
    name: Susi Raum Reihenfolge
    value: ""
    restore: false

# Room name comes from the integration to match attribute names
template:
  unique_id: deebot_susi_queue
  trigger:
    - platform: homeassistant
      event: start
    - platform: state
      entity_id: variable.deebot_susi_queue
  sensor:
    # Add for each room the following. Change "living_room" accordingly
    - unique_id: deebot_susi_queue_living_room
      name: deebot_susi_queue_living_room
      state: >
        {% set queue = trigger.to_state.state.split(",") if trigger.to_state is defined else "" %}
        {{ queue.index('living_room')+1 if 'living_room' in queue else 0 }}
```

### UI configuration

```yaml
type: vertical-stack
cards:
  - type: custom:vacuum-card
    entity: vacuum.susi
    stats:
      default:
        - entity_id: sensor.susi_life_span_brush
          unit: "%"
          subtitle: Hauptbürste
        - entity_id: sensor.susi_life_span_side_brush
          unit: "%"
          subtitle: Seitenbürsten
        - entity_id: sensor.susi_life_span_filter
          unit: "%"
          subtitle: Filter
      cleaning:
        - entity_id: sensor.susi_stats_area
          unit: m²
          subtitle: Geputzte Fläche
        - entity_id: sensor.susi_stats_time
          unit: Minuten
          subtitle: Reinigungsdauer
    show_status: true
    show_toolbar: true
    compact_view: false
    image: /local/deebot950.svg
  - type: custom:button-card
    color: auto-no-temperature
    name: Räume zum Putzen auswählen
    styles:
      card:
        - font-size: 18px
        - height: 30px
      name:
        - color: var(--primary-color)
  - type: horizontal-stack
    cards:
      # Add the following chard for each room. Change room values accordingly
      - type: custom:button-card
        entity: sensor.deebot_susi_queue_living_room
        icon: mdi:sofa
        name: Wohnzimmer
        state:
          - styles:
              card:
                - background-color: var(--primary-color)
            operator: ">="
            value: 1
        styles:
          card:
            - font-size: 12px
          grid:
            - position: relative
          custom_fields:
            notification:
              - display: |
                  [[[
                    if (entity.state == "0")
                      return "none";
                    return "block";
                  ]]]
              - position: absolute
              - right: 5%
              - top: 5%
              - height: 20px
              - width: 20px
              - font-size: 20px
              - font-weight: bold
              - line-height: 20px
        custom_fields:
          notification: |
            [[[ return entity.state ]]]
        tap_action:
          action: call-service
          service: script.deebot_room_queue
          service_data:
            queue: deebot_susi_queue
            room: living_room
```
