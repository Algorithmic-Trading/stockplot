import numpy as np
import pandas as pd
from randomwalk import *
from plotly.tools import FigureFactory as FF
import plotly.offline as pyo
import plotly.graph_objs as go
import stockstats as ss
pyo.init_notebook_mode(connected=True)


class Base:
    """candlec chartとその指標を描くクラス
    入力: ohlcデータフレーム
    出力: plrtolyファイル(htmlファイル)"""

    def __init__(self, df):
        # self.df = df
        self.df = ss.StockDataFrame(df)
        self.add_line = []  # indicatorプロットの入れ子

    # ----------DATA MAKE----------
    def _sma_(self, window, columns='close'):
        """Simple Moving Average
        windowの足の分だけ移動平均
        dfに格納する
        column名はSMA{移動した足}

        引数:
            window: 移動足
            columns: 平均を適用する足{open, high, low, close}どれか
        戻り値: smaを格納したdf"""
        colname = 'SMA%d' % window
        self.df[colname] = self.df[columns].rolling(window).mean()
        plotter = go.Scatter(x=self.df.index, y=self.df[colname],
                             name=colname)
        self.add_line.append(plotter)
        return self.df

    def sma(self, indicator, name=None):
        """example
        `Base.sma('close_5_sma')`

        **then**

        * DataFrame will be added SMA5 columns
        * Add column made by above to plotly data (named 'self.add_line')

        More information will be show if you type `base_chart.ss.StockDataFrame._get_sma?`

        ``` python
        # Set sampltdata
        from randomwalk import randomwalk
        df = randomwalk(10000, freq='T').resample('H').ohlc(); df

        import basechart as B

        # Candlechart add
        x = B.Base(df)
        x.plot()

        # SMA 5 add
        x.sma('close_5_sma')
        x.plot()
        ```

        """
        self.df.get(indicator)
        plotter = go.Scatter(x=self.df.index, y=self.df[indicator],
                             name=indicator if name is None else name)
        self.add_line.append(plotter)
        return self.df

    # ---------PLOT----------
    def plot(self, filename='candlestick_and_trace.html'):
        fig = FF.create_candlestick(self.df.open, self.df.high,
                                    self.df.low, self.df.close, dates=self.df.index)
        fig['data'].extend(self.add_line)
        fig['layout'].update(xaxis={'showgrid': True})
        pyo.plot(fig, filename=filename, validate=False)


if __name__ == '__main__':
    np.random.seed(1)
    df = randomwalk(60 * 24 * 90, freq='T', tick=0.01,
                    start=pd.datetime(2017, 3, 20)).resample('B').ohlc() + 115
    x = Base(df)  # ohlcをbaseに渡す
    # x.bollinger(20)
    # x.bollinger(20, 1)
    x.sma('close_5_sma')
    x.sma('close_25_sma')
    x.sma('close_25_ema')
    # x.ema(5)
    # x.ema(25)
    print(x.df.tail(5))
    x.plot()
