import pytest
from src.utils.metrics import SortMetrics
from src.utils.list_generator import ListGenerator
from src.algorithms.base import SortingAlgorithm
from src.algorithms.bubble import BubbleSort
from src.algorithms.selection import SelectionSort
from src.algorithms.insertion import InsertionSort
from src.algorithms.quick import QuickSort
from src.algorithms.merge import MergeSort

# Lista de todos os algoritmos para parametrização
ALGO_CLASSES = [
    BubbleSort,
    SelectionSort,
    InsertionSort,
    QuickSort,
    MergeSort
]

@pytest.mark.parametrize("algo_class", ALGO_CLASSES)
@pytest.mark.parametrize("size", [0, 1, 2, 5, 10, 50])
def test_sorting_various_sizes(algo_class, size):
    """Testa algoritmos com diferentes tamanhos de lista."""
    data = ListGenerator.generate_random(size)
    metrics = SortMetrics()
    algo = algo_class(data, metrics)
    
    # Consumir o gerador
    for _ in algo.run():
        pass
        
    # Verificar se está ordenado
    assert all(data[i] <= data[i+1] for i in range(len(data) - 1))
    assert algo.is_sorted()

@pytest.mark.parametrize("algo_class", ALGO_CLASSES)
def test_already_sorted(algo_class):
    """Testa comportamento com lista já ordenada."""
    data = [1, 2, 3, 4, 5]
    metrics = SortMetrics()
    algo = algo_class(data, metrics)
    for _ in algo.run():
        pass
    assert data == [1, 2, 3, 4, 5]
    assert algo.is_sorted()

@pytest.mark.parametrize("algo_class", ALGO_CLASSES)
def test_reverse_sorted(algo_class):
    """Testa comportamento com lista inversamente ordenada."""
    data = [5, 4, 3, 2, 1]
    metrics = SortMetrics()
    algo = algo_class(data, metrics)
    for _ in algo.run():
        pass
    assert data == [1, 2, 3, 4, 5]
    assert algo.is_sorted()

def test_list_generation():
    """Testa se os geradores de lista funcionam como esperado."""
    size = 20
    assert len(ListGenerator.generate_random(size)) == size
    
    rev = ListGenerator.generate_reversed(size)
    assert len(rev) == size
    assert all(rev[i] >= rev[i+1] for i in range(size - 1))
    
    almost = ListGenerator.generate_almost_sorted(size)
    assert len(almost) == size

def test_base_class_abstract():
    """Verifica se a classe base lança erro se instanciada ou sem implementação."""
    with pytest.raises(TypeError):
        SortingAlgorithm([1, 2, 3], SortMetrics())

    class IncompleteAlgo(SortingAlgorithm):
        pass
    
    with pytest.raises(TypeError):
        IncompleteAlgo([1, 2, 3], SortMetrics())
