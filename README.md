<img src="https://pbs.twimg.com/media/E0m6c9FX0AIX0p1.png" style="height:350px" align="center"/> <br><br>


![GitHub Repo stars](https://img.shields.io/github/stars/tmwProjects/Georoc_jupyter?style=social) ![GitHub followers](https://img.shields.io/github/followers/tmwProjects?style=social) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/tmwProjects/Georoc_jupyter) 

***

The GEOROC Database (Geochemistry of Rocks of the Oceans and Continents) is a comprehensive collection of published analyses of igneous and metamorphic rocks and minerals. It contains major and trace element concentrations, radiogenic and nonradiogenic isotope ratios as well as analytical ages for whole rocks, glasses, minerals and inclusions. Metadata include geospatial and other sample information, analytical details and references.

The GEOROC Database was established at the Max Planck Institute for Chemistry in Mainz (Germany). In 2021, the database was moved to Göttingen University, where it continues to be curated as part of the DIGIS project of the Department of Geochemistry and Isotope Geology at the Geoscience Centre (GZG) and the University and State Library (SUB). Development for GEOROC 2.0 includes a new data model for greater interoperability, options to contribute data, and improved access to the database.

As part of the DIGIS project, a new API interface has been created for the GEOROC database, allowing easy access to its contents with simple programming skills. Users can now query the database and retrieve data using the new API, making it more accessible and useful for researchers and other interested parties. This notebook demonstrates the basic capabilities of GEOROC data access via the new DIGIS API. 

For feedback, questions and further information contact [Digis-Info](mailto:digis-info@uni-goettingen.de) directly.


<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width="150" />

***

# Jupyter-Notebook

We have created a Jupyter notebook specifically designed to illustrate the features of GEOROC 2.0. Our main focus is on data access via the API, after which we follow suggested workflows for data formatting, cleaning, resampling, and presentation.

The first part of the notebook illustrates the process of sending API requests. It shows how users can query the API and retrieve data from the GEOROC database. The examples covered in this notebook cover API requests and demonstrate the usability and accessibility of the new API. 
The second part is all about general data formatting techniques. It explains how to prepare, clean, and format data retrieved from the GEOROC database for further analysis.
The third and final part focuses on data visualization and includes a detailed reconstruction of a geochemical publication. More specifically, we reconstructed the publication "Major Element, Volatile and stable Isotope geochemistry of Hawaiian submarine tholeiitic glasses" by Garcia et al. (1989). This notebook illustrates how the formatted and cleaned data can be visualized to provide valuable insight and interpretation. It demonstrates various methods of data visualization and their effective use to present results in a clear and understandable manner.

***

### Usage:

Launch our notebook on Binder by clicking the button [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tmwProjects/Georoc_jupyter/HEAD?labpath=DIGIS_GeoRoc.ipynb) **OR** [Download our Notebook](https://github.com/tmwProjects/Georoc_jupyter/blob/main/DIGIS_GeoRoc.ipynb) and use it on your local machine or in your browser. If you are not familiar with Jupyter, you can visit the [official website](https://jupyter.org/) for more information.


###### Hint: To utilize our notebooks, please note that it is necessary to have an API key from GEOROC. If you do not have an API key, we recommend visiting the official homepage to request one.

***

### Social:

[Visit our Website](https://georoc.eu/)

![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FDIGISgeo)

***

### References

[1] Garcia, M. O., Muenow, D. W., Aggrey, K. E., and O'Neil, J. R. (1989), Major element, volatile, and stable isotope geochemistry of Hawaiian submarine tholeiitic glasses, J. Geophys. Res., 94( B8), 10525– 10538, doi:10.1029/JB094iB08p10525. 

[2] requests - Python HTTP library for humans. [Online]. Available: https://requests.readthedocs.io

[3] json - This is part of Python's standard library. Python Software Foundation. Python Language Reference, version 3.x. Available at http://www.python.org

[4] pandas - Wes McKinney. Data Structures for Statistical Computing in Python, Proceedings of the 9th Python in Science Conference, 51-56 (2010) [Online]. Available: https://pandas.pydata.org

[5] geopandas - GeoPandas developers. GeoPandas: Python tools for geographic data [Online]. Available: https://geopandas.org

[6] seaborn - Michael Waskom, Olga Botvinnik, Drew O’Kane, Paul Hobson, Joel Ostblom, Saulius Lukauskas, ... & Tom Augspurger. (2020, October 4). mwaskom/seaborn: v0.11.0 (Version v0.11.0). Zenodo. http://doi.org/10.5281/zenodo.4019147

[7] matplotlib - John D. Hunter. Matplotlib: A 2D Graphics Environment, Computing in Science & Engineering, 9, 90-95 (2007), DOI:10.1109/MCSE.2007.55

[8] contextily - Darribas, D., Arribas-Bel, D., Nshan, B., & van den Bosch, M. (2020). contextily: context geo-tiles in Python. Journal of Open Source Software, 5(55), 2302. https://doi.org/10.21105/joss.02302

[9] adjustText - Ilya Flyamer. (2016). adjustText: A small library for automatically adjusting text position in matplotlib plots to minimize overlaps. Zenodo. http://doi.org/10.5281/zenodo.4922517

[10] ipywidgets - Project Jupyter. (2017). ipywidgets: Interactive HTML widgets for Jupyter notebooks and the IPython kernel. Zenodo. https://doi.org/10.5281/zenodo.836874