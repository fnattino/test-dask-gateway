
# Configure the gateway to use SLURM
c.DaskGateway.backend_class = (
    "dask_gateway_server.backends.jobqueue.slurm.SlurmBackend"
)
c.DaskGateway.log_level = 'DEBUG'

# Activate a local conda environment before startup
c.SlurmClusterConfig.scheduler_setup = "source ~/mambaforge/bin/activate ~/mambaforge/envs/dask"
c.SlurmClusterConfig.worker_setup = "source ~/mambaforge/bin/activate ~/mambaforge/envs/dask"

# Configuration of the proxy is needed in order to reach the 
c.Proxy.address = 'ui-02:8000'

# System specific
c.SlurmClusterConfig.partition = 'normal'
c.SlurmClusterConfig.scheduler_cores = 1
c.SlurmClusterConfig.scheduler_memory = '8 G'
c.SlurmClusterConfig.cluster_max_workers = 5
c.SlurmClusterConfig.worker_cores = 4
c.SlurmClusterConfig.worker_memory = '30 G'

# Increase startup timeouts to 1000 seconds each
c.SlurmBackend.cluster_config_class = 'dask_gateway_server.backends.jobqueue.slurm.SlurmClusterConfig'
c.SlurmBackend.cluster_start_timeout = 1000
c.SlurmBackend.worker_start_timeout = 1000
c.SlurmBackend.cluster_heartbeat_timeout = 600

# Parameter introduced to disable sudo-ing
c.JobQueueBackend.can_sudo = False

