# Migration from [And3rsL/Deebot-for-Home-Assistant](https://github.com/And3rsL/Deebot-for-Home-Assistant)

Unfortunately Andrea is not any more active and I don't have the required privileges to do certain changes.
So I decided to fork the project under a new organization [DeebotUniverse](https://github.com/DeebotUniverse).

!!! warning

    Please read the complete migration until the end before performing some actions.

## Breaking changes

### Camera

The live map was renamed to have a consistent naming schema.

`camera.RBOTNAME_livemap` -> `camera.RBOTNAME_live_map`

### Last cleaning

In the old component only the image of the last cleaning job was available.
The new sensor [last_cleaning](entities.md#last-cleaning) has a lot more information.
The image url can be found as attribute of the new sensor `last_cleaning`.

### Life span sensors

Life span sensor are renamed to group them together:

- `sensor.ROBOTNAME_brush` -> `sensor.ROBOTNAME_life_span_brush`
- `sensor.ROBOTNAME_heap` -> `sensor.ROBOTNAME_life_span_filter`
- `sensor.ROBOTNAME_sidebrush` -> `sensor.ROBOTNAME_life_span_side_brush`

### Vacuum room attributes

Room attributes are now group under one attribute `rooms`.

<table>
  <thead>
     <tr>
        <th>Before</th>
        <th>After</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td>
           ```yaml
           room_living_room: 7
           room_bedroom: 17
           room_bathroom: 14
           room_kitchen: 11
           ```
        </td>
        <td>
           ```yaml
           rooms:
             living_room: 7
             bedroom: 17
             bathroom: 14
             kitchen: 11
           ```
        </td>
     </tr>
  </tbody>
</table>

### Water amount

The water amount (old level) is now available as select entity. Made it easy to know all available values and change it directly in the UI.

`sensor.ROBOTNAME_water_level` -> `select.ROBOTNAME_water_amount`

### Removed

- `sensor.ROBOTNAME_stats_start`: The start time can be identified via Home Assistant when the vacuum change state. Also in some cases the start time had a random time zone, so it was not really helpful.
- `sensor.ROBOTNAME_stats_cid`: The id on the stats command is different from the id of the same cleaning job on the rest of the commands.

Please use the new event [deebot_cleaning_job](events.md#deebot_cleaning_job) instead.

## Steps

!!! note

    At least Home Assistant `2021.11.0` is required to use the integration, because entity categories are introduced in that version.

1. Verify that you are running at least HA `2021.11.0`. If not please update first
2. Remove all configuration of _Deebot for Home Assistant_
3. Uninstall _Deebot **for** Home Assistant_ (via Hacs)
4. Install _Deebot **4** Home Assistant_ (via Hacs)
5. Restart Home Assistant
6. Start adding all config entries again
