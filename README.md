#Archiver
[![Travis](https://travis-ci.org/chrisseto/Archiver.svg?branch=develop)](https://travis-ci.org/chrisseto/Archiver)
[![Coverage Status](https://coveralls.io/repos/chrisseto/Archiver/badge.png?branch=develop)](https://coveralls.io/r/chrisseto/Archiver?branch=develop)

###Work flow

* Server sends [properly formatted json](formats/container.json)
* Json is parsed by flask app
* Job is passed to foreman
* [201 (created)](formats/confirmation.json) and the container id are sent back to the server
* foreman begins the archival process
* Project is chunked up even more
* On completion a callback is fired and the celeryworker pings the foreman

###Vocabulary

* [Container](formats/container.json)
    - Any given osf project that is not a registration
* Registration
    - A "frozen" osf project
* Foreman
    - The controlling flask app
* Worker
    - The celery worker
* [Service](formats/services)
    - An arbitrary 3rd party service


###To do
* ansible
* Par2 files

###Usage
1. Fill out local.py with your settings of choice.
2. Run `invoke setup` to make the executables executable
3. Ensure that RabbitMQ is running
4. Launch the foreman with `./Foreman`
5. On any number of machines launch the celery worker with `./Worker`

###Registration structure

registration will have directory structure as such:
(subject to change)

```
{project id}/
    metadata.json
    children/
        {child id}/
            {project}
    services/
        github/
            {repo name}/
                {repo contents}
        s3/
            {bucket name}/
                {bucker contents}
        figshare/
            {id}/
                {figshare contents}
        dropbox/
            {folder}/
                {folder contents}
```
