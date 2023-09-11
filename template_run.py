import wx
import wx.grid
import pandas as pd

from template import Software as Software2

#changed the even row colour to baby pink (thought it would match with our background colour(which is lightblue)
EVEN_ROW_COLOUR = '#F7DAD9'
GRID_LINE_COLOUR = '#ccc'

df1 = pd.read_csv("listings_dec18.csv", low_memory=False)
df2 = pd.read_csv("reviews_dec18.csv", low_memory=False)
df3 = pd.read_csv("listings_summary_dec18.csv", low_memory=False)


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


class SoftwareFrame(Software2):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.table = DataTable(df3)
        self.m_grid4.SetTable(self.table, takeOwnership=True)
        self.m_grid4.AutoSize()
        self.Show(True)
        self.Layout()
    def OnSearch(self, event):
        min_price = float(self.m_textCtrl10.GetValue())
        df3_1 = df3[df3['price'] > min_price]

        max_price = float(self.m_textCtrl11.GetValue())
        df3_1 = df3[df3['price'] < max_price]

        tabel = DataTable(df3_1)
        self.m_grid4.ClearGrid()
        self.m_grid4.SetTable(tabel, True)
        self.m_grid4.AutoSize()
        self.Layout()

# I dont know whats wrong with this part :(
if __name__ == "__main__":

    app = wx.App(False)
    frame = SoftwareFrame()
    app.MainLoop()
