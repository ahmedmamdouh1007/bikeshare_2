import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('what do you want to see from this cities (chicago, new york city, washington): ').lower()

        if city not in CITY_DATA:
            print('invalid inputs \n please rewrite city right ^_^')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    while True:
        month = input('Now Put the Month you want (january, february, ... , june):').lower()
        if month not in months:
            print('invalid inputs \n please rewrite your inpute (month) right ^_^')

        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    while True:
        day = input('Now Put the day you want (monday, tuesday, ... sunday): ').lower()
        if day not in days:
            print('invalid inputs \n please rewrite your inpute (day) right ^_^')

        else:
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month

    df["day"] = df["Start Time"].dt.day_name()

    # filter of month
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]
    if month != "all":
        month = months.index(month) + 1
        df = df[df["month"] == month]

    #  filter of day
    if day != "all":
        df = df[df["day"] == day.title()]

    return df


def display_user_row(df):
    # this def for ask user whether they would like want to see the raw data ?
    # row = 0
    # user_answer = input('would you like to see the first 5 rows of data ? \n please choise from (yes/no): ').lower()
    # # get user input for whether they would like want to see the first 5 raws data ?
    # pd.set_option('display.max_columns', None)  # None ---> display columns to max
    #
    # while True:
    #     if user_answer == 'no':
    #         break
    #
    #     print(df[row:row + 5])  # to display the next 5 rows
    #     user_answer = input('would you like to see the next 5 rows of data (yes , no)? : ').lower()
    #     # lower ---> Anywhere to convert the user input to lowercase letters
    #     row += 5

    start = 0
    viaw_data = input("would you like see the first 5 rows?: ").lower()
    while True:
        if viaw_data != "yes":
            break
        print(df.iloc[start:start + 5])
        viaw_data = input("do you need next 5 rows? : ").lower()
        start += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df["month"].mode()[0]
    print('Most common month: {}'.format(most_common_month))

    # display the most common day of week
    most_common_week = df["day"].mode()[0]
    print("Most common day of week: {}".format(most_common_week))

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    M_C_S_H = df["hour"].mode()[0]
    print("Most common start hour: {}".format(M_C_S_H))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df["Start Station"].mode()[0]
    print("most commonly used start station \n {}".format(start_station))

    # display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print("most commonly used end statio\n {}".format(end_station))

    # display most frequent combination of start station and end station trip
    combination_S_E = start_station + "<----->" + end_station
    print("most frequent combination of start station and end station trip: {}".format(combination_S_E))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_travel_time = df["Trip Duration"].sum()
    print("total travel time: {} Hours".format(sum_travel_time / 3600) )  # 60 to convert form secand to minutes

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time: {} Hours".format(mean_travel_time / 3600))  # 60 to convert form secand to minutes

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    c_user_type = df["User Type"].value_counts().to_frame()
    print("counts of user types(Subscriber , Customer): {}".format(c_user_type))

    # Display counts of gender
    if "Gender" in df:
        # because gender not in washington sheet
        c_counts_of_gender = df["Gender"].value_counts().to_frame()
        print("counts of user gender( Male , Female ): {}".format(c_counts_of_gender))

        # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        # because Birth Year not in washington sheet
        R_birth = df["Birth Year"].min()
        print("earliest birth year: {}".format(R_birth))

        M_birth = df["Birth Year"].max()
        print("recent birth year: {}".format(M_birth))

        M_C_birth = df["Birth Year"].mode()[0]
        print("most common of birth year : {}".format(M_C_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_user_row(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
