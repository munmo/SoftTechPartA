import wx
import wx.grid
import pandas as pd

from WK06 import Software as Software2





def OnSearch(self, event):
    min_price = float(self.m_textCtrl0.GetValue())
    ## change the temperature to price
    # df_1 = df[df['temperature_celsius'] > min_price]

    max_price = float(self.m_textCtrl11.GetValue())
    ## change the temperature to price
    # df_1 = df_1[df_1['temperature_celsius'] < max_price]

    tabel = DataTable(df_1)
    self.m_grid2.ClearGrid()
    self.m_grid2.SetTable(tabel, True)
    self.m_grid2.AutoSize()
    self.Layout()

if __name__ == "__main__":

    app = wx.App(False)
    ##frame = CalcFrame()
    app.MainLoop()

