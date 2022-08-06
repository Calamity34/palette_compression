<center><h2>Palette Compression</h2>
<h6>fork by Calamity34, original by volyomaS</h6>

---
This script can compress the color palette of your image using ML algorithms (KMeans and DBSCAN).\
You can run this script from the console:\
`python main.py <filename> [colors=2] [use DBSCAN=no]`

For example:\
`python main.py lenin.jpg 7 yes`\
DBSCAN is off by default. Warning: using DBSCAN on high resolution images will work for a long time.

Source:\
![Source img](https://github.com/Calamity34/palette_compression/raw/master/imgs/lenin.jpg)\
KMeans with 7 colors:\
![KMeans img](https://github.com/Calamity34/palette_compression/raw/master/imgs/lenin_kmeans_7.jpg)
