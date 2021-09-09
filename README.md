# Immuni metrics uploader

Immuni app metrics uploader for [dashboard](https://www.immuni.italia.it/dashboard.html).
This is an internal tool to exchange data with the dashboard generation pipeline. 

## Install dependencies

```
poetry install
```

## Run

- Create a folder `metrics` where to put csv files taken from Apple Store and Google Play.

- Set env variables to support 🇮🇹 language.

```
export LANG=it_IT.UTF-8
export LC_ALL=it_IT.UTF-8
```

- Run cron

```
cd app
poetry run huey_consumer.py tasks.huey
```

Processed metrics can be found inside `metrics_processed` folder

## Set up Google Drive

This app is able to exchange data using Google Drive and it needs `client_secrets.json`
file stored inside `app` folder ([Using Google API for Python- where do I get the client_secrets.json file from?](https://stackoverflow.com/questions/40136699/using-google-api-for-python-where-do-i-get-the-client-secrets-json-file-from))

```
export GDRIVE_PARENT_FOLDER_ID='Y0URP4R3NTF0LD3R1D'
```

⚠️ Note that if you use Google Drive integration, uploaded file will be removed
from `metrics_processed`.
