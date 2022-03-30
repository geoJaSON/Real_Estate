import pandas as pd
import os
import arcgis

folder_path = r'W:\CADD\Sabine to Galveston\Architecture and Engineering\Orange SATOC\TO#5 - Programmatic Activities 20F0048\Post-Award\Submittals\Survey Submittal\Parcel Data Organized by Owner'

owner_list = os.listdir(folder_path)

sdf = pd.DataFrame.spatial.from_featureclass(r"C:\Users\M3ECHJJJ\AppData\Local\Temp\2\ArcGISProTemp9732\1c9c9d35-e5de-4fa7-9347-4e8908ae1c08\Default.gdb\Deedplot_Mosiac_Orange_Count\Annotation")

sdf.to_csv(r'D:\deeds.csv')

sdf




m = sdf['TxtMemo'].str.isnumeric()

ddf = sdf[m]
ddf

ddf.spatial.to_featureclass(location=r"D:\Submitted_Deeds.shp")
