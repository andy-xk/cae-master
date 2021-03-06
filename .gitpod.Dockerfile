FROM gitpod/workspace-full-vnc

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

# copypasted to run VS Code with novnc
RUN sudo apt-get update
RUN sudo apt install -y libreoffice && \
    sudo rm -rf /var/lib/apt/lists/*
