import arcpy


def log_warning(warning):

    arcpy.AddWarning(warning)
    print(warning)


def log_message(message):
    arcpy.AddMessage(message)
    print(message)