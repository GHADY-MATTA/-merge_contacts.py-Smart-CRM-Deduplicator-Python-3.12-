# 🧠 merge_contacts.py — Smart CRM Deduplicator (Python 3.12)

In every CRM system, duplicate contacts are a recurring nightmare — cluttering data, confusing sales teams, and breaking reports.

This CLI tool intelligently merges duplicates in **newline-delimited JSON** files, following smart rules, and outputs a clean, deduplicated contact list.

> 📌 Built with Python 3.12 — zero external dependencies.  
> ✅ Optimized for O(n log n) performance.  
> 🚀 Perfect for backend devs, data teams, and CRM clean-up ops.

---

## 🛠️ Features

- ✅ Detects duplicates by **email (case-insensitive)** OR by `(first_name, last_name, company_id)`
- ✅ Keeps:
  - The **earliest `created_at`**
  - **Longest `title`**
  - **First available phone**
  - The **ID of the earliest record**
- ✅ Command-line friendly
- ✅ Unit tested using `unittest`

---

## 🗂️ File Structure

merge_contacts_project/
│
├── contacts.jsonl # Sample input (manually created)
├── merge_contacts.py # CLI tool — run this
├── test_merge_contacts.py # Unit tests for merging logic
├── cleaned.jsonl # Output file (generated)
└── README.md # This file



---

## ▶️ How to Run

### 🟦 If using **PowerShell** (Windows):

```powershell
Get-Content contacts.jsonl | python merge_contacts.py > cleaned.jsonl
Get-Content cleaned.jsonl
🟨 If using Git Bash / Unix shell:
python merge_contacts.py < contacts.jsonl > cleaned.jsonl
cat cleaned.jsonl


✅ Unit Tests
To verify all merging logic:
python -m unittest test_merge_contacts.py
🧪 Sample Input (contacts.jsonl)

{"id":1,"first_name":"Ada","last_name":"Lovelace","email":"ada@acme.io","company_id":5,"phone":"+1 555-1","title":"CTO","created_at":"2025-05-01"}
{"id":2,"first_name":"Ada","last_name":"Lovelace","email":"Ada@acme.io","company_id":5,"phone":null,"title":"Chief Tech Officer","created_at":"2025-05-03"}
{"id":3,"first_name":"Alan","last_name":"Turing","email":"alan@acme.io","company_id":5,"phone":"+1 555-2","title":"Engineer","created_at":"2025-05-02"}

🧼 Sample Output (cleaned.jsonl)

{"id":1,"first_name":"Ada","last_name":"Lovelace","email":"ada@acme.io","company_id":5,"phone":"+1 555-1","title":"Chief Tech Officer","created_at":"2025-05-01"}
{"id":3,"first_name":"Alan","last_name":"Turing","email":"alan@acme.io","company_id":5,"phone":"+1 555-2","title":"Engineer","created_at":"2025-05-02"}

✨ Author
👨‍💻 Built by Ghady Matta
📬 Contact: ghady5255@gmail.com

💡 License
MIT — use it, extend it, build better CRMs.



---

Let me know if you want:
- A cover image or GitHub badge setup
- To turn this into a pip-installable CLI tool
- To generate synthetic contact data with Faker

You're all set to push this to GitHub! 🧠🔥








