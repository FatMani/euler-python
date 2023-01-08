# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:17:18 2018

@author: Jakub-P.Lech

Project Euler 19: How many Sundays fell on the first of the month during the 
                  20th century?
"""
from datetime import timedelta, date

def dateRange(startDate, endDate):
  for n in range(int((endDate - startDate).days)):
    yield startDate + timedelta(n)

def main():
  startDate = date(1901, 1, 1)
  endDate = date(2000, 12, 31)
  
  sundayCount = sum(1 for d in dateRange(startDate, endDate) if (d.day == 1 and
                    d.weekday() == 6))
  print(sundayCount)

if __name__ == "__main__":
  main()