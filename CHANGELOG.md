# Changelog

## v2.2 - Bitmap Support (Dicembre 2024) 🖼️

### ✨ Nuova Funzionalità: Supporto Immagini/Bitmap!
- **drawBitmap()** - Disegna bitmap monocromatiche (1 bit per pixel)
- **Parsing automatico** degli array `const unsigned char[] PROGMEM`
- **Qualsiasi dimensione** supportata
- **Multi-bitmap** - Più immagini nello stesso sketch
- **Colori personalizzati** - Usa qualsiasi colore per i pixel "1"

### 📊 Formato Supportato
- Bitmap monocromatiche (1 bit/pixel)
- Array in formato Arduino PROGMEM
- Compatibile con convertitori standard (image2cpp)

### 🎯 Esempio d'Uso
```cpp
const unsigned char logo[] PROGMEM = {
  0x00, 0x7F, 0xFF, ... // dati bitmap
};

tft.drawBitmap(100, 50, logo, 64, 64, TFT_WHITE);
```

### 📖 Documentazione
Vedi [BITMAP_GUIDE.md](BITMAP_GUIDE.md) per guida completa.

---

## v2.1 - Font 7 Size Correction (Dicembre 2024) 🔧

### 🐛 Fix Critico
- **RISOLTO**: Font 7 ora ha la dimensione corretta (75px invece di 48px)
- **RISOLTO**: Font 8 aumentato a 90px per essere veramente enorme

### 📊 Dimensioni Font Corrette (Basate su Test Reali)
Il problema era che i font "Free" (6, 7, 8) in TFT_eSPI hanno dimensioni molto diverse dai font built-in:

| Font | Vecchia | Nuova | Tipo |
|------|---------|-------|------|
| 1 | 8px | 8px | Built-in |
| 2 | 16px | 16px | Built-in |
| 3 | 24px | 24px | Standard |
| 4 | 26px | 26px | Built-in |
| 5 | 32px | 32px | Standard |
| 6 | 48px | 48px | FreeFont |
| 7 | ❌ 48px | ✅ **75px** | FreeSans (MOLTO GRANDE!) |
| 8 | ❌ 75px | ✅ **90px** | FreeFont (ENORME!) |

Il Font 7 è usato tipicamente per display numerici grandi (RPM, velocità, temperatura) e deve essere prominente!

---

## v2.0 - Font Fix Update (Dicembre 2024)

### 🐛 Bug Fix Principali
- **RISOLTO**: I font ora cambiano dimensione correttamente
- **RISOLTO**: Il cursore si aggiorna correttamente con `print()` e `println()`
- **RISOLTO**: Font multipli sulla stessa riga funzionano perfettamente

### ✨ Miglioramenti

#### Dimensioni Font Corrette
Ora le dimensioni dei font corrispondono accuratamente a quelle di TFT_eSPI:
- Font 1: 8px (tiny)
- Font 2: 16px (small)
- Font 3: 24px (medium) - **AGGIUNTO**
- Font 4: 26px (large)
- Font 5: 32px (larger) - **AGGIUNTO**
- Font 6: 48px (very large)
- Font 7: 48px (very large - 7-segment style)
- Font 8: 75px (huge)

#### Tracking Cursore Migliorato
- `print()` ora muove il cursore orizzontalmente (sulla stessa riga)
- `println()` muove il cursore a capo (nuova riga)
- Il cursore tiene traccia della posizione corretta anche con font multipli

#### Cambio Font Inline
Ora puoi scrivere codice come questo e funziona perfettamente:
```cpp
tft.setTextFont(2);
tft.print("Small ");
tft.setTextFont(4);
tft.print("Medium ");
tft.setTextFont(7);
tft.print("BIG");
```

### 🎯 Esempi Aggiunti
- `test_fonts.txt` - Test di tutte le dimensioni font
- `comprehensive_test.txt` - Demo completa con cambio font inline e RPM gauge

### 📝 Note Tecniche
- Migliore calcolo della larghezza del testo per tracking cursore accurato
- Spaziatura tra righe migliorata (20% extra per leggibilità)
- Font 3 e 5 ora disponibili (erano mancanti nella v1.0)

---

## v1.0 - Rilascio Iniziale

### ✨ Funzionalità
- Supporto forme geometriche complete
- Supporto testo base
- Rotazione display (0-3)
- Colori TFT predefiniti + RGB565/RGB888
- Cicli for annidati
- Variabili ed espressioni matematiche
- Export PNG scalato 2x
