#!/usr/bin/python3

import joblib

model = joblib.load('salary.pk1')
yrs = float(input('Please enter years of experience you have: '))
salary = model.predict([[yrs]])
print(f"Your salary should be around: Rs.{salary}")
