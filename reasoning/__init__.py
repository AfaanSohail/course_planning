"""Member 1: evidence-preserving multi-hop course planning."""
from .engine import Reasoner
from .kg import KG
from functools import lru_cache


@lru_cache(maxsize=1)
def _default_reasoner():
    return Reasoner(KG())


def reason(template, **kwargs):
    """Convenient agreed interface; use Reasoner(KG(path)) for another snapshot."""
    return _default_reasoner().reason(template, **kwargs)


__all__ = ["KG", "Reasoner", "reason"]
