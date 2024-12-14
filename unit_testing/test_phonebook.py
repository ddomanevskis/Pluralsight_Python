import unittest
from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = Phonebook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add('bob', '12345')
        number = self.phonebook.lookup('bob')
        self.assertEqual(number, '12345')

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    def test_empty_phonebook_is_consistent(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    def test_is_consitent_with_different_entries(self):
        self.phonebook.add('bob', '12345')
        self.phonebook.add('anna', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsitent_with_duplicate_entries(self):
        self.phonebook.add('bob', '12345')
        self.phonebook.add('sue', '12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicates_prefix(self):
        self.phonebook.add('bob', '12345')
        self.phonebook.add('sue', '123')
        self.assertFalse(self.phonebook.is_consistent())


if __name__ == '__main__':
    unittest.main()
