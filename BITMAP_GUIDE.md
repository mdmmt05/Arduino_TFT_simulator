# 🖼️ Guida al Supporto Immagini/Bitmap

## Supporto Bitmap Monocromatiche nel Simulatore

Il simulatore ora supporta **bitmap monocromatiche** (1 bit per pixel) come quelle usate comunemente in Arduino con TFT_eSPI!

---

## 📊 Formato Supportato

### Bitmap Monocromatica (1-bit)
Il formato più comune per Arduino - ogni pixel è 0 (trasparente) o 1 (colorato).

```cpp
const unsigned char myImage[] PROGMEM = {
  0x00, 0x00, 0xFF, 0xFF, // ... dati bitmap
};
```

---

## 🚀 Come Usare

### 1. Definisci la Bitmap nel Codice Arduino

```cpp
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();

// Array bitmap (1 bit per pixel)
const unsigned char myLogo[] PROGMEM = {
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x7F, 0xFC, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0xFF, 0xFE, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x01, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00,
  // ... altri dati
};

void setup() {
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);
  
  // Disegna la bitmap
  // drawBitmap(x, y, nome_array, larghezza, altezza, colore)
  tft.drawBitmap(100, 50, myLogo, 64, 64, TFT_WHITE);
}

void loop() {
}
```

### 2. Esegui il Simulatore

```bash
python tft_simulator_interactive.py mio_sketch.ino
```

Il simulatore:
1. ✅ Trova automaticamente l'array `const unsigned char ... PROGMEM`
2. ✅ Carica i dati della bitmap
3. ✅ Disegna la bitmap quando incontra `drawBitmap()`

---

## 🎨 Esempio Completo

**File: logo_demo.txt**
```cpp
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();

// Logo 32x32 pixel (128 bytes)
const unsigned char arduino_logo[] PROGMEM = {
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x03, 0xff, 0xc0, 0x00, 0x0f, 0xff, 0xf0,
  0x00, 0x1f, 0xff, 0xf8, 0x00, 0x3f, 0xff, 0xfc,
  0x00, 0x7f, 0x00, 0xfe, 0x00, 0xfc, 0x00, 0x3f,
  0x01, 0xf8, 0x00, 0x1f, 0x03, 0xf0, 0x00, 0x0f,
  0x07, 0xe0, 0x00, 0x07, 0x0f, 0xc0, 0x18, 0x03,
  0x1f, 0x80, 0x3c, 0x01, 0x3f, 0x00, 0x7e, 0x00,
  0x7e, 0x00, 0xff, 0x00, 0xfc, 0x01, 0xff, 0x80,
  0xf8, 0x03, 0xc3, 0xc0, 0xf8, 0x07, 0x81, 0xe0,
  0xf0, 0x0f, 0x00, 0xf0, 0xf0, 0x1e, 0x00, 0x78,
  0xf0, 0x3c, 0x00, 0x3c, 0xf0, 0x78, 0x00, 0x1e,
  0xf0, 0xf0, 0x00, 0x0f, 0xf0, 0xe0, 0x00, 0x07,
  0xf0, 0xc0, 0x00, 0x03, 0xf8, 0x00, 0x00, 0x01,
  0x7e, 0x00, 0x00, 0x00, 0x3f, 0x00, 0x00, 0x00,
  0x1f, 0x80, 0x00, 0x01, 0x0f, 0xc0, 0x00, 0x03,
  0x07, 0xe0, 0x00, 0x07, 0x03, 0xf0, 0x00, 0x0f
};

void setup() {
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_NAVY);
  
  // Titolo
  tft.setCursor(150, 20);
  tft.setTextColor(TFT_CYAN);
  tft.setTextFont(4);
  tft.println("ARDUINO LOGO");
  
  // Logo bianco
  tft.drawBitmap(100, 80, arduino_logo, 32, 32, TFT_WHITE);
  
  // Logo verde
  tft.drawBitmap(220, 80, arduino_logo, 32, 32, TFT_GREEN);
  
  // Logo arancione (più grande - stesso array)
  tft.drawBitmap(340, 80, arduino_logo, 32, 32, TFT_ORANGE);
  
  // Testo sotto
  tft.setCursor(100, 150);
  tft.setTextFont(2);
  tft.setTextColor(TFT_LIGHTGREY);
  tft.println("Bitmap Support v2.2");
}

void loop() {
}
```

---

## 🔧 Come Creare Bitmap

### Metodo 1: Convertitore Online
1. Vai su: http://javl.github.io/image2cpp/
2. Carica la tua immagine
3. Imposta:
   - Width/Height: dimensioni desiderate
   - Code output format: **Arduino code**
   - Draw mode: **Horizontal - 1 bit per pixel**
4. Copia l'array generato

### Metodo 2: GIMP + Plugin
1. Apri immagine in GIMP
2. Converti in scala di grigi
3. Modalità → Indicizzato → 2 colori
4. Esporta come .xbm
5. Converti .xbm in formato C array

### Metodo 3: Script Python
```python
from PIL import Image

def image_to_bitmap_array(image_path, threshold=128):
    img = Image.open(image_path).convert('L')  # Scala di grigi
    w, h = img.size
    
    bytes_data = []
    for y in range(h):
        for x in range(0, w, 8):
            byte = 0
            for bit in range(8):
                if x + bit < w:
                    pixel = img.getpixel((x + bit, y))
                    if pixel > threshold:  # Bianco = 1
                        byte |= (1 << (7 - bit))
            bytes_data.append(byte)
    
    # Stampa array C
    print(f"const unsigned char myImage[] PROGMEM = {{")
    for i in range(0, len(bytes_data), 16):
        line = ", ".join(f"0x{b:02x}" for b in bytes_data[i:i+16])
        print(f"  {line},")
    print("};")
    print(f"\n// Dimensioni: {w}x{h} pixel, {len(bytes_data)} bytes")

# Uso
image_to_bitmap_array("logo.png")
```

---

## 📐 Calcolo Dimensione Array

Per una bitmap MxN pixel monocromatica:
- **Bytes necessari** = (M × N) / 8 (arrotonda per eccesso)
- Esempio: 200×200 pixel = 40,000 bit = 5,000 bytes

---

## 🎯 Caratteristiche

### ✅ Supportato
- Bitmap monocromatiche (1 bit/pixel)
- Array `const unsigned char[] PROGMEM`
- Qualsiasi dimensione (limitata solo dalla RAM Arduino)
- Colori personalizzati tramite parametro color
- Più bitmap nello stesso sketch
- Stessa bitmap disegnata più volte con colori diversi

### ❌ Non Supportato (per ora)
- Bitmap a colori (RGB565, RGB888)
- File esterni (.bmp, .png, .jpg)
- Compressione bitmap
- Anti-aliasing
- Rotazione/scaling bitmap

---

## 💡 Suggerimenti

1. **Dimensioni Ottimali**: 
   - Piccole icone: 16×16, 32×32, 64×64
   - Loghi medi: 100×100, 128×128
   - Immagini grandi: 200×200 (attenzione alla RAM!)

2. **Memoria Arduino**:
   - ESP32: Può gestire bitmap grandi (>100KB)
   - Arduino Uno: Limitato (~2KB RAM)
   - Usa PROGMEM per salvare in Flash invece di RAM

3. **Performance**:
   - Nel simulatore: drawBitmap è veloce (pixel-per-pixel)
   - Su Arduino reale: Dipende dal microcontrollore

4. **Colori**:
   - Pixel "1" = colorato (usa il colore specificato)
   - Pixel "0" = trasparente (non disegnato)
   - Per sfondo diverso, usa `fillRect` prima di `drawBitmap`

---

## 🐛 Troubleshooting

### "Bitmap 'xxx' non trovata"
- Verifica che l'array sia dichiarato con `PROGMEM`
- Controlla che il nome nell'array corrisponda a quello in drawBitmap()
- Assicurati che la dichiarazione sia PRIMA di setup()

### "L'immagine appare corrotta"
- Verifica width e height in drawBitmap()
- Controlla che i byte dell'array siano corretti
- Usa un convertitore affidabile (image2cpp)

### "L'immagine è al contrario/ruotata"
- Il formato è: bit MSB first, byte per byte, row-major
- Prova ad invertire i bit se necessario
- Usa l'opzione corretta nel convertitore

---

## 📝 Esempio dal Tuo File

Il tuo file `graphic.txt` contiene:
```cpp
const unsigned char manufacture[] PROGMEM = {
  0x00, 0x00, 0x00, ... // 5000 bytes
};

tft.drawBitmap(100, 100, manufacture, 200, 200, 0xadff00);
```

Questo disegna:
- **Bitmap**: manufacture (200×200 pixel)
- **Posizione**: x=100, y=100
- **Colore**: 0xadff00 (verde lime brillante)
- **Dimensione**: 5000 bytes (200×200/8 = 5000)

---

## ✨ Novità v2.2

- ✅ Supporto completo bitmap monocromatiche
- ✅ Parsing automatico array `PROGMEM`
- ✅ Rendering pixel-perfect
- ✅ Qualsiasi dimensione supportata
- ✅ Più bitmap nello stesso sketch

Buon divertimento con le tue immagini! 🎨
