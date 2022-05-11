---
data_type: json
commands:
  - name: getNetInfo
    description: Command to get some network related information.
    response:
      arguments:
        ip: The ip address of the robot
        mac: The mac address of the robot
        ssid: the service set identifier (network name) of the Wi-Fi
        rssi: the received signal strength indication (signal strength)
      example: >-
        {
          "ip": "192.168.0.88",
          "mac": "00:80:41:AE:FD:7E",
          "ssid": "someRandomNetworkName",
          "rssi": "-62"
        }
---

{% include 'advanced/data_types/commands-template.jinja2' %}
