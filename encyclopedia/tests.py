from django.test import TestCase

from encyclopedia.util import save_entry, get_entry

# Save a new entry
title = "TestPage"
content = "# Header\nThis is some test content."
save_entry(title, content)

# Retrieve the entry
retrieved_content = get_entry(title)
print("Retrieved content:")
print(retrieved_content)

