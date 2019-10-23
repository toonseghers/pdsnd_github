import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

available_citys=["chicago","new york city","washington"]
available_months=['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december','all']
available_days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
available_answer_display_raw=["yes","no"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    print('Hello! Let\'s explore some US bikeshare data!')

    city = str(input("What's the prefered city? Type 'all' if no preference: "))
    while isinstance(city, str) == 'False':
        print("No data was gathered on this city or no string was entered. Pleaese try again...")
        print("Suggested citys are:{}".format(available_citys))
        city = input("What's the prefered city? Type 'all' if no preference: ")

    month = input("What's the prefered month? Type 'all' if no preference: ")
    while month.lower() not in available_months:
        print("No valid month was entered. Pleaese try again...")
        month = input("What's the prefered month? Type 'all' if no preference: ")

    day = input("What's the prefered day (in words)? Type 'all' if no preference: ")
    while day.lower() not in available_days:
        print("No valid day was entered. Pleaese try again...")
        day = input("What's the prefered day? Type 'all' if no preference: ")


    print('-'*40)
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
    pf = pd.read_csv(CITY_DATA[city])

    pf['Start Time'] = pd.to_datetime(pf['Start Time'])

    pf['months']=pf['Start Time'].dt.month
    pf['days']=pf['Start Time'].dt.weekday_name
    pf['hours']=pf['Start Time'].dt.hour

    if month != "all":
        month = available_months.index(month) +1
        pf['months']=pf[pf['months'] == month]

    if day != "all":
        pf['days']=pf[pf['days'] == day]

    return pf


def time_stats(pf):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=pf['months'].mode()
    print("The most common month is {}".format((available_months[(most_common_month[0]-1)]).title()))

    # TO DO: display the most common day of week
    most_common_day=pf['days'].mode()
    print("The most common day of the week is {}".format(most_common_day[0]))

    # TO DO: display the most common start hour
    most_common_hour=pf['hours'].mode()
    print("The most common start hour is {}:00".format(most_common_hour[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_start_station=df['Start Station'].mode()

    # TO DO: display most commonly used end station
    most_commonly_end_station=df['End Station'].mode()

    # TO DO: display most frequent combination of start station and end station trip
    combination=(df['Start Station'] + " // " + df['End Station'])
    most_combination=combination.mode()

    print("The most commonly used start station is {}".format(most_commonly_start_station[0]))
    print("The most commonly used end station is {}".format(most_commonly_end_station[0]))
    print("The most frequent combination of start and end station is {}".format(most_combination[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()

    print("The total travel time expressed in seconds is: {}".format(total_travel_time))
    print("The mean travel time of a trip is: {}".format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types=df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender=df['Gender'].value_counts()
        print('Female vs. male ratio...')
        print(count_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest=df['Birth Year'].min()
        most_recent=df['Birth Year'].max()
        most_common=df['Birth Year'].mode()

        print("")
        print("")
        print('The earliest year of birth is {}'.format(earliest))
        print('The most recent year of birth is {}'.format(most_recent))
        print('The most common it year of birth is {}'.format(most_common[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_info(df):
    display_raw_info=input("Do you wish to see the RAW data? Please only input yes/no... ")
    while display_raw_info.lower() not in available_answer_display_raw:

        print("No valid answer was entered. Pleaese try again...")
        display_raw_info=input("Do you wish to see the RAW data? Please only input yes/no...")

    if display_raw_info =="yes":
        print(df.head(5))

def main():
    city, month, day=get_filters()
    df=load_data(city, month, day)
    time_stats(df)
    user_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    get_raw_info(df)


if __name__ == "__main__":
	main()
