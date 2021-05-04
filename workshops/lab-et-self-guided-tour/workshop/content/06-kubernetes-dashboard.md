Creating workshops targetting Kubernetes was a key focus of Educates, but you aren't restricted to workshops being specifically related to Kubernetes.

Where a workshop does utilize Kubernetes, a web console for accessing Kubernetes can be enabled and will be embedded directly in the workshop dashboard.

```dashboard:open-dashboard
name: Console
```

When a workshop has a user deploy applications into their namespace into the Kubernetes cluster:

```terminal:execute
command: kubectl apply -f nginx-sample
```

they can then use the Kubernetes web console to explore their deployment or update resources.

If necessary you can direct users to a specific view within the Kubernetes web console using a clickable action block, rather than relying on them being able to find the correct view.

```dashboard:reload-dashboard
name: Console
prefix: Console
title: List pods in namespace {{session_namespace}}
url: {{ingress_protocol}}://{{session_namespace}}-console.{{ingress_domain}}/#/pod?namespace={{session_namespace}}
```

If desired, instead of using the standard Kubernetes dashboard you can enable as part of the workshop definition the use of the Octant console for Kubernetes.
