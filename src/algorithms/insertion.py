from typing import List, Generator, Tuple
from .base import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
    """Implementação do algoritmo Insertion Sort."""

    def run(self) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        n = len(self.data)
        sorted_indices = [0]
        
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            
            while j >= 0:
                self.metrics.add_comparison()
                yield self.data, [j, j + 1], [], sorted_indices
                
                if self.data[j] > key:
                    self.metrics.add_swap()
                    self.data[j + 1] = self.data[j]
                    j -= 1
                    yield self.data, [], [j + 1, j + 2], sorted_indices
                else:
                    break
            
            self.data[j + 1] = key
            sorted_indices = list(range(i + 1))
            yield self.data, [], [], sorted_indices
            
        self.is_finished = True
        yield self.data, [], [], list(range(n))
