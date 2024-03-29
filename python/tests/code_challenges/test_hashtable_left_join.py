import pytest
from code_challenges.hashtable_left_join.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = {
        'diligent': ['employed', 'idle'], 
        'fond': ['enamored', 'averse'], 
        'guide': ['usher', 'follow'], 
        'outfit': ['garb', None], 
        'wrath': ['anger', 'delight']
        }

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_empty_maps():
    map1 = {}
    map2 = {}
    expected = {}
    actual = left_join(map1, map2)
    assert actual == expected

def test_no_intersecting_maps():
    map1 = {"a": 1, "b": 2, "c": 3}
    map2 = {"x": 10, "y": 20, "z": 30}
    expected = {"a": [1, None], "b": [2, None], "c": [3, None]}
    actual = left_join(map1, map2)
    assert actual == expected