# Issues

If you have an issue with [Deebot 4 Home Assistant](https://github.com/DeebotUniverse/Deebot-4-Home-Assistant) component, please create a [GitHub Issue](https://github.com/DeebotUniverse/Deebot-4-Home-Assistant/issues/new/choose) and include your Home Assistant logs in the report.
To get full debug output from both the deebot integration and the underlying deebot-client library, place this in your `configuration.yaml` file:

```yaml
logger:
  logs:
    homeassistant.components.vacuum: debug
    custom_components.deebot: debug
    deebot_client: debug
```

More information can be found in the [HA logger documentation](https://www.home-assistant.io/integrations/logger/).

!!! warning

    Doing this will cause your authentication token to visible in your log files.
    Be sure to remove any tokens and other authentication details from your log before posting them in an issue.
