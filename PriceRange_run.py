import wx
import wx.grid
import pandas as pd

from PriceRangeTem import PriceRange as PriceRange1

# changed the even row colour to baby pink (thought it would match with our background colour(which is lightblue)
EVEN_ROW_COLOUR = '#F7DAD9'
GRID_LINE_COLOUR = '#ccc'

df1 = pd.read_csv("listings_dec18.csv", low_memory=False)
df2 = pd.read_csv("reviews_dec18.csv", low_memory=False)
df3 = pd.read_csv("calendar_dec18.csv", low_memory=False)


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


class DataFrame(PriceRange1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = DataTable(df1)

        self.m_grid2.SetTable(self.table, takeOwnership=True)
        self.m_grid2.AutoSize()
        self.Show(True)
        self.Layout()

    def OnSearch(self, event):
        min_price = float(self.m_textCtrl2.GetValue())
        df1_1 = df1[df1['price'] > min_price]
        max_price = float(self.m_textCtrl3.GetValue())
        df1_1 = df1_1[df1_1['price'] < max_price]

        tabel = DataTable(df1_1)
        self.m_grid2.ClearGrid()
        self.m_grid2.SetTable(tabel, True)
        self.m_grid2.AutoSize()
        self.Layout()



if __name__ == "__main__":
    app = wx.App(False)
    frame = DataFrame()
    app.MainLoop()
