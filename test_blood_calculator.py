import pytest

@pytest.mark.parametrize("input, expected",
                         [(85, "normal"),
                          (50, "borderline low"),
                          (35, "low")])
def test_check_HDL(input, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input)

#%% Notes
# Although you could move the "from blood_calculator import check_HDL" outside of all
#   3 functions, we prefer to keep it inside and avoid any potential downstream errors
# Combining all the different testing conditions into one test function is typically ont considered
#   best practice since it doesn't provide detail regarding which test case failed