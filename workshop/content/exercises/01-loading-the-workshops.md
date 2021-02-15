To get started we will deploy a set of existing workshops.

There are a number of ways workshops can be deployed using Educates, but the recommended method involves deploying a training portal which provides a web interface which you or others can then use to select which workshop you want to do.

Specifying which workshops can be deployed to a Kubernetes cluster, and which are available through a specific instance of a training portal, is dictated through the creation of custom resources in the Kubernetes cluster.

The first step of this process is to load the `Workshop` custom resource definitions corresponding to each of the workshops you want to make available. For this example we will load two different workshops.

Run:

```execute
kubectl apply -f https://raw.githubusercontent.com/eduk8s/lab-markdown-sample/master/resources/workshop.yaml
```

and:

```execute
kubectl apply -f https://raw.githubusercontent.com/eduk8s/lab-asciidoc-sample/master/resources/workshop.yaml
```

If you haven't already worked it out, you do not need to manually enter the commands above. Whenever you see action blocks in the workshop instructions like those above, you can click on them and the action described will be done for you. This can include running a command in the terminal for you, copying text into the browser paste buffer, opening a new web page etc.

Once you have loaded the workshop definitions run:

```execute
kubectl get workshops -o name
```

The result should include the workshop resources:

```
workshop.training.eduk8s.io/lab-asciidoc-sample
workshop.training.eduk8s.io/lab-markdown-sample
workshop.training.eduk8s.io/{{workshop_name}}
```

That for `{{workshop_name}}` is the definition for this workshop, and the others are for those you just loaded. You may see other workshops listed if someone is already using Educates to run workshops within the same Kubernetes cluster as the workshop definitions are cluster scoped and not namespace scoped.

The action of loading the workshop definitions does nothing besides creating the custom resources within the Kubernetes cluster. No actual workshop environment or sessions will be created.

The loading of the workshop definitions as a separate step before actually creating any deployments for the workshops is to ensure there is an opportunity for any cluster admin to audit the workshop definitions and decide first that they want to allow them to be run in the cluster. It is only after the workshop definitions have been loaded that they will be able to be associated with a training portal instance. It is not possible to refer directly to a remote hosted resource definition in the configuration for the training portal.

A more detailed look into the workshop definition is covered in a separate workshop on creating workshops, but if you want to have a quick look at what one looks like run:

```execute
kubectl get workshop/lab-markdown-sample -o yaml
```
