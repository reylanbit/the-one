import pygame
from typing import List, Optional, Type
from src.algorithms.base import SortingAlgorithm
from src.algorithms import ALGORITHMS
from src.utils.metrics import SortMetrics
from src.utils.list_generator import ListGenerator
from src.utils.sound_manager import SoundManager

class Controller:
    """Gerencia o estado da aplicação, eventos e execução dos algoritmos."""

    def __init__(self, list_size: int = 100):
        self.list_size = list_size
        self.data: List[int] = []
        self.original_data: List[int] = []
        self.metrics = SortMetrics()
        self.sound_manager = SoundManager()
        
        self.algorithm_name = "Bubble Sort"
        self.algorithm_class: Type[SortingAlgorithm] = ALGORITHMS[self.algorithm_name]
        self.sorting_gen = None
        
        self.is_paused = True
        self.is_sorting = False
        self.speed = 1.0  # Multiplicador de velocidade (1x)
        self.step_by_step = False
        
        self.comparing = []
        self.swapping = []
        self.sorted_indices = []
        
        self.shuffle()

    def shuffle(self, mode: str = "random"):
        """Gera uma nova lista baseada no modo selecionado."""
        self.stop_sorting()
        if mode == "random":
            self.data = ListGenerator.generate_random(self.list_size)
        elif mode == "reversed":
            self.data = ListGenerator.generate_reversed(self.list_size)
        elif mode == "almost_sorted":
            self.data = ListGenerator.generate_almost_sorted(self.list_size)
        elif mode == "few_distinct":
            self.data = ListGenerator.generate_few_distinct(self.list_size)
        
        self.original_data = list(self.data)
        self.metrics.reset()
        self.sorted_indices = []
        self.comparing = []
        self.swapping = []

    def reset(self):
        """Restaura a lista original."""
        self.stop_sorting()
        self.data = list(self.original_data)
        self.metrics.reset()
        self.sorted_indices = []
        self.comparing = []
        self.swapping = []

    def stop_sorting(self):
        """Para a ordenação atual."""
        self.is_sorting = False
        self.sorting_gen = None
        self.metrics.stop()

    def start_sorting(self):
        """Inicia a ordenação."""
        if not self.is_sorting:
            algo_instance = self.algorithm_class(self.data, self.metrics)
            self.sorting_gen = algo_instance.run()
            self.is_sorting = True
            self.is_paused = False
            self.metrics.start()
        else:
            self.is_paused = not self.is_paused

    def set_algorithm(self, name: str):
        """Troca o algoritmo selecionado."""
        if name in ALGORITHMS:
            self.algorithm_name = name
            self.algorithm_class = ALGORITHMS[name]
            self.reset()

    def update(self):
        """Atualiza o estado da ordenação (avança um passo)."""
        if self.is_sorting and not self.is_paused:
            self.metrics.update_time()
            try:
                # O número de passos por frame depende da velocidade e do tamanho da lista
                # Modo Turbo: Para listas > 200 elementos, aumentamos a velocidade base
                base_steps = 1
                if len(self.data) > 200:
                    base_steps = 10
                
                steps = max(base_steps, int(self.speed * base_steps))
                
                # Se a velocidade for muito baixa (< 1), usamos um acumulador
                if self.speed < 1:
                    # Simulação simples de slow motion
                    if pygame.time.get_ticks() % (int(1/self.speed)) != 0:
                        return

                for _ in range(steps):
                    result = next(self.sorting_gen)
                    self.data, self.comparing, self.swapping, self.sorted_indices = result
                    
                    # Som apenas em velocidades razoáveis para não sobrecarregar
                    if steps < 5:
                        if self.swapping:
                            self.sound_manager.play_swap()
                        elif self.comparing:
                            self.sound_manager.play_compare()
            except StopIteration:
                self.stop_sorting()

    def handle_event(self, event: pygame.event.Event):
        """Trata eventos de teclado e mouse."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.start_sorting()
            elif event.key == pygame.K_r:
                self.reset()
            elif event.key == pygame.K_s:
                self.shuffle()
            elif event.key == pygame.K_UP:
                self.speed = min(50.0, self.speed + 1.0)
            elif event.key == pygame.K_DOWN:
                self.speed = max(0.5, self.speed - 1.0)
            elif event.key == pygame.K_1:
                self.set_algorithm("Bubble Sort")
            elif event.key == pygame.K_2:
                self.set_algorithm("Selection Sort")
            elif event.key == pygame.K_3:
                self.set_algorithm("Insertion Sort")
            elif event.key == pygame.K_4:
                self.set_algorithm("Merge Sort")
            elif event.key == pygame.K_5:
                self.set_algorithm("Quick Sort")
            elif event.key == pygame.K_a: # Modo quase ordenado
                self.shuffle("almost_sorted")
            elif event.key == pygame.K_z: # Modo reverso
                self.shuffle("reversed")
            elif event.key == pygame.K_f: # Poucos valores distintos
                self.shuffle("few_distinct")
            elif event.key == pygame.K_RIGHT: # Passo a passo
                if self.is_sorting:
                    self.is_paused = True
                    self.step_forward()

    def step_forward(self):
        """Avança exatamente um passo na ordenação."""
        if self.is_sorting:
            try:
                result = next(self.sorting_gen)
                self.data, self.comparing, self.swapping, self.sorted_indices = result
                self.metrics.update_time()
                
                if self.swapping:
                    self.sound_manager.play_swap()
                elif self.comparing:
                    self.sound_manager.play_compare()
            except StopIteration:
                self.stop_sorting()
