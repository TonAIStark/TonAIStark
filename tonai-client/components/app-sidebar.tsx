'use client'

import Link from "next/link"
import { usePathname, useRouter } from "next/navigation"
import {
  Sidebar,
  SidebarContent,
  SidebarHeader,
  SidebarFooter,
  SidebarGroup,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuButton,
  SidebarGroupLabel,
  SidebarGroupAction
} from "@/components/ui/sidebar"
import { Bot, Plus, MessageSquare } from "lucide-react"
import { useChatStore } from "@/stores/chat-store"
import ThemeSwitcher from "./theme-switcher"

export function AppSidebar() {
  const pathname = usePathname()
  const router = useRouter()
  const { chats, addChat } = useChatStore()

  const handleAddChat = () => {
    const newChat = addChat()
    router.push(`/chat/${newChat.id}`)
  }

  return (
    <Sidebar>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton size="lg" asChild>
              <Link href="/">
                <div className="flex aspect-square size-10 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                  <img src="/assets/tonai-icon-bgw.png" alt="AI" className="size-10 rounded-lg bg-white-100"/>
                </div>
                <span className="font-semibold">Ton<span className="text-red-600">AI</span>-Stark</span>
              </Link>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Chats</SidebarGroupLabel>
          <SidebarGroupAction title="Add Project" onClick={handleAddChat}>
            <Plus /> <span className="sr-only">New Chat</span>
          </SidebarGroupAction>
          <SidebarMenu>
            {chats.map((chat) => (
              <SidebarMenuItem key={chat.id}>
                <SidebarMenuButton asChild isActive={pathname === `/chat/${chat.id}`}>
                  <Link href={`/chat/${chat.id}`}>
                    <MessageSquare />
                    <span>{chat.name}</span>
                  </Link>
                </SidebarMenuButton>
              </SidebarMenuItem>
            ))}
          </SidebarMenu>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <div className="flex flex-col items-center text-sm gap-4 pb-2">
          <ThemeSwitcher />
        </div>
      </SidebarFooter>
    </Sidebar>
  )
}