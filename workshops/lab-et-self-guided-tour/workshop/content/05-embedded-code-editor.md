Editors ``vi`` and ``nano`` are provided for working from the terminal, however not everyone will be familiar with using these editors. For that reason a GUI based IDE usually provides a better experience for workshops as you don't have to worry so much about the users experience level.

The embedded IDE which can be enabled for the workshop environments is VS Code. This runs in the same container that the workshop session uses and is available under the "Editor" tab, or you can provide a clickable action to expose the tab.

```dashboard:open-dashboard
name: Editor
```

In order to help guide users when viewing, creating or editing files, a range of clickable actions are provided which can act directly on the VS Code editor.

Actions include being able to open a file:

```editor:open-file
file: ~/exercises/nginx-sample/deployment.yaml
```

Selecting a specific section of a file when explaining contents or where a user needs to make modifications:

```editor:select-matching-text
file: ~/exercises/nginx-sample/deployment.yaml
text: "image: (nginx:.*)"
isRegex: true
group: 1
```

Modify the selected region of a file:

```editor:replace-text-selection
file: ~/exercises/nginx-sample/deployment.yaml
text: nginx:1.20.0-alpine
```

Or creating a new file with contents from the workshop instructions:

```editor:append-lines-to-file
file: ~/exercises/nginx-sample/ingress.yaml
text: |
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: nginx
    labels:
        app: nginx
  spec:
    rules:
    - host: {{session_namespace}}-nginx.{{ingress_domain}}
      http:
        paths:
        - path: "/"
          pathType: Prefix
          backend:
            service:
              name: nginx
              port:
                number: 80
```
