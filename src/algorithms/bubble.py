from typing import List, Generator, Tuple
from .base import SortingAlgorithm

class BubbleSort(SortingAlgorithm):
    """Implementação do algoritmo Bubble Sort."""

    def run(self) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        n = len(self.data)
        sorted_indices = []
        
        for i in range(n):
            for j in range(0, n - i - 1):
                self.metrics.add_comparison()
                # Yield comparando
                yield self.data, [j, j + 1], [], sorted_indices
                
                if self.data[j] > self.data[j + 1]:
                    self.metrics.add_swap()
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    # Yield trocando
                    yield self.data, [], [j, j + 1], sorted_indices
            
            sorted_indices.append(n - i - 1)
            yield self.data, [], [], sorted_indices
            
        self.is_finished = True
        yield self.data, [], [], list(range(n))
