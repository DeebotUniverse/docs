# ECOVACS GOAT mowers

!!! attention "Important notice"

    We do not provide support that is the same, equal, or similar to manufacturer support
    because we are in no way affiliated with ECOVACS nor is it sponsored or endorsed by ECOVACS

`deebot-client` includes initial support for selected ECOVACS GOAT robotic lawn mowers. In the client, GOAT devices are represented as `DeviceType.MOWER`.

The project historically focuses on vacuum cleaners, so some shared Python and protocol APIs still use vacuum-oriented names such as `clean`. For GOAT devices, those shared APIs map to mower actions where the hardware profile exposes them. Integrations built on top of `deebot-client` may choose to present mower-specific wording to users, but the underlying Python and protocol names are not renamed in the documentation.

Model support means that `deebot-client` has a hardware profile and a conservative set of known capabilities for a device. It does not mean that every feature from the ECOVACS app is supported.

- [Supported models](supported-models.md)
- [Mowing control](mowing-control.md)
