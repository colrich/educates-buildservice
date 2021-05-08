The process of working on content within the playground then becomes:

* Make modifications to workshop content.
* Upload the workshop content to the playground registry using ``imgpkg``.
* Terminate the existing playground workshop session if still running.
* Start a new playground workshop session.

You would cycle through this process until you are happy with the changes, then committing your changes back to your source code repository.

Each time you go through this cycle the existing workshop session is terminated and a new one created with the updated version of the workshop content.

When making minor edits to fix the instructions and you only want to re-test that part of the instructions, rather that tear down the whole workshop session and create a new one, you can refresh the workshop content within the existing running workshop session.

To show how this is done, open up the editor here in the workshop session and open the first page of the workshop.

```editor:open-file
path: ~/exercises/lab-markdown-sample/workshop/content/workshop-overview.md
```

Append to this file an additional paragraph and ensure the change is saved.

```editor:append-to-file
path: ~/exercises/lab-markdown-sample/workshop/content/workshop-overview.md
text: |
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
  eget auctor purus, ac pellentesque magna. In laoreet et quam quis
  viverra. Praesent venenatis lacus eget leo elementum venenatis.
  Etiam vel venenatis sem, a molestie lorem.
```

Upload the modified workshop content to the playground registry.

{% if ingress_protocol == 'http' %}

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} --registry-insecure -f .
```

{% else %}

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} -f .
```

{% endif %}

Now head back over to the window for the playground workshop session.

Rather than terminating the workshop session, this time at the terminal prompt run:

```workshop:copy
text: update-workshop
```

Refresh the browser window for the workshop session and you should see the additional paragraph of text.

Doing an in place update on the workshop content in this way means that if the workshop involves having to deploy an application to the Kubernetes cluster, that you don't have to go through all the prior steps again. Depending on what you are re-testing, you may need to manually undo the result of previously running the same step. This is something you will need to work out depending on what your workshop is about. If you can't you would need to terminate the workshop session and start over.

Note that using ``update-workshop`` will not always alone be enough, such as if new pages of instructions were added, or pages were renamed. In this case you will need to restart the workshop renderer so that it can re-read the configuration about what pages there are. To handle this case you will also need to run ``restart-workshop``, then refresh the page.

For more details on using these and others scripts you can use when working on workshop content in a live workshop session, see:

* https://docs.edukates.io/en/latest/workshop-content/working-on-content.html

