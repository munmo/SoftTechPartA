import wx
import wx.grid
import pandas as pd


class Keyword(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Airbnb Data Software",
                          pos=wx.DefaultPosition, size=wx.Size(874, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer3 = wx.GridSizer(2, 4, 0, 0)

        # Read the unique dates from the CSV file
        df_calendar = pd.read_csv("calendar_dec18.csv")
        unique_dates = df_calendar['date'].unique().tolist()
        unique_dates.sort()

        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Check-In Date", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        gSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_comboBox2 = wx.ComboBox(self.m_panel2, wx.ID_ANY, u"Select Date", wx.DefaultPosition, wx.DefaultSize, unique_dates, 0)
        gSizer3.Add(self.m_comboBox2, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Check-Out Date", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        gSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_comboBox3 = wx.ComboBox(self.m_panel2, wx.ID_ANY, u"Select Date", wx.DefaultPosition, wx.DefaultSize, unique_dates, 0)
        gSizer3.Add(self.m_comboBox3, 0, wx.ALL, 5)

        # Add a text input field for the keyword
        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Keyword", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        gSizer3.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self.m_panel2, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button8.SetBackgroundColour(wx.Colour(255, 255, 174))

        gSizer3.Add(self.m_button8, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(gSizer3)
        self.m_panel2.Layout()
        gSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(5, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1.Add(self.m_grid2, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button8.Bind(wx.EVT_BUTTON, self.OnSearch)

    def __del__(self):
        pass

    def OnSearch(self, event):
        try:
            checkin_date = self.m_comboBox2.GetValue()
            checkout_date = self.m_comboBox3.GetValue()

            keyword = self.m_textCtrl1.GetValue()  # Get the keyword entered by the user

            if not checkin_date or not checkout_date:
                wx.MessageBox("Please select both Check-In and Check-Out dates.", "Error", wx.OK | wx.ICON_ERROR)
                return

            # Convert to datetime type
            checkin_date = pd.Timestamp(checkin_date)
            checkout_date = pd.Timestamp(checkout_date)

            # Read the data
            df_calendar = pd.read_csv("calendar_dec18.csv", engine='python')
            df_calendar['date'] = pd.to_datetime(df_calendar['date'])

            df_listings = pd.read_csv("listings_dec18.csv", low_memory=False, usecols=['id', 'name', 'description'])

            df_filtered = df_calendar[(df_calendar['date'] >= checkin_date) & (df_calendar['date'] <= checkout_date)]

            df_filtered_listings = df_listings[df_listings['description'].str.contains(keyword, case=False, na=False)]

            num_rows = (len(df_filtered_listings) - 5)
            self.m_grid2.AppendRows(num_rows)

            self.m_grid2.AppendCols(len(df_filtered_listings.columns))
            self.m_grid2.SetColLabelValue(0, 'ID')
            self.m_grid2.SetColLabelValue(1, 'Name')
            self.m_grid2.SetColLabelValue(2, 'Description')

            # Fill in the data in the grid
            for row, (_, row_data) in enumerate(df_filtered_listings.iterrows()):
                for col, value in enumerate(row_data):
                    self.m_grid2.SetCellValue(row, col, str(value))

            # Refresh the grid to display the updated data
            self.m_grid2.AutoSize()
            self.m_grid2.Refresh()

        except Exception as e:
            wx.LogError(f"Error: {e}")
            return

        if df_filtered.empty or df_filtered_listings.empty:
            wx.MessageBox(f"No data available for the selected date range with keyword '{keyword}'.", "Info", wx.OK | wx.ICON_INFORMATION)
            return

if __name__ == "__main__":
    app = wx.App(False)
    frame = Keyword(None)
    frame.Show(True)
    app.MainLoop()