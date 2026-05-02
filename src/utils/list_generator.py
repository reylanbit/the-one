import random
from typing import List

class ListGenerator:
    """Gerador de listas para visualização de algoritmos de ordenação."""

    @staticmethod
    def generate_random(size: int, min_val: int = 10, max_val: int = 500) -> List[int]:
        """Gera uma lista de inteiros aleatórios."""
        return [random.randint(min_val, max_val) for _ in range(size)]

    @staticmethod
    def generate_reversed(size: int, min_val: int = 10, max_val: int = 500) -> List[int]:
        """Gera uma lista ordenada de forma decrescente."""
        lst = ListGenerator.generate_random(size, min_val, max_val)
        lst.sort(reverse=True)
        return lst

    @staticmethod
    def generate_almost_sorted(size: int, min_val: int = 10, max_val: int = 500, swaps: int = 5) -> List[int]:
        """Gera uma lista quase ordenada com alguns elementos trocados."""
        lst = ListGenerator.generate_random(size, min_val, max_val)
        lst.sort()
        for _ in range(swaps):
            idx1 = random.randint(0, size - 1)
            idx2 = random.randint(0, size - 1)
            lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
        return lst

    @staticmethod
    def generate_few_distinct(size: int, distinct_count: int = 5, min_val: int = 10, max_val: int = 500) -> List[int]:
        """Gera uma lista com poucos valores distintos."""
        distinct_values = [random.randint(min_val, max_val) for _ in range(distinct_count)]
        return [random.choice(distinct_values) for _ in range(size)]
