#!/usr/bin/python3

team_file = open("team", "r")

members = team_file.readlines()

for member in members:
    print(member.split(" ")[-1].strip())
