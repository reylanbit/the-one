import pygame
import sys
from src.visualization.drawer import Drawer
from src.visualization.controller import Controller

def main():
    """Ponto de entrada principal do SortViz."""
    pygame.init()
    
    # Configurações da Janela
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 650
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("SortViz - Visualizador de Algoritmos de Ordenação")
    
    # Inicializar Componentes
    controller = Controller(list_size=100)
    drawer = Drawer(screen)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # 1. Tratar Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Repassar eventos para o controlador
            controller.handle_event(event)
            
            # Suporte a redimensionamento simples
            if event.type == pygame.VIDEORESIZE:
                new_size = event.dict['size']
                screen = pygame.display.set_mode(new_size, pygame.RESIZABLE)
                drawer = Drawer(screen)

        # 2. Atualizar Estado
        controller.update()
        
        # 3. Desenhar
        drawer.draw(
            data=controller.data,
            metrics=controller.metrics,
            algorithm_name=controller.algorithm_name,
            comparing=controller.comparing,
            swapping=controller.swapping,
            sorted_indices=controller.sorted_indices,
            fps=int(clock.get_fps())
        )
        
        # Controlar FPS (limite de 60 para não consumir CPU desnecessariamente)
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
