To start a workshop jump back over to the web interface of the training portal for the sample workshops you deployed.

Click on the "Start workshop" button for the "AsciiDoc Sample" workshop.

Once the workshop dashboard for the sample workshop is displayed, take note of the URL in the web browser, you should see that it includes the session name `sample-workshops-w01-s001` corresponding to the workshop session which was created in reserve, ready to be used.

Check again the state of the watch on namespaces in the terminal.

```dashboard:open-dashboard
name: Terminal
```

You should see that a new namespace has now been created with name `sample-workshops-w01-s002`. This is the namespace for a new workshop session created in reserve to replace the one which was justed allocated to the workshop session you requested.

You can also verify this by again listing the workshop sessions, this time qualifying the query by the name of the training portal.

```execute
kubectl get workshopsessions -o name -l training.eduk8s.io/portal.name=sample-workshops
```

This should output:

```
workshopsession.training.eduk8s.io/sample-workshops-w01-s001
workshopsession.training.eduk8s.io/sample-workshops-w02-s002
workshopsession.training.eduk8s.io/sample-workshops-w01-s002
```

Note that there isn't any way from looking at the resources for the workshop sessions to determine whether they are in use. As we will explore later, the state of workshop sessions can be determined by using the admin web interface of the training portal.
