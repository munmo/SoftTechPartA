# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class PriceRange
###########################################################################

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
        self.m_grid2.CreateGrid(5, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

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
        event.Skip()
