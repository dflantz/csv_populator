import csv

def populate(source_file, dest_file, criterion_column, columns_for_pop, output_name):

    source = list(csv.reader(open(source_file, "rU"), delimiter = ","))
    dest = list(csv.reader(open(dest_file, "rU"), delimiter = ","))

    for row in source:
        for row_2 in dest:
            if row[criterion_column - 1].lower().strip() in (x.lower().strip() for x in row_2):
                for column in columns_for_pop:
                    row_2.append(row[0])

    with open(output_name, "wb") as f:
        writer = csv.writer(f)
        writer = writer.writerows(dest)

populate("/users/delantz/downloads/ci_v2.csv","/users/delantz/downloads/dg_data_split.csv", 3, [5,6,1], "civ_populated.csv")
