import json
import requests
from bs4 import BeautifulSoup

url = "https://example-university.edu/scholarships"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for item in soup.select(".scholarship-item"):
    title = item.text.strip()
    data.append({"title": title})

with open("scholarships.json", "w") as f:
    json.dump(data, f, indent=2)

print("Scholarship data saved!")
