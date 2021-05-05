Where a user is being asked to perform actions as part of the workshop instructions but you haven't told them how to do it and they need to work it out themselves, you can provide validation checks they can trigger to test that they got the desired result.

```examiner:execute-test
name: test-that-nginx-pod-exists
title: Verify that nginx pod is running
cascade: true
```

These can be manually triggered as above, or you can set them up to automatically start checking when the page is loaded, or when the prior check has succeeded.

Trigger the check above to verify that the deployment of nginx to the Kubernetes cluster was done, then delete the deployment.

```terminal:execute
command: kubectl delete -f nginx-sample
```

When the deployment has been deleted, the following test should show as passed. 

```examiner:execute-test
name: test-that-nginx-pod-does-not-exist
title: Verify that nginx pod no longer exists
timeout: 5
retries: .INF
delay: 1
```
