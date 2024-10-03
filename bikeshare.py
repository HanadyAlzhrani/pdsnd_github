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
    # Input city name 
    
    city = input("Enter city name (chicago, new york city, washington): ").lower() #to convert the input into small letters 

    # Check city name validation
    while city not in  ['chicago','new york city','washington']:
        print("Invalid name!, Try Again.") 
        city = input().lower() 

    # Lists for valid months, days
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all'] 
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all'] 

    # Input month and day, Then check the validation 
    month = input("Enter a valid month (january, february, march, april, may, june, all):  ").lower() 
    while month not in months: 
        print("Invalid month!, Try Again.") 
        month = input().lower() 

    day = input("Input a day (sunday, monday, tuesday, wednesday, thursday, friday, all): ").lower() 
    while day not in days: 
        print("Invalid day!, Try Again.") 
        day = input().lower() 

    print('-' * 40)  # Move this line above the return statement
    return city, month, day 

    


def load_data(city, month, day):
  #Load data from CSV file into data frame 
    df = pd.read_csv(CITY_DATA[city]) #to load data from csv file into dataframe 
#Convert start time column values into date 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

#Extract month & Day, Hour from start time column 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start Hour'] = df['Start Time'].dt.hour


#FLITERATIN By month, day
    if month != 'all' : 
         months = ['januray','february', 'march' ,'april','may','june'] 
         month = months.index(month)+1 #plus 1 cause python zero-based indexed, i want it to start from one 
         df = df[df['month']==month] 

    if day != 'all': 
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'Thursday', 'friday', 'saturday'] 
        df = df[df['day_of_week']==day.title()] #title() to make it start with capital letter 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # TO DO: display the most common month
    common_month = df['month'].mode()[0] #[0] to return just first repeated mode 
    print(f"The most common month is : {common_month}") #f, {} to format and display in good way 


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"the most common day of week is: {common_day}") 


    # TO DO: display the most common start hour
    common_start_hour = df['start Hour'].mode()[0]
    print(f"most common start hour is: {common_start_hour}")


    print("\nThis took %s seconds." %  (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

        # TO DO: display most commonly used start station
    Common_Start_Station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station is: {Common_Start_Station}")

    # TO DO: display most commonly used end station
    Common_End_Station = df['End Station'].mode()[0]
    print(f"Most commonly used end station is: {Common_End_Station}")

    # TO DO: display most frequent combination of start station and end station trip
    Frequent_Combination = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print(f"Most frequent combination of start station and end station trip is:  {Frequent_Combination}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum() 
    print(f"The total travel time is: {Total_Travel_Time}")


    # TO DO: display mean travel time
    Mean_Travel_Time = Total_Travel_Time.mean() 
    print(f"Mean travel time is: {Mean_Travel_Time}") 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of User Type is: ", df['User Type'].value_counts()) #to count values of user type 

    # TO DO: Display counts of gender
    if 'Gender' in df: #Because gender is not found in washington file 
        print("Gender Counts", df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df: #Because birthyear is not found in washington file 
        
        print("Earliest year is: ", int(df['Birth Year'].min()))
        print("Most recent year is: ", int(df['Birth Year'].max()))
        print("Most common year is: ", int(df['Birth Year'].mode()[0]))
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def returning_five_lines(df): #function to return 5 lines instead of return all data 
    counter = 0
    while True:
        answer = input("Do you want to show five lines of data? (yes/no): ").lower()
        if answer == 'no':
            print("Thanks!")
            break
        elif answer == 'yes':
            while counter < df.shape[0]: #while counter less than dataframe size 
                print(df.iloc[counter:counter+5]) #iloc to access data based on its positiion
                counter += 5
                answer = input("Do you want to show five more lines of data? (yes/no): ").lower()
                if answer != 'yes':
                    print("Thanks!")
                    break
            break  
        else:
            print("Invalid input!, Enter(yes\no)") #if its not neither yes or no 

        
    
def main(): 
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        returning_five_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Good bye, Thanks!.") 
            break


if __name__ == "__main__":
	main()
