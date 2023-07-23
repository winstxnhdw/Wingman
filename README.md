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

If you would like to contribute to `Wingman`, here are some instructions to get you started.

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
