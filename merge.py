import pandas as pd
import sys
import numpy as np
from datetime import datetime
from os import path

merge_list = ['AMD','ADBE','ABNB','ALGN','AMZN','AMGN','AEP','ADI','ANSS','AAPL','AMAT','ASML','TEAM','ADSK','ATVI','ADP','AZN','AVGO','BIDU','BIIB','AMRN','BKNG','CDNS','CHTR','CPRT','CRWD','CTAS','CSCO','CMCSA','COST','CSX','CTSH','DDOG','DOCU','DXCM','DLTR','EA','EBAY','EXC','FAST','FB','FISV','FTNT','GILD','GOOG','GOOGL','HON','ILMN','INTC','INTU','ISRG','MRVL','IDXX','JD','KDP','KLAC','KHC','LRCX','LCID','LULU','MELI','MAR','MTCH','MCHP','MDLZ','MRNA','MNST','MSFT','MU','NFLX','NTES','NVDA','NXPI','OKTA','ODFL','ORLY','PCAR','PANW','PAYX','PDD','PYPL','PEP','QCOM','REGN','ROST','SIRI','SGEN','SPLK','SWKS','SBUX','SNPS','TSLA','TXN','TMUS','VRSN','VRSK','VRTX','WBA','WDAY','XEL','ZM','ZS']

posts_dir = '../posts/'
stocks_dir = '../hist/'

all_stocks = pd.DataFrame(columns=['Date','Open','High','Low','Close','Adj Close','Volume','Stock'])
for s in merge_list:
    if path.isfile('{0}{1}.csv'.format(stocks_dir, s)):
        stock_df = pd.read_csv('{0}{1}.csv'.format(stocks_dir, s))
        stock_df['Stock'] = [s for _ in range(len(stock_df.index))]
        all_stocks = all_stocks.append(stock_df, ignore_index=True)
        del stock_df

all_stocks = all_stocks.sort_values('Date')
all_stocks.to_csv('../merged_stocks_NDX100.csv', index=False)
del all_stocks
    
all_posts = pd.DataFrame(columns=['title','score','num_comments','body','created','Stock', 'Date'])
for s in merge_list:
    if path.isfile('{0}{1}_posts.csv'.format(posts_dir, s)):
        stock_df = pd.read_csv('{0}{1}_posts.csv'.format(posts_dir, s))
        stock_df = stock_df.drop(stock_df.columns[0], axis=1)
        stock_df['Stock'] = [s for _ in range(len(stock_df.index))]
        stock_df['Date'] = [datetime.fromtimestamp(ts) for ts in list(stock_df['created'])]
        all_posts = all_posts.append(stock_df, ignore_index=True)
        del stock_df

all_posts = all_posts.sort_values('Date')
all_posts.to_csv('../merged_posts_NDX100.csv', index=False)
del all_posts
                         