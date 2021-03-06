  import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
			  
def time_stats_data(df):
    i = 0
    while True:
        raw = input("Would you like to see 5 lines of raw data? Enter yes or no.\n")
        
        if raw.lower() != 'yes':
            break
        else:
             print(df[i:i+5])
             i = i + 5

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
	get filter method is added.
    get filter method is added by refactorring.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            city = input("Please write the name of the city:")
            city = city.lower()
            
            month = input("Please write the name of the month:")
            month = month.lower()
            
            day = input("Please write the name of the day:")
            day = day.lower()     
                        
            print('-'*40)
                        
            return city, month, day
                        


def time_stats_data(df):
    i = 0
    while True:
        raw = input("Would you like to see 5 lines of raw data? Enter yes or no.\n")
        
        if raw.lower() != 'yes':
            break
        else:
             print(df[i:i+5])
             i = i + 5
			 
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

    # Convert the Start Time and End Time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Combine Start Station and End Station
    
    df['Combined Stations'] = df['Start Station'] + ' to ' +  df['End Station']
    
    # Subtrack Start Time from End time in order to calculate Trip Duration.
    
    df['Trip Duration'] = (df['End Time'] - df['Start Time']).dt.seconds
    
        # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
       
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculating the most common month.
    
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # Calculating the most common day of week.
    
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Start Day of Week:', popular_day_of_week)
    
    # Calculating the most common start hour.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculating the most common month.
    
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # Calculating the most common day of week.
    
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Start Day of Week:', popular_day_of_week)
    
    # Calculating the most common start hour.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculating most commonly used start station.
    
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    # Calculating most commonly used end station.
    
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # Calculating most frequent combination of start station and end station trip.
    
    popular_combined_station = df['Combined Stations'].mode()[0]
    print('Most Popular Combined Station:', popular_combined_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculating total travel time.
    
    total_travel_time_in_seconds= df['Trip Duration'].sum()
    total_travel_time_in_minutes= df['Trip Duration'].sum()/60
    total_travel_time_in_hours= df['Trip Duration'].sum()/3600
    print("Total Travel Time: {} hours".format(total_travel_time_in_hours))

    # Calculating mean travel time.
    mean_of_travel_time = df['Trip Duration'].mean()
    mean_of_travel_time_in_minutes = mean_of_travel_time / 60
    print("Mean Travel Time: {} minutes".format(mean_of_travel_time_in_minutes))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculating counts of user types.
    user_types = df["User Type"].value_counts()
    print(user_types)
    print()
    
    # Calculating counts of gender.
    # Calculating earliest, most recent, and most common year of birth.
    # Since washington.csv doesn't have Gender and Birth Year informations, we used try, except for KeyError.
    
    while True:
        try:
            gender = df["Gender"].value_counts()
            print(gender)
            print()
            
            earliest_year_of_birth = df["Birth Year"].max()
            most_recent_year_of_birth = df["Birth Year"].min()
            common_year_of_birth = df["Birth Year"].mode()[0]
            
            print("Earliest Year of Birth: {}".format(int(earliest_year_of_birth)))
            print("Most Recent Year of Birth: {}".format(int(most_recent_year_of_birth)))
            print("Common Year of Birth: {}".format(int(common_year_of_birth)))


            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            
        except(KeyError):
            print("*****washington.csv doesn't have Gender and Birth Year informations.*****\n*****So calculations about Gender and Birth year can't be done!*****")
            print()
            break
  
   
def display_data(df):
    i = 0
    while True:
        raw = input("Would you like to see 5 lines of raw data? Enter yes or no.\n")
        
        if raw.lower() != 'yes':
            break
        else:
             print(df[i:i+5])
             i = i + 5
def time_stats_data(df):
    i = 0
    while True:
        raw = input("Would you like to see 5 lines of raw data? Enter yes or no.\n")
        
        if raw.lower() != 'yes':
            break
        else:
             print(df[i:i+5])
             i = i + 5
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
