## Asynchronous and synchronous Oxford dictionary scrapper.
### Asynchronous
```python
import asyncio
from oxfordscrapper import Async

loop = asyncio.get_event_loop()

loop.run_until_complete(Async.define('Word'))
```
### Synchronous
```python
from oxfordscrapper import define

define('Word')
```
**Check `how_to.py` for more information about how to use it.**
### Error handling
**`urbanscrapper.NotFound`**: raised when no definition is found.

**`ValueError`**: raised when user tries to search more than one word.

### Return value
It returns dictionary object. Check and run **`how_to.py`** for more info.
