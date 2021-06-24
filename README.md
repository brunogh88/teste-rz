# Quick Start

> All commands below are using docker containers

### Testing

```bash
docker-compose exec cluster tox
```

### Generating Dist

The `dist` is the directory that contains the package to be deployed.

```bash
docker-compose exec cluster tox -e gen_dist
```


### Running Locally

#### Scripts

```bash
docker-compose exec cluster ./scripts/pipe-run-local.sh 20210612 SALES_OIL_DERIVATIVE_FUELS
```

#### Project

> **Here we have two ways to execute the project...**  
> _1 - Project Root_  
> While executing the project from project root location all changes you make in the code are going to be applied
> automatically in the next execution.  
> _2 - Dist_  
> While using the files generated from "dist" your execution will be very similar to a cluster execution.   
> To make it possible you must [generate the "dist" folder](#generating-dist) before executing or after every new code
> change.

##### Help

**Executing from project root location**

```bash
docker-compose exec cluster spark-submit main.py -h
```

**Executing from dist**

```bash
docker-compose exec cluster spark-submit \
  --py-files dist/src.zip \
  dist/main.py -h
```

##### Execution Examples
```bash
# Example 01 - to run pipe is necessary have file in folder /data/RAW/{pipe name}/{date processing}
#Pipes avaliable: SALES_OIL_DERIVATIVE_FUELS and SALES_DISEL  
docker-compose exec cluster spark-submit main.py \
    --pipe SALES_OIL_DERIVATIVE_FUELS --date 20210612
```

```bash
docker-compose exec cluster spark-submit \
  --master local[2] \
  --files "/opt/spark/conf/log4j.properties" \
  --py-files "dist/src.zip" \
  "/opt/app/main.py" --date 20210612 --pipe SALES_OIL_DERIVATIVE_FUELS
```


## Dev Environment

You can use the docker image, that was created to be the developer environment, like this...

```bash
docker-compose up -d  # Build and up the docker container
docker-compose down   # When you finish using, just clean everything up
```

Or you can configure everything on your own machine.

- [Docker](https://www.docker.com/products/docker-desktop)
- [Java 8](https://www.java.com/pt_BR/download/)
- [Maven 3.6.1](https://www.mkyong.com/maven/how-to-install-maven-in-windows/)
- [Python 2.7 and 3](https://www.python.org/)

### Project Lombok Plugin

### Hadoop

> **⚠️ Windows Only**

1. Download [winutils.exe](https://github.com/kontext-tech/winutils) file.
2. Add to `C:\hadoop\bin` path.
3. Create an environment variable called `HADOOP_HOME` with `c:\hadoop` (without `\bin`) as value.
4. Finally, add the `%HADOOP_HOME%\bin` path to `PATH` environment variable.

---