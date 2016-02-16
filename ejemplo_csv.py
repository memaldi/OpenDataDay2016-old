# encoding=utf-8

import csv
import json

with open('HabitantesTotalesDistritoBarrioEstudios.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    rowcount = 1
    item_list = []
    current_neighborhood = None
    current_item = None
    for row in csvreader:
        if rowcount > 1:
            neighborhood = row[3]
            if current_neighborhood is None or current_neighborhood != neighborhood:
                current_neighborhood = neighborhood
                if current_item is not None:
                    item_list.append(current_item)
                current_item = {'DISTRITO': row[0],
                                'NOMBRE_DISTRITO': row[1].decode('iso-8859-1'),
                                'BARRIO': row[2],
                                'NOMBRE_BARRIO': row[3].decode('iso-8859-1'),
                                'CODIGO_TITULO': row[4],
                                row[5].decode('iso-8859-1'): row[6]}
            else:
                current_item[row[5].decode('iso-8859-1')] = row[6]

        rowcount += 1

    output_json = open('csv.json', 'w+')
    json.dump(item_list, output_json)
