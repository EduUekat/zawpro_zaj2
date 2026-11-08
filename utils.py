import re
from collections import Counter

def is_palindrome(text: str) -> bool:
  """Sprawdza czy ciąg znaków jest palindromem (ignorując wielkość liter i spacje)."""
  cleaned = "".join(c.lower() for c in text if not c.isspace())
  return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
  """Zwraca n-ty element ciągu Fibonacciego."""
  if n < 0:
    raise ValueError("Wartość n nie może być ujemna.")
  if n == 0:
    return 0
  if n == 1:
    return 1

  a, b = 0, 1
  for _ in range(2, n + 1):
    a, b = b, a + b
  return b


def count_vowels(text: str) -> int:
  """Zlicza liczbę samogłosek ignorując wielkość liter."""
  vowels = set("aeiouyąęó")
  return sum(1 for c in text.lower() if c in vowels)


def calculate_discount(price: float, discount: float) -> float:
  """Zwraca cenę po zniżce. Zgłasza ValueError, jeśli zniżka jest spoza zakresu 0-1."""
  if not (0 <= discount <= 1):
    raise ValueError("Zniżka musi mieścić się w zakresie od 0 do 1.")
  return float(price * (1 - discount))


def flatten_list(nested_list: list) -> list:
  """Spłaszcza zagnieżdżoną listę."""
  result = []
  for item in nested_list:
    if isinstance(item, list):
      result.extend(flatten_list(item))
    else:
      result.append(item)
  return result


def word_frequencies(text: str) -> dict:
  """Zwraca słownik z częstością występowania słów (ignorując wielkość liter i interpunkcję)."""
  if not text:
    return {}
  words = re.findall(r"[a-ząćęłńóśźż]+", text.lower())
  return dict(Counter(words))


def is_prime(n: int) -> bool:
  """Sprawdza, czy liczba jest pierwsza (n < 2 zwraca False)."""
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True