```terminal:execute
command: git clone https://github.com/eduk8s/lab-markdown-sample.git
```

{% if ingress_protocol == 'http' %}

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest -f lab-markdown-sample --registry-username={{registry_username}} --registry-password={{registry_password}} --registry-insecure
```

{% else %}

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest -f lab-markdown-sample --registry-username={{registry_username}} --registry-password={{registry_password}}
```

{% endif %}

```dashboard:open-url
url: {{ingress_protocol}}://{{session_namespace}}-labs.{{ingress_domain}}
```
