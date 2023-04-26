import re
import io
import csv

def split_strip_file(contents):
 semicolon_split = re.split(''';(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', contents)
 semicolon_split = [i.strip() for i in semicolon_split]
 splitted = list(filter(None, semicolon_split))
 final_splitted = []
 for each in splitted:
  final = each + ';'
  final_splitted.append(final)
 value_with_semicolon = []
 for line in final_splitted:
  if 'CREATE MEMBER CURRENTCUBE.[Measures]' in line:
   value=re.sub(r"^.+?(?=CREATE MEMBER)", "", line)
   value_with_semicolon.append(value)
 value_without_semicolon = []  
 for lines in value_with_semicolon:
  data = lines.rstrip(lines[-1])
  value_without_semicolon.append(data) 
 return value_without_semicolon
 


if __name__ == '__main__' :
 with io.open('inputfile.txt',newline=None) as input_txt:
  contents = input_txt.read().replace('\n','')
  needed_value = split_strip_file(contents)
  dot_split = []
  for each in needed_value:
   if "CREATE MEMBER CURRENTCUBE.[Measures]" in each:
    splits = each.split('.',maxsplit=2)
    dot_split.append(splits[2])
  measures_name = []
  measures_calculation = []
  for item in dot_split:
   if 'AS ' in item:
    from_value = 'AS '
   else:
    from_value = 'as ' 
   name = item.find(f'{from_value}')
   if 'FORMAT_STRING' in item:
    to_value = 'FORMAT_STRING'
   else:
    to_value = 'VISIBLE'  
   calculation = re.findall(f'{from_value}(.*){to_value}', item)
   calculation = [i.rstrip(', ').replace('//',' ').strip() for i in calculation]
   calculation = [re.sub('\s{2,}', ' ',i) for i in calculation]
   measures_name.append(item[:name])
   measures_name_final = [each_item.replace('[','').replace(']','').replace('//','').rstrip() for each_item in measures_name]
   measures_calculation.append(calculation[0])
  print(measures_calculation)
  with open('output_data.csv','w',newline='') as output_csv:
   writer = csv.writer(output_csv)
   writer.writerow(['MEASURES_NAME', 'ACTUAL_CALCULATION','CALCULATION_WITH_FORMAT'])
   writer.writerows(zip(measures_name_final,measures_calculation,needed_value))