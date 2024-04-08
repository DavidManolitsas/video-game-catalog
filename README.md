# Video Game Catalog

This is a python application that generates a single page application. 
Highlighting the latest video games releases, upcoming games, 
recently reviewed games and the best games released of the past year.

To view the latest deployed web page visit: 
https://davidmanolitsas.github.io/video-game-catalog/

## Setup Project

Install virtualenv package with pip:

```shell
pip3 install -U virtualenv
```

Start virtual environment (venv) with:

```shell
python3 -m virtualenv .venv
```

```shell
source .venv/bin/activate
```

Install requirements:

```shell
pip3 install -U -r requirements.txt
```

## Quick Start

Run the project with:

```shell
python3 -m games -k $OPEN_CRITIC_API_KEY
```