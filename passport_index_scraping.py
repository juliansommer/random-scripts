from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver


def make_request(url: str) -> str:
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    return html


def parse_visa_info(html_text: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html_text, "html.parser")
    rows = soup.find_all("tr", class_="show-tr")
    results = []
    for row in rows:
        if not isinstance(row, Tag):
            continue  # Skip if not a Tag
        country_tag = row.find("a")
        visa_tag = row.find(
            "td",
            class_=lambda x: bool(
                x
                and (
                    "vr-bckgr" in x
                    or "vf-bckgr" in x
                    or "voa-bckgr" in x
                    or "eta-bckgr" in x
                )
            ),
        )
        country = country_tag.text.strip() if country_tag else ""
        visa_status = visa_tag.get_text(strip=True) if visa_tag else ""

        # Strip "Apply now" from end of visa status
        if visa_status.endswith("Apply now"):
            visa_status = visa_status.rsplit("Apply now", 1)[0].strip()

        results.append({"country": country, "visa_status": visa_status})
    return results


def compare_data(
    data1: list[dict[str, str]], data2: list[dict[str, str]]
) -> dict[str, tuple]:
    dict1 = {item["country"]: item["visa_status"] for item in data1}
    dict2 = {item["country"]: item["visa_status"] for item in data2}
    differences = {}

    # Check countries in both
    for country in dict1.keys() & dict2.keys():
        if dict1[country] != dict2[country]:
            differences[country] = (dict1[country], dict2[country])

    return differences


def main() -> None:
    print(
        "This program compares visa information between two places on passportindex.org"
    )
    site1 = input("Enter the URL of the first passport site: ")
    site2 = input("Enter the URL of the second passport site: ")

    r1 = make_request(site1)
    data1 = parse_visa_info(r1)

    r2 = make_request(site2)
    data2 = parse_visa_info(r2)

    diffs = compare_data(data1, data2)
    if not diffs:
        print("No differences found.")
        return

    # print out differences in a table format
    print("\n{:<25} {:<30} {:<30}".format("COUNTRY", "SITE1 STATUS", "SITE2 STATUS"))
    print("-" * 85)
    for country in sorted(diffs.keys()):
        v1, v2 = diffs[country]
        print("{:<25} {:<30} {:<30}".format(country, v1, v2))


if __name__ == "__main__":
    main()
