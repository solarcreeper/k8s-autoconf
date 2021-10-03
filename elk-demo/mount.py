import argparse
import os
import random

from elasticsearch import Elasticsearch
import socket

es = Elasticsearch(['192.168.101.201:30100'], http_auth="elastic:qjlvT5sg50T8RU053Y8k6V9x")


def log(msg):
    data = {'hostname': socket.gethostname(), 'message': msg}
    es.index(index='mount_log', doc_type='test_type', body=data)


def mount(mounts, version):
    try:
        mount_points = mounts.split(',')
        log("mount points: " % mount_points)

        log("version: %s" % version)

        for mount_point in mount_points:
            if version == 'all':
                version = random.choice([3, 4, 4.1])
            mount_path = '/mnt%s' % mount_point.split(':')[1]
            os.popen('mkdir -p %s' % mount_path).read()
            cmd = 'mount -t nfs -o nfsvers=%s %s %s' % (version, mount_point, mount_path)
            log("mount cmd: %s" % cmd)
            os.popen(cmd)
            cmd = 'mount | grep %s' % mount_point
            log("mount result:%s" % os.popen(cmd).read())

    except Exception as e:
        log(str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--mount', type=str, help='mount_point, 192.168.101.100:xxx,')
    parser.add_argument('-v', '--version', type=str, help='nfs_version: 3, 4, 4,1, all')
    args = parser.parse_args()

    mount(mounts=args.mount, version=args.version)
