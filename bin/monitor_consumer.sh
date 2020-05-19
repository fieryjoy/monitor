#!/bin/bash
set -e
set -u

cli.py --service-uri ${KAFKA_URI} --ca-path ${CA_PATH} --cert-path ${SERVICE_PATH} --key-path ${KEY_PATH} --consumer --db-uri ${DB_URI}