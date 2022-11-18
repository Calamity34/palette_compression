<center>
<h2>Palette Compression</h2>
<!-- <h6>fork by Calamity34, original by volyomaS</h6> -->
<img src="imgs/header.png">
</center>



---
This script can compress the color palette of your image using ML algorithms (KMeans and DBSCAN).\

Installation requires you to have `poetry` installed via `pip`, to install you need to
run `poetry install` in the folder, then `poetry shell` to get into the venv.

You can run this script like this:\
`python -m palette_compression <filename> [colors=2] [use DBSCAN=N/y]`

For example:\
`python -m palette_compression armstrong.png 7`
<details>
<summary><b>DBScan is broken</b></summary>

> DBSCAN method is currently broken. Images have artifacts, if you can fix it - PLEASE drop a PR.  
> Here's a comparison of timings, also look in the [`imgs/`](imgs/) folder to see the results:  
> ![difference](imgs/db_km_difference.png)
</details>

More examples can be seen in **[samples.md](samples.md)**

<!-- Source:\
<img src="imgs/armstrong.png" alt="Armstrong in full colors" width="350">\
KMeans with 7 colors:\
<img src="imgs/armstrong_kmeans_7.png" alt="Armstrong in 7 colors" width="350"> -->
