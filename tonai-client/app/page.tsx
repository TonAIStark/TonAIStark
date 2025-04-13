'use client'

import { useChatStore } from "@/stores/chat-store"
import { useRouter } from "next/navigation"
import { useState } from "react"
import { connectArgentX } from "@/lib/starknet"

export default function WelcomePage() {
  const { addChat } = useChatStore()
  const router = useRouter()
  const [walletAddress, setWalletAddress] = useState<string | null>(null)

  const handleAddChat = () => {
    const newChat = addChat()
    router.push(`/chat/${newChat.id}`)
  }

  const handleSendTransaction = async () => {
    const provider = (window as any).starknet;
  
    if (!provider) {
      alert("Argent X not found");
      return;
    }
  
    try {
      await provider.enable();
      const account = provider.account;
  
      const tx = await account.execute({
        contractAddress: "0x2c56e8b00dbe2a71e57472685378fc8988bba947e9a99b26a00fade2b4fe7c2", // Replace with real address
        entrypoint: "multi_route_swap", // Replace with actual function name
        calldata: [
          "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
          "0x8ac7230489e80000",
          "0x0",
          "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
          "0xe84a61acbc05f",
          "0x0",
          "0xdcad0ffdb29f3",
          "0x0",
          "0x6bcdf9e4a67af8d194d0bfd2778e23cdb4593604cca46f9afcc0dae0bcfe1b",
          "0x0",
          "0x0",
          "0x3",
          "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
          "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
          "0x444a09d96389aa7148f1aada508e30b71299ffe650d9c97fdaae38cb9a23384",
          "0x180f25810",
          "0x6",
          "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
          "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
          "0x20c49ba5e353f80000000000000000",
          "0x3e8",
          "0x0",
          "0x244ac2d3bad981346909982badd920",
          "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
          "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
          "0x444a09d96389aa7148f1aada508e30b71299ffe650d9c97fdaae38cb9a23384",
          "0xe8d4a51000",
          "0x6",
          "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
          "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
          "0x20c49ba5e353f80000000000000000",
          "0x3e8",
          "0x0",
          "0x76f40538a1d96f3ab632666faf",
          "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
          "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
          "0x444a09d96389aa7148f1aada508e30b71299ffe650d9c97fdaae38cb9a23384",
          "0xe8d4a51000",
          "0x6",
          "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
          "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
          "0x20c49ba5e353f80000000000000000",
          "0x3e8",
          "0x0",
          "0xd2814d35653ca3d8f72db6de3"
        ], // Adjust arguments to match ABI
      });
  
      console.log("Transaction sent! Hash:", tx.transaction_hash);
    } catch (err) {
      console.error("Transaction error:", err);
    }
  };
  

  const handleConnectWallet = async () => {
    const address = await connectArgentX()
    if (address) {
      setWalletAddress(address)
    } else {
      alert("Could not connect to Argent X")
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-background via-background/80 to-primary/5 flex items-center">
      <div className="container px-4 py-8 mx-auto space-y-12">
        {/* Hero Section */}
        <div className="text-center space-y-3 max-w-4xl mx-auto">
          <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
            Ton<span className="text-red-600">AI</span>-Stark
          </h1>
          <div className="h-1 w-20 bg-primary mx-auto rounded-full" />
        </div>

        {/* Wallet Connect Button */}
        <div className="text-center">
          <button
            className="bg-secondary text-secondary-foreground hover:opacity-90 transition-opacity px-6 py-3 rounded-lg text-base font-medium mr-4"
            onClick={handleConnectWallet}
          >
            {walletAddress ? `Connected: ${walletAddress.slice(0, 6)}...` : "Connect Argent X"}
          </button>
        </div>

        <div className="text-center">
          <button
            className="bg-blue-600 text-white hover:opacity-90 transition-opacity px-8 py-4 rounded-lg text-lg font-medium mt-4"
            onClick={handleSendTransaction}
          >
            Send Test Transaction
          </button>
        </div>


        {/* CTA Button */}
        <div className="text-center">
          <button
            className="bg-primary text-primary-foreground hover:opacity-90 transition-opacity px-8 py-4 rounded-lg text-lg font-medium"
            onClick={handleAddChat}
          >
            Start New Chat
          </button>
        </div>
      </div>
    </div>
  )
}


function FeatureBlock({
  title,
  description,
}: {
  title: string
  description: string
}) {
  return (
    <div className="group p-4 rounded-lg bg-secondary/5 hover:bg-secondary/10 transition-colors duration-300">
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p className="text-muted-foreground">{description}</p>
    </div>
  )
}

