def process_lists(list1: list, list2: list) -> list:
  # Połączenie i usunięcie duplikatów za pomocą rzutowania na set
  combined_unique = set(list1 + list2)
  # Podniesienie każdego elementu do potęgi 3 i zwrócenie jako lista
  return [x**3 for x in combined_unique]


if __name__ == "__main__":
  l1 = [1, 2, 3]
  l2 = [2, 3, 4]
  print(process_lists(l1, l2))