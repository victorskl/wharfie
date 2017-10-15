#!/usr/bin/env python

import docker

# TODO: write backup using Docker Python SDK API
# http://docker-py.readthedocs.io/en/stable/index.html
# http://docker-py.readthedocs.io/en/stable/api.html
# https://docs.docker.com/develop/sdk/examples/

BACKUP_DIR = '/mnt/docker_backup'


def main():
    print (BACKUP_DIR)
    client = docker.from_env()
    print (client.images.list())


if __name__ == '__main__':
    main()
