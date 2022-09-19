import pytest

@pytest.mark.parametrize("input, expected",
                         [(85, "normal"),
                          (50, "borderline low"),
                          (35, "low")])
def test_check_HDL(input, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input)
    assert answer == expected

@pytest.mark.parametrize("input, expected",
                         [(200, "very high"),
                          (170, "high"),
                          (150, "borderline high"),
                          (120, "normal")])
def test_check_LDL(input, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(input)
    assert answer == expected

@pytest.mark.parametrize("input, expected",
                         [(300, "high"),
                          (220, "borderline high"),
                          (190, "normal")])
def test_check_totchol(input, expected):
    from blood_calculator import check_totchol
    answer = check_totchol(input)
    assert answer == expected
