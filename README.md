# Arduino TFT Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

> Python-based simulator for prototyping Arduino-style TFT interfaces without repeatedly flashing physical hardware.

Arduino TFT Simulator interprets a subset of common `tft.xxx()` drawing commands and renders the resulting interface on a desktop computer. It was created to speed up experimentation with embedded display layouts, gauges, text, colours, and monochrome bitmaps.

## Project status

This repository is a **software prototyping tool**, not a cycle-accurate or library-accurate emulator of TFT hardware.

It approximates selected Arduino/TFT graphics calls well enough for UI prototyping, but it does not emulate the underlying display controller, timing behaviour, DMA, touch interfaces, or every feature of TFT_eSPI / Adafruit_GFX / other libraries.

## Development approach and authorship

This project was developed with **heavy AI assistance**.

The author defined the original need, intended workflow, supported command families, expected simulator behaviour, and practical use cases. AI tools were used extensively to generate and expand the Python implementation, add parsers and rendering features, refactor code, and review the assembled program.

The author's role was mainly to:

- define what Arduino constructs the simulator should accept;
- specify the expected visual behaviour;
- test outputs against intended interfaces;
- integrate generated additions;
- identify missing or incorrect behaviour;
- request iterative corrections and extensions.

Accordingly, this repository demonstrates the specification and integration of a useful engineering tool through an AI-assisted workflow rather than fully manual Python implementation.

## Why it exists

Embedded TFT interface development often involves a slow edit-build-flash-check cycle. This simulator allows a subset of display code to be previewed on a PC before deployment to hardware.

Typical uses include:

- layout prototyping;
- dashboard and gauge design;
- bitmap placement;
- quick validation of coordinates and dimensions;
- producing screenshots for documentation;
- experimenting without having the target display connected.

## Main features

### Graphics primitives

Supported operations include:

- rectangles and rounded rectangles;
- circles;
- triangles;
- lines;
- individual pixels;
- filled and outline variants.

### Text

The simulator supports operations such as:

- `setCursor()`;
- `setTextColor()`;
- `setTextFont()`;
- `setTextSize()`;
- `print()` / `println()`;
- `drawString()`;
- optional TTF/OTF font substitution through the Python API.

Font rendering is an approximation and does not reproduce TFT_eSPI built-in fonts exactly.

### Bitmaps

Supported functionality includes:

- monochrome bitmaps;
- parsing of `PROGMEM` byte arrays;
- configurable bitmap colour.

### Display behaviour

Implemented features include:

- rotation values 0–3;
- `fillScreen()`;
- configurable display dimensions;
- common named TFT colours;
- RGB565 and RGB888 colour inputs.

### Basic code parsing

The simulator can interpret a limited subset of Arduino-like constructs, including:

- simple variables;
- arithmetic expressions;
- selected `for` loops;
- `tft.function(...)` drawing calls.

It is not a general C/C++ interpreter.

## Quick start

```bash
pip install pygame
git clone https://github.com/mdmmt05/Arduino_TFT_simulator.git
cd Arduino_TFT_simulator
python tft_simulator_interactive_v2.py main_interface.txt
```

## Custom fonts

```python
from tft_simulator_interactive_v2 import TFTSimulator

sim = TFTSimulator()
sim.setCustomFont(7, "./fonts/digital-7.ttf")

with open("main_interface.txt") as f:
    code = f.read()

sim.parse_and_execute(code)
```

## Bitmap example

```cpp
const unsigned char myLogo[] PROGMEM = {
  0x00, 0xFF /* ... */
};

tft.drawBitmap(100, 50, myLogo, 64, 64, TFT_GREEN);
```

## Selected supported calls

```text
tft.drawRect(...)
tft.fillRect(...)
tft.drawCircle(...)
tft.fillCircle(...)
tft.drawTriangle(...)
tft.fillTriangle(...)
tft.drawRoundRect(...)
tft.fillRoundRect(...)
tft.drawLine(...)
tft.drawPixel(...)
tft.setCursor(...)
tft.setTextColor(...)
tft.setTextFont(...)
tft.setTextSize(...)
tft.print(...)
tft.println(...)
tft.drawString(...)
tft.drawBitmap(...)
tft.setRotation(...)
tft.fillScreen(...)
```

## Not supported / limitations

Current limitations include:

- no complete `loop()` execution model;
- no timing-accurate `delay()` simulation;
- no animation engine;
- no touch-input simulation;
- no TFT DMA or double-buffering behaviour;
- no sprites / `TFT_eSprite`;
- no complete `setFreeFont()` / Arduino font parsing;
- no colour-image pipeline comparable to real embedded libraries;
- no guarantee of compatibility with arbitrary Arduino code;
- system fonts only approximate actual display fonts;
- large bitmaps may render slowly.

The simulator is library-agnostic only in the limited sense that it recognizes selected `tft.xxx()` command patterns; it does **not** emulate the internals of every library exposing that syntax.

## Repository structure

```text
Arduino_TFT_simulator/
├── tft_simulator_interactive_v2.py
├── main_interface.txt
├── graphic.txt
├── README.md
├── CHANGELOG.md
├── BITMAP_GUIDE.md
├── CUSTOM_FONTS_GUIDE.md
└── LICENSE
```

## Repository purpose

This project is retained as a practical experiment in building a desktop tool around an embedded-development workflow. It is particularly useful as documentation of the problem definition, supported feature set, and iterative testing process used to create the simulator.

## License

MIT License. See `LICENSE`.
