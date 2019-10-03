def test_input_text(expected_result: int, actual_result: int):
    """
    Sample Input:
    8 11

    Sample Output:
    expected 8, got 11
    """
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


def test_substring(full_string: str, substring: str):
    """
    Sample Input:
    fulltext some_value

    Sample Output:
    expected 'some_value' to be substring of 'fulltext'
    """
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


if __name__ == '__main__':
    # test_input_text(8, 11)
    test_substring('My Name is Julia', '1Name')

