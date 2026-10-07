# Internship Listings Analyzer

A Python tool that pulls live tech internship data and surfaces trends —
which companies are hiring the most interns right now, where the roles are
located, and which skills/keywords show up most in job titles.

## What it does

- Fetches real, currently-active internship postings from the
  [SimplifyJobs/Summer2027-Internships](https://github.com/SimplifyJobs/Summer2027-Internships)
  repo, which is updated daily by Pitt CSC and Simplify.
- Counts postings by company and by location.
- Scans job titles for common role keywords (backend, full stack, data,
  machine learning, etc.) to show what's in demand.
- Exports the filtered, active listings to a CSV.
- Generates a bar chart of the top hiring companies.

## Why I built this

As a CS student actively applying to internships, I wanted a fast way to
see which companies are hiring right now and what skills show up most in
postings — instead of manually scrolling through hundreds of listings.

## Tech used

- Python
- `requests` for pulling live JSON data
- `matplotlib` for visualization
- `csv` for exporting results

## How to run it

```bash
pip install requests matplotlib
python internship_analyzer.py
```

This prints a summary to the terminal and creates two files:
- `active_internships.csv` — every currently active listing
- `top_companies.png` — a chart of the top hiring companies

## Example output

```
Total postings: 480
Currently active: 210

Top 10 companies hiring interns:
  Google                         8
  Microsoft                      7
  ...
```

## Possible next steps

- Add a `--keyword` command-line flag to filter listings by role type
- Track how listings change day to day
- Add a simple web dashboard

## Author

Nylan Mack — [GitHub](https://github.com/sneakynik) · [LinkedIn](https://www.linkedin.com/in/nylan-mack-830438339)
