import os.path
import pandas as pd
import wx
import pytest
from unittest import mock
import matplotlib.pyplot as plt
from PriceDistribution_Run import Price

calendar_csv_file = "calendar_dec18.csv"

def test_calendar_csv():
    # Check if the file exists.
    assert os.path.exists(calendar_csv_file), f"CSV file '{calendar_csv_file}' not found."

    # Read the unique dates from the CSV file
    df_calendar = pd.read_csv(calendar_csv_file)
    unique_dates = df_calendar['date'].unique().tolist()
    unique_dates.sort()

    # Initialize the application and frame.
    app = wx.App(False)
    frame = Price(None)

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
def price_frame(wx_app):
    return Price(None)

# Test if check-in date and check-out date are both selected
@mock.patch.object(plt, 'show')
def test_dates_provided(mocked_show, price_frame):
    # Mocking the scenario where both "Check-in Date" and "Check-out Date" are selected
    price_frame.m_comboBox2.SetValue('2019-01-01')  # A value for Check-in Date
    price_frame.m_comboBox3.SetValue('2019-02-02')  # A value for Check-out Date

    try:
        price_frame.OnPlot(None)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")


# Mock both plt.title and plt.show to capture its arguments and prevent the actual plot rendering respectively
@mock.patch.object(plt, 'show')
@mock.patch.object(plt, 'title')
def test_plot_title_correctness(mocked_title, mocked_show, price_frame):
    checkin_date = '2019-01-01'
    checkout_date = '2019-02-02'

    # Set the check-in and check-out dates
    price_frame.m_comboBox2.SetValue(checkin_date)
    price_frame.m_comboBox3.SetValue(checkout_date)

    # Call the plotting function
    price_frame.OnPlot(None)

    # Verify that plt.title() was called with the correct argument
    expected_title = f"Airbnb Sydney Price Distribution: {checkin_date} to {checkout_date}"
    mocked_title.assert_called_with(expected_title)
