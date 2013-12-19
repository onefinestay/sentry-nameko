try:
    VERSION = __import__('pkg_resources') \
        .get_distribution(__name__).version
except Exception:
    VERSION = 'unknown'

from interface import CallIdStack
