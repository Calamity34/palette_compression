<center><h2>Palette Compression</h2>
<h6>fork by Calamity34, original by volyomaS</h6></center>

---
This script can compress the color palette of your image using ML algorithms (KMeans and DBSCAN).\
You can run this script from the console:\
`python main.py <filename> [colors=2] [use DBSCAN=N/y]`

For example:\
`python main.py armstrong.png 7`\
DBSCAN is off by default. Warning: using DBSCAN on high resolution images will work for a long time.

Source:\
<img src="imgs/armstrong.png" alt="Armstrong in full colors" width="350">\
KMeans with 7 colors:\
<img src="imgs/armstrong_kmeans_7.png" alt="Armstrong in 7 colors" width="350">

**KNOWN BUG: jpegs have worse render quality**