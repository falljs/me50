import re
import logging
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

logger = logging.getLogger(__name__)

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    
    content_file = ContentFile(content.encode('utf-8'))  # Ensure content is encoded in UTF-8
    default_storage.save(filename, content_file)


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None or an error message.
    """
    try:
        with default_storage.open(f"entries/{title}.md") as f:
            return f.read().decode("utf-8")  # Ensure decoding with UTF-8
    except FileNotFoundError:
        return None
    except UnicodeDecodeError:
        return "Error: Unable to decode the file. Please check the file encoding."




