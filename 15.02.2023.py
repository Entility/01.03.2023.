import csv
import json

file_name = 'Programmēšana 2022/08.02.2023/spotify.csv'
json_file_name = 'Programmēšana 2022/08.02.2023/songs.json'


songs_list=[]

with open(file_name, "ŗ", encoding='UTF8') as data_file:
    for line in csv.reader(data_file):
        songs_list.append(line)

with open(json_file_name, "w", encoding='UTF8') as json_file:
    json.dump(songs_list, json_file)