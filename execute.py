"""Post-install verification: test Hermes connection."""
import asyncio
import sys
sys.path.insert(0, "/a0/usr/plugins/hermes_bridge")
from helpers.client import HermesClient

async def verify():
    print("\n[Hermes Bridge] Post-install verification...")
    client = HermesClient()
    try:
        health = await client.health()
        if health.get("healthy"):
            print(f"  ✅ Connection OK: {client.base_url}")
            tools = await client.list_tools()
            print(f"  ✅ Hermes tools: {len(tools)}")
            return True
        else:
            print(f"  ⚠️  Hermes not responding at {client.base_url}")
            print(f"  ℹ️  Configure base_url in plugin settings.")
            return False
    except Exception as e:
        print(f"  ❌ Connection failed: {e}")
        print(f"  ℹ️  Hermes Agent may not be running at {client.base_url}")
        return False

if __name__ == "__main__":
    ok = asyncio.run(verify())
    sys.exit(0 if ok else 0)
