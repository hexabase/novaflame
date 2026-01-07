# Accessibility Guidelines

NovaflameはAdobe Spectrumの設計思想に基づき、WCAG 2.1+準拠のアクセシブルなUIを提供します。すべてのユーザーが快適に使えるインターフェースを実現するためのガイドラインです。

## Table of Contents

- [キーボードナビゲーション](#キーボードナビゲーション)
- [フォーカス管理](#フォーカス管理)
- [カラーコントラスト](#カラーコントラスト)
- [ARIA属性](#aria属性)
- [フォームアクセシビリティ](#フォームアクセシビリティ)
- [モーダルアクセシビリティ](#モーダルアクセシビリティ)

---

## キーボードナビゲーション

すべてのインタラクティブ要素はキーボードのみで操作可能でなければなりません。

### 基本原則

1. **Tab**: 次のフォーカス可能要素へ移動
2. **Shift + Tab**: 前のフォーカス可能要素へ移動
3. **Enter / Space**: ボタンやリンクを実行
4. **Escape**: モーダルやダイアログを閉じる
5. **矢印キー**: リスト、メニュー、タブ内の移動

### 実装例

**適切なフォーカス順序:**

```tsx
// ✅ 良い例：論理的なフォーカス順序
<form>
  <Input placeholder="名前" />           {/* Tab順序: 1 */}
  <Input placeholder="メール" />         {/* Tab順序: 2 */}
  <Button variant="primary">送信</Button>  {/* Tab順序: 3 */}
  <Button variant="secondary">キャンセル</Button> {/* Tab順序: 4 */}
</form>

// ❌ 悪い例：tabIndexを無理やり変更
<form>
  <Input tabIndex={2} />  {/* 混乱を招く */}
  <Input tabIndex={1} />
</form>
```

**キーボードショートカット:**

```tsx
// Escキーでモーダルを閉じる例
useEffect(() => {
  const handleEscape = (e: KeyboardEvent) => {
    if (e.key === 'Escape') {
      onClose();
    }
  };
  document.addEventListener('keydown', handleEscape);
  return () => document.removeEventListener('keydown', handleEscape);
}, [onClose]);
```

---

## フォーカス管理

フォーカスリングは、キーボードユーザーが現在どの要素にフォーカスしているかを示す重要な視覚的手がかりです。

### フォーカスリングの原則

1. **コントラスト比**: 背景に対して最低3:1のコントラスト比（WCAG 2.1+）
2. **可視性**: フォーカス時に明確に表示される
3. **一貫性**: アプリ全体で統一されたスタイル

### Novaflameのフォーカススタイル

`globals.css`でグローバルに定義されています：

```css
*:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

**フォーカスリングの色**: `--color-accent` (ティール: #00c6ab)

### 実装例

**カスタムフォーカススタイル:**

```tsx
// Buttonコンポーネントのフォーカススタイル
<button
  className={cn(
    'focus-visible:outline-none',
    'focus-visible:ring-2 focus-visible:ring-accent',
    'focus-visible:ring-offset-2 focus-visible:ring-offset-main'
  )}
>
  ボタン
</button>
```

**フォーカストラップ（モーダル内）:**

モーダル内でフォーカスをトラップし、モーダル外の要素にフォーカスが移らないようにします：

```tsx
// モーダルが開いた時、最初のフォーカス可能要素にフォーカス
useEffect(() => {
  if (isOpen) {
    const firstFocusable = modalRef.current?.querySelector(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    if (firstFocusable) {
      (firstFocusable as HTMLElement).focus();
    }
  }
}, [isOpen]);
```

---

## カラーコントラスト

視覚障害やカラービジョン欠損を持つユーザーのために、十分なカラーコントラストを確保します。

### WCAG 2.1 コントラスト比要件

| 要素タイプ | 最小コントラスト比 | レベル |
|-----------|------------------|--------|
| 通常テキスト（18px未満） | 4.5:1 | AA |
| 大きいテキスト（18px以上） | 3:1 | AA |
| UIコンポーネント、グラフィック | 3:1 | AA |
| フォーカスインジケーター | 3:1 | AA (WCAG 2.1+) |

### Novaflameのカラーコントラスト

**ダークテーマ:**
- テキスト（#ffffff）vs 背景（#0a0a0a）: **19:1** ✅
- アクセント（#00c6ab）vs 背景（#0a0a0a）: **8.5:1** ✅
- サブテキスト（#999999）vs 背景（#0a0a0a）: **4.7:1** ✅

**ライトテーマ:**
- テキスト（#1a1a1a）vs 背景（#ffffff）: **19:1** ✅
- プライマリテキスト（#00b29a）vs 背景（#ffffff）: **3.2:1** ✅

### 使用ガイドライン

```tsx
// ✅ 良い例：十分なコントラスト
<p className="text-text-base">メインテキスト</p>        {/* 19:1 */}
<p className="text-text-sub">サブテキスト</p>           {/* 4.7:1 */}

// ❌ 悪い例：不十分なコントラスト
<p className="text-[#555555]">読みにくいテキスト</p>   {/* 2.5:1 - 基準未達 */}
```

---

## ARIA属性

スクリーンリーダーユーザーのために、適切なARIA属性を使用します。

### 基本的なARIA属性

**ボタン:**

```tsx
<button
  aria-label="メニューを開く"
  aria-expanded={isOpen}
  aria-controls="menu-dropdown"
>
  <MenuIcon />
</button>
```

**フォーム:**

```tsx
<form aria-labelledby="form-title">
  <h2 id="form-title">ユーザー登録</h2>

  <div>
    <label htmlFor="username">ユーザー名</label>
    <input
      id="username"
      type="text"
      aria-required="true"
      aria-invalid={hasError}
      aria-describedby={hasError ? "username-error" : undefined}
    />
    {hasError && (
      <p id="username-error" className="text-error">
        ユーザー名は必須です
      </p>
    )}
  </div>
</form>
```

**モーダル:**

```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <h2 id="modal-title">確認</h2>
  <p id="modal-description">本当に削除しますか？</p>
</div>
```

**ライブリージョン（動的コンテンツ）:**

```tsx
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
>
  {message && <p>{message}</p>}
</div>
```

---

## フォームアクセシビリティ

フォームは多くのユーザーにとって重要なインタラクションポイントです。

### 必須要素

1. **Label**: すべてのInputに対応するlabelを提供
2. **エラーメッセージ**: aria-invalid、aria-describedbyで関連付け
3. **必須フィールド**: aria-required="true"を追加
4. **フィールドグループ**: fieldsetとlegendでグループ化

### 実装例

```tsx
<form>
  {/* ラベルとInputの関連付け */}
  <div>
    <label htmlFor="email" className="block text-sm font-bold mb-2">
      メールアドレス <span className="text-error">*</span>
    </label>
    <Input
      id="email"
      type="email"
      aria-required="true"
      aria-invalid={!!emailError}
      aria-describedby={emailError ? "email-error" : undefined}
      error={emailError}
    />
    {emailError && (
      <p id="email-error" className="text-xs text-error mt-1">
        {emailError}
      </p>
    )}
  </div>

  {/* ラジオボタンのグループ */}
  <fieldset>
    <legend className="text-sm font-bold mb-2">テーマ選択</legend>
    <div className="space-y-2">
      <label className="flex items-center gap-2">
        <input type="radio" name="theme" value="dark" />
        ダークテーマ
      </label>
      <label className="flex items-center gap-2">
        <input type="radio" name="theme" value="light" />
        ライトテーマ
      </label>
    </div>
  </fieldset>

  <Button type="submit" variant="primary">送信</Button>
</form>
```

---

## モーダルアクセシビリティ

モーダルは適切に実装しないとアクセシビリティの問題を引き起こします。

### モーダルの要件

1. **フォーカストラップ**: モーダル内でフォーカスを保持
2. **Escキーで閉じる**: キーボードで閉じられる
3. **role="dialog"**: スクリーンリーダーに通知
4. **aria-modal="true"**: モーダルであることを明示
5. **初期フォーカス**: 開いた時に適切な要素にフォーカス
6. **閉じた後**: 元の要素にフォーカスを戻す

### 実装例

```tsx
function AccessibleModal({ isOpen, onClose }) {
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      // 開く前のフォーカス要素を保存
      previousFocusRef.current = document.activeElement as HTMLElement;
    } else {
      // 閉じた後、元の要素にフォーカスを戻す
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <div
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
      >
        <h2 id="modal-title" className="text-xl font-bold mb-4">
          モーダルタイトル
        </h2>
        <p>モーダルコンテンツ</p>
        <div className="flex gap-4 mt-6">
          <Button variant="secondary" onClick={onClose}>
            キャンセル
          </Button>
          <Button variant="primary" onClick={handleConfirm}>
            確認
          </Button>
        </div>
      </div>
    </Modal>
  );
}
```

---

## アクセシビリティチェックリスト

新しいページやコンポーネントを作成する際は、以下をチェックしてください：

### キーボード操作
- [ ] すべてのインタラクティブ要素にキーボードでアクセスできる
- [ ] Tabキーで論理的な順序で移動できる
- [ ] フォーカスリングが明確に表示される
- [ ] Escキーでモーダルやダイアログを閉じられる

### 視覚的アクセシビリティ
- [ ] テキストと背景のコントラスト比が4.5:1以上（通常テキスト）
- [ ] カラーだけで情報を伝えていない（エラーは色+テキスト）
- [ ] フォントサイズが十分（最低14px推奨）

### スクリーンリーダー
- [ ] すべての画像にalt属性がある
- [ ] フォームのlabelとInputが関連付けられている
- [ ] エラーメッセージがaria-describedbyで関連付けられている
- [ ] 動的コンテンツにaria-liveが設定されている

### セマンティックHTML
- [ ] 適切なHTML要素を使用（button、nav、mainなど）
- [ ] 見出しレベルが適切（h1→h2→h3）
- [ ] リストはul/olを使用

---

## 参考リソース

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Adobe Spectrum Accessibility](https://react-spectrum.adobe.com/react-aria/index.html)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)

**原則**: アクセシビリティは後付けではなく、最初から組み込むべきものです。すべてのユーザーが快適に使えるUIを目指しましょう。
