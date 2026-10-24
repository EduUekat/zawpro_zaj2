def list_contains_value(elements: list, value: int) -> bool:
  return value in elements


if __name__ == "__main__":
  znaleziono = list_contains_value([1, 2, 3, 4, 5], 3)
  print(znaleziono)  # True