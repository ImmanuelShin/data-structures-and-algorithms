import pytest
from code_challenges.linked_list.linked_list import Linked_List, Node

def test_add_node_to_end():
    ll = Linked_List()
    ll.append(1)
    assert ll.to_string() == "{ 1 } -> NULL"

def test_add_multiple_nodes_to_end():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    assert ll.to_string() == "{ 1 } -> { 2 } -> NULL"

def test_insert_node_before_middle():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 1.5)
    assert ll.to_string() == "{ 1 } -> { 1.5 } -> { 2 } -> { 3 } -> NULL"

def test_insert_node_before_first():
    ll = Linked_List()
    ll.append(1)
    ll.insert_before(1, 0)
    assert ll.to_string() == "{ 0 } -> { 1 } -> NULL"

def test_insert_node_before_end():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(3, 4)
    assert ll.to_string() == "{ 1 } -> { 2 } -> { 4 } -> { 3 } -> NULL"

def test_insert_node_after_middle():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 2.5)
    assert ll.to_string() == "{ 1 } -> { 2 } -> { 2.5 } -> { 3 } -> NULL"

def test_insert_node_after_last():
    ll = Linked_List()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 4)
    assert ll.to_string() == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"