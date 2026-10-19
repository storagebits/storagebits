### Hi, I'm François.

Software engineer in Montréal, twenty years in systems, storage and cloud infrastructure.
At night I build things I want to use, with AI agents, on real hardware: a 2020 smartwatch, an Android TV box,
a NUCLEO board, an iPhone, a homelab.

Since October 2026 that workshop runs as a small company of agents: **[ALGOTITAN](https://github.com/algotitanhq)**.
I bring the ideas, the north stars and the decisions. Agents on Claude Code design, build, test, publish and
write the story. Nothing goes public without me, and every project says plainly how it was made.

<p>
  <a href="https://github.com/storagebits/kronograf"><img src="https://github.com/storagebits/kronograf/raw/main/docs/screens/kronograf-demo.gif" height="230" alt="Kronograf on the T-Watch: aviator face, time circuits, launcher, weather, an iPhone notification"></a>
  &nbsp;
  <a href="https://github.com/algotitanhq/almanak"><img src="https://github.com/algotitanhq/almanak/raw/main/docs/screens/almanak-demo.gif" height="230" alt="Almanak on Android TV: the Nocturne theme, the forecast, the settings drawer and the three themes"></a>
</p>

#### Shipped

| | |
|---|---|
| **[Kronograf](https://github.com/storagebits/kronograf)** | A from-scratch firmware for the LilyGO T-Watch 2020: an aviator chronograph, *Back to the Future* time circuits, iPhone notifications over BLE, live buses, a network toolbox. ESP32, LVGL, a macOS simulator. MIT. |
| **[Almanak](https://github.com/algotitanhq/almanak)** | An ambient almanac for Android TV, made to be left on: time, weather, the next bus, sun and moon, a generative sky. Kotlin, Compose for TV, open data, no account. MIT. |
| **[Hubris on a NUCLEO-F412ZG](https://blok.storagebits.workers.dev/blog/hubris-f412/)** | Oxide's Hubris kernel brought up on a board it does not support: first light, console, 100 MHz clock, a task that faults on purpose and gets restarted. With a [Humility](https://github.com/storagebits/humility) fork for the debugger. |

#### On the bench

Lukarne (fly over a globe of live webcams from the couch), DropboksTV (the family Dropbox on the TV, signed in by QR code),
Shot2Cart (from a photo to an open shopping cart in under 15 seconds). They come out when they are finished.

#### Writing

**[blok](https://blok.storagebits.workers.dev)** is the workshop notebook: what works, what breaks, and what building
with an AI changes. Written in French, with English and Spanish editions. Each post lists its sources and how much I rewrote.

- [Twelve minutes from idea to TV](https://blok.storagebits.workers.dev/blog/quatre-jours/): four days, six projects, 159 commits.
- [A 2020 watch, a complete firmware, three days](https://blok.storagebits.workers.dev/blog/ressusciter-kronograf/)
- [Testing the NUCLEO-F412ZG with Hubris and Humility](https://blok.storagebits.workers.dev/blog/hubris-f412/)

#### How the workshop runs

A homelab on Incus, every service behind a Pangolin tunnel with authentication, backed up and monitored.
Agents organised as a company in Paperclip, with an org chart, budgets and approvals; Claude Code does the hands-on work
in throwaway VMs. Twenty years of infrastructure leave one rule: sober, coherent, reproducible.

<sub>*Créer. Transmettre. Explorer. Aimer. — et pas forcément dans cet ordre.* · [X @storagebits](https://x.com/storagebits)</sub>
