import wx
import wx.grid
import pandas as pd


class Suburb ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Airbnb Data Software", pos = wx.DefaultPosition, size = wx.Size( 874,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        fgSizer1 = wx.FlexGridSizer( 1, 7, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
        fgSizer1.Add( self.m_comboBox1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Check-In Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        m_comboBox2Choices = []
        self.m_comboBox2 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
        fgSizer1.Add( self.m_comboBox2, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Check-Out Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        m_comboBox3Choices = []
        self.m_comboBox3 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
        fgSizer1.Add( self.m_comboBox3, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button6.SetBackgroundColour( wx.Colour( 255, 255, 174 ) )

        fgSizer1.Add( self.m_button6, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( fgSizer1 )
        self.m_panel2.Layout()
        fgSizer1.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid2.CreateGrid( 5, 4 )
        self.m_grid2.EnableEditing( True )
        self.m_grid2.EnableGridLines( True )
        self.m_grid2.EnableDragGridSize( False )
        self.m_grid2.SetMargins( 0, 0 )

        # Columns
        self.m_grid2.EnableDragColMove( False )
        self.m_grid2.EnableDragColSize( True )
        self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid2.EnableDragRowSize( True )
        self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        fgSizer2.Add( self.m_grid2, 0, wx.ALL, 5 )


        bSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button6.Bind( wx.EVT_BUTTON, self.OnSearch )

        # suburb
        self.m_comboBox1.Clear()
        df_listings = pd.read_csv("listings_dec18.csv", usecols=['neighbourhood'])
        unique_suburbs = df_listings['neighbourhood'].unique()
        self.m_comboBox1.AppendItems([str(suburb) for suburb in unique_suburbs])

        # date
        self.m_comboBox2.Clear()
        self.m_comboBox3.Clear()
        df_calendar = pd.read_csv("calendar_dec18.csv")
        df_calendar['date'] = pd.to_datetime(df_calendar['date'])
        unique_dates = df_calendar['date'].dt.strftime('%Y-%m-%d').unique()
        self.m_comboBox2.AppendItems([str(date) for date in unique_dates])
        self.m_comboBox3.AppendItems([str(date) for date in unique_dates])

        # column names
        self.m_grid2.SetColLabelValue(0, 'ID')
        self.m_grid2.SetColLabelValue(1, 'Name')
        self.m_grid2.SetColLabelValue(2, 'Description')
        self.m_grid2.SetColLabelValue(3, 'Suburb')

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnSearch(self, event):
        select_suburb = self.m_comboBox1.GetValue()
        checkin_date = self.m_comboBox2.GetValue()
        checkout_date = self.m_comboBox3.GetValue()

        # convert datetime
        checkin_date = pd.Timestamp(checkin_date)
        checkout_date = pd.Timestamp(checkout_date)

        # Read the data
        df_calendar = pd.read_csv("calendar_dec18.csv")
        df_listings = pd.read_csv("listings_dec18.csv",
                                  usecols=['id', 'name', 'description', 'neighbourhood'])
        df_calendar['date'] = pd.to_datetime(df_calendar['date'])

        # filter data
        df_calendar_filtered = df_calendar[
            (df_calendar['date'] >= checkin_date) & (df_calendar['date'] <= checkout_date)]
        df_listings_filtered = df_listings[df_listings['neighbourhood'] == select_suburb]

        # Display the filtered data
        self.m_grid2.ClearGrid()
        self.m_grid2.DeleteCols(0, self.m_grid2.GetNumberCols())
        self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())

        self.m_grid2.AppendCols(len(df_listings_filtered.columns))
        self.m_grid2.SetColLabelValue(0, 'ID')
        self.m_grid2.SetColLabelValue(1, 'Name')
        self.m_grid2.SetColLabelValue(2, 'Description')
        self.m_grid2.SetColLabelValue(3, 'Suburb')

        for row, (_, data) in enumerate(df_listings_filtered.iterrows()):
            self.m_grid2.AppendRows(1)
            for col, value in enumerate(data):
                self.m_grid2.SetCellValue(row, col, str(value))


if __name__ == "__main__":
    app = wx.App(False)
    frame = Suburb(None)
    frame.Show(True)
    app.MainLoop()
