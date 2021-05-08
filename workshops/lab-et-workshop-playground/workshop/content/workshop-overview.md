```terminal:execute
command: git clone https://github.com/eduk8s/lab-markdown-sample.git
```

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest -f lab-markdown-sample
```

```dashboard:open-url
url: {{ingress_protocol}}://{{session_namespace}}-labs.{{ingress_domain}}
```
