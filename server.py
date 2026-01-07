# /// script
# dependencies = [
#   "mcp",
#   "httpx"
# ]
# ///

import httpx
import asyncio
from mcp.server.fastmcp import FastMCP

# ==========================================
# 設定
# ==========================================
ORG_NAME = "hexabase"
REPO_NAME = "novaflame"
BRANCH = "main"

BASE_URL = f"https://raw.githubusercontent.com/{ORG_NAME}/{REPO_NAME}/{BRANCH}"
SKILL_ROOT = ""

FILES_TO_LOAD = {
    "Main Skill": "SKILL.md",
    "Accessibility": "references/accessibility.md",
    "Components Catalog": "references/components-catalog.md",
    "Design System": "references/design-system.md",
    "Layout Patterns": "references/layout-patterns.md",
    "Usage Guidelines": "references/usage-guidelines.md"
}

mcp = FastMCP("Novaflame")

async def fetch_file(client, label, relative_path):
    # パスの調整
    if SKILL_ROOT:
        path = f"{SKILL_ROOT}/{relative_path}"
    else:
        path = relative_path
    
    # スラッシュが重複しないように調整
    path = path.lstrip("/")
    
    url = f"{BASE_URL}/{path}"
    try:
        response = await client.get(url)
        if response.status_code == 200:
            return f"\n\n--- {label} ({relative_path}) ---\n{response.text}"
        else:
            return f"\n\n--- {label} ---\n[Error: {response.status_code} Not Found at {url}]"
    except Exception as e:
        return f"\n\n--- {label} ---\n[Error: {str(e)}]"

async def get_combined_context() -> str:
    """全ファイルを結合したテキストを返すヘルパー関数"""
    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_file(client, label, path) 
            for label, path in FILES_TO_LOAD.items()
        ]
        results = await asyncio.gather(*tasks)

    combined_text = """
=== NOVAFLAME DESIGN SYSTEM ===
以下のデザインシステムとガイドラインに従って実装を行ってください。
"""
    combined_text += "".join(results)
    return combined_text

# ---------------------------------------------------------
# 1. ツールとしての定義 (Claudeが「発動」と言われたらこれを使う)
# ---------------------------------------------------------
@mcp.tool()
async def load_novaflame_design_system() -> str:
    """
    Novaflameデザインシステム全体（SKILL.mdおよび全リファレンス）を読み込みます。
    ユーザーから「Novaflame発動」「デザインシステムを適用して」などの指示があった場合に実行してください。
    """
    return await get_combined_context()

# ---------------------------------------------------------
# 2. リソースとしての定義 (Claudeが中身を探索したい場合に使う)
# ---------------------------------------------------------
@mcp.resource("novaflame://system/all")
async def get_novaflame_resource() -> str:
    """Novaflameデザインシステムの全テキストデータ"""
    return await get_combined_context()

if __name__ == "__main__":
    mcp.run()