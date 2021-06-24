#!/bin/bash -xe
# @script  extract-run-local.sh
#
# @description
# Script to execute "Test Raizen" collector.
#
# @params
# 01 - Date (yyyyMMdd)
# 02 - Pipe (Pipe name)
#
# @usage
# ./pipe-run-local.sh --date [date process] --pipe [pipe name]

spark2-submit \
  --master local[2] \
  --files "/opt/spark/conf/log4j.properties" \
  --conf "spark.yarn.maxAppAttempts=1" \
  --py-files "dist/src.zip" \
  "/opt/app/main.py" --date $1 --pipe $2
