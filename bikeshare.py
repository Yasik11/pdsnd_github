import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

day_names = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday', 'sunday'] 
month_names =  ['january', 'february', 'march', 'april', 'may', 'june']           

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
    
    city = None
    while city not in ('chicago', 'new york city', 'washington'):
        if city != None:
            print("Wrong input, please try again")
        city = input('\nEnter a city name (Chicago, New York City, Washington): \n').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)

    month = None
    while month not in month_names and month not in ['all']:
        if month != None:
            print("Wrong input, please try again")
        month = input('\nEnter a month from January to June or "all": \n').lower()
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day not in day_names and day not in ['all']:
        if day != None:
            print("Wrong input, please try again")
        day = input('\nEnter day of a week or "all": \n').lower()

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    if month != 'all':
        month_idx = month_names.index(month) + 1
        df = df[df['month'] == month_idx]

    if day != 'all':
        df = df[df['day_of_week'] == day_names.index(day)]

    print('-'*40)
    return df
  
def display_time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', month_names[common_month - 1].title())

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', day_names[common_day].title())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' and ' + df['End Station']
    print('Most frequent combination of start station and end station trip: ', df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User types: ', df['User Type'].value_counts())

    if city != 'washington':
        # TO DO: Display counts of gender
        print('Gender: ', df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth: ', int(df['Birth Year'].min()))
        print('Most recent year of birth: ', int(df['Birth Year'].max()))
        print('Most common year of birth: ', int(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def wait_for_yes_no(text_to_print):
    """ Check users input for 'yes' or 'no'.
        Returns 'yes' or 'no' """

    user_input = None
    while user_input not in ('yes','no'):
        if user_input != None:
            print("Wrong input, please try again")
        user_input = input(text_to_print).lower()
    return user_input

def display_data(df):
    """ Displays raw data upon users request."""
    a = 0
    b = 5
    user_iput = wait_for_yes_no('\nWould you like to see raw data? Enter yes or no.\n')
    if user_iput == 'no':
        return
    print(df.iloc[a:b])
    while True:
        user_iput = wait_for_yes_no('\nWould you like to see more 5 lines of raw data?? Enter yes or no.\n')
        if user_iput == 'no':
            break
        a += 5
        b += 5
        print(df.iloc[a:b])
    
        
   

    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_time_stats(df)
        display_station_stats(df)
        trip_duration_stats(df)
        display_user_stats(df, city)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
