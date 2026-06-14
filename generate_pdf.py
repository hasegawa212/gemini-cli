from fpdf import FPDF, XPos, YPos

# PDF クラス定義（日本語対応フォント設定）
class PDF(FPDF):
    def header(self):
        self.set_font("NotoSansCJK", "B", 16)
        self.cell(0, 10, "商談プロセス総括報告書", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(5)

# PDF作成
pdf = PDF()
# 日本語フォント（Noto Sans CJK JP）を追加
pdf.add_font("NotoSansCJK", "", "fonts/NotoSansCJKjp-Regular.otf")
pdf.add_font("NotoSansCJK", "B", "fonts/NotoSansCJKjp-Bold.otf")
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("NotoSansCJK", size=12)

# コンテンツ
content = """
【概要】
・訪問から商談・クロージング・アフターフォローまでの全工程を整理。
・目的：営業プロセスの標準化と心理的アプローチの共有。

【導入トーク】
・顧客の関心を引く第一印象の形成。
・信頼構築のための共感的アプローチ。

【ヒアリング】
・顧客課題とニーズの明確化。
・潜在的需要の発掘。

【提案フェーズ】
・製品・サービス訴求点の提示。
・競合比較を踏まえた説得要素の設計。

【クロージング】
・意思決定を促す心理的トリガー。
・条件提示の最適化による成約率向上。

【アフターフォロー】
・顧客満足度の維持と信頼深化。
・リピート・紹介につながる仕組みづくり。

【成果・課題・今後の方針】
・成果：商談成立率・顧客満足度の向上。
・課題：提案資料の強化、タイミング調整。
・今後：営業トークの標準化と改善サイクル確立。
"""

pdf.multi_cell(0, 10, content)

# 保存
file_path = "商談プロセス総括報告書.pdf"
pdf.output(file_path)

print(f"PDFが作成されました: {file_path}")
