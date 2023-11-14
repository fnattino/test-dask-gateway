# Run Dask Gateway on Spider

Create environment for the server and for the client (here we keep them separate, but they might be the same):

```shell
# server environment 
mamba env create -f environment_server.yaml
# client environment 
mamba env create -f environment.yaml 
```

We make use of [a modified version](https://github.com/fnattino/dask-gateway/tree/run-as-user) of `dask-gateway-server`, which allows one to run as a user withoud sudo privileges.

Start the server as:

```shell
bash dask_gateway_start.sh
```

Activate the client environment:
```shell
mamba activate dask
```

Create a client connection and instantiate a new cluster:

```python
from dask_gateway import Gateway 

gateway = Gateway('http://ui-02:8000')

gateway.list_clusters()
# []

cluster = gateway.new_cluster()
cluster
# GatewayCluster<141c70529f974acea8d52c9eaab4a6c0, status=running>

cluster.scale(2)

client = cluster.get_client()
client
# <Client: 'tls://10.0.0.52:38723' processes=2 threads=8, memory=60.00 GiB> 
```
