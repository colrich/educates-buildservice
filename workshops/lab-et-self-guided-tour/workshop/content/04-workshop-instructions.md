The workshop instructions provided with a workshop can be written using either Markdown or AsciiDoc formatting. Markdown works great for most workshops, but if you need a richer set of features for page formatting, AsciiDoc is the way to go.

Which ever document format you use, both support the ability to drop in custom HTML, including Javascript and stylesheets, for that extra bit of flexibility.

Although you can resort to custom HTML and Javascript, Educates also provides some of its own magic to help improve the experience for a user when working through workshop instructions. These are what are called clickable actions, with the most common a workshop is likely to be used being one to execute a command in the terminal.

```terminal:execute
command: kubectl get namespace/{{session_namespace}} -o yaml
```
