"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file has been produced to generate an interactive survey for primary data collection and
is solely for the private use of project members. All forms of distribution of this code, whether
as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 by Harshkumar Patel, Darpan Mishra, Janel Gilani, Aviral Bhardwaj.
"""
import tkinter
import vader
from graph import plotting_data


def show_data(screen: tkinter.Tk, storage: vader.Vader,
              word_responses: list[tkinter.Entry], time_responses: list[tkinter.Entry]) -> None:
    """Take the input data, perform the necessary computation through Vader and produce graphs"""
    # Add all the survey data to its respective dictionary in Vader
    for response in time_responses:
        # Check if there are any faulty inputs in the survey and stop the code accordingly
        if not response.get().isdigit():
            screen.destroy()
            raise NotIntegerError
    response_travel = (word_responses[0].get(), word_responses[1].get())
    time_travel = (int(time_responses[0].get()), int(time_responses[1].get()))
    storage.add_category('Travelling and Transport', response_travel, time_travel)
    response_home = (word_responses[2].get(), word_responses[3].get())
    time_home = (int(time_responses[2].get()), int(time_responses[3].get()))
    storage.add_category('Working from Home', response_home, time_home)
    response_fit = (word_responses[4].get(), word_responses[5].get())
    time_fit = (int(time_responses[4].get()), int(time_responses[5].get()))
    storage.add_category('Staying Fit', response_fit, time_fit)
    response_garden = (word_responses[6].get(), word_responses[7].get())
    time_garden = (int(time_responses[6].get()), int(time_responses[7].get()))
    storage.add_category('Gardening and DIY', response_garden, time_garden)
    response_rest = (word_responses[8].get(), word_responses[9].get())
    time_rest = (int(time_responses[8].get()), int(time_responses[9].get()))
    storage.add_category('Sleep and Rest', response_rest, time_rest)
    response_fun = (word_responses[10].get(), word_responses[11].get())
    time_fun = (int(time_responses[10].get()), int(time_responses[11].get()))
    storage.add_category('Entertainment and Socializing', response_fun, time_fun)
    storage.increase_participant_num()

    # Add the survey response without any changes to the raw data file
    storage.add_raw()
    # Close the survey window after the survey has been completed
    screen.destroy()

    # Compute the data within the Vader class and output the data through a graph
    storage.compute()
    plotting_data('processed_data.csv', 'secondary_data.csv')


def display_survey() -> None:
    """Display the survey for the user to take.

    The submit button should close the survey
    """
    # create the screen and set its properties
    screen = tkinter.Tk()
    screen.geometry("800x1200")
    screen.title("CSC110 Project Survey")
    title_submit = tkinter.Frame(screen)
    title_submit.pack()
    storage = vader.Vader()

    # title and submit button at the top of the form
    heading = tkinter.Label(title_submit, text="Primary Data Collection Survey", height="2",
                            font=("Bahnschrift", 17))
    submit = tkinter.Button(title_submit, text="Submit", bg="White", fg="Black",
                            command=lambda: show_data(screen, storage, word_responses,
                                                      time_responses))
    heading.pack(side=tkinter.LEFT)
    submit.pack(side=tkinter.RIGHT)

    # travelling and transportation section questions in survey
    travel = tkinter.Frame(screen)
    travel.pack()
    time_pre_travel = tkinter.StringVar(travel, 'Minutes Spent Daily (pre-COVID)')
    time_post_travel = tkinter.StringVar(travel, 'Minutes Spent Daily (post-COVID)')
    pre_travel = tkinter.StringVar(travel, 'Describe your experience while partaking in '
                                           'travelling/transport before COVID-19')
    post_travel = tkinter.StringVar(travel, 'Describe your experience while partaking in '
                                            'travelling/transport during COVID-19')
    travel_activity = tkinter.Label(travel, text="Travelling/Transport", font=("Bahnschrift", 15))
    pre_traveling = tkinter.Entry(travel, textvariable=time_pre_travel, width=36)
    post_traveling = tkinter.Entry(travel, textvariable=time_post_travel, width=36)
    pre_travel_response = tkinter.Entry(textvariable=pre_travel, width=73)
    post_travel_response = tkinter.Entry(textvariable=post_travel, width=73)
    travel_activity.pack()
    pre_traveling.pack(side=tkinter.LEFT)
    post_traveling.pack(side=tkinter.RIGHT)
    pre_travel_response.pack()
    post_travel_response.pack()

    # work from home section questions in survey
    home = tkinter.Frame(screen)
    home.pack()
    time_pre_home = tkinter.StringVar(home, 'Minutes Spent Daily (pre-COVID)')
    time_post_home = tkinter.StringVar(home, 'Minutes Spent Daily (post-COVID)')
    pre_home = tkinter.StringVar(home, 'Describe your experience while partaking in working'
                                       ' from home before COVID-19')
    post_home = tkinter.StringVar(home, 'Describe your experience while partaking in working'
                                        ' from home during COVID-19')
    home_activity = tkinter.Label(home, text="Working from Home", font=("Bahnschrift", 15))
    pre_work_home = tkinter.Entry(home, textvariable=time_pre_home, width=36)
    post_work_home = tkinter.Entry(home, textvariable=time_post_home, width=36)
    pre_home_response = tkinter.Entry(textvariable=pre_home, width=73)
    post_home_response = tkinter.Entry(textvariable=post_home, width=73)
    home_activity.pack()
    pre_work_home.pack(side=tkinter.LEFT)
    post_work_home.pack(side=tkinter.RIGHT)
    pre_home_response.pack()
    post_home_response.pack()

    # staying fit section questions in survey
    fit = tkinter.Frame(screen)
    fit.pack()
    time_pre_fit = tkinter.StringVar(fit, 'Minutes Spent Daily (pre-COVID)')
    time_post_fit = tkinter.StringVar(fit, 'Minutes Spent Daily (post-COVID)')
    pre_fit = tkinter.StringVar(fit, 'Describe your experience while partaking in physical'
                                     ' activities before COVID-19')
    post_fit = tkinter.StringVar(fit, 'Describe your experience while partaking in physical'
                                      ' activities during COVID-19')
    fit_activity = tkinter.Label(fit, text="Staying Fit", font=("Bahnschrift", 15))
    pre_keep_fit = tkinter.Entry(fit, textvariable=time_pre_fit, width=36)
    post_keep_fit = tkinter.Entry(fit, textvariable=time_post_fit, width=36)
    pre_fit_response = tkinter.Entry(textvariable=pre_fit, width=73)
    post_fit_response = tkinter.Entry(textvariable=post_fit, width=73)
    fit_activity.pack()
    pre_keep_fit.pack(side=tkinter.LEFT)
    post_keep_fit.pack(side=tkinter.RIGHT)
    pre_fit_response.pack()
    post_fit_response.pack()

    # gardening and DIY section questions in survey
    garden = tkinter.Frame(screen)
    garden.pack()
    time_pre_garden = tkinter.StringVar(garden, 'Minutes Spent Daily (pre-COVID)')
    time_post_garden = tkinter.StringVar(garden, 'Minutes Spent Daily (post-COVID)')
    pre_garden = tkinter.StringVar(garden, 'Describe your experience while partaking in'
                                           ' gardening/DIY before COVID-19')
    post_garden = tkinter.StringVar(garden, 'Describe your experience while partaking in'
                                            ' gardening/DIY during COVID-19')
    garden_activity = tkinter.Label(garden, text="Gardening/DIY", font=("Bahnschrift", 15))
    pre_gardening = tkinter.Entry(garden, textvariable=time_pre_garden, width=36)
    post_gardening = tkinter.Entry(garden, textvariable=time_post_garden, width=36)
    pre_garden_response = tkinter.Entry(textvariable=pre_garden, width=73)
    post_garden_response = tkinter.Entry(textvariable=post_garden, width=73)
    garden_activity.pack()
    pre_gardening.pack(side=tkinter.LEFT)
    post_gardening.pack(side=tkinter.RIGHT)
    pre_garden_response.pack()
    post_garden_response.pack()

    # rest and sleep section questions in survey
    rest = tkinter.Frame(screen)
    rest.pack()
    time_pre_rest = tkinter.StringVar(rest, 'Minutes Spent Daily (pre-COVID)')
    time_post_rest = tkinter.StringVar(rest, 'Minutes Spent Daily (post-COVID)')
    pre_rest = tkinter.StringVar(rest, 'Describe your experience while partaking in'
                                       ' sleeping/resting before COVID-19')
    post_rest = tkinter.StringVar(rest, 'Describe your experience while partaking in'
                                        ' sleeping/resting during COVID-19')
    rest_activity = tkinter.Label(rest, text="Sleep/Rest", font=("Bahnschrift", 17))
    pre_sleep_rest = tkinter.Entry(rest, textvariable=time_pre_rest, width=36)
    post_sleep_rest = tkinter.Entry(rest, textvariable=time_post_rest, width=36)
    pre_rest_response = tkinter.Entry(textvariable=pre_rest, width=73)
    post_rest_response = tkinter.Entry(textvariable=post_rest, width=73)
    rest_activity.pack()
    pre_sleep_rest.pack(side=tkinter.LEFT)
    post_sleep_rest.pack(side=tkinter.RIGHT)
    pre_rest_response.pack()
    post_rest_response.pack()

    # work from home section questions in survey
    fun = tkinter.Frame(screen)
    fun.pack()
    time_pre_fun = tkinter.StringVar(fun, 'Minutes Spent Daily (pre-COVID)')
    time_post_fun = tkinter.StringVar(fun, 'Minutes Spent Daily (post-COVID)')
    pre_fun = tkinter.StringVar(fun, 'Your experience while partaking in '
                                     'entertainment/socializing before COVID-19')
    post_fun = tkinter.StringVar(fun, 'Your experience while partaking in '
                                      'entertainment/socializing during COVID-19')
    fun_activity = tkinter.Label(fun, text="Entertainment/Socializing", font=("Bahnschrift", 15))
    pre_social_fun = tkinter.Entry(fun, textvariable=time_pre_fun, width=36)
    post_social_fun = tkinter.Entry(fun, textvariable=time_post_fun, width=36)
    pre_fun_response = tkinter.Entry(textvariable=pre_fun, width=73)
    post_fun_response = tkinter.Entry(textvariable=post_fun, width=73)
    fun_activity.pack()
    pre_social_fun.pack(side=tkinter.LEFT)
    post_social_fun.pack(side=tkinter.RIGHT)
    pre_fun_response.pack()
    post_fun_response.pack()

    # grouping the input data together by the experience and how much time spent
    word_responses = [pre_travel_response, post_travel_response, pre_home_response,
                      post_home_response, pre_fit_response, post_fit_response, pre_garden_response,
                      post_garden_response, pre_rest_response, post_rest_response,
                      pre_fun_response, post_fun_response]

    time_responses = [pre_traveling, post_traveling, pre_work_home, post_work_home, pre_keep_fit,
                      post_keep_fit, pre_gardening, post_gardening, pre_sleep_rest, post_sleep_rest,
                      pre_social_fun, post_social_fun]

    screen.mainloop()


class NotIntegerError(Exception):
    """Exception raised when not inputting integer in 'Minutes Spent Daily' questions."""

    def __str__(self) -> str:
        """Return a string representation of this error."""
        return "you may only enter an integer in 'Minutes Spent Daily' questions."


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['tkinter', 'vader', 'graph'],
        'allowed-io': ['show_data', 'display_survey'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
