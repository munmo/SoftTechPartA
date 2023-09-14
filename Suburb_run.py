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
        gSizer3 = wx.GridSizer( 1, 7, 0, 0 )

        self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        gSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
        gSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Check-In Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        gSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

        m_comboBox2Choices = []
        self.m_comboBox2 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
        gSizer3.Add( self.m_comboBox2, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Check-Out Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

        m_comboBox3Choices = []
        self.m_comboBox3 = wx.ComboBox( self.m_panel2, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
        gSizer3.Add( self.m_comboBox3, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button6.SetBackgroundColour( wx.Colour( 255, 255, 174 ) )

        gSizer3.Add( self.m_button6, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( gSizer3 )
        self.m_panel2.Layout()
        gSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid2.CreateGrid( 5, 5 )
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
        bSizer1.Add( self.m_grid2, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        def __del__( self ):
            pass
