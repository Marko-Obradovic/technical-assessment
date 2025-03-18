# Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD
# Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind

[
    {
        "constituency": "Cardiff West",
        "totals": [
            {
                "code": "C",
                "votes": 21313
            }
        ]
    }
]


codes = {
    "C": "Conservative Party",
    "L": "Labour Party",
    "UKIP": "UKIP",
    "LD": "Liberal Democrats",
    "G": "Green Party",
    "Ind": "Independent",
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



def generate_totals(split_entry: list[str]) -> list[tuple[str]]:
    # Loop through entry after idx 0 in steps of 2 (enumerating)
    # create a tuple - first we reference the number, then 
    totals = []
    for i in range(1, len(split_entry), 2):
        totals.append((split_entry[i], split_entry[i+1]))
    return totals    

def format_totals(totals: list[tuple[str]]) -> list[dict[str, str]]:
    # [("1", "A"), ("2", "B")]
    # [{"votes": "1", "party_code": "A"}, {"votes": "2", "party_code": "B"}]
    formatted_totals = []
    for total in totals:
        formatted_totals.append({"votes": total[0], "party_code": total[-1]})
    return formatted_totals


def format_entry(entry: str) -> dict:
    '''
    Split the entry
    separate out the totals
    format the totals
    add the constituency to the dictionary
    add the totals to the dictionary
    return the dictionary
    '''

    formatted_entry = {}

    split_entry = entry.split(", ")

    totals = generate_totals(split_entry)
    formatted_totals = format_totals(totals)

    formatted_entry["constituency"] = split_entry[0]
    formatted_entry["totals"] = formatted_totals

    return formatted_entry


def generate_formatted_entries(entries: list[str]) -> list[dict]:
    # Loop through entries
    # Format each one into a dict (format_entry), then store it in a list
    # Output a list of dict (representing formatted entries)
    formatted_entries = []
    for entry in entries:
        formatted_entries.append(format_entry(entry))
    return formatted_entries





def format_one_entry_to_standard_result(formatted_entry: dict) -> dict:
    # TODO
    constituency_name = formatted_entry.get("constituency")
    parties = []
    for totals in formatted_entry.get("totals"):
        parties.append(codes[totals["party_code"]])
    return parties

    


def generate_standard_result(formatted_entries: list[dict]) -> dict:
    # TODO
    ...    


def read_csv_file() -> list[str]:
    # Open the csv
    # for each line, add the line as a string to a list
    # Return that list
    ...
