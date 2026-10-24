import argparse
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


def fetch_breweries(city: str = None) -> list[Brewery]:
  url = "https://api.openbrewerydb.org/v1/breweries"
  params = {"per_page": 20}

  if city:
    params["by_city"] = city

  response = requests.get(url, params=params)
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
  parser = argparse.ArgumentParser(
      description="Pobieranie listy browarów z Open Brewery DB."
  )
  parser.add_argument(
      "--city", type=str, help="Filtruj browary według wybranego miasta"
  )
  args = parser.parse_args()

  breweries = fetch_breweries(city=args.city)
  for brewery in breweries:
    print(brewery)

##użycie z python zad_9.py --city="Berlin"