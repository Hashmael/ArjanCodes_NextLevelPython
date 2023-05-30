import asyncio
import datetime

async def fetch_data(url: str) -> str:
  # Simulate network delay
  await asyncio.sleep(2)
  return f"Data from {url} collected at {datetime.datetime.now():%H:%M:%S:%f}"

async def main() -> None:
  urls = [
    "https://www.arjancodes.com",
    "https://www.google.com",
    "https://www.python.org",
  ]
  data = await asyncio.gather(*[fetch_data(url) for url in urls])
  print(f'{datetime.datetime.now():%H:%M:%S:%f}: Collected all data')
  for datum in data:
    print(datum)

if __name__ == "__main__":
  asyncio.run(main())