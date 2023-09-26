import os.path
import pandas as pd
import wx
import pytest
from Suburb_run import Suburb

# test calendar csv file exists
calandar_csv_file = "calendar_dec18.csv"
def test_calendar_csv():
    assert os.path.exists(calandar_csv_file), f"CSV file '{calandar_csv_file}' not found."
    app = wx.App(False)
    frame = Suburb(None)

    assert len(frame.m_comboBox2.GetItems()) > 0
    assert len(frame.m_comboBox3.GetItems()) > 0

# test different check-in & check-out dates when suburb is specified ("Pyrmont"), and search then check if the grid contains the specific data.
@pytest.fixture()
def suburb_cases():
    app = wx.App(False)
    frame = Suburb(None)
    yield frame
    frame.Destroy()
    app.MainLoop()

# Test different check-in & check-out dates when suburb is specified, and search then check if the grid contains the specific data.
@pytest.mark.parametrize("checkin_date, checkout_date", [("2019-08-01", "2019-08-05"), ("2019-07-26", "2019-07-30")])
def test_data_exits(suburb_cases, checkin_date, checkout_date):
    # set suburb as "Pyrmont"
    suburb_cases.m_comboBox1.SetValue("Pyrmont")
    suburb_cases.m_comboBox2.SetValue(checkin_date)
    suburb_cases.m_comboBox3.SetValue(checkout_date)
    suburb_cases.OnSearch(None)
    num_rows = suburb_cases.m_grid2.GetNumberRows()
    assert num_rows > 0

# Test suburb input(if no input is suburb, get "Missing Suburb" message
@pytest.mark.parametrize("suburb_input, checkin_date, checkout_date, expected_message",
                         [("Avalon", "2019-07-15", "2019-07-20", ""),
                          ("", "2019-08-01", "2019-08-05", "Missing Suburb")])
def test_suburb_input(suburb_cases, suburb_input, checkin_date, checkout_date, expected_message):
    suburb_cases.m_comboBox1.SetValue(suburb_input)
    suburb_cases.m_comboBox2.SetValue(checkin_date)
    suburb_cases.m_comboBox3.SetValue(checkout_date)
    suburb_cases.OnSearch(None)

    status_message = suburb_cases.GetStatusMessage()
    if status_message is not None:
        status_message = status_message.strip()

    expected_message = expected_message.strip() if expected_message else None

    assert status_message == expected_message

# Test if the listing csv file exists
def test_listings_csv_exits(suburb_cases):
    csv_path = "listings_dec18.csv"
    assert os.path.exists(csv_path), f"The LISTING CSV file '{csv_path}' does not exist."
    suburb_cases.m_comboBox1.Clear()
    df_listings = pd.read_csv(csv_path, usecols=['neighbourhood'])
    unique_suburbs = df_listings['neighbourhood'].unique()
    suburb_cases.m_comboBox1.AppendItems([str(suburb) for suburb in unique_suburbs])
    assert suburb_cases.m_comboBox1.GetCount() > 0, "Failed to load suburb from listing csv file"

# Test with different combinations of suburb and date range to verify that the grid displays the specific data.
@pytest.mark.parametrize("suburb_input, checkin_date, checkout_date, expected_message",
                         [("Bondi Beach", "2019-07-01", "2019-07-10", ""),
                          ("", "2019-08-01", "2019-08-05","Missing Suburb"),
                          ("North Bondi", "2019-07-22", "", "Missing Dates")])
def test_combined_data(suburb_cases, suburb_input, checkin_date, checkout_date, expected_message):
    suburb_cases.m_comboBox1.SetValue(suburb_input)
    suburb_cases.m_comboBox2.SetValue(checkin_date)
    suburb_cases.m_comboBox3.SetValue(checkout_date)
    suburb_cases.OnSearch(None)

    status_message = suburb_cases.GetStatusMessage()
    if status_message is not None:
        status_message = status_message.strip()

    assert status_message == expected_message
    if not expected_message:
        assert suburb_cases.m_grid2.GetNumberRows() > 0
        assert suburb_cases.m_grid2.GetNumberCols() == 4






