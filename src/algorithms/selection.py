from typing import List, Generator, Tuple
from .base import SortingAlgorithm

class SelectionSort(SortingAlgorithm):
    """Implementação do algoritmo Selection Sort."""

    def run(self) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        n = len(self.data)
        sorted_indices = []
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.metrics.add_comparison()
                yield self.data, [j, min_idx], [], sorted_indices
                
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
                    yield self.data, [min_idx], [], sorted_indices
            
            if min_idx != i:
                self.metrics.add_swap()
                self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
                yield self.data, [], [i, min_idx], sorted_indices
            
            sorted_indices.append(i)
            yield self.data, [], [], sorted_indices
            
        self.is_finished = True
        yield self.data, [], [], list(range(n))
