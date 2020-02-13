# Palette compression
This script can compress the color palette of your image using ML algorithms (KMeans and DBSCAN).\
You can run this script from the console:\
 **python main.py [filename] [count of colors in new palette] [[yes/no (for DBSCAN)]]**\
 For example:\
 **python main.py C:\Users\1.jpg 3 yes**\
 DBSCAN is off by default. Warning: using DBSCAN on high resolution images will work for a long time.
