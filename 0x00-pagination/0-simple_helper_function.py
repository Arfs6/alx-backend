#!/usr/bin/env python3
"""Helper function for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the slice index for the page."""
    return (page - 1) * page_size, page * page_size
