
from hypothesis import given, example, strategies as st

from processor import parse_int_list, calculate_average, validate_age


# Test 1: Fuzz testing for parse_int_list()
@given(st.text())
@example("")
@example("1,,3")
@example("one,two")
@example(None)
def test_parse_int_list(value):
    result = parse_int_list(value)

    assert isinstance(result, list)
    assert all(type(item) is int for item in result)


# Test 2: Fuzz testing for calculate_average()
@given(st.lists(st.integers(min_value=-100, max_value=100)))
def test_calculate_average(numbers):
    result = calculate_average(numbers)

    if numbers:
        assert result == sum(numbers) / len(numbers)
    else:
        assert result == 0.0


# Test 3: Fuzz testing for validate_age()
@given(st.one_of(
    st.integers(),
    st.text(),
    st.booleans(),
    st.none()
))
def test_validate_age(age):
    result = validate_age(age)

    expected = (
        type(age) is int and 0 <= age <= 120
    )

    assert result == expected
