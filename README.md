# IE3 Second Semester Electrical Engineering Lab

3年後期の電子工学実験資料と、LuaLaTeXのレポートひな形・予習プリントです。

## フォルダ構成

- 各実験の直下：資料のA4版PDF、レポートと予習のTeX。
- 各実験の build/：コンパイル済みPDF、ログ、aux、SyncTeX等のすべての出力。
- [preamble.tex](preamble.tex)：日本語フォント、余白、表紙、振り返り、記入枠等を集約。各文書が \input{../preamble.tex} で読み込みます。

## 文書一覧

| 実験                                       | レポート                                                                                                                                                          | 予習プリント                                                                                                                                                      |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A：回路網                                  | [TeX](IE3_expA_回路網/IE3_expA_report.tex) / [PDF](IE3_expA_回路網/build/IE3_expA_report.pdf)                                                                     | [TeX](IE3_expA_回路網/IE3_expA_prelab.tex) / [PDF](IE3_expA_回路網/build/IE3_expA_prelab.pdf)                                                                     |
| B：共振回路                                | [TeX](IE3_expB_共振回路/IE3_expB_report.tex) / [PDF](IE3_expB_共振回路/build/IE3_expB_report.pdf)                                                                 | [TeX](IE3_expB_共振回路/IE3_expB_prelab.tex) / [PDF](IE3_expB_共振回路/build/IE3_expB_prelab.pdf)                                                                 |
| C：電源回路                                | [TeX](IE3_expC_電源回路/IE3_expC_report.tex) / [PDF](IE3_expC_電源回路/build/IE3_expC_report.pdf)                                                                 | [TeX](IE3_expC_電源回路/IE3_expC_prelab.tex) / [PDF](IE3_expC_電源回路/build/IE3_expC_prelab.pdf)                                                                 |
| D：LC発振回路                              | [TeX](IE3_expD_発振回路/IE3_expD_report.tex) / [PDF](IE3_expD_発振回路/build/IE3_expD_report.pdf)                                                                 | [TeX](IE3_expD_発振回路/IE3_expD_prelab.tex) / [PDF](IE3_expD_発振回路/build/IE3_expD_prelab.pdf)                                                                 |
| E：マルチバイブレータ                      | [TeX](IE3_expE_マルチバイブレータ/IE3_expE_report.tex) / [PDF](IE3_expE_マルチバイブレータ/build/IE3_expE_report.pdf)                                             | [TeX](IE3_expE_マルチバイブレータ/IE3_expE_prelab.tex) / [PDF](IE3_expE_マルチバイブレータ/build/IE3_expE_prelab.pdf)                                             |
| F：カウンタ回路                            | [TeX](IE3_expF_カウンタ回路/IE3_expF_report.tex) / [PDF](IE3_expF_カウンタ回路/build/IE3_expF_report.pdf)                                                         | [TeX](IE3_expF_カウンタ回路/IE3_expF_prelab.tex) / [PDF](IE3_expF_カウンタ回路/build/IE3_expF_prelab.pdf)                                                         |
| G1：マイコンによるステッピング・モータ制御 | [TeX](IE3_expG1_マイコンによるステッピング・モータ制御/IE3_expG1_report.tex) / [PDF](IE3_expG1_マイコンによるステッピング・モータ制御/build/IE3_expG1_report.pdf) | [TeX](IE3_expG1_マイコンによるステッピング・モータ制御/IE3_expG1_prelab.tex) / [PDF](IE3_expG1_マイコンによるステッピング・モータ制御/build/IE3_expG1_prelab.pdf) |
| G2：マイコンによる7セグメントLED表示制御   | [TeX](IE3_expG2_マイコンによる7セグメントLED表示制御/IE3_expG2_report.tex) / [PDF](IE3_expG2_マイコンによる7セグメントLED表示制御/build/IE3_expG2_report.pdf)     | [TeX](IE3_expG2_マイコンによる7セグメントLED表示制御/IE3_expG2_prelab.tex) / [PDF](IE3_expG2_マイコンによる7セグメントLED表示制御/build/IE3_expG2_prelab.pdf)     |
| H：PICを用いたフルカラーLED制御            | [TeX](IE3_expH_PICを用いたフルカラーLED制御/IE3_expH_report.tex) / [PDF](IE3_expH_PICを用いたフルカラーLED制御/build/IE3_expH_report.pdf)                         | [TeX](IE3_expH_PICを用いたフルカラーLED制御/IE3_expH_prelab.tex) / [PDF](IE3_expH_PICを用いたフルカラーLED制御/build/IE3_expH_prelab.pdf)                         |
| I：A/D変換とD/A変換                        | [TeX](IE3_expI_AD変換とDA変換/IE3_expI_report.tex) / [PDF](IE3_expI_AD変換とDA変換/build/IE3_expI_report.pdf)                                                     | [TeX](IE3_expI_AD変換とDA変換/IE3_expI_prelab.tex) / [PDF](IE3_expI_AD変換とDA変換/build/IE3_expI_prelab.pdf)                                                     |
| J：PLCによるシーケンス制御                 | [TeX](IE3_expJ_PLCによるシーケンス制御/IE3_expJ_report.tex) / [PDF](IE3_expJ_PLCによるシーケンス制御/build/IE3_expJ_report.pdf)                                   | [TeX](IE3_expJ_PLCによるシーケンス制御/IE3_expJ_prelab.tex) / [PDF](IE3_expJ_PLCによるシーケンス制御/build/IE3_expJ_prelab.pdf)                                   |

## VS Code / LaTeX Workshop

1. このルートフォルダをVS Codeで開き、各実験の *_report.tex または *_prelab.tex を開きます。
2. 「LaTeX Workshop: Build LaTeX project」を実行します。レシピは LuaLaTeX (latexmk) です。保存時にもビルドします。
3. 「LaTeX Workshop: View LaTeX PDF file」で build/ 内の対応PDFを開きます。

共有プリアンブル単体ではなく本文のTeXをビルドしてください。各本文の先頭には自身を指定する % !TEX root を設定しています。
[.vscode/settings.json](.vscode/settings.json) がビルド・プレビュー先を指定し、[.latexmkrc](.latexmkrc) も build/ を出力先にしています。

TeX Live / MacTeX、latexmk、LaTeX Workshopが必要です。主なパッケージは jlreq、luatexja-fontspec、amsmath、tabularx、booktabs、tikz、circuitikz、hyperref、日本語は原ノ味フォントです。この環境ではTeX Live 2026 / LuaHBTeXを使用しました。

### コマンドによるビルド

ルートから1文書をビルド：

~~~sh
latexmk -cd -lualatex -outdir=build 'IE3_expA_回路網/IE3_expA_report.tex'
~~~

全22文書をビルド：

~~~sh
python3 scripts/build_lab_documents.py
~~~

全体ビルドの標準出力も各 build/*.build.log に保存します。PDFはGit対象とし、他の補助ファイルは.gitignoreで除外します。

## レポートの使い方

表紙、事前・事後の記録、器具番号・レンジ・実際の素子値を記入します。目的・原理・手順は資料から整理済みです。
測定表を埋め、必要な行や図を追加してください。波形には測定点、軸、単位、プローブ倍率を示します。
\writing{高さ} は記入枠です。電子提出時には実際の文章や \includegraphics に置き換えます。
実験後に実測データに基づく考察・結論を書きます。予習プリントの例題は実測結果ではありません。

表紙・振り返り・本文構成は First Semester All＿電子工学実験.pdf を参考にしました。見本の氏名や測定結果は転記していません。授業で正式な提出表紙・採点票が指定されている場合はそちらを優先してください。

## 資料の補足

- C：資料のリプル電圧はピーク間値の半分です。
- F：7492全体は12分周で、6進には6分周部分を使用します。
- G2：資料の数字7は27h（fを含む字形）です。
- H：共通アノードLEDの点灯割合はLOW時間の割合です。
- I：ADC0804はメーカー資料の「逐次比較形」に合わせて説明を補足しました。3ビットの並列比較回路とは方式が異なります。

TIの555/ADC0804、MicrochipのPIC12F683、OMRONのCP1L公式資料を補足に使用し、該当プリントにURLを記載しています。

元スキャン画像、中間PDF、OCR・プレビュー等の output/ はGit対象外です。
