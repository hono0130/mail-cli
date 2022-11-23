import pandas as pd
import numpy as np

from module.glob_date import get_sent_date_in_n
from module.preprocess import count, high_prospect
from module.glob_file import get_sent_file, get_click_file, get_open_file
from module.visualize import bar_and_plot

def usual_open_ratio(n, high_prospective: bool):

    date_lst = get_sent_date_in_n(n)

    x_H3 = []
    x_H2 = []
    x_H1 = []
    y_bar_H3 = []
    y_plot_H3 = []
    y_bar_H2 = []
    y_plot_H2 = []
    y_bar_H1 = []
    y_plot_H1 = []

    for date in date_lst:
        if high_prospective: 
            open_dict = count(high_prospect(get_open_file(date)))
            sent_dict = count(high_prospect(get_sent_file(date)))
        else:
            open_dict = count(get_open_file(date))
            sent_dict = count(get_sent_file(date))
        if open_dict["H3"] != 0:
            if date == "221101" or date == "221102":
                continue
            else:
                x_H3.append(date)
                y_bar_H3.append(open_dict["H3"])
                y_plot_H3.append(round(open_dict["H3"] / sent_dict["H3"] * 100, 1))

        if open_dict["H2"] != 0:
            x_H2.append(date)
            y_bar_H2.append(open_dict["H2"])
            y_plot_H2.append(round(open_dict["H2"] / sent_dict["H2"] * 100, 1))

        if open_dict["H1"] != 0:
            x_H1.append(date)
            y_bar_H1.append(open_dict["H1"])       
            y_plot_H1.append(round(open_dict["H1"] / sent_dict["H1"] * 100, 1))

        if high_prospective: 
            bar_and_plot(f"open/high_prospect_compare_in_n/high_prospect_H3_mail", x_H3, y_bar_H3, y_plot_H3, 100)
            bar_and_plot(f"open/high_prospect_compare_in_n/high_prospect_H2_mail", x_H2, y_bar_H2, y_plot_H2, 100)
            bar_and_plot(f"open/high_prospect_compare_in_n/high_prospect_H1_mail", x_H1, y_bar_H1, y_plot_H1, 100)
        else: 
            bar_and_plot(f"open/compare_in_n/H3_mail", x_H3, y_bar_H3, y_plot_H3, 100)
            bar_and_plot(f"open/compare_in_n/H2_mail", x_H2, y_bar_H2, y_plot_H2, 100)
            bar_and_plot(f"open/compare_in_n/H1_mail", x_H1, y_bar_H1, y_plot_H1, 100)


def usual_click_ratio(n, high_prospective: bool):

    date_lst = get_sent_date_in_n(n)

    x_H3 = []
    x_H2 = []
    x_H1 = []
    y_bar_H3 = []
    y_plot_H3 = []
    y_bar_H2 = []
    y_plot_H2 = []
    y_bar_H1 = []
    y_plot_H1 = []

    for date in date_lst: 
        if high_prospective:
            click_dict = count(high_prospect(get_click_file(date)))
            open_dict = count(high_prospect(get_open_file(date)))
        else:
            click_dict = count(get_click_file(date))
            open_dict = count(get_open_file(date))
        if click_dict["H3"] != 0:
            if date == "221101" or date == "221102":
                continue
            else:
                x_H3.append(date)
                y_bar_H3.append(click_dict["H3"])
                y_plot_H3.append(round(click_dict["H3"] / open_dict["H3"] * 100, 1))

        if click_dict["H2"] != 0:
            x_H2.append(date)
            y_bar_H2.append(click_dict["H2"])
            y_plot_H2.append(round(click_dict["H2"] / open_dict["H2"] * 100, 1))

        if click_dict["H1"] != 0:
            x_H1.append(date)
            y_bar_H1.append(click_dict["H1"])       
            y_plot_H1.append(round(click_dict["H1"] / open_dict["H1"] * 100, 1))

        if high_prospective:
            bar_and_plot(f"click/high_prospect_compare_in_n/high_prospect_H3_mail", x_H3, y_bar_H3, y_plot_H3, 30)
            bar_and_plot(f"click/high_prospect_compare_in_n/high_prospect_H2_mail", x_H2, y_bar_H2, y_plot_H2, 30)
            bar_and_plot(f"click/high_prospect_compare_in_n/high_prospect_H1_mail", x_H1, y_bar_H1, y_plot_H1, 30)
        else:
            bar_and_plot(f"click/compare_in_n/H3_mail", x_H3, y_bar_H3, y_plot_H3, 30)
            bar_and_plot(f"click/compare_in_n/H2_mail", x_H2, y_bar_H2, y_plot_H2, 30)
            bar_and_plot(f"click/compare_in_n/H1_mail", x_H1, y_bar_H1, y_plot_H1, 30)
