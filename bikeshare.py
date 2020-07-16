import time
import pandas as pd
import numpy as np
import sys
pd.set_option('display.max_columns', None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # Get user input for city (chicago, new york city, washington).
    while True:
        try:
            cities = ['chicago','new york city','washington']
            city = input("Please enter one of the following cities for bikeshare data analysis - Chicago, New York City, or Washington:\n")

            if city.lower() not in cities:
                print('Invalid input. Please enter Chicago, New York City, or Washington\n')
            else:
                break
        except KeyboardInterrupt:
            user_cancel()

    # Get user input for month (none, january, february, ... , june)
    while True:
        try:
            months = ['january','february','march','april','may','june']
            month = input("Please enter a month (January, February, ... , June) to filter the data or enter 'none' to apply no month filter:\n")

            if month.lower() not in months and month.lower() != 'none':
                print('Please enter a valid month (January, February, ... , June) or none to apply no month filter.\n')
            else:
                break
        except KeyboardInterrupt:
            user_cancel()

    # Get user input for day of week (none, monday, tuesday, ... sunday)
    while True:
        try:
            days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            day = input("Please enter a day (Monday, Tuesday, ... Sunday) to filter the data or enter 'none' to apply no day filter:\n")

            if day.lower() not in days and day.lower() != 'none':
                print('Please enter a valid weekday (Monday, Tuesday, ... Sunday) or none to apply no day filter.\n')
            else:
                print('-'*40)
                return city.lower(), month.lower(), day.lower()
                break
        except KeyboardInterrupt:
            user_cancel()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df.month == month]

    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week.str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # Display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['day_of_week'].mode()[0]
    print('Most Frequent Day of the week:', popular_weekday)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    # Display most frequent combination of start station and end station trip
    popular_start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Frequent Start/End Station Combination:', popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # Display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', total_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Type:')
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('\nCount of Gender:')
        print(count_gender)
    else:
        print('\nThere is no Gender data for this data set.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarlist birth year:', int(df['Birth Year'].min(skipna = True)))
        print('Most recent birth year:', int(df['Birth Year'].max(skipna = True)))
        print('Most common birth year:', int(df['Birth Year'].mode()[0]))
    else:
        print('\nThere is no Birth Year data for this data set.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays 5 lines of raw data on bikeshare users per the request of the user"""
    try:
        printed_row_count = 0
        raw_restart = yes_no_check(input('\nWould you like to see raw data? Please enter yes or no.\n'))

        if raw_restart == 'yes':
            if {'Gender', 'Birth Year'}.issubset(df.columns):
                print(df.iloc[printed_row_count:(printed_row_count+5),1:9])
                printed_row_count += 5
            else:
                print(df.iloc[printed_row_count:(printed_row_count+5),1:7])
                printed_row_count += 5
            while True:
                try:
                    raw_restart2 = yes_no_check(input('\nWould you like to see more raw data? Please enter yes or no.\n'))

                    if raw_restart2 == 'yes':
                        if {'Gender', 'Birth Year'}.issubset(df.columns):
                            print(df.iloc[printed_row_count:(printed_row_count+5),1:9])
                            printed_row_count += 5
                        else:
                            print(df.iloc[printed_row_count:(printed_row_count+5),1:7])
                            printed_row_count += 5
                    else:
                        break
                except KeyboardInterrupt:
                    user_cancel()
    except KeyboardInterrupt:
        user_cancel()

def user_cancel():
    """Displays message when a user cancel's the script."""
    print('You cancelled the script.')
    sys.exit(0)

def yes_no_check(user_response):
    """
    Verifies a user's input is 'yes' or 'no'. If the input is invalid, it will prompt the user to enter 'yes' or 'no'

    Returns:
        (str) user_response - a user's 'yes' or 'no' response
    """
    valid_response = ['yes','no']

    while user_response.lower() not in valid_response:
        user_response = input('Invalid input. Please enter yes or no.\n')
    return user_response.lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        try:
            response = yes_no_check(input('\nWould you like to restart? Please enter yes or no.\n'))
            if response != 'yes':
                break
        except KeyboardInterrupt:
            user_cancel()


if __name__ == "__main__":
	main()
