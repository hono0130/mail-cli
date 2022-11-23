import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

def bar_and_plot(title, X, y_bar, y_plot, y_lim):
    plt.rcParams['font.size'] = 18
    fig, ax1 = plt.subplots(1,1,figsize=(10,8))
    ax2 = ax1.twinx()

    x = X.copy()

    zero_index = []
    index = 0

    for ratio in y_plot:
        if ratio == 0:
            zero_index.append(index)
        index += 1

    count = 0
    if len(zero_index) != []:
        for i in zero_index:
            x.pop(i - count)
            y_bar.pop(i - count)
            y_plot.pop(i - count)
            count += 1  

    # if "H3" in title:
    #     x.pop(-4)
    #     y_bar.pop(-4)
    #     y_plot.pop(-4)
    #     x.pop(-4)
    #     y_bar.pop(-4)
    #     y_plot.pop(-4)

    ax1.bar(x, y_bar, color="lightblue")
    ax2.plot(y_plot, color="orange", marker=".")
    ax2.set_ylim(0,y_lim)
    ax1.set_title(title[-7:], fontsize=25)
    ax1.set_xticklabels(x,fontsize=18, rotation=45)

    for i in range(len(y_plot)):
        ax2.text(x[i], y_plot[i], y_plot[i], fontsize=15)
    
    plt.savefig(f"{title}.png")

def double_bar_and_plot(title, x, y_bar_left, y_bar_right, y_plot_left, y_plot_right):
    width = 0.4

    fig, ax1 = plt.subplots(1,1,figsize=(10,8))
    ax2 = ax1.twinx()
    moshi1 = title.split("/")[2].split("_")[1]
    moshi2 = title.split("/")[2].split("_")[2]

    

    ax1.bar(x, y_bar_right, color="lightblue", align="edge", width=width, label=moshi2)
    ax1.bar(x, y_bar_left, color="orange", align="edge", width=-width, label=moshi1)
    
    ax1.set_xticks(x)
    
    
    ax2.plot(y_plot_left, color="blue", marker=".", label=moshi1)
    ax2.plot(y_plot_right, color="red", marker=".", label=moshi2)
    ax2.set_ylim(0,100)
    ax1.set_title(title)
    ax1.set_xticklabels(x,fontsize=18, rotation=45)


    ax1.legend(fontsize=12)

    ax2.legend(fontsize=12)

    
    plt.savefig(f"{title}.png")

def pile_up_bar(df: pd.DataFrame):
    """

    Args:
        df (pd.DataFrame): columnsがx軸
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    for i in range(len(df)):
        ax.bar(df.columns, df.iloc[i], bottom=df.iloc[:i].sum())
    ax.legend(df.index)
    plt.show()

def many_bar(df: pd.DataFrame):
    plt.rcParams['font.size'] = 15
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    df.plot(ax=ax, kind="bar", rot=0)
    ax.set_xticklabels(df.index, fontsize=18, rotation=45)
    ax.legend(fontsize=12)