
```examiner:execute-test
name: test-that-nginx-pod-exists
title: Verify that nginx pod is running
cascade: true
```

```terminal:execute
command: kubectl delete -f nginx-sample
```

```examiner:execute-test
name: test-that-nginx-pod-does-not-exist
title: Verify that nginx pod no longer exists
