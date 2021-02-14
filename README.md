Educates Tutorials
==================

This repository contains a set of workshops for educates which aims to guide
you through how to deploy workshops with Educates on Kubernetes, and how to
create your own custom workshops.

Warning
-------

The workshops should only be deployed on private instances of Kubernetes such
as a local instances of Minikube, K3s and Kind, or other disposable Kubernetes
cluster that can be deleted once the workshop has been completed. This is
because although the workshop environment user does not have any elevated
privileges in the Kubernetes cluster, the user can indirectly deploy Educates
workshops to the cluster that may grant elevated privileges. Do not therefore
deploy these workshops to a production cluster.

Prerequisites
-------------

In order to use the workshop you must already have the Educates operator
installed. You need to have cluster admin access for the Kubernetes cluster
to deploy the operator and the workshop.

For installation instructions for the Educates operator see:

* https://github.com/eduk8s/eduk8s

Deployment
----------

To load the workshop definition run:

```
kubectl apply -f https://raw.githubusercontent.com/eduk8s/lab-workshop-deployment/master/resources/workshop.yaml
```

To deploy a training portal for accessing the workshop, run:

```
kubectl apply -f https://raw.githubusercontent.com/eduk8s/lab-workshop-deployment/master/resources/training-portal.yaml
```

Then run:

```
kubectl get trainingportal/lab-workshop-deployment
```

This will output the URL and login credentials to access the web portal for
the training environment.

Deletion
--------

To delete the training portal deployment, run:

```
kubectl delete -f https://raw.githubusercontent.com/eduk8s/lab-workshop-deployment/master/resources/training-portal.yaml
```

When you are finished with the workshop definition, you can delete it by running:

```
kubectl delete -f https://raw.githubusercontent.com/eduk8s/lab-workshop-deployment/master/resources/workshop.yaml
```

If you deployed any workshops from the workshop environment, and did not
delete them as per the instructions provided in the workshop, you will need
to delete them manually.

To see what workshops are deployed run:

```
kubectl get trainingportals
```

Identify those which were created due to running the workshop, and delete
the corresponding ``trainingportal`` resource.

You will also need to run:

```
kubectl get workshops
```

and delete any ``workshop`` resource for workshop definitions created as part
of the workshop.
