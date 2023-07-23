import type { PromptResponse } from '@/api/types'
import got from 'got'

export class API {
  private port: number

  constructor(port: number) {
    this.port = port
  }

  private async request<T>(endpoint: string, body: Record<string, unknown>): Promise<T> {
    const response = await got
      .post(`http://localhost:${this.port}${endpoint}`, {
        json: body,
        retry: { limit: 0 },
      })
      .json()

    return response as T
  }

  async generate_text(prompt: string): Promise<PromptResponse> {
    return this.request<PromptResponse>('/v1/generate', {
      prompt: prompt,
    })
  }
}
