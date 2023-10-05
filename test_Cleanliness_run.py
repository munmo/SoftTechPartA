import os.path
import wx
import pytest
from Cleanliness_Run import Cleanliness

# Check if the file exists.
reviews_csv_file = "reviews_dec18.csv"


def test_reviews_csv_exists():
    assert os.path.exists(reviews_csv_file), f"CSV file '{reviews_csv_file}' not found."

def test_csv_file_extension_valid():
    # Check if the file extension is valid
    _, file_extension = os.path.splitext(reviews_csv_file)
    assert len(file_extension) in (3, 4) and file_extension[1:].isalpha(), f"Invalid file extension: '{file_extension}'"

def test_csv_file_name_startswith_alphabetical():
    file_name = os.path.basename(reviews_csv_file)
    assert file_name[0].isalpha(), f"CSV file name '{file_name}' does not start with an alphabetical character."

@pytest.fixture(scope="module")
def wx_app():
    return wx.App(False)

@pytest.fixture
def cleanliness_frame(wx_app):
    return Cleanliness(None)

def test_cleanliness_selection(cleanliness_frame):
    # Simulate selecting a cleanliness keyword from the list
    keyword_to_select = "Tidy"
    cleanliness_frame.m_comboBox1.SetValue(keyword_to_select)

    # Check if the selected keyword matches the expected selection
    selected_keyword = cleanliness_frame.m_comboBox1.GetValue()
    assert selected_keyword == keyword_to_select, f"Expected '{keyword_to_select}' but got '{selected_keyword}'"

    try:
        cleanliness_frame.OnSearch(None)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")


def test_cleanliness_selection_no_keyword(cleanliness_frame):
    # Do not select any cleanliness keyword from the list

    # Check if the selected keyword is empty
    selected_keyword = cleanliness_frame.m_comboBox1.GetValue()
    assert selected_keyword == "", "Expected an empty keyword selection."

    try:
        cleanliness_frame.OnSearch(None)
        assert True

    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

def test_cleanliness_keyword_filtering(cleanliness_frame):
    # Simulate selecting a cleanliness keyword from the list
    keyword_to_select = "Tidy"
    cleanliness_frame.m_comboBox1.SetValue(keyword_to_select)

    try:
        cleanliness_frame.OnSearch(None)

        # Check if the grid contains only rows with the selected cleanliness keyword in the "Comments" column
        for row in range(cleanliness_frame.m_grid2.GetNumberRows()):
            comment = cleanliness_frame.m_grid2.GetCellValue(row, 1)  # Get the "Comments" column value
            assert keyword_to_select.lower() in comment.lower(), f"Keyword '{keyword_to_select}' not found in comment: '{comment}'"

    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")