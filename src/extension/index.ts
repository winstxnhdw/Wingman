import { API } from '@/api'
import { get_property } from '@/property'
import type { Disposable } from 'vscode'
import { Range, window } from 'vscode'

export class Extension implements Disposable {
  private api: API
  private max_read_lines: number

  constructor() {
    const port_number = get_property('serverPortNumber')
    this.api = new API(port_number)
    this.max_read_lines = get_property('maxReadLines')
  }

  private format_prompt(text_before_cursor: string): string {
    const formatted_text = text_before_cursor
      .split('\n')
      .filter((line) => line.trim() !== '')
      .slice(-this.max_read_lines)
      .join('\n')

    return `${formatted_text}`
  }

  async generate_text() {
    const active_editor = window.activeTextEditor

    if (!active_editor) {
      return
    }

    const document = active_editor.document
    const cursor_position = active_editor.selection.active

    const range_before_cursor = new Range(document.positionAt(0), cursor_position)
    const text_before_cursor = document.getText(range_before_cursor)
    const prompt = this.format_prompt(text_before_cursor)
    const response = await this.api.generate_text(prompt)

    await active_editor.edit((edit_builder) => {
      edit_builder.insert(cursor_position, response.text)
    })
  }

  dispose(): void {}
}
