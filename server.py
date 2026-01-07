# /// script
# dependencies = [
#   "mcp",
#   "httpx"
# ]
# ///

import httpx
from mcp.server.fastmcp import FastMCP

# ==========================================
# 1. 設定：ファイルの場所
# ==========================================
ORG = "hexabase"
REPO = "novaflame"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{ORG}/{REPO}/{BRANCH}"

# リファレンスのマップ（キー名: ファイルパス）
# ※ ここを増やせば、Claudeが読める本が増えます
REFERENCE_DOCS = {
    "components": "references/components-catalog.md",  # コンポーネント詳細
    "design": "references/design-system.md",          # 色・文字・トークン
    "layout": "references/layout-patterns.md",        # レイアウトパターン
    "usage": "references/usage-guidelines.md",        # ガイドライン
    "a11y": "references/accessibility.md"             # アクセシビリティ
}

MAIN_SKILL_FILE = "SKILL.md"

mcp = FastMCP("Novaflame")

async def fetch_github_text(path: str) -> str:
    """GitHubからRawテキストを取得する共通関数"""
    url = f"{BASE_URL}/{path.lstrip('/')}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return response.text
            return f"Error: {response.status_code} Not Found at {url}"
        except Exception as e:
            return f"Error: {str(e)}"

# ==========================================
# 2. 受付カウンター（発動用ツール）
# ==========================================
@mcp.tool()
async def activate_novaflame_system() -> str:
    """
    【必須】ユーザーが「Novaflame発動」と指示したら最初に実行するツール。
    
    システム全体をロードするのではなく、
    1. 基本ルール(SKILL.md)
    2. 利用可能なリファレンスのリスト(目次)
    をAIに認識させます。詳細は別途 read_reference ツールで取得させます。
    """
    # 1. 基本ルールだけ軽く読み込む
    skill_content = await fetch_github_text(MAIN_SKILL_FILE)
    
    # 2. 読める本のリストを作る
    docs_list = "\n".join([f"- {key}" for key in REFERENCE_DOCS.keys()])

    return f"""
✅ Novaflame System Activated (Librarian Mode).

基本ルールをロードしました。コンテキスト保護のため、詳細は分割管理されています。
実装時に詳細情報が必要になったら、必ずツール `read_novaflame_reference(key)` を使用して情報を取得してください。

■ 利用可能なリファレンスキー一覧:
{docs_list}

---
[基本ルール (SKILL.md)]
{skill_content}
"""

# ==========================================
# 3. 書庫（詳細取得用ツール）
# ==========================================
@mcp.tool()
async def read_novaflame_reference(key: str) -> str:
    """
    特定のリファレンス詳細を読み込みます。
    activate_novaflame_system 実行後、具体的な実装コードや仕様が必要になったタイミングで
    AIが自発的に呼び出してください。
    
    Args:
        key: 取得したいドキュメントのキー (例: "components", "layout", "design")
    """
    if key not in REFERENCE_DOCS:
        valid_keys = ", ".join(REFERENCE_DOCS.keys())
        return f"エラー: '{key}' というドキュメントはありません。利用可能: {valid_keys}"

    path = REFERENCE_DOCS[key]
    content = await fetch_github_text(path)
    
    return f"""
📖 REFERENCE LOADED: {key}
(Source: {path})
--------------------------------------------------
{content}
"""

if __name__ == "__main__":
    mcp.run()