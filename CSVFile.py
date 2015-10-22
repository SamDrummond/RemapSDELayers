import csv
import arcpy


def csv_to_list(csv_path=None):

    if csv_path is None:
        csv_path = arcpy.GetParameterAsText(0)

    raw_list = []

    with open(csv_path, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        raw_list = list(reader)

    return raw_list




