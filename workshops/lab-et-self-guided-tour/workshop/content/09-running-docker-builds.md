Although the workshop environment is running inside of Kubernetes as a container, it is possible to enable the ability to perform container builds using ``docker`` or other tools such as ``pack``. This is done using Docker-in-Docker (dind).

```terminal:execute
command: (cd nginx-files; docker build -t my-nginx-server .)
```

The deployment of an image registry per session for use by the user can also be configured. The resulting images from the docker build can be tagged and pushed to the image registry.

```terminal:execute
command: |-
  docker tag {{registry_host}}/my-nginx-server:latest my-nginx-server
  docker push {{registry_host}}/my-nginx-server:latest
```

Kubernetes deployment resource definitions you are using can then be set up to use images from this image registry.

```editor:select-matching-text
file: ~/exercises/nginx-sample/deployment.yaml
text: "image: nginx:(.*)"
isRegex: true
group: 1
```

```editor:replace-text-selection
file: ~/exercises/nginx-sample/deployment.yaml
text: {{registry_host}}/my-nginx-server:latest
```

```terminal:execute
command: |-
  kubectl apply -f nginx-sample
  kubectl rollout status deployment/nginx
```

```terminal:execute
command: curl {{ingress_protocol}}://{{session_namespace}}-nginx-via-proxy.{{ingress_domain}}
```
