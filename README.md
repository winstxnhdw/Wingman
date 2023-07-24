# Wingman

[![main.yml](https://github.com/winstxnhdw/Wingman/actions/workflows/main.yml/badge.svg)](https://github.com/winstxnhdw/Wingman/actions/workflows/main.yml)
[![formatter.yml](https://github.com/winstxnhdw/Wingman/actions/workflows/formatter.yml/badge.svg)](https://github.com/winstxnhdw/Wingman/actions/workflows/formatter.yml)
[![dependabot.yml](https://github.com/winstxnhdw/Wingman/actions/workflows/dependabot.yml/badge.svg)](https://github.com/winstxnhdw/Wingman/actions/workflows/dependabot.yml)

<p align="center"><b>Monorepo for Wingman</b></p>

> Did you know that the **Win** in **Win**gman stands for **Win**dows?

`Wingman` is a **fast CPU-first offline AI pair programmer** for [Visual Studio Code](https://code.visualstudio.com/) on Windows. `Wingman` comes with a self-contained [FastAPI](https://fastapi.tiangolo.com/) server that leverages the fast inference speeds of [ctransformers](https://github.com/marella/ctransformers) and a lightweight 4-bit quantised model to provide a seamless pair programming experience on low-end machines. You may find the used model [here](https://huggingface.co/winstxnhdw/Replit-v2-CodeInstruct-3B-ggml-4bit).

## Features

- No internet connection required
- No API keys required
- No GPU required
- Self-contained
- Fast

## Development

If you would like to contribute to `Wingman`, here is some information to get you started.

### Requirements

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Node.js 16](https://nodejs.org/ja/blog/release/v16.16.0)
- [Poetry](https://python-poetry.org/)
- [Yarn](https://yarnpkg.com/)

### Setup

Install all TypeScript dependencies.

```bash
yarn
```

Install all server dependencies.

```bash
poetry install
```

Download the model.

```bash
python scripts/download_model.py
```

### Build

Minify, bundle and package the extension.

```bash
yarn package
```

Human-readable bundle of your Node application. For debugging purposes.

```bash
yarn build test
```

Build the installer.

```bash
python scripts/build.py
```

### Test

Test the Visual Studio Code extension.

```bash
yarn test
```

Test the server.

```bash
pytest
```
