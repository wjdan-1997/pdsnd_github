import time
import pandas as pd
import numpy as np
import sys
CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'All']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    answers = [i  for i,l in CITY_DATA.items()]
    # for i, l in CITY_DATA.items():
    #     answers.append(i)
    while True:
        cities = input(
            "\n Which city would you like to explore by? \n New York , Chicago or Washington. only one \n").lower()
        # cities = cities
        if cities not in answers:  # ('new york', 'chicago', 'washington'):
            print("Sorry , Invalid City Input. Try again.")
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "\n Which month would you like to explore by? \n January', 'February', 'March', 'April', 'May', 'June' or type 'all' .\n").lower()
        if month in month_list:
            break
        else:
            print("Sorry, Invalid Month Input. Try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        days = input(
            "\n Which day would you like to explore by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' .\n").capitalize()

        if days in days_list:
            break
        else:
            print("Sorry , Invalid Day Input. Try again.")


    print('-'*40,'\n')
  
    return cities, month, days


def load_data(city, month, day):
    # step 1
    df = pd.read_csv(CITY_DATA[city])  # city user will input
    # print('hereeeeeeee \n', pd.read_csv(CITY_DATA[city]))

    # step 2
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # step 3
    df['month'] = df['Start Time'].dt.month  # month new column
    # print(' new column Month : \n', df['month'], '\n')

    df['day_of_week'] = df['Start Time'].dt.day_name()
    # print(' new column day_name : \n', df['day_of_week'], '\n')

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # print ('hereeee month \n ',month)

        df = df[df['month'] == month]  # input for user in month stored here
        # print('okay here ?? \n',df ,'\n')
    if day != 'All':
        # print('day for user', day)
        df = df[df['day_of_week'] == day.title()]
        # print(' mmm here !? \n',df,'\n')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    try:
        df['month'] = df['Start Time'].dt.month
        print('Most commen month for your travel :',
              df['month'].mode()[0], '\n')
    except KeyError:
        print('Please Enter a valid month and day to filter by')
        # display the most common day of week
    try:
        df['day_of_week'] = df['Start Time'].dt.day_name()
        print('Most commen day of week for your travel : \n',
              df['day_of_week'].mode()[0], '\n')
    except KeyError:
        print('Please Enter a valid month and day to filter by')

    try:
        # display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        print('Most commen hour for your travel :', df['hour'].mode()[0], '\n')
    except KeyError:
        print('Please Enter a valid month and day to filter by')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    S_station = df['Start Station'].mode()[0]
    print('\n Here most commonly used start station for trip :', S_station)

    # display most commonly used end station
    E_station = df['End Station'].mode()[0]
    print('\n Here most commonly used end station for trip: ', E_station)

    # display most frequent combination of start station and end station trip
    df['CM'] = df['Start Station'] + " " + df['End Station']
    CM = df['CM'].mode()[0]
    print('\n Here most frequent combination of start station and end station trip :', CM)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Sum_Duration = df['Trip Duration'].sum()
    print('Total travel time :', Sum_Duration)

    # display mean travel time
    mean_Duration = df['Trip Duration'].mean()
    print('Mean travel time :', mean_Duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print('\n Users Type \n ', user_types)
    except:
        print('sorry')
    try:
        # Display counts of gender
        gen = df['Gender'].value_counts()
        print('\n Genders Type \n', gen)
    
        
        # Display earliest, most recent, and most common year of birth
        mc = df['Birth Year'].mode()[0]
        print('\n Most commen year of birth : ', mc)
        er = df['Birth Year'].min()
        print('\n Earliest year of birth : ', er)
        re = df['Birth Year'].max()
        print('\n Recent year of birth : ', re)
    except:
        print(' \n Sorry ! Gender stats cannot be calculated because Gender does not appear in the dataframe \n and Washington data does not have Gender and Birth Year columns')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks I hope you Enjoyed.')
            break


if __name__ == "__main__":
    main()
