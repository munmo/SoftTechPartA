import wx
import wx.grid
import pandas as pd

from SuburbTem import Suburb
from PriceDistribution_Run import Price
from KeywordTem import Keyword
from CleanlinessTem import Cleanliness
from PriceDistribution_Run import Price #Linked
from Keyword_Run import Keyword
from Cleanliness_Run import Cleanliness
from PriceRangeTem import PriceRange
from PriceRange_run import PriceRange # linked
from Suburb_run import Suburb # Linked

# changed the even row colour to baby pink (thought it would match with our background colour(which is lightblue)
EVEN_ROW_COLOUR = '#F7DAD9'
GRID_LINE_COLOUR = '#ccc'

df1 = pd.read_csv("listings_dec18.csv", low_memory=False)
df2 = pd.read_csv("reviews_dec18.csv", low_memory=False)
df3 = pd.read_csv("calendar_dec18.csv", low_memory=False)

# buttons for navigation
class Main(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title=u"Airbnb Data Software", pos=wx.DefaultPosition,
                          size=wx.Size(874, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(1, 5, 0, 0)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Suburb Listing", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetBackgroundColour(wx.Colour(255, 174, 174))

        gSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"Price Distribution", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        self.m_button2.SetBackgroundColour(wx.Colour(255, 174, 174))

        gSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"Search Keyword", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetBackgroundColour(wx.Colour(255, 174, 174))

        gSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"Cleanliness", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetBackgroundColour(wx.Colour(255, 174, 174))

        gSizer1.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"Price Range", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetBackgroundColour(wx.Colour(255, 174, 174))

        gSizer1.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(gSizer1)
        self.m_panel1.Layout()
        gSizer1.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

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
        bSizer1.Add(self.m_grid2, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.OnSuburb)
        self.m_button2.Bind(wx.EVT_BUTTON, self.OnPriceDist)
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnKeyword)
        self.m_button4.Bind(wx.EVT_BUTTON, self.OnCleanliness)
        self.m_button5.Bind(wx.EVT_BUTTON, self.OnPriceRange)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def OnSuburb(self, event):
        secondWindow = Suburb(self)
        secondWindow.Show()

    def OnPriceDist(self, event):
        secondWindow = Price(self)
        secondWindow.Show()

    def OnKeyword(self, event):
        secondWindow = Keyword(self)
        secondWindow.Show()

    def OnCleanliness(self, event):
        secondWindow = Cleanliness(self)
        secondWindow.Show()

    def OnPriceRange(self, event):
        secondWindow = PriceRange(self)
        secondWindow.Show()

    def OnKeyword(self, event):
        secondWindow = Keyword(self)
        secondWindow.Show()

    def OnCleanliness(self, event):
        secondWindow = Cleanliness(self)
        secondWindow.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = Main(None)  # Pass None as the parent
    frame.Show()  # This line is necessary to show the frame
    app.MainLoop()