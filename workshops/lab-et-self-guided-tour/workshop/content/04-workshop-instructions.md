The workshop instructions provided with a workshop can be written using either Markdown or AsciiDoc formatting. Markdown works great for most workshops, but if you need a richer set of features for page formatting, AsciiDoc is the way to go.

Whichever document format you use, both support the ability to drop in custom HTML, including Javascript and stylesheets, for that extra bit of flexibility.

Although you can resort to custom HTML and Javascript, Educates does provide some of its own magic to help improve the experience for a user when working through workshop instructions. These are what are called clickable action blocks, with the most common a workshop is likely to use being one to indicate that a command should be executed by the workshop user in the terminal.

```terminal:execute
command: kubectl label namespace/{{session_namespace}} --list
```

In workshops, requiring a user to manually enter commands from the instructions, or even copy and paste them, can be quite error prone though.

As the name implies though, these actions are clickable.

If you haven't done so already, click anywhere on the outlined block and the command will be run for you automatically in the appropriate terminal.

In this case the command is listing the labels applied to the Kubernetes namespace resource for this workshop session. The correct namespace for this workshop session was queried because the workshop instructions can be filled out with details specific to the users session. This can be done within clickable actions or general text.

In addition to a clickable action for executing a command, for use with the terminals there are also actions for copying text, interrupting a running command, or clearing the terminal.
