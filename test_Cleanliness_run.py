import os.path
import wx
import pytest
from Cleanliness_Run import Cleanliness

# Check if the file exists.
reviews_csv_file = "reviews_dec18.csv"

def test_reviews_csv():
    assert os.path.exists(reviews_csv_file), f"CSV file '{reviews_csv_file}' not found."

@pytest.fixture(scope="module")
def wx_app():
    return wx.App(False)

@pytest.fixture
def cleanliness_frame(wx_app):
    return Cleanliness(None)

    try:
        cleanliness_frame.OnSearch(None)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")
