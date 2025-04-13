// lib/starknet.ts
export async function connectArgentX(): Promise<string | null> {
  if (typeof window === "undefined") return null;

  const provider = (window as any).starknet;

  if (!provider) {
    alert("Argent X not detected. Please install it.");
    return null;
  }

  try {
    await provider.enable(); // Prompts user to connect
    return provider.selectedAddress;
  } catch (err) {
    console.error("Argent X connection error:", err);
    return null;
  }
}
