from src import bursts


def test_detect_bursts_splits_on_gap():
    events = [0.0, 1.0, 10.0, 10.5]
    assert bursts.detect_bursts(events, min_gap=5.0) == [0, 2]
