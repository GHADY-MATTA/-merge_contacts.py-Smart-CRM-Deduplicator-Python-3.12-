import unittest
from merge_contacts import merge_contacts

class TestMergeContacts(unittest.TestCase):
    def test_merge_by_email_case_insensitive(self):
        input_data = [
            {
                "id": 1, "first_name": "Ada", "last_name": "Lovelace",
                "email": "ada@acme.io", "company_id": 5,
                "phone": "+1 555-1", "title": "CTO", "created_at": "2025-05-01"
            },
            {
                "id": 2, "first_name": "Ada", "last_name": "Lovelace",
                "email": "Ada@acme.io", "company_id": 5,
                "phone": None, "title": "Chief Tech Officer", "created_at": "2025-05-03"
            }
        ]
        result = merge_contacts(input_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["phone"], "+1 555-1")
        self.assertEqual(result[0]["title"], "Chief Tech Officer")

    def test_merge_by_name_company(self):
        input_data = [
            {
                "id": 1, "first_name": "John", "last_name": "Doe",
                "email": None, "company_id": 1,
                "phone": None, "title": "Manager", "created_at": "2025-05-01"
            },
            {
                "id": 2, "first_name": "John", "last_name": "Doe",
                "email": None, "company_id": 1,
                "phone": "+1 555-5", "title": "Senior Manager", "created_at": "2025-05-03"
            }
        ]
        result = merge_contacts(input_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["phone"], "+1 555-5")
        self.assertEqual(result[0]["title"], "Senior Manager")

    def test_no_merge(self):
        input_data = [
            {
                "id": 1, "first_name": "Alan", "last_name": "Turing",
                "email": "alan@acme.io", "company_id": 5,
                "phone": "+1 555-2", "title": "Engineer", "created_at": "2025-05-02"
            }
        ]
        result = merge_contacts(input_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

if __name__ == "__main__":
    unittest.main()
