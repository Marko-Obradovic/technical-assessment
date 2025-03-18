codes = {
    "C": "Conservative Party",
    "L": "Labour Party"
    "UKIP": "UKIP"
    "LD": "Liberal Democrats"
    "G": "Green Party"
    "Ind": "Independent"
    "SNP": "SNP"
}

'''
[{
    "constituency": "Cardiff West",
    "totals": [
            {"votes": 11014}
            {"party_code": "C"}
        ]
        }]
'''

entry = "Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD"

entries = [
        "Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD",
        "Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind"
        ]


def format_entry(entry: str) -> dict:
    # TODO
    ...


def generate_formatted_entries(entries: list[str]) -> list[dict]:
    # Loop through entries
    # Format each one into a dict (format_entry), then store it in a list
    # Output a list of dict (representing formatted entries)
    ...


def read_csv_file() -> list[str]:
    # Open the csv
    # for each line, add the line as a string to a list
    # Return that list
    ...
