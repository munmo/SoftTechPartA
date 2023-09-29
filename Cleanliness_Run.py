import wx
import wx.grid
import pandas as pd


class Cleanliness (wx.Frame):

	def __init__( self, parent ):
		wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"Airbnb Data Software", pos = wx.DefaultPosition, size = wx.Size(874, 300), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		fgSizer11 = wx.FlexGridSizer(2, 3, 0, 0)
		fgSizer11.SetFlexibleDirection(wx.BOTH)
		fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Select Cleanliness Keyword", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)

		fgSizer11.Add(self.m_staticText4, 0, wx.ALL, 5)

		m_comboBox1Choices = ['Aseptic', 'Crisp', 'Disinfected', 'Elegant', 'Fresh', 'Gleaming', 'Hygienic',
							  'Immaculate', 'Neat', 'Pristine', 'Sanitary', 'Shining', 'Spotless', 'Sterile',
							  'Tidy', 'Unblemished', 'Well-kept']

		self.m_comboBox1 = wx.ComboBox(self.m_panel2, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0)
		fgSizer11.Add(self.m_comboBox1, 0, wx.ALL, 5)

		self.m_button6 = wx.Button(self.m_panel2, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button6.SetBackgroundColour(wx.Colour(255, 255, 174))

		fgSizer11.Add(self.m_button6, 0, wx.ALL, 5)

		self.result_count_label = wx.StaticText(self.m_panel2, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer11.Add(self.result_count_label, 0, wx.ALL, 5)

		self.m_panel2.SetSizer(fgSizer11)
		self.m_panel2.Layout()
		fgSizer11.Fit(self.m_panel2)
		bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

		fgSizer12 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer12.SetFlexibleDirection(wx.BOTH)
		fgSizer12.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

		# Grid
		self.m_grid2.CreateGrid(5, 2)
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
		self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
		fgSizer12.Add(self.m_grid2, 0, wx.ALL, 5)

		bSizer1.Add(fgSizer12, 1, wx.EXPAND, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button6.Bind(wx.EVT_BUTTON, self.OnSearch)

		# Column names
		self.m_grid2.SetColLabelValue(0, 'Listing ID')
		self.m_grid2.SetColLabelValue(1, 'Comments')

	def __del__( self ):
		pass

	def OnSearch(self, event):
		try:
			cleanliness_keyword = self.m_comboBox1.GetValue()

			if not cleanliness_keyword:
				wx.MessageBox("Please select a cleanliness keyword.", "Error", wx.OK | wx.ICON_ERROR)
				return

			df_reviews = pd.read_csv("reviews_dec18.csv", usecols=['listing_id', 'comments'])
			df_filtered_reviews = df_reviews[df_reviews['comments'].str.contains(cleanliness_keyword, case=False, na=False)]

			num_rows = len(df_filtered_reviews)
			self.result_count_label.SetLabel(f"Number of Results: {num_rows}")

			self.m_grid2.ClearGrid()
			self.m_grid2.DeleteCols(0, self.m_grid2.GetNumberCols())
			self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())
			self.m_grid2.AppendRows(num_rows)

			self.m_grid2.AppendCols(len(df_filtered_reviews.columns))
			self.m_grid2.SetColLabelValue(0, 'Listing ID')
			self.m_grid2.SetColLabelValue(1, 'Comments')

			for row, (_, row_data) in enumerate(df_filtered_reviews.iterrows()):
				for col, value in enumerate(row_data):
					self.m_grid2.SetCellValue(row, col, str(value))

			self.m_grid2.AutoSize()
			self.m_grid2.Refresh()

		except Exception as e:
			wx.LogError(f"Error: {e}")
			return

		if df_filtered_reviews.empty:
			wx.MessageBox(f"No data available for the selected date range with keyword '{keyword}'.", "Info", wx.OK | wx.ICON_INFORMATION)
			return

if __name__ == "__main__":
	app = wx.App(False)
	frame = Cleanliness(None)
	frame.Show(True)
	app.MainLoop()

