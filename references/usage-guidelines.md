# Usage Guidelines

Novaflameの一貫した使用方法を定義するガイドラインです。いつどのコンポーネントやカラーを使うべきかを明確にします。

## 基本原則

**novaflameスキル使用時の絶対的なルール:**

### ✅ やるべきこと
- 既存コンポーネント（Atoms, Molecules, Frames, Layouts, Features）を組み合わせて使用する
- components-catalog.mdから適切なコンポーネントを選択する
- layout-patterns.mdのパターンを参考にする

### ❌ やってはいけないこと
- **新しいコンポーネントファイルを作成しない**（src/components/配下に新規ファイルを作らない）
- **既存コンポーネントを編集・変更しない**（Atoms, Molecules, Frames, Layouts, Featuresのファイルを変更しない）
- カスタムコンポーネントを作らず、既存の組み合わせで実現する

**理由**: デザインシステムの一貫性を保ち、コンポーネントライブラリを統一的に管理するためです。

---

## Table of Contents

- [基本原則](#基本原則)
- [コンポーネント選択ガイドライン](#コンポーネント選択ガイドライン)
- [カラー使用ルール](#カラー使用ルール)
- [スペーシングルール](#スペーシングルール)
- [タイポグラフィ階層](#タイポグラフィ階層)
- [インタラクションパターン](#インタラクションパターン)
- [Frames使用ルール（推奨バリアント）](#frames使用ルール推奨バリアント)

---

## コンポーネント選択ガイドライン

### Buttonのvariant選択

| Variant | 使用場面 | 例 |
|---------|---------|---|
| `primary` | **主要アクション**。ページで最も重要な操作。1ページに1つ推奨。 | 「保存」「送信」「作成」「次へ」 |
| `secondary` | **副次的アクション**。主要アクションをサポートする操作。削除などの破壊的な操作もこれを使用。 | 「キャンセル」「戻る」「編集」「削除」 |
| `ghost` | **軽微なアクション**。目立たせたくない操作。 | 「詳細」「もっと見る」「折りたたむ」 |

**🚨 このプロジェクト固有の重要ルール:**
- **`danger`バリアント（赤色）は使用禁止**
- 削除などの破壊的な操作には`secondary`バリアントを使用する
- すべてのボタンは`primary`, `secondary`, `ghost`のいずれかを使用する

**原則:**
- 1つの画面にprimaryボタンは1つまで（例外：モーダル内は別カウント）
- 削除などの破壊的な操作には`secondary`を使用（赤色は使わない）
- 確認ダイアログでは、安全な選択肢（キャンセル）を左、破壊的な選択肢を右に配置

```tsx
// ✅ 良い例：明確なアクション階層
<div className="flex gap-4">
  <Button variant="secondary">キャンセル</Button>
  <Button variant="primary">保存</Button>
</div>

// ✅ 良い例：削除ボタンもsecondaryを使用
<div className="flex gap-4">
  <Button variant="secondary">ダウンロード</Button>
  <Button variant="secondary">削除</Button>  {/* 赤色は使わない */}
</div>

// ❌ 悪い例：primaryが複数
<div className="flex gap-4">
  <Button variant="primary">保存</Button>
  <Button variant="primary">送信</Button>  {/* 混乱を招く */}
</div>

// ❌ 悪い例：dangerバリアント使用（使用禁止）
<div className="flex gap-4">
  <Button variant="secondary">キャンセル</Button>
  <Button variant="danger">削除</Button>  {/* このプロジェクトでは使用禁止 */}
</div>
```

### Containerのvariant選択

| Variant | 使用場面 | max-width |
|---------|---------|-----------|
| `narrow` | フォーム、記事、ログインページなど読みやすさ重視 | 768px (max-w-3xl) |
| `main` | 一般的なページ、デフォルト | 1024px (max-w-5xl) |
| `wide` | ダッシュボード、テーブル、グリッド表示 | 1280px (max-w-7xl) |
| `full` | 全幅が必要なページ（エディタなど） | 無制限 |

**原則:**
- テキストの読みやすさを優先する場合は`narrow`
- 迷ったら`main`を選択
- データテーブルやダッシュボードは`wide`

### Panelのvariant選択

| Variant | 使用場面 | 視覚的特徴 |
|---------|---------|-----------|
| `default` | シンプルなカード | 背景色のみ |
| `elevated` | 重要なコンテンツ、浮き上がった印象 | 背景色 + 影 |
| `bordered` | 明確な区切りが必要な場合 | 背景色 + ボーダー |

**原則:**
- ダークテーマでは`elevated`（影が映える）
- ライトテーマでは`bordered`も選択肢
- 複数のPanelを並べる場合は、すべて同じvariantを使用

---

## カラー使用ルール

### セマンティックカラーの意味と使用

| カラー | 意味 | 使用場面 | Tailwindクラス |
|--------|------|---------|---------------|
| **Accent** (ティール) | ブランド、アクション、強調 | リンク、プライマリボタン、フォーカス | `bg-accent`, `text-text-primary`, `border-accent` |
| **Error** (赤) | エラー、警告、削除 | エラーメッセージ、削除ボタン | `bg-error`, `text-error`, `border-error` |
| **Success** (緑) | 成功、完了 | 成功メッセージ、完了状態 | `bg-success`, `text-success`, `border-success` |
| **Neutral** (グレー) | 通常のUI、背景、ボーダー | ほとんどのUI要素 | `bg-main`, `bg-base`, `border-border` |

### カラー使用の原則

1. **globals.cssを必ず参照する**: ページを作成する際は、必ず`src/app/globals.css`を確認し、定義されているセマンティックカラーのみを使用する
2. **セマンティックトークンを使用**: プリミティブカラー（`#00c6ab`など）を直接使わない
3. **Tailwindデフォルトカラーを使わない**: `text-yellow-400`、`bg-red-500`などのTailwindデフォルトカラーは使用禁止。globals.cssに定義されたセマンティックカラーのみ使用
4. **カラーだけで情報を伝えない**: エラーは赤色+テキスト/アイコン
5. **ブランドカラーは控えめに**: アクセントカラーは重要な要素のみ
6. **テーマ対応**: セマンティックトークンを使えば自動でテーマ切り替え対応

```tsx
// ✅ 良い例：globals.cssのセマンティックトークン使用
<div className="bg-base border border-border">
  <p className="text-text-base">メッセージ</p>
  <p className="text-error">エラー: 入力が不正です</p>
  <p className="text-accent">重要な情報</p>
</div>

// ❌ 悪い例1: プリミティブカラー直接使用
<div className="bg-[#1a1a1a] border border-[#333333]">
  <p className="text-[#ffffff]">メッセージ</p>
  <p className="text-[#dc2626]">エラー</p>
</div>

// ❌ 悪い例2: Tailwindデフォルトカラー使用
<div className="bg-gray-900 border border-gray-700">
  <p className="text-white">メッセージ</p>
  <p className="text-red-500">エラー</p>
  <p className="text-yellow-400">警告</p>  {/* globals.cssに未定義 */}
</div>
```

### ステート表示のカラールール

| ステート | カラー | アイコン/テキスト | 例 |
|---------|--------|------------------|---|
| 成功 | `text-success` + `bg-success-bg` | ✓ 成功しました | 保存完了 |
| エラー | `text-error` + `bg-error-bg` | ✗ エラーが発生しました | バリデーションエラー |
| 情報 | `text-text-primary` + `bg-accent/10` | ℹ お知らせ | ヒント、通知 |
| 警告 | `text-error` | ⚠ 注意してください | 削除前の警告 |

```tsx
// 成功メッセージ
<div className="bg-success-bg border border-success p-4 rounded-lg">
  <p className="text-success">✓ 保存に成功しました</p>
</div>

// エラーメッセージ
<div className="bg-error-bg border border-error p-4 rounded-lg">
  <p className="text-error">✗ 入力内容に誤りがあります</p>
</div>
```

---

## スペーシングルール

### コンポーネント間のスペーシング

Novaflameは8pxグリッドシステムを採用しています。**8の倍数**を優先的に使用してください。

| 用途 | 推奨値 | Tailwindクラス | 実際の値 |
|------|--------|---------------|----------|
| 非常に小さい余白 | 0.5, 1 | `p-0.5`, `p-1`, `gap-1` | 2px, 4px |
| 小さい余白 | 2 | `p-2`, `gap-2` | 8px |
| 標準余白 | 4 | `p-4`, `gap-4` | 16px |
| 中程度の余白 | 6, 8 | `p-6`, `gap-6`, `p-8` | 24px, 32px |
| 大きい余白 | 12, 16 | `py-12`, `py-16` | 48px, 64px |

### スペーシングの階層

```tsx
// コンポーネント内部の小さい余白: gap-2 (8px)
<div className="flex items-center gap-2">
  <Icon />
  <span>テキスト</span>
</div>

// コンポーネント内のパディング: p-4 (16px)
<Panel padding="md">  {/* p-4 */}
  <h2>タイトル</h2>
  <p>コンテンツ</p>
</Panel>

// コンポーネント間の余白: gap-4 (16px) または gap-6 (24px)
<div className="space-y-6">
  <Panel>カード1</Panel>
  <Panel>カード2</Panel>
</div>

// セクション間の余白: py-8 (32px) または py-12 (48px)
<Section padding="lg">  {/* py-12 */}
  <h1>セクション</h1>
</Section>
```

### 原則

1. **8の倍数を優先**: 8px, 16px, 24px, 32px, 48px, 64px
2. **一貫性**: 同じ階層のコンポーネントは同じスペーシング
3. **space-yを活用**: 垂直方向のスタックには`space-y-{n}`
4. **任意の値は避ける**: `p-[13px]`のような任意の値は使わない

```tsx
// ✅ 良い例：8の倍数
<div className="space-y-6">  {/* 24px */}
  <Panel padding="md">  {/* 16px */}
    <div className="flex gap-4">  {/* 16px */}
      <Button>ボタン1</Button>
      <Button>ボタン2</Button>
    </div>
  </Panel>
</div>

// ❌ 悪い例：任意の値
<div className="space-y-[13px]">
  <Panel className="p-[17px]">
    <div className="flex gap-[9px]">
      ...
    </div>
  </Panel>
</div>
```

---

## タイポグラフィ階層

### 見出しレベルの使い分け

| レベル | フォントサイズ | フォントウェイト | 使用場面 | Tailwindクラス |
|--------|--------------|----------------|---------|---------------|
| H1 | 32px | Bold | ページタイトル（1ページに1つ） | `text-3xl font-bold` |
| H2 | 24px | Bold | メインセクション見出し | `text-2xl font-bold` |
| H3 | 21px | Bold | サブセクション見出し | `text-xl font-bold` |
| H4 | 18px | Bold | 小セクション、カードタイトル | `text-lg font-bold` |
| Body Large | 18px | Normal | リード文、強調したい本文 | `text-lg` |
| Body | 16px | Normal | 通常の本文、デフォルト | `text-base` |
| Caption | 14px | Normal | 補足情報、説明文 | `text-sm` |
| Small | 12px | Normal | 最小のテキスト、ラベル | `text-xs` |

### タイポグラフィの原則

1. **階層を守る**: H1→H2→H3の順序を守る（H1の次にH3を使わない）
2. **1ページにH1は1つ**: ページタイトルのみ
3. **本文はtext-base**: 通常のテキストは16px
4. **小さすぎない**: 12px未満は使わない

### 使用例

```tsx
// ページタイトル
<h1 className="text-3xl font-bold mb-8">ダッシュボード</h1>

// セクション見出し
<h2 className="text-2xl font-bold mb-6">最近のアクティビティ</h2>

// サブセクション
<h3 className="text-xl font-bold mb-4">今週の統計</h3>

// カードタイトル
<Panel>
  <h4 className="text-lg font-bold mb-2">タスク一覧</h4>
  <p className="text-base">ここに本文が入ります。</p>
  <p className="text-sm text-text-sub">補足情報や説明文</p>
</Panel>
```

### 日本語テキストの配慮

日本語テキストにはレタースペーシングを追加：

```tsx
// 日本語見出し
<h1 className="text-3xl font-bold tracking-wide">
  日本語のタイトル
</h1>

// 英語見出し（tracking不要）
<h1 className="text-3xl font-bold">
  English Title
</h1>
```

---

## インタラクションパターン

### ローディング状態

```tsx
// ボタンのローディング状態
<Button variant="primary" loading>
  処理中...
</Button>

// ページ全体のローディング
<div className="flex items-center justify-center h-screen">
  <div className="w-8 h-8 border-4 border-accent border-t-transparent rounded-full animate-spin" />
</div>

// コンテンツのスケルトン
<Panel padding="md">
  <div className="animate-pulse space-y-4">
    <div className="h-4 bg-border rounded w-3/4"></div>
    <div className="h-4 bg-border rounded w-1/2"></div>
  </div>
</Panel>
```

### エラー状態

```tsx
// Inputのエラー状態
<Input
  placeholder="メールアドレス"
  error="有効なメールアドレスを入力してください"
/>

// ページレベルのエラー
<Panel variant="bordered" padding="lg">
  <div className="text-center">
    <p className="text-error text-xl font-bold mb-2">
      ✗ エラーが発生しました
    </p>
    <p className="text-text-sub">
      ページの読み込みに失敗しました。再度お試しください。
    </p>
    <Button variant="primary" className="mt-4">
      再読み込み
    </Button>
  </div>
</Panel>
```

### 空状態（Empty State）

```tsx
<Panel variant="bordered" padding="lg">
  <div className="text-center py-12">
    <p className="text-xl font-bold mb-2">まだ項目がありません</p>
    <p className="text-text-sub mb-6">
      最初の項目を作成してみましょう
    </p>
    <Button variant="primary">+ 新規作成</Button>
  </div>
</Panel>
```

### ホバー状態

```tsx
// カードのホバー
<Panel
  variant="elevated"
  className="transition-transform hover:scale-105 cursor-pointer"
>
  クリック可能なカード
</Panel>

// ボタンのホバー（既に定義済み）
<Button variant="primary">
  ホバーでopacityが変わる
</Button>
```

---

## ベストプラクティスチェックリスト

新しいページを作成する際は、以下を確認してください：

### デザインの一貫性
- [ ] **globals.cssを参照した**（`src/app/globals.css`を確認し、定義されたセマンティックカラーを把握）
- [ ] セマンティックトークン（`bg-main`、`text-text-base`、`text-accent`、`text-error`など）を使用している
- [ ] プリミティブカラー（`#00c6ab`など）を直接使っていない
- [ ] **Tailwindデフォルトカラー**（`text-yellow-400`、`bg-red-500`など）を使っていない
- [ ] スペーシングは8の倍数（8px, 16px, 24px...）
- [ ] タイポグラフィ階層が適切（H1→H2→H3）

### コンポーネント選択
- [ ] 適切なContainerのvariantを選択している
- [ ] 1ページにprimaryボタンは1つまで
- [ ] **dangerバリアント（赤色）は使用していない（使用禁止）**
- [ ] 削除などの破壊的な操作にはsecondaryボタンを使用
- [ ] 既存コンポーネントを組み合わせている（新規作成していない）

### インタラクション
- [ ] ローディング状態を実装している
- [ ] エラー状態を実装している
- [ ] 空状態（Empty State）を実装している
- [ ] ホバー状態が明確

### アクセシビリティ
- [ ] キーボードで操作可能
- [ ] フォーカスリングが表示される
- [ ] カラーコントラストが十分（4.5:1以上）
- [ ] ARIA属性が適切に設定されている

**原則**: 一貫性のあるデザインは、ユーザーの学習コストを下げ、使いやすさを向上させます。

---

## Frames使用ルール（推奨バリアント）

**重要**: novaflameでページを構築する際は、まず**Framesを決めてから**中にコンポーネントを入れていきます。以下の推奨バリアントを使用することで、デザインの一貫性を保ちます。

### 推奨バリアントの原則

1. **迷ったら推奨バリアントを使う**: 各Framesコンポーネントには推奨バリアントが定義されています
2. **Container → Section → GridFrame/Panel の順で決める**: レイアウトは外側から内側へ構築
3. **一貫性を保つ**: 同じ種類のページでは同じFramesバリアントを使用

---

### Container の推奨バリアント

| バリアント | 推奨度 | 使用場面 | max-width |
|-----------|-------|---------|-----------|
| **`main`** | ⭐⭐⭐ **推奨** | 一般的なページ（デフォルト） | 1024px (max-w-5xl) |
| `narrow` | ⭐⭐ | フォーム、記事、ログインページ | 768px (max-w-3xl) |
| `wide` | ⭐⭐ | ダッシュボード、テーブル、グリッド表示 | 1280px (max-w-7xl) |
| `full` | ⭐ | エディタなど全幅が必要なページ | 無制限 |

**推奨例**:
```tsx
// ✅ 推奨: 一般的なページ
<Container variant="main">
  <PageTitle>ユーザー管理</PageTitle>
  {/* コンテンツ */}
</Container>

// ✅ 推奨: フォームページ
<Container variant="narrow">
  <form>...</form>
</Container>
```

---

### Section の推奨バリアント

| バリアント | 推奨度 | 使用場面 | 背景色 |
|-----------|-------|---------|--------|
| **`main`** | ⭐⭐⭐ **推奨** | アプリケーション標準背景 | bg-main |
| `default` | ⭐⭐ | 透明背景が必要な場合 | 透明 |
| `base` | ⭐⭐ | ベース背景 | bg-base |
| `accent` | ⭐ | Hero、CTAセクション | bg-accent/10 |

**固定padding**: `p-8` (32px) - すべての方向に32px

**推奨例**:
```tsx
// ✅ 推奨: 標準的なページセクション
<Section variant="main">
  <Container variant="main">
    {/* コンテンツ */}
  </Container>
</Section>
```

---

### Panel の推奨バリアント

| バリアント | 推奨度 | 使用場面 | 視覚的特徴 |
|-----------|-------|---------|-----------|
| **`elevated`** | ⭐⭐⭐ **推奨** | カード型UI、重要なコンテンツ | 背景色 + 影 (shadow-lg) |
| `bordered` | ⭐⭐ | 明確な区切りが必要な場合 | 背景色 + ボーダー |
| `default` | ⭐ | シンプルなカード | 背景色のみ |

| Padding | 推奨度 | 値 | 使用場面 |
|---------|-------|---|---------|
| **`md`** | ⭐⭐⭐ **推奨** | 16px (p-4) | 標準的なカード |
| `sm` | ⭐⭐ | 8px (p-2) | コンパクトなカード |
| `lg` | ⭐⭐ | 24px (p-6) | 余白が必要な場合 |
| `none` | ⭐ | 0px (p-0) | カスタムレイアウト |

**推奨例**:
```tsx
// ✅ 推奨: 統計カード
<Panel variant="elevated" padding="md">
  <h2 className="text-xl font-bold mb-4">統計</h2>
  <p className="text-2xl">1,234</p>
</Panel>
```

---

### GridFrame の推奨バリアント

| Columns | 推奨度 | 使用場面 |
|---------|-------|---------|
| **`3`** | ⭐⭐⭐ **推奨** | ダッシュボード統計カード |
| `2` | ⭐⭐ | 2カラムレイアウト |
| `4` | ⭐⭐ | 多数のアイテム表示 |
| `1` | ⭐ | リスト表示 |

| Gap | 推奨度 | 値 | 使用場面 |
|-----|-------|---|---------|
| **`md`** | ⭐⭐⭐ **推奨** | 16px (gap-4) | 標準的な間隔 |
| `sm` | ⭐⭐ | 8px (gap-2) | コンパクトな表示 |
| `lg` | ⭐⭐ | 24px (gap-6) | ゆったりした表示 |

**推奨例**:
```tsx
// ✅ 推奨: 3カラムダッシュボード
<GridFrame columns={3} gap="md">
  <Panel variant="elevated" padding="md">統計1</Panel>
  <Panel variant="elevated" padding="md">統計2</Panel>
  <Panel variant="elevated" padding="md">統計3</Panel>
</GridFrame>
```

---

### SidebarContainer の推奨バリアント

| Props | 推奨値 | 理由 |
|-------|-------|------|
| **`width`** | `"md"` (256px) | 標準的なサイドバー幅 |
| **`background`** | `"main"` | 統一感のある背景 |
| **`border`** | `"right"` (左サイドバー) / `"left"` (右サイドバー) | 視覚的区切り |
| **`collapsible`** | `true` | ユーザー体験向上 |
| **`fullHeight`** | `true` | 全高表示 |

**推奨例**:
```tsx
// ✅ 推奨: 開閉可能な左サイドバー
<SidebarContainer
  width="md"
  background="main"
  border="right"
  collapsible={true}
  fullHeight={true}
>
  {/* サイドバーコンテンツ */}
</SidebarContainer>
```

---

### ScrollArea の推奨バリアント

| Direction | 推奨度 | 使用場面 |
|-----------|-------|---------|
| **`vertical`** | ⭐⭐⭐ **推奨** | 縦スクロール（デフォルト） |
| `horizontal` | ⭐⭐ | 横スクロールが必要 |
| `both` | ⭐ | 両方向スクロール |

**推奨例**:
```tsx
// ✅ 推奨: 縦スクロール
<ScrollArea direction="vertical" height="400px">
  {/* 長いコンテンツ */}
</ScrollArea>
```

---

### Modal の推奨バリアント

| Size | 推奨度 | max-width | 使用場面 |
|------|-------|-----------|---------|
| **`md`** | ⭐⭐⭐ **推奨** | max-w-2xl | 一般的なモーダル |
| `sm` | ⭐⭐ | max-w-md | 確認ダイアログ |
| `lg` | ⭐⭐ | max-w-4xl | フォームモーダル |
| `xl` | ⭐ | max-w-6xl | 特大コンテンツ |
| `full` | ⭐ | 全画面 | エディタなど |

| Props | 推奨値 | 理由 |
|-------|-------|------|
| **`closeOnOverlayClick`** | `true` | ユーザー体験向上 |

**推奨例**:
```tsx
// ✅ 推奨: 一般的なモーダル
<Modal isOpen={isOpen} onClose={onClose} size="md" closeOnOverlayClick={true}>
  <div className="p-6">
    <h2 className="text-xl font-bold mb-4">モーダルタイトル</h2>
    {/* コンテンツ */}
  </div>
</Modal>
```

---

### Frames構築の推奨フロー

新しいページを作成する際は、以下の順序でFramesを決定します:

```tsx
// ステップ1: Containerでmax-widthを決める
<Container variant="main">  {/* または narrow/wide/full */}

  // ステップ2: 必要に応じてSectionで背景とpaddingを設定
  <Section variant="main">  {/* または default/base/accent */}

    // ステップ3: レイアウトが必要ならGridFrameを使う
    <GridFrame columns={3} gap="md">

      // ステップ4: カード型のUIならPanelを使う
      <Panel variant="elevated" padding="md">

        // ステップ5: 中にAtomsやMoleculesを配置
        <h2>タイトル</h2>
        <p>コンテンツ</p>
        <Button variant="primary">ボタン</Button>

      </Panel>

    </GridFrame>

  </Section>

</Container>
```

**重要**: Framesを決めてから中にコンポーネントを入れていくことで、一貫性のあるレイアウトを実現できます。
