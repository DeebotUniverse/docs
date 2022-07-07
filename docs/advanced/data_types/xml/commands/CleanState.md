---

data_type: xml
commands:

- name: getCleanState
  description: Command to get information about clean state.
  response:
  arguments:
  "[clean]":
  description: A list with a result object for each requested component.
  arguments:
  <<: &component_type
  speed:
  description: The corresponding value for the component.
  <<: *component_values
  strong: max force of vacuum
  auto: min force of vacuum
  <<: &component_type
  type:
  description: The corresponding value for the component.
  <<:*component_values
  auto: auto clean
  border: border clean
  spot: spot clean
  <<: &component_type
  st:
  description: The corresponding value for the component.
  <<: *component_values
  p: pause
  h: stop
  s: start
  <<: &component_type
  mode:
  description: The corresponding value for the component.
  <<:*component_values
  R: unknown  
   <<: &component_type
  t and a:
  description: unknown.
  <<: \*component_values
  int: unknown

          example: >-
            [
              <clean type='auto' speed='standard' st='h' mode='R' t='100' a='100'/>
            ]

  {% include 'advanced/data_types/commands-template.jinja2' %}
