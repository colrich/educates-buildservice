This workshop environment provides a gateway to a playground where you can work on your own workshop content using a designated workshop base image.

If you are not familiar with how to use the workshop playground click on "Explore Playground" at the bottom of this page and run through the workshop explaining its usage.

If you are familiar with how to use the workshop playground click below to reveal the command for packaging up workshop content and details for accessing the playground.

```section:begin
prefix: Playground
title: Command Summary
```

The command to use for bundling and pushing up workshop content to the registry for this workshop playground is:

{% if ingress_protocol == 'https' %}

```workshop:copy
text: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} -f .
```
{% else %}

```workshop:copy
text: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} --registry-insecure -f .
```

{% endif %}

The portal for the workshop playground can be accessed at:

```dashboard:open-url
url: {{ingress_protocol}}://{{session_namespace}}-playground.{{ingress_domain}}
```

The password for the portal giving access to the workshop playground is:

```workshop:copy
text: {{registry_password}}
```

Remember that you need to keep this browser page open and cannot close it otherwise the workshop playground will be removed automatically after a period of time. You will need to extend the session for this workshop environment if time starts to run out. This can be done by clicking on the countdown timer when it turns red.

```section:end
```
