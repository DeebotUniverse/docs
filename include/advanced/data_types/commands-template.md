# Commands template

This template is expecting the following variables:

- `data_type`: The datatype to format the code blocks.
- `commands`: The commands to render. Each command should have the following schema:
  - `name`: command name
  - `description`: command description
  - `request`: _Optional_ The request object
    - `arguments`: Request arguments as dict, currently this two options are supported
      - `[arguments name]`: `[description]`
      - `[arguments name]`:
        - `description`: arguments description
        - `data_values`: _Optional_ Dictionary describing all possible values
        - `arguments`: _Optional_ Arguments dictionary
    - `example`: _Optional_ an example, will be formatted which the provided data_type
    - `additional`: _Optional_ Additional markdown to be rendered
  - `response`: _Optional_ The response object. Same schema as request
