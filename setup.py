import os
import subprocess
import sys


def check_docker_installed():
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Docker is already installed.")
        return True
    except subprocess.CalledProcessError:
        print("Docker is not installed.")
        return False


def install_docker():
    print("Installing Docker...")
    try:
        # Update package index
        subprocess.run(["sudo", "apt-get", "update"], check=True)

        # Install required packages for Docker
        subprocess.run(["sudo", "apt-get", "install", "-y",
                        "ca-certificates", "curl", "gnupg", "lsb-release"], check=True)

        # Add Docker’s official GPG key
        subprocess.run(['sudo', 'mkdir', '-p', '/etc/apt/keyrings'], check=True)
        subprocess.run(['curl', '-fsSL', 'https://download.docker.com/linux/ubuntu/gpg',
                        '|', 'sudo', 'gpg', '--dearmor', '-o', '/etc/apt/keyrings/docker.gpg'], check=True)

        # Set up the Docker repository
        subprocess.run(['echo', '"deb [arch=$(dpkg --print-architecture) '
                                'signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu',
                        '$(lsb_release -cs) stable"', '|', 'sudo', 'tee',
                        '/etc/apt/sources.list.d/docker.list', '> /dev/null'], shell=True)

        # Install Docker engine
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "docker-ce", "docker-ce-cli", "containerd.io"], check=True)

        print("Docker installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during Docker installation: {e}")
        sys.exit(1)


def start_docker_daemon():
    print("Starting Docker daemon...")
    try:
        subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)
        print("Docker daemon started and enabled at startup.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start Docker daemon: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if not check_docker_installed():
        install_docker()

    start_docker_daemon()
    print("Docker setup completed.")
