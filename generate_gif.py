import pygame
import imageio
import os
from src.algorithms.bubble import BubbleSort
from src.algorithms.quick import QuickSort
from src.utils.metrics import SortMetrics
from src.utils.list_generator import ListGenerator
from src.visualization.drawer import Drawer

def generate_demo_gif(output_path="demo.gif", duration=0.05):
    print("Iniciando geração do GIF demo...")
    pygame.init()
    
    # Configurações
    WIDTH, HEIGHT = 1000, 600
    screen = pygame.Surface((WIDTH, HEIGHT))
    drawer = Drawer(screen)
    
    list_size = 50
    data_bubble = ListGenerator.generate_random(list_size)
    data_quick = list(data_bubble)
    
    metrics_bubble = SortMetrics()
    metrics_quick = SortMetrics()
    
    algo_bubble = BubbleSort(data_bubble, metrics_bubble)
    algo_quick = QuickSort(data_quick, metrics_quick)
    
    gen_bubble = algo_bubble.run()
    gen_quick = algo_quick.run()
    
    frames = []
    
    # Para o GIF, vamos mostrar o Bubble Sort e depois o Quick Sort
    # Ou poderíamos tentar dividir a tela, mas vamos manter simples: 
    # Mostrar os primeiros 50 passos de cada um
    
    print("Capturando frames do Bubble Sort...")
    for i in range(100):
        try:
            data, comp, swap, sorted_idx = next(gen_bubble)
            if i % 2 == 0: # Pular alguns frames para o GIF não ficar gigante
                drawer.draw(data, metrics_bubble, "Bubble Sort (Demo)", comp, swap, sorted_idx)
                frame = pygame.surfarray.array3d(screen)
                frame = frame.transpose([1, 0, 2]) # Corrigir orientação do pygame
                frames.append(frame)
        except StopIteration:
            break
            
    print("Capturando frames do Quick Sort...")
    for i in range(100):
        try:
            data, comp, swap, sorted_idx = next(gen_quick)
            if i % 2 == 0:
                drawer.draw(data, metrics_quick, "Quick Sort (Demo)", comp, swap, sorted_idx)
                frame = pygame.surfarray.array3d(screen)
                frame = frame.transpose([1, 0, 2])
                frames.append(frame)
        except StopIteration:
            break

    print(f"Salvando {len(frames)} frames em {output_path}...")
    imageio.mimsave(output_path, frames, duration=duration)
    pygame.quit()
    print("GIF gerado com sucesso!")

if __name__ == "__main__":
    # Garantir que o diretório existe
    os.makedirs("assets", exist_ok=True)
    generate_demo_gif()
