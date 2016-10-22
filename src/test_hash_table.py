# -*- coding: utf-8 -*-
"""File tests our hash table implementation."""
from hash_table import HashTable
import pytest


@pytest.fixture(scope="function")
def create_ht():
    """Create instance of a hash table."""
    return HashTable()


@pytest.fixture(scope="function")
def second_ht():
    """Create instance of a hash table with the 2nd hash function."""
    return HashTable(hashing_algorithm='strong')


def test_hash_table_init(create_ht):
    """Test our init sets up a hash_list attribute that is a list."""
    assert isinstance(create_ht.hash_list, list)
    assert '_hash' in create_ht.hashing_algorithm


def test_hash_table_init_2nd_hash(second_ht):
    """Test our init sets up a hash_list attribute that is a list."""
    assert isinstance(second_ht.hash_list, list)
    assert '_hash_not_naive' in second_ht.hashing_algorithm


def test_hash_table_init_bucket_size(create_ht):
    """Test our init sets up a hash_list attribute that is a list."""
    assert len(create_ht.hash_list) == 10


def test_hash_table_init_error_when_algorithm_not_found():
    """Test our init sets up a hash_list attribute that is a list."""
    with pytest.raises(KeyError) as e:
        HashTable(hashing_algorithm='unknown')
    assert 'Hashing algorithm not found' in str(e)


def test_hash_table_hash(create_ht):
    """Test hash table _hash method converts key into a number."""
    hashed_value = create_ht._hash('ab')
    assert hashed_value == 195


def test_hash_table_2nd_hash(second_ht):
    """Test hash table _hash method converts key into a number."""
    hashed_value = second_ht._hash_not_naive('ab')
    assert hashed_value == 9798


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


def test_hash_table_set_method_2nd_hash(second_ht):
    """Test set method adds key and value to the hash table."""
    second_ht.set('xy', "Hi Will")
    assert second_ht.hash_list[1] == [('xy', 'Hi Will')]


def test_hash_table_get_method_2nd_hash(second_ht):
    """Test get method returns value associated with key used."""
    second_ht.set('xyz', 'Hi Nic')
    assert second_ht.get('xyz') == 'Hi Nic'


def test_hash_table_get_key_not_in_hash_table_2nd_hash(second_ht):
    """Test get method for non existant key returns None."""
    assert second_ht.get('z') is None
