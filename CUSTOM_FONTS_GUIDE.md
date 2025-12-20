# 🎨 Guida Font Personalizzati

## Come usare font personalizzati nel simulatore TFT

### 📥 Dove trovare font

#### Font per display digitali/RPM:
- **Digital-7** - Font stile display LCD digitale
  - Download: https://www.1001fonts.com/digital-7-font.html
  - Perfetto per: RPM, velocità, temperature
  
- **DSEG7** - Font stile seven-segment display
  - Download: https://github.com/keshikan/DSEG/releases
  - Perfetto per: Display numerici, contatori
  
- **Calculator** - Font stile calcolatrice
  - Download: https://www.dafont.com/calculator.font
  
#### Font automotive/racing:
- **Eurostile** - Font usato in molte auto sportive
- **Microgramma** - Font racing classico
- **Orbitron** - Font futuristico per HUD

#### Font gratuiti:
- Google Fonts: https://fonts.google.com
- DaFont: https://www.dafont.com
- 1001 Fonts: https://www.1001fonts.com

---

## 🚀 Metodi per usare font personalizzati

### Metodo 1: Font specifico per un numero font

Perfetto quando vuoi usare un font "digital" solo per Font 7 (grandi numeri RPM):

```python
#!/usr/bin/env python3
from tft_simulator_interactive import TFTSimulator

sim = TFTSimulator()

# Font 7 usa digital-7.ttf per numeri grandi
sim.setCustomFont(7, "./fonts/digital-7.ttf")

# Font 8 usa un altro font
sim.setCustomFont(8, "./fonts/calculator.ttf")

# Gli altri font (1-6) usano il font di sistema di default

# Carica e esegui il codice Arduino
with open("main_interface.txt") as f:
    code = f.read()
sim.parse_and_execute(code)

# ... resto del loop pygame ...
```

### Metodo 2: Font default per tutti

Usa lo stesso font personalizzato per TUTTI i font (1-8):

```python
sim = TFTSimulator()

# Tutti i font useranno questo
sim.setDefaultCustomFont("./fonts/myfont.ttf")

# Esegui il codice...
```

### Metodo 3: Configurazione diretta

Massimo controllo - configura ogni font:

```python
sim = TFTSimulator()

sim.custom_fonts = {
    1: "./fonts/small.ttf",      # Font piccolo
    2: "./fonts/small.ttf",      # Font piccolo
    4: "./fonts/medium.ttf",     # Font medio
    6: "./fonts/large.ttf",      # Font grande
    7: "./fonts/digital-7.ttf",  # Font digitale per RPM
    8: "./fonts/calculator.ttf"  # Font enorme
}

# Font 3 e 5 non specificati → usano font di sistema
```

### Metodo 4: Modifica nel main()

Modifica direttamente `tft_simulator_interactive.py`:

```python
def main():
    # ... dopo sim = TFTSimulator() ...
    
    # Aggiungi questa riga:
    sim.setCustomFont(7, "./fonts/digital-7.ttf")
    
    # ... resto del codice ...
```

---

## 📂 Struttura directory consigliata

```
il_tuo_progetto/
├── tft_simulator_interactive.py
├── main_interface.txt
└── fonts/
    ├── digital-7.ttf
    ├── calculator.ttf
    └── orbitron.ttf
```

Poi usa percorsi relativi:
```python
sim.setCustomFont(7, "./fonts/digital-7.ttf")
```

---

## 💡 Esempio completo: Dashboard RPM

**File: dashboard_rpm.txt**
```cpp
#include <TFT_eSPI.h>
TFT_eSPI tft = TFT_eSPI();

void setup() {
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);
  
  // Titolo normale
  tft.setCursor(10, 10);
  tft.setTextFont(2);
  tft.setTextColor(TFT_WHITE);
  tft.println("ENGINE RPM");
  
  // RPM con font digitale (Font 7)
  tft.setCursor(50, 50);
  tft.setTextFont(7);
  tft.setTextColor(0xEB8015);
  tft.println("5280");
}
void loop() {}
```

**File: run_with_custom_font.py**
```python
#!/usr/bin/env python3
import pygame
from tft_simulator_interactive import TFTSimulator

# Crea simulatore
sim = TFTSimulator()

# Font digitale per Font 7 (RPM)
sim.setCustomFont(7, "./fonts/digital-7.ttf")

# Carica il codice
with open("dashboard_rpm.txt") as f:
    code = f.read()

sim.parse_and_execute(code)

# Loop pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    sim.clock.tick(60)

pygame.quit()
```

**Esegui:**
```bash
python run_with_custom_font.py
```

---

## 🔧 Troubleshooting

### "FileNotFoundError: font not found"
- Verifica che il percorso sia corretto
- Usa percorsi assoluti se relativi non funzionano:
  ```python
  import os
  font_path = os.path.abspath("./fonts/digital-7.ttf")
  sim.setCustomFont(7, font_path)
  ```

### "Il font non cambia"
- Controlla che il numero font sia corretto (1-8)
- Verifica che il file .ttf sia valido
- Controlla i messaggi di errore nella console

### "Font troppo grande/piccolo"
Le dimensioni sono automatiche, ma puoi modificare il mapping:
```python
# Nel codice del simulatore:
sim.font_sizes[7] = 60  # Cambia da 75 a 60
```

### Font .otf vs .ttf
Pygame supporta sia .ttf che .otf! Usa quello che hai.

---

## 🎯 Font consigliati per tipo di display

| Tipo Display | Font Consigliato | Uso |
|--------------|------------------|-----|
| RPM/Velocità | Digital-7, DSEG7 | Font digitali grandi |
| Temperature | Calculator | Numeri chiari |
| Titoli | Orbitron, Eurostile | Header moderni |
| Testo body | Roboto, Open Sans | Leggibilità |
| Racing HUD | Microgramma Bold | Look sportivo |

---

## 📝 Note importanti

1. I font personalizzati funzionano SOLO con `tft_simulator_interactive.py` (pygame)
2. La versione PNG usa font di sistema (Pillow/PIL)
3. I font devono essere file .ttf o .otf
4. La dimensione è gestita automaticamente in base al font number
5. Se un font custom non viene trovato, usa il font di sistema di default

---

## ✅ Checklist

- [ ] Scarica il font .ttf/.otf
- [ ] Crea cartella `fonts/` nel progetto
- [ ] Copia il font nella cartella
- [ ] Aggiungi `sim.setCustomFont(7, "./fonts/yourfont.ttf")`
- [ ] Verifica che il percorso sia corretto
- [ ] Esegui il simulatore!

Buon divertimento! 🚀
