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
**Check [`how_to.py`](https://github.com/m-y-x-i/oxford-scrapper/blob/main/how_to.py) for more information about how to use it.**
### Error handling
[**`urbanscrapper.NotFound`**](https://github.com/m-y-x-i/oxford-scrapper/blob/45562e9cc3a92695a08eadb0d0752db9713c55b3/oxfordscrapper.py#L8-L9): raised when no definition is found.

[**`ValueError`**](https://docs.python.org/3/library/exceptions.html#ValueError): raised when user tries to search more than one word.

### Return value
It returns dictionary object. Check and run [**`how_to.py`**](https://github.com/m-y-x-i/oxford-scrapper/blob/main/how_to.py#L23-L26) for more info.
