import os
import tarfile


def application(environ, start_response):
    name = environ["PATH_INFO"].lstrip("/")
    path = os.path.expanduser(os.path.join("~", "exercises", name))

    with tarfile.open(os.path.join("/tmp/downloads", f"{name}.tar.gz"), "w:gz") as tar:
        if os.path.isdir(os.path.join(path, "workshop")):
            tar.add(path, arcname=".")

    status = "200 OK"
    response_headers = [("Location", f"/{name}.tar.gz")]
    start_response(status, response_headers)

    return []
