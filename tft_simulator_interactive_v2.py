#!/usr/bin/env python3
"""
TFT_eSPI Display Simulator (Interactive Pygame Version)
Simula un display TFT su PC con finestra interattiva
"""

import re
import pygame
import sys
from typing import Tuple

# Colori TFT_eSPI
TFT_COLORS = {
    'TFT_BLACK': (0, 0, 0),
    'TFT_WHITE': (255, 255, 255),
    'TFT_RED': (255, 0, 0),
    'TFT_GREEN': (0, 255, 0),
    'TFT_BLUE': (0, 0, 255),
    'TFT_YELLOW': (255, 255, 0),
    'TFT_CYAN': (0, 255, 255),
    'TFT_MAGENTA': (255, 0, 255),
    'TFT_ORANGE': (255, 165, 0),
    'TFT_PINK': (255, 192, 203),
    'TFT_PURPLE': (128, 0, 128),
    'TFT_NAVY': (0, 0, 128),
    'TFT_DARKGREEN': (0, 128, 0),
    'TFT_DARKCYAN': (0, 128, 128),
    'TFT_MAROON': (128, 0, 0),
    'TFT_OLIVE': (128, 128, 0),
    'TFT_LIGHTGREY': (211, 211, 211),
    'TFT_DARKGREY': (128, 128, 128),
    'TFT_GREENYELLOW': (173, 255, 47),
    'TFT_BROWN': (150, 75, 0),
}

class TFTSimulator:
    def __init__(self, width=480, height=320):
        """Inizializza il simulatore"""
        self.default_width = width
        self.default_height = height
        self.width = width
        self.height = height
        self.rotation = 0
        self.scale = 1  # Nessuno scaling - dimensione 1:1
        
        # Text properties
        self.cursor_x = 0
        self.cursor_y = 0
        self.text_color = (255, 255, 255)
        self.text_font_size = 1
        self.text_font_num = 1
        
        # Font sizes (v2.1 corrected)
        self.font_sizes = {
            1: 8, 2: 16, 3: 24, 4: 26, 5: 32,
            6: 48, 7: 75, 8: 90
        }
        
        # Custom font paths (opzionali)
        # Puoi specificare font TTF/OTF personalizzati per ogni font number
        # Esempio: self.custom_fonts[7] = "/path/to/digital-7.ttf"
        self.custom_fonts = {}
        
        # Se vuoi usare lo stesso font custom per tutti:
        self.default_custom_font = "bittypix_monospace/Bittypix Monospace.ttf"
        #self.default_custom_font = None
        
        # Bitmap storage per immagini monocromatiche
        self.bitmaps = {}  # {nome_array: (width, height, bytes_data)}
        
        pygame.init()
        self.update_display()
        pygame.display.set_caption("TFT_eSPI Simulator (Interactive)")
        self.clock = pygame.time.Clock()
        
    def update_display(self):
        """Aggiorna display in base alla rotazione"""
        if self.rotation in [1, 3]:
            w, h = self.height, self.width
        else:
            w, h = self.width, self.height
            
        self.screen = pygame.display.set_mode((w * self.scale, h * self.scale))
        self.surface = pygame.Surface((w, h))
        
    def parse_color(self, color_str: str) -> Tuple[int, int, int]:
        """Converte colore TFT in RGB"""
        color_str = color_str.strip()
        if color_str in TFT_COLORS:
            return TFT_COLORS[color_str]
        
        if color_str.startswith('0x'):
            try:
                value = int(color_str, 16)
                if value <= 0xFFFF:  # RGB565
                    r = ((value >> 11) & 0x1F) * 255 // 31
                    g = ((value >> 5) & 0x3F) * 255 // 63
                    b = (value & 0x1F) * 255 // 31
                    return (r, g, b)
                else:  # RGB888
                    r = (value >> 16) & 0xFF
                    g = (value >> 8) & 0xFF
                    b = value & 0xFF
                    return (r, g, b)
            except:
                pass
        
        return (255, 255, 255)
    
    def parse_value(self, value_str: str, variables: dict) -> int:
        """Valuta espressioni matematiche"""
        value_str = value_str.strip()
        for var, val in variables.items():
            value_str = value_str.replace(var, str(val))
        try:
            return int(eval(value_str))
        except:
            return 0
    
    def setRotation(self, rotation: int):
        """Imposta rotazione (0-3)"""
        self.rotation = rotation % 4
        if self.rotation in [1, 3]:
            self.width, self.height = self.default_height, self.default_width
        else:
            self.width, self.height = self.default_width, self.default_height
        self.update_display()
    
    def fillScreen(self, color: Tuple[int, int, int]):
        """Riempie schermo"""
        self.surface.fill(color)
    
    def drawRect(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int]):
        """Rettangolo vuoto"""
        pygame.draw.rect(self.surface, color, (x, y, w, h), 1)
    
    def fillRect(self, x: int, y: int, w: int, h: int, color: Tuple[int, int, int]):
        """Rettangolo pieno"""
        pygame.draw.rect(self.surface, color, (x, y, w, h))
    
    def drawCircle(self, x: int, y: int, r: int, color: Tuple[int, int, int]):
        """Cerchio vuoto"""
        pygame.draw.circle(self.surface, color, (x, y), r, 1)
    
    def fillCircle(self, x: int, y: int, r: int, color: Tuple[int, int, int]):
        """Cerchio pieno"""
        pygame.draw.circle(self.surface, color, (x, y), r)
    
    def drawLine(self, x0: int, y0: int, x1: int, y1: int, color: Tuple[int, int, int]):
        """Linea"""
        pygame.draw.line(self.surface, color, (x0, y0), (x1, y1), 1)
    
    def drawRoundRect(self, x: int, y: int, w: int, h: int, r: int, color: Tuple[int, int, int]):
        """Rettangolo arrotondato vuoto"""
        pygame.draw.rect(self.surface, color, (x, y, w, h), 1, border_radius=r)
    
    def fillRoundRect(self, x: int, y: int, w: int, h: int, r: int, color: Tuple[int, int, int]):
        """Rettangolo arrotondato pieno"""
        pygame.draw.rect(self.surface, color, (x, y, w, h), border_radius=r)
    
    def drawTriangle(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int]):
        """Triangolo vuoto"""
        pygame.draw.polygon(self.surface, color, [(x0, y0), (x1, y1), (x2, y2)], 1)
    
    def fillTriangle(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int, color: Tuple[int, int, int]):
        """Triangolo pieno"""
        pygame.draw.polygon(self.surface, color, [(x0, y0), (x1, y1), (x2, y2)])
    
    def drawBitmap(self, x: int, y: int, bitmap_name: str, w: int, h: int, color: Tuple[int, int, int]):
        """
        Disegna una bitmap monocromatica (1 bit per pixel)
        
        Args:
            x, y: Posizione top-left
            bitmap_name: Nome dell'array bitmap nel codice
            w, h: Larghezza e altezza in pixel
            color: Colore per i pixel "1" (i pixel "0" sono trasparenti)
        """
        if bitmap_name not in self.bitmaps:
            print(f"⚠️  Bitmap '{bitmap_name}' non trovata")
            return
        
        bitmap_data = self.bitmaps[bitmap_name]
        
        # Disegna pixel per pixel
        for row in range(h):
            for col in range(w):
                # Calcola byte e bit index
                bit_index = row * w + col
                byte_index = bit_index // 8
                bit_offset = 7 - (bit_index % 8)  # MSB first
                
                if byte_index < len(bitmap_data):
                    # Leggi il bit
                    byte_val = bitmap_data[byte_index]
                    bit_set = (byte_val >> bit_offset) & 1
                    
                    # Se il bit è 1, disegna il pixel
                    if bit_set:
                        px = x + col
                        py = y + row
                        if 0 <= px < self.width and 0 <= py < self.height:
                            self.surface.set_at((px, py), color)
    
    # ===== TEXT SUPPORT =====
    
    def setCursor(self, x: int, y: int, font=None):
        """Posiziona cursore testo"""
        self.cursor_x = x
        self.cursor_y = y
        if font is not None:
            self.text_font_num = font
    
    def setTextColor(self, color):
        """Imposta colore testo"""
        if isinstance(color, tuple):
            self.text_color = color
        elif isinstance(color, str):
            self.text_color = self.parse_color(color)
        else:
            # Assume sia un valore hex
            color_str = f"0x{color:X}" if isinstance(color, int) else str(color)
            self.text_color = self.parse_color(color_str)
    
    def setTextFont(self, font_num: int):
        """Imposta font (1-8)"""
        self.text_font_num = font_num
    
    def setTextSize(self, size: int):
        """Imposta moltiplicatore dimensione"""
        self.text_font_size = size
    
    def setCustomFont(self, font_number: int, font_path: str):
        """
        Imposta un font personalizzato per un font number specifico
        
        Args:
            font_number: Numero del font (1-8)
            font_path: Percorso al file .ttf o .otf
            
        Esempio:
            sim.setCustomFont(7, "/path/to/digital-7.ttf")
        """
        self.custom_fonts[font_number] = font_path
        print(f"✓ Font personalizzato impostato per font {font_number}: {font_path}")
    
    def setDefaultCustomFont(self, font_path: str):
        """
        Imposta un font personalizzato da usare per tutti i font
        
        Args:
            font_path: Percorso al file .ttf o .otf
            
        Esempio:
            sim.setDefaultCustomFont("/path/to/myfont.ttf")
        """
        self.default_custom_font = font_path
        print(f"✓ Font di default personalizzato impostato: {font_path}")
    
    def get_pygame_font(self):
        """Ottiene font pygame con dimensione corretta"""
        base_size = self.font_sizes.get(self.text_font_num, 16)
        size = int(base_size * self.text_font_size)
        
        # 1. Controlla se c'è un font custom per questo numero
        if self.text_font_num in self.custom_fonts:
            try:
                return pygame.font.Font(self.custom_fonts[self.text_font_num], size)
            except Exception as e:
                print(f"⚠️  Errore caricamento font custom: {e}")
        
        # 2. Usa il font custom di default se specificato
        if self.default_custom_font:
            try:
                return pygame.font.Font(self.default_custom_font, size)
            except Exception as e:
                print(f"⚠️  Errore caricamento font di default: {e}")
        
        # 3. Fallback a font di sistema
        try:
            return pygame.font.SysFont('dejavusans', size, bold=True)
        except:
            return pygame.font.Font(None, size)
    
    def print_text(self, text: str):
        """Stampa testo (inline)"""
        if not text:
            return
        
        font = self.get_pygame_font()
        text_surface = font.render(str(text), True, self.text_color)
        self.surface.blit(text_surface, (self.cursor_x, self.cursor_y))
        
        # Aggiorna cursore X (muove orizzontalmente)
        self.cursor_x += text_surface.get_width()
    
    def println_text(self, text: str):
        """Stampa testo con a capo"""
        self.print_text(text)
        # Va a capo
        self.cursor_x = 0
        line_height = self.font_sizes.get(self.text_font_num, 8)
        self.cursor_y += int(line_height * 1.2)
    
    def drawString(self, text: str, x: int, y: int, font=None):
        """Disegna stringa in posizione"""
        old_x, old_y = self.cursor_x, self.cursor_y
        old_font = self.text_font_num
        
        self.cursor_x, self.cursor_y = x, y
        if font is not None:
            self.text_font_num = font
        
        self.print_text(text)
        
        self.cursor_x, self.cursor_y = old_x, old_y
        self.text_font_num = old_font
    
    def render(self):
        """Renderizza su finestra"""
        scaled = pygame.transform.scale(self.surface, 
                                        (self.surface.get_width() * self.scale,
                                         self.surface.get_height() * self.scale))
        self.screen.blit(scaled, (0, 0))
        pygame.display.flip()
    
    def parse_and_execute(self, code: str):
        """Esegue codice Arduino"""
        variables = {}
        
        # === PARSING BITMAP ARRAYS ===
        # Cerca array di bitmap tipo: const unsigned char nome[] PROGMEM = { ... };
        bitmap_pattern = r'const\s+unsigned\s+char\s+(\w+)\[\]\s+PROGMEM\s*=\s*\{([^}]+)\}'
        for match in re.finditer(bitmap_pattern, code, re.DOTALL):
            bitmap_name = match.group(1)
            bitmap_data_str = match.group(2)
            
            # Estrae i valori esadecimali
            hex_values = re.findall(r'0x([0-9A-Fa-f]{2})', bitmap_data_str)
            bitmap_bytes = bytes([int(val, 16) for val in hex_values])
            
            # Salva la bitmap
            self.bitmaps[bitmap_name] = bitmap_bytes
            print(f"✓ Bitmap '{bitmap_name}' caricata: {len(bitmap_bytes)} bytes")
        
        # Estrae dimensioni display
        width_match = re.search(r'int\s+displayWidth\s*=\s*(\d+)', code)
        height_match = re.search(r'int\s+displayHeight\s*=\s*(\d+)', code)
        
        if width_match and height_match:
            self.default_width = int(width_match.group(1))
            self.default_height = int(height_match.group(1))
            self.width = self.default_width
            self.height = self.default_height
        
        # Estrae variabili int
        for match in re.finditer(r'int\s+(\w+)\s*=\s*([^;]+);', code):
            var_name = match.group(1)
            var_value = match.group(2)
            try:
                variables[var_name] = self.parse_value(var_value, variables)
            except:
                pass
        
        # Trova setup() con parsing corretto delle parentesi
        setup_start = re.search(r'void\s+setup\s*\(\s*\)\s*{', code)
        if not setup_start:
            print("⚠️  Funzione setup() non trovata")
            return
        
        # Parsing parentesi bilanciate
        start_pos = setup_start.end()
        brace_count = 1
        pos = start_pos
        
        while pos < len(code) and brace_count > 0:
            if code[pos] == '{':
                brace_count += 1
            elif code[pos] == '}':
                brace_count -= 1
            pos += 1
        
        setup_code = code[start_pos:pos-1]
        
        # Esegue comandi non-for
        lines = setup_code.split('\n')
        in_for = False
        brace_count = 0
        
        for line in lines:
            stripped = line.strip()
            
            if 'for' in stripped and 'int' in stripped and '(' in stripped:
                in_for = True
                brace_count = 0
            
            if in_for:
                brace_count += stripped.count('{') - stripped.count('}')
                if brace_count <= 0 and '}' in stripped:
                    in_for = False
                continue
            
            if stripped and not stripped.startswith('//'):
                self.execute_command(stripped, variables)
        
        # Esegue cicli for
        self.execute_for_loops(setup_code, variables)
        
        self.render()
    
    def execute_for_loops(self, code_text: str, vars_dict: dict):
        """Esegue cicli for"""
        lines = code_text.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            for_match = re.match(r'for\s*\(\s*int\s+(\w+)\s*=\s*(\d+)\s*;\s*\1\s*<\s*([^;]+)\s*;\s*(.+?)\s*\)\s*{?', line)
            
            if for_match:
                loop_var = for_match.group(1)
                start = int(for_match.group(2))
                end_expr = for_match.group(3).strip()
                increment_expr = for_match.group(4).strip()
                
                end = self.parse_value(end_expr, vars_dict)
                
                # Determina incremento
                increment = 1
                if '+=' in increment_expr:
                    inc_match = re.search(r'\+=\s*(\d+)', increment_expr)
                    if inc_match:
                        increment = int(inc_match.group(1))
                elif '=' in increment_expr and '+' in increment_expr:
                    inc_match = re.search(r'=\s*\w+\s*\+\s*(\d+)', increment_expr)
                    if inc_match:
                        increment = int(inc_match.group(1))
                    else:
                        inc_match = re.search(r'=\s*\w+\s*\+\s*(\w+)', increment_expr)
                        if inc_match:
                            increment = vars_dict.get(inc_match.group(1), 1)
                
                # Trova corpo del for
                if '{' in line:
                    brace_count = line.count('{') - line.count('}')
                    i += 1
                    body_lines = []
                    
                    while i < len(lines) and brace_count > 0:
                        body_lines.append(lines[i])
                        brace_count += lines[i].count('{') - lines[i].count('}')
                        i += 1
                    
                    if body_lines and body_lines[-1].strip() == '}':
                        body_lines = body_lines[:-1]
                    
                    body = '\n'.join(body_lines)
                else:
                    i += 1
                    body = lines[i] if i < len(lines) else ''
                    i += 1
                    continue
                
                # Esegue loop
                for loop_val in range(start, end, increment):
                    local_vars = vars_dict.copy()
                    local_vars[loop_var] = loop_val
                    
                    if 'for' in body and 'int' in body:
                        self.execute_for_loops(body, local_vars)
                    else:
                        for body_line in body.split('\n'):
                            cmd = body_line.strip()
                            if cmd and not cmd.startswith('//') and cmd != '}':
                                self.execute_command(cmd, local_vars)
            else:
                i += 1
    
    def execute_command(self, line: str, variables: dict):
        """Esegue singolo comando TFT"""
        
        # setRotation
        if 'setRotation' in line:
            match = re.search(r'setRotation\s*\(\s*(\d+)\s*\)', line)
            if match:
                self.setRotation(int(match.group(1)))
                print(f"✓ setRotation({match.group(1)})")
        
        # fillScreen
        elif 'fillScreen' in line:
            match = re.search(r'fillScreen\s*\(\s*(\w+)\s*\)', line)
            if match:
                self.fillScreen(self.parse_color(match.group(1)))
                print(f"✓ fillScreen({match.group(1)})")
        
        # drawRect
        elif 'drawRect' in line and 'fillRect' not in line and 'RoundRect' not in line:
            match = re.search(r'drawRect\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                w = self.parse_value(match.group(3), variables)
                h = self.parse_value(match.group(4), variables)
                color = self.parse_color(match.group(5))
                self.drawRect(x, y, w, h, color)
                print(f"✓ drawRect({x}, {y}, {w}, {h})")
        
        # fillRect
        elif 'fillRect' in line and 'RoundRect' not in line:
            match = re.search(r'fillRect\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                w = self.parse_value(match.group(3), variables)
                h = self.parse_value(match.group(4), variables)
                color = self.parse_color(match.group(5))
                self.fillRect(x, y, w, h, color)
                print(f"✓ fillRect({x}, {y}, {w}, {h})")
        
        # fillRoundRect
        elif 'fillRoundRect' in line:
            match = re.search(r'fillRoundRect\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                w = self.parse_value(match.group(3), variables)
                h = self.parse_value(match.group(4), variables)
                r = self.parse_value(match.group(5), variables)
                color = self.parse_color(match.group(6))
                self.fillRoundRect(x, y, w, h, r, color)
                print(f"✓ fillRoundRect({x}, {y}, {w}, {h}, {r})")
        
        # drawRoundRect
        elif 'drawRoundRect' in line:
            match = re.search(r'drawRoundRect\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                w = self.parse_value(match.group(3), variables)
                h = self.parse_value(match.group(4), variables)
                r = self.parse_value(match.group(5), variables)
                color = self.parse_color(match.group(6))
                self.drawRoundRect(x, y, w, h, r, color)
                print(f"✓ drawRoundRect({x}, {y}, {w}, {h}, {r})")
        
        # drawCircle
        elif 'drawCircle' in line and 'fillCircle' not in line:
            match = re.search(r'drawCircle\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                r = self.parse_value(match.group(3), variables)
                color = self.parse_color(match.group(4))
                self.drawCircle(x, y, r, color)
                print(f"✓ drawCircle({x}, {y}, {r})")
        
        # fillCircle
        elif 'fillCircle' in line:
            match = re.search(r'fillCircle\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                r = self.parse_value(match.group(3), variables)
                color = self.parse_color(match.group(4))
                self.fillCircle(x, y, r, color)
                print(f"✓ fillCircle({x}, {y}, {r})")
        
        # drawLine
        elif 'drawLine' in line:
            match = re.search(r'drawLine\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x0 = self.parse_value(match.group(1), variables)
                y0 = self.parse_value(match.group(2), variables)
                x1 = self.parse_value(match.group(3), variables)
                y1 = self.parse_value(match.group(4), variables)
                color = self.parse_color(match.group(5))
                self.drawLine(x0, y0, x1, y1, color)
                print(f"✓ drawLine({x0}, {y0}, {x1}, {y1})")
        
        # drawTriangle
        elif 'drawTriangle' in line and 'fillTriangle' not in line:
            match = re.search(r'drawTriangle\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x0 = self.parse_value(match.group(1), variables)
                y0 = self.parse_value(match.group(2), variables)
                x1 = self.parse_value(match.group(3), variables)
                y1 = self.parse_value(match.group(4), variables)
                x2 = self.parse_value(match.group(5), variables)
                y2 = self.parse_value(match.group(6), variables)
                color = self.parse_color(match.group(7))
                self.drawTriangle(x0, y0, x1, y1, x2, y2, color)
                print(f"✓ drawTriangle({x0}, {y0}, {x1}, {y1}, {x2}, {y2})")
        
        # fillTriangle
        elif 'fillTriangle' in line:
            match = re.search(r'fillTriangle\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x0 = self.parse_value(match.group(1), variables)
                y0 = self.parse_value(match.group(2), variables)
                x1 = self.parse_value(match.group(3), variables)
                y1 = self.parse_value(match.group(4), variables)
                x2 = self.parse_value(match.group(5), variables)
                y2 = self.parse_value(match.group(6), variables)
                color = self.parse_color(match.group(7))
                self.fillTriangle(x0, y0, x1, y1, x2, y2, color)
                print(f"✓ fillTriangle({x0}, {y0}, {x1}, {y1}, {x2}, {y2})")
        
        # drawBitmap
        elif 'drawBitmap' in line:
            match = re.search(r'drawBitmap\s*\(\s*([^,]+),\s*([^,]+),\s*(\w+),\s*([^,]+),\s*([^,]+),\s*([^\)]+)\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                bitmap_name = match.group(3)
                w = self.parse_value(match.group(4), variables)
                h = self.parse_value(match.group(5), variables)
                color = self.parse_color(match.group(6))
                self.drawBitmap(x, y, bitmap_name, w, h, color)
                print(f"✓ drawBitmap({x}, {y}, {bitmap_name}, {w}, {h})")
        
        # setCursor
        elif 'setCursor' in line:
            match = re.search(r'setCursor\s*\(\s*([^,]+),\s*([^,]+)(?:,\s*(\d+))?\s*\)', line)
            if match:
                x = self.parse_value(match.group(1), variables)
                y = self.parse_value(match.group(2), variables)
                font = int(match.group(3)) if match.group(3) else None
                self.setCursor(x, y, font)
                print(f"✓ setCursor({x}, {y}{f', {font}' if font else ''})")
        
        # setTextColor
        elif 'setTextColor' in line:
            match = re.search(r'setTextColor\s*\(\s*([^,\)]+)', line)
            if match:
                color_str = match.group(1).strip()
                if color_str.startswith('0x'):
                    color_val = int(color_str, 16)
                    if color_val <= 0xFFFF:
                        r = ((color_val >> 11) & 0x1F) * 255 // 31
                        g = ((color_val >> 5) & 0x3F) * 255 // 63
                        b = (color_val & 0x1F) * 255 // 31
                    else:
                        r = (color_val >> 16) & 0xFF
                        g = (color_val >> 8) & 0xFF
                        b = color_val & 0xFF
                    self.setTextColor((r, g, b))
                    print(f"✓ setTextColor({color_str}) -> RGB({r},{g},{b})")
                else:
                    self.setTextColor(color_str)
                    print(f"✓ setTextColor({color_str})")
        
        # setTextFont
        elif 'setTextFont' in line:
            match = re.search(r'setTextFont\s*\(\s*(\d+)\s*\)', line)
            if match:
                font_num = int(match.group(1))
                self.setTextFont(font_num)
                print(f"✓ setTextFont({font_num})")
        
        # setTextSize
        elif 'setTextSize' in line:
            match = re.search(r'setTextSize\s*\(\s*(\d+)\s*\)', line)
            if match:
                size = int(match.group(1))
                self.setTextSize(size)
                print(f"✓ setTextSize({size})")
        
        # print / println
        elif 'tft.println' in line or 'tft.print(' in line:
            match = re.search(r'(?:print|println)\s*\(\s*["\']([^"\']+)["\']|(?:print|println)\s*\(\s*(\w+)', line)
            if match:
                text = match.group(1) if match.group(1) else str(variables.get(match.group(2), match.group(2)))
                if 'println' in line:
                    self.println_text(text)
                else:
                    self.print_text(text)
                print(f"✓ print('{text}')")
        
        # drawString
        elif 'drawString' in line:
            match = re.search(r'drawString\s*\(\s*["\']([^"\']+)["\']\s*,\s*([^,]+),\s*([^,]+)(?:,\s*(\d+))?\s*\)', line)
            if match:
                text = match.group(1)
                x = self.parse_value(match.group(2), variables)
                y = self.parse_value(match.group(3), variables)
                font = int(match.group(4)) if match.group(4) else None
                self.drawString(text, x, y, font)
                print(f"✓ drawString('{text}', {x}, {y})")

def main():
    if len(sys.argv) < 2:
        print("Uso: python tft_simulator_interactive.py <file.ino>")
        print("\nEsempio: python tft_simulator_interactive.py main_interface.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"❌ File '{filename}' non trovato")
        sys.exit(1)
    
    print(f"\n🖥️  TFT_eSPI Simulator (Interactive)")
    print(f"📁 Caricamento: {filename}\n")
    
    sim = TFTSimulator()
    sim.parse_and_execute(code)
    
    print(f"\n✅ Rendering completato!")
    print(f"📐 Dimensioni: {sim.width}x{sim.height} (Rotazione: {sim.rotation})")
    print(f"\n🎮 Premi ESC o chiudi la finestra per uscire\n")
    
    # Loop principale
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

if __name__ == "__main__":
    main()
