import { build } from 'esbuild'
import { cp, mkdir, rm } from 'fs/promises'
import { argv } from 'process'

const build_directory = 'dist'
const external_modules = [] as string[]

async function main(args: string[]) {
  await rm(build_directory, { recursive: true, force: true })
  await mkdir(build_directory)

  const results = await Promise.allSettled(
    external_modules.map((module) =>
      cp(
        `node_modules/${module}`,
        `${build_directory}/node_modules/${module}`,
        {
          recursive: true,
        }
      )
    )
  )

  results.forEach((result) => {
    if (result.status !== 'rejected') return
    console.error(result.reason)
  })

  await build({
    entryPoints: ['src/index.ts'],
    outfile: `${build_directory}/index.js`,
    bundle: true,
    minify: args.slice(2)[0] !== 'test',
    platform: 'node',
    external: external_modules,
  })
}

void main(argv)
