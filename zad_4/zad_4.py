def is_even(number: int) -> bool:
  return number % 2 == 0


if __name__ == "__main__":
  czy_parzysta = is_even(4)
  if czy_parzysta:
    print("Liczba parzysta")
  else:
    print("Liczba nieparzysta")