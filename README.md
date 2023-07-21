# copilot

A no-compromise boilerplate for projects willing to be on the cutting edge of ECMAScript and Node.

## Commands

### Setup

Install all dependencies.

```bash
yarn
```

Run your application.

```bash
yarn dev
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

### Test

Run your tests with hot reloading.

```bash
yarn test
```

Run your tests without hot reloading. For testing in a CI pipeline.

```bash
yarn testci
```
