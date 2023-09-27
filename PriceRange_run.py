import wx
import wx.grid
import pandas as pd

class PriceRange(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Airbnb Data Software", pos=wx.DefaultPosition,
                          size=wx.Size(874, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer13 = wx.FlexGridSizer(1, 5, 0, 0)
        fgSizer13.SetFlexibleDirection(wx.BOTH)
        fgSizer13.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Minimum Price", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        fgSizer13.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Maximum Price", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        fgSizer13.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer13.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(self.m_panel2, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.SetBackgroundColour(wx.Colour(255, 255, 174))

        fgSizer13.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(fgSizer13)
        self.m_panel2.Layout()
        fgSizer13.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer14 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(100, 3)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 100)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        fgSizer14.Add(self.m_grid2, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer14, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.OnSearch)



    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnSearch(self, event):
        try:
            # get min/max price
            min_price = float(self.m_textCtrl2.GetValue())
            max_price = float(self.m_textCtrl3.GetValue())

            if not min_price or not max_price:
                wx.LogError("Please Enter both Minimum and Maximum prices")
                return


            df = pd.read_csv("listings_dec18.csv", usecols=['id', 'name', 'price'])
            df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

            filtered_df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

            # Display the filtered data
            self.m_grid2.ClearGrid()
            self.m_grid2.DeleteCols(0, self.m_grid2.GetNumberCols())
            self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())

            self.m_grid2.AppendCols(len(filtered_df.columns))
            self.m_grid2.SetColLabelValue(0, 'id')
            self.m_grid2.SetColLabelValue(1, 'name')
            self.m_grid2.SetColLabelValue(2, 'price')

         # Append rows with data
            for row, (_, data) in enumerate(filtered_df.iterrows()):
                self.m_grid2.AppendRows(1)
                for col, value in enumerate(data):
                    self.m_grid2.SetCellValue(row, col, str(value))


        except ValueError:
            wx.LogError(f"Please Enter both Minimum and Maximum prices")




if __name__ == "__main__":
    app = wx.App(False)
    frame = PriceRange(None)
    frame.Show(True)
    app.MainLoop()


