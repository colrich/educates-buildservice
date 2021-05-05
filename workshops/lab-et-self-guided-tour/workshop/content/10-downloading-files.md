Workshops are typically setup as being time based and when the time expires the workshop session will be deleted, along with anything created within the Kubernetes cluster.

If you wanted to allow a workshop user to download files from the workshop session, a download server within the workshop session can be enabled. By default the complete home directory of the workshop user will be exposed, but you can be more selective and allow access to only a specific directory. Access to any files is gated by the same user authentication mechanism used for the workshop session, so only the workshop user can access files.

This feature would allow you for example to instruct a user to package up sample application files they may have created as part of the workshop instructions:

```terminal:execute
command: tar cvf workshop-files.tar ./nginx-sample
clear: true
```

with a clickable action included in the workshop instructions to trigger the download.

```files:download-file
path: workshop-files.tar
```

If a browsable view of all files is required, a custom dashboard tab can be created with a view of the exposed part of the filesystem

```dashboard:create-dashboard
name: Files
prefix: Files
title: Open file browser
description: ""
url: /files/
```

In addition to access through the web browser, it is also possible to enable WebDav access if you wanted to allow a workshop user to mount the filesystem of the workshop session onto their own local machine, or access it with separate file download tools.
