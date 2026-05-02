from typing import List, Generator, Tuple
from .base import SortingAlgorithm

class QuickSort(SortingAlgorithm):
    """Implementação do algoritmo Quick Sort com pivô no final."""

    def run(self) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        yield from self._quick_sort(0, len(self.data) - 1)
        self.is_finished = True
        yield self.data, [], [], list(range(len(self.data)))

    def _quick_sort(self, low: int, high: int) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        if low < high:
            # part_idx é o índice do pivô após a partição
            # Usaremos um gerador intermediário para capturar o valor de part_idx
            partition_gen = self._partition(low, high)
            part_idx = None
            try:
                while True:
                    val = next(partition_gen)
                    if isinstance(val, int):
                        part_idx = val
                    else:
                        yield val
            except StopIteration as e:
                part_idx = e.value

            yield from self._quick_sort(low, part_idx - 1)
            yield from self._quick_sort(part_idx + 1, high)

    def _partition(self, low: int, high: int) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, int]:
        pivot = self.data[high]
        i = low - 1
        
        for j in range(low, high):
            self.metrics.add_comparison()
            yield self.data, [j, high], [], []
            
            if self.data[j] <= pivot:
                i += 1
                self.metrics.add_swap()
                self.data[i], self.data[j] = self.data[j], self.data[i]
                yield self.data, [], [i, j], []
        
        self.metrics.add_swap()
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        yield self.data, [], [i + 1, high], []
        
        return i + 1
