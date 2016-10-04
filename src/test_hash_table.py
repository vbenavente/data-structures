# -*- coding: utf-8 -*-
"""File tests our hash table implementation."""
from hash_table import HashTable
import pytest


@pytest.fixture(scope="function")
def create_ht():
    """Create instance of a hash table."""
    return HashTable()


def test_hash_table_init(create_ht):
    """Test our init sets up a hash_list attribute that is a list."""
    assert isinstance(create_ht.hash_list, list)


def test_hash_table_hash(create_ht):
    """Test hash table _hash method converts key into a number."""
    hashed_value = create_ht._hash('a')
    assert hashed_value == 97


def test_hash_table_hash_is_int(create_ht):
    """Test _hash method passed int as key returns key."""
    hashed_value = create_ht._hash(8374)
    assert hashed_value == 8374


def test_hash_table_hash_other_structure(create_ht):
    """Test _hash returns none when not passing int or string."""
    hashed_value = create_ht._hash([1, 2, 'a'])
    assert hashed_value is None


def test_hash_table_set_method(create_ht):
    """Test set method adds key and value to the hash table."""
    create_ht.set('x', "Hi Will")
    assert create_ht.hash_list[0] == [("x", "Hi Will")]


def test_hash_table_get_method(create_ht):
    """Test get method returns value associated with key used."""
    create_ht.set('x', "Hi Nic")
    assert create_ht.get('x') == "Hi Nic"


def test_hash_table_get_key_not_in_hash_table(create_ht):
    """Test get method for non existant key returns None."""
    assert create_ht.get('z') is None
