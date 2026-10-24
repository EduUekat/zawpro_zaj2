#1.2.1
def multiply_by_two_for(numbers: list) -> list:
  result = []
  for num in numbers:
    result.append(num * 2)
  return result


#1.2.2
def multiply_by_two_comprehension(numbers: list) -> list:
  return [num * 2 for num in numbers]


if __name__ == "__main__":
  liczby = [1, 2, 3, 4, 5]
  print("Pętla for:", multiply_by_two_for(liczby))
  print("Lista składana:", multiply_by_two_comprehension(liczby))