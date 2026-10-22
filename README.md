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
a kernel on a board nobody ported it to. To keep up with the ideas, I gave them an organization of AI agents: **[ALGOTITAN](https://github.com/algotitanhq)**.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-repos-dark.svg">
  <img src="assets/section-repos-light.svg" width="100%" alt="01, repositories: code that runs on real hardware">
</picture>

<!-- repos:start -->
| Project | What it is | Stack & topics |
|---|---|---|
|  <a href="https://github.com/algotitanhq/uberblok"><img src="assets/thumbs/uberblok.png" width="160" alt="Uberblok: an exploded hard disk beside the uberblock struct and its block tree"></a><br>**[Uberblok](https://github.com/algotitanhq/uberblok)**<br><picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-uberblok-dark.svg"><img src="assets/status-uberblok-light.svg" width="140" alt="CI PASSING"></picture>  | An interactive museum of ZFS, visited room by room: copy-on-write, transaction groups, RAID-Z, the ARC, the ZIL. Every animation is read from the OpenZFS source. [Visit it](https://uberblok.storagebits.workers.dev). | <img src="https://img.shields.io/badge/Astro-16140F?style=flat-square&logo=astro&logoColor=F2EDE4" alt="Astro"> <img src="https://img.shields.io/badge/TypeScript-16140F?style=flat-square&logo=typescript&logoColor=F2EDE4" alt="TypeScript"> <img src="https://img.shields.io/badge/Three.js-16140F?style=flat-square&logo=threedotjs&logoColor=F2EDE4" alt="Three.js"> <img src="https://img.shields.io/badge/OpenZFS-16140F?style=flat-square" alt="OpenZFS"><br><br><code>filesystem</code> <code>openzfs</code> <code>storage</code> <code>zfs</code> |
|  <a href="https://github.com/storagebits/kronograf"><img src="assets/thumbs/kronograf.png" width="160" alt="Kronograf aviator face on the T-Watch"></a><br>**[Kronograf](https://github.com/storagebits/kronograf)**<br><picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-kronograf-dark.svg"><img src="assets/status-kronograf-light.svg" width="140" alt="BETA 0.7.0"></picture>  | A from-scratch firmware for the LilyGO T-Watch 2020: aviator chronograph, *Back to the Future* time circuits, iPhone notifications over BLE, live buses, a network toolbox, and a macOS simulator. | <img src="https://img.shields.io/badge/ESP32-16140F?style=flat-square&logo=espressif&logoColor=F2EDE4" alt="ESP32"> <img src="https://img.shields.io/badge/C-16140F?style=flat-square&logo=c&logoColor=F2EDE4" alt="C"> <img src="https://img.shields.io/badge/LVGL-16140F?style=flat-square" alt="LVGL"> <img src="https://img.shields.io/badge/PlatformIO-16140F?style=flat-square&logo=platformio&logoColor=F2EDE4" alt="PlatformIO"> <img src="https://img.shields.io/badge/BLE-16140F?style=flat-square&logo=bluetooth&logoColor=F2EDE4" alt="BLE"><br><br><code>ancs</code> <code>ble</code> <code>esp32</code> <code>firmware</code> <code>gtfs-realtime</code> <code>lilygo</code> |
|  <a href="https://github.com/algotitanhq/almanak"><img src="assets/thumbs/almanak.png" width="160" alt="Almanak, Nocturne theme on the TV"></a><br>**[Almanak](https://github.com/algotitanhq/almanak)**<br><picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-almanak-dark.svg"><img src="assets/status-almanak-light.svg" width="140" alt="CI PASSING"></picture>  | An ambient almanac for Android TV, made to be left on: time, weather, the next bus in real time, sun and moon, a generative sky. Open data, no account. | <img src="https://img.shields.io/badge/Android%20TV-16140F?style=flat-square&logo=android&logoColor=F2EDE4" alt="Android TV"> <img src="https://img.shields.io/badge/Kotlin-16140F?style=flat-square&logo=kotlin&logoColor=F2EDE4" alt="Kotlin"> <img src="https://img.shields.io/badge/Compose-16140F?style=flat-square&logo=jetpackcompose&logoColor=F2EDE4" alt="Compose"><br><br><code>android-tv</code> <code>compose-for-tv</code> <code>kotlin</code> <code>open-data</code> <code>screensaver</code> |
|  <a href="https://github.com/storagebits/humility"><img src="assets/thumbs/humility.png" width="160" alt="The NUCLEO-F412ZG board running Hubris"></a><br>**[Humility](https://github.com/storagebits/humility)**<br><picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-humility-dark.svg"><img src="assets/status-humility-light.svg" width="140" alt="FORK OF OXIDE"></picture>  | Fork of Oxide's Hubris debugger, used to bring Hubris up on a NUCLEO-F412ZG, a board it does not support. [The write-up](https://blok.storagebits.workers.dev/blog/hubris-f412/). | <img src="https://img.shields.io/badge/Rust-16140F?style=flat-square&logo=rust&logoColor=F2EDE4" alt="Rust"> <img src="https://img.shields.io/badge/STM32-16140F?style=flat-square&logo=stmicroelectronics&logoColor=F2EDE4" alt="STM32"> <img src="https://img.shields.io/badge/Hubris-16140F?style=flat-square" alt="Hubris"> |
|  <a href="https://github.com/storagebits/lukarne-catalog"><img src="assets/thumbs/lukarne-catalog.png" width="160" alt="Lukarne's night globe of live webcams"></a><br>**[lukarne-catalog](https://github.com/storagebits/lukarne-catalog)**<br><picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-lukarne-catalog-dark.svg"><img src="assets/status-lukarne-catalog-light.svg" width="140" alt="DAILY DATA"></picture>  | The live-webcam catalogue behind Lukarne, an Android TV globe of webcams (the app is still on the bench). Regenerated every day. | <img src="https://img.shields.io/badge/GitHub%20Actions-16140F?style=flat-square&logo=githubactions&logoColor=F2EDE4" alt="GitHub Actions"> <img src="https://img.shields.io/badge/JSON-16140F?style=flat-square&logo=json&logoColor=F2EDE4" alt="JSON"> <img src="https://img.shields.io/badge/YouTube-16140F?style=flat-square&logo=youtube&logoColor=F2EDE4" alt="YouTube"><br><br><code>catalogue</code> <code>github-actions</code> <code>json</code> <code>lukarne</code> <code>webcams</code> |
|  <a href="https://github.com/storagebits/KISSS"><img src="assets/thumbs/kisss.png" width="160" alt="The KISSS slide scanner rig"></a><br>**[KISSS](https://github.com/storagebits/KISSS)**<br><picture><source media="(prefers-color-scheme: dark)" srcset="assets/status-kisss-dark.svg"><img src="assets/status-kisss-light.svg" width="140" alt="DIY HARDWARE"></picture>  | *Keep It Simple Slide Scanner*: a DIY rig to digitise old film slides. | <img src="https://img.shields.io/badge/Raspberry%20Pi-16140F?style=flat-square&logo=raspberrypi&logoColor=F2EDE4" alt="Raspberry Pi"> <img src="https://img.shields.io/badge/Python-16140F?style=flat-square&logo=python&logoColor=F2EDE4" alt="Python"> <img src="https://img.shields.io/badge/Bash-16140F?style=flat-square&logo=gnubash&logoColor=F2EDE4" alt="Bash"> <img src="https://img.shields.io/badge/Nextcloud-16140F?style=flat-square&logo=nextcloud&logoColor=F2EDE4" alt="Nextcloud"><br><br><code>nextcloud</code> <code>opencv-python</code> <code>photography</code> <code>raspberry</code> <code>relay-switch</code> <code>scanning</code> |
<!-- repos:end -->

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
- [`algotitanhq/uberblok`](https://github.com/algotitanhq/uberblok) · [From algotitanhq/root-redirect-referrer](https://github.com/algotitanhq/uberblok/commit/85cb8214ffa3906a1d43e2ce0f42bf3c703b0ee2) <sub>today</sub>
- [`storagebits/lukarne-catalog`](https://github.com/storagebits/lukarne-catalog) · [Catalogue 2026-10-22T09:30Z](https://github.com/storagebits/lukarne-catalog/commit/f62017ef084c11adeeb170f9ad751ae8d09d8c40) <sub>today</sub>
- [`algotitanhq/almanak`](https://github.com/algotitanhq/almanak) · [Almanak v1.0.0](https://github.com/algotitanhq/almanak/commit/039bfacf60b5c40c61b8e9c1efebf13bb8052a96) <sub>yesterday</sub>
- [`algotitanhq/.github`](https://github.com/algotitanhq/.github) · [Profile: organization, in the Hermes row too](https://github.com/algotitanhq/.github/commit/90ab50093afc6c619085c726929baabe5a184373) <sub>yesterday</sub>
<!-- activity:end -->

**Writing.** The stories behind the code are on [blok](https://blok.storagebits.workers.dev), in French, English and Spanish:

<!-- posts:start -->
- **[Uberblok, an OpenZFS museum where every room cites the code](https://blok.storagebits.workers.dev/blog/uberblok/)** <sub>Oct 20, 2026</sub><br/>Uberblok is an interactive museum about OpenZFS in 14 stops: every technical claim points to the exact lines of zfs-2.4.4. Agents built it; I set…
- **[Testing the NUCLEO-F412ZG with Hubris and Humility](https://blok.storagebits.workers.dev/blog/hubris-f412/)** <sub>Oct 18, 2026</sub><br/>Porting Hubris, Oxide Computer's embedded OS, to a NUCLEO-F412ZG at 100 MHz: what had to change, from the untouched kernel to the two Humility…
<!-- posts:end -->

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img src="assets/footer-light.svg" width="100%" alt="Create. Share. Explore. Love. — not necessarily in that order.">
</picture>
