# Mowing control

!!! attention "Important notice"

    We do not provide support that is the same, equal, or similar to manufacturer support
    because we are in no way affiliated with ECOVACS nor is it sponsored or endorsed by ECOVACS

GOAT mower control currently uses the shared `deebot-client` JSON command names. These names are inherited from the vacuum support in the library, so `clean` means the general work action exposed by the profile. For a mower, integrations may display this as mowing, but the Python and protocol APIs remain named `clean`.

| Model                         | General mowing | Selected-area mowing | Return to charging station |
| ----------------------------- | -------------- | -------------------- | -------------------------- |
| ECOVACS GOAT G1               | `CleanV2`      | `CleanAreaV2`        | `Charge`                   |
| ECOVACS GOAT A1600 RTK        | `CleanV2`      | `CleanAreaV2`        | `Charge`                   |
| ECOVACS GOAT A3000 LiDAR Pro  | `CleanV2`      | `CleanAreaV2`        | `Charge`                   |
| ECOVACS GOAT O500 Panorama    | `CleanV2`      | `CleanAreaV2`        | `Charge`                   |
| ECOVACS GOAT O1200 LiDAR      | `CleanV2`      | Not exposed          | `Charge`                   |

All five reviewed GOAT profiles expose general mowing through `CleanV2`, and use `Charge` to return the mower to the charging station.

The G1, A1600 RTK, A3000 LiDAR Pro and O500 Panorama profiles currently expose `CleanAreaV2`. The current upstream O1200 profile exposes `CleanV2`, but does not expose `CleanAreaV2`.

Absence of `CleanAreaV2` in a hardware profile only means that selected-area mowing is not exposed through that upstream `deebot-client` capability. It must not be interpreted as proof that the physical mower or the ECOVACS app lacks selected-area mowing.
