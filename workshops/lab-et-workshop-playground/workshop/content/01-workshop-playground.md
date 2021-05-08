This workshop environment provides a gateway to a playground where you can work on your own workshop content using one of the available workshop base images.

If you are not familiar with how to use the workshop playground skip to the bottom of this page and run through the workshop explaining its usage.

If you do know how to use the workshop playground, the command to use for bundling and pushing up workshop content to the registry for this workshop session is:

{% if ingress_protocol == 'https' %}

```workshop:copy
text: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} -f .
```
{% else %}

```workshop:copy
text: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} --registry-insecure -f .
```

{% endif %}

The portal for the actual workshop playground can be found at:

```dashboard:open-url
url: {{ingress_protocol}}://{{session_namespace}}-labs.{{ingress_domain}}
```

The password for accessing the portal is:

```workshop:copy
text: {{registry_password}}
```

Remember that you need to keep this browser page open and cannot close it otherwise the workshop playground will be removed automatically after a period of time. You will need to extend the session for this workshop environment if time starts to run out. This can be done by clicking on the countdown timer when it turns red.

If none of that made any sense, then continue on to the next page to start the workshop to learn how to use the workshop playground.
