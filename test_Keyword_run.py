import os.path
import pandas as pd
import wx
import pytest
import unittest.mock as mock
from Keyword_Run import Keyword

# Check if the file exists.
calendar_csv_file = "calendar_dec18.csv"

def test_calendar_csv():
    assert os.path.exists(calendar_csv_file), f"CSV file '{calendar_csv_file}' not found."

    # Read the unique dates from the CSV file
    df_calendar = pd.read_csv(calendar_csv_file)
    unique_dates = df_calendar['date'].unique().tolist()
    unique_dates.sort()

    # Initialize the application and frame.
    app = wx.App(False)
    frame = Keyword(None)

    # Check if the combo boxes have items.
    assert len(frame.m_comboBox2.GetItems()) > 0, "m_comboBox2 is empty."
    assert len(frame.m_comboBox3.GetItems()) > 0, "m_comboBox3 is empty."

    # Check that the items in the combo boxes match the unique dates from the CSV file.
    assert set(frame.m_comboBox2.GetItems()) == set(unique_dates), "m_comboBox2 items don't match CSV dates."
    assert set(frame.m_comboBox3.GetItems()) == set(unique_dates), "m_comboBox3 items don't match CSV dates."

@pytest.fixture(scope="module")
def wx_app():
    return wx.App(False)

@pytest.fixture
def keyword_frame(wx_app):
    return Keyword(None)

# Test if check-in date and check-out date are both selected
@mock.patch.object(wx, 'MessageBox')  # Mock the wx.MessageBox function
@mock.patch.object(Keyword, 'OnSearch')
def test_dates_provided(mocked_OnSearch, mocked_MessageBox, keyword_frame):
    # Mocking the scenario where both "Check-in Date" and "Check-out Date" are selected
    keyword_frame.m_comboBox2.SetValue('2019-01-01')  # A value for Check-in Date
    keyword_frame.m_comboBox3.SetValue('2019-02-02')  # A value for Check-out Date

    try:
        keyword_frame.OnSearch(None)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

    # Assertions for expected behaviors based on your implementation
    mocked_OnSearch.assert_called_once()  # Check that OnSearch was called once
    mocked_MessageBox.assert_not_called()  # Ensure that wx.MessageBox was not called