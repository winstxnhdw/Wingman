import type { InputBoxOptions } from 'vscode'
import { window } from 'vscode'

export const get_input = async (options: InputBoxOptions): Promise<string> => {
  let response = undefined

  while (true) {
    if (response !== undefined) break
    response = await window.showInputBox(options)
  }

  return response
}
