{% macro list_arguments(arguments, initial_depth=0) -%}
{% for key, object in arguments.items() recursive %}
{%- set description = "" %}
{%- if object is string %}
{%- set description = object %}
{%- elif object is mapping %}
{%- set description = object.description %}
{%- endif %}
{{ "  " * (loop.depth0 + initial_depth) }}- `{{ key }}`: {{ description }}
{%- if object is mapping %}
{%- if object.data_values is defined %}

{{ "  " * (loop.depth0 + initial_depth + 1) }}| Value | Description |
{{ "  " * (loop.depth0 + initial_depth + 1) }}| ----- | ----------- |
{%- for key, value in object.data_values.items() %}
{{ "  " * (loop.depth0 + initial_depth + 1) }}| {{ key }} | {{ value }} |
{%- endfor %}
{% elif object.arguments is defined %}
{{ loop(object.arguments.items()) }}
{%- endif %}
{%- endif %}
{%- endfor %}
{%- endmacro %}



{% macro add_additional(object) -%}
{% if object.additional is defined %}
{{ object.additional }}
{% endif %}
{%- endmacro %}



{% macro example(code, data_type, title="example") %}

!!! example "{{ title }}"

    ```{{ data_type }}
    {{ code | replace("\n","\n    ") }}
    ```

{% endmacro %}