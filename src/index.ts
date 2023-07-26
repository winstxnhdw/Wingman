import { Extension } from '@/extension'
import { register_command } from '@/helpers'
import type { ExtensionContext } from 'vscode'

export function activate(context: ExtensionContext) {
  const extension = new Extension()

  context.subscriptions.push(
    extension,
    register_command('suggest', async () => {
      await extension.generate_text()
    }),
    register_command('fix', async () => {
      await extension.fix_code()
    }),
  )
}
