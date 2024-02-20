import pytest
from code_challenges.linked_list.linked_list import Linked_List


# @pytest.mark.skip("TODO")
def test_kth_from_end_zero():
    linked_list = Linked_List()
    values = ["apples", "bananas", "cucumbers"]
    for value in values:
        linked_list.insert(value)
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_one():
    linked_list = Linked_List()
    values = ["apples", "bananas", "cucumbers"]
    for value in values:
        linked_list.insert(value)
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_two():
    linked_list = Linked_List()
    values = ["apples", "bananas", "cucumbers"]
    for value in values:
        linked_list.insert(value)
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_kth_from_end_out_of_range():
    linked_list = Linked_List()
    values = ["apples", "bananas", "cucumbers"]
    for value in values:
        linked_list.insert(value)
    with pytest.raises(IndexError):
        linked_list.kth_from_end(3)


# @pytest.mark.skip("TODO")
def test_kth_from_end_under_range():
    linked_list = Linked_List()
    values = ["apples", "bananas", "cucumbers"]
    for value in values:
        linked_list.insert(value)
    with pytest.raises(IndexError):
        linked_list.kth_from_end(-1)


# @pytest.mark.skip("TODO")
def test_kth_from_end_size_one():
    linked_list = Linked_List()
    linked_list.insert("apples")
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected


def test_kth_from_end_middle():
    linked_list = Linked_List()
    values = ["apples", "peaches", "kiwis", "mangoes", "blueberries", "strawberries", "bananas", "cucumbers"]
    for value in values:
        linked_list.append(value)
    actual = linked_list.kth_from_end(4)
    expected = "mangoes"
    assert actual == expected