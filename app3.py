import pandas as pd
from awesome_table import AwesomeTable
from awesome_table.column import Column
from awesome_table.column import ColumnDType
import csv
import json
from pandas.io.json import json_normalize






# # Function to convert a CSV to JSON
# # Takes the file paths as arguments
# def make_json(csvFilePath, jsonFilePath):
	
# 	# create a dictionary
# 	data = {}
	
# 	# Open a csv reader called DictReader
# 	with open(csvFilePath, encoding='utf-8') as csvf:
# 		csvReader = csv.DictReader(csvf)
		
# 		# Convert each row into a dictionary
# 		# and add it to data
# 		for rows in csvReader:
			
# 			# Assuming a column named 'No' to
# 			# be the primary key
# 			key = rows['State_Name']
# 			data[key] = rows

# 	# Open a json writer, and use the json.dumps()
# 	# function to dump data
# 	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
# 		jsonf.write(json.dumps(data, indent=4))
		
# # Driver Code

# # Decide the two file paths according to your
# # computer system
# csvFilePath = r'iti_trades.csv'
# jsonFilePath = r'iti_trades2.json'

# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)

sample_data = r'iti_trades.csv'

AwesomeTable(pd.read_csv(sample_data), columns=[
    Column(name='Trade_Name', label='Trade Name'),
    Column(name='Course_Duration', label='Course Duration'),
    Column(name='ITI_Name', label='ITI Name'),
    Column(name='Year', label='Year'),
    Column(name='ITI_Address', label='ITI Address'),
    Column(name='State_Name', label='State Name'),
    Column(name='District_Name', label='District Name'),
    Column(name='ITI_Category', label='ITI Category'),
    Column(name='Principal_Name', label='Principal Name'),
    Column(name='Principal_Email_id', label='Principal Email id'),
    Column(name='Details', label='NSTI/ITI')
    # Column(name='_url.social_media', label='Social Media', dtype=ColumnDType.ICONBUTTON, icon='fa-solid fa-share-nodes'), ## From FontAwesome v6.0.0
    # Column(name='_url.document', label='Document', dtype=ColumnDType.DOWNLOAD),
], show_order=True, show_search=True, show_search_order_in_sidebar=True)