#!/bin/bash -xe
# @script  extract-run-yarn.sh
#
# @description
# Script to execute "Test Raizen" collector.
#
# @params
# 01 - Date (yyyyMMdd)
# 02 - Pipe (Pipe name)
#
# @usage
# ./pipe-run-yarn.sh --date [date process] --pipe [pipe name]

spark2-submit \
  --master yarn \
  --deploy-mode cluster \
  --name "test-raizen" \
  --files "/opt/spark/conf/log4j.properties" \
  --conf "spark.driver.extraJavaOptions=-Dlog4j.configuration=file:log4j.properties" \
  --conf "spark.executor.extraJavaOptions=-Dlog4j.configuration=file:log4j.properties" \
  --conf "spark.yarn.maxAppAttempts=1" \
  "/opt/app/src/main.py" "--date $1 --pipe $2"
