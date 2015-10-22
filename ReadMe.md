# Remap Enterprise Geodatabase Layers #
This python script is used to repath SDE layers within a Map Document when the database and feature class name has changed. 

This script was developed to help Waimakariri District Council when they migrated from ArcGIS 10.0 to ArcGIS 10.3. During this process four databases were reconciled to one and many feature class names changed. 

## Requirements ##
- ArcGIS Desktop 10.3
- ArcSDE 10.3
- Python 2.7
- arcpy 10.3

## Parameters ##
The script requires a csv table as an input parameter and can be configured as follows.

The CSV file should have the following columns:

- Connection File (e.g. \\[path to]\[connection file].sde)
- PublishFeatureClass (e.g. [Database Name].[schema].[Feature Class Name])
- SourceDatabase (e.g. [Database name])
- SourceFeatureClass (e.g. [Source Feature Class Name])