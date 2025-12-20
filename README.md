# TFT Display Simulator for Arduino

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

**The first comprehensive TFT display simulator for Arduino development** - No hardware needed!

> **Note**: While OLED simulators exist, this is the first full-featured simulator specifically designed for TFT displays with Arduino. Test your TFT graphics code instantly on your PC before uploading to hardware!

---

## 🎯 Why This Project?

Developing TFT display interfaces for Arduino is **slow and frustrating**:
- ❌ Upload code → Wait → See result → Repeat
- ❌ No OLED-style simulation tools available for TFT
- ❌ Difficult to iterate on UI designs
- ❌ Wasted time on syntax errors and layout bugs

**This simulator solves all of that:**
- ✅ Instant visual feedback - see changes immediately
- ✅ Iterate 10x faster on designs
- ✅ Catch bugs before uploading to hardware
- ✅ Perfect for prototyping dashboards, gauges, and UIs

---

## ✨ Key Features

### 🎨 Graphics Primitives
- **Shapes**: Rectangles, circles, triangles, rounded rectangles
- **Lines & Pixels**: Draw individual pixels or lines
- **Fill & Outline**: Both filled and outline versions of all shapes

### 📝 Text Rendering
- **8 Font Sizes**: Font 1-8 with accurate TFT_eSPI dimensions
- **Custom Fonts**: Load your own TTF/OTF fonts (digital-7, etc.)
- **Text Positioning**: `setCursor()`, `print()`, `println()`
- **Inline Font Changes**: Switch fonts mid-line

### 🖼️ Bitmap/Image Support
- **Monochrome Bitmaps**: 1-bit images (logos, icons)
- **PROGMEM Arrays**: Automatic parsing of `const unsigned char[]`
- **Any Size**: From 16×16 icons to 512×512 images
- **Custom Colors**: Render bitmaps in any color

### 🔧 Display Control
- **Rotation**: 0-3 (0°, 90°, 180°, 270°)
- **Screen Fill**: `fillScreen()` with any color
- **Variable Size**: Configure display dimensions

### 💡 Code Features
- **Variables & Math**: `int margin = 10; width - (2 * margin)`
- **For Loops**: Nested loops with various increment styles
- **Color Formats**: RGB565, RGB888, named colors (TFT_RED, etc.)

---

## 🚀 Quick Start

### Installation

```bash
# Install pygame
pip install pygame

# Download simulator
git clone https://github.com/yourusername/tft-simulator.git
cd tft-simulator

# Run example
python tft_simulator_interactive.py examples/dashboard.ino
```

### Basic Example

```cpp
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();

void setup() {
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);
  
  // Draw rectangle border
  tft.drawRect(10, 10, 460, 300, TFT_CYAN);
  
  // Display text
  tft.setCursor(50, 50);
  tft.setTextColor(TFT_WHITE);
  tft.setTextFont(7);
  tft.println("5280 RPM");
}

void loop() {}
```

**Run it:**
```bash
python tft_simulator_interactive.py my_sketch.ino
```

**Result:** Instant window showing your TFT output! 🎉

---

## 📚 Comprehensive Examples

### Dashboard with Gauges
```cpp
tft.fillRoundRect(10, 10, 460, 100, 15, TFT_MAROON);
tft.setTextFont(7);
tft.setTextColor(0xEB8015);  // Orange
tft.setCursor(50, 30);
tft.println("120 km/h");
```

### Bitmap Logo Display
```cpp
const unsigned char logo[] PROGMEM = {
  0x00, 0xFF, 0x7E, ... // bitmap data
};

tft.drawBitmap(100, 50, logo, 64, 64, TFT_WHITE);
```

### Multi-Font Text
```cpp
tft.setTextFont(2);
tft.print("Speed: ");
tft.setTextFont(6);
tft.print("120");
tft.setTextFont(2);
tft.print(" km/h");
```

More examples in [`/examples`](examples/) folder!

---

## 🎨 Custom Fonts

Load custom TTF/OTF fonts for professional displays:

```python
sim = TFTSimulator()

# Use digital-7 font for Font 7 (RPM displays)
sim.setCustomFont(7, "./fonts/digital-7.ttf")

# Or set default font for all
sim.setDefaultCustomFont("./fonts/my-font.ttf")
```

Perfect for:
- Digital speedometers (Digital-7, DSEG7)
- Racing dashboards (Eurostile, Orbitron)
- Retro displays (Calculator fonts)

See [CUSTOM_FONTS_GUIDE.md](CUSTOM_FONTS_GUIDE.md) for details.

---

## 🖼️ Bitmap/Image Support

Convert images to Arduino-compatible bitmaps:

1. **Use online converter**: http://javl.github.io/image2cpp/
2. **Copy generated array** to your Arduino code
3. **Simulator renders automatically**!

```cpp
const unsigned char myLogo[] PROGMEM = {
  0x00, 0xFF, ... // from image2cpp
};

tft.drawBitmap(100, 50, myLogo, 64, 64, TFT_GREEN);
```

See [BITMAP_GUIDE.md](BITMAP_GUIDE.md) for complete guide.

---

## 🔧 Library-Agnostic Design

**Important**: This simulator is **library-agnostic**. It works with any Arduino TFT library that uses the `tft.xxx()` syntax:

✅ **Supported Libraries:**
- TFT_eSPI (primary target)
- Adafruit_GFX + display drivers
- UTFT
- Arduino_GFX
- Any library using `tft.drawRect()`, `tft.print()`, etc.

The simulator **doesn't care** which library you're using - it only parses the **command syntax**, not library implementations. As long as your code uses `tft.functionName()` format, it will work!

---

## ✅ Supported Features

### Graphics
- ✅ `tft.drawRect(x, y, w, h, color)`
- ✅ `tft.fillRect(x, y, w, h, color)`
- ✅ `tft.drawCircle(x, y, r, color)`
- ✅ `tft.fillCircle(x, y, r, color)`
- ✅ `tft.drawTriangle(x0, y0, x1, y1, x2, y2, color)`
- ✅ `tft.fillTriangle(x0, y0, x1, y1, x2, y2, color)`
- ✅ `tft.drawRoundRect(x, y, w, h, r, color)`
- ✅ `tft.fillRoundRect(x, y, w, h, r, color)`
- ✅ `tft.drawLine(x0, y0, x1, y1, color)`
- ✅ `tft.drawPixel(x, y, color)`

### Text
- ✅ `tft.setCursor(x, y, font)`
- ✅ `tft.setTextColor(color)`
- ✅ `tft.setTextFont(1-8)` - Accurate TFT_eSPI sizes
- ✅ `tft.setTextSize(1-7)` - Size multiplier
- ✅ `tft.print("text")`
- ✅ `tft.println("text")`
- ✅ `tft.drawString("text", x, y, font)`
- ✅ Custom TTF/OTF font loading

### Images
- ✅ `tft.drawBitmap(x, y, array, w, h, color)` - Monochrome bitmaps
- ✅ Automatic `PROGMEM` array parsing

### Display
- ✅ `tft.init()`
- ✅ `tft.setRotation(0-3)`
- ✅ `tft.fillScreen(color)`

### Colors
- ✅ Named colors: `TFT_BLACK`, `TFT_WHITE`, `TFT_RED`, etc. (20+ colors)
- ✅ RGB565 format: `0xF800` (red)
- ✅ RGB888 format: `0xFF0000` (red)

### Code Features
- ✅ Variables: `int x = 10;`
- ✅ Math expressions: `width - (2 * margin)`
- ✅ For loops (nested, multiple increment styles)

---

## ❌ Not Yet Supported

### Text Features
- ⏳ `setFreeFont()` / `setFont()` - **Custom font integration from Arduino code**
- ⏳ Text background colors
- ⏳ Text datum/alignment settings
- ⏳ `drawCentreString()`, `drawRightString()`

> **Note on Font Integration**: While the simulator supports loading custom TTF/OTF fonts through Python API, it **does not yet support** TFT_eSPI's `setFreeFont()` or `setFont()` functions that load fonts defined in Arduino code (e.g., from the Fonts folder). This is a planned feature for future releases.

### Images
- ⏳ Color bitmaps (RGB565, RGB888)
- ⏳ External image files (.bmp, .png, .jpg)
- ⏳ `pushImage()` function
- ⏳ Image rotation/scaling
- ⏳ Sprites/TFT_eSprite

### Advanced Graphics
- ⏳ `drawArc()`, `fillArc()`
- ⏳ `drawEllipse()`, `fillEllipse()`
- ⏳ Bezier curves
- ⏳ Anti-aliasing
- ⏳ Gradients

### Display Features
- ⏳ `invertDisplay()`
- ⏳ Partial screen updates
- ⏳ DMA/double buffering simulation
- ⏳ Touch input simulation

### Code Features
- ⏳ `loop()` function execution (currently only `setup()`)
- ⏳ `delay()` / timing simulation
- ⏳ Animation playback
- ⏳ Serial output capture

**Want to contribute?** These features are great candidates for PRs! See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 🎮 Controls

- **ESC** or **Close Window**: Exit simulator
- Window shows display at 1:1 scale (no upscaling)

---

## 📐 Display Configuration

Default: 480×320 (standard TFT size)

Configure in your Arduino code:
```cpp
int displayWidth = 480;
int displayHeight = 320;
```

Or modify in Python:
```python
sim = TFTSimulator(width=800, height=480)  # 7" display
```

---

## 🎯 Use Cases

### Rapid Prototyping
Iterate on UI designs 10x faster without hardware

### Educational
Perfect for teaching Arduino graphics programming

### Code Validation
Catch layout bugs before uploading to hardware

### Documentation
Generate screenshots for project documentation

### Demonstrations
Show TFT output in presentations without hardware

---

## 🏗️ Project Structure

```
tft-simulator/
├── tft_simulator_interactive.py    # Main simulator
├── examples/                        # Example Arduino sketches
│   ├── dashboard.ino
│   ├── gauges.ino
│   └── bitmap_demo.ino
├── fonts/                           # Optional custom fonts
│   └── digital-7.ttf
├── docs/
│   ├── BITMAP_GUIDE.md
│   ├── CUSTOM_FONTS_GUIDE.md
│   └── API_REFERENCE.md
├── README.md                        # This file
├── CHANGELOG.md
└── LICENSE
```

---

## 🤝 Contributing

Contributions welcome! Priority areas:

1. **Arduino font integration** (`setFreeFont()`, `setFont()`)
2. **Missing TFT_eSPI features** (sprites, arcs, etc.)
3. **Animation support** (loop() execution)
4. **Image formats** (RGB bitmaps, PNG loading)
5. **Touch simulation**
6. **Performance optimization**

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📝 Version History

### v2.2 (Current)
- ✅ Bitmap/image support (monochrome)
- ✅ PROGMEM array parsing
- ✅ Custom font loading via Python API

### v2.1
- ✅ Corrected font sizes (Font 7: 75px, Font 8: 90px)
- ✅ Inline font switching
- ✅ Proper cursor tracking

### v2.0
- ✅ Text rendering support
- ✅ 8 font sizes
- ✅ Color text

### v1.0
- ✅ Basic graphics primitives
- ✅ Display rotation
- ✅ For loop support

See [CHANGELOG.md](CHANGELOG.md) for complete history.

---

## 🐛 Known Issues

1. **Font rendering**: Uses system fonts instead of TFT_eSPI built-in fonts (close approximation)
2. **Arduino font integration**: `setFreeFont()` not yet supported
3. **`loop()` not executed**: Only `setup()` runs (animations not supported yet)
4. **No touch input**: Mouse clicks not simulated
5. **Performance**: Large bitmaps may be slow (Python pixel-by-pixel rendering)

See [Issues](https://github.com/yourusername/tft-simulator/issues) for more.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **TFT_eSPI Library** by Bodmer - Inspiration for command syntax
- **pygame** - Rendering engine
- **image2cpp** - Bitmap conversion tool
- Arduino community for feedback and testing

---

## 📧 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/tft-simulator/issues)
- **Discussions**: [Ask questions or share projects](https://github.com/yourusername/tft-simulator/discussions)
- **Hackster.io**: [Full tutorial article](https://hackster.io/link-to-article)

---

## ⭐ Star History

If this project helped you, please star it! ⭐

It encourages development and helps others discover this tool.

---

**Made with ❤️ for the Arduino community**

*Finally, a proper TFT simulator that actually works!*
