import time
from dataclasses import dataclass

@dataclass
class SortMetrics:
    """Classe para armazenar métricas de execução de algoritmos de ordenação."""
    comparisons: int = 0
    swaps: int = 0
    start_time: float = 0.0
    elapsed_time: float = 0.0
    is_running: bool = False

    def reset(self) -> None:
        """Reseta todas as métricas para os valores iniciais."""
        self.comparisons = 0
        self.swaps = 0
        self.start_time = 0.0
        self.elapsed_time = 0.0
        self.is_running = False

    def start(self) -> None:
        """Inicia a contagem de tempo."""
        self.start_time = time.time()
        self.is_running = True

    def stop(self) -> None:
        """Para a contagem de tempo e calcula o tempo total decorrido."""
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False

    def update_time(self) -> None:
        """Atualiza o tempo decorrido sem parar a contagem."""
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time

    def add_comparison(self) -> None:
        """Incrementa o contador de comparações."""
        self.comparisons += 1

    def add_swap(self) -> None:
        """Incrementa o contador de trocas."""
        self.swaps += 1
