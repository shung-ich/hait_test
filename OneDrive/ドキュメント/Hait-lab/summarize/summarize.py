
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import MeCab

#文字数が長すぎるとNon-UTF-8 code starting with '\xe3'というエラーが起こってしまうので文章を分けて読み込む仕組みが必要

document = '人間がお互いにコミュニケーションを行うための自然発生的な言語である。「自然言語」に対置される語に「形式言語」「人工言語」がある。'
document+='形式言語との対比では、その構文や意味が明確に揺るぎなく定められ利用者に厳格な規則の遵守を強いる（ことが多い）形式言語に対し、話者集団の社会的文脈に沿った曖昧な規則が存在していると考えられるものが自然言語である。'
document+='自然言語には、規則が曖昧であるがゆえに、話者による規則の解釈の自由度が残されており、話者が直面した状況に応じて規則の解釈を変化させることで、状況を共有する他の話者とのコミュニケーションを継続する事が可能となっている。'


import MeCab
 
mecab = MeCab.Tagger()
target_str = "DOS窓では、基本的には日本語がアウトです"
print(mecab.parse(target_str))

# 自動要約のオブジェクト
auto_abstractor = AutoAbstractor()

# 日本語のトークナイザーを設定
auto_abstractor.tokenizable_doc = MeCabTokenizer()

# 文のリストを作成するための区切り文字を設定
auto_abstractor.delimiter_list = ["。", "\n"]

# キュメントを抽象化およびフィルタリングするオブジェクト
abstractable_doc = TopNRankAbstractor()

# 変数を渡し文書を要約
result_dict = auto_abstractor.summarize(document, abstractable_doc)

"""result_dictは辞書型となっています。
dict{
     "summarize_result": "要約された文のリスト。", 
     "scoring_data":     "スコアのリスト（重要度のランク）。"
 }
"""

# 出力
for sentence in result_dict["summarize_result"]:
    print(sentence)
