def format_greeting(name: str, surname: str) -> str:
  return f"Cześć {name} {surname}!"


if __name__ == "__main__":
  greeting = format_greeting("John", "Gothic")
  print(greeting)