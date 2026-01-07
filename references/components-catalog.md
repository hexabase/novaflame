# Component Catalog

Novaflameで利用可能な既存コンポーネントの完全なカタログです。

**重要**:
- ✅ これらの既存コンポーネントを組み合わせてページを構築します
- ❌ 新しいコンポーネントを作成しません（src/components/配下に新規ファイルを作らない）
- ❌ このカタログ内のコンポーネントファイルを編集・変更しません

## Table of Contents

- [Atoms（基本要素）](#atoms基本要素)
- [Molecules（複合要素）](#molecules複合要素)
- [Frames（レイアウトフレーム）](#framesレイアウトフレーム)
- [Layouts（レイアウトコンポーネント）](#layoutsレイアウトコンポーネント)
- [Features（機能別コンポーネント）](#features機能別コンポーネント)

---

## Atoms（基本要素）

基本的なUI要素。最小単位のコンポーネント。

### Button

**場所**: `src/components/atoms/Button.tsx`

ボタンコンポーネント。4つのバリアント、3つのサイズ、ローディング状態をサポート。

**Props:**

```typescript
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  fullWidth?: boolean;
  className?: string;
  children: React.ReactNode;
  // + HTMLButtonElement の全属性
}
```

**使用例:**

```tsx
import { Button } from '@/components/atoms/Button';

<Button variant="primary" size="md">保存</Button>
<Button variant="secondary" size="sm">キャンセル</Button>
<Button variant="danger" size="md">削除</Button>
<Button variant="ghost" size="sm">詳細</Button>
<Button loading variant="primary">処理中...</Button>
<Button fullWidth variant="primary">全幅ボタン</Button>
```

**バリアント詳細:**
- `primary`: アクセントカラー背景、白テキスト（主要アクション用）
- `secondary`: ボーダーあり、透明背景（副次的アクション用）
- `ghost`: ボーダーなし、透明背景（軽微なアクション用）
- `danger`: エラーカラー背景、白テキスト（削除などの危険なアクション用）

---

### Input

**場所**: `src/components/atoms/Input.tsx`

入力フィールドコンポーネント。エラー表示、左右アイコンをサポート。

**Props:**

```typescript
interface InputProps {
  error?: string;
  leftIcon?: ReactNode;
  rightIcon?: ReactNode;
  className?: string;
  // + HTMLInputElement の全属性
}
```

**使用例:**

```tsx
import { Input } from '@/components/atoms/Input';
import { Search, Eye } from 'lucide-react';

<Input placeholder="メールアドレス" type="email" />
<Input placeholder="検索..." leftIcon={<Search size={16} />} />
<Input
  placeholder="パスワード"
  type="password"
  rightIcon={<Eye size={16} />}
/>
<Input
  placeholder="ユーザー名"
  error="このフィールドは必須です"
/>
```

---

### Logo

**場所**: `src/components/atoms/Logo.tsx`

Hexabaseロゴコンポーネント。

**使用例:**

```tsx
import { Logo } from '@/components/atoms/Logo';

<Logo />
```

---

### NavItem

**場所**: `src/components/atoms/NavItem.tsx`

ナビゲーションアイテム。サイドバーやメニューで使用するリンク/ボタン。hrefがある場合はLink、ない場合はbuttonとして動作。アイコン表示はオプション。

**Props:**

```typescript
interface NavItemProps {
  href?: string;              // リンク先（省略時はbuttonとして動作）
  icon?: LucideIcon;          // アイコン（オプション）
  isActive?: boolean;         // アクティブ状態
  onClick?: () => void;       // クリックハンドラ
  className?: string;         // 追加スタイル
  children: React.ReactNode;  // 表示テキスト
}
```

**使用例:**

```tsx
import { NavItem } from '@/components/atoms/NavItem';
import { MessageSquare, Settings, CheckCircle } from 'lucide-react';

// リンクモード（hrefあり）- アイコン付き
<NavItem href="/chat/123" icon={MessageSquare} isActive={true}>
  チャットタイトル
</NavItem>

// リンクモード - アイコンなし
<NavItem href="/settings" isActive={false}>
  設定
</NavItem>

// ボタンモード（hrefなし）- フィルターなどに使用
<NavItem
  icon={CheckCircle}
  isActive={selectedStatus === 'Running'}
  onClick={() => setSelectedStatus('Running')}
>
  Running (10)
</NavItem>

// ボタンモード - アイコンなし
<NavItem
  isActive={selectedNamespace === 'default'}
  onClick={() => setSelectedNamespace('default')}
>
  default (5)
</NavItem>
```

**スタイル:**
- アクティブ状態: `bg-accent/20 text-accent font-medium`
- 非アクティブ状態: `text-text-base hover:bg-base`
- アイコンサイズ: 16px（固定）
- テキストは自動的にtruncate（省略記号）

**動作:**
- `href`が指定されている場合: Next.jsの`<Link>`として動作
- `href`が省略されている場合: `<button>`として動作

---

### PageTitle

**場所**: `src/components/atoms/PageTitle.tsx`

ページタイトルコンポーネント。ページの主見出しとして使用。

**Props:**

```typescript
interface PageTitleProps {
  level?: 1 | 2 | 3 | 4 | 5 | 6;  // 見出しレベル (default: 1)
  className?: string;              // 追加スタイル
  children: React.ReactNode;       // タイトルテキスト
}
```

**使用例:**

```tsx
import { PageTitle } from '@/components/atoms/PageTitle';

// ✅ 推奨：ページメインタイトルは level={4} を使用
<PageTitle level={4}>Pod管理</PageTitle>

// セクションタイトル
<PageTitle level={2}>統計情報</PageTitle>

// カスタムスタイル
<PageTitle level={4} className="text-accent">ダッシュボード</PageTitle>
```

**スタイル:**
- レベル1（h1）: `text-3xl font-bold mb-8` - 30px
- レベル2（h2）: `text-2xl font-bold mb-8` - 24px
- レベル3（h3）: `text-xl font-bold mb-8` - 20px
- レベル4（h4）: `text-lg font-bold mb-8` - 18px ⭐ **推奨**
- レベル5（h5）: `text-base font-bold mb-8` - 16px
- レベル6（h6）: `text-sm font-bold mb-8` - 14px

**ベストプラクティス:**
- ⭐ **ページのメインタイトルには `level={4}` を使用**してください
- `level={4}`（18px）は統計カードやコンテンツとのバランスが最適
- `level={1}`（デフォルト、32px）は大きすぎるため避けてください

---

## Molecules（複合要素）

複数のAtomsを組み合わせた要素。

### ConfirmModal

**場所**: `src/components/molecules/ConfirmModal.tsx`

確認ダイアログ。削除確認などに使用。

**Props:**

```typescript
interface ConfirmModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
}
```

**使用例:**

```tsx
import { ConfirmModal } from '@/components/molecules/ConfirmModal';

<ConfirmModal
  isOpen={isDeleteModalOpen}
  onClose={() => setIsDeleteModalOpen(false)}
  onConfirm={handleDelete}
  title="削除の確認"
  message="本当にこの項目を削除しますか？"
  confirmText="削除"
  cancelText="キャンセル"
/>
```

---

### FileIcon

**場所**: `src/components/molecules/FileIcon.tsx`

ファイルタイプに応じたアイコン表示。

**使用例:**

```tsx
import { FileIcon } from '@/components/molecules/FileIcon';

<FileIcon filename="document.pdf" />
<FileIcon filename="script.js" />
```

---

## Frames（レイアウトフレーム）

ページレイアウトの基礎となるフレーム。

**重要な原則**:
1. **新しいページを構築する際は、まずFramesを選択してから他のコンポーネントを配置します**
2. **Framesを決めてから中にコンポーネントを入れていく**ことで、一貫性のあるレイアウトを実現
3. **推奨バリアントを優先的に使用**することで、デザインの統一性を保つ

### Frames構築フロー

```
1. Container でmax-widthを決める (推奨: variant="main")
   ↓
2. Section で背景とpaddingを設定 (推奨: variant="main")
   ↓
3. GridFrame または SidebarContainer でレイアウト構造を決める
   ↓
4. Panel でカード型UIを作る (推奨: variant="elevated" + padding="md")
   ↓
5. Atoms / Molecules を配置
```

詳細な推奨バリアントのガイドラインは [usage-guidelines.md](../usage-guidelines.md#frames使用ルール推奨バリアント) を参照してください。

---

### Container

**推奨バリアント**: ⭐ `variant="main"` (デフォルト)

**場所**: `src/components/frames/Container.tsx`

メインエリア用コンテナ。max-widthを制御し、コンテンツを中央に配置。

**Props:**

```typescript
interface ContainerProps {
  variant?: 'narrow' | 'main' | 'wide' | 'full';
  className?: string;
  children: React.ReactNode;
}
```

**使用例:**

```tsx
import { Container } from '@/components/frames/Container';

<Container variant="main">
  {/* メインコンテンツ */}
</Container>

<Container variant="narrow">
  {/* 狭い幅のコンテンツ（フォームなど） */}
</Container>

<Container variant="wide">
  {/* 広い幅のコンテンツ（ダッシュボードなど） */}
</Container>
```

**バリアント:**
- `narrow`: max-w-3xl（フォーム、記事など）
- `main`: max-w-5xl（標準的なページ）
- `wide`: max-w-7xl（ダッシュボード、テーブルなど）
- `full`: max-w-none（全幅）

---

### Section

**場所**: `src/components/frames/Section.tsx`

背景色・余白付きセクション。ページの区切りや背景色の変更に使用。

**Props:**

```typescript
interface SectionProps {
  variant?: 'default' | 'main' | 'base' | 'accent';
  className?: string;
  children: React.ReactNode;
}
```

**使用例:**

```tsx
import { Section } from '@/components/frames/Section';

<Section variant="main">
  {/* メイン背景のセクション */}
</Section>

<Section variant="accent">
  {/* アクセントカラー背景のセクション */}
</Section>

<Section variant="base" className="h-full">
  {/* 高さ100%のベース背景セクション */}
</Section>
```

**バリアント:**
- `default`: 透明背景
- `main`: bg-main
- `base`: bg-base
- `accent`: bg-accent/10

**Padding:**
- 固定値: `p-8` (32px) - すべての方向に32pxのpadding

---

### GridFrame

**場所**: `src/components/frames/GridFrame.tsx`

グリッドレイアウトフレーム。1〜4カラムのグリッド表示。

**Props:**

```typescript
interface GridFrameProps {
  columns: 1 | 2 | 3 | 4;
  gap?: 'sm' | 'md' | 'lg';
  className?: string;
  children: React.ReactNode;
}
```

**使用例:**

```tsx
import { GridFrame } from '@/components/frames/GridFrame';

<GridFrame columns={3} gap="md">
  <Card />
  <Card />
  <Card />
</GridFrame>

<GridFrame columns={2} gap="lg">
  <Panel>左</Panel>
  <Panel>右</Panel>
</GridFrame>
```

**Gap:**
- `sm`: gap-2 (8px)
- `md`: gap-4 (16px)
- `lg`: gap-6 (24px)

---

### Panel

**場所**: `src/components/frames/Panel.tsx`

カード型フレーム。背景、影、パディングを制御。

**Props:**

```typescript
interface PanelProps {
  variant?: 'default' | 'elevated' | 'bordered';
  padding?: 'none' | 'sm' | 'md' | 'lg';
  className?: string;
  children: React.ReactNode;
}
```

**使用例:**

```tsx
import { Panel } from '@/components/frames/Panel';

<Panel variant="elevated" padding="md">
  {/* 影付きカード */}
</Panel>

<Panel variant="bordered" padding="lg">
  {/* ボーダー付きカード */}
</Panel>
```

**バリアント:**
- `default`: bg-base（影なし、ボーダーなし）
- `elevated`: bg-base + shadow-lg
- `bordered`: bg-base + border

**Padding:**
- `none`: p-0
- `sm`: p-2
- `md`: p-4
- `lg`: p-6

---

### Modal

**場所**: `src/components/frames/Modal.tsx`

モーダルフレーム。オーバーレイとコンテンツ領域を提供。Escキーで閉じる機能付き。

**Props:**

```typescript
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  size?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  closeOnOverlayClick?: boolean;
  className?: string;
  children: React.ReactNode;
}
```

**使用例:**

```tsx
import { Modal } from '@/components/frames/Modal';

<Modal isOpen={isOpen} onClose={() => setIsOpen(false)} size="md">
  <div className="p-6">
    <h2 className="text-xl font-bold mb-4">モーダルタイトル</h2>
    <p>モーダルコンテンツ</p>
  </div>
</Modal>
```

**Size:**
- `sm`: max-w-md
- `md`: max-w-2xl
- `lg`: max-w-4xl
- `xl`: max-w-6xl
- `full`: max-w-none + h-full

---

### ScrollArea

**場所**: `src/components/frames/ScrollArea.tsx`

スクロール可能なエリア。

**使用例:**

```tsx
import { ScrollArea } from '@/components/frames/ScrollArea';

<ScrollArea className="h-96">
  {/* 長いコンテンツ */}
</ScrollArea>
```

---

### SidebarContainer

**場所**: `src/components/frames/SidebarContainer.tsx`

サイドバー用コンテナ。開閉機能をサポート。

**Props:**

```tsx
interface SidebarContainerProps {
  width?: 'sm' | 'md' | 'lg';          // 幅サイズ (sm=192px, md=256px, lg=320px)
  position?: 'left' | 'right';         // 配置位置
  background?: 'none' | 'main' | 'base'; // 背景色
  border?: 'none' | 'left' | 'right';  // ボーダー
  overflow?: 'visible' | 'hidden' | 'auto'; // オーバーフロー制御
  fullHeight?: boolean;                // 高さを100%にする
  collapsible?: boolean;               // 開閉機能を有効化
  defaultOpen?: boolean;               // 初期開閉状態 (default: true)
  className?: string;
  children: React.ReactNode;
}
```

**使用例:**

```tsx
import { SidebarContainer } from '@/components/frames/SidebarContainer';

// 通常のサイドバー
<SidebarContainer width="md" background="main" border="right">
  {/* サイドバーコンテンツ */}
</SidebarContainer>

// 開閉機能付きサイドバー
<SidebarContainer
  width="md"
  background="main"
  border="right"
  collapsible={true}
  defaultOpen={true}
>
  {/* サイドバーコンテンツ */}
</SidebarContainer>
```

**備考:**
- `collapsible={true}` で開閉ボタンが自動的に追加される
- 開閉ボタンは左上 (left-4 top-[76px]) に配置される
- アニメーションは300msで滑らかに動作する

---

## Layouts（レイアウトコンポーネント）

アプリケーション全体のレイアウト構造。**すべてのページで共通のHeaderコンポーネントを使用することを推奨します。**

### Header

**場所**: `src/components/layouts/Header.tsx`

グローバルヘッダーコンポーネント。ロゴ、ナビゲーションリンク、ユーザーメニューを含みます。

**機能:**
- ロゴ表示（左上）
- ナビゲーションリンク（デスクトップ）
  - チャット (`/chat`)
  - エージェント (`/agents`)
- ユーザーメニュー（右上）
  - ユーザー設定 (`/settings`)
  - ログアウト
- モバイル対応
  - ハンバーガーメニュー
  - オーバーレイメニュー

**Props:**

```typescript
// Propsなし - 内部でuseAuthStoreから状態を取得
```

**基本使用例:**

```tsx
import { Header } from '@/components/layouts/Header';

export default function MyPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <main>
        {/* ページコンテンツ */}
      </main>
    </div>
  );
}
```

**レイアウトパターン別使用例:**

```tsx
// タイプ1: シンプルレイアウト（ヘッダーのみ）
import { Header } from '@/components/layouts/Header';
import { Section } from '@/components/frames/Section';
import { Container } from '@/components/frames/Container';

export default function UsersPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <Section variant="main" padding="lg">
        <Container variant="wide">
          {/* コンテンツ */}
        </Container>
      </Section>
    </div>
  );
}

// タイプ2: ナビゲーションレイアウト（ヘッダー + サイドバー）
import { Header } from '@/components/layouts/Header';
import { Sidebar } from '@/components/layouts/Sidebar';

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <div className="flex">
        <Sidebar />
        <main className="flex-1">
          {/* コンテンツ */}
        </main>
      </div>
    </div>
  );
}
```

**スタイル:**
- 高さ: `h-16` (64px)
- 背景: `bg-main`
- ボーダー: `border-b border-border`
- パディング: `px-3 sm:px-6`

**依存関係:**
- `useAuthStore`: ユーザー情報、ログアウト機能
- `usePathname`: アクティブリンクの判定
- `Logo`: ロゴコンポーネント
- `Panel`: ドロップダウンメニュー

**重要:**
- すべてのページで使用することを推奨
- モバイルとデスクトップ両対応
- ナビゲーションリンクは既存の機能（チャット、エージェント）に対応
- カスタマイズが必要な場合は、`Header.tsx`を直接編集

---

### Sidebar

**場所**: `src/components/layouts/Sidebar.tsx`

グローバルサイドバーコンポーネント。チャット履歴とファイルブラウザを含みます。

**機能:**
- チャット履歴表示
- ファイルツリー表示
- タブ切り替え（チャット/ファイル）
- 開閉ボタン
- モバイル対応（オーバーレイ表示）
- `/chat`配下で自動表示

**Props:**

```typescript
// Propsなし - 内部で状態を管理
```

**基本使用例:**

```tsx
import { Header } from '@/components/layouts/Header';
import { Sidebar } from '@/components/layouts/Sidebar';

export default function ChatPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />
      <div className="flex">
        <Sidebar />
        <main className="flex-1">
          {/* チャットコンテンツ */}
        </main>
      </div>
    </div>
  );
}
```

**動作:**
- `/chat`配下のページでのみ使用
- デスクトップ: 左側に固定、開閉可能
- モバイル: オーバーレイ表示
- チャット詳細ページ: チャット/ファイルタブを表示

**スタイル:**
- 幅: `w-64` (256px)
- 背景: `bg-main`
- ボーダー: `border-r border-border`

**依存関係:**
- `useEditorStore`: ファイル操作
- `usePathname`: ページ判定
- `SidebarContainer`: サイドバーフレーム
- `NavItem`: ナビゲーションアイテム
- `ScrollArea`: スクロール可能エリア

**重要:**
- チャット機能専用のコンポーネント
- 汎用的なサイドバーが必要な場合は`SidebarContainer`を使用
- カスタムナビゲーションが必要な場合は、`SidebarContainer`と`NavItem`を組み合わせて構築

---

### ResizablePanelLayout

**場所**: `src/components/layouts/ResizablePanelLayout.tsx`

リサイズ可能なパネルレイアウト（react-resizable-panels使用）。

**使用例:**

```tsx
import { ResizablePanelLayout } from '@/components/layouts/ResizablePanelLayout';

<ResizablePanelLayout
  leftPanel={<div>左パネル</div>}
  rightPanel={<div>右パネル</div>}
/>
```

---

## Features（機能別コンポーネント）

特定の機能に特化したコンポーネント。

### Agents

- **AgentCard** (`src/components/features/agents/AgentCard.tsx`): エージェント情報カード
- **AgentModal** (`src/components/features/agents/AgentModal.tsx`): エージェント作成/編集モーダル
- **DeleteAgentModal** (`src/components/features/agents/DeleteAgentModal.tsx`): エージェント削除確認モーダル

### Auth

- **AuthGuard** (`src/components/features/auth/AuthGuard.tsx`): 認証が必要なページのガード
- **GuestGuard** (`src/components/features/auth/GuestGuard.tsx`): 未認証ユーザー専用ページのガード
- **LoginForm** (`src/components/features/auth/LoginForm.tsx`): ログインフォーム
- **SSOButtons** (`src/components/features/auth/SSOButtons.tsx`): SSO認証ボタン

### Chat

- **AgentSelector** (`src/components/features/chat/AgentSelector.tsx`): エージェント選択UI
- **ChatInput** (`src/components/features/chat/ChatInput.tsx`): チャット入力欄
- **ChatTextarea** (`src/components/features/chat/ChatTextarea.tsx`): チャットテキストエリア

### Editor

- **FileEditor** (`src/components/features/editor/FileEditor.tsx`): ファイルエディタ（CodeMirror）
- **FileEditorContent** (`src/components/features/editor/FileEditorContent.tsx`): エディタコンテンツ
- **FileEditorStatusBar** (`src/components/features/editor/FileEditorStatusBar.tsx`): ステータスバー
- **FileEditorTabs** (`src/components/features/editor/FileEditorTabs.tsx`): ファイルタブ
- **ViewModeToggle** (`src/components/features/editor/ViewModeToggle.tsx`): 表示モード切り替え

### Settings

- **ApiSection** (`src/components/features/settings/ApiSection.tsx`): API設定セクション
- **AppearanceSection** (`src/components/features/settings/AppearanceSection.tsx`): 外観設定セクション
- **ProfileSection** (`src/components/features/settings/ProfileSection.tsx`): プロフィール設定セクション

---

## コンポーネント選択ガイドライン

### 新しいページを作る際の基本パターン

1. **Containerでmax-widthを決める**
   ```tsx
   <Container variant="main">
     {/* コンテンツ */}
   </Container>
   ```

2. **必要に応じてSectionで背景とpaddingを設定**
   ```tsx
   <Section variant="base" padding="lg">
     <Container variant="main">
       {/* コンテンツ */}
     </Container>
   </Section>
   ```

3. **レイアウトが必要ならGridFrameを使う**
   ```tsx
   <Container variant="wide">
     <GridFrame columns={3} gap="md">
       <Panel>カード1</Panel>
       <Panel>カード2</Panel>
       <Panel>カード3</Panel>
     </GridFrame>
   </Container>
   ```

4. **カード型のUIならPanelを使う**
   ```tsx
   <Panel variant="elevated" padding="md">
     <h2 className="text-xl font-bold mb-4">タイトル</h2>
     <p>コンテンツ</p>
   </Panel>
   ```

5. **ボタンとInputで入力UIを構築**
   ```tsx
   <div className="space-y-4">
     <Input placeholder="名前" />
     <Input placeholder="メール" type="email" />
     <Button variant="primary" fullWidth>送信</Button>
   </div>
   ```

**原則**: 常に既存コンポーネントの組み合わせで構築し、新しいコンポーネントは作らない。
