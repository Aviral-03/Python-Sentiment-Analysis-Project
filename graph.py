"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file has been produced to visualise the processed data by producing the final graph and
is solely for the private use of project members. All forms of distribution of this code, whether
as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 by Harshkumar Patel, Darpan Mishra, Janel Gilani, Aviral Bhardwaj.
"""
import csv
import plotly.graph_objects as px
import pandas as pd
from plotly.subplots import make_subplots


def processing_data(primary_filename: str) -> list[list]:
    """Processing Data from CSV and returning axes values List"""
    # ACCUMULATOR activities_so_far: Listed Activities
    activities_so_far = []
    # ACCUMULATOR before_covid_enjoyscore: Activity's Enjoyability Score before COVID
    before_covid_enjoyscore = []
    # ACCUMULATOR after_covid_enjoyscore: Activity's Enjoyability Score after COVID
    after_covid_enjoyscore = []
    # ACCUMULATOR before_covid_timespent: Time Spent Daily Before the Pandemic (Minutes)
    before_covid_timespent = []
    # ACCUMULATOR after_covid_timespent: Time Spent Daily After the Pandemic (Minutes)
    after_covid_timespent = []

    with open(primary_filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            assert len(row) == 5, 'Expected every row to contain 5 elements.'
            if len(activities_so_far) < 6:
                activity = str(row[0])
                benjoy = float(row[1])
                aenjoy = float(row[2])
                btime_spent = float(row[3])
                atime_dpent = float(row[4])
                activities_so_far = activities_so_far + [activity]
                before_covid_enjoyscore = before_covid_enjoyscore + [benjoy]
                after_covid_enjoyscore = after_covid_enjoyscore + [aenjoy]
                before_covid_timespent = before_covid_timespent + [btime_spent]
                after_covid_timespent = after_covid_timespent + [atime_dpent]

    return [activities_so_far, before_covid_enjoyscore, after_covid_enjoyscore,
            before_covid_timespent, after_covid_timespent]


def plotting_data(primary_filename: str, secondary_filename: str) -> None:
    """Returning plotted Processed Data Points on Plotly"""
    final_list = processing_data(primary_filename)

    # Sub-polts
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Before the onset of "
                                                        "COVID-19 pandemic", "After the onset of "
                                                                             "COVID-19 pandemic"))
    # Bar 1
    df = pd.read_csv(secondary_filename)
    fig.add_trace(px.Bar(
        x=df['Activity'], y=df['Before_AverageDailyTime'], width=[0.1] * len(final_list[4]),
        marker=dict(color='rgb(120, 199, 255)'),
        name="Average Daily Time<br>"
             "before the pandemic<br>"
             "from Secondary Dat"
             "a"), row=1, col=1
    )

    colour_so_far = []
    for element in final_list[1]:
        if element > 0:
            colour_so_far.append('rgb(44, 160, 101)')
        else:
            colour_so_far.append('rgb(202, 0, 42)')

    # Bubble 1
    fig.add_trace(px.Scatter(
        x=final_list[0], y=[abs(x) for x in final_list[3]],
        mode='markers',
        name="<b>Primary Data: <br> Positive enjoyability, <br> bigger circle means <br> "
             "more enjoyable <br> higher position means <br> more time spent daily <br> "
             "lower position means <br> less time spent daily<b>",
        marker=dict(
            color=colour_so_far,
            opacity=[0.5],
            size=[abs(x) * 175 for x in final_list[1]],
        )
    ), row=1, col=1)

    # Bar 2
    fig.add_trace(px.Bar(
        x=df['Activity'], y=df['After_AverageDailyTime'], width=[0.1] * len(final_list[4]),
        marker=dict(color='rgb(158, 115, 250)'),
        name="Average Daily Time<br>"
             "during the pandemic<br>"
             "from Secondary Dat"
             "a"), row=1, col=2
    )

    colour2_so_far = []
    for element in final_list[2]:
        if element > 0:
            colour2_so_far.append('rgb(44, 160, 101)')
        else:
            colour2_so_far.append('rgb(202, 0, 42)')

    # Bubble 2
    fig.add_trace(px.Scatter(
        x=final_list[0], y=[abs(x) for x in final_list[4]],
        mode='markers',
        name="<b> Primary Data: <br> Negative enjoyability, <br> bigger circle means <br>"
             "less enjoyable, <br> higher position means <br> more time spent daily, <br> "
             "lower position means <br> less time spent daily<b>",
        marker=dict(
            color=colour2_so_far,
            opacity=[0.5],
            size=[abs(x) * 175 for x in final_list[2]],
        ),
    ), row=1, col=2)

    fig.update_layout(title_font_family="Bahnschrift", title_font_size=25,
                      title={
                          'text': "The Impact of COVID-19 on Popularity and Enjoyability of "
                                  "Individuals' Hobbies",
                          'y': 0.95,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'})

    fig.update_xaxes(title_text='Name of the Activity')
    fig.update_yaxes(title_text='Average time spent on the activity (in minutes)', range=[-25, 600])

    # Show the figure in the browser
    fig.show()
    # Is the above not working for you? Comment it out, and uncomment the following:
    # fig.write_html('final_visualization.html')
    # You will need to manually open the final_visualization.html file created above.


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'plotly.subplots', 'plotly.graph_objects', 'csv'],
        'allowed-io': ['processing_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
