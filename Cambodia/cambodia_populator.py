import csv

#filepath_dest refers to the file to be populated
def populate(filepath_source, filepath_dest, output_name):
	list1 = list(csv.reader(open(filepath_source, "rU"), delimiter = ','))
	list2 = list(csv.reader(open(filepath_dest, "rU"), delimiter = ','))
	
	for row in list1:
		for row2 in list2:
			if row[0].lower().strip() == row2[0].lower().strip():
				row2.append(row[1])
				row2.append(row[2])
				row2.append(row[3])

	with open(output_name, "wb") as f:
		writer = csv.writer(f)
		writer.writerows(list2)

populate("/users/delantz/Downloads/cambodia_locations.csv", \
	"/users/delantz/Downloads/cambodia_simple.csv", "cambodia_populated.csv")


