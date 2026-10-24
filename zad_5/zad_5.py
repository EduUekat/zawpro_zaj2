def check_sum_condition(a: int, b: int, c: int) -> bool:
  return (a + b) >= c


if __name__ == "__main__":
  wynik = check_sum_condition(3, 4, 7)
  print(wynik)  # True