


import aiohttp


async def paste(text: str, ext:str = 'txt'):
    # Update your paste service 

    url = 'https://spaceb.in/api/'
    data = {
        'content': text,
        'extension': ext,
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as result:
                results: dict = await result.json()
    except Exception as e:
        results: dict = {}

    pasted_id = results.get('payload', {}).get('id', None)
    
    if not pasted_id:
        url = None
    else:
        url = f"https://spaceb.in/{pasted_id}"
        
    return url