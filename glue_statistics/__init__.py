import os

from . import tools

def setup():
    from .glue_statistics import StatsDataViewer
    from glue.config import qt_client
    qt_client.add(StatsDataViewer)
