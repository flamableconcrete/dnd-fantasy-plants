from generate_gmbinder import get_die_entries


def test_die_entries():
    assert get_die_entries(6, 6) == [1, 2, 3, 4, 5, 6]
    assert get_die_entries(4, 3) == ['1-2', 3, 4]
