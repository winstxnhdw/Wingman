import { API } from '@/api'
import { get_input } from '@/helpers'
import { get_property } from '@/property'
import type { Disposable, ProgressOptions } from 'vscode'
import { ProgressLocation, Range, window } from 'vscode'

export class Extension implements Disposable {
  private api: API
  private max_read_lines: number
  private progress_options: ProgressOptions

  constructor() {
    const port_number = get_property('serverPortNumber')
    this.api = new API(port_number)
    this.max_read_lines = get_property('maxReadLines')

    this.progress_options = {
      location: ProgressLocation.Window,
      cancellable: false,
      title: 'Querying Wingman..',
    }
  }

  private format_suggestion_prompt(text_before_cursor: string): string {
    const formatted_text = text_before_cursor
      .split('\n')
      .filter((line) => line.trim() !== '')
      .slice(-this.max_read_lines)
      .join('\n')

    return `${formatted_text}`
  }

  private format_fix_prompt(highlighted_text: string, context: string): string {
    return `${context}\n\n${highlighted_text}`
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

    const prompt = this.format_suggestion_prompt(text_before_cursor)
    const response = await this.api.generate_text(prompt)

    await active_editor.edit((edit_builder) => edit_builder.insert(cursor_position, response.text))
  }

  async fix_code() {
    const active_editor = window.activeTextEditor

    if (!active_editor) {
      return
    }

    const selection = active_editor.selection

    if (selection.isEmpty) {
      await window.showInformationMessage('Wingman: No selection was provided.')
      return
    }

    const selection_range = new Range(
      selection.start.line,
      selection.start.character,
      selection.end.line,
      selection.end.character,
    )

    const context = await get_input({ placeHolder: 'Enter your context here..' })
    const highlighted_text = active_editor.document.getText(selection_range)
    const prompt = this.format_fix_prompt(highlighted_text, context)

    const response = await window.withProgress(this.progress_options, async (progress) => {
      progress.report({ increment: 0 })
      const response = await this.api.generate_text(prompt)
      progress.report({ increment: 100 })
      return response
    })

    await active_editor.edit((edit_builder) => edit_builder.replace(selection_range, response.text))
  }

  dispose(): void {}
}
