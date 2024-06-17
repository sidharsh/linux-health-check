import psutil
import subprocess

def test_cpu_usage():
    """Tests if the CPU usage is below 50%."""
    cpu_percent = psutil.cpu_percent()
    assert cpu_percent < 50, f"CPU usage is {cpu_percent}%, which exceeds the limit of 50%"
    print("CPU usage test passed!")

def test_kernel_version():
    """Tests if the kernel version is higher than 10.0.0."""
    result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
    kernel_version = result.stdout.strip()

    major, minor, patch = kernel_version.split('.')
    assert int(major) >= 10, f"Kernel version is {kernel_version}, which is lower than 10.0.0"
    print("Kernel version test passed!")


if __name__ == "__main__":
    try:
        test_cpu_usage()
        test_kernel_version()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
