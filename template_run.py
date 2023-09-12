import wx
import wx.grid
import pandas as pd

from MainTem import Main as Main1
from SuburbTem import Suburb as Suburb1

# changed the even row colour to baby pink (thought it would match with our background colour(which is lightblue)
EVEN_ROW_COLOUR = '#F7DAD9'
GRID_LINE_COLOUR = '#ccc'

df1 = pd.read_csv("listings_dec18.csv", low_memory=False)
df2 = pd.read_csv("reviews_dec18.csv", low_memory=False)
df3 = pd.read_csv("listings_summary_dec18.csv", low_memory=False)


# buttons for navigation
class MainFrame(Main1):
    def __init__(self, parent=None, title=u"Airbnb Data Software", size=wx.Size(874, 300)):
        wx.Frame.__init__(self, parent=parent, title=title, size=size)

        panel = wx.Panel(self)
        button_suburb = wx.Button(panel, label="Open Suburb Window")
        button_suburb.Bind(wx.EVT_BUTTON, self.open_suburb_window)

        # Add more widgets and layout for your main window here

    def open_suburb_window(self, event):
        secondWindow = Suburb(self)
        secondWindow.Show()


class Suburb(Suburb1):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.ID_ANY, title=u"Suburb Window", size=wx.Size(874, 300))
        self.Centre()
        # Add widgets and layout for your suburb window here


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
