FROM gitpod/workspace-full-vnc

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

# copypasted to run VS Code with novnc
RUN sudo apt-get update && \
    sudo apt-get install -y libx11-dev libxkbfile-dev libsecret-1-dev libgconf2–4 libnss3 && \
    sudo rm -rf /var/lib/apt/lists/*
