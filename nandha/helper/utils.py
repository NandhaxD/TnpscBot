import re
import io
import uuid



def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    text = "%.2f %s" % (size, units[i])
    return text.upper()


def get_as_document(text_string: str, ext: str = "txt"):
    filename = f"{uuid.uuid4()}.{ext}"
    file = io.BytesIO(str.encode(text_string))
    file.name = filename
    return file


def fixed_file_name(
        name:str,
        file_type:str,
        file_size:str
    ):
    name = re.sub(r"_|\.|<|>|@|#|\(|\)|[|]", " ", name)
    return f"[📁 {file_size}] {file_type} {name}"	
