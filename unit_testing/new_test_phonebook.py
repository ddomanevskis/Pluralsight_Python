import pytest
from new_phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    phonebook = Phonebook(tmpdir)
    yield phonebook
    phonebook.clear()


def test_lookup_by_name(phonebook):
    phonebook.add("bob", "12345")
    number = phonebook.lookup('bob')
    assert number == '12345'


def test_contains_all_names(phonebook):
    phonebook.add('bob', '12345')
    assert 'missing' in phonebook.all_names()
    assert phonebook.all_names() == {'bob', 'missing'}


def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('bob')


def test_is_consistent_with_diffrent_entries(phonebook):
    phonebook.add('bob', '12345')
    phonebook.add('mary', '67890')
    assert phonebook.is_consistent()


def test_is_consistent_with_duplicate_entries(phonebook):
    phonebook.add('bob', '12345')
    phonebook.add('mary', '12345')
    assert phonebook.is_consistent()


def test_inconsistent_with_duplicate_prefix(phonebook):
    phonebook.add('bob', '12345')
    phonebook.add('mary', '123')
    assert not phonebook.is_consistent()


@pytest.mark.parametrize(
    "entry1, entry2, is_consistent", [
        (('bob', '12345'), ('anna', '01234'), True),
        (('bob', '12345'), ('anna', '12345'), False),
        (('bob', '12345'), ('anna', '123'), False),
    ]
)


def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent
