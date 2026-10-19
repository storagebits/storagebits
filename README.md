<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="François Lesage, storagebits, Montréal. I build at night, with AI agents, on real hardware. Today's moon and Montréal's sunrise and sunset, regenerated every morning.">
</picture>

<p>
  <a href="https://blok.storagebits.workers.dev"><img src="https://img.shields.io/badge/blog-blok-E89E5C?style=flat-square&labelColor=0E0D0B" alt="Blog: blok"></a>
  <a href="https://github.com/algotitanhq"><img src="https://img.shields.io/badge/company-ALGOTITAN-F2B35B?style=flat-square&labelColor=0E0D0B" alt="ALGOTITAN on GitHub"></a>
  <a href="https://x.com/storagebits"><img src="https://img.shields.io/badge/X-@storagebits-F2EDE4?style=flat-square&labelColor=0E0D0B" alt="X: @storagebits"></a>
</p>

I make things I want to use myself: a firmware for a 2020 smartwatch, apps for the TV in the living room,
an embedded kernel on a board it was never ported to, a homelab that rebuilds from its own docs.
Since October 2026 the agents that build them are organised as a company, **[ALGOTITAN](https://github.com/algotitanhq)**.

> [!NOTE]
> Everything here is built with AI agents, and each project says so. I set the direction, test on the real device and approve what ships; the agents write most of the code and the first drafts.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-work-dark.svg">
  <img src="assets/section-work-light.svg" width="100%" alt="01, from the workshop: things that run on real hardware">
</picture>

<a href="https://github.com/storagebits/kronograf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-kronograf-dark.svg"><img src="assets/card-kronograf-light.svg" width="49%" alt="Kronograf, shipped, v0.7 beta. Firmware for the LilyGO T-Watch 2020: a watch you want to raise your wrist for."></picture></a> <a href="https://github.com/algotitanhq/almanak"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-almanak-dark.svg"><img src="assets/card-almanak-light.svg" width="49%" alt="Almanak, shipped, open source. Android TV: an almanac for the TV, made to be left on."></picture></a>
<a href="https://blok.storagebits.workers.dev/blog/hubris-f412/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-hubris-dark.svg"><img src="assets/card-hubris-light.svg" width="49%" alt="Hubris on a NUCLEO-F412ZG, runs, with a write-up. Oxide's kernel, on a board it never met."></picture></a> <a href="https://blok.storagebits.workers.dev/blog/quatre-jours/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-lukarne-dark.svg"><img src="assets/card-lukarne-light.svg" width="49%" alt="Lukarne, on the bench. Android TV: spin a globe, dive into live webcams."></picture></a>

<details>
<summary><b>See them run</b></summary>
<br>
<p>
  <img src="https://github.com/storagebits/kronograf/raw/main/docs/screens/kronograf-demo.gif" height="300" alt="Kronograf on the T-Watch: aviator face, time circuits, launcher, weather, an iPhone notification, the network toolbox">
  <img src="https://github.com/algotitanhq/almanak/raw/main/docs/screens/almanak-demo.gif" height="300" alt="Almanak on Android TV: the Nocturne theme, the forecast, then the three themes cycled live">
</p>
</details>

Also on the bench: **DropboksTV** (the family Dropbox on the TV, signed in with a QR code) and **Shot2Cart** (from a photo to an open shopping cart in under 15 seconds). They come out when they are finished.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-notebook-dark.svg">
  <img src="assets/section-notebook-light.svg" width="100%" alt="02, the notebook: blok, in French, English and Spanish">
</picture>

[blok](https://blok.storagebits.workers.dev) is the workshop notebook: what works, what breaks, and what building with an AI changes. Each post lists its sources and how much of the draft I rewrote.

<!-- posts:start -->
- **[Testing the NUCLEO-F412ZG with Hubris and Humility](https://blok.storagebits.workers.dev/blog/hubris-f412/)** <sub>Oct 18, 2026</sub><br/>Porting Hubris, Oxide Computer's embedded OS, to a NUCLEO-F412ZG at 100 MHz: what had to change, from the untouched kernel to the two Humility…
- **[A 2020 watch, a complete firmware, three days](https://blok.storagebits.workers.dev/blog/ressusciter-kronograf/)** <sub>Oct 16, 2026</sub><br/>A 2020 T-Watch was sitting in a corner: developing for it took too much effort. In three days, with an agent, it got a firmware written from…
- **[Twelve minutes from idea to TV](https://blok.storagebits.workers.dev/blog/quatre-jours/)** <sub>Oct 12, 2026</sub><br/>Four days, six projects, 159 commits. The gap between “I'd like that” and “it runs on the device” has become ridiculous. What still slows things…
<!-- posts:end -->

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/section-made-dark.svg">
  <img src="assets/section-made-light.svg" width="100%" alt="03, how it is made: a company of agents, one human">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/workshop-dark.svg">
  <img src="assets/workshop-light.svg" width="100%" alt="Five steps: 01 Idea, a north star and a few decisions, mine. 02 ALGOTITAN, agents run as a company in Paperclip, with budgets. 03 Forge, Claude Code builds and tests in throwaway VMs. 04 Gate, nothing goes public without my approval. 05 Shipped, a repo, a release and a post on the blog.">
</picture>

Underneath: a homelab on Incus where every service sits behind an authenticated tunnel, is backed up and monitored, and can be rebuilt from its documentation. Twenty years of infrastructure leave one rule: sober, coherent, reproducible.

<details>
<summary><b>Earlier work</b></summary>
<br>

| | |
|---|---|
| [KISSS](https://github.com/storagebits/KISSS) | *Keep It Simple Slide Scanner*: a DIY rig to digitise old film slides. |
| [nasa-meteor-to-planetaryjs](https://github.com/storagebits/nasa-meteor-to-planetaryjs) | NASA Space Apps hackathon: meteorite falls on a 3D globe, with an international team of six. |
| [vectests](https://github.com/storagebits/vectests) | Programming the Vectrex, a 1982 vector-display console. |
| [board-explorer](https://github.com/storagebits/board-explorer) | Electronics meets board games, in Go. |
| [terraform-oci-free-compute](https://github.com/storagebits/terraform-oci-free-compute-maximal-example) | Getting the most out of Oracle Cloud's free tier with Terraform. |

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img src="assets/footer-light.svg" width="100%" alt="Créer. Transmettre. Explorer. Aimer. — et pas forcément dans cet ordre.">
</picture>
