import { Disposable, commands } from 'vscode'

type RegisterCommandParameter = Parameters<typeof commands.registerCommand>

export const register_command = (
  command_name: string,
  callback: RegisterCommandParameter[1],
  this_arg?: RegisterCommandParameter[2],
): Disposable => commands.registerCommand(`wingman.${command_name}`, callback, this_arg)
