#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl, pprint
print('Opening workbook ...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows....')
for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    country = sheet['C'+ str(row)].value
    pop = sheet['D'+ str(row)].value

    countyData.setdefault(state,{})
    countyData[state].setdefault(country, {'tracts': 0, 'pop' : 0})

    countyData[state][country]['tracts'] += 1
    countyData[state][country]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done. ')

