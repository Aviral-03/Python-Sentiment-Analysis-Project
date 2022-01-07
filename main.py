"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file is the final product of our project and is solely for the private use of project members.
All forms of distribution of this code, whether as given or with any changes, are expressly
prohibited.

This file is Copyright (c) 2021 by Harshkumar Patel, Darpan Mishra, Janel Gilani, Aviral Bhardwaj.
"""
from survey import *


def choice() -> None:
    """Lets the user decide if they wish to take the survey or see the results"""
    user_input = input("Would you like to take the survey or see the results,"
                       "(Input 'survey' to take the survey and 'graph' to see the results):")
    if user_input == 'survey':
        display_survey()
    elif user_input == 'graph':
        plotting_data('processed_data.csv', 'secondary_data.csv')
    else:
        print("Please input either 'survey' or 'graph'.")


if __name__ == '__main__':
    choice()
