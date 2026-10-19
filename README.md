<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="storagebits@workshop: public repos, commits in the last 30 days, languages, latest release and today's moon, regenerated every morning. Create. Share. Explore. Love.">
</picture>

<p>
  <a href="https://blok.storagebits.workers.dev"><img src="https://img.shields.io/badge/blog-blok-E89E5C?style=flat-square&labelColor=0E0D0B" alt="Blog: blok"></a>
  <a href="https://github.com/algotitanhq"><img src="https://img.shields.io/badge/agentic%20organization-ALGOTITAN-F2B35B?style=flat-square&labelColor=0E0D0B" alt="Agentic organization: ALGOTITAN"></a>
  <img src="https://img.shields.io/badge/runs%20on-real%20hardware-F2EDE4?style=flat-square&labelColor=0E0D0B" alt="Runs on real hardware">
  <a href="https://x.com/storagebits"><img src="https://img.shields.io/badge/X-@storagebits-F2EDE4?style=flat-square&labelColor=0E0D0B" alt="X: @storagebits"></a>
</p>

More ideas than nights. I invent things for the pleasure of seeing them run: a firmware for a forgotten watch, apps for the living-room TV,
a kernel on a board nobody ported it to. To keep up with the ideas, I gave them a company of AI agents: **[ALGOTITAN](https://github.com/algotitanhq)**.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-repos-dark.svg">
  <img src="assets/section-repos-light.svg" width="100%" alt="01, repositories: code that runs on real hardware">
</picture>

| Project | What it is | Status |
|---|---|:---:|
| **[Kronograf](https://github.com/storagebits/kronograf)**<br><sub>ESP32 · C · LVGL</sub> | A from-scratch firmware for the LilyGO T-Watch 2020: aviator chronograph, *Back to the Future* time circuits, iPhone notifications over BLE, live buses, a network toolbox, and a macOS simulator. | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-kronograf-dark.svg"><img src="assets/status-kronograf-light.svg" width="150" alt="Beta release"></picture> |
| **[Almanak](https://github.com/algotitanhq/almanak)**<br><sub>Android TV · Kotlin · Compose</sub> | An ambient almanac for Android TV, made to be left on: time, weather, the next bus in real time, sun and moon, a generative sky. Open data, no account. | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-almanak-dark.svg"><img src="assets/status-almanak-light.svg" width="150" alt="CI status"></picture> |
| **[Humility](https://github.com/storagebits/humility)**<br><sub>Rust · STM32</sub> | Fork of Oxide's Hubris debugger, used to bring Hubris up on a NUCLEO-F412ZG, a board it does not support. [The write-up](https://blok.storagebits.workers.dev/blog/hubris-f412/). | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-humility-dark.svg"><img src="assets/status-humility-light.svg" width="150" alt="Fork of Oxide"></picture> |
| **[lukarne-catalog](https://github.com/storagebits/lukarne-catalog)**<br><sub>Data · daily job</sub> | The live-webcam catalogue behind Lukarne, an Android TV globe of webcams (the app is still on the bench). Regenerated every day. | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-lukarne-catalog-dark.svg"><img src="assets/status-lukarne-catalog-light.svg" width="150" alt="Daily data"></picture> |
| **[KISSS](https://github.com/storagebits/KISSS)**<br><sub>Python · Shell</sub> | *Keep It Simple Slide Scanner*: a DIY rig to digitise old film slides. | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-kisss-dark.svg"><img src="assets/status-kisss-light.svg" width="150" alt="DIY hardware"></picture> |

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
  <img src="assets/footer-light.svg" width="100%" alt="Create. Share. Explore. Love. — not necessarily in that order.">
</picture>
