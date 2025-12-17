import json
import requests
from bs4 import BeautifulSoup

# Step 1: Website URL (practice site)
url = "https://www.scholarships.com/financial-aid/college-scholarships/"

# Step 2: Request with User-Agent (important for scraping)
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

scholarships = []

# Step 4: Extract data (simple & safe selector)
for item in soup.select("h3"):
    title = item.get_text(strip=True)

    if len(title) > 10:   # filter useless headings
        scholarships.append({
            "title": title
        })

# Step 5: Save to JSON file
with open("scholarships.json", "w", encoding="utf-8") as f:
    json.dump(scholarships, f, indent=2, ensure_ascii=False)

print(f"Saved {len(scholarships)} scholarships successfully!")
