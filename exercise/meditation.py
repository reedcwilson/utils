#!/usr/bin/env python

import csv


def get_activities():
    with open('InsightTimerLogs.csv', 'r') as f:
        _ = f.readline().strip()
        return [list(csv.reader([line]))[0] for line in f.readlines()]


def calculate_hours(activities):
    hours = 0
    for activity in activities:
        h, m, s = activity[1].split(':')
        hours += float(h) + (float(m)/60) + (float(s)/60/60)
    return hours


def report(activities):
    hours = calculate_hours(activities)
    num = len(activities)
    average = hours / num
    print(f'meditated: {num} for {hours:.2f} hr - avg {average:.2f} hr')


def main():
    activities = get_activities()
    report(activities)


if __name__ == '__main__':
    main()
