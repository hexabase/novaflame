# Layout Patterns

Novaflameでよく使用されるレイアウトパターンのコレクション。既存コンポーネントの組み合わせで実現できるパターンを提供します。

---

## Frames構築の基本原則

**重要**: novaflameでページを構築する際は、必ず以下の原則に従ってください:

### 原則1: Framesを決めてから中にコンポーネントを入れる

Framesコンポーネント（Container, Section, Panel, GridFrame, SidebarContainer, ScrollArea, Modal）はレイアウトの**骨組み**です。まずFramesを決めてから、その中にAtomsやMoleculesを配置します。

```tsx
// ✅ 良い例: Framesを先に決める
<Container variant="main">        {/* 1. まずContainerで幅を決める */}
  <Section variant="main">        {/* 2. Sectionで背景を決める */}
    <GridFrame columns={3} gap="md">  {/* 3. GridFrameでレイアウトを決める */}
      <Panel variant="elevated" padding="md">  {/* 4. Panelでカード型UIを決める */}
        {/* 5. 最後にAtomsやMoleculesを配置 */}
        <PageTitle>タイトル</PageTitle>
        <Input placeholder="入力" />
        <Button variant="primary">送信</Button>
      </Panel>
    </GridFrame>
  </Section>
</Container>

// ❌ 悪い例: Framesを後から追加
<div>
  <h1>タイトル</h1>
  <input />
  <button>送信</button>
  {/* Framesがないため、レイアウトが一貫しない */}
</div>
```

### 原則2: 推奨バリアントを優先的に使用

各Framesコンポーネントには**推奨バリアント**が定義されています。迷ったら推奨バリアントを使用してください。

| Framesコンポーネント | 推奨バリアント |
|-------------------|--------------|
| Container | `variant="main"` |
| Section | `variant="main"` |
| Panel | `variant="elevated"` + `padding="md"` |
| GridFrame | `columns={3}` + `gap="md"` |
| SidebarContainer | `width="md"` + `background="main"` + `border="right"` + `collapsible={true}` |
| ScrollArea | `direction="vertical"` |
| Modal | `size="md"` + `closeOnOverlayClick={true}` |

詳細な推奨バリアントのガイドラインは [usage-guidelines.md](usage-guidelines.md#frames使用ルール推奨バリアント) を参照してください。

### 原則3: 外側から内側へ構築

レイアウトは必ず**外側から内側**へ構築します:

1. **Container**: max-widthを決める
2. **Section**: 背景色とpaddingを決める
3. **GridFrame / SidebarContainer**: レイアウト構造を決める
4. **Panel**: カード型UIを決める
5. **Atoms / Molecules**: 具体的なコンテンツを配置

```tsx
// ✅ 正しい順序: 外側から内側へ
Container → Section → GridFrame → Panel → Atoms/Molecules

// ❌ 誤った順序: 内側から外側へ
Atoms/Molecules → Panel → GridFrame → Section → Container
```

---

## Table of Contents

- [アプリケーション全体のレイアウトタイプ](#アプリケーション全体のレイアウトタイプ)
  - [タイプ1: シンプルレイアウト（ヘッダーのみ）](#タイプ1-シンプルレイアウトヘッダーのみ)
  - [タイプ2: ナビゲーションレイアウト（ヘッダー + サイドバー）](#タイプ2-ナビゲーションレイアウトヘッダー--サイドバー)
  - [タイプ3: 詳細レイアウト（ヘッダー + 左右サイドバー）](#タイプ3-詳細レイアウトヘッダー--左右サイドバー)
- [ダッシュボードレイアウト](#ダッシュボードレイアウト)
- [フォームページ](#フォームページ)
- [リスト/グリッドページ](#リストグリッドページ)
- [詳細画面](#詳細画面)
- [設定画面](#設定画面)
- [モーダルダイアログ](#モーダルダイアログ)

---

## アプリケーション全体のレイアウトタイプ

**重要**: すべてのページは基本的に共通のHeaderコンポーネントを使用します。以下の3つのレイアウトタイプから適切なものを選択してください。

### タイプ1: シンプルレイアウト（ヘッダーのみ）

ヘッダーのみを表示し、サイドバーなしのシンプルな構成。

**適用ページ例**: ユーザー管理、設定ページ、フォーム、詳細画面など

```tsx
import { Header } from '@/components/layouts/Header';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <main className="flex-1">
        {children}
      </main>
    </div>
  );
}
```

**使用例（ユーザー管理ページ）**:

```tsx
import { Header } from '@/components/layouts/Header';
import { Container } from '@/components/frames/Container';
import { Section } from '@/components/frames/Section';
import { Panel } from '@/components/frames/Panel';

export default function UsersPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <Section variant="main" padding="lg">
        <Container variant="wide">
          <h1 className="text-3xl font-bold mb-8">ユーザー管理</h1>
          <Panel variant="elevated" padding="lg">
            {/* コンテンツ */}
          </Panel>
        </Container>
      </Section>
    </div>
  );
}
```

---

### タイプ2: ナビゲーションレイアウト（ヘッダー + サイドバー）

ヘッダーと左側にナビゲーションサイドバーを配置。開閉機能付き。

**適用ページ例**: ダッシュボード、メイン機能ページ、チャットページなど

```tsx
import { Header } from '@/components/layouts/Header';
import { Sidebar } from '@/components/layouts/Sidebar';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <div className="flex">
        <Sidebar />
        <main className="flex-1">
          {children}
        </main>
      </div>
    </div>
  );
}
```

**使用例（ダッシュボードページ）**:

```tsx
import { Header } from '@/components/layouts/Header';
import { Sidebar } from '@/components/layouts/Sidebar';
import { Container } from '@/components/frames/Container';
import { GridFrame } from '@/components/frames/GridFrame';
import { Panel } from '@/components/frames/Panel';

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <div className="flex">
        <Sidebar />
        <main className="flex-1">
          <Section variant="main" padding="lg">
            <Container variant="wide">
              <h1 className="text-3xl font-bold mb-8">ダッシュボード</h1>
              <GridFrame columns={3} gap="md">
                <Panel variant="elevated" padding="md">
                  {/* 統計カード */}
                </Panel>
              </GridFrame>
            </Container>
          </Section>
        </main>
      </div>
    </div>
  );
}
```

---

### タイプ3: 詳細レイアウト（ヘッダー + 左右サイドバー）

ヘッダー、左にナビゲーション、右に詳細情報やフィルターを配置。

**適用ページ例**: 複雑なデータ管理ページ、エディタ、詳細分析画面など

```tsx
import { Header } from '@/components/layouts/Header';
import { SidebarContainer } from '@/components/frames/SidebarContainer';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <div className="flex">
        {/* 左サイドバー */}
        <SidebarContainer
          width="md"
          background="main"
          border="right"
          collapsible={true}
        >
          {/* ナビゲーションコンテンツ */}
        </SidebarContainer>

        {/* メインコンテンツ */}
        <main className="flex-1">
          {children}
        </main>

        {/* 右サイドバー */}
        <SidebarContainer
          width="sm"
          background="base"
          border="left"
          position="right"
        >
          {/* 詳細情報・フィルター */}
        </SidebarContainer>
      </div>
    </div>
  );
}
```

---

## レイアウトタイプ選択ガイド

| ページタイプ | 推奨レイアウト | 理由 |
|-------------|--------------|------|
| ユーザー管理、設定 | タイプ1（シンプル） | サイドバー不要、コンテンツに集中 |
| ダッシュボード、メイン機能 | タイプ2（ナビゲーション） | 主要機能への素早いアクセスが必要 |
| エディタ、詳細分析 | タイプ3（詳細） | 多くの情報と操作パネルが必要 |
| フォーム | タイプ1（シンプル） | 入力に集中させる |
| リスト/グリッド | タイプ1またはタイプ2 | データ量に応じて選択 |

---

## ダッシュボードレイアウト

複数のカードを並べたダッシュボード。

### パターン1: 3カラムグリッド

```tsx
import { Container } from '@/components/frames/Container';
import { Section } from '@/components/frames/Section';
import { GridFrame } from '@/components/frames/GridFrame';
import { Panel } from '@/components/frames/Panel';

export default function DashboardPage() {
  return (
    <Section variant="main" padding="lg">
      <Container variant="wide">
        <h1 className="text-3xl font-bold mb-8">ダッシュボード</h1>

        <GridFrame columns={3} gap="md">
          <Panel variant="elevated" padding="md">
            <h2 className="text-xl font-bold mb-4">統計1</h2>
            <p className="text-2xl">1,234</p>
          </Panel>

          <Panel variant="elevated" padding="md">
            <h2 className="text-xl font-bold mb-4">統計2</h2>
            <p className="text-2xl">5,678</p>
          </Panel>

          <Panel variant="elevated" padding="md">
            <h2 className="text-xl font-bold mb-4">統計3</h2>
            <p className="text-2xl">9,012</p>
          </Panel>
        </GridFrame>
      </Container>
    </Section>
  );
}
```

### パターン2: 2カラム（メイン + サイドバー風）

```tsx
import { Container } from '@/components/frames/Container';
import { GridFrame } from '@/components/frames/GridFrame';
import { Panel } from '@/components/frames/Panel';

export default function DashboardPage() {
  return (
    <Container variant="wide">
      <GridFrame columns={2} gap="lg" className="py-8">
        {/* メインコンテンツ */}
        <div className="space-y-6">
          <Panel variant="elevated" padding="lg">
            <h2 className="text-2xl font-bold mb-4">最近のアクティビティ</h2>
            {/* アクティビティリスト */}
          </Panel>

          <Panel variant="elevated" padding="lg">
            <h2 className="text-2xl font-bold mb-4">統計情報</h2>
            {/* チャートやグラフ */}
          </Panel>
        </div>

        {/* サイドバー風 */}
        <div className="space-y-6">
          <Panel variant="bordered" padding="md">
            <h3 className="text-lg font-bold mb-4">お知らせ</h3>
            {/* お知らせリスト */}
          </Panel>

          <Panel variant="bordered" padding="md">
            <h3 className="text-lg font-bold mb-4">ショートカット</h3>
            {/* ショートカットボタン */}
          </Panel>
        </div>
      </GridFrame>
    </Container>
  );
}
```

---

## フォームページ

入力フォームのレイアウトパターン。

### パターン1: 基本フォーム

```tsx
import { Container } from '@/components/frames/Container';
import { Section } from '@/components/frames/Section';
import { Panel } from '@/components/frames/Panel';
import { Input } from '@/components/atoms/Input';
import { Button } from '@/components/atoms/Button';

export default function FormPage() {
  return (
    <Section variant="main" padding="lg">
      <Container variant="narrow">
        <Panel variant="elevated" padding="lg">
          <h1 className="text-2xl font-bold mb-6">ユーザー登録</h1>

          <form className="space-y-4">
            <div>
              <label className="block text-sm font-bold mb-2">名前</label>
              <Input placeholder="山田太郎" />
            </div>

            <div>
              <label className="block text-sm font-bold mb-2">メールアドレス</label>
              <Input type="email" placeholder="example@hexabase.com" />
            </div>

            <div>
              <label className="block text-sm font-bold mb-2">パスワード</label>
              <Input type="password" placeholder="8文字以上" />
            </div>

            <div className="flex gap-4 pt-4">
              <Button variant="primary" fullWidth>登録</Button>
              <Button variant="secondary" fullWidth>キャンセル</Button>
            </div>
          </form>
        </Panel>
      </Container>
    </Section>
  );
}
```

### パターン2: セクション分割フォーム

```tsx
import { Container } from '@/components/frames/Container';
import { Panel } from '@/components/frames/Panel';
import { Input } from '@/components/atoms/Input';
import { Button } from '@/components/atoms/Button';

export default function SettingsFormPage() {
  return (
    <Container variant="main" className="py-8">
      <h1 className="text-3xl font-bold mb-8">設定</h1>

      <div className="space-y-6">
        {/* 基本情報セクション */}
        <Panel variant="bordered" padding="lg">
          <h2 className="text-xl font-bold mb-4">基本情報</h2>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-bold mb-2">表示名</label>
              <Input placeholder="表示名" />
            </div>
            <div>
              <label className="block text-sm font-bold mb-2">メール</label>
              <Input type="email" placeholder="email@example.com" />
            </div>
          </div>
        </Panel>

        {/* セキュリティセクション */}
        <Panel variant="bordered" padding="lg">
          <h2 className="text-xl font-bold mb-4">セキュリティ</h2>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-bold mb-2">現在のパスワード</label>
              <Input type="password" />
            </div>
            <div>
              <label className="block text-sm font-bold mb-2">新しいパスワード</label>
              <Input type="password" />
            </div>
          </div>
        </Panel>

        {/* 保存ボタン */}
        <div className="flex justify-end gap-4">
          <Button variant="secondary">キャンセル</Button>
          <Button variant="primary">変更を保存</Button>
        </div>
      </div>
    </Container>
  );
}
```

---

## リスト/グリッドページ

アイテムのリストやグリッド表示。

### パターン1: グリッドビュー

```tsx
import { Container } from '@/components/frames/Container';
import { GridFrame } from '@/components/frames/GridFrame';
import { Panel } from '@/components/frames/Panel';
import { Button } from '@/components/atoms/Button';

export default function GridViewPage() {
  return (
    <Container variant="wide" className="py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">エージェント一覧</h1>
        <Button variant="primary">+ 新規作成</Button>
      </div>

      <GridFrame columns={3} gap="md">
        {agents.map((agent) => (
          <Panel key={agent.id} variant="elevated" padding="md">
            <h3 className="text-lg font-bold mb-2">{agent.name}</h3>
            <p className="text-sm text-text-sub mb-4">{agent.description}</p>
            <div className="flex gap-2">
              <Button variant="secondary" size="sm">編集</Button>
              <Button variant="danger" size="sm">削除</Button>
            </div>
          </Panel>
        ))}
      </GridFrame>
    </Container>
  );
}
```

### パターン2: リストビュー

```tsx
import { Container } from '@/components/frames/Container';
import { Panel } from '@/components/frames/Panel';
import { Button } from '@/components/atoms/Button';

export default function ListViewPage() {
  return (
    <Container variant="main" className="py-8">
      <h1 className="text-3xl font-bold mb-8">タスク一覧</h1>

      <div className="space-y-4">
        {tasks.map((task) => (
          <Panel key={task.id} variant="bordered" padding="md">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="text-lg font-bold mb-1">{task.title}</h3>
                <p className="text-sm text-text-sub">{task.description}</p>
              </div>
              <div className="flex gap-2">
                <Button variant="ghost" size="sm">詳細</Button>
                <Button variant="secondary" size="sm">編集</Button>
              </div>
            </div>
          </Panel>
        ))}
      </div>
    </Container>
  );
}
```

---

## 詳細画面

単一アイテムの詳細表示。

### パターン1: ヘッダー + 詳細情報

```tsx
import { Container } from '@/components/frames/Container';
import { Section } from '@/components/frames/Section';
import { Panel } from '@/components/frames/Panel';
import { Button } from '@/components/atoms/Button';

export default function DetailPage() {
  return (
    <>
      {/* ヘッダーセクション */}
      <Section variant="base" padding="lg">
        <Container variant="main">
          <div className="flex justify-between items-start">
            <div>
              <h1 className="text-3xl font-bold mb-2">プロジェクト名</h1>
              <p className="text-text-sub">作成日: 2025-01-01</p>
            </div>
            <div className="flex gap-2">
              <Button variant="secondary">編集</Button>
              <Button variant="danger">削除</Button>
            </div>
          </div>
        </Container>
      </Section>

      {/* 詳細情報セクション */}
      <Section variant="main" padding="lg">
        <Container variant="main">
          <Panel variant="elevated" padding="lg">
            <h2 className="text-xl font-bold mb-4">詳細情報</h2>
            <dl className="space-y-4">
              <div>
                <dt className="text-sm font-bold text-text-sub">説明</dt>
                <dd className="mt-1">プロジェクトの説明文...</dd>
              </div>
              <div>
                <dt className="text-sm font-bold text-text-sub">ステータス</dt>
                <dd className="mt-1">進行中</dd>
              </div>
              <div>
                <dt className="text-sm font-bold text-text-sub">担当者</dt>
                <dd className="mt-1">山田太郎</dd>
              </div>
            </dl>
          </Panel>
        </Container>
      </Section>
    </>
  );
}
```

---

## 設定画面

アプリケーション設定のレイアウト。

### パターン1: タブ風セクション

```tsx
import { Container } from '@/components/frames/Container';
import { Panel } from '@/components/frames/Panel';
import { Input } from '@/components/atoms/Input';
import { Button } from '@/components/atoms/Button';

export default function SettingsPage() {
  return (
    <Container variant="main" className="py-8">
      <h1 className="text-3xl font-bold mb-8">設定</h1>

      {/* ナビゲーション */}
      <div className="flex gap-4 mb-6 border-b border-border">
        <button className="px-4 py-2 font-bold border-b-2 border-accent">
          プロフィール
        </button>
        <button className="px-4 py-2 text-text-sub hover:text-text-base">
          セキュリティ
        </button>
        <button className="px-4 py-2 text-text-sub hover:text-text-base">
          外観
        </button>
      </div>

      {/* 設定コンテンツ */}
      <Panel variant="bordered" padding="lg">
        <h2 className="text-xl font-bold mb-6">プロフィール設定</h2>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-bold mb-2">ユーザー名</label>
            <Input placeholder="ユーザー名" />
          </div>
          <div>
            <label className="block text-sm font-bold mb-2">メールアドレス</label>
            <Input type="email" placeholder="email@example.com" />
          </div>
          <div className="pt-4">
            <Button variant="primary">保存</Button>
          </div>
        </div>
      </Panel>
    </Container>
  );
}
```

---

## モーダルダイアログ

モーダルのレイアウトパターン。

### パターン1: 確認ダイアログ

```tsx
import { Modal } from '@/components/frames/Modal';
import { Button } from '@/components/atoms/Button';

function DeleteConfirmModal({ isOpen, onClose, onConfirm }) {
  return (
    <Modal isOpen={isOpen} onClose={onClose} size="sm">
      <div className="p-6">
        <h2 className="text-xl font-bold mb-4">削除の確認</h2>
        <p className="text-text-sub mb-6">
          本当にこの項目を削除しますか？この操作は取り消せません。
        </p>
        <div className="flex gap-4 justify-end">
          <Button variant="secondary" onClick={onClose}>
            キャンセル
          </Button>
          <Button variant="danger" onClick={onConfirm}>
            削除
          </Button>
        </div>
      </div>
    </Modal>
  );
}
```

### パターン2: フォームモーダル

```tsx
import { Modal } from '@/components/frames/Modal';
import { Input } from '@/components/atoms/Input';
import { Button } from '@/components/atoms/Button';

function CreateItemModal({ isOpen, onClose }) {
  return (
    <Modal isOpen={isOpen} onClose={onClose} size="md">
      <div className="p-6">
        <h2 className="text-2xl font-bold mb-6">新規作成</h2>
        <form className="space-y-4">
          <div>
            <label className="block text-sm font-bold mb-2">名前</label>
            <Input placeholder="アイテム名" />
          </div>
          <div>
            <label className="block text-sm font-bold mb-2">説明</label>
            <Input placeholder="説明文" />
          </div>
          <div className="flex gap-4 justify-end pt-4">
            <Button variant="secondary" onClick={onClose}>
              キャンセル
            </Button>
            <Button variant="primary" type="submit">
              作成
            </Button>
          </div>
        </form>
      </div>
    </Modal>
  );
}
```

---

## レイアウトパターン選択ガイド

| ページタイプ | 推奨パターン | 使用コンポーネント |
|-------------|------------|------------------|
| ダッシュボード | 3カラムグリッド | Container(wide) + GridFrame + Panel(elevated) |
| フォーム | 基本フォーム | Container(narrow) + Panel(elevated) + Input + Button |
| リスト | グリッドビュー/リストビュー | Container(main/wide) + GridFrame/space-y + Panel |
| 詳細画面 | ヘッダー + 詳細情報 | Section + Container + Panel |
| 設定画面 | セクション分割 | Container(main) + Panel(bordered) |
| モーダル | 確認/フォーム | Modal + Button |

**原則**:
1. まず適切なContainerでmax-widthを決める
2. 必要に応じてSectionで背景を設定
3. GridFrameまたはspace-yでレイアウトを構築
4. Panelでカード型UIを実現
5. Input、Buttonで入力UIを構築
