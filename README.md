# Wingman

[![main.yml](https://github.com/winstxnhdw/Wingman/actions/workflows/main.yml/badge.svg)](https://github.com/winstxnhdw/Wingman/actions/workflows/main.yml)
[![formatter.yml](https://github.com/winstxnhdw/Wingman/actions/workflows/formatter.yml/badge.svg)](https://github.com/winstxnhdw/Wingman/actions/workflows/formatter.yml)
[![dependabot.yml](https://github.com/winstxnhdw/Wingman/actions/workflows/dependabot.yml/badge.svg)](https://github.com/winstxnhdw/Wingman/actions/workflows/dependabot.yml)

<p align="center"><b>Welcome to the Wingman Monorepo</b></p>

`Wingman` is a fast CPU-based offline AI pair programmer for [Visual Studio Code](https://code.visualstudio.com/) on Windows.

## Features

- No internet connection required
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

### Build

Minify and bundle the Node application with [esbuild](https://esbuild.github.io/).

```bash
yarn build
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
