import { AgentState } from "../../agent-types";
import { Loader2 } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import SwapCard from "./swap-card";

interface SwapNodeProps {
  nodeState: Partial<AgentState>;
}

export default function SwapNode({ nodeState }: SwapNodeProps) {
  console.log("SwapNode", nodeState);
  if (nodeState?.swap_data?.done === false) {
    return (
      <div className="flex justify-end">
        <Card className="inline-block">
          <CardContent className="p-2">
            <div className="flex items-center gap-2">
              <Loader2 className="w-6 h-6 animate-spin" />
              <div className="text-sm">{nodeState?.swap_data?.contractAddress}</div>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  if (nodeState?.swap_data?.done === true) {
    return null;
  }

  return (
    <div className="flex justify-end">
      <SwapCard />
    </div>
  );
}