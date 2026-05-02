from typing import List, Generator, Tuple
from .base import SortingAlgorithm

class MergeSort(SortingAlgorithm):
    """Implementação do algoritmo Merge Sort."""

    def run(self) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        yield from self._merge_sort(0, len(self.data) - 1)
        self.is_finished = True
        yield self.data, [], [], list(range(len(self.data)))

    def _merge_sort(self, l: int, r: int) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        if l < r:
            m = l + (r - l) // 2
            yield from self._merge_sort(l, m)
            yield from self._merge_sort(m + 1, r)
            yield from self._merge(l, m, r)

    def _merge(self, l: int, m: int, r: int) -> Generator[Tuple[List[int], List[int], List[int], List[int]], None, None]:
        n1 = m - l + 1
        n2 = r - m

        L = [self.data[l + i] for i in range(n1)]
        R = [self.data[m + 1 + j] for j in range(n2)]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            self.metrics.add_comparison()
            yield self.data, [l + i, m + 1 + j], [], []
            
            if L[i] <= R[j]:
                self.data[k] = L[i]
                i += 1
            else:
                self.data[k] = R[j]
                j += 1
            
            self.metrics.add_swap() # No merge sort, atribuições contam como operações custosas
            yield self.data, [], [k], []
            k += 1

        while i < n1:
            self.data[k] = L[i]
            i += 1
            k += 1
            yield self.data, [], [k-1], []

        while j < n2:
            self.data[k] = R[j]
            j += 1
            k += 1
            yield self.data, [], [k-1], []
