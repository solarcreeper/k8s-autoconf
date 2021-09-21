import os
import argparse
from time import sleep

yaml_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..')), 'yaml', 'elk')
master_config_path = os.path.join(yaml_path, 'elasticsearch-master.configmap.yaml')
master_sfs_path = os.path.join(yaml_path, 'elasticsearch-master.statefulset.yaml')
master_svc_path = os.path.join(yaml_path, 'elasticsearch-master.service.yaml')
client_config_path = os.path.join(yaml_path, 'elasticsearch-client.configmap.yaml')
client_deploy_path = os.path.join(yaml_path, 'elasticsearch-client.deployment.yaml')
client_svc_path = os.path.join(yaml_path, 'elasticsearch-client.service.yaml')
data_config_path = os.path.join(yaml_path, 'elasticsearch-data.configmap.yaml')
data_sfs_path = os.path.join(yaml_path, 'elasticsearch-data.statefulset.yaml')
data_svc_path = os.path.join(yaml_path, 'elasticsearch-data.service.yaml')
kibana_config_path = os.path.join(yaml_path, 'kibana.configmap.yaml')
kibana_deploy_path = os.path.join(yaml_path, 'kibana.deployment.yaml')
kibana_svc_path = os.path.join(yaml_path, 'kibana.service.yaml')
yaml_data = os.path.join(os.path.split(__file__)[0], 'yaml_data.yaml')


def install(namespace='test'):
    print(os.popen('kubectl create namespace %s' % namespace).read())
    install_configs = [master_config_path, master_sfs_path, master_svc_path,
                       client_config_path, client_deploy_path, client_svc_path,
                       data_config_path, data_sfs_path, data_svc_path,
                       kibana_config_path, kibana_deploy_path, kibana_svc_path]
    for p in install_configs:
        with open(yaml_data, 'w') as f:
            with open(p, 'r') as d:
                content = d.read()
                new_content = content.replace('namespace_template', namespace)
                f.write(new_content)
        print('install %s: %s' % (os.path.split(p)[-1], os.popen('kubectl apply -f %s' % yaml_data).read()))
        sleep(5)
        os.remove(yaml_data)
    passwd_cmd = "kubectl exec $(kubectl get pods -n elastic | grep elasticsearch-client | sed -n 1p | awk '{print $1}')  -n elastic  -- bin/elasticsearch-setup-passwords auto -b"
    secret_cmd = "kubectl create secret generic elasticsearch-pw-elastic -n elastic  --from-literal password=上一条命令中elastic的密码"
    print("请手动生成kibana的登录密码: %s" % passwd_cmd)
    print("请手动配置kibana的登录密码: %s" % secret_cmd)
    print('success')


def uninstall(namespace='test'):
    uninstall_configs = [master_config_path, master_sfs_path, master_svc_path,
                         client_config_path, client_deploy_path, client_svc_path,
                         data_config_path, data_sfs_path, data_svc_path,
                         kibana_config_path, kibana_deploy_path, kibana_svc_path]
    for p in uninstall_configs:
        with open(yaml_data, 'w') as f:
            with open(p, 'r') as d:
                content = d.read()
                new_content = content.replace('namespace_template', namespace)
                f.write(new_content)
        print('install %s: %s' % (os.path.split(p)[-1], os.popen('kubectl delete -f %s' % yaml_data).read()))
        sleep(5)
        os.remove(yaml_data)
    print('remove kibana secret: %s' % os.popen('kubectl delete -f %s' % yaml_data).read())
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
