"""
Timetagger - Tag your time, get the insight.
"""

__version__ = "21.1.1"

version_info = tuple(map(int, __version__.split(".")))


from . import server  # noqa
