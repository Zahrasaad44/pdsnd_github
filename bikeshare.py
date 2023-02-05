import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    """
        
    print('Hello! Let\'s explore some US bikeshare data! \n')
    
    city = input('Which city you want to see data for Chicago, New york city, Washington? ').lower()

    while True:
        if city not in CITY_DATA.keys():
            print('Please enter one of these cities only (Chicago, New york city, Washington)')
            city = input('Which city you want to see data for Chicago, New york city, Washington? ').lower()
           
        else:
            month = input('Which month? January, February, March, April, May, June. Please type out the full month name ').lower()
            
            if month not in MONTHS:
                print('Please enter one of these months, (January, February, March, April, May, June)')
            
            else:
                day = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. Please type out the full day name ').lower()
                
                if day not in DAYS:
                    print('Please enter a correct day name, (sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday)')
                else:
                    break

 
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Creating 'month' and 'day' columns from 'Start Time' column
    
    df['month'] = df['Start Time'].dt.month # This column has the months by number not by name  
    df['day'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        month = MONTHS.index(month) + 1  
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
   
    print('The most common month of travel: \n', df['month'].mode()[0])

    print('The most common day of travel: \n', df['day'].mode()[0])

    # Creating the 'hour' column from the 'Start Time' column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    
    print('The most common start hour: \n', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    print('Most commonly used start station: \n', df['Start Station'].mode()[0])

    print('Most commonly used end station: \n', df['End Station'].mode()[0])

   # From StakOverflow https://stackoverflow.com/a/53037757
    print('most frequent combination of start station and end station trip: \n', df.groupby(['Start Station', 'End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

  
    print('Total travel time (in seconds): \n', df['Trip Duration'].sum())

    print('Average travel time (in seconds): \n', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('Counts of user types: \n', df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print('Counts of gender: \n', df['Gender'].value_counts())
        
    else:
        print('The dataset of this city has no "Gender" column')
    
   
    if 'Birth Year' in df.columns:
        print('Earliest year of birth: \n', df['Birth Year'].min())
        print('Most recent year of birth: \n', df['Birth Year'].max())
        print('Most common year of birth: \n', df['Birth Year'].mode()[0])
    
    else:
        print('The dataset of this city has no "Birth Year" column')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def disply_raw_data(df):
    rows = 5
    
    while True:
        more_data = input("Would you like to see all the details of the trips? (type 'Y' for 'yes' and N for 'No')").upper()
        
        if more_data == 'Y':
            print(df.head(rows))
            rows += 5
            
        elif more_data == 'N':
            break
            
        else:
            print("Your input is not correct. You can enter 'Y' or 'N' only")
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disply_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

