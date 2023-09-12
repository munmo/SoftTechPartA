import wx
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt

class Price(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Airbnb Data Software",
                          pos=wx.DefaultPosition, size=wx.Size(874, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer3 = wx.GridSizer(1, 5, 0, 0)

        # Read the unique dates from the CSV file
        df_calendar = pd.read_csv("calendar_18.csv")
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

        self.m_button7 = wx.Button(self.m_panel2, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.SetBackgroundColour(wx.Colour(255, 255, 174))
        gSizer3.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(gSizer3)
        self.m_panel2.Layout()
        gSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_grid2.CreateGrid(5, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1.Add(self.m_grid2, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button7.Bind(wx.EVT_BUTTON, self.OnPlot)

    def __del__(self):
        pass

    def OnPlot(self, event):
        checkin_date = self.m_comboBox2.GetValue()
        checkout_date = self.m_comboBox3.GetValue()

        if not checkin_date or not checkout_date:
            wx.MessageBox("Please select both Check-In and Check-Out dates.", "Error", wx.OK | wx.ICON_ERROR)
            return

        df_calendar = pd.read_csv("calendar_18.csv")
        df_calendar['date'] = pd.to_datetime(df_calendar['date'])
        df_calendar['price'] = df_calendar['price'].replace('[\$,]', '', regex=True).astype(float)

        mask = (df_calendar['date'] >= checkin_date) & (df_calendar['date'] <= checkout_date)
        df_filtered = df_calendar.loc[mask]

        if df_filtered.empty:
            wx.MessageBox("No data available for the selected date range.", "Info", wx.OK | wx.ICON_INFORMATION)
            return

        plt.figure(figsize=(10, 6))
        plt.hist(df_filtered['price'].dropna(), bins=30, color='blue', edgecolor='black')
        plt.title("Price Distribution")
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.show()

# Run the program
app = wx.App(False)
frame = Price(None)
frame.Show(True)
app.MainLoop()