import { Extension } from '@/extension'
import { register_command } from '@/helpers'
import { ExtensionContext } from 'vscode'

export function activate(context: ExtensionContext) {
  const extension = new Extension()

  context.subscriptions.push(
    extension,
    register_command('stealth', async () => {
      await extension.toggle_stealth()
    }),
    register_command('suggest', async () => {
      await extension.generate_text()
    }),
  )
}
