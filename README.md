# MSiA423 Project Repositiory
## MBTI Assessment App
### By Srividya Ganapathi
### QA - Bhavya Kaushik

<!-- toc -->
- [Project Charter](#Project-Charter)
- [Sprint Plan](#Sprint-Planning)
- [Backlog](#Backlog)
- [Icebox](#Icebox)
- [Running the application](#running-the-application)
  * [1. Initial setup](#1-initial-setup)
  * [2. Set up environment](#2-set-up-environment)
  * [3. Download the data](#3-download-the-data)
  * [4. Initialize the database](#4-initialize-the-database)
  
- [Logging](#logging)



## Project Charter
<!-- toc -->
### Vision 
The Myers Briggs Type Indicator (or MBTI for short) is a popular personality test that divides everyone into 16 distinct personality types. Companies use it to analyze job applicants, managers use it to determine which employees might get along with one another, and your friends might use it to tell the world what kind of person they are.
The objective of this project is to identify the personality and characteristics of a user as indicated by the MBTI test using patterns in the user's chosen statements or writing styles.

### Mission
The MBTI test is used in various domains like business, medicine and others everyday but recently, the validity of the test has been questioned because of unreliability in experiments surrounding it, along with other reasons. But it has still proven to be a very useful tool in a lot of areas, and the purpose of this dataset [https://www.kaggle.com/datasnaek/mbti-type] is to help see if any patterns can be detected in specific types and style of writing of people and if these patterns are indicative of a person's personality. A machine learning predictive model will be developed to classify a user into a personality type. The model will be hosted and a web application interface will be created for the users. This overall explores the validity of the test in analysing, predicting or categorising behaviour. 

### Content
This dataset contains over 8600 rows of data, on each row is a person’s:
 - Type (This persons 4 letter MBTI code/type)
 - A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))

### Success Criteria
- The success criterion for the model performance evaluation would be the classification accuracy.
In such psychological tests, even an accuracy of 50% is acceptable for the tool to be relied upon. The app will take feedback on whether it was right or wrong which will also be used to test accuracy.  
- The business outcome will be measured by the perusal of the app by third parties or business stakeholders to delve deeper into an individual's personality using their social media activity.
- User engagement and agreement with their personality assessment is also a success criterion.

<!-- toc -->


## Sprint Planning
For the next 4 sprints (Each sprint of 2 weeks) the Initiatives are:

### Initiative 1: Models to extract writing styles and patterns associated with each MBTI type.

#### Epic-1: Exploratory Data Analysis and preprocessing.
   - Story 1: EDA of the Data
   - Story 2: Apply different embeddings to the data (Count vectorizer, word2vec, GloVe etc.)
     
#### Epic-2: Comparison of models 
   - Story 1: Build models like regression, random forest, LSTM, KNN etc. under cross validation to identify the best model.

### Initiative 2: Develop the front and back ends of the model

#### Epic-1: Build the front end Flask app
   - Story 1: Create the first page layout
   - Story 2: Design the user input layer
   - Story 3: Set connections to the backend servers
     
#### Epic-2: Set up the cloud server for the data using AWS RDS and S3

#### Epic-3: Performing sanity check using test cases

### Initiative 3 : Model to predict the MBTI type from selected statements
#### Epic-1: Curate statements for the user to choose from
   - Story 1: Map sets of statements corresponding to each personality type.
   - Story 2: Set connections to the backend servers
   
#### Epic-2: Predict personality type
   - Story 1: Create a new dataset of the statements selected by the user 
   - Story 2: Predict the personality based on the selected statements.
   
### Initiative 4 : Fine tuning the model to increase accuracy 

#### Epic-1: Accuracy Check 
   - Story 1: Receive the actual MBTI Type from the user as input
   - Story 2: Append this to the record of the current user.
   - Story 3: For every few use cases append the record to the train data.

#### Epic-2: Finetuning the model
  - Story 1: Penalize the statements that led to a misclassification.
  - Story 2: Retrain the model to increase accuracy.
  
## Backlog

The story points are assigned as follows:
-   0 points - quick chore
-   1 point ~ 1 hour (small)
-   2 points ~ 1/2 day (medium)
-   4 points ~ 1 day (large)
-   8 points - big and needs to be broken down more when it comes to execution 


1. Initiative1.Epic1.Story1  (4) [Planned]
2. Initiative1.Epic1.Story2  (4) [Planned]
3. Initiative1.Epic2.Story1  (8) [Planned]
4. Initiative2.Epic1.Story1  (8) [Planned]
5. Initiative2.Epic1.Story2  (2) [Planned]
6. Initiative2.Epic1.Story3  (2) [Planned]
7. Initiative2.Epic2         (1) [Planned]
8. Initiative2.Epic3         (2) [Planned]
9. Initiative3.Epic1.Story1  (2) [Planned]
10. Initiative3.Epic1.Story2 (2) [Planned]
11. Initiative3.Epic2.Story1 (8) [Planned]
12. Initiative3.Epic2.Story2 (1) [Planned]


## Icebox

* Initiative4          



## Running the application

### 1. Initial Setup

To run the app, ensure to go through the following:
* Docker desktop should be running
* Set up AWS CLI. Kindly refer to this [link](https://www.kaggle.com/datasnaek/mbti-type/download).
* Set the following environment variables with the following commands in command line:
```bash
    export AWS_KEY_ID=""
    export AWS_ACCESS_KEY=""
    export AWS_DEFAULT_REGION=""
```


### 2. Download the data

Original Data Source: [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

For the ease of downloading, the raw data has been downloaded and placed in the **data/raw** folder. 


### 3. Upload to AWS
Input the following in the load_data dictionary of the config/config.yml:
- SOURCE_BUCKET - Name of the S3 bucket where the data has to be uploaded.
- local_location - Location of the data in local system. (In this case - data/raw/mbti_1.csv)

#### Docker Image
Build the docker image with the following command in command line:
```bash
docker build -t mbti .
```
Run the docker image with the aws credentials using the following command in command line. Note that the data will be uploaded to a dump folder that will be created in the s3 bucket.
```bash
docker run -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION  mbti
```
The data sould be successfully uploaded to your s3 bucket.


### 4. Initialize the database

#### Local
Input the following in the db_config dictionary of the config/config.yml:
- SQLALCHEMY_DATABASE_URL - "sqlite:///<location>/<name_of_database>.db"
In this case, running the following code in command line will create a sqlite database of the mbti data at: **data/msia423.db**
 
```bash
 docker run --mount type=bind,source="$(pwd)"/data,target=/app/data mbti
```

#### AWS
Set the following environment variables with the following commands in command line:
```bash
    export MYSQL_USER=""
    export MYSQL_PASSWORD=""
```
Input the following in the rds dictionary of the config/config.yml:
- SQLALCHEMY_DATABASE_URL - "sqlite:///<location>/<name_of_database>.db"
- MYSQL_HOST - <Host_Name_of_RDS_Instance>
  MYSQL_PORT - 3306
  MYSQL_DB - <Name of an existing database>, here - msia423_db
 
Run the following command in command line:
```bash
docker run -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION -e MYSQL_USER=$MYSQL_USER -e MYSQL_PASSWORD=$MYSQL_PASSWORD mbti
```

Running this code will create the database specified in the given RDS instance.



----------------------------------------------------------------------------------------------------------------------------------------




- [Directory structure](#directory-structure)
- [Running the app](#running-the-app)
  * [1. Initialize the database](#1-initialize-the-database)
    + [Create the database with a single song](#create-the-database-with-a-single-song)
    + [Adding additional songs](#adding-additional-songs)
    + [Defining your engine string](#defining-your-engine-string)
      - [Local SQLite database](#local-sqlite-database)
  * [2. Configure Flask app](#2-configure-flask-app)
  * [3. Run the Flask app](#3-run-the-flask-app)
- [Running the app in Docker](#running-the-app-in-docker)
  * [1. Build the image](#1-build-the-image)
  * [2. Run the container](#2-run-the-container)
  * [3. Kill the container](#3-kill-the-container)

<!-- tocstop -->

## Directory structure 

```
├── README.md                         <- You are here
├── api
│   ├── static/                       <- CSS, JS files that remain static
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│   ├── boot.sh                       <- Start up script for launching app in Docker container.
│   ├── Dockerfile                    <- Dockerfile for building image to run app  
│
├── config                            <- Directory for configuration files 
│   ├── local/                        <- Directory for keeping environment variables and other local configurations that *do not sync** to Github 
│   ├── logging/                      <- Configuration of python loggers
│   ├── flaskconfig.py                <- Configurations for Flask API 
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git. 
│   ├── external/                     <- External data sources, usually reference data,  will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── deliverables/                     <- Any white papers, presentations, final work products that are presented or delivered to a stakeholder 
│
├── docs/                             <- Sphinx documentation based on Python docstrings. Optional for this project. 
│
├── figures/                          <- Generated graphics and figures to be used in reporting, documentation, etc
│
├── models/                           <- Trained model objects (TMOs), model predictions, and/or model summaries
│
├── notebooks/
│   ├── archive/                      <- Develop notebooks no longer being used.
│   ├── deliver/                      <- Notebooks shared with others / in final state
│   ├── develop/                      <- Current notebooks being used in development.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports, helper functions, and SQLAlchemy setup. 
│
├── reference/                        <- Any reference material relevant to the project
│
├── src/                              <- Source data for the project 
│
├── test/                             <- Files necessary for running model tests (see documentation below) 
│
├── app.py                            <- Flask wrapper for running the model 
├── run.py                            <- Simplifies the execution of one or more of the src scripts  
├── requirements.txt                  <- Python package dependencies 
```

## Running the app
### 1. Initialize the database 

#### Create the database with a single song 
To create the database in the location configured in `config.py` with one initial song, run: 

`python run.py create_db --engine_string=<engine_string> --artist=<ARTIST> --title=<TITLE> --album=<ALBUM>`

By default, `python run.py create_db` creates a database at `sqlite:///data/tracks.db` with the initial song *Radar* by Britney spears. 
#### Adding additional songs 
To add an additional song:

`python run.py ingest --engine_string=<engine_string> --artist=<ARTIST> --title=<TITLE> --album=<ALBUM>`

By default, `python run.py ingest` adds *Minor Cause* by Emancipator to the SQLite database located in `sqlite:///data/tracks.db`.

#### Defining your engine string 
A SQLAlchemy database connection is defined by a string with the following format:

`dialect+driver://username:password@host:port/database`

The `+dialect` is optional and if not provided, a default is used. For a more detailed description of what `dialect` and `driver` are and how a connection is made, you can see the documentation [here](https://docs.sqlalchemy.org/en/13/core/engines.html). We will cover SQLAlchemy and connection strings in the SQLAlchemy lab session on 
##### Local SQLite database 

A local SQLite database can be created for development and local testing. It does not require a username or password and replaces the host and port with the path to the database file: 

```python
engine_string='sqlite:///data/tracks.db'

```

The three `///` denote that it is a relative path to where the code is being run (which is from the root of this directory).

You can also define the absolute path with four `////`, for example:

```python
engine_string = 'sqlite://///Users/cmawer/Repos/2020-MSIA423-template-repository/data/tracks.db'
```


### 2. Configure Flask app 

`config/flaskconfig.py` holds the configurations for the Flask app. It includes the following configurations:

```python
DEBUG = True  # Keep True for debugging, change to False when moving to production 
LOGGING_CONFIG = "config/logging/local.conf"  # Path to file that configures Python logger
HOST = "0.0.0.0" # the host that is running the app. 0.0.0.0 when running locally 
PORT = 5000  # What port to expose app on. Must be the same as the port exposed in app/Dockerfile 
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/tracks.db'  # URI (engine string) for database that contains tracks
APP_NAME = "penny-lane"
SQLALCHEMY_TRACK_MODIFICATIONS = True 
SQLALCHEMY_ECHO = False  # If true, SQL for queries made will be printed
MAX_ROWS_SHOW = 100 # Limits the number of rows returned from the database 
```

### 3. Run the Flask app 

To run the Flask app, run: 

```bash
python app.py
```

You should now be able to access the app at http://0.0.0.0:5000/ in your browser.

## Running the app in Docker 

### 1. Build the image 

The Dockerfile for running the flask app is in the `app/` folder. To build the image, run from this directory (the root of the repo): 

```bash
 docker build -f app/Dockerfile -t pennylane .
```

This command builds the Docker image, with the tag `pennylane`, based on the instructions in `app/Dockerfile` and the files existing in this directory.
 
### 2. Run the container 

To run the app, run from this directory: 

```bash
docker run -p 5000:5000 --name test pennylane
```
You should now be able to access the app at http://0.0.0.0:5000/ in your browser.

This command runs the `pennylane` image as a container named `test` and forwards the port 5000 from container to your laptop so that you can access the flask app exposed through that port. 

If `PORT` in `config/flaskconfig.py` is changed, this port should be changed accordingly (as should the `EXPOSE 5000` line in `app/Dockerfile`)

### 3. Kill the container 

Once finished with the app, you will need to kill the container. To do so: 

```bash
docker kill test 
```

where `test` is the name given in the `docker run` command.
