import csv

def populate(source_file, dest_file, criterion_column, comparison_column, columns_for_pop, output_name):

    source = list(csv.reader(open(source_file, "rU"), delimiter = ","))
    dest = list(csv.reader(open(dest_file, "rU"), delimiter = ","))

    rowLength =  len(dest[0])

    for row in source:
        for row_2 in dest:
           if len(row_2) == rowLength:
               if row[criterion_column - 1].lower().strip() == row_2[comparison_column-1].lower().strip():
                    for column in columns_for_pop:
                        row_2.append(row[column-1])

    with open(output_name, "wb") as f:
        writer = csv.writer(f)
        writer = writer.writerows(dest)

populate("/Users/delantz/programming/aiddata/csv_populator/cote_divoire/ci_v2.csv", "/Users/delantz/programming/aiddata/csv_populator/cote_divoire/dg_data_split.csv", 3, 13, [1,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], "civ_populated.csv")
