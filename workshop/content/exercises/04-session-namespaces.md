Before a user can do a workshop they need to be allocated a workshop session. These can be created on demand when necessary, but can also be allocated from a pool of ready to go workshop sessions that are kept in reserve waiting to be used. Keeping workshop sessions in reserve ensures users don't need to wait too long for a workshop session to be ready.

By default a training portal instance will attempt to create one workshop session in reserve for each workshop. The number of workshop sessions to create in reserve can be overridden on a per workshop basis. When one of the workshop sessions kept in reserve is allocated to a user, a new workshop session will be created as a reserve to replace it.

The maximum number of workshop sessions (inclusive of any workshops sessions being kept in reserve), that can be created can be set for the whole training portal or on a per workshop basis.

With the training portal configuration we used, as it wasn't overridden, one reserve workshop session was created by the training portal for each of the workshop environments. This was done by the training portal creating instances of the `WorkshopSession` custom resource. As with `WorkshopEnvironment`, although you can see they exist, you don't need to directly deal with instances of the `WorkshopSession` resource.

If you did want to see what workshop sessions exist, independent of what training portal or workshop environment they were created from, run:

```execute
kubectl get workshopsessions -o name
```

This should yield:

```
workshopsession.training.eduk8s.io/{{session_namespace}}
workshopsession.training.eduk8s.io/sample-workshops-w01-s001
workshopsession.training.eduk8s.io/sample-workshops-w02-s001
```

Similar to before, you will see that there is one workshop session for the current workshop session you are working through. This is the session named `{{session_namespace}}`.

The other sessions are for the sample workshops you just deployed. Right now neither of those has been allocated to a user and are sitting there in reserve waiting.

Since the intent of deploying workshops to Kubernetes is often to be able to teach something about Kubernetes, each workshop session is given a namespace in the cluster to use. This is called the session namespace and would be where a user working through a workshop could deploy applications.

This is what the:

```
sample-workshops-w01-s001
sample-workshops-w02-s001
```

namespaces are that the watch on namespaces displayed.

Like with naming of the namespace for the workshop environment, the name of the namespaces matches the name of the custom resource for the workshop session. The convention in this case is that the session namespace has name with prefix matching the name of the workshop environment, with a `-s` suffix, and number corresponding to the workshop session for that workshop environment.

This session namespace would be accessible to the user doing the workshop session. It can also be accessed by a cluster admin. You as the user of this workshop session cannot access it, nor would any other user doing a workshop, even if the same workshop.

Access to session namespaces is controlled by virtue of each workshop session running with the access rights of a different Kubernetes service account. Role based access control (RBAC) rules are then used to determine what a user can do. This way a user can be restricted to only being able to work in their namespace.

If you want to be able to work out what workshop a session namespace corresponds to, you can query the labels present on the namespace.

```execute
kubectl get namespaces -l training.eduk8s.io/portal.name=sample-workshops,training.eduk8s.io/component=session -o json | jq '[.items[] | {name: .metadata.name, labels: .metadata.labels}]'
```

This should yield in this case.

```
[
  {
    "name": "sample-workshops-w01-s001",
    "labels": {
      "training.eduk8s.io/component": "session",
      "training.eduk8s.io/environment.name": "sample-workshops-w01",
      "training.eduk8s.io/portal.name": "sample-workshops",
      "training.eduk8s.io/session.name": "sample-workshops-w01-s001",
      "training.eduk8s.io/workshop.name": "lab-asciidoc-sample"
    }
  },
  {
    "name": "sample-workshops-w02-s001",
    "labels": {
      "training.eduk8s.io/component": "session",
      "training.eduk8s.io/environment.name": "sample-workshops-w02",
      "training.eduk8s.io/portal.name": "sample-workshops",
      "training.eduk8s.io/session.name": "sample-workshops-w02-s001",
      "training.eduk8s.io/workshop.name": "lab-markdown-sample"
    }
  }
]
```
