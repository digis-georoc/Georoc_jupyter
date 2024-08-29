<img src="https://pbs.twimg.com/media/E0m6c9FX0AIX0p1.png" style="height:350px" align="center"/> <br><br>

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/digis-georoc/Georoc_jupyter) 
![GitHub Repo stars](https://img.shields.io/github/stars/digis-georoc/Georoc_jupyter?style=social)

***

<span style="text-align: justify; display: block; max-width: 850px; margin: 0 auto;">

The GEOROC Database (Geochemistry of Rocks of the Oceans and Continents) is a comprehensive collection of published 
analyses of igneous and metamorphic rocks and minerals. It contains major and trace element concentrations, radiogenic 
and nonradiogenic isotope ratios as well as analytical ages for whole rocks, glasses, minerals and inclusions. Metadata 
include geospatial and other sample information, analytical details and references.

The GEOROC Database was established at the Max Planck Institute for Chemistry in Mainz (Germany). In 2021, the database #
was moved to Göttingen University, where it continues to be curated as part of the DIGIS project of the Department of 
Geochemistry and Isotope Geology at the Geoscience Centre (GZG) and the University and State Library (SUB). Development 
for GEOROC 2.0 includes a new data model for greater interoperability, options to contribute data, and improved access 
to the database.

As part of the DIGIS project, a new API interface has been created for the GEOROC database, allowing easy access to its 
contents with simple programming skills. Users can now query the database and retrieve data using the new API, making it 
more accessible and useful for researchers and other interested parties. This notebook demonstrates the basic capabilities 
of GEOROC data access via the new DIGIS API. 

For feedback, questions and further information contact [DIGIS-Info](mailto:digis-info@uni-goettingen.de) directly.

</span>

<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width="150" />

***

### Table of Contents

* [Exploring GEOROC 2.0](#exploring-georoc-20)
* [Usage](#usage)
  * [Online](#online)
    * [Browser](#launch-our-notebook-on-binder-in-your-browser-by-clicking-the-button)
    * [Smartphone](#or-scan-the-qr-code-to-run-our-notebook-over-binder-on-your-smartphone)
  * [Local](#local)
    * [Minimal installation](#minimal-installation)
    * [Comprehensive Installation](#comprehensive-installation-advanced-user-interface)
* [Social](#social)
* [Contribution](#contribution)
* [References](#references)
* [License](#license)

***

## **Exploring GEOROC 2.0:** 
### Data Access, Formatting, and Visualization for Geochemical Analysis

<span style="text-align: justify; display: block; max-width: 850px; margin: 0 auto;">

We have created a Jupyter notebook specifically designed to illustrate the features of GEOROC 2.0. Our main focus is 
on data access via the API, after which we follow suggested workflows for data formatting, cleaning, resampling, and presentation.

The first part of the notebook illustrates the process of sending API requests. It shows how users can query the API 
and retrieve data from the GEOROC database. The examples covered in this notebook cover API requests and demonstrate 
the usability and accessibility of the new API. 
The second part is all about general data formatting techniques. It explains how to prepare, clean, and format data 
retrieved from the GEOROC database for further analysis.
The third and final part focuses on data visualization and includes a detailed reconstruction of a geochemical 
publication. More specifically, we reconstructed the publication **"Major Element, Volatile and stable Isotope 
geochemistry of Hawaiian submarine tholeiitic glasses"** by **Garcia et al. (1989)**. This notebook illustrates how 
the formatted and cleaned data can be visualized to provide valuable insight and interpretation. It demonstrates various 
methods of data visualization and their effective use to present results in a clear and understandable manner.

[Back to table of contents](#table-of-contents)

</span>

***

## Usage:

<span style="text-align: justify; display: block; max-width: 850px; margin: 0 auto;">

### Online

##### Launch our notebook on Binder in your browser by clicking the button:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/digis-georoc/Georoc_jupyter/HEAD?labpath=Georoc_Notebook.ipynb)

##### or scan the QR-Code to run our Notebook over Binder on your smartphone:

<img src="grafics/BINDER_JUPYTER_QR.png" style="height:315px" align="center"/> <br><br>

###### Hint: Please note that an API key from GEOROC is required to use our notebook. If you would like to request one, contact [DIGIS-Info](mailto:digis-info@uni-goettingen.de) directly.

[Back to table of contents](#table-of-contents)



### Local

These instructions assume that Python and pip are installed on your system. If you do not have Python or pip installed 
yet, you can find the installation instructions on the [official Python website](https://www.python.org/).

<br>

#### Minimal installation:

**Step 1**: Install Jupyter Notebook.

Open a command line on your computer. This could be the command prompt on a Windows PC, the terminal on a Mac, 
or the console on a Linux system.

```Bash
pip install notebook
```
**Step 2**: Start Jupyter Notebook

You can start Jupyter by entering the following command in your command line:

```Bash
jupyter notebook
```

In this case, a new tab will open in your web browser displaying the Jupyter interface.

**Step 3**: Download and open the Jupyter Notebook.

* Click on the following link to go to the page containing the Jupyter Notebook you wish to download: 
[Download our Notebook](https://github.com/digis-georoc/Georoc_jupyter/blob/main/Georoc_Notebook.ipynb)

* Once on the page, find the "Download raw file" button at the top right of Github and click on it.

* Start Jupyter or JupyterLab (as started in the previous steps). You should see a list of files located in the 
directory from which you started Jupyter or JupyterLab.

* Navigate to the directory where you saved the .ipynb file. You can do this by clicking on the folders in the 
file list to go to them.

* Click on the .ipynb file to open it.

* You should now be able to use the downloaded Jupyter Notebook locally on your computer. 

###### Hint: Please note that an API key from GEOROC is required to use our notebook. If you would like to request one, contact [DIGIS-Info](mailto:digis-info@uni-goettingen.de) directly.

[Back to table of contents](#table-of-contents)

<br>

#### Comprehensive Installation (Advanced User Interface):

**Step 1**: Install Jupyter and JupyterLab.

Open a command line on your computer. This could be the command prompt on a Windows PC, the terminal on a Mac or the 
console on a Linux system.

Type the following command to install Jupyter:

```Bash
pip install jupyter
```

Enter the following command to install JupyterLab:

```Bash
pip install jupyterlab
```

**Step 2**: Start Jupyter or JupyterLab

You can start Jupyter by entering the following command in your command line:

```Bash
jupyter notebook
```

You can start JupyterLab by entering the following command in your command line:

```Bash
jupyter lab
```

In both cases, a new tab will open in your web browser displaying the Jupyter interface.

**Step 3**: Download and open the Jupyter Notebook.

* Click on the following link to go to the page containing the Jupyter Notebook you wish to download: 
[Download our Notebook](https://github.com/digis-georoc/Georoc_jupyter/blob/main/Georoc_Notebook.ipynb)

* Once on the page, find the "Download raw file" button at the top right of Github and click on it.

* Start Jupyter or JupyterLab (as started in the previous steps). You should see a list of files located in the 
directory from which you started Jupyter or JupyterLab.

* Navigate to the directory where you saved the .ipynb file. You can do this by clicking on the folders in the file 
list to go to them.

* Click on the .ipynb file to open it.

* You should now be able to use the downloaded Jupyter Notebook locally on your computer. 

**Step 4**:

Remember that you will need to install additional Python packages that may be required by the particular Jupyter 
Notebook you are using.

You can do this in this case by using the **requirements.txt** file and using the packages listed in it on your 
command line to install them as follows:

```Bash
cd /to/your/path
```

Once you have reached the path where the **requirements.txt** file is located, you can install all the necessary 
packages as follows:

```Bash
pip install -r requirements.txt
```

<br>

If you have **Git** installed, you can clone the entire repository:

```Bash
cd /to/your/path
```

Now the whole command to clone our repository:

```Bash
git clone https://github.com/digis-georoc/Georoc_jupyter.git
```

If you are considering installing Git, you can visit the [official Git website](https://git-scm.com/) for more information.

###### Hint: Please note that an API key from GEOROC is required to use our notebook. If you would like to request one, contact [DIGIS-Info](mailto:digis-info@uni-goettingen.de) directly.

[Back to table of contents](#table-of-contents)

</span>

***

### Social:

[Visit official GEOROC website](https://georoc.eu/)

<a id="follow-button" class="btn" title="Follow @DIGISgeo on Twitter" href="https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fgeoroc.eu%2F&amp;ref_src=twsrc%5Etfw%7Ctwcamp%5Ebuttonembed%7Ctwterm%5Efollow%7Ctwgr%5EDIGISgeo&amp;region=follow_link&amp;screen_name=DIGISgeo"><i></i><span class="label" id="l">Follow <b>@DIGISgeo</b></span></a>

[Back to table of contents](#table-of-contents)

***

### Contribution

If you would like to participate in the DIGIS-GEOROC 2.0 project in a student or academic setting, 
please [email](mailto:digis-info@uni-goettingen.de) us directly or visit our university 
[job portal](#https://www.uni-goettingen.de/de/305223.html).

***

### References

<span style="text-align: justify; display: block; max-width: 850px; margin: 0 auto;">

[1] **Garcia, M. O., Muenow, D. W., Aggrey, K. E., and O'Neil, J. R. (1989)**, Major element, volatile, and stable isotope geochemistry of Hawaiian submarine tholeiitic glasses, J. Geophys. Res., 94(B8), 10525– 10538, http://doi.org/10.1029/JB094iB08p10525. 

[2] **requests** - Python HTTP library for humans. [Online]. Available: https://requests.readthedocs.io

[3] **json** - This is part of Python's standard library. Python Software Foundation. Python Language Reference, version 3.x. Available at http://www.python.org

[4] **pandas** - Wes McKinney. Data Structures for Statistical Computing in Python, Proceedings of the 9th Python in Science Conference, 51-56 (2010) [Online]. Available: https://pandas.pydata.org

[5] **geopandas** - GeoPandas developers. GeoPandas: Python tools for geographic data [Online]. Available: https://geopandas.org

[6] **seaborn** - Michael Waskom, Olga Botvinnik, Drew O’Kane, Paul Hobson, Joel Ostblom, Saulius Lukauskas, ... & Tom Augspurger. (2020, October 4). mwaskom/seaborn: v0.11.0 (Version v0.11.0). Zenodo. http://doi.org/10.5281/zenodo.4019147

[7] **matplotlib** - John D. Hunter. Matplotlib: A 2D Graphics Environment, Computing in Science & Engineering, 9, 90-95 (2007), DOI:10.1109/MCSE.2007.55

[8] **contextily** - Darribas, D., Arribas-Bel, D., Nshan, B., & van den Bosch, M. (2020). contextily: context geo-tiles in Python. Journal of Open Source Software, 5(55), 2302. https://doi.org/10.21105/joss.02302

[9] **adjustText** - Ilya Flyamer. (2016). adjustText: A small library for automatically adjusting text position in matplotlib plots to minimize overlaps. Zenodo. http://doi.org/10.5281/zenodo.4922517

[10] **ipywidgets** - Project Jupyter. (2017). ipywidgets: Interactive HTML widgets for Jupyter notebooks and the IPython kernel. Zenodo. https://doi.org/10.5281/zenodo.836874

[Back to table of contents](#table-of-contents)

### License

#### Attribution-ShareAlike 4.0 International

With this licence, you may use, modify and share the work as long as you credit the original author. However, you may 
not use it for commercial purposes, i.e. you may not make money from it. And if you make changes and share the new work, 
it must be shared under the same conditions.

[Back to table of contents](#table-of-contents)

</span>
