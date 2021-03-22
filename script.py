# Correlation plot
houses = pd.read_csv('data/melb_data.csv')

## Calculate pairwise-correlation
matrix = houses.corr()

## Create a mask
mask = np.triu(np.ones_like(matrix, dtype=bool))

## Create a custom diverging palette
cmap = sns.diverging_palette(250, 15, s=75, l=40,
                             n=9, center="light", as_cmap=True)

plt.figure(figsize=(16, 12))

sns.heatmap(matrix, mask=mask, center=0, annot=True,
             fmt='.2f', square=True, cmap=cmap)

plt.show();

# Include Missing Values in value_counts

houses.CouncilArea.value_counts(dropna=False, normalize=True).head()
## proportion of missing values across all columns,

missing_props = houses.isna().sum() / len(houses)
missing_props[missing_props > 0].sort_values(ascending=False)

# Using Pandas DataFrame Styler
diamonds = sns.load_dataset('diamonds')

pd.crosstab(diamonds.cut, diamonds.clarity).\
                style.background_gradient(cmap='rocket_r')

# Finding the average price of each diamond cut and clarity combination in crosstab
pd.crosstab(diamonds.cut, diamonds.clarity,
          aggfunc=np.mean, values=diamonds.price).\
          style.background_gradient(cmap='flare')
  
  
agg_prices = pd.crosstab(diamonds.cut, diamonds.clarity,
                         aggfunc=np.mean, values=diamonds.price).\
                         style.background_gradient(cmap='flare')

agg_prices.format('{:.2f}')

# Configuring Global Plot Settings With Matplotlib

from matplotlib import rcParams

rcParams

## set a fixed figure size, tick label font size, and a few others:

## Remove top and right spines
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

## Set fixed figure size
rcParams['figure.figsize'] = [12, 9]

## Set dots per inch to 300, very high quality images
rcParams['figure.dpi'] = 300

## Enable autolayout
rcParams['figure.autolayout'] = True

## Set global fontsize
rcParams['font.style'] = 16

## Fontsize of ticklabels
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10

# Configuring Global Settings of Pandas

pd.set_option('display.max_columns', None)

## revert back to the default setting with
pd.reset_option('display.max_columns')

## Plotly is becoming vastly popular, so it would be nice to set it as default plotting backed for pandas. 
## By doing so, you will get interactive plotly diagrams whenever you call .plot on pandas DataFrames
pd.set_option('plotting.backend', 'plotly')


## To apply certain code block
df = pd.DataFrame(np.random.randn(5, 5))
pd.reset_option('display.max_rows')
with pd.option_context('float_format', '{:f}'.format):
        df.describe()
