# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Airbnb Data Software", pos = wx.DefaultPosition, size = wx.Size( 874,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 1, 5, 0, 0 )

		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Suburb Listing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetBackgroundColour( wx.Colour( 255, 174, 174 ) )

		gSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Price Distribution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetBackgroundColour( wx.Colour( 255, 174, 174 ) )

		gSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"Search Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetBackgroundColour( wx.Colour( 255, 174, 174 ) )

		gSizer1.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"Cleanliness", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetBackgroundColour( wx.Colour( 255, 174, 174 ) )

		gSizer1.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"Price Range", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetBackgroundColour( wx.Colour( 255, 174, 174 ) )

		gSizer1.Add( self.m_button5, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( gSizer1 )
		self.m_panel1.Layout()
		gSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnSuburb )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnPriceDist )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnKeyword )
		self.m_button4.Bind( wx.EVT_BUTTON, self.OnCleanliness )
		self.m_button5.Bind( wx.EVT_BUTTON, self.OnPriceRange )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnSuburb( self, event ):
		event.Skip()

	def OnPriceDist( self, event ):
		event.Skip()

	def OnKeyword( self, event ):
		event.Skip()

	def OnCleanliness( self, event ):
		event.Skip()

	def OnPriceRange( self, event ):
		event.Skip()


