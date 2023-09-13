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

        self.m_button7 = wx.Button(self.m_panel2, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.SetBackgroundColour(wx.Colour(255, 255, 174))
        gSizer3.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(gSizer3)
        self.m_panel2.Layout()
        gSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

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

        # Convert to datetime type
        checkin_date = pd.Timestamp(checkin_date)
        checkout_date = pd.Timestamp(checkout_date)

        # Read the data
        df_calendar = pd.read_csv("calendar_dec18.csv")
        df_calendar['date'] = pd.to_datetime(df_calendar['date'])
        df_calendar['price'] = df_calendar['price'].replace('[\$,]', '', regex=True).astype(float)

        # Filter the DataFrame based on the selected date range
        df_filtered = df_calendar[(df_calendar['date'] >= checkin_date) & (df_calendar['date'] <= checkout_date)]

        if df_filtered.empty:
            wx.MessageBox("No data available for the selected date range.", "Info", wx.OK | wx.ICON_INFORMATION)
            return

        # Further filter to only include prices up to $1000
        df_filtered = df_filtered[df_filtered['price'] <= 1000]

        if df_filtered.empty:
            wx.MessageBox("No data available for the selected date range under $1000.", "Info",
                          wx.OK | wx.ICON_INFORMATION)
            return

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.hist(df_filtered['price'], bins=range(0, 1001, 100), color='pink', edgecolor='black')
        plt.title(
            f"Airbnb Sydney Price Distribution: {checkin_date.strftime('%Y-%m-%d')} to {checkout_date.strftime('%Y-%m-%d')}")
        plt.xlabel("Price")
        plt.xticks([x for x in range(0, 1001, 100)], [f"${x}" for x in range(0, 1001, 100)])  # Add $ to x-axis labels
        plt.ylabel("Number of properties")
        plt.grid(True)
        plt.ticklabel_format(style='plain', axis='y', useOffset=False)  # Disable scientific notation for y-axis
        plt.show()


# Run the program
app = wx.App(False)
frame = Price(None)
frame.Show(True)
app.MainLoop()
