import { AgentState } from "../../agent-types";
import { Loader2 } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import SwapCard from "./swap-card";

interface SwapNodeProps {
  nodeState: Partial<AgentState>;
}

export default function SwapNode({ nodeState }: SwapNodeProps) {
  
  async function someAsyncFunction(swapData: Record<string, any>): Promise<any> {
    const provider = (window as any).starknet;
  
    if (!provider) {
      alert("Argent X not found");
      return;
    }
  
    try {
      await provider.enable();
      const account = provider.account;
      
      console.log("Account:", account.address);
      console.log("Swap Data:", swapData.quoteId);
      const url = "https://sepolia.api.avnu.fi/swap/v2/build";

      const payload = {
        quoteId: swapData.quoteId,            // parameter passed via swapData
        takerAddress: account.address,  // parameter passed via swapData
        slippage: 0.05,
        includeApprove: true
      };

      
    
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "accept": "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });
    
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const responseDict = await response.json();
      console.log("Response JSON:", responseDict);
      
      // For each responseDict["calls"] element, you need to call the contract
      // and execute the function with the appropriate parameters 

      
      for (const call of responseDict.calls) {
        const tx = await account.execute({
          contractAddress: call.contractAddress, // Replace with real address
          entrypoint: call.entrypoint, // Replace with actual function name
          calldata: call.calldata // Adjust arguments to match ABI
        });
          console.log("Transaction sent! Hash:", tx.transaction_hash);

          // Delay 3 seconds before checking the transaction status
          await new Promise(resolve => setTimeout(resolve, 3000));
          
      }
    } catch (err) {
      console.error("Transaction error:", err);
    }
  };


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

  if (!nodeState?.swap_data) {
    return null;
  }

  return (
    <div className="flex justify-end">
      <div onClick={handleCall}>
        <SwapCard priceIn={nodeState?.swap_data.sellAmountInUsd} priceOut={nodeState?.swap_data.buyAmountInUsd} priceRatio={nodeState?.swap_data.priceRatioUsd} />
      </div>
    </div>
  );

}