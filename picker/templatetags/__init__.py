
__all__ = ['VERSION']


try:
    import pkg_resources
    VERSION = pkg_resources.get_distribution('django-picker').version
except Exception:
    VERSION = 'unknown'
