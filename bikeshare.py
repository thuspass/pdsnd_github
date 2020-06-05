<<<<<<< HEAD
#Python code to evaluate usage patterns for as bike share system provider
||||||| 14161e6
=======
#Import libraries
>>>>>>> 96c0e40b88567e0ee5b1dd08e35e2fe26e25aef4
import time
import pandas as pd
import numpy as np

#Available cities for bikeshare evaluation
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Introducing MONTH_DATA and DAY_DATA to have the ability to extend the choosing options if required
MONTH_DATA = ['all','january','february','march','april','may','june']

DAY_DATA = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

# TO DO: get user input for city (Chicago, New York City, Washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city you want to analyze (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        city = input("Invalid city. Please enter your city (Chicago, New York City, Washington) again: ").lower()
    #print(city)

# TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month you want to analyze (all, january, february, ... , june): ").lower()
    while month not in MONTH_DATA:
        month = input("Invalid month. Please enter the month (all, january, february, ... , june) again: ").lower()
    #print(month)

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day you want to analyze (all, monday, tuesday, ... sunday): ").lower()
    while day not in DAY_DATA:
        day = input("Invalid day. Please enter the day (all, monday, tuesday, ... sunday) again: ").lower()
    #print(day)

    print('-'*40)
    return city, month, day

#city, month, day = get_filters()



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.#

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load city data
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    #print(df)

    # change time variables to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['End Time'] = pd.to_datetime(df['End Time']) 
    #print(df['Start Time'])
    #print(df['End Time'])

    # identification of month and day and save them as new variable 
    df['month'] = df['Start Time'].apply(lambda x: x.strftime('%B').lower()) 
    df['day'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower()) 
    #print(df['month'])
    #print(df['day'])

    # filter data by month and day if necessary
    if month != 'all': 
        df = df.loc[df['month'] == month,:] 

    if day != 'all': 
        df = df.loc[df['day'] == day,:] 
    #print(df)


    return df

#df = load_data(city, month, day)
#print(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('...the most common month (relevant when considering all month): {}'.format(str(df['month'].mode().values[0])))

    # TO DO: display the most common day of week
    print('...the most common day (relevant when considering all day): {}'.format(str(df['day'].mode().values[0])))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].apply(lambda x: x.strftime('%H').lower())
    print('...the most common start hour: {}'.format(str(df['start_hour'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("...the most commonly used start station: {}".format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print("...the most commonly used end station: {}".format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    print("...the most frequent combination of start station and end station trip: {}".format(df['trip'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#station_stats(df)

def trip_duration_stats(df):
    #"""Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Calculaton of travel time
    df['travel_time'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print('...total travel time: {}'.format(df['travel_time'].sum()))

    # TO DO: display mean travel time
    print('...mean travel time: {}'.format(df['travel_time'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#trip_duration_stats(df)

def user_stats(df,city):
    #"""Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('...counts of user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # For Washington no information about gender is available, as the column 'Gender' is not available in the file washington.csv
    # --> Index(['Unnamed: 0', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type'],
    if city != 'washington':
        print('...counts of gender:')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    # For Washington no information about gender is available, as the column 'Birth Year' is not available in the file washington.csv
    # --> Index(['Unnamed: 0', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type'],
    if city != 'washington':
        print('Earliast year of birth: {}'.format(int(df['Birth Year'].min())))

        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))

        print('Most common year of birth: {}'.format(int(df['Birth Year'].mode().values[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#user_stats(df)

def display_data(df):
    obs_start = 0
    obs_end = 5

    view_data = ''

    while view_data.lower() not in ['yes', 'no']:
        view_data = input('Would you like to see some raw data? Enter \'yes\' or \'no\'.')
        if view_data.lower() not in ['yes', 'no']:
            print('You have entered an invalid choice. Please try again')
        elif view_data.lower() == "yes":
            print(df.iloc[obs_start:obs_end])
            while True:
                add_data = input('Would you like to see some more raw data? Enter \'yes\' or \'no\'.')
                if add_data.lower() not in ['yes', 'no']:
                    print('You have entered an invalid choice. Please try again')
                elif add_data.lower() == 'yes':
                    obs_start += 5
                    obs_end += 5
                    print(df.iloc[obs_start:obs_end])
                elif add_data.lower() == 'no':
                    return
        elif view_data.lower() == 'no':
            return
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()