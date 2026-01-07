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
# 設定: GitHubリポジトリの情報
# ==========================================
ORG_NAME = "hexabase"
REPO_NAME = "novaflame"
BRANCH = "main"

# GitHubのRawデータアクセスのベースURL
BASE_URL = f"https://raw.githubusercontent.com/{ORG_NAME}/{REPO_NAME}/{BRANCH}"

# 読み込むファイルリスト
# 左側: ログに表示される名前, 右側: リポジトリルートからの相対パス
FILES_TO_LOAD = {
    "Main Skill": "SKILL.md",
    "Accessibility": "references/accessibility.md",
    "Components Catalog": "references/components-catalog.md",
    "Design System": "references/design-system.md",
    "Layout Patterns": "references/layout-patterns.md",
    "Usage Guidelines": "references/usage-guidelines.md"
}

# サーバー名の定義
mcp = FastMCP("Novaflame")

async def fetch_file(client, label, relative_path):
    """ファイルを非同期で取得する関数"""
    url = f"{BASE_URL}/{relative_path}"
    
    try:
        response = await client.get(url)
        if response.status_code == 200:
            # 取得成功時
            return f"\n\n--- {label} ({relative_path}) ---\n{response.text}"
        else:
            # ファイルが見つからないなどのエラー時
            return f"\n\n--- {label} ---\n[Error: {response.status_code} Not Found at {url}]"
    except Exception as e:
        # 通信エラー時
        return f"\n\n--- {label} ---\n[Error: {str(e)}]"

@mcp.prompt()
async def novaflame_skill() -> str:
    """Novaflameデザインシステムと全リファレンスをロードして発動します"""
    
    async with httpx.AsyncClient() as client:
        # 定義された全ファイルを並列で一気に取得（高速化）
        tasks = [
            fetch_file(client, label, path) 
            for label, path in FILES_TO_LOAD.items()
        ]
        results = await asyncio.gather(*tasks)

    # プロンプトの組み立て
    combined_text = """
あなたはこれより、Hexabaseの「Novaflame Design System」の定義に従ってUI設計・実装を行います。
以下に定義されているメインスキルと、すべてのリファレンスガイドラインを遵守してください。

==================================================
NOVAFLAME DESIGN SYSTEM CONTEXT
==================================================
"""
    # 取得した全テキストを結合
    combined_text += "".join(results)
    
    combined_text += """
==================================================
ロード完了。指示を待機中。
"""
    return combined_text

if __name__ == "__main__":
    mcp.run()