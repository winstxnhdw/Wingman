import { workspace } from 'vscode'

interface Properties {
  serverPortNumber: number
  maxReadLines: number
}

export const get_property = <Key extends keyof Properties>(property_name: Key): Properties[Key] =>
  workspace.getConfiguration('wingman').get(property_name) as Properties[Key]
