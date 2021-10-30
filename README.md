# Documentation

This repo is the source for the unofficial [Deebot documentation](https://deebot.readthedocs.io/).

This documentation is unofficial, and is not sponsored, owned or endorsed by Ecovacs (Robotics).

## How to contribute

To add a new link on the navigation panel you need to edit the `mkdocs.yml` file in the root of the repo. There is a guide for building the navbar [on the mkdocs wiki](https://www.mkdocs.org/user-guide/configuration/#nav)

To add a new document:

- Navigate to the directory where it will be hosted.
- Create the file using a URL friendly filename.
- Edit your document using Markdown, there are loads of resources available for the correct syntax.

## Testing your changes

When working on this repo, it is advised that you review your changes locally before committing them. The `mkdocs serve` command can be used to live preview your changes (as you type) on your local machine.

Please make sure you fork the repo and change the clone URL in the example below for your fork:

- Linux Mint / Ubuntu 18.04 LTS / 19.10 / 20.04 LTS:

    - Preparations (only required once):

  ```bash
  git clone https://github.com/YOUR-USERNAME/docs
  cd docs
  sudo apt install python3-pip
  sudo pip3 install -r requirements.txt
  ```

    - Running the docs server:

  ```bash
  mkdocs serve --dev-addr 0.0.0.0:8000
  ```

- Fedora Linux instructions (tested on Fedora Linux 28):

    - Preparations (only required once):

  ```bash
  git clone https://github.com/YOUR-USERNAME/docs
  cd docs
  pip install --user -r requirements.txt
  ```

    - Running the docs server:

  ```bash
  mkdocs serve --dev-addr 0.0.0.0:8000
  ```

- Docker instructions:

    - One-shot run:

  ```bash
  docker run -v `pwd`:/opt/app/ -w /opt/app/ -p 8000:8000 -it nikolaik/python-nodejs:python3.7-nodejs12 \
    sh -c "pip install --user -r requirements.txt && \
    /root/.local/bin/mkdocs build && \
    npm ci && \
    npm test && \
    /root/.local/bin/mkdocs serve --dev-addr 0.0.0.0:8000"
  ```

After these commands, the current branch is accessible through your favorite browser at <http://localhost:8000>
