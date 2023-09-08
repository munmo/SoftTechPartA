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
## Class Software
###########################################################################

class Software ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Airbnb Data Analysis Software", pos = wx.DefaultPosition, size = wx.Size( 1168,349 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 3, 10, 0, 0 )

		gSizer4.SetMinSize( wx.Size( -3,-3 ) )
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )

		m_comboBox5Choices = []
		self.m_comboBox5 = wx.ComboBox( self, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
		gSizer4.Add( self.m_comboBox5, 0, 0, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Minimum Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Maximum Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer4.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Check-In Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		m_comboBox6Choices = []
		self.m_comboBox6 = wx.ComboBox( self, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox6Choices, 0 )
		gSizer4.Add( self.m_comboBox6, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Check-Out Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer4.Add( self.m_staticText16, 0, wx.ALL, 5 )

		m_comboBox7Choices = []
		self.m_comboBox7 = wx.ComboBox( self, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		gSizer4.Add( self.m_comboBox7, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Room Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		gSizer4.Add( self.m_staticText19, 0, wx.ALL, 5 )

		m_comboBox8Choices = []
		self.m_comboBox8 = wx.ComboBox( self, wx.ID_ANY, u"Room type", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, 0 )
		gSizer4.Add( self.m_comboBox8, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Search Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer4.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Cleanliness Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
... (53줄 남음)
접기
message.txt
6KB
﻿
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
## Class Software
###########################################################################

class Software ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Airbnb Data Analysis Software", pos = wx.DefaultPosition, size = wx.Size( 1168,349 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 3, 10, 0, 0 )

		gSizer4.SetMinSize( wx.Size( -3,-3 ) )
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )

		m_comboBox5Choices = []
		self.m_comboBox5 = wx.ComboBox( self, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, m_comboBox5Choices, 0 )
		gSizer4.Add( self.m_comboBox5, 0, 0, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Minimum Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Maximum Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer4.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Check-In Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		m_comboBox6Choices = []
		self.m_comboBox6 = wx.ComboBox( self, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox6Choices, 0 )
		gSizer4.Add( self.m_comboBox6, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Check-Out Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer4.Add( self.m_staticText16, 0, wx.ALL, 5 )

		m_comboBox7Choices = []
		self.m_comboBox7 = wx.ComboBox( self, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		gSizer4.Add( self.m_comboBox7, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Room Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		gSizer4.Add( self.m_staticText19, 0, wx.ALL, 5 )

		m_comboBox8Choices = []
		self.m_comboBox8 = wx.ComboBox( self, wx.ID_ANY, u"Room type", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, 0 )
		gSizer4.Add( self.m_comboBox8, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Search Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer4.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Cleanliness Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.Search = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Search.SetBackgroundColour( wx.Colour( 185, 185, 255 ) )

		gSizer4.Add( self.Search, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetBackgroundColour( wx.Colour( 185, 185, 255 ) )

		gSizer4.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer4.Add( gSizer4, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_grid4 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid4.CreateGrid( 5, 5 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )

		# Columns
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.m_grid4, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


message.txt
6KB