In this workshop we have used a custom dashboard tab to embed the documentation for Educates.

```dashboard:open-dashboard
name: Docs
```

This was done by configuring the dashboard tab in the workshop definition. It is also possible to dynamically add custom dashboard tabs from the workshop instructions using a clickable action.

```dashboard:create-dashboard
name: External
url: https://www.example.com
```

This could be an existing external web site, or an application which you had a user deploy as part of the workshop instructions.

One requirement when doing this is that the web site doesn't enforce restrictions which would prevent it from being embedded in a browser iframe.

Further, the web site will not be able to be embedded if accessed using an insecure HTTP URL, and the Educates workshop is deployed using a secure HTTPS URL. In these cases you can open up a separate browser window/tab instead.

```dashboard:open-url
url: http://{{session_namespace}}-nginx.{{ingress_domain}}
```

In the case of accessing an application deployed as part of the workshop instructions within the same container as the workshop, or deployed to the Kubernetes cluster, the workshop definition can be configured to create a proxy to the application using a secure ingress when a secure ingress is being used for the workshop environment as a whole. When the proxy is used, access to the application will also be gated by the same security mechanism used to ensure only the owner of the workshop session can access the session.

```dashboard:create-dashboard
name: Internal
url: {{ingress_protocol}}://{{session_namespace}}-nginx-via-proxy.{{ingress_domain}}
```

For custom dashboards, when you are done with them you can have the user remove them as well.

```dashboard:delete-dashboard
name: Internal
```

```dashboard:delete-dashboard
name: External
```
