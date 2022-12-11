



# Step 1. Add current path

```sh
export PYTHONPATH="${PYTHONPATH}:{your_path}/new"
```

# Step 2. 

    The access key in json must be placed in the folder 
    ,"gcloud_key" before implementing the code. Double check the IAM polcy has granted the assigned account to access and use all the storage services without any restriction. The key will be automatically mounted to our airflowdocker conatiner that enables us to store and read data.

```
|-gcloud_key
   |-{your cloud access_key name}.json

```

# 3. Creating a new docker image for airflow

To run requirement.txt, we need to create a new docker image. 
Open Dockerfile to check and modify the contents at your disposal. 
Now,we have a new created image named "customising_airflow:latest".


```sh
docker build . --build-arg AIRFLOW_VERSION='2.0.3' --tag customising_airflow:latest
```


After successfully creating the docker image, make a small modification to our docker-compose file. 

```yaml

 &airflow-common
  image: ${AIRFLOW_IMAGE_NAME:-customising_airflow:latest}
  
```




# 3.run docker-compose

```sh
docker-compose up airflow-init
docker-compose up -d
```


