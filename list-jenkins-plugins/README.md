# List Jenkins plugins

Tiny command to get the list of plugins installed in a Jenkins instance at a moment in time via `http(s)` connection to the master.
The list of plugins is printed on stdout in [plugins.txt][plugins-txt-link] format, so you can use it to create 
a fresh Jenkins instance with that plugins set by [building a Jenkins Docker image][dockerfile-link].

It gets the plugins list from the `pluginManager/api/xml` ReST endpoint of Jenkins master, loading the `xml` response body
into memory in chunks of configurable size to tackle huge plugins sets. Plugins are listed in alphabetical order so you can 
point out for which plugins two instances differs(or the same instance over time) via common diffing tools(i.e. `git diff`)

## Installation
The implementation is a single *Python 3* module with a `setup.py` script to pack it via [`setuptools`][setuptools-link]. 
Thus it can be distributed on a [Python package index][pypi-link] and installed via a package manager like [`Pip`][pip-link]:

```
    pip install .
```
Supposing that your current directory is a checkout of the [module one][github-link]

## Usage

run `list-jenkins-plugins -h` to get a help message like the following:

```
list-jenkins-plugins -h
usage: list-jenkins-plugins [-h] [--user USER] [--password PASSWORD]
                            [--chunk-size CHUNK_SIZE]
                            [jenkins_base_url]

snapshot list of installed plugins on a Jenkins instance in plugins.txt format

positional arguments:
  jenkins_base_url      Jenkins instance base url. Defaults to
                        http://localhost:8080

optional arguments:
  -h, --help            show this help message and exit
  --user USER, -u USER
  --password PASSWORD, -p PASSWORD
  --chunk-size CHUNK_SIZE, -c CHUNK_SIZE
                        Jenkins response streaming chunks size. Defaults to 20
                        kB
```

So by running:

```
list-jenkins-plugins -u <USER> -p <PASSWORD>
```

You can get the list of installed plugins on a local Jenkins instance exposed on port `8080` via `http`

```
.... 

pipeline-model-definition:1.6.0
pipeline-model-extensions:1.6.0
pipeline-rest-api:2.13
pipeline-stage-step:2.3
pipeline-stage-tags-metadata:1.6.0
pipeline-stage-view:2.13
plain-credentials:1.7
resource-disposer:0.14
scm-api:2.6.3
script-security:1.71
ssh-credentials:1.18.1
ssh-slaves:1.31.2
structs:1.20

.... 
```

[plugins-txt-link]: https://github.com/rikZerac/gradle-hello-world/blob/master/plugins.txt
[dockerfile-link]: https://github.com/rikZerac/gradle-hello-world/blob/master/Dockerfile
[setuptools-link]: https://packaging.python.org/guides/distributing-packages-using-setuptools/
[pypi-link]: https://pypi.org/
[pip-link]: https://pip.pypa.io/en/stable/
[github-link]: https://github.com/rikZerac/gradle-hello-world/tree/master/list-jenkins-plugins