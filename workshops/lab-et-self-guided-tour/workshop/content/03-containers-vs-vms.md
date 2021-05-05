Other products or services providing hosted workshop environments accessible through a web browser generally rely on creating a virtual machine for each users workshop session. This means that workshop sessions can be slow to start up if being created on demand. They can also be difficult to use due to relying on applications which mirror a traditional desktop environment in the web browser.

In Educates each workshop environment, rather than consuming a complete virtual machine, is a container in a Kubernetes cluster.

Rather than having access to a full operating system running in a virtual machine, you are only able to interact with the container for the workshop session.

This doesn't mean you cannot run additional applications. If required for a workshop, you can start up extra processes local to the container. For more complicated scenarios, you can deploy applications into the Kubernetes cluster. This can be done as part of starting up the workshop session, or it could be done by a workshop user as part of the workshop instructions.

In the case of using the Kubernetes cluster, what a workshop user can do in the cluster is controlled through the use of role base access control (RBAC) mechanisms of Kubernetes.

By default you can only deploy applications into a single Kubernetes namespace allocated to the workshop session. You cannot perform any actions beyond that, such as actions which might require cluster admin access.

For specific workshops you can customize the RBAC and security policies applied to the workshop user granting them additional privileges, such as the ability to create custom resources managed by a custom operator deployed to the cluster.

In addition to RBAC controlling what a workshop user can do, resource quotas and limits are used to control how much resources a workshop user can use. This ensures that a single workshop user cannot monopolize the resources of the cluster and that all workshop sessions running in a cluster can access the resources they need.

Just because a workshop session is a container running in a Kubernetes cluster doesn't though mean that virtual machines could not be used for a workshop if required. Theoretically it is possible to use systems such as [KubeVirt](https://kubevirt.io/) or a [VM operator](https://github.com/vmware-tanzu/vm-operator) to trigger the creation of virtual machines. Such an ability isn't bundled with Educates, but for each workshop session it is possible to have additional Kubernetes resources created. This means you could use a custom resource to trigger the creation of a virtual machine, which could then be accessed from the workshop session.

When all is over and done and the workshop session is being deleted, resources being used in the Kubernetes cluster, such as the Kubernetes namespaces assigned to the session, are automatically deleted.
