"""CLIP-EBC: Crowd counting with CLIP."""

__version__ = "0.1.0"

from .custom.clip_ebc import ClipEBC
from .models import get_model
from .utils import *

__all__ = ["ClipEBC", "get_model"]