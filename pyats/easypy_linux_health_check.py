from pyats.topology import Device
import yaml

def main(runtime):

    # Load configuration from YAML file
    with open('/path/to/your/config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    remote_ip = config['remote_host']['ip']
    remote_port = config['remote_host']['port']
    remote_user = config['remote_host']['username']
    remote_password = config['remote_host']['password']
    

    # Create a pyATS Device object (represents the remote host)
    device = Device(name='remote_linux_host', os='linux')
    device.connections.setdefault('cli', {})['protocol'] = 'ssh'
    device.connections['cli']['ip'] = remote_ip
    device.connections['cli']['port'] = remote_port
    device.connections['cli']['username'] = remote_user
    device.connections['cli']['password'] = remote_password

    # Connect to the remote device
    device.connect(via='cli')

    # Transfer the health check script to the remote host
    device.api.execute('mkdir -p /tmp/health_check')
    device.api.transmit('/path/to/your/local/linux_health_check.py', '/tmp/health_check/linux_health_check.py')
    
    # Make the script executable and run it remotely
    device.api.execute('chmod +x /tmp/health_check/linux_health_check.py')
    result = device.api.execute('python3 /tmp/health_check/linux_health_check.py')
   
    # Print output to the local console
    print(result)

    # Disconnect from the remote device
    device.disconnect()
