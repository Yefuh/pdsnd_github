import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nPlease enter city name by which you intend to filter by? New York City, Chicago or Washington?\n").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("\nPlease you must enter one of the cities of chicago, new york or washington\n")
    

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nPlease enter the name for month from the months January through june or all to analyze the data for all months\n").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("\nPlease you must enter one of the months of January, February, March, April, May, June, or all\n")       
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # In the following piece of code, a check is performed to validate the value read for day of the week.
    while True:
        day = input(" \nPlease enter a name of the day of week to analyze by or all to analyze all the days \n").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            day = input("\nPlease enter a valid input which must be the name of a day in the week or enter 'all' to analyze for all the days of the week\n").lower()
    

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
	This has just been written for the purpose of refactoring code
    """
    # The data file is being read into dataframe and day and month extracted from datetime format
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day    
                                      
    # filtering by the month of year if it is applicable
                                      
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filtering by the day of week if applicable
    
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("The most common month is {}".format(most_common_month))


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week  is {}".format(most_common_day))
       

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common start hour is {}".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].value_counts().idxmax()
    print('\nMost Commonly used start station:', most_common_start)


    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].value_counts().idxmax()
    print('\nThe most commonly used end station:', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).count()
    #common = (df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)).value_counts().idxmax()
    print('\n The Most Commonly used combination of start and end station is:', most_frequent_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is {}".format(Total_travel_time))  


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is {}".format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users. Code refactoring is done here too"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types:\n', df['User Type'].value_counts())



    # TO DO: Display counts of gender
    if('Gender' in df):
        number_females = df['Gender'].str.count('Female').sum()
        
        number_of_males = df['Gender'].str.count('Male').sum()
        
        print('\nThere are {} male users\n'.format(int(number_of_males)))
        
        print('\nThere are {} female users\n'.format(int(number_females)))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        most_common = df['Birth Year'].value_counts().idxmax()
        
        earliest = df['Birth Year'].min()
        
        most_recent = df['Birth Year'].max()
        
        print('\n The earliest Birth Year is {}\n The most recent Birth Year is {}\n The Most common Birth Year is {}\n'.format(int(earliest), int(most_recent), int(most_common)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_raw_data(df):    
    raw_input = input('\nPlease enter yes if you would like to see 5 lines of raw data or a no if you will not want to see it.\n').lower() 
    count = 0
    while True :
        if raw_input == 'yes':
            print(df.iloc[count : count + 5])
            count = count + 5
            raw_input = input('\nEnter yes or no to see more data or not.\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
