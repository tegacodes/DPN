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

* To get images, download the metadata of a collection from the gbif site.
* Create a folder called data on the same level as the python script. Save the multimedia.csv inside the data folder.  Update the python script with variables on how many images you want and what size you want to resize them too.

Run

```
python download.py
```

* Images will be saved in the images folder
* Thumbs will be saved in the thumbs folder
