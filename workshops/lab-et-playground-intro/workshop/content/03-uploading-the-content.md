The idea with the playground is that you would create or checkout the repository for an existing workshop on your own local machine where you want to work on it.

For this workshop explaining how the playground works, rather than do that on your own local machine, we will do it in this workshop environment.

First up, create a clone of the Educates sample workshop which uses Markdown.

```terminal:execute
command: git clone https://github.com/eduk8s/lab-markdown-sample.git
```

Change the working directory to be inside of the directory created.

```terminal:execute
command: cd lab-markdown-sample
```

If you were creating a new workshop you wouldn't do this, and instead would create a copy of the workshop on GitHub using GitHub's template feature and give it your own name, then clone that copy. That or otherwise create a copy in whatever source code hosting system you were using and check it out on your local machine.

To upload the workshop content into the registry associated with this workshop session so it can be found when creating a workshop session in the playground, you first need to have available the ``imgpkg`` tool from the [Carvel](https://carvel.dev/) tool set. With that on your local machine, from the root of the workshop content you would then run:

{% if ingress_protocol == 'http' %}

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} --registry-insecure -f .
```

{% else %}

```terminal:execute
command: imgpkg push -i {{registry_host}}/workshop-content:latest --registry-username={{registry_username}} --registry-password={{registry_password}} -f .
```

{% endif %}

What this does it package up the workshop content as an OCI image artifact.

This is like a container image except that all it has in it is the workshop content, there are no operating system files in the image.

Head back to the training portal for the playgrounds and click on "Standard Environment" again. This time the workshop should come up successfully with the workshop content from the Git repository we checked out within this workshop session.
