Coding Exercise: Simple OAuth2 HTTP Server - DevOps

## Tasks

*    Create a simple http server, using Python, Bash, or any scripting or programming language of your preference
*    Return HTTP 200 on endpoint `/token` when a client authenticates successfully using Client Credentials Grant with Basic Authentication (rfc6749)
*    Provide deployment manifests to deploy the server in a Kubernetes cluster
*    Make the service available outside the cluster

## Remarks

* Publish the exercise in a git server and grant us access to review it.
* Avoid a single commit with the whole solution to see how the solution was developed incrementally.
* Provide instructions to execute it


## Instructions

### Application

The source code is in the src directory, if you want to run it locally first you need to install Flask with "pip install flask".
and then run python3 server.py. The application will start listening on port 5000, if you want to try the app you can use the following curl command

```
curl -X POST -H "Authorization: Basic $(echo -n 'my_client_id:my_client_secret' | base64)" http://localhost:5000/token
```

### Deployment

To deploy the application, you will need a Kubernetes cluster and the configuration to use it in your kube config file.
All the manifests provided were tested in an AKS cluster.

To deploy the application first you need to deploy the namespace and then the service and deployment as follows:
```
cd manifests
kubectl apply -f namespace.yaml
kubectl apply -f ./
```
