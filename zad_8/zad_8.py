import requests


class Brewery:

  def __init__(
      self,
      id: str,
      name: str,
      brewery_type: str,
      city: str,
      state: str,
      country: str,
  ):
    self.id: str = id
    self.name: str = name
    self.brewery_type: str = brewery_type
    self.city: str = city
    self.state: str = state
    self.country: str = country

  def __str__(self) -> str:
    return (
        f"Brewery: {self.name} (Typ: {self.brewery_type}) - Miasto: {self.city},"
        f" Kraj: {self.country}"
    )


def fetch_breweries() -> list[Brewery]:
  url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
  response = requests.get(url)
  data = response.json()

  breweries_list = []
  for item in data:
    brewery = Brewery(
        id=item.get("id", ""),
        name=item.get("name", ""),
        brewery_type=item.get("brewery_type", ""),
        city=item.get("city", ""),
        state=item.get("state", ""),
        country=item.get("country", ""),
    )
    breweries_list.append(brewery)

  return breweries_list


if __name__ == "__main__":
  breweries = fetch_breweries()
  for brewery in breweries:
    print(brewery)