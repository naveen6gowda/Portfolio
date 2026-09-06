[← Portfolio](../README.md) · [Related ESPHome firmware](../esphome/README.md)

# PCB design — compute carrier and connected relay

**KiCad design work connecting embedded software, interfaces, and power considerations.**

This directory contains design notes. Schematics, board layouts, BOMs, Gerbers, fabrication records, and validation reports are not published here. The descriptions distinguish intended features from verified hardware results.

## Compute Module 5 carrier adaptation

I adapted an existing open-source CM5 carrier design toward a smaller board with the interfaces needed for a home-automation / edge-compute use case. My contribution is the adaptation, not authorship of the original reference design.

Design considerations included the CM5 interface, power input, USB, HDMI, GPIO access, board size, and expansion options. An ESP32-C6 companion was considered for wireless and IoT integration. These are design goals rather than a validated product specification.

The upstream project and its exact revision are not yet identified in this public write-up; the attribution needs completing before any derived CAD files are distributed. No accelerator performance, manufacturing readiness, or DRC result is claimed without the corresponding design evidence.

## ESP32-C6 relay board

A two-channel relay-board design intended to integrate with Home Assistant through ESPHome and MQTT. The design work covers relay control, input/output separation, power conversion, and firmware integration.

The documented power concept uses an AC-to-5 V module. **The ESP32-C6-MINI-1 module requires a regulated 3.0–3.6 V supply**; a 5 V output must not feed its supply directly. See [Espressif's module datasheet](https://documentation.espressif.com/esp32-c6-mini-1_mini-1u_datasheet_en.html).

Relay contact ratings, mains spacing, protection, enclosure, and isolation require assessment against the actual schematic, PCB, components, and intended load. This portfolio does not establish mains safety or product certification.

## Skills demonstrated by the design work

KiCad schematic and layout work · embedded interfaces · power-domain planning · ESP32 integration · hardware/firmware coordination

For inspectable implementation files, start with the [published ESPHome configurations](../esphome/README.md).
