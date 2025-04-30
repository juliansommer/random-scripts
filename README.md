# Random Scripts

- This is a collection of random scripts I have made since 2021 when I cannot be bothered working on a large scale project

## Setup

Follow these steps to run the project locally.

**Prerequisites**

Make sure the following are installed.

- [Git](https://git-scm.com)
- [Python](https://www.python.org)

**Cloning the Repository**

```bash
git clone https://github.com/juliansommer/random-scripts.git
cd random-scripts
```

**Creating a Virtual Environment**

On Windows
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

On MacOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Installing Dependencies**

```bash
pip install -r requirements.txt
```

## Files

- `australia_tax_calculator.py` is a tax calculator for Australia
- `binary_search.py` is a basic implementation of binary search
- `character_replace.py` will read a list of strings in a txt file and return all the permutations from replacing characters eg S -> $
- `factorial.py` will find factorial of a number
- `metadata.py` will read an image's metadata and EXIF data
- `passport_index_scraping.py` will scrape [Passport Index](https://www.passportindex.org/) for visa requirements for 2 countries and compare them
- `password.py` will generate a password
- `prime.py` will find all prime numbers in a txt file
- `rename.py` will mass rename files
