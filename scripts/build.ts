import { build } from 'esbuild'
import { mkdir, rm } from 'fs/promises'
import { argv } from 'process'

const build_directory = 'dist'
const external_modules = ['vscode'] as string[]

async function main(args: string[]) {
  await rm(build_directory, { recursive: true, force: true })
  await mkdir(build_directory)

  await build({
    entryPoints: ['src/extension.ts'],
    outfile: `${build_directory}/extension.js`,
    bundle: true,
    minify: args.slice(2)[0] !== 'test',
    platform: 'node',
    external: external_modules,
  })
}

void main(argv)
