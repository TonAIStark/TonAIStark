"use client"

import { DollarSign, ArrowUpFromDot, ArrowDownToDot } from "lucide-react"
import { Card } from "@/components/ui/card"
import { motion } from "framer-motion"
import { Arrow } from "@radix-ui/react-tooltip"

interface SwapCardProps {
  priceIn: number;
  priceOut: number;
  priceRatio: number;
}

export default function SwapCard({ priceIn, priceOut, priceRatio }: SwapCardProps) {
  return (
    <Card className="relative overflow-hidden group w-72 h-40 cursor-pointer transition-all hover:shadow-lg">
      {/* Gradient Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-orange-50 via-yellow-50 to-orange-100 dark:from-amber-900/20 dark:via-yellow-900/20 dark:to-orange-800/30 opacity-50" />

      {/* Content Container */}
      <div className="relative h-full p-6 flex flex-col justify-between">
        {/* Top Section */}
        <div className="flex items-center space-x-4">
          <div className="relative p-2 bg-amber-100 dark:bg-amber-900/40 rounded-full group-hover:bg-amber-200 dark:group-hover:bg-amber-800/60 transition-colors">
            {/* Animated Sun Rays Effect */}
            {[...Array(10)].map((_, i) => (
              <motion.div
                key={i}
                className="absolute w-16 h-0.5 bg-amber-200 dark:bg-yellow-500/30"
                style={{
                  left: "50%",
                  top: "50%",
                  rotate: i * 30,
                  transformOrigin: "0 50%",
                  transform: "translateY(-50%)",
                }}
                animate={{
                  opacity: [0.3, 0.8, 0.3],
                  scale: [1, 1.2, 1],
                }}
                transition={{
                  duration: 2,
                  repeat: Number.POSITIVE_INFINITY,
                  delay: i * 0.2,
                  ease: "easeInOut",
                }}
              />
            ))}
          </div>
          <div>
            <h3 className="text-xl font-semibold text-gray-800 dark:text-gray-100">AVNU Swap</h3>
            <p className="text-sm text-gray-600 dark:text-gray-400">Click here to submit</p>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="flex justify-between items-center mt-4">
          <div className="flex items-center space-x-1 text-gray-600 dark:text-gray-400">
            <ArrowUpFromDot className="w-4 h-4" />
            <DollarSign className="w-4 h-4" />
            <span className="text-sm">{priceIn.toFixed(2)}</span>
          </div>
          <div className="flex items-center space-x-1 text-gray-600 dark:text-gray-400">
            <ArrowDownToDot className="w-4 h-4" />
            <DollarSign className="w-4 h-4" />
            <span className="text-sm">{priceOut.toFixed(2)}</span>
          </div>
          <div className="text-l font-bold text-gray-800 dark:text-gray-100">{priceRatio.toFixed(2)}%</div>
        </div>
      </div>
    </Card>
  )
}

