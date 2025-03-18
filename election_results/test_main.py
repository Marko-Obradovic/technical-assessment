import pytest
from main import format_totals, generate_totals, format_entry, generate_formatted_entries, generate_standard_result, format_one_entry_to_standard_result

@pytest.fixture
def entry():
    return "Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD"


@pytest.fixture
def entries():
    return ["Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD", "Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind"]


@pytest.fixture
def formatted_entries():
    return [{'constituency': 'Cardiff West', 'totals': [{'votes': '11014', 'party_code': 'C'}, {'votes': '17803', 'party_code': 'L'}, {'votes': '4923', 'party_code': 'UKIP'}, {'votes': '2069', 'party_code': 'LD'}]}, {'constituency': 'Islington South & Finsbury', 'totals': [{'votes': '22547', 'party_code': 'L'}, {'votes': '9389', 'party_code': 'C'}, {'votes': '4829', 'party_code': 'LD'}, {'votes': '3375', 'party_code': 'UKIP'}, {'votes': '3371', 'party_code': 'G'}, {'votes': '309', 'party_code': 'Ind'}]}]


@pytest.fixture
def formatted_entry():
    return {'constituency': 'Cardiff West', 'totals': [{'votes': '11014', 'party_code': 'C'}, {'votes': '17803', 'party_code': 'L'}, {'votes': '4923', 'party_code': 'UKIP'}, {'votes': '2069', 'party_code': 'LD'}]}


#------------------------------------------------ TESTS ------------------------------------------------#

def test_generate_totals():
    split_entry = ['Cardiff West', '11014', 'C', '17803', 'L', '4923', 'UKIP', '2069', 'LD']
    assert generate_totals(split_entry) == [("11014", "C"), ("17803", "L"), ("4923", "UKIP"), ("2069", "LD")] 


def test_format_totals():
    assert format_totals([('11014', 'C'), ('17803', 'L'), ('4923', 'UKIP'), ('2069', 'LD')]) == [{'votes': '11014', 'party_code': 'C'}, {'votes': '17803', 'party_code': 'L'}, {'votes': '4923', 'party_code': 'UKIP'}, {'votes': '2069', 'party_code': 'LD'}]
    

def test_format_entry(entry, formatted_entry):
    assert format_entry(entry) == formatted_entry


def test_generate_formatted_entries(entries, formatted_entries):
    assert generate_formatted_entries(entries) == formatted_entries


def test_format_one_entry_to_standard_result():
    mock_formatted_entry = {
        'constituency': 'Constituency A', 'totals': 
        [
            {'votes': '11014', 'party_code': 'C'},
            {'votes': '17803', 'party_code': 'L'}
            ]
            }
    assert format_one_entry_to_standard_result(mock_formatted_entry) == {"constituency_name": "Constituency A", "party_name": "Conservative Party", "vote_percentage": 38.2}


def test_generate_standard_result():
    mock_formatted_entries = [
        {'constituency': 'Constituency A', 'totals': 
         [
             {'votes': '11014', 'party_code': 'C'},
             {'votes': '17803', 'party_code': 'L'}
             ]
             },
        {'constituency': 'Constituency B', 'totals': 
         [
             {'votes': '22547', 'party_code': 'L'},
             {'votes': '9389', 'party_code': 'C'}
             ]
             }
             ]
    assert generate_standard_result(mock_formatted_entries) == [{"constituency_name": "Constituency A", "party_name": "Conservative Party", "vote_percentage": 38.2}, {"constituency_name": "Constituency B", "party_name": "Conservative Party", "vote_percentage": 61.8}, ]