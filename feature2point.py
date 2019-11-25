# Name: feature2point.py 
# Description: Use FeatureToPoint function to find a point inside each park 
# Author: zhangpengye  
import arcpy 
from arcpy import env  
# Set environment settings 
env.workspace = "D:/temp/tdt.gdb" 
fcs = []
dscount = 0
fscount = 0
lstFC = arcpy.ListFeatureClasses()
for fc in lstFC:
    print(fc)
    outFeatureClass = "D:/temp/test/"+str(fc)
    print(outFeatureClass)
    arcpy.FeatureToPoint_management(fc, outFeatureClass, "INSIDE")
#print(lstFC)
## Set local variables 
#inFeatures = "parks.shp" 
#outFeatureClass = "c:/output/output.gdb/parks_pt"  
## Use FeatureToPoint function to find a point inside each park 
#arcpy.FeatureToPoint_management(inFeatures, outFeatureClass, "INSIDE")
