# Novaflame Design System

Novaflameは、Captain UIをベースとしたHexabaseプロダクト全体のデザイン標準です。Adobe Spectrumの設計思想を参考に、一貫性のある美しいUIを提供します。

## Table of Contents

- [カラーシステム](#カラーシステム)
- [タイポグラフィ](#タイポグラフィ)
- [スペーシング](#スペーシング)
- [テーマ（ダーク/ライト）](#テーマダークライト)

---

## カラーシステム

### プリミティブカラーパレット

Novaflameは、2つの主要なカラーパレットで構成されています：

#### Brand Neutral（グレースケール）

```css
--brand-neutral-0: #ffffff    /* 純白 */
--brand-neutral-50: #f2f2f2
--brand-neutral-100: #e5e5e5
--brand-neutral-200: #cccccc
--brand-neutral-300: #b2b2b2
--brand-neutral-400: #999999
--brand-neutral-500: #808080
--brand-neutral-600: #666666
--brand-neutral-700: #4d4d4d
--brand-neutral-800: #333333
--brand-neutral-900: #1a1a1a
--brand-neutral-950: #0a0a0a   /* 純黒に近い */
```

#### Brand Primary（ティール）

Hexabaseのブランドカラーはティール系です：

```css
--brand-primary-50: #eafdfc
--brand-primary-100: #d4fff9
--brand-primary-200: #aafff3
--brand-primary-300: #09ffdd
--brand-primary-400: #00f0cf
--brand-primary-500: #00dabc
--brand-primary-600: #00c6ab   /* メインアクセントカラー */
--brand-primary-700: #00b29a
--brand-primary-800: #00a08b
--brand-primary-900: #00907d
```

**推奨使用**: `--brand-primary-600` をアクセントカラーとして使用

#### セマンティックカラー

```css
/* Error（エラー） */
--error-default: #dc2626
--error-bg: #fee2e2
--error-border: #dc2626

/* Success（成功） */
--success-default: #16a34a
--success-bg: #dcfce7
--success-border: #16a34a
```

### セマンティックトークン（テーマ対応）

実際のコンポーネントでは、セマンティックトークンを使用します：

```css
/* Tailwindクラス */
bg-main           /* メイン背景 */
bg-base           /* ベース背景（カード、パネルなど） */
bg-accent         /* アクセント背景 */

text-text-base    /* メインテキスト */
text-text-sub     /* サブテキスト */
text-text-primary /* プライマリテキスト（アクセントカラー） */

border-border     /* デフォルトボーダー */
```

---

## タイポグラフィ

### フォントファミリー

```css
/* 日本語 - Yu Gothic */
--font-family-sans: "Yu Gothic", "游ゴシック", YuGothic, "Hiragino Sans", ...

/* モノスペース - Geist Mono */
--font-family-mono: var(--font-geist-mono), monospace
```

**Tailwindクラス**: `font-sans`, `font-mono`

### フォントサイズ

Novaflameでは、ユーザースケール対応のフォントサイズシステムを採用しています（アクセシビリティ機能）：

```css
--font-size-2xs: 10px
--font-size-xs: 12px
--font-size-sm: 14px
--font-size-base: 16px   /* デフォルト */
--font-size-lg: 18px
--font-size-xl: 21px
--font-size-2xl: 24px
--font-size-3xl: 32px
```

**Tailwindクラス**: `text-2xs`, `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl`, `text-3xl`

### フォントウェイト

```css
--font-weight-regular: 400   /* font-normal */
--font-weight-bold: 600      /* font-bold */
```

### レタースペーシング

```css
--letter-spacing-heading-jp: 0.05em   /* 日本語見出し */
--letter-spacing-body-jp: 0.05em      /* 日本語本文 */
--letter-spacing-heading-en: 0        /* 英語見出し */
--letter-spacing-body-en: 0           /* 英語本文 */
```

**Tailwindクラス**: `tracking-wide` (0.05em), `tracking-normal` (0), `tracking-tight` (0)

### ラインハイト

```css
--line-height-tight: 1.25
--line-height-snug: 1.375
--line-height-normal: 1.5     /* デフォルト */
--line-height-relaxed: 1.625
--line-height-loose: 2
```

**Tailwindクラス**: `leading-tight`, `leading-snug`, `leading-normal`, `leading-relaxed`, `leading-loose`

### タイポグラフィ階層の推奨使用

| 用途 | フォントサイズ | フォントウェイト | 使用例 |
|------|--------------|----------------|--------|
| 大見出し (H1) | `text-3xl` | `font-bold` | ページタイトル |
| 中見出し (H2) | `text-2xl` | `font-bold` | セクション見出し |
| 小見出し (H3) | `text-xl` | `font-bold` | サブセクション |
| 強調テキスト | `text-lg` | `font-bold` | 重要なラベル |
| 本文 | `text-base` | `font-normal` | 通常のテキスト |
| キャプション | `text-sm` | `font-normal` | 補足情報 |
| 小さいラベル | `text-xs` | `font-normal` | フォームラベル |

### ページタイトルの使用ルール

**重要**: ページのメインタイトルには、`PageTitle`コンポーネントを`level={4}`で使用してください。

```tsx
import { PageTitle } from '@/components/atoms/PageTitle';

// ✅ 推奨：level-4を使用（text-lg / 18px）
<PageTitle level={4}>Pod管理</PageTitle>

// ❌ 非推奨：level-1（デフォルト）は大きすぎる
<PageTitle>Pod管理</PageTitle>
```

**理由**:
- `level={4}`（`text-lg` / 18px）は、統計カードやコンテンツとのバランスが最適
- `level={1}`（`text-3xl` / 32px）は大きすぎてページ全体のバランスを崩す
- 一貫性のあるページ構造を維持できる

---

## スペーシング

Novaflameは、8pxを基準とした体系的なスペーシングシステムを採用しています：

```css
--spacing-xs: 2px           /* 0.5 → p-0.5, gap-0.5 */
--spacing-sm: 4px           /* 1 → p-1, gap-1 */
--spacing-md: 8px           /* 2 → p-2, gap-2 */
--spacing-base: 16px        /* 4 → p-4, gap-4 */
--spacing-lg: 24px          /* 6 → p-6, gap-6 */
--spacing-xl: 32px          /* 8 → p-8, gap-8 */
--spacing-xxl: 40px         /* 10 → p-10, gap-10 */
--spacing-xxxl: 48px        /* 12 → p-12, gap-12 */
--spacing-plus: 56px        /* 14 → p-14, gap-14 */
--spacing-extended: 64px    /* 16 → p-16, gap-16 */
--spacing-super: 80px       /* 20 → p-20, gap-20 */
--spacing-queen: 120px      /* 30 → p-30, gap-30 (カスタム) */
--spacing-king: 160px       /* 40 → p-40, gap-40 */
```

### スペーシング使用ガイドライン

| 用途 | 推奨値 | Tailwindクラス例 |
|------|--------|-----------------|
| コンポーネント内の小さな余白 | 4px-8px | `p-1`, `p-2`, `gap-2` |
| コンポーネント内の標準余白 | 16px | `p-4`, `gap-4` |
| コンポーネント間の余白 | 16px-24px | `gap-4`, `gap-6` |
| セクション間の余白 | 32px-48px | `py-8`, `py-12` |
| 大きなセクション間 | 64px以上 | `py-16`, `py-20` |

**原則**: 8の倍数（8px, 16px, 24px, 32px...）を優先的に使用してください。

---

## テーマ（ダーク/ライト）

Novaflameは、ダークテーマとライトテーマの両方をサポートしています。

### ダークテーマ（デフォルト）

```css
--theme-main: #0a0a0a           /* メイン背景（ほぼ黒） */
--theme-base: #1a1a1a           /* ベース背景（カード等） */
--theme-attention: #00c6ab      /* アクセント（ティール） */
--theme-text-base: #ffffff      /* メインテキスト（白） */
--theme-text-sub: #999999       /* サブテキスト（グレー） */
--theme-border: #333333         /* ボーダー */
```

### ライトテーマ

```css
--theme-main: #f2f2f2           /* メイン背景（明るいグレー） */
--theme-base: #ffffff           /* ベース背景（白） */
--theme-attention: #d4fff9      /* アクセント（明るいティール） */
--theme-text-base: #1a1a1a      /* メインテキスト（黒） */
--theme-text-primary: #00b29a   /* プライマリテキスト */
--theme-border: #e5e5e5         /* ボーダー */
```

### テーマ切り替え

テーマは`.dark`または`.light`クラスで切り替えます：

```tsx
<body className="dark">  {/* ダークテーマ */}
<body className="light"> {/* ライトテーマ */}
```

セマンティックトークン（`bg-main`、`text-text-base`など）を使用すれば、テーマ切り替えが自動で反映されます。

---

## デザイントークンの使用方法

### ✅ 推奨：セマンティックトークンを使用

```tsx
<div className="bg-base text-text-base border border-border">
  <h1 className="text-2xl font-bold text-text-primary">タイトル</h1>
  <p className="text-sm text-text-sub">説明文</p>
</div>
```

### ❌ 非推奨：プリミティブカラーを直接使用

```tsx
<div className="bg-[#1a1a1a] text-[#ffffff]">  {/* テーマ切り替えが機能しない */}
```

**原則**: 常にセマンティックトークンを使用し、テーマ切り替えに対応させてください。
