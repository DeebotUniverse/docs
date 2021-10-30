# Setup

## Installation

You can install the integration in two different ways:

### Hacs (Preferred)

1. Install [HACS](https://hacs.xyz)
2. In HACS: Go to Integrations and search and install **Deebot 4 Home Assistant**
3. Restart Home Assistant

### Manual

1. Go to the [integration releases](https://github.com/DeebotUniverse/Deebot-4-Home-Assistant/releases)
2. Download `deebot.zip` and extract into the folder `custom_components` of your Home Assistant instance.
3. Restart Home Assistant

!!! tip

    If possible please use the installation via Hacs, as Hacs will inform you when a new release is available.

## Configuration

1. [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=deebot)

   Click on the button above or go to HA Settings -> Integration -> Add -> Deebot 4 Home Assistant.

2. Configure
   - **Country:** Iso two-letter code. A list can be found [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
   - **Continent:** Iso two-letter code. If your continent code is not working, please fallback to `ww`.

!!! attention "Password"

    There are some issues during the password encoding. Using some special characters (e.g.`, -`) in your password does not work.

!!! info "Chinese server configuration"

    For chinese server username you require "short id" and password. Short id look like "EXXXXXX".
    Don't use your mobile phone number, it won't work.

    Since these servers are in China and unless you are close to China, don't expect very fast response.
