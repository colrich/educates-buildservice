In this workshop we have used a custom dashboard tab to embed the documentation for Educates.

```dashboard:open-dashboard
name: Docs
```

This was done by configuring the dashboard tab in the workshop definition. It is also possible to dynamically add custom dashboard tabs from the workshop instructions using a clickable action.

```dashboard:create-dashboard
name: Nginx
url: http://{{session_namespace}}-nginx.{{ingress_domain}}
```

This could be an existing external web site, or an application which you had a user deploy as part of the workshop instructions as in this case.

The only requirement is that the web site doesn't enforce restrictions which would prevent it from being embedded in a browser iframe. Many web sites with a requirement for a user to login will implement such a restriction, so in that case you will need to open up a separate browser window/tab.

```dashboard:open-url
url: http://{{session_namespace}}-nginx.{{ingress_domain}}
```

For custom dashboards, when you are done with it you can have the user remove it as well.

```dashboard:delete-dashboard
name: Nginx
```
