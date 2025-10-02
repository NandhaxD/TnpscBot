

from nandha import database
from pymongo import ASCENDING

import re

db = database['files']

async def add_file(
    file_unique_id: str,
    file_id: str,
    file_name: str,
    category: str,
    file_type: str
):
    file = {
        "file_unique_id": file_unique_id,
        "file_id": file_id,
        "file_name": file_name,
        "category": category,
        "file_type": file_type
    }
    ok = await db.insert_one(file)
    return ok.inserted_id is not None



async def get_files_by_name(
    search_query: str,
    category: str = None,
    limit: int = 50
) -> list[dict]:
    """
    Fast regex-based search for files by name.
    """
    words = [
        re.escape(word) for word in search_query.lower().split()
    ]
    pattern = '.*'.join(words)
    query = {
        'file_name': {'$regex': pattern, '$options': 'i'}
    }

    if category:
        query.update(
        {'category': category}
    )
    projection = {
        'file_id': 1,
        'file_unique_id': 1,
        'category': 1,
        'file_type': 1,
        'file_name': 1,
        '_id': 0
    }
    files = await db.files.find(query, projection).sort('_id', 1).limit(limit).to_list(length=None)
    return files if files else []

async def get_file_by_file_unique_id(file_unique_id: str):
    return await db.find_one(
        {"file_unique_id": file_unique_id}
    )

async def remove_file_by_file_unique_id(file_unique_id: str):
    result = await db.delete_one({"file_unique_id": file_unique_id})
    return result.deleted_count > 0

async def update_file_by_file_unique_id(
    file_unique_id: str,
    update_data: dict
):
    result = await db.update_one(
        {"file_unique_id": file_unique_id},
        {"$set": update_data}
    )
    return result.modified_count > 0

