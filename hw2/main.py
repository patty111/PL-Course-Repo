import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import fontManager
import mplcursors
import seaborn as sns

sns.set_theme()

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

# read in data
data = pd.read_csv('tpMetro.csv', encoding='big5')  # using big5 for traditional Chinese

# dop odd number rows
data = data[data.index % 2 == 0]

data['年別'] = data['年別'].str.replace('年', '').astype(int)

df = pd.read_csv("tpMetro.csv", encoding='big5')


# Taipei MRT Historical assenger Traffic Statistics
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(data['年別'], data['總計人次'], marker='o', linestyle='-')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Passenger Traffic')
axs[0, 0].grid(True)
axs[0, 0].set_title('Taipei MRT Historical assenger Traffic Statistics')


# Taipei MRT Historical Passenger Traffic Percentage Change
percentage_change = data['總計人次'].pct_change()*100
axs[0, 1].plot(data['年別'], percentage_change, marker='o', linestyle='-')
axs[0, 1].set_xlabel('Year')
axs[0, 1].set_ylabel('Percentage Change in Passenger Traffic(%)')
axs[0, 1].set_title('Taipei MRT Historical Passenger Traffic Percentage Change')
axs[0, 1].grid(True)


# 
df = pd.read_csv("tpMetro.csv", encoding='big5')

# merge 進站&出站together, consider total traffic only
df_in = df[df['進站/出站人次'] == '進站人次']
df_out = df[df['進站/出站人次'] == '出站人次']

# drop unused columns
df_in = df_in.drop(columns=['進站/出站人次', '總計人次'])
df_out = df_out.drop(columns=['進站/出站人次', '總計人次'])

df_in.columns = df_in.columns.str.replace('人次', '')
df_out.columns = df_out.columns.str.replace('人次', '')

df_total = df_in.set_index('年別').add(df_out.set_index('年別'), fill_value=0).reset_index()

# 人流最多: 108年
traffic_count_in_108 = df_total.loc[df_total['年別'] == '108年']

tmp = traffic_count_in_108.drop(columns=['年別'])

# fill Nan to 0
tmp.fillna(0, inplace=True)
stations = tmp.columns

data_to_1D = tmp.iloc[0]

# plotting
axs[1,0].pie(data_to_1D, labels=stations, autopct=lambda p: '{:.0f}%'.format(p) if p > 3 else '', startangle=90, textprops={'fontsize': 6})
axs[1,0].set_title('108 年北捷各捷運站人流比例圖')


# 各捷運站108年度總人流差異直條圖
# 46: 進站, 47: 出站
data = pd.read_csv('tpMetro.csv', encoding='big5')  # using big5 for traditional Chinese
tmp = data.loc[data['年別'] == '108年'].drop(columns=['年別', '進站/出站人次', '總計人次'])

# replace Nan to 0 and convert type from str to int
tmp = tmp.fillna(0).astype(int)
diff = tmp.diff().iloc[1].astype(int)

x = stations.tolist()

# plotting
bar = axs[1, 1].bar(x, diff)
axs[1, 1].set_xticks(range(len(x)))
axs[1, 1].set_xticklabels(axs[1, 1].get_xticks(), rotation=90, fontsize=6)
# Draw a horizontal line at 0
axs[1, 1].axhline(0, color='black')

# Add labels and title
axs[1, 1].set_xlabel('Station')
axs[1, 1].set_ylabel('Difference')
axs[1, 1].set_title('各捷運站108年度總人流差異直條圖')

# Display the chart
plt.tight_layout()
cursor = mplcursors.cursor()
cursor.connect("add", lambda sel: sel.annotation.set_text('Index: {}\nValue: {}'.format(sel.target[0], sel.target[1])))
plt.show()