import pprint

import openpyxl
print('Opening Document')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
sheet.freeze_panes = 'A2'
county_data = {}
print('Processing calculation')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + f'{row}'].value
    county = sheet['C' + f'{row}'].value
    pop = sheet['D' + f'{row}'].value

    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

file = open('pop_result.txt', 'w')
file.write('all data = ' + pprint.pformat(county_data))
file.close()
print('Done.')
