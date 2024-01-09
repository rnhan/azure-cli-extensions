# Azure CLI ContainerStorage Extension #
This is an extension to Azure CLI to manage Container Storage resources.

## How to use ##
## Storage Pool
### Create a Storage Pool.
`az container-storage pool create -g {rg} ---pool-name {pool_name} --pool-type "{ephemeralDisk:{replicas:3}}" --resources "{requests:{storage:2048}}" -l eastus2`
### Delete a Storage Pool.
`az container-storage pool delete -g {rg} -n {pool_name}`
### Get a list of Storage Pools in a subscription.
`az container-storage pool list -g {rg}`
### Get a Storage Pool.
`az container-storage pool show -g {rg} -n {pool_name}`
### Update a Storage Pool.
`az container-storage pool update -n {pool_name} -g {rg} --set resources.requests.storage=4096 --tags "{key1710:bbbb}"`

## Volume
### Create a Volume.
`az container-storage pool volume create -g {rg} --pool-name {pool_name} -n {volume_name} --capacity-gi-b 2`
### Delete a Volume.
`az container-storage pool volume delete -g {rg} --pool-name {pool_name} -n {volume_name}`
### List Volumes.
`az container-storage pool volume list -g {rg} --pool-name {pool_name}`
### Get a Volume.
`az container-storage pool volume show -g {rg} --pool-name {pool_name} -n {volume_name}`
### Update a Volume.
`az container-storage pool volume update -g {rg}  --pool-name {pool_name}-n {volume_name} --set capacityGiB=3 --tags "{key2011:cccc}"`

## Volume Snapshot
### Create a Snapshot.
`az container-storage pool snapshot create -g {rg} --pool-name {pool_name} -n {snapshot_name} --source {volume_name}`
### Delete a Snapshot.
`az container-storage pool snapshot delete -g {rg} --pool-name {pool_name} -n {snapshot_name}`
### List Volumes in a Snapshot.
`az container-storage pool snapshot list -g {rg} --pool-name {pool_name}`
### Get a Snapshot.
`az container-storage pool snapshot show -g {rg} --pool-name {pool_name} -n {snapshot_name}`
### Update a Snapshot.
`az container-storage pool snapshot update -g {rg} --pool-name {pool_name} -n {snapshot_name} --tags "{key2011:cccc}"`
