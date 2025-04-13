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


        {/* CTA Button */}
        <div className="text-center">
          <button
            className="bg-primary text-primary-foreground hover:opacity-90 transition-opacity px-8 py-4 rounded-lg text-lg font-medium"
            onClick={handleAddChat}
            disabled={!walletAddress}
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

