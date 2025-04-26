import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n+1)

def cyclic123_array(n): 
    """2. Генерирует numpy массив длины 3𝑛, заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n, 2)

def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    arr = np.zeros((n, n))
    arr[0, :] = 1  # первая строка
    arr[-1, :] = 1  # последняя строка
    arr[:, 0] = 1  # первый столбец
    arr[:, -1] = 1  # последний столбец
    return arr

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    board = np.zeros((n, n), dtype=int)
    board[1::2, ::2] = 1
    board[::2, 1::2] = 1
    return board

def matrix_with_sum_index(n):
    """6. Создаёт 𝑛 × 𝑛 матрицу с (𝑖,𝑗)-элементами равным 𝑖+𝑗."""
    i = np.arange(n).reshape(n, 1)
    j = np.arange(n)
    return i + j

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив."""
    x = np.arange(a, b, dx)
    cos_values = np.cos(x)
    sin_values = np.sin(x)
    return np.vstack((cos_values, sin_values))

def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    mean = np.mean(A)
    row_sums = np.sum(A, axis=1)
    col_sums = np.sum(A, axis=0)
    return mean, row_sums, col_sums

def sort_array_by_column(A, j):
    """9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[A[:, j].argsort()]

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:  
    method == 'rectangular' - методом прямоугольника   
    method == 'trapezoidal' - методом трапеций   
    method == 'simpson' - методом Симпсона  
    """
    x = np.arange(a, b + dx, dx)
    y = f(x)
    
    if method == 'rectangular':
        # Метод прямоугольников (левые точки)
        return np.sum(y[:-1] * dx)
    elif method == 'trapezoidal':
        # Метод трапеций
        return np.sum((y[:-1] + y[1:]) * dx / 2)
    elif method == 'simpson':
        # Метод Симпсона
        n = len(x) - 1
        if n % 2 == 1:
            # Для нечетного числа интервалов
            return (dx/3) * (np.sum(y[:-2:2] + 4*y[1:-1:2] + y[2:-1:2])) + (dx/2)*(y[-2] + y[-1])
        else:
            # Для четного числа интервалов
            return (dx/3) * np.sum(y[:-1:2] + 4*y[1::2] + y[2::2])
    else:
        raise ValueError("Неизвестный метод интегрирования")
