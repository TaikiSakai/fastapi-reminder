FROM python:3.11

RUN apt-get update && apt-get install -y  \
git \
zsh \
neovim
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN mkdir /api
WORKDIR /api

COPY  ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r ./requirements.txt

COPY . .

