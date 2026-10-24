def print_every_second(numbers: list) -> None:
  for num in numbers[::2]:
    print(num)

if __name__ == "__main__":
  liczby_10 = list(range(1, 11))
  print_every_second(liczby_10)