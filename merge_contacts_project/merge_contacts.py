import sys
import json
from datetime import datetime

def normalize_email(email):
    return email.lower() if email else None

def get_keys(contact):
    # Return two keys for duplicate detection
    email_key = normalize_email(contact.get("email"))
    name_key = (contact.get("first_name"), contact.get("last_name"), contact.get("company_id"))
    return email_key, name_key

def merge_records(a, b):
    # Determine which contact has the earlier created_at
    created_a = datetime.fromisoformat(a["created_at"])
    created_b = datetime.fromisoformat(b["created_at"])
    if created_a <= created_b:
        primary, secondary = a, b
    else:
        primary, secondary = b, a

    return {
        "id": primary["id"],
        "first_name": primary["first_name"],
        "last_name": primary["last_name"],
        "email": normalize_email(primary["email"]),
        "company_id": primary["company_id"],
        "phone": primary.get("phone") or secondary.get("phone"),
        "title": max(primary.get("title", ""), secondary.get("title", ""), key=len),
        "created_at": primary["created_at"]
    }

def merge_contacts(contacts):
    by_email = {}
    by_name = {}

    for contact in contacts:
        email_key, name_key = get_keys(contact)
        if email_key and email_key in by_email:
            merged = merge_records(by_email[email_key], contact)
            by_email[email_key] = merged
            by_name[(merged["first_name"], merged["last_name"], merged["company_id"])] = merged
        elif name_key in by_name:
            merged = merge_records(by_name[name_key], contact)
            by_name[name_key] = merged
            if email_key:
                by_email[email_key] = merged
        else:
            if email_key:
                by_email[email_key] = contact
            by_name[name_key] = contact

    # Deduplicate final results by ID
    seen_ids = set()
    result = []
    for record in list(by_email.values()) + list(by_name.values()):
        if record["id"] not in seen_ids:
            seen_ids.add(record["id"])
            result.append(record)

    return result

if __name__ == "__main__":
    contacts = [json.loads(line) for line in sys.stdin if line.strip()]
    merged = merge_contacts(contacts)
    for contact in merged:
        print(json.dumps(contact))
