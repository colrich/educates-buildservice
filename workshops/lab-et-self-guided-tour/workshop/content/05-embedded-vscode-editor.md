Editors ``vi`` and ``nano`` are provided for working from the terminal, however not everyone will be familiar with using these editors. For that reason a GUI based IDE usually provides a better experience for workshops as you don't have to worry so much about the users experience level.

The embedded IDE which can be enabled for the workshop environments is VS Code. This runs in the same container as the workshop session uses. This is available under the "Editor" tab, or you can provide a clickable action to expose the editor.

```dashboard:open-dashboard
name: Editor
```

To avoid having to provide explicit instructions to a workshop user for how to view, create or edit files, with users cut and pasting content from instructions, a range of clickable actions are provided which can act directly on the VS Code editor.

Actions include being able to open a file:

```editor:open-file
file: ~/exercises/nginx-sample/deployment.yaml
```

Highlighting specific sections of a file when explaining contents or how to make modifications:

```editor:select-matching-text
file: ~/exercises/nginx-sample/deployment.yaml
text: "image: nginx:1.20.0"
```

For YAML files, it is even possible to effect updates to the file:

```editor:insert-value-into-yaml
file: ~/exercises/nginx-sample/deployment.yaml
path: spec.template.spec.containers
value:
- name: nginx
    image: nginx:1.20.0-alpine
```
