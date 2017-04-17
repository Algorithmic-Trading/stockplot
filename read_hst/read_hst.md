
# ヒストリカルデータの読み込み

## ヒストリカルデータの扱い方
* [FXDD - メタトレーダのヒストリカルデータ](http://www.fxdd.com/bm/jp/forex-resources/forex-trading-tools/metatrader-1-minute-data/)よりzipファイルをダウンロード。
* 解凍して.hstを取り出す。
* 以下の`hst_to_df.py`に食べさせると.h5ファイルのうんこを出す。


```python
 %run hst_to_df.py  -f data/EURUSD.hst -ty old 
```

    --- Convert Start ---
    `EURUSD/EURUSD.hst` --> `EURUSD/EURUSD.h5` ---
    Please wait a moment...
    
                            open     high      low    close  volume
    openTime                                                       
    2005-01-10 02:31:00  1.30470  1.30550  1.30470  1.30540    12.0
    2005-01-10 02:32:00  1.30540  1.30580  1.30540  1.30550    10.0
    2005-01-10 02:33:00  1.30550  1.30550  1.30540  1.30540     4.0
    2005-01-10 02:34:00  1.30540  1.30540  1.30540  1.30540     5.0
    2005-01-10 02:35:00  1.30540  1.30540  1.30540  1.30540     3.0
    2005-01-10 02:36:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:37:00  1.30540  1.30540  1.30530  1.30540     6.0
    2005-01-10 02:38:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:39:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:40:00  1.30540  1.30540  1.30540  1.30540     3.0
    2005-01-10 02:41:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:42:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:43:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:44:00  1.30540  1.30540  1.30540  1.30540     3.0
    2005-01-10 02:45:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:46:00  1.30540  1.30540  1.30540  1.30540     2.0
    2005-01-10 02:47:00  1.30540  1.30540  1.30540  1.30540     3.0
    2005-01-10 02:48:00  1.30540  1.30620  1.30540  1.30580    15.0
    2005-01-10 02:49:00  1.30570  1.30630  1.30570  1.30610    18.0
    2005-01-10 02:50:00  1.30610  1.30630  1.30610  1.30630    23.0
    2005-01-10 02:51:00  1.30650  1.30660  1.30620  1.30650    12.0
    2005-01-10 02:52:00  1.30640  1.30670  1.30640  1.30660    10.0
    2005-01-10 02:53:00  1.30660  1.30670  1.30650  1.30670     8.0
    2005-01-10 02:54:00  1.30660  1.30660  1.30660  1.30660     4.0
    2005-01-10 02:55:00  1.30650  1.30670  1.30650  1.30670    11.0
    2005-01-10 02:56:00  1.30670  1.30680  1.30670  1.30680     5.0
    2005-01-10 02:57:00  1.30690  1.30710  1.30680  1.30710    21.0
    2005-01-10 02:58:00  1.30710  1.30720  1.30710  1.30720     4.0
    2005-01-10 02:59:00  1.30720  1.30720  1.30720  1.30720     3.0
    2005-01-10 03:00:00  1.30720  1.30720  1.30720  1.30720     2.0
    ...                      ...      ...      ...      ...     ...
    2016-12-23 23:16:00  1.04495  1.04497  1.04495  1.04496    15.0
    2016-12-23 23:17:00  1.04496  1.04502  1.04496  1.04498    23.0
    2016-12-23 23:18:00  1.04498  1.04511  1.04497  1.04506    24.0
    2016-12-23 23:19:00  1.04506  1.04506  1.04504  1.04504    12.0
    2016-12-23 23:20:00  1.04504  1.04505  1.04504  1.04505    14.0
    2016-12-23 23:21:00  1.04505  1.04507  1.04505  1.04507     9.0
    2016-12-23 23:22:00  1.04509  1.04509  1.04504  1.04504    18.0
    2016-12-23 23:23:00  1.04504  1.04505  1.04503  1.04503    11.0
    2016-12-23 23:24:00  1.04505  1.04505  1.04505  1.04505    42.0
    2016-12-23 23:25:00  1.04505  1.04505  1.04504  1.04504    23.0
    2016-12-23 23:26:00  1.04504  1.04504  1.04493  1.04494    16.0
    2016-12-23 23:27:00  1.04494  1.04494  1.04494  1.04494     6.0
    2016-12-23 23:28:00  1.04494  1.04496  1.04492  1.04496    27.0
    2016-12-23 23:29:00  1.04496  1.04500  1.04496  1.04498    17.0
    2016-12-23 23:30:00  1.04498  1.04499  1.04498  1.04498    19.0
    2016-12-23 23:31:00  1.04498  1.04498  1.04498  1.04498     5.0
    2016-12-23 23:32:00  1.04499  1.04501  1.04499  1.04501    11.0
    2016-12-23 23:33:00  1.04501  1.04504  1.04498  1.04503    13.0
    2016-12-23 23:34:00  1.04503  1.04503  1.04501  1.04501    12.0
    2016-12-23 23:35:00  1.04501  1.04501  1.04501  1.04501     6.0
    2016-12-23 23:36:00  1.04501  1.04506  1.04501  1.04505    39.0
    2016-12-23 23:37:00  1.04505  1.04505  1.04505  1.04505     4.0
    2016-12-23 23:38:00  1.04506  1.04507  1.04504  1.04507    63.0
    2016-12-23 23:39:00  1.04507  1.04511  1.04507  1.04509    55.0
    2016-12-23 23:40:00  1.04510  1.04511  1.04507  1.04508   104.0
    2016-12-23 23:41:00  1.04508  1.04518  1.04508  1.04518    32.0
    2016-12-23 23:42:00  1.04517  1.04522  1.04517  1.04522    18.0
    2016-12-23 23:43:00  1.04521  1.04525  1.04521  1.04524    22.0
    2016-12-23 23:44:00  1.04525  1.04528  1.04518  1.04524    42.0
    2016-12-23 23:45:00  1.04526  1.04527  1.04522  1.04526    18.0
    
    [4352848 rows x 5 columns]
    
    ---End of Convert---
    Using EURUSD/EURUSD.h5 file, type below...
    `df = pd.read_hdf(EURUSD/EURUSD.h5, key="main")`
    

## hdfファイル(.h5)の扱い


```python
df = pd.read_hdf('data/EURUSD.h5', key="main")
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>openTime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2005-01-10 02:31:00</th>
      <td>1.30470</td>
      <td>1.30550</td>
      <td>1.30470</td>
      <td>1.30540</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:32:00</th>
      <td>1.30540</td>
      <td>1.30580</td>
      <td>1.30540</td>
      <td>1.30550</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:33:00</th>
      <td>1.30550</td>
      <td>1.30550</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:34:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:35:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:36:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:37:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30530</td>
      <td>1.30540</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:38:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:39:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:40:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:41:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:42:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:43:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:44:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:45:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:46:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:47:00</th>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>1.30540</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:48:00</th>
      <td>1.30540</td>
      <td>1.30620</td>
      <td>1.30540</td>
      <td>1.30580</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:49:00</th>
      <td>1.30570</td>
      <td>1.30630</td>
      <td>1.30570</td>
      <td>1.30610</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:50:00</th>
      <td>1.30610</td>
      <td>1.30630</td>
      <td>1.30610</td>
      <td>1.30630</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:51:00</th>
      <td>1.30650</td>
      <td>1.30660</td>
      <td>1.30620</td>
      <td>1.30650</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:52:00</th>
      <td>1.30640</td>
      <td>1.30670</td>
      <td>1.30640</td>
      <td>1.30660</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:53:00</th>
      <td>1.30660</td>
      <td>1.30670</td>
      <td>1.30650</td>
      <td>1.30670</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:54:00</th>
      <td>1.30660</td>
      <td>1.30660</td>
      <td>1.30660</td>
      <td>1.30660</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:55:00</th>
      <td>1.30650</td>
      <td>1.30670</td>
      <td>1.30650</td>
      <td>1.30670</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:56:00</th>
      <td>1.30670</td>
      <td>1.30680</td>
      <td>1.30670</td>
      <td>1.30680</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:57:00</th>
      <td>1.30690</td>
      <td>1.30710</td>
      <td>1.30680</td>
      <td>1.30710</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:58:00</th>
      <td>1.30710</td>
      <td>1.30720</td>
      <td>1.30710</td>
      <td>1.30720</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2005-01-10 02:59:00</th>
      <td>1.30720</td>
      <td>1.30720</td>
      <td>1.30720</td>
      <td>1.30720</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2005-01-10 03:00:00</th>
      <td>1.30720</td>
      <td>1.30720</td>
      <td>1.30720</td>
      <td>1.30720</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-12-23 23:16:00</th>
      <td>1.04495</td>
      <td>1.04497</td>
      <td>1.04495</td>
      <td>1.04496</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:17:00</th>
      <td>1.04496</td>
      <td>1.04502</td>
      <td>1.04496</td>
      <td>1.04498</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:18:00</th>
      <td>1.04498</td>
      <td>1.04511</td>
      <td>1.04497</td>
      <td>1.04506</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:19:00</th>
      <td>1.04506</td>
      <td>1.04506</td>
      <td>1.04504</td>
      <td>1.04504</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:20:00</th>
      <td>1.04504</td>
      <td>1.04505</td>
      <td>1.04504</td>
      <td>1.04505</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:21:00</th>
      <td>1.04505</td>
      <td>1.04507</td>
      <td>1.04505</td>
      <td>1.04507</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:22:00</th>
      <td>1.04509</td>
      <td>1.04509</td>
      <td>1.04504</td>
      <td>1.04504</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:23:00</th>
      <td>1.04504</td>
      <td>1.04505</td>
      <td>1.04503</td>
      <td>1.04503</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:24:00</th>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:25:00</th>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>1.04504</td>
      <td>1.04504</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:26:00</th>
      <td>1.04504</td>
      <td>1.04504</td>
      <td>1.04493</td>
      <td>1.04494</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:27:00</th>
      <td>1.04494</td>
      <td>1.04494</td>
      <td>1.04494</td>
      <td>1.04494</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:28:00</th>
      <td>1.04494</td>
      <td>1.04496</td>
      <td>1.04492</td>
      <td>1.04496</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:29:00</th>
      <td>1.04496</td>
      <td>1.04500</td>
      <td>1.04496</td>
      <td>1.04498</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:30:00</th>
      <td>1.04498</td>
      <td>1.04499</td>
      <td>1.04498</td>
      <td>1.04498</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:31:00</th>
      <td>1.04498</td>
      <td>1.04498</td>
      <td>1.04498</td>
      <td>1.04498</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:32:00</th>
      <td>1.04499</td>
      <td>1.04501</td>
      <td>1.04499</td>
      <td>1.04501</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:33:00</th>
      <td>1.04501</td>
      <td>1.04504</td>
      <td>1.04498</td>
      <td>1.04503</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:34:00</th>
      <td>1.04503</td>
      <td>1.04503</td>
      <td>1.04501</td>
      <td>1.04501</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:35:00</th>
      <td>1.04501</td>
      <td>1.04501</td>
      <td>1.04501</td>
      <td>1.04501</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:36:00</th>
      <td>1.04501</td>
      <td>1.04506</td>
      <td>1.04501</td>
      <td>1.04505</td>
      <td>39.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:37:00</th>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>1.04505</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:38:00</th>
      <td>1.04506</td>
      <td>1.04507</td>
      <td>1.04504</td>
      <td>1.04507</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:39:00</th>
      <td>1.04507</td>
      <td>1.04511</td>
      <td>1.04507</td>
      <td>1.04509</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:40:00</th>
      <td>1.04510</td>
      <td>1.04511</td>
      <td>1.04507</td>
      <td>1.04508</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:41:00</th>
      <td>1.04508</td>
      <td>1.04518</td>
      <td>1.04508</td>
      <td>1.04518</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:42:00</th>
      <td>1.04517</td>
      <td>1.04522</td>
      <td>1.04517</td>
      <td>1.04522</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:43:00</th>
      <td>1.04521</td>
      <td>1.04525</td>
      <td>1.04521</td>
      <td>1.04524</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:44:00</th>
      <td>1.04525</td>
      <td>1.04528</td>
      <td>1.04518</td>
      <td>1.04524</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>2016-12-23 23:45:00</th>
      <td>1.04526</td>
      <td>1.04527</td>
      <td>1.04522</td>
      <td>1.04526</td>
      <td>18.0</td>
    </tr>
  </tbody>
</table>
<p>4352848 rows × 5 columns</p>
</div>



open, high, low, closeだけにして、
resampleで指定した期間だけデータを丸める

休日はbfill()かdropna()でなくす

## 日足に圧縮する


```python
dff = df.ix[:, :4].resample('d').agg({'open':'first',
                                      'high':'max',
                                      'low':'min',
                                      'close':'last'}).dropna()
dff
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>low</th>
      <th>open</th>
      <th>high</th>
      <th>close</th>
    </tr>
    <tr>
      <th>openTime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2005-01-10</th>
      <td>1.30470</td>
      <td>1.30470</td>
      <td>1.31220</td>
      <td>1.30830</td>
    </tr>
    <tr>
      <th>2005-01-11</th>
      <td>1.30650</td>
      <td>1.30830</td>
      <td>1.31700</td>
      <td>1.31110</td>
    </tr>
    <tr>
      <th>2005-01-12</th>
      <td>1.30810</td>
      <td>1.31100</td>
      <td>1.32920</td>
      <td>1.32630</td>
    </tr>
    <tr>
      <th>2005-01-13</th>
      <td>1.31920</td>
      <td>1.32620</td>
      <td>1.32660</td>
      <td>1.32190</td>
    </tr>
    <tr>
      <th>2005-01-14</th>
      <td>1.30550</td>
      <td>1.32210</td>
      <td>1.32260</td>
      <td>1.31070</td>
    </tr>
    <tr>
      <th>2005-01-17</th>
      <td>1.30630</td>
      <td>1.31040</td>
      <td>1.31250</td>
      <td>1.30670</td>
    </tr>
    <tr>
      <th>2005-01-18</th>
      <td>1.29930</td>
      <td>1.30660</td>
      <td>1.30750</td>
      <td>1.30200</td>
    </tr>
    <tr>
      <th>2005-01-19</th>
      <td>1.29640</td>
      <td>1.30210</td>
      <td>1.31180</td>
      <td>1.30050</td>
    </tr>
    <tr>
      <th>2005-01-20</th>
      <td>1.29200</td>
      <td>1.30050</td>
      <td>1.30220</td>
      <td>1.29710</td>
    </tr>
    <tr>
      <th>2005-01-21</th>
      <td>1.29330</td>
      <td>1.29700</td>
      <td>1.30650</td>
      <td>1.30540</td>
    </tr>
    <tr>
      <th>2005-01-24</th>
      <td>1.30270</td>
      <td>1.30460</td>
      <td>1.30990</td>
      <td>1.30580</td>
    </tr>
    <tr>
      <th>2005-01-25</th>
      <td>1.29440</td>
      <td>1.30570</td>
      <td>1.30760</td>
      <td>1.29680</td>
    </tr>
    <tr>
      <th>2005-01-26</th>
      <td>1.29650</td>
      <td>1.29690</td>
      <td>1.31070</td>
      <td>1.30730</td>
    </tr>
    <tr>
      <th>2005-01-27</th>
      <td>1.30120</td>
      <td>1.30730</td>
      <td>1.31230</td>
      <td>1.30340</td>
    </tr>
    <tr>
      <th>2005-01-28</th>
      <td>1.29840</td>
      <td>1.30330</td>
      <td>1.30770</td>
      <td>1.30400</td>
    </tr>
    <tr>
      <th>2005-01-31</th>
      <td>1.29730</td>
      <td>1.30190</td>
      <td>1.30580</td>
      <td>1.30330</td>
    </tr>
    <tr>
      <th>2005-02-01</th>
      <td>1.30010</td>
      <td>1.30340</td>
      <td>1.30630</td>
      <td>1.30430</td>
    </tr>
    <tr>
      <th>2005-02-02</th>
      <td>1.30080</td>
      <td>1.30440</td>
      <td>1.30910</td>
      <td>1.30320</td>
    </tr>
    <tr>
      <th>2005-02-03</th>
      <td>1.29370</td>
      <td>1.30310</td>
      <td>1.30350</td>
      <td>1.29710</td>
    </tr>
    <tr>
      <th>2005-02-04</th>
      <td>1.28660</td>
      <td>1.29700</td>
      <td>1.30410</td>
      <td>1.28730</td>
    </tr>
    <tr>
      <th>2005-02-07</th>
      <td>1.27290</td>
      <td>1.28710</td>
      <td>1.28710</td>
      <td>1.27630</td>
    </tr>
    <tr>
      <th>2005-02-08</th>
      <td>1.27320</td>
      <td>1.27640</td>
      <td>1.27960</td>
      <td>1.27660</td>
    </tr>
    <tr>
      <th>2005-02-09</th>
      <td>1.27380</td>
      <td>1.27670</td>
      <td>1.28120</td>
      <td>1.28040</td>
    </tr>
    <tr>
      <th>2005-02-10</th>
      <td>1.27370</td>
      <td>1.28030</td>
      <td>1.29040</td>
      <td>1.28700</td>
    </tr>
    <tr>
      <th>2005-02-11</th>
      <td>1.28460</td>
      <td>1.28690</td>
      <td>1.28930</td>
      <td>1.28650</td>
    </tr>
    <tr>
      <th>2005-02-14</th>
      <td>1.28750</td>
      <td>1.28750</td>
      <td>1.29890</td>
      <td>1.29600</td>
    </tr>
    <tr>
      <th>2005-02-15</th>
      <td>1.29530</td>
      <td>1.29610</td>
      <td>1.30500</td>
      <td>1.30170</td>
    </tr>
    <tr>
      <th>2005-02-16</th>
      <td>1.29590</td>
      <td>1.30170</td>
      <td>1.30640</td>
      <td>1.30240</td>
    </tr>
    <tr>
      <th>2005-02-17</th>
      <td>1.30130</td>
      <td>1.30240</td>
      <td>1.30870</td>
      <td>1.30750</td>
    </tr>
    <tr>
      <th>2005-02-18</th>
      <td>1.30130</td>
      <td>1.30740</td>
      <td>1.30800</td>
      <td>1.30630</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-11-14</th>
      <td>1.07081</td>
      <td>1.08269</td>
      <td>1.08394</td>
      <td>1.07359</td>
    </tr>
    <tr>
      <th>2016-11-15</th>
      <td>1.07132</td>
      <td>1.07357</td>
      <td>1.08155</td>
      <td>1.07186</td>
    </tr>
    <tr>
      <th>2016-11-16</th>
      <td>1.06652</td>
      <td>1.07190</td>
      <td>1.07586</td>
      <td>1.06893</td>
    </tr>
    <tr>
      <th>2016-11-17</th>
      <td>1.06191</td>
      <td>1.06892</td>
      <td>1.07447</td>
      <td>1.06258</td>
    </tr>
    <tr>
      <th>2016-11-18</th>
      <td>1.05683</td>
      <td>1.06261</td>
      <td>1.06419</td>
      <td>1.05905</td>
    </tr>
    <tr>
      <th>2016-11-21</th>
      <td>1.05775</td>
      <td>1.05908</td>
      <td>1.06483</td>
      <td>1.06263</td>
    </tr>
    <tr>
      <th>2016-11-22</th>
      <td>1.05828</td>
      <td>1.06255</td>
      <td>1.06569</td>
      <td>1.06256</td>
    </tr>
    <tr>
      <th>2016-11-23</th>
      <td>1.05252</td>
      <td>1.06228</td>
      <td>1.06427</td>
      <td>1.05518</td>
    </tr>
    <tr>
      <th>2016-11-24</th>
      <td>1.05171</td>
      <td>1.05494</td>
      <td>1.05844</td>
      <td>1.05501</td>
    </tr>
    <tr>
      <th>2016-11-25</th>
      <td>1.05376</td>
      <td>1.05482</td>
      <td>1.06265</td>
      <td>1.05947</td>
    </tr>
    <tr>
      <th>2016-11-28</th>
      <td>1.05627</td>
      <td>1.06049</td>
      <td>1.06847</td>
      <td>1.06125</td>
    </tr>
    <tr>
      <th>2016-11-29</th>
      <td>1.05641</td>
      <td>1.06117</td>
      <td>1.06534</td>
      <td>1.06484</td>
    </tr>
    <tr>
      <th>2016-11-30</th>
      <td>1.05518</td>
      <td>1.06473</td>
      <td>1.06657</td>
      <td>1.05871</td>
    </tr>
    <tr>
      <th>2016-12-01</th>
      <td>1.05837</td>
      <td>1.05872</td>
      <td>1.06678</td>
      <td>1.06583</td>
    </tr>
    <tr>
      <th>2016-12-02</th>
      <td>1.06243</td>
      <td>1.06588</td>
      <td>1.06889</td>
      <td>1.06676</td>
    </tr>
    <tr>
      <th>2016-12-05</th>
      <td>1.05040</td>
      <td>1.06263</td>
      <td>1.07956</td>
      <td>1.07618</td>
    </tr>
    <tr>
      <th>2016-12-06</th>
      <td>1.06976</td>
      <td>1.07618</td>
      <td>1.07844</td>
      <td>1.07176</td>
    </tr>
    <tr>
      <th>2016-12-07</th>
      <td>1.07090</td>
      <td>1.07154</td>
      <td>1.07673</td>
      <td>1.07514</td>
    </tr>
    <tr>
      <th>2016-12-08</th>
      <td>1.05963</td>
      <td>1.07513</td>
      <td>1.08728</td>
      <td>1.06116</td>
    </tr>
    <tr>
      <th>2016-12-09</th>
      <td>1.05301</td>
      <td>1.06113</td>
      <td>1.06289</td>
      <td>1.05554</td>
    </tr>
    <tr>
      <th>2016-12-12</th>
      <td>1.05244</td>
      <td>1.05287</td>
      <td>1.06508</td>
      <td>1.06336</td>
    </tr>
    <tr>
      <th>2016-12-13</th>
      <td>1.06030</td>
      <td>1.06323</td>
      <td>1.06664</td>
      <td>1.06238</td>
    </tr>
    <tr>
      <th>2016-12-14</th>
      <td>1.04954</td>
      <td>1.06238</td>
      <td>1.06693</td>
      <td>1.05328</td>
    </tr>
    <tr>
      <th>2016-12-15</th>
      <td>1.03657</td>
      <td>1.05324</td>
      <td>1.05386</td>
      <td>1.04118</td>
    </tr>
    <tr>
      <th>2016-12-16</th>
      <td>1.03999</td>
      <td>1.04118</td>
      <td>1.04734</td>
      <td>1.04483</td>
    </tr>
    <tr>
      <th>2016-12-19</th>
      <td>1.03916</td>
      <td>1.04369</td>
      <td>1.04786</td>
      <td>1.04005</td>
    </tr>
    <tr>
      <th>2016-12-20</th>
      <td>1.03514</td>
      <td>1.04003</td>
      <td>1.04173</td>
      <td>1.03869</td>
    </tr>
    <tr>
      <th>2016-12-21</th>
      <td>1.03816</td>
      <td>1.03869</td>
      <td>1.04502</td>
      <td>1.04228</td>
    </tr>
    <tr>
      <th>2016-12-22</th>
      <td>1.04213</td>
      <td>1.04214</td>
      <td>1.04986</td>
      <td>1.04355</td>
    </tr>
    <tr>
      <th>2016-12-23</th>
      <td>1.04256</td>
      <td>1.04340</td>
      <td>1.04682</td>
      <td>1.04526</td>
    </tr>
  </tbody>
</table>
<p>3191 rows × 4 columns</p>
</div>



## 最新100日、約3か月分のプロット


```python
dfl = dff[-100:]
dfl.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x191bb118470>




![png](read_hst_files/read_hst_9_1.png)


# ローソク足のプロット


```python
import matplotlib.finance as fi
```


```python
dfl
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>low</th>
      <th>open</th>
      <th>high</th>
      <th>close</th>
    </tr>
    <tr>
      <th>openTime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016-08-18</th>
      <td>1.12832</td>
      <td>1.12868</td>
      <td>1.13654</td>
      <td>1.13516</td>
    </tr>
    <tr>
      <th>2016-08-19</th>
      <td>1.13032</td>
      <td>1.13516</td>
      <td>1.13589</td>
      <td>1.13201</td>
    </tr>
    <tr>
      <th>2016-08-21</th>
      <td>1.13201</td>
      <td>1.13201</td>
      <td>1.13201</td>
      <td>1.13201</td>
    </tr>
    <tr>
      <th>2016-08-22</th>
      <td>1.12701</td>
      <td>1.13037</td>
      <td>1.13298</td>
      <td>1.13185</td>
    </tr>
    <tr>
      <th>2016-08-23</th>
      <td>1.13023</td>
      <td>1.13183</td>
      <td>1.13544</td>
      <td>1.13036</td>
    </tr>
    <tr>
      <th>2016-08-24</th>
      <td>1.12443</td>
      <td>1.13037</td>
      <td>1.13105</td>
      <td>1.12623</td>
    </tr>
    <tr>
      <th>2016-08-25</th>
      <td>1.12583</td>
      <td>1.12623</td>
      <td>1.12966</td>
      <td>1.12831</td>
    </tr>
    <tr>
      <th>2016-08-26</th>
      <td>1.11799</td>
      <td>1.12781</td>
      <td>1.13399</td>
      <td>1.11947</td>
    </tr>
    <tr>
      <th>2016-08-28</th>
      <td>1.11751</td>
      <td>1.11947</td>
      <td>1.11947</td>
      <td>1.11754</td>
    </tr>
    <tr>
      <th>2016-08-29</th>
      <td>1.11571</td>
      <td>1.11775</td>
      <td>1.12068</td>
      <td>1.11874</td>
    </tr>
    <tr>
      <th>2016-08-30</th>
      <td>1.11312</td>
      <td>1.11873</td>
      <td>1.11914</td>
      <td>1.11413</td>
    </tr>
    <tr>
      <th>2016-08-31</th>
      <td>1.11222</td>
      <td>1.11413</td>
      <td>1.11646</td>
      <td>1.11567</td>
    </tr>
    <tr>
      <th>2016-09-01</th>
      <td>1.11267</td>
      <td>1.11567</td>
      <td>1.12042</td>
      <td>1.11955</td>
    </tr>
    <tr>
      <th>2016-09-02</th>
      <td>1.11494</td>
      <td>1.11954</td>
      <td>1.12513</td>
      <td>1.11546</td>
    </tr>
    <tr>
      <th>2016-09-05</th>
      <td>1.11388</td>
      <td>1.11550</td>
      <td>1.11814</td>
      <td>1.11457</td>
    </tr>
    <tr>
      <th>2016-09-06</th>
      <td>1.11399</td>
      <td>1.11457</td>
      <td>1.12622</td>
      <td>1.12527</td>
    </tr>
    <tr>
      <th>2016-09-07</th>
      <td>1.12280</td>
      <td>1.12535</td>
      <td>1.12707</td>
      <td>1.12383</td>
    </tr>
    <tr>
      <th>2016-09-08</th>
      <td>1.12336</td>
      <td>1.12382</td>
      <td>1.13261</td>
      <td>1.12591</td>
    </tr>
    <tr>
      <th>2016-09-09</th>
      <td>1.11976</td>
      <td>1.12593</td>
      <td>1.12842</td>
      <td>1.12310</td>
    </tr>
    <tr>
      <th>2016-09-11</th>
      <td>1.12310</td>
      <td>1.12310</td>
      <td>1.12310</td>
      <td>1.12310</td>
    </tr>
    <tr>
      <th>2016-09-12</th>
      <td>1.12095</td>
      <td>1.12355</td>
      <td>1.12674</td>
      <td>1.12337</td>
    </tr>
    <tr>
      <th>2016-09-13</th>
      <td>1.12031</td>
      <td>1.12337</td>
      <td>1.12597</td>
      <td>1.12175</td>
    </tr>
    <tr>
      <th>2016-09-14</th>
      <td>1.12107</td>
      <td>1.12175</td>
      <td>1.12732</td>
      <td>1.12466</td>
    </tr>
    <tr>
      <th>2016-09-15</th>
      <td>1.12182</td>
      <td>1.12466</td>
      <td>1.12829</td>
      <td>1.12424</td>
    </tr>
    <tr>
      <th>2016-09-16</th>
      <td>1.11487</td>
      <td>1.12423</td>
      <td>1.12491</td>
      <td>1.11552</td>
    </tr>
    <tr>
      <th>2016-09-18</th>
      <td>1.11552</td>
      <td>1.11552</td>
      <td>1.11552</td>
      <td>1.11552</td>
    </tr>
    <tr>
      <th>2016-09-19</th>
      <td>1.11488</td>
      <td>1.11514</td>
      <td>1.11969</td>
      <td>1.11727</td>
    </tr>
    <tr>
      <th>2016-09-20</th>
      <td>1.11492</td>
      <td>1.11725</td>
      <td>1.12126</td>
      <td>1.11497</td>
    </tr>
    <tr>
      <th>2016-09-21</th>
      <td>1.11222</td>
      <td>1.11499</td>
      <td>1.11958</td>
      <td>1.11861</td>
    </tr>
    <tr>
      <th>2016-09-22</th>
      <td>1.11839</td>
      <td>1.11860</td>
      <td>1.12564</td>
      <td>1.12067</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-11-14</th>
      <td>1.07081</td>
      <td>1.08269</td>
      <td>1.08394</td>
      <td>1.07359</td>
    </tr>
    <tr>
      <th>2016-11-15</th>
      <td>1.07132</td>
      <td>1.07357</td>
      <td>1.08155</td>
      <td>1.07186</td>
    </tr>
    <tr>
      <th>2016-11-16</th>
      <td>1.06652</td>
      <td>1.07190</td>
      <td>1.07586</td>
      <td>1.06893</td>
    </tr>
    <tr>
      <th>2016-11-17</th>
      <td>1.06191</td>
      <td>1.06892</td>
      <td>1.07447</td>
      <td>1.06258</td>
    </tr>
    <tr>
      <th>2016-11-18</th>
      <td>1.05683</td>
      <td>1.06261</td>
      <td>1.06419</td>
      <td>1.05905</td>
    </tr>
    <tr>
      <th>2016-11-21</th>
      <td>1.05775</td>
      <td>1.05908</td>
      <td>1.06483</td>
      <td>1.06263</td>
    </tr>
    <tr>
      <th>2016-11-22</th>
      <td>1.05828</td>
      <td>1.06255</td>
      <td>1.06569</td>
      <td>1.06256</td>
    </tr>
    <tr>
      <th>2016-11-23</th>
      <td>1.05252</td>
      <td>1.06228</td>
      <td>1.06427</td>
      <td>1.05518</td>
    </tr>
    <tr>
      <th>2016-11-24</th>
      <td>1.05171</td>
      <td>1.05494</td>
      <td>1.05844</td>
      <td>1.05501</td>
    </tr>
    <tr>
      <th>2016-11-25</th>
      <td>1.05376</td>
      <td>1.05482</td>
      <td>1.06265</td>
      <td>1.05947</td>
    </tr>
    <tr>
      <th>2016-11-28</th>
      <td>1.05627</td>
      <td>1.06049</td>
      <td>1.06847</td>
      <td>1.06125</td>
    </tr>
    <tr>
      <th>2016-11-29</th>
      <td>1.05641</td>
      <td>1.06117</td>
      <td>1.06534</td>
      <td>1.06484</td>
    </tr>
    <tr>
      <th>2016-11-30</th>
      <td>1.05518</td>
      <td>1.06473</td>
      <td>1.06657</td>
      <td>1.05871</td>
    </tr>
    <tr>
      <th>2016-12-01</th>
      <td>1.05837</td>
      <td>1.05872</td>
      <td>1.06678</td>
      <td>1.06583</td>
    </tr>
    <tr>
      <th>2016-12-02</th>
      <td>1.06243</td>
      <td>1.06588</td>
      <td>1.06889</td>
      <td>1.06676</td>
    </tr>
    <tr>
      <th>2016-12-05</th>
      <td>1.05040</td>
      <td>1.06263</td>
      <td>1.07956</td>
      <td>1.07618</td>
    </tr>
    <tr>
      <th>2016-12-06</th>
      <td>1.06976</td>
      <td>1.07618</td>
      <td>1.07844</td>
      <td>1.07176</td>
    </tr>
    <tr>
      <th>2016-12-07</th>
      <td>1.07090</td>
      <td>1.07154</td>
      <td>1.07673</td>
      <td>1.07514</td>
    </tr>
    <tr>
      <th>2016-12-08</th>
      <td>1.05963</td>
      <td>1.07513</td>
      <td>1.08728</td>
      <td>1.06116</td>
    </tr>
    <tr>
      <th>2016-12-09</th>
      <td>1.05301</td>
      <td>1.06113</td>
      <td>1.06289</td>
      <td>1.05554</td>
    </tr>
    <tr>
      <th>2016-12-12</th>
      <td>1.05244</td>
      <td>1.05287</td>
      <td>1.06508</td>
      <td>1.06336</td>
    </tr>
    <tr>
      <th>2016-12-13</th>
      <td>1.06030</td>
      <td>1.06323</td>
      <td>1.06664</td>
      <td>1.06238</td>
    </tr>
    <tr>
      <th>2016-12-14</th>
      <td>1.04954</td>
      <td>1.06238</td>
      <td>1.06693</td>
      <td>1.05328</td>
    </tr>
    <tr>
      <th>2016-12-15</th>
      <td>1.03657</td>
      <td>1.05324</td>
      <td>1.05386</td>
      <td>1.04118</td>
    </tr>
    <tr>
      <th>2016-12-16</th>
      <td>1.03999</td>
      <td>1.04118</td>
      <td>1.04734</td>
      <td>1.04483</td>
    </tr>
    <tr>
      <th>2016-12-19</th>
      <td>1.03916</td>
      <td>1.04369</td>
      <td>1.04786</td>
      <td>1.04005</td>
    </tr>
    <tr>
      <th>2016-12-20</th>
      <td>1.03514</td>
      <td>1.04003</td>
      <td>1.04173</td>
      <td>1.03869</td>
    </tr>
    <tr>
      <th>2016-12-21</th>
      <td>1.03816</td>
      <td>1.03869</td>
      <td>1.04502</td>
      <td>1.04228</td>
    </tr>
    <tr>
      <th>2016-12-22</th>
      <td>1.04213</td>
      <td>1.04214</td>
      <td>1.04986</td>
      <td>1.04355</td>
    </tr>
    <tr>
      <th>2016-12-23</th>
      <td>1.04256</td>
      <td>1.04340</td>
      <td>1.04682</td>
      <td>1.04526</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
</div>



各列をnp.arrayで取り出すには、ドットで列名綴って、valuesメソッドで取り出す。

ixなどで列番号を使って取り出す時と比べて、列の入れ替え問題が解消される。


```python
dfl.open.values
```




    array([ 1.12868,  1.13516,  1.13201,  1.13037,  1.13183,  1.13037,
            1.12623,  1.12781,  1.11947,  1.11775,  1.11873,  1.11413,
            1.11567,  1.11954,  1.1155 ,  1.11457,  1.12535,  1.12382,
            1.12593,  1.1231 ,  1.12355,  1.12337,  1.12175,  1.12466,
            1.12423,  1.11552,  1.11514,  1.11725,  1.11499,  1.1186 ,
            1.12068,  1.12265,  1.1228 ,  1.12527,  1.12133,  1.1216 ,
            1.12209,  1.12396,  1.12254,  1.12093,  1.12031,  1.1203 ,
            1.11486,  1.11753,  1.11366,  1.10523,  1.1005 ,  1.10548,
            1.09671,  1.09975,  1.09785,  1.09723,  1.09284,  1.088  ,
            1.0876 ,  1.08799,  1.08862,  1.09068,  1.08946,  1.09893,
            1.0979 ,  1.10538,  1.10959,  1.11035,  1.1056 ,  1.10372,
            1.1024 ,  1.0907 ,  1.08897,  1.08301,  1.08269,  1.07357,
            1.0719 ,  1.06892,  1.06261,  1.05908,  1.06255,  1.06228,
            1.05494,  1.05482,  1.06049,  1.06117,  1.06473,  1.05872,
            1.06588,  1.06263,  1.07618,  1.07154,  1.07513,  1.06113,
            1.05287,  1.06323,  1.06238,  1.05324,  1.04118,  1.04369,
            1.04003,  1.03869,  1.04214,  1.0434 ])




```python
def mydate(x,pos):
    try:
        return xdate[int(x)]
    except IndexError:
        return ''


def candlechart(ohlc, width=0.8):
    """入力されたデータフレームに対してローソク足チャートを返す
        引数:
            * ohlc: 
                *データフレーム
                * 列名に'open'", 'close', 'low', 'high'を入れること
                * 順不同"
            * widrh: ローソクの線幅 
        戻り値: ax: subplot"""
    fig, ax = plt.subplots()
    # ローソク足
    fi.candlestick2_ohlc(ax, opens=ohlc.open.values, closes=ohlc.close.values,
                         lows=ohlc.low.values, highs=ohlc.high.values,
                         width=width, colorup='r', colordown='b')
    
    # x軸を時間にする
    xdate = dfl.index
    ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))

    fig.autofmt_xdate()
    fig.tight_layout()

    return fig, ax
```


```python
candlechart(dfl)
```




    (<matplotlib.figure.Figure at 0x191cc5bd208>,
     <matplotlib.axes._subplots.AxesSubplot at 0x191cb3afcf8>)




![png](read_hst_files/read_hst_16_1.png)



```python

```