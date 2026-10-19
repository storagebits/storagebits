<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="François Lesage, storagebits, Montréal. I build at night, with AI agents, on real hardware. Today's moon and Montréal's sunrise and sunset, regenerated every morning.">
</picture>

<p>
  <a href="https://blok.storagebits.workers.dev"><img src="https://img.shields.io/badge/blog-blok-E89E5C?style=flat-square&labelColor=0E0D0B" alt="Blog: blok"></a>
  <a href="https://github.com/algotitanhq"><img src="https://img.shields.io/badge/company-ALGOTITAN-F2B35B?style=flat-square&labelColor=0E0D0B" alt="ALGOTITAN on GitHub"></a>
  <a href="https://x.com/storagebits"><img src="https://img.shields.io/badge/X-@storagebits-F2EDE4?style=flat-square&labelColor=0E0D0B" alt="X: @storagebits"></a>
</p>

Firmware, TV apps, embedded kernels and a homelab, built with AI agents and tested on the real device.
Since October 2026 the agents work as a company, **[ALGOTITAN](https://github.com/algotitanhq)**; its public repos sit next to mine below.

> [!NOTE]
> Every project here is built with AI agents, and its README says so. I set the direction, test on the hardware and approve what ships; the agents write most of the code.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-repos-dark.svg">
  <img src="assets/section-repos-light.svg" width="100%" alt="01, repositories: code that runs on real hardware">
</picture>

| Project | What it is | Status |
|---|---|---|
| **[Kronograf](https://github.com/storagebits/kronograf)**<br><sub>ESP32 · C · LVGL</sub> | A from-scratch firmware for the LilyGO T-Watch 2020: aviator chronograph, *Back to the Future* time circuits, iPhone notifications over BLE, live buses, a network toolbox, and a macOS simulator. | [![CI](https://img.shields.io/github/actions/workflow/status/storagebits/kronograf/ci.yml?style=flat-square&label=CI&labelColor=0E0D0B)](https://github.com/storagebits/kronograf/actions/workflows/ci.yml)<br>[![release](https://img.shields.io/github/v/release/storagebits/kronograf?include_prereleases&style=flat-square&color=E89E5C&labelColor=0E0D0B)](https://github.com/storagebits/kronograf/releases) |
| **[Almanak](https://github.com/algotitanhq/almanak)**<br><sub>Android TV · Kotlin · Compose</sub> | An ambient almanac for Android TV, made to be left on: time, weather, the next bus in real time, sun and moon, a generative sky. Open data, no account. | [![CI](https://img.shields.io/github/actions/workflow/status/algotitanhq/almanak/ci.yml?style=flat-square&label=CI&labelColor=0E0D0B)](https://github.com/algotitanhq/almanak/actions/workflows/ci.yml)<br>![license](https://img.shields.io/badge/license-MIT-F2EDE4?style=flat-square&labelColor=0E0D0B) |
| **[Humility](https://github.com/storagebits/humility)**<br><sub>Rust · STM32</sub> | Fork of Oxide's Hubris debugger, used to bring Hubris up on a NUCLEO-F412ZG, a board it does not support. [The write-up](https://blok.storagebits.workers.dev/blog/hubris-f412/). | ![fork](https://img.shields.io/badge/fork-oxidecomputer-F2EDE4?style=flat-square&labelColor=0E0D0B) |
| **[lukarne-catalog](https://github.com/storagebits/lukarne-catalog)**<br><sub>Data · daily job</sub> | The live-webcam catalogue behind Lukarne, an Android TV globe of webcams (the app is still on the bench). Regenerated every day. | ![generated](https://img.shields.io/badge/data-daily-F2B35B?style=flat-square&labelColor=0E0D0B) |
| **[KISSS](https://github.com/storagebits/KISSS)**<br><sub>Python · Shell</sub> | *Keep It Simple Slide Scanner*: a DIY rig to digitise old film slides. | ![stars](https://img.shields.io/github/stars/storagebits/KISSS?style=flat-square&color=F2EDE4&labelColor=0E0D0B) |

<details>
<summary><b>See Kronograf and Almanak run</b></summary>
<br>
<p>
  <img src="https://github.com/storagebits/kronograf/raw/main/docs/screens/kronograf-demo.gif" height="300" alt="Kronograf on the T-Watch: aviator face, time circuits, launcher, weather, an iPhone notification, the network toolbox">
  <img src="https://github.com/algotitanhq/almanak/raw/main/docs/screens/almanak-demo.gif" height="300" alt="Almanak on Android TV: the Nocturne theme, the forecast, then the three themes cycled live">
</p>
</details>

<details>
<summary><b>Earlier work</b></summary>
<br>

| Project | What it was |
|---|---|
| [nasa-meteor-to-planetaryjs](https://github.com/storagebits/nasa-meteor-to-planetaryjs) | NASA Space Apps hackathon: meteorite falls on a 3D globe, with an international team of six. |
| [vectests](https://github.com/storagebits/vectests) | Programming the Vectrex, a 1982 vector-display console. |
| [board-explorer](https://github.com/storagebits/board-explorer) | Electronics meets board games, in Go. |
| [terraform-oci-free-compute](https://github.com/storagebits/terraform-oci-free-compute-maximal-example) | Getting the most out of Oracle Cloud's free tier with Terraform. |

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-stack-dark.svg">
  <img src="assets/section-stack-light.svg" width="100%" alt="02, stack: what I reach for">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img src="assets/stack-light.svg" width="100%" alt="Embedded: C on ESP32 with LVGL, Rust on STM32 (Hubris), BLE, IR and I²C sensors. Apps: Kotlin and Compose for TV, OpenGL ES on Android, Expo and React Native. Infra: Incus, Docker, Pangolin, Go, Python, Terraform, GitHub Actions, Cloudflare.">
</picture>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-lately-dark.svg">
  <img src="assets/section-lately-light.svg" width="100%" alt="03, lately: latest commits, refreshed every morning">
</picture>

<!-- activity:start -->
- README and MIT licence, in 7 repos: [`vectests`](https://github.com/storagebits/vectests), [`nasa-meteor-to-planetaryjs`](https://github.com/storagebits/nasa-meteor-to-planetaryjs), [`KISSS`](https://github.com/storagebits/KISSS), [`board-explorer-makecode`](https://github.com/storagebits/board-explorer-makecode), [`board-explorer`](https://github.com/storagebits/board-explorer), [`storagebits.github.io`](https://github.com/storagebits/storagebits.github.io), [`lukarne-catalog`](https://github.com/storagebits/lukarne-catalog) <sub>today</sub>
- [`algotitanhq/almanak`](https://github.com/algotitanhq/almanak) · [Initial public import of Almanak](https://github.com/algotitanhq/almanak/commit/77c5d35687add036a5a34aea9dfc3a780f1e761d) <sub>today</sub>
- [`storagebits/kronograf`](https://github.com/storagebits/kronograf) · [Toolbox: keep Wi-Fi modem sleep while Bluetooth is on (fixes reboots…](https://github.com/storagebits/kronograf/commit/3e82b01be65432e8db7f3a5c7230f1a6d87da451) <sub>4 days ago</sub>
<!-- activity:end -->

**Writing.** The stories behind the code are on [blok](https://blok.storagebits.workers.dev), in French, English and Spanish:

<!-- posts:start -->
- **[Testing the NUCLEO-F412ZG with Hubris and Humility](https://blok.storagebits.workers.dev/blog/hubris-f412/)** <sub>Oct 18, 2026</sub><br/>Porting Hubris, Oxide Computer's embedded OS, to a NUCLEO-F412ZG at 100 MHz: what had to change, from the untouched kernel to the two Humility…
- **[A 2020 watch, a complete firmware, three days](https://blok.storagebits.workers.dev/blog/ressusciter-kronograf/)** <sub>Oct 16, 2026</sub><br/>A 2020 T-Watch was sitting in a corner: developing for it took too much effort. In three days, with an agent, it got a firmware written from…
<!-- posts:end -->

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img src="assets/footer-light.svg" width="100%" alt="Créer. Transmettre. Explorer. Aimer. — et pas forcément dans cet ordre.">
</picture>
