import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Clean data
df = df.drop(df[(df.value<df.value.quantile(0.025)) | (df.value>df.value.quantile(0.975))].index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.plot(df);

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
   df_bap = df.copy()
   df_bap["Years"] = df_bap.index.year
   df_bap["Months"] = df_bap.index.month_name()
   df_bap = pd.DataFrame(df_bap.groupby(["Years", "Months"], sort=False)["value"].mean().astype(int))
   df_bap = df_bap.reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.set_title("Months")

    sns.barplot(data=df_bap, x="Years", y="value", hue='Months');

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(24, 6), dpi=100)
    
    # Yearly boxplot
    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    
    # Monthly boxplot
    sns.boxplot(data=df_box, x="month", y="value", ax=ax[1])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views");

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
