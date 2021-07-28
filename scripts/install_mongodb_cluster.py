import os
from time import sleep
import argparse

yaml_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..')), 'yaml', 'mongodb-cluster')
rbac_path = os.path.join(yaml_path, 'mongo.rbac.yaml')
service_path = os.path.join(yaml_path, 'mongo.service.yaml')
deploy_path = os.path.join(yaml_path, 'mongo.stateful.yaml')
yaml_data = os.path.join(os.path.split(__file__)[0], 'yaml_data.yaml')


def install(namespace='test'):
    response = os.popen('kubectl create namespace %s' % namespace).read()
    print(response)

    for p in [rbac_path, service_path, deploy_path]:
        with open(yaml_data, 'w') as f:
            with open(p, 'r') as d:
                content = d.read()
                new_content = content.replace('namespace_template', namespace)
                f.write(new_content)
        response = os.popen('kubectl apply -f %s' % yaml_data).read()
        print(response)
        sleep(5)
        os.remove(yaml_data)
    print('success')


def uninstall(namespace='test'):
    for p in [deploy_path, service_path, rbac_path]:
        with open(yaml_data, 'w') as f:
            with open(p, 'r') as d:
                content = d.read()
                new_content = content.replace('namespace_template', namespace)
                f.write(new_content)
        response = os.popen('kubectl delete -f %s' % yaml_data).read()
        print(response)
        sleep(5)
        os.remove(yaml_data)
    print('success')


if __name__ == '__main__':
    def usage():
        parser = argparse.ArgumentParser()
        parser.add_argument('-o', dest='operation', help='support: install/uninstall')
        parser.add_argument('-n', dest='namespace', help='namespace,default: test', default='test')

        return parser.parse_args()


    args = usage()
    if args.operation == 'install':
        install(namespace=args.namespace)
    elif args.operation == 'uninstall':
        uninstall(namespace=args.namespace)
    else:
        print('type not support')
