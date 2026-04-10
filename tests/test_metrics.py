import pytest
from app.services.metrics import calculate_gc, compute_length_stats, quality_score


def test_gc_half():
    assert calculate_gc("AGCT") == 50.0


def test_gc_all():
    assert calculate_gc("GGCC") == 100.0


def test_gc_none():
    assert calculate_gc("ATAT") == 0.0


def test_gc_n():
    assert calculate_gc("AGCTN") == 40.0


def test_length_stats():
    lengths = [100, 150, 200, 250, 300]
    stats = compute_length_stats(lengths)
    assert stats["min"] == 100
    assert stats["max"] == 300
    assert stats["mean"] == 200.0
    assert stats["median"] == 200.0


class MockRecord:
    def __init__(self, qualities):
        self.letter_annotation = {"phred_quality": qualities}


def test_quality_score():
    records = [
        MockRecord([30, 30, 30]),
        MockRecord([20, 20, 20]),
        MockRecord([10, 10, 10]),
        MockRecord([])
    ]
    result = quality_score(records, threshold=25)
    assert result["mean_quality_per_read"] == [30.0, 20.0, 10.0, 0.0]
    assert result["low_quality_per_count"] == 2
    assert result["quality_threshold"] == 25