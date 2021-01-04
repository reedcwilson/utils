#!/usr/bin/env python

import csv


def get_activities():
    with open('activities.csv', 'r') as f:
        _ = f.readline().strip()
        return [list(csv.reader([line]))[0] for line in f.readlines()]


def calculate_hours(activities):
    hours = 0
    for activity in activities:
        h, m, s = activity[6].split(':')
        hours += float(h) + (float(m)/60) + (float(s)/60/60)
    return hours


def report(activities):
    name = activities[0][0]
    hours = calculate_hours(activities)
    num = len(activities)
    average = hours / num
    print(f'{name}: {num} for {hours:.2f} hr - avg {average:.2f} hr')


def main():
    activities = get_activities()
    mtb, virtual, cycling, running, skiing = [], [], [], [], []
    for activity in activities:
        name = activity[0].lower()
        if 'mountain biking' in name:
            mtb.append(activity)
        if 'virtual cycling' in name:
            virtual.append(activity)
        if 'indoor cycling' in name:
            virtual.append(activity)
        if 'cycling' == name:  # must equal - there are other types of cycling
            cycling.append(activity)
        if 'running' in name:
            running.append(activity)
        if 'skiing' in name:
            skiing.append(activity)
    report(mtb)
    report(virtual)
    report(cycling)
    report(running)
    report(skiing)


if __name__ == '__main__':
    main()
