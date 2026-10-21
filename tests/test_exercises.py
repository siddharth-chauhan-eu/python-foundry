"""Tests for exercises that expose reusable functions."""

from __future__ import annotations

from helpers import load_module

duplicates = load_module(
    "duplicate_check", "01-python-fundamentals/exercises/10_duplicate_check.py"
)


def test_has_duplicates_detects_repeated_items():
    assert duplicates.has_duplicates([1, 2, 2, 3]) is True


def test_has_duplicates_accepts_unique_items():
    assert duplicates.has_duplicates([1, 2, 3]) is False
    assert duplicates.has_duplicates([]) is False
