The deployment of a training portal for a set of workshops is triggered by creating an instance of a `TrainingPortal` custom resource. This provides the name for the training portal deployment and the list of workshops which should be available through it.

Create the file `~/exercises/sample-workshops.yaml` containing the following resource definition.

```editor:insert-value-into-yaml
file: ~/exercises/sample-workshops.yaml
path: "."
value:
  apiVersion: training.eduk8s.io/v1alpha1
  kind: TrainingPortal
  metadata:
    name: sample-workshops
  spec:
    portal:
      sessions:
        maximum: 3
      registration:
        type: anonymous
    workshops:
    - name: lab-asciidoc-sample
      expires: 10m
      orphaned: 5m
    - name: lab-markdown-sample
      expires: 10m
      orphaned: 5m
```

There are two key sections in the training portal specification.

The `spec.portal` section is used to define properties which apply to the training portal as a whole such as access controls and the overall number of workshop sessions that can be created.

The `spec.workshops` section is a list of the workshops to be made available. The names of the workshops must match the names of the `Workshop` custom resource definitions you loaded previously.

Against each workshop you can set properties which apply only to that workshop. This can include a specific capacity for the workshop, a specific number of reserved workshop sessions that should be pre-created in readiness, and time limits.

In this workshop we will dive further into a few of the different things you can define in `TrainingPortal`. For a more thorough description consult the documentation.

```dashboard:reload-dashboard
name: Documentation
url: https://docs.edukates.io/en/latest/runtime-environment/training-portal.html
```

Before we create the deployment for the training portal start a watch on namespaces in the cluster. In doing this we will qualify the watch based on a resource label which will be added to namespaces associated with the training portal deployment.

```execute-2
watch kubectl get namespaces -l training.eduk8s.io/portal.name=sample-workshops
```

Now create the deployment of the training portal by running:

```execute
kubectl apply -f sample-workshops.yaml
```

This should display the output:

```
trainingportal.training.eduk8s.io/sample-workshops created
```

As the deployment of the training portal progresses, the watch on the namespaces will show that a number of namespaces are created.

The first namespace created will be:

```
sample-workshops-ui
```

The name of this namespace is constructed from the name of the training portal with a `-ui` suffix added. This initial namespace is where the training portal application will be deployed.

As the user of your workshop session is not a priviliged user it cannot see within this or other namespaces which are created for the training portal. A cluster admin would however be able to view the contents of the namespaces.
