[← Portfolio](../README.md) · [Infrastructure](../homelab/infrastructure.md) · [PCB design notes](../pcb/README.md)

# ESPHome devices

**Nine published configurations for sensors, displays, and a touch/voice interface.**

These are sanitized configurations from personal projects. They show hardware integration and application logic, but require your own credentials, matching wiring, and Home Assistant entities before validation or flashing.

## Device index

| Configuration | Board / display | What to inspect |
|---|---|---|
| [Mailbox alert](mailbox-alert.yaml) | ESP32-C6 | Door/reed events, AHT temperature/humidity, battery ADC, MQTT, deep sleep, wake/reconnect and OTA handling |
| [Plant moisture](plant-moisture.yaml) | ESP32-C3 / SSD1306 OLED | Capacitive moisture ADC, calibration, MQTT, display, deep sleep and wake handling |
| [Hall clock](hall-clock.yaml) | ESP32-C3 / ST7789V TFT | Clock display, LD2410 presence sensor over UART, Home Assistant time with SNTP fallback |
| [Kitchen display](kitchen-display.yaml) | ESP32-C3 / SSD1306 OLED | BME280, LD2410 presence, local buttons, Home Assistant actions and status display |
| [Bathroom monitor](bathroom-monitor.yaml) | ESP32-C3 / SSD1306 OLED | Environmental readings and Home Assistant display integration |
| [Office monitor](office-monitor.yaml) | ESP32-C3 / SSD1306 OLED | AHT temperature/humidity, ENS160 air-quality estimates, LD2410 presence |
| [Living-room monitor](livingroom-monitor.yaml) | ESP32-C3 / SSD1306 OLED | BME280, ADC input and Home Assistant values |
| [Touch / voice assistant](touch-voice-assistant.yaml) | ESP32-S3 / ILI9341 TFT + XPT2046 touch | I²S microphone/speaker, local wake-word detection, Home Assistant voice pipeline and touch controls |
| [E-paper dashboard](epaper.yaml) | ESP32-C3 / Waveshare 2.9-inch display | Home Assistant entity import, SPI display, clock and environmental status |

The ENS160 reports **estimated equivalent CO₂ (eCO₂)** and VOC-related air quality, not a direct CO₂ concentration measurement. Some retained entity/display names say “CO2”; interpret those ENS160 values as estimates. See the [ESPHome ENS160 documentation](https://esphome.io/components/sensor/ens160/).

## Engineering focus

- **Battery devices:** event-driven wake-up, bounded connectivity attempts, MQTT publication, and returning to deep sleep. OTA requires an awake device and the configured maintenance behavior.
- **Interfaces:** I²C sensors and OLEDs, SPI displays, UART presence sensing, ADC measurement, and I²S audio.
- **User interfaces:** local status screens, physical buttons, touch controls, and voice interaction through Home Assistant.
- **Integration:** Home Assistant API entities, MQTT, time synchronization, and reconnect behavior.

## Prepare a configuration

1. Match the exact board, display, sensor, pins, and power arrangement to your hardware.
2. Replace every `YOUR_*` placeholder locally. ESPHome API encryption requires a valid generated key; the placeholder text cannot pass device configuration validation. Use a private `secrets.yaml` for real credentials.
3. Update Home Assistant entity IDs, MQTT topics/broker details, timezone, and any installation-specific addresses.
4. Supply `fonts/materialdesignicons-webfont.ttf` for the bathroom, living-room, and e-paper configurations. The font binary is not included. Google Fonts entries require network access during preparation.
5. With ESPHome installed, validate your edited copy first, then compile it before choosing to flash:

```bash
esphome config your-device.yaml
esphome compile your-device.yaml
```

Use the [ESPHome getting-started guide](https://esphome.io/guides/getting_started_command_line/) for installation and device connection. The public files have been reviewed as source examples; this portfolio refresh did not compile or flash hardware, or establish battery-life measurements.
