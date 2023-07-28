# HTTP Web API for Neural Network Model Utilization

## Create the environment

### Clone the repository

Clone the repository:

```bash
git clone https://github.com/zhukovanadezhda/web-api.git
cd web-api
```
### Setup the conda environment

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html). Create the `web-api` conda environment:

```bash
conda env create -f binder/environment.yml
```

### Load the environment

```bash
conda activate web-api
```

## Use the API

The API can be used either via Postman or via a Shell script:

### To run from a Shell script:
Run this line:
```bash
./scripts/call_api.sh <path_to_xml_file>
```
The model prediction will be saved in ```output.json``` file.


### To run from Postman:
First, run this line:
```bash
python scripts/app.py
```
Then go to Postman and follow the steps:
1. Put "http://localhost:5000" as a URL
2. Change the method to POST
3. Click ```Body``` -> ```form-data```
   Choose "file" as a key and select "File" as a type of the key.
   Select your .xml file for the value.
4. Click ```Send``` and enjoy the results.
5. To download the results click ```Save Response``` on the right.
   
