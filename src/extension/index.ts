import got from 'got'
import type { Disposable } from 'vscode'
import { window } from 'vscode'

export class Extension implements Disposable {
  constructor() {
    this.start_listeners()
  }

  private start_listeners() {}

  async generate_text() {
    const active_editor = window.activeTextEditor

    if (!active_editor) {
      return
    }

    const response: { text: string } = await got
      .post('http://localhost:3997/v1/generate', {
        json: {
          prompt: 'hello world',
        },
        retry: {
          limit: 0,
        },
      })
      .json()

    const cursor_position = active_editor.document.positionAt(
      active_editor.document.offsetAt(active_editor.selection.active),
    )

    await active_editor.edit((edit_builder) => {
      edit_builder.insert(cursor_position, response.text)
    })
  }

  async toggle_stealth() {}

  dispose(): void {}
}
