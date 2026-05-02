import pygame
from typing import List, Tuple, Dict
from src.utils.metrics import SortMetrics

# Cores
COLOR_BACKGROUND = (30, 30, 30)
COLOR_BAR_DEFAULT = (100, 149, 237)  # Cornflower Blue
COLOR_BAR_COMPARING = (220, 20, 60)   # Crimson Red
COLOR_BAR_SWAPPING = (255, 215, 0)    # Gold
COLOR_BAR_SORTED = (50, 205, 50)     # Lime Green
COLOR_TEXT = (240, 240, 240)
COLOR_UI_BG = (45, 45, 45)

class Drawer:
    """Responsável por renderizar a visualização e interface no Pygame."""

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.ui_height = 120
        self.viz_height = self.height - self.ui_height
        
        # Fontes
        pygame.font.init()
        self.font_main = pygame.font.SysFont('Arial', 16)
        self.font_title = pygame.font.SysFont('Arial', 20, bold=True)

    def draw(self, 
             data: List[int], 
             metrics: SortMetrics, 
             algorithm_name: str,
             comparing: List[int] = [], 
             swapping: List[int] = [], 
             sorted_indices: List[int] = [],
             fps: int = 0):
        """Desenha o estado atual da visualização."""
        self.screen.fill(COLOR_BACKGROUND)
        
        # 1. Desenhar Área de Visualização (Barras)
        if data:
            self._draw_bars(data, comparing, swapping, sorted_indices)
            
        # 2. Desenhar Área de UI
        self._draw_ui(metrics, algorithm_name, len(data), fps)
        
        pygame.display.flip()

    def _draw_bars(self, data: List[int], comparing: List[int], swapping: List[int], sorted_indices: List[int]):
        n = len(data)
        bar_width = self.width / n
        max_val = max(data) if data else 1
        
        # Margem superior para não encostar no topo
        padding_top = 20
        available_height = self.viz_height - padding_top
        
        for i, val in enumerate(data):
            # Calcular altura proporcional
            bar_height = (val / max_val) * available_height
            
            # Definir cor
            color = COLOR_BAR_DEFAULT
            if i in swapping:
                color = COLOR_BAR_SWAPPING
            elif i in comparing:
                color = COLOR_BAR_COMPARING
            elif i in sorted_indices:
                color = COLOR_BAR_SORTED
            
            # Desenhar retângulo
            # x, y, width, height
            rect = pygame.Rect(
                i * bar_width, 
                self.viz_height - bar_height, 
                bar_width - (1 if n < 100 else 0), # Espaçamento se houver poucas barras
                bar_height
            )
            pygame.draw.rect(self.screen, color, rect)

    def _draw_ui(self, metrics: SortMetrics, algorithm_name: str, list_size: int, fps: int):
        # Fundo da UI
        ui_rect = pygame.Rect(0, self.viz_height, self.width, self.ui_height)
        pygame.draw.rect(self.screen, COLOR_UI_BG, ui_rect)
        pygame.draw.line(self.screen, (100, 100, 100), (0, self.viz_height), (self.width, self.viz_height), 2)

        # Informações
        margin = 20
        col1_x = margin
        col2_x = self.width // 3
        col3_x = (self.width // 3) * 2
        
        y_start = self.viz_height + 15
        line_spacing = 25

        # Coluna 1: Algoritmo e Status
        title_surf = self.font_title.render(f"Algoritmo: {algorithm_name}", True, COLOR_TEXT)
        self.screen.blit(title_surf, (col1_x, y_start))
        
        size_surf = self.font_main.render(f"Tamanho da Lista: {list_size}", True, COLOR_TEXT)
        self.screen.blit(size_surf, (col1_x, y_start + line_spacing * 2))

        # Coluna 2: Métricas
        comp_surf = self.font_main.render(f"Comparações: {metrics.comparisons}", True, COLOR_TEXT)
        self.screen.blit(comp_surf, (col2_x, y_start))
        
        swap_surf = self.font_main.render(f"Trocas: {metrics.swaps}", True, COLOR_TEXT)
        self.screen.blit(swap_surf, (col2_x, y_start + line_spacing))
        
        time_surf = self.font_main.render(f"Tempo: {metrics.elapsed_time:.2f}s", True, COLOR_TEXT)
        self.screen.blit(time_surf, (col2_x, y_start + line_spacing * 2))

        # Coluna 3: Controles/FPS
        fps_surf = self.font_main.render(f"FPS: {fps}", True, (150, 150, 150))
        self.screen.blit(fps_surf, (col3_x, y_start))
        
        controls_text = "[SPACE] Iniciar/Pausar  [R] Reset  [S] Embaralhar  [UP/DOWN] Velocidade"
        controls_surf = self.font_main.render(controls_text, True, (200, 200, 200))
        self.screen.blit(controls_surf, (col1_x, self.height - 30))
