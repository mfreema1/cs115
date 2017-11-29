'''
Created on 11/29/2017
@author:   Mark Freeman mfreema1
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day

    def tomorrow(self):
        if self.day == DAYS_IN_MONTH[self.month]:
            self.day = 1
            if self.month == (len(DAYS_IN_MONTH) - 1):
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
    
    def yesterday(self):
        if self.day == 1:
            self.day = DAYS_IN_MONTH[self.month - 1]
            if self.month == 1:
                self.month = (len(DAYS_IN_MONTH) - 1)
                self.year -= 1
            else:
                self.month -= 1
        else:
            self.day -= 1
            
    def addNDays(self, N):
        for _ in range(N):
            self.tomorrow()
    
    def subNDays(self, N):
        for _ in range(N):
            self.yesterday()
            
    def isBefore(self, d2):
        if self.year > d2.year:
            return False
        elif self.year < d2.year:
            return True
        elif self.month > d2.month:
            return False
        elif self.month < d2.month:
            return True
        elif self.day > d2.day:
            return False
        elif self.day < d2.day:
            return True
        else:
            return False
        
    def isAfter(self, d2):
        if self.equals(d2):
            return False
        return not self.isBefore(d2)
    
    def diff(self, d2):
        if self.equals(d2):
            return 0
        d2Copy = d2.copy()
        counter = 0
        if self.isBefore(d2):
            while(not d2Copy.equals(self)):
                d2Copy.yesterday()
                counter -= 1
            return counter
        else:
            while(not d2Copy.equals(self)):
                d2Copy.tomorrow()
                counter += 1
            return counter
        
    def dow(self):
        DAYS_IN_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', \
                       'Saturday', 'Sunday']
        d = Date(11, 6, 2011) #A Sunday
        return DAYS_IN_WEEK[((self.diff(d) % len(DAYS_IN_WEEK))) + 1]
