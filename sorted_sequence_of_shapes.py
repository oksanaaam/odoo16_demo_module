import math


def circle_area(radius: float) -> float:
    return math.pi * math.pow(radius, 2)


def rectangle_area(arr: list) -> list:
    return arr[0] * arr[1]


def sort_by_area(array: list) -> list:
    areas = [rectangle_area(shape) if isinstance(shape, list) else circle_area(shape) for shape in array]
    return sorted(array, key=lambda shape: areas[array.index(shape)])


if __name__ == "__main__":
    array = [[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]]
    print(sort_by_area(array))  # Output: [[1.342, 3.212], 1.23, [4.23, 6.43], 3.444]
