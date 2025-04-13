import { AgentState } from "../../agent-types";
import { Loader2 } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import SwapCard from "./swap-card";

interface SwapNodeProps {
  nodeState: Partial<AgentState>;
}

export default function SwapNode({ nodeState }: SwapNodeProps) {
  
  console.log("porcodio... Salvata:", nodeState?.swap_data);

  const handleCall = async () => {
    if (nodeState?.swap_data) {
      try {
        const result = await someAsyncFunction(nodeState.swap_data);
        console.log("Async function result:", result);
      } catch (error) {
        console.error("Async function error:", error);
      }
    }
  };

  if (nodeState?.swap_data) {
    return (
      <div className="flex justify-end">
        <Card className="inline-block">
          <CardContent className="p-2">
            <div className="flex items-center gap-2">
              <Loader2 className="w-6 h-6 animate-spin" />
              {/* Clicking the div triggers the async function */}
              <div className="text-sm" onClick={handleCall}>
                {nodeState.swap_data["quoteId"]}
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    );
   }

  if (nodeState?.swap_data) {
    return null;
  }

  return (
    <div className="flex justify-end">
      <SwapCard />
    </div>
  );

  return null;
}