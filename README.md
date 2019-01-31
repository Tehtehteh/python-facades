# Laravel-like facades in python!
```python
from cache import Cache
Cache.get('key')
```
Results in resolving actual instance of `cache`
facading service from registered services in application.
