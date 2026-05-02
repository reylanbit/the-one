from .bubble import BubbleSort
from .selection import SelectionSort
from .insertion import InsertionSort
from .quick import QuickSort
from .merge import MergeSort

ALGORITHMS = {
    "Bubble Sort": BubbleSort,
    "Selection Sort": SelectionSort,
    "Insertion Sort": InsertionSort,
    "Quick Sort": QuickSort,
    "Merge Sort": MergeSort
}
