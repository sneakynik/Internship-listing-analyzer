"""
Internship Listings Analyzer
-----------------------------
Pulls live tech internship data from the SimplifyJobs/Summer2027-Internships
GitHub repo (updated daily by Pitt CSC + Simplify) and analyzes it:
  - which companies are posting the most roles
  - which locations show up most
  - which keywords (backend, data, full stack, etc.) are most common in titles

Run with:  python internship_analyzer.py
Requires:  pip install requests matplotlib
"""

import requests
from collections import Counter
import csv
import matplotlib.pyplot as plt

# The repo stores all internship postings as one big JSON file.
LISTINGS_URL = (
    "https://raw.githubusercontent.com/SimplifyJobs/"
    "Summer2027-Internships/dev/.github/scripts/listings.json"
)

# Keywords we care about — feel free to edit this list.
ROLE_KEYWORDS = [
    "software", "backend", "front end", "frontend", "full stack",
    "data", "machine learning", "ai", "systems", "security",
    "mobile", "cloud", "devops",
]


def fetch_listings():
    """Download and parse the internship listings JSON."""
    print("Fetching latest internship listings...")
    response = requests.get(LISTINGS_URL, timeout=15)
    response.raise_for_status()
    return response.json()


def filter_active(listings):
    """Keep only postings that are still open."""
    return [job for job in listings if job.get("active")]


def count_by_company(listings, top_n=10):
    counts = Counter(job.get("company_name", "Unknown") for job in listings)
    return counts.most_common(top_n)


def count_by_location(listings, top_n=10):
    counts = Counter()
    for job in listings:
        for loc in job.get("locations", []):
            counts[loc] += 1
    return counts.most_common(top_n)


def count_by_keyword(listings):
    counts = Counter()
    for job in listings:
        title = job.get("title", "").lower()
        for keyword in ROLE_KEYWORDS:
            if keyword in title:
                counts[keyword] += 1
    return counts.most_common()


def save_to_csv(listings, filename="active_internships.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Company", "Title", "Locations", "URL"])
        for job in listings:
            writer.writerow([
                job.get("company_name", ""),
                job.get("title", ""),
                ", ".join(job.get("locations", [])),
                job.get("url", ""),
            ])
    print(f"Saved {len(listings)} active listings to {filename}")


def plot_top_companies(company_counts, filename="top_companies.png"):
    companies = [c for c, _ in company_counts]
    counts = [n for _, n in company_counts]

    plt.figure(figsize=(9, 5))
    plt.barh(companies[::-1], counts[::-1], color="#2f5fa8")
    plt.xlabel("Number of Open Internship Postings")
    plt.title("Top Companies Hiring Interns Right Now")
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Saved chart to {filename}")


def main():
    all_listings = fetch_listings()
    active = filter_active(all_listings)
    print(f"\nTotal postings: {len(all_listings)}")
    print(f"Currently active: {len(active)}\n")

    print("Top 10 companies hiring interns:")
    top_companies = count_by_company(active)
    for company, count in top_companies:
        print(f"  {company:<30} {count}")

    print("\nTop 10 locations:")
    for location, count in count_by_location(active):
        print(f"  {location:<30} {count}")

    print("\nMost common keywords in job titles:")
    for keyword, count in count_by_keyword(active):
        print(f"  {keyword:<20} {count}")

    save_to_csv(active)
    plot_top_companies(top_companies)


if __name__ == "__main__":
    main()
