from pyats.easypy import run
from pyats.topology import Device

def main(runtime):

    # Get remote device information from user
    remote_ip = runtime.args.remote_ip  # Get IP from command-line arguments
    remote_port = runtime.args.remote_port  # Get port from command-line arguments
    remote_user = runtime.args.remote_user if hasattr(runtime.args, 'remote_user') else 'username'
    remote_password = runtime.args.remote_password if hasattr(runtime.args, 'remote_password') else 'password'

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
