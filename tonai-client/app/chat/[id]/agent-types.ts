import { WithMessages } from "@/hooks/useLangGraphAgent/types";

// The agent state which mirrors the LangGraph state. If your sate have messages, extend WithMessages interface.
export interface AgentState extends WithMessages {
  swap_quote_id: string;
}

// export interface SwapData {
//   contractAddress: string;
//   entrypoint: string;
//   calldata: [string];
//   done: boolean;
// }

// All possible interrupt types from the graph. We are using string for Reminder node
export type InterruptValue = string | number | { "question": string };

// All possible resume types to send to the graph. We are using string for Reminder node
export type ResumeValue = string | number;
