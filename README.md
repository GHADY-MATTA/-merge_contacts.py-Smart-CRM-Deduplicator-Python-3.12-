# -merge_contacts.py-Smart-CRM-Deduplicator-Python-3.12-
implement a CLI tool merge_contacts.py that reads a list of contacts from STDIN (newline-delimited JSON), merges duplicates, and writes the cleaned list to STDOUT.  Two contacts are duplicates if their email fields match case-insensitively OR their (first_name, last_name, company_id) triples match exactly.
