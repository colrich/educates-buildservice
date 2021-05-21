The workshop playgrounds are setup for you and you cannot modify the workshop or training portal definitions through the playground environment. To try and provide as much flexibility in what you can do, as many features of a workshop session are enabled as can be.

The canonical workshop definition is:

```
apiVersion: training.eduk8s.io/v1alpha2
kind: Workshop
metadata:
  name: $(session_namespace)-playground
spec:
  title: Playground
  description: Creates the playground.
  content:
    image: base-environment:*
    files: imgpkg+$(ingress_protocol)://$(registry_username):$(registry_password)@$(registry_host)/workshop-content:latest
  session:
    namespaces:
      budget: large
    applications:
      terminal:
        enabled: true
        layout: split
      console:
        enabled: true
        vendor: octant
      editor:
        enabled: true
      examiner:
        enabled: true
      docker:
        enabled: true
      registry:
        enabled: true
```

The ``large`` budget means you can use up to 4Gi of memory. Depending on how many applications you may need to deploy to the namespace of the Kubernetes cluster, you may still have to override resource requests and limits for the applications in the deployment resources.

You will not be able to create deployments using container images that require ``root`` to run.

No persistent storage is provided for the workshop session.

You cannot define Kubernetes resources that are to be created for the workshop environment as a whole or a specific workshop session.

You cannot use a custom workshop base image.

If the idea of a playground for working on content is of interest but you need to use a custom workshop image, or want to tailor the workshop definition, you can always copy what this playground does, change the workshop definition and deploy your own playground.

You can see the full workshop definition at:

```dashboard:open-url
url: https://github.com/eduk8s/eduk8s-tutorials/blob/master/resources/lab-et-basic-playground.yaml
```

and the content for this workshop can be found at:

```dashboard:open-url
url: https://github.com/eduk8s/eduk8s-tutorials/blob/master/workshops/lab-et-playground-intro
```
