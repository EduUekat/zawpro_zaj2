#zad_1_3.py
def print_even_numbers(numbers: list) -> None:
  for num in numbers:
    if num % 2 == 0:
      print(num)


if __name__ == "__main__":
  liczby_10 = list(range(1, 11))
  print_even_numbers(liczby_10)