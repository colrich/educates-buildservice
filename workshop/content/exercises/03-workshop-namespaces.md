Once the deployment of the training portal has completed and it is starting up, it will consult the list of workshops defined in the custom resource for that training portal. The training portal will then trigger the creation of a workshop environment for each workshop. Under the covers this is initiated by the training portal creating instances of the `WorkshopEnvironment` custom resource, but you usually don't need to worry about those.

If you did want to see what workshop environments exist, independent of what training portal they were created from, run:

```execute
kubectl get workshopenvironments -o name
```

This should yield:

```
workshopenvironment.training.eduk8s.io/{{workshop_namespace}}
workshopenvironment.training.eduk8s.io/sample-workshops-w01
workshopenvironment.training.eduk8s.io/sample-workshops-w02
```

The `{{workshop_namespace}}` is for this workshop you are working through. The others are for the sample workshops you just deployed.

With the workshop environments for each workshop created, the next pair of namespaces that will show up via the watch are:

```
sample-workshops-w01 
sample-workshops-w02
```

The names of the namespaces for these is the name of the training portal with a `-w` suffix, and number corresponding to an instance of a workshop environment. These names will be the same as was used for the instances of the `WorkshopEnvironment` custom resource created by the training portal.

Because the training portal definition for this example listed two workshops, there were two workshop environment namespaces.

You can see which workshop a namespace corresponds to by viewing the labels defined on the namespace.

```execute
kubectl get namespaces -l training.eduk8s.io/portal.name=sample-workshops,training.eduk8s.io/component=environment -o json | jq '[.items[] | {name: .metadata.name, labels: .metadata.labels}]'
```

This should yield:

```
[
  {
    "name": "sample-workshops-w01",
    "labels": {
      "training.eduk8s.io/component": "environment",
      "training.eduk8s.io/environment.name": "sample-workshops-w01",
      "training.eduk8s.io/portal.name": "sample-workshops",
      "training.eduk8s.io/workshop.name": "lab-asciidoc-sample"
    }
  },
  {
    "name": "sample-workshops-w02",
    "labels": {
      "training.eduk8s.io/component": "environment",
      "training.eduk8s.io/environment.name": "sample-workshops-w02",
      "training.eduk8s.io/portal.name": "sample-workshops",
      "training.eduk8s.io/workshop.name": "lab-markdown-sample"
    }
  }
]
```

The namespaces for the workshop environments are where the application providing the workshop dashboard, terminals, Kubernetes console and editor are deployed for each user. This namespace may also be used to deploy applications or services specific to a workshop which need to be shared between all workshop sessions.
