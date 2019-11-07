# Download Images from GBIF

## Installation

2. Clone this repo

3. Create a virtualenvironment inside the gbif folder

```
virtualenv env
source env/bin/activate
```

4. Install requirements

```
pip install -r requirements.txt
```

## Usage

* To get images, download the metadata of a collection from the gbif site. For example download the data from the link at the API endpoint at the bottom of this page:
[https://www.gbif.org/dataset/34f8683a-dfc0-46b8-acf6-390fe5ca6b92](https://www.gbif.org/dataset/34f8683a-dfc0-46b8-acf6-390fe5ca6b92)
* Create a folder called data on the same level as the python script. Save the multimedia.csv inside the data folder.  Update the python script with variables on how many images you want and what size you want to resize them too.

Run

```
python download.py
```

* Images will be saved in the images folder
* Thumbs will be saved in the thumbs folder
* There is a function in there to rename files too
