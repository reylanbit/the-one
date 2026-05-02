from abc import ABC, abstractmethod
from typing import List, Generator, Tuple, Optional
from src.utils.metrics import SortMetrics

class SortingAlgorithm(ABC):
    """Classe base abstrata para todos os algoritmos de ordenação."""

    def __init__(self, data: List[int], metrics: SortMetrics):
        self.data = data
        self.metrics = metrics
        self.n = len(data)
        self.is_finished = False

    @abstractmethod
    def run(self) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        """
        Executa o algoritmo de ordenação passo a passo.
        
        Yields:
            Tuple contendo:
            - data: A lista atualizada.
            - comparing: Índices sendo comparados (cor vermelha).
            - swapping: Índices sendo trocados (cor amarela).
            - sorted_indices: Índices já ordenados (cor verde).
        """
        pass

    def is_sorted(self) -> bool:
        """Verifica se a lista está totalmente ordenada."""
        return all(self.data[i] <= self.data[i+1] for i in range(len(self.data) - 1))
