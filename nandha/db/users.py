
from nandha import database, LOG

collection = database['users']


USER_IDS = []
BLOCKED_USERS = []

async def check_user_exists(user_id: int):
    user = await collection.find_one({'user_id': user_id})
    return True if user else False

async def add_user(obj):
    try:
        user_id = obj['id']
        filter = {'user_id': user_id}
        user_data = {
            "$set": {
                'user_id': user_id,
                'first_name': obj.get('first_name'),
                'username': obj.get('username'),
                'active': True,
            }
        }
        await collection.update_one(filter, user_data, upsert=True)
    except Exception as e:
        LOG.error(f"Error adding user: {e}")


async def get_all_blocked_users():
        users = await collection.find(
            {'blocked': True}, {'user_id': 1}).to_list(length=None)
        return [ user['user_id'] for user in users ] if users else []


async def initialize_blocked_users():
    users = await get_all_blocked_users()
    BLOCKED_USERS.extend(users)


async def get_blocked_users():
    try:
        users = await collection.find({'blocked': True}).to_list(length=None)
        return [user['user_id'] for user in users] if users else []
    except Exception as e:
        LOG.error(f"Error getting blocked users: {e}")
        return []


async def update_user_block(user_id:int, option:bool):
        user = {'user_id': user_id}
        data = {
            "$set": {
            "blocked": option
        }
    }
        file = await collection.update_one(
            user, data
    )
        return file.modified_count > 0


async def update_users_status(users_id: list, status=True):
    filter = {'user_id': {'$in': users_id}}
    update = {'$set': {'active': status}}
    result = await collection.update_many(filter, update)
    return result.modified_count > 0

async def remove_user(user_id):
    try:
        await collection.delete_one({'user_id': user_id})
    except Exception as e:
        LOG.error(f"Error removing user: {e}")

async def get_user_data(user_id):
    try:
        user = await collection.find_one({'user_id': user_id})
        if user:
            return {key: value for key, value in user.items() if not key.startswith('_')}
        else:
            return {}
    except Exception as e:
        LOG.error(f"Error getting user: {e}")
        return {}

async def get_users_by_first_name(first_name):
    try:
        users = await collection.find(
            {'first_name': {'$regex': first_name, '$options': 'i'}}
        ).to_list(None)
        return users
    except Exception as e:
        LOG.error(f'Error while searching for user_ids by first_name: {str(e)}')
        return []


async def get_users_by_username(username):
    try:
        users = await collection.find(
            {'username': {'$regex': username, '$options': 'i'}}
        ).to_list(None)
        return users
    except Exception as e:
        LOG.error(f'Error while searching for user_ids by first_name: {str(e)}')
        return []

async def get_user_id_by_username(username):
    try:
        user = await collection.find_one(
        {'username': {'$regex': username, '$options': 'i'}}
        )
        return user['user_id'] if user else None
    except Exception as e:
        LOG.error(f'Error while searching for user_id by username: {str(e)}')
        return None


async def update_users_status_to_active(users_id: list):
    filter = {'user_id': {'$in': users_id}}
    update = {'$set': {'active': True}}
    result = await collection.update_many(filter, update)
    return result.modified_count > 0

async def update_users_status_to_inactive(users_id: list):
    filter = {'user_id': {'$in': users_id}}
    update = {'$set': {'active': False}}
    result = await collection.update_many(filter, update)
    return result.modified_count > 0


async def update_user_premium(user_id: int, premium: bool):
    try:
        filter = {'user_id': user_id}
        update = {'$set': {'premium': premium}}
        result = await collection.update_one(filter, update)
        return result.modified_count > 0
    except Exception as e:
        LOG.error(f"Error updating user premium status: {e}")
        return False
    
async def get_user_premium_status(user_id: int):
    try:
        user = await collection.find_one({'user_id': user_id})
        if user:
            return user.get('premium', False)
        return False
    except Exception as e:
        LOG.error(f"Error getting user premium status: {e}")
        return False
    
        
async def is_user_premium(user_id: int):
    try:
        user = await collection.find_one({'user_id': user_id, 'premium': True})
        return True if user else False
    except Exception as e:
        LOG.error(f"Error checking if user is premium: {e}")
        return False 

async def get_all_premium_users():
    try:
        users = await collection.find({'premium': True}).to_list(length=None)
        return [user['user_id'] for user in users] if users else []
    except Exception as e:
        LOG.error(f"Error getting premium users: {e}")
        return []    


async def get_all_inactive_users():
    filter = {'active': False}
    users = await collection.find(filter).to_list(length=None)
    return [ user['user_id'] for user in users ] if users else []


async def get_all_active_users():
    filter = {'active': True}
    users = await collection.find(filter).to_list(length=None)
    return [ user['user_id'] for user in users ] if users else []

async def count_users() -> int:
    count = await collection.count_documents({})
    return count           

async def get_all_users_data():
    try:
        users = await collection.find().to_list(length=None)
        return users if users else []
    except Exception as e:
        LOG.error(f"Error getting all users: {e}")
        return []

async def get_all_users():
    try:
        users = await collection.find().to_list(length=None)
        return [user['user_id'] for user in users]
    except Exception as e:
        LOG.error(f"Error getting all users: {e}")
        return []

async def initialize_db_users():
    users = await get_all_users()
    USER_IDS.extend(users)


