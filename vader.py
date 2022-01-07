"""CSC110 Fall 2021 Final Project

Copyright and Usage Information
===============================

This file has been produced to process the raw data as well as adding it to the processed_data.csv
and is solely for the private use of project members. All forms of distribution of this code,
whether as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 by Harshkumar Patel, Darpan Mishra, Janel Gilani, Aviral Bhardwaj.
"""
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Vader:
    """ A converter that takes the survey data and compiles new data based on current csv data

    Representation Invariants:
        - self._num_responses >= 0
        - all(category in {'Travel and Transport', 'Work from Home', 'Staying Fit',
            'Gardening and DIY', 'Rest and Sleep', 'Entertainment and Socializing'}
            for category in self._responses.keys())
        - all(category in {'Travel and Transport', 'Work from Home', 'Staying Fit',
            'Gardening and DIY', 'Rest and Sleep', 'Entertainment and Socializing'}
            for category in self._time_spent.keys())
        - all(category in {'Travel and Transport', 'Work from Home', 'Staying Fit',
            'Gardening and DIY', 'Rest and Sleep', 'Entertainment and Socializing'}
            for category in self._scored_responses.keys())
        - all(category in {'Travel and Transport', 'Work from Home', 'Staying Fit',
            'Gardening and DIY', 'Rest and Sleep', 'Entertainment and Socializing',
            'Number Surveyed'} for category in self._csv_enjoy())
        - all(category in {'Travel and Transport', 'Work from Home', 'Staying Fit',
            'Gardening and DIY', 'Rest and Sleep', 'Entertainment and Socializing',
            'Number Surveyed'} for category in self._csv_time())

    """
    # Private Instance Attributes:
    #     - _responses: the survey response represented by a dictionary that maps the category to
    #     a tuple of the responses before and after covid respectively
    #     - _num_responses: The number of people who have took the survey
    #     - _time_spent: The survey response represented by a dictionary mapping the category to
    #     a tuple of the time spent before and after covid respectively
    #     - _scored_responses: the survey response represented by a dictionary that maps the
    #     category to a tuple of the responses converted to their sentiment scores through vader
    #     lexicon before and after covid respectively
    #     - _csv_enjoy: the data from the csv file represented by a dictionary that maps the
    #     category to a tuple of their sentiment scores before and after covid respectively
    #     - _csv_time: the data from the csv file represented by a dictionary mapping the category
    #     to a tuple of the time spent before and after covid respectively

    _responses: dict[str, tuple[str, str]]
    _num_responses: int
    _time_spent: dict[str, tuple[int, int]]
    _scored_responses: dict[str, tuple[float, float]]
    _csv_enjoy: dict[str, tuple[float, float]]
    _csv_time: dict[str, tuple[float, float]]

    def __init__(self) -> None:
        """Initialize a new Vader converter object

        The converter will not start with any stored data
        """
        self._responses = {}
        self._num_responses = 0
        self._time_spent = {}
        self._scored_responses = {}
        self._csv_enjoy = {}
        self._csv_time = {}

    def add_category(self, activity: str, response: tuple[str, str], time: tuple[int, int]) -> None:
        """Add a new categories response along with time spent"""
        self._responses[activity] = response
        self._time_spent[activity] = time

    def increase_participant_num(self) -> None:
        """Increase the number of participants by 1, the additional person that took the survey"""
        self._num_responses = self._num_responses + 1

    def convert_response(self) -> None:
        """Convert all the responses to their respective sentiment score"""
        sentiment = SentimentIntensityAnalyzer()
        for activity, set_response in self._responses.items():
            pre_convert = sentiment.polarity_scores(set_response[0])
            post_convert = sentiment.polarity_scores(set_response[1])
            self._scored_responses[activity] = (pre_convert['compound'], post_convert['compound'])

    def add_raw(self) -> None:
        """Add the survey response to the raw_data csv file"""
        with open('raw_data.csv', 'a') as csv_file:
            csv_appender = csv.writer(csv_file)
            csv_appender.writerow([self._time_spent['Travelling and Transport'][0],
                                   self._time_spent['Travelling and Transport'][1],
                                   self._responses['Travelling and Transport'][0],
                                   self._responses['Travelling and Transport'][1],
                                   self._time_spent['Working from Home'][0],
                                   self._time_spent['Working from Home'][1],
                                   self._responses['Working from Home'][0],
                                   self._responses['Working from Home'][1],
                                   self._time_spent['Staying Fit'][0],
                                   self._time_spent['Staying Fit'][1],
                                   self._responses['Staying Fit'][0],
                                   self._responses['Staying Fit'][1],
                                   self._time_spent['Gardening and DIY'][0],
                                   self._time_spent['Gardening and DIY'][1],
                                   self._responses['Gardening and DIY'][0],
                                   self._responses['Gardening and DIY'][1],
                                   self._time_spent['Sleep and Rest'][0],
                                   self._time_spent['Sleep and Rest'][1],
                                   self._responses['Sleep and Rest'][0],
                                   self._responses['Sleep and Rest'][1],
                                   self._time_spent['Entertainment and Socializing'][0],
                                   self._time_spent['Entertainment and Socializing'][1],
                                   self._responses['Entertainment and Socializing'][0],
                                   self._responses['Entertainment and Socializing'][1]
                                   ])

    def get_from_csv(self) -> None:
        """Get all the relevant data from the csv file"""
        with open('processed_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                if line[0] == 'Number Surveyed':
                    self._num_responses = self._num_responses + int(line[1])
                    break
                self._csv_enjoy[line[0]] = (float(line[1]), float(line[2]))
                self._csv_time[line[0]] = (float(line[3]), float(line[4]))

    def compile_data(self) -> None:
        """Add the new survey data to the current csv data"""
        for activity in self._csv_enjoy:
            self._csv_enjoy[activity] = ((self._csv_enjoy[activity][0] * (self._num_responses - 1)
                                          + self._scored_responses[activity][0])
                                         / self._num_responses,
                                         (self._csv_enjoy[activity][1] * (self._num_responses - 1)
                                          + self._scored_responses[activity][1])
                                         / self._num_responses)

        for activity in self._csv_time:
            self._csv_time[activity] = ((self._csv_time[activity][0] * (self._num_responses - 1)
                                         + self._time_spent[activity][0])
                                        / self._num_responses,
                                        (self._csv_time[activity][1] * (self._num_responses - 1)
                                         + self._time_spent[activity][1])
                                        / self._num_responses)

    def overwrite_csv(self) -> None:
        """Overwrite the csv file with the new data"""
        overall_list = []
        for activity, enjoyment in self._csv_enjoy.items():
            temp_row = [activity, str(enjoyment[0]), str(enjoyment[1])]
            overall_list.append(temp_row)

        for row in overall_list:
            for activity, time in self._csv_time.items():
                if activity == row[0]:
                    row.append(str(time[0]))
                    row.append(str(time[1]))

        overall_list.insert(0, ['Activity', 'Enjoyment Before the Pandemic',
                                'Enjoyment After the Pandemic',
                                'Time Spent Daily Before the Pandemic (Minutes)',
                                'Time Spent Daily After the Pandemic (Minutes)'])

        overall_list.append(['Number Surveyed', str(self._num_responses), 0, 0, 0])

        with open('processed_data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in overall_list:
                csv_writer.writerow(row)

    def compute(self) -> None:
        """Take the survey response and convert it and modify the csv file with the new survey data
        """
        self.convert_response()
        self.get_from_csv()
        self.compile_data()
        self.overwrite_csv()


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['vaderSentiment.vaderSentiment', 'csv'],
        'allowed-io': ['compute', 'overwrite_csv', 'get_from_csv', 'add_raw'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
