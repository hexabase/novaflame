---
name: novaflame
description: HexabaseのデザインシステムとCaptain UIのコンポーネントを活用し、Adobe Spectrumの設計思想に基づいた一貫性のある美しいUIページをデザインします。Next.js 15 + Tailwind CSS 4を使用し、既存コンポーネント（Atoms, Molecules, Frames, Layouts）を組み合わせてページを構築します。【重要】ページ作成前に必ずレイアウトタイプ（シンプル/ナビゲーション/詳細）をユーザーに確認し、全ページに必ずHeaderコンポーネントを設置してください。novaflameスキルを使用する際は、必ず既存コンポーネントのカタログを参照してください。
---

# Novaflame

NovaflameはCaptain UIをベースとしたHexabaseプロダクト全体のデザイン標準です。Adobe Spectrumの設計思想を参考に、一貫性のある美しいUIを提供します。

## スキルの目的

**既存コンポーネントを組み合わせてNovaflameデザインガイドラインに則ったページを構築することが目的です。**

**重要な制約事項**:
- ✅ **既存コンポーネントを組み合わせて使用する**
- ❌ **新しいコンポーネントを作成しない**（src/components/配下に新規ファイルを作らない）
- ❌ **既存コンポーネントを編集・変更しない**（既存ファイルを変更しない）

このスキルは、既存のコンポーネントカタログから適切なコンポーネントを選択し、組み合わせることに専念します。

## ページ作成の必須ルール

**🚨 重要: このnovaflameスキルを使用してページを作成する際は、以下のルールを必ず守ってください。**

### ルール1: 必ず共通ヘッダを設置する（強制）

**すべてのページには必ず`Header`コンポーネントを設置してください。** これはHexabaseプロダクト全体の一貫性を保つための絶対的なルールです。

```tsx
import { Header } from '@/components/layouts/Header';

export default function YourPage() {
  return (
    <div className="min-h-screen bg-main">
      <Header />  {/* 必須！ */}
      {/* ページコンテンツ */}
    </div>
  );
}
```

❌ **禁止**: Headerなしでページを作成すること

### ルール2: ページ作成前にレイアウトタイプを確認する（必須）

ページを作成する前に、必ずユーザーに以下の3つのレイアウトタイプから選択してもらってください：

**レイアウトタイプの選択肢:**

1. **タイプ1: シンプルレイアウト（ヘッダーのみ）**
   - ヘッダーのみを表示し、サイドバーなしのシンプルな構成
   - 適用ページ例: ユーザー管理、設定ページ、フォーム、詳細画面など
   ```tsx
   <div className="min-h-screen bg-main">
     <Header />
     <main className="flex-1">
       {children}
     </main>
   </div>
   ```

2. **タイプ2: ナビゲーションレイアウト（ヘッダー + サイドバー）**
   - ヘッダーと左側にナビゲーションサイドバーを配置。開閉機能付き
   - 適用ページ例: ダッシュボード、メイン機能ページ、チャットページなど
   ```tsx
   <div className="min-h-screen bg-main">
     <Header />
     <div className="flex">
       <Sidebar />
       <main className="flex-1">
         {children}
       </main>
     </div>
   </div>
   ```

3. **タイプ3: 詳細レイアウト（ヘッダー + 左右サイドバー）**
   - ヘッダー、左サイドバー、右サイドバーの3ペイン構成
   - 適用ページ例: チャット詳細、エージェント詳細、ドキュメントビューアなど
   ```tsx
   <div className="min-h-screen bg-main">
     <Header />
     <div className="flex">
       <Sidebar />
       <main className="flex-1">
         {children}
       </main>
       <SidebarContainer position="right">
         {/* 右サイドバーコンテンツ */}
       </SidebarContainer>
     </div>
   </div>
   ```

**実装フロー:**
1. ユーザーに「どのレイアウトタイプを使用しますか？」と質問する
2. ユーザーが選択したレイアウトタイプに基づいてページを構築する
3. 必ずHeaderコンポーネントを含める

詳細は [layout-patterns.md](references/layout-patterns.md#アプリケーション全体のレイアウトタイプ) を参照してください。

### ルール3: dangerバリアント（赤色）は使用禁止（必須）

**🚨 このプロジェクトでは、すべてのボタンで`danger`バリアント（赤色）の使用を禁止します。**

- ❌ **禁止**: `<Button variant="danger">削除</Button>`
- ✅ **推奨**: `<Button variant="secondary">削除</Button>`

**理由**:
- 削除などの破壊的な操作には`secondary`バリアントを使用する
- すべてのボタンは`primary`, `secondary`, `ghost`のいずれかを使用する
- 赤色は視覚的に強すぎるため、このプロジェクトのデザイン方針として使用しない

詳細は [usage-guidelines.md](references/usage-guidelines.md#buttonのvariant選択) を参照してください。

---

## 主要なリファレンス

このスキルはnovaflameスキルを使用する際に、以下の4つの主要リファレンスを活用します:

1. **コンポーネントカタログ**: 利用可能なすべてのコンポーネント一覧
2. **レイアウトパターン集**: [layout-patterns.md](references/layout-patterns.md)によく使うパターン集
3. **デザインシステム仕様**: [components-catalog.md](references/components-catalog.md)に詳細なコンポーネント仕様
4. **カラーとタイポグラフィ**: [design-system.md](references/design-system.md)の基本スタイル定義
5. **使用ガイドライン**: [usage-guidelines.md](references/usage-guidelines.md)で適切な使い方
6. **アクセシビリティ基準**: [accessibility.md](references/accessibility.md)の基本ルール
7. **実例**: 既存コンポーネントを組み合わせた実装例

## リファレンスファイルの詳細

### [design-system.md](references/design-system.md)
NovaflameのカラーシステムやBrand Neutral（グレースケール）、Brand Primary（ティール）、タイポグラフィルール、スペーシングルールを定義。

**活用する場面**: カラートークンの確認、テキストサイズの決定時

### [components-catalog.md](references/components-catalog.md)
既存コンポーネントの完全なカタログ。Atoms、Molecules、Frames、Layouts、Featuresごとに分類されたpropsと使用例。

**活用する場面**: どのコンポーネントが利用可能か確認、正しいpropsやimportパスの確認時

### [layout-patterns.md](references/layout-patterns.md)
よく使用される実用的なレイアウトパターンの実装例。ダッシュボード、フォーム、リスト/グリッド、詳細画面、設定画面、モーダルダイアログなどのパターン。

**活用する場面**: 新しいページのレイアウトを設計する時、どう組み合わせるべきか迷った時

### [accessibility.md](references/accessibility.md)
アクセシビリティのベストプラクティス。キーボードナビゲーション、フォーカス管理、カラーコントラスト、ARIA属性の使い方を定義。

**活用する場面**: フォームやモーダルを実装する時、アクセシビリティ基準を満たす必要がある時

### [usage-guidelines.md](references/usage-guidelines.md)
いつ何を使うべきかの判断基準。Button variantの選択ルール、Panel variantのユースケース、invariantな規則やvariantによる違いを明確化。

**活用する場面**: invariantな実装をする時、variantの選び方で迷った時

## 使い方の例

### 0. Framesを決めてから中にコンポーネントを入れる（重要）

**最も重要な原則**: novaflameでページを構築する際は、まず**Framesを決めてから**中にコンポーネントを入れていきます。

```tsx
// ✅ 推奨: Framesを先に決める
<Container variant="main">
  <Section variant="main">
    <GridFrame columns={3} gap="md">
      <Panel variant="elevated" padding="md">
        <PageTitle>タイトル</PageTitle>
        <Button variant="primary">ボタン</Button>
      </Panel>
    </GridFrame>
  </Section>
</Container>
```

詳細な推奨バリアントのガイドラインは [usage-guidelines.md](references/usage-guidelines.md#frames使用ルール推奨バリアント) を参照してください。

---

### 1. 既存コンポーネントの使用

新しいページを作る際は、必ず[components-catalog.md](references/components-catalog.md)を参照して既存コンポーネントを使用します。

```tsx
// 良い例：既存コンポーネントを組み合わせる
import { Container } from '@/components/frames/Container';
import { GridFrame } from '@/components/frames/GridFrame';
import { Panel } from '@/components/frames/Panel';
import { Button } from '@/components/atoms/Button';

export default function DashboardPage() {
  return (
    <Container variant="wide">
      <h1 className="text-3xl font-bold mb-8">ダッシュボード</h1>
      <GridFrame columns={3} gap="md">
        <Panel variant="elevated" padding="md">...</Panel>
        <Panel variant="elevated" padding="md">...</Panel>
        <Panel variant="elevated" padding="md">...</Panel>
      </GridFrame>
    </Container>
  );
}

// 悪い例：新規コンポーネントを作成
// 警告: src/components/atoms/CustomCard.tsx を作成しない
```

### 2. セマンティックトークンの使用

セマンティック変数を使ってセマンティックトークンを使用し、ハードコードを避けます。

```tsx
// 良い例：セマンティックトークン使用
<div className="bg-base text-text-base border border-border">

// 悪い例：セマンティック変数を使わない
<div className="bg-[#1a1a1a] text-[#ffffff] border border-[#333333]">
```

### 3. スペーシングのルール

8pxの倍数を基準にし、8, 16, 24, 32, 48, 64pxなどを使用します。

```tsx
// 良い例：8pxの倍数
<div className="p-4 gap-6">  {/* 16px, 24px */}

// 悪い例：任意の値
<div className="p-[13px] gap-[17px]">
```

### 4. タイポグラフィ階層の遵守

H1、H2、H3の階層を守り、セマンティックな見出しを使用します。

```tsx
// 良い例：セマンティック階層
<h1 className="text-3xl font-bold">メインタイトル</h1>
<h2 className="text-2xl font-bold">セクション見出し</h2>
<h3 className="text-xl font-bold">サブセクション</h3>

// 悪い例：階層がスキップされている
<h1 className="text-3xl font-bold">タイトル</h1>
<h3 className="text-xl font-bold">次の見出し</h3>  {/* H2がない */}
```

### 5. アクセシビリティ対応

フォームには適切なラベルとARIA属性を付与します。

```tsx
// 良い例：アクセシブルなフォーム
<form>
  <label htmlFor="email" className="block text-sm font-bold mb-2">
    メールアドレス
  </label>
  <Input
    id="email"
    type="email"
    aria-required="true"
    aria-invalid={!!error}
    error={error}
  />
</form>
```

## 実装例

### 例1: ダッシュボードページ

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
            <h2 className="text-xl font-bold mb-4">統計サマリー</h2>
            <p className="text-3xl font-bold text-text-primary">1,234</p>
          </Panel>

          <Panel variant="elevated" padding="md">
            <h2 className="text-xl font-bold mb-4">売上合計</h2>
            <p className="text-3xl font-bold text-text-primary">¥5,678,900</p>
          </Panel>

          <Panel variant="elevated" padding="md">
            <h2 className="text-xl font-bold mb-4">達成率</h2>
            <p className="text-3xl font-bold text-text-primary">89%</p>
          </Panel>
        </GridFrame>
      </Container>
    </Section>
  );
}
```

### 例2: フォームページ

```tsx
import { Container } from '@/components/frames/Container';
import { Panel } from '@/components/frames/Panel';
import { Input } from '@/components/atoms/Input';
import { Button } from '@/components/atoms/Button';

export default function CreateUserPage() {
  return (
    <Container variant="narrow" className="py-8">
      <Panel variant="elevated" padding="lg">
        <h1 className="text-2xl font-bold mb-6">ユーザー新規作成</h1>

        <form className="space-y-4">
          <div>
            <label htmlFor="name" className="block text-sm font-bold mb-2">
              名前
            </label>
            <Input id="name" placeholder="山田太郎" />
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-bold mb-2">
              メールアドレス
            </label>
            <Input id="email" type="email" placeholder="example@hexabase.com" />
          </div>

          <div className="flex gap-4 pt-4">
            <Button variant="secondary" fullWidth>キャンセル</Button>
            <Button variant="primary" fullWidth>作成</Button>
          </div>
        </form>
      </Panel>
    </Container>
  );
}
```

## よくある質問

### Q: 既存コンポーネントがない場合はどうすればいいですか？

A: 既存コンポーネントを組み合わせて実現できないか検討してください。どうしても必要な場合は、`Panel`や`div`を組み合わせて簡易的に実装できます。ただし、スキル使用時は既存コンポーネントを最大限活用することが目的です。新しいコンポーネントが必要な場合は、ユーザーに相談してください。

### Q: レイアウトパターンが見つからない場合はどうしますか？

A: [layout-patterns.md](references/layout-patterns.md)のパターンを組み合わせるか、Container + GridFrame + Panelの組み合わせで実装してください。

### Q: カラートークンや任意の値を使いたい場合はどうしますか？

A: [design-system.md](references/design-system.md)または[usage-guidelines.md](references/usage-guidelines.md)を参照してください。

## 実装時の心構え

- **必ず`src/app/globals.css`を参照する**: 定義されているセマンティックカラーを把握し、それのみを使用
- **まず[components-catalog.md](references/components-catalog.md)を確認**: 利用可能なコンポーネントを把握
- **[layout-patterns.md](references/layout-patterns.md)を参考にする**: 既存パターンから学ぶ
- **セマンティックトークンを使用し、ハードコードを避ける**: 保守性を高める
- **Tailwindデフォルトカラーを使わない**: `text-yellow-400`などは使用禁止
- **適切な見出し階層を使用**: SEOとアクセシビリティ
- **アクセシビリティを意識する**: フォームには適切なラベルを

## まとめ

Novaflameは**既存コンポーネントを組み合わせて**、一貫性のある美しいUIページを構築するためのデザインシステムです。カラートークンを使い、適切なスペーシングとアクセシビリティを守り、Hexabaseプロダクト全体で統一感のあるUIを実現します。
