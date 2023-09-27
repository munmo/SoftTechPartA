import sys
import pytest
import wx
import pandas as pd
from PriceRange_run import PriceRange

@pytest.fixture
def price_range_cases():
    app = wx.App(False)
    frame = PriceRange(None)
    yield frame
    frame.Destroy()
    app.ExitMainLoop()

# test minimum price and maximum price to see if the grid contains specific data
@pytest.mark.parametrize("min_price, max_price", [(50,100), (150, 300), (100, 800)])
def test_min_max_prices(price_range_cases, min_price, max_price):
    price_range_cases.m_textCtrl2.SetValue(str(min_price))
    price_range_cases.m_textCtrl3.SetValue(str(max_price))

    event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, price_range_cases.m_button6.GetId())
    price_range_cases.m_button6.Command(event)

    grid = []
    for row in range(price_range_cases.m_grid2.GetNumberRows()):
        row_data = []
        for col in range(price_range_cases.m_grid2.GetNumberCols()):
            cell_value = price_range_cases.m_grid2.GetCellValue(row,col)
            try:
                cell_value_float = float(cell_value)
                row_data.append(cell_value_float)
            except ValueError:
                row_data.append(None)
            grid.append(row_data)

    for row_data in grid:
        if row_data:
            price = row_data[2]
            assert min_price <= price <= max_price

# Test if the result grid refreshes correctly after data is re-loaded
@pytest.mark.parametrize("min_price, max_price", [(50, 400), (100, 400)])
def test_grid_refresh(price_range_cases, min_price, max_price):
    price_range_cases.m_textCtrl2.SetValue(str(min_price))
    price_range_cases.m_textCtrl3.SetValue(str(max_price))

    event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, price_range_cases.m_button6.GetId())
    price_range_cases.m_button6.Command(event)

    assert price_range_cases.m_grid2.GetNumberRows() > 0
    price_range_cases.m_grid2.ClearGrid()
    wx.CallLater(100, check_grid_empty, price_range_cases.m_grid2)
def check_grid_empty(grid):
    assert grid.GetNumberRows() == 0

# Test filtered data
@pytest.mark.parametrize("min_price, max_price", [(100,300), (500, 800), (250, 750)])
def test_filtered_data(price_range_cases, min_price, max_price):
    min_price_input = price_range_cases.m_textCtrl2
    max_price_input = price_range_cases.m_textCtrl3

    min_price_input.SetValue(str(min_price))
    max_price_input.SetValue(str(max_price))

    event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, price_range_cases.m_button6.GetId())
    price_range_cases.m_button6.Command(event)

    grid = price_range_cases.m_grid2
    num_rows = grid.GetNumberRows()
    num_cols = grid.GetNumberCols()

    # check the data in the grid after filtering
    df = pd.read_csv("listings_dec18.csv", usecols= ["id", "name", "price"])
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    for row in range(num_rows):
        price_in_grid = float(grid.GetCellValue(row, 2)) # price column is third one
        assert min_price <= price_in_grid <= max_price

















