import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!, I have data on washington, new york and chicago')

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('wich city would you like to explore data on: ').lower()
        if city not in CITY_DATA.keys():
            print('please choose a valid city ')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june

    months = ['january', 'feburary', 'march', 'april', 'may', 'june']
    while True:
        month = input('you may choose to filter the data further, you can choose a month between january and june or type \'all\' to see all months: ').lower()
        if month != 'all' and month not in months:
            print('pleae provide a valid month ')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('you may also filter the data for any specific day of the week or you can type \'all\' to see the data for all days: ').lower()

        if day != 'all' and day not in days:
            print('please choose weekday or you can choose to view all of them')
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode(0)
    print('the most common month is', int(common_month))

    # TO DO: display the most common day of week
    common_day = df['day of week'].mode(0)
    print('the most common day of the week is', str(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode(0)
    print('the most common hour start hour is', int(common_hour), 'O\'clock')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df['Start Station'].mode(0)
    print('the most commonly used start station is', str(common_station))

    # TO DO: display most commonly used end station
    common_station = df['End Station'].mode(0)
    print('the most commonly ued end station is', str(common_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = (df['Start Station'] + '-' + df['End Station']).mode(0)
    print('the most frequent combination of start and end stations are', str(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('the total time of tavel is ', total_time, 'seconds')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('the mean travel time is ', mean_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print(user_count)
    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
     gender_count = df['Gender'].value_counts()     
     print('the gender count is', gender_count)
   
  
    
    # TO DO: Display earliest, most recent, and most common year of birth    
    if 'Birth Year' in (df.columns):
      df['Birth Year'] = pd.to_datetime(df['Birth Year']).dt.year
      most_recent = df['Birth Year'].min()
      common_birth = df['Birth Year'].mode(0)
      earliest_birth = df['Birth Year'].max()
      print('the earliest birth day is', int(earliest_birth), ' the most recent is', int(most_recent), 'and the most common is', int(common_birth))
        
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
 
def raw_data(df):
    i = 0 
    x = ['yes','no']
    while True:       
       answer = input('would you like to view 5 rows of raw data?: ').lower()
       if answer not in x :
           print('answer with yes or no only please')
       if answer == 'no':
           break
       if answer == 'yes':
            print(df[i:i +5])
            i += 5
            
                                                   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no: \n')               
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
