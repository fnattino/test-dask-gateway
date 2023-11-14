#!/bin/bash


source ~/mambaforge/bin/activate ~/mambaforge/envs/dask-gateway


dask-gateway-server -f dask_gateway_config.py 
