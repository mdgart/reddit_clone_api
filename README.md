# Majestc ETL Framework #


## Requirements ##

* Python >=3.4.#
* PostgreSQL >=9.#


## Build the environment ##

### Install PIP and Virtualenv ###

[Installing packages](https://packaging.python.org/tutorials/installing-packages/)

### Create a virtual environment with python3 ###
You will only run `virtualenv` once. It sets up a persistent environment running a sandboxed version of python and its packages. Run this from the top directory of the project:

`> virtualenv -p python3 env`


### Activate the virtual environment ###

You will run the following command every time you enter a terminal to work within this project. It will load your python environment. Run this from the top directory of the project:

`> source env/bin/activate`

### Install all necessary python packages into your virtual environment ###

You will only need to run this command once. It will be saved as part of your virtualenv environment.

`> pip install -r requirements.txt`


## Run the app ##

`> ./run`

## Run the shell (repl) ##

`> ./shell`

## Setup Env Valiables for Development

`> source init`


## Database Migration

`> source init`
`> flask db upgrade`
