# HTTP Web API for Neural Network Model Utilization

This repository contains an HTTP Web API without a graphical interface, which provides access to a pretrained neural network. The neural network is stored in a single HDF5 file, which includes both the network's architecture and its optimized weights.

The API is developed using Flask and offers a single path that allows users to send data for processing through the neural network. The data is expected to be submitted in the form of an XML file, where each data object comprises matrices of decimal values (5000 values per object) separated by commas. The API extracts these matrices and forwards them to the pretrained model for prediction. The results generated by the model are then returned to the user in a JSON format.

Users can interact with this API by utilizing tools such as Postman or any other HTTP client to send their XML files and receive predictions from the neural network.

## Create the environment

### Clone the repository

```bash
git clone git@github.com:zhukovanadezhda/web-api.git
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

The API can be used via [Postman](https://www.postman.com/downloads/) HTTP client.

First, run this line:
```bash
python scripts/app.py
```
Then go to Postman and follow the steps:
1. Put "http://localhost:5000" as a URL
2. Change the method to POST
3. Click `Body` -> `form-data` <br>
   Choose `file` as a key and select `File` as a type of the key.
   Select your .xml file for the value.
4. Click `Send` and enjoy the results.
5. To download the results click `Save Response` on the right.
   
