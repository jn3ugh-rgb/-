import streamlit as st
import plotly.graph_objects as go

# --- ページ設定 ---
st.set_page_config(
    page_title="Partnership Health Check",
    page_icon="❤️",
    layout="wide"  # ワイド表示にして文章を読みやすく
)

# --- スタイリング (Dark Mode Safe & Readability) ---
st.markdown("""
<style>
    /* 全体のフォント調整 */
    body {
        font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
    }
    /* レポートボックス */
    .report-card {
        background-color: #ffffff;
        color: #1e1e1e;
        padding: 25px;
        border-radius: 12px;
        border-left: 8px solid #FF4B4B;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .report-card h3 {
        color: #d32f2f;
        margin-top: 0;
        font-size: 1.4em;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
    }
    .report-card h4 {
        color: #444;
        margin-top: 15px;
        margin-bottom: 5px;
        font-size: 1.1em;
        font-weight: bold;
    }
    .report-card p {
        line-height: 1.8;
        font-size: 1.05em;
        margin-bottom: 15px;
    }
    /* 強みボックス */
    .asset-card {
        background-color: #f1f8e9;
        color: #2e7d32;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #c8e6c9;
        margin-bottom: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- ヘッダーエリア ---
st.title("❤️ Partnership Health Check / Deep Strategy")
st.markdown("""
あなたのパートナーシップの状態を**「8つの指標」**から徹底的に分解・言語化します。  
表面的なスコアだけでなく、その裏にある**「関係性の構造」**と**「心理的背景」**まで踏み込んで分析します。
""")

st.divider()

# --- 入力フォーム ---
with st.form("check_form"):
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        st.subheader("Ⅰ. 言語的コミュニケーション (Verbal)")
        st.info("言葉による「意思表示」と「受容」のバランス")
        q1 = st.slider("Q1. 【発信：快】ポジティブな要望（好き・したい）を伝えている", 0, 10, 5)
        q2 = st.slider("Q2. 【発信：不快】ネガティブな主張（嫌・やめて）を冷静に伝えている", 0, 10, 5)
        q3 = st.slider("Q3. 【受信：快】相手の「夢」や「やりたいこと」に関心を持っている", 0, 10, 5)
        q4 = st.slider("Q4. 【受信：不快】相手の「NO」や断りを、不機嫌にならず受け止めている", 0, 10, 5)

    with col_input2:
        st.subheader("Ⅱ. 非言語・身体 (Non-Verbal & Physical)")
        st.info("二人の間に流れる「空気感」と「体温」")
        q5 = st.slider("Q5. 【空気感】相手が話しやすい「安心できる空気・表情」を作っている", 0, 10, 5)
        q6 = st.slider("Q6. 【スキンシップ】日常的に手をつなぐ等の肌の温もりを大切にしている", 0, 10, 5)

        st.subheader("Ⅲ. 行動的コミュニケーション (Action)")
        st.info("相手のために「すること」と「ただ居ること」")
        q7 = st.slider("Q7. 【能動的貢献(Doing)】家事やサポートなど、相手のための行動をしている", 0, 10, 5)
        q8 = st.slider("Q8. 【受動的共有(Being)】何もしない時間を心地よく共有できている", 0, 10, 5)

    submitted = st.form_submit_button("深層分析レポートを作成する", type="primary")


# --- ロジックコア：グレード判定関数 ---
def get_grade(score):
    if score <= 2: return "Danger"
    if score <= 4: return "Warning"
    if score <= 6: return "Average"
    if score <= 8: return "Good"
    return "Master"

# --- 深層診断ロジック ---
def generate_deep_feedback(q1, q2, q3, q4, q5, q6, q7, q8):
    reports = []

    # グレード変換
    g_q1, g_q2 = get_grade(q1), get_grade(q2)
    g_q3, g_q4 = get_grade(q3), get_grade(q4)
    g_q7, g_q8 = get_grade(q7), get_grade(q8)

    # ---------------------------------------------------------
    # 分析1: 「NOと言える力」の深度分析 (Q2 focus)
    # ---------------------------------------------------------
    if g_q2 in ["Danger", "Warning"]:
        title = "🛡️ 『境界線』の喪失と自己犠牲"
        if g_q1 in ["Good", "Master"]:
            # YESは言えるがNOは言えない（良い子ちゃん）
            analysis = """
            あなたは「やりたいこと」は明るく提案できる一方で、「嫌だ」という感情には蓋をしてしまう傾向が強く出ています。
            これは典型的な**「愛着不安による迎合」**のパターンです。「NOと言ったら、場の空気が悪くなる」「嫌われるかもしれない」という無意識の恐れが、あなたの口を塞いでいます。
            しかし、ネガティブな感情を共有できない関係は、実は非常に脆いものです。あなたが我慢することで保たれている平和は、いつかあなたの心が折れた時に崩壊してしまいます。
            """
            action = """
            まずは「小さなNO」からリハビリを始めましょう。重要な決断ではなく、「今日はその店に行きたくない」「今は疲れているから話せない」といった、些細な拒否を伝えてみてください。
            あなたが断っても、相手はあなたを嫌いになったりしない。その「安全確認」を積み重ねることが、今のあなたには必要です。
            """
        else:
            # YESもNOも言えない（完全受け身）
            analysis = """
            自分の意思を表明すること自体に、強いブロックがかかっています。相手に合わせすぎて、自分自身の輪郭がぼやけてしまっている危険な状態です。
            「どうせ聞いてもらえない」という諦めがあるか、あるいは「自分には主張する権利がない」と自己価値を低く見積もっている可能性があります。
            """
            action = """
            パートナーシップの前に、まずは「自分を取り戻す」時間が必要です。相手がいないところで、自分が何を食べたいか、何をしたいかを真剣に考え、それを一人で実行してみてください。
            """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析2: 「受信力」と「安全基地」の相関 (Q3, Q4, Q5)
    # ---------------------------------------------------------
    receptivity_score = q3 + q4 + q5
    if receptivity_score <= 12: # 平均4以下
        title = "📡 『受信アンテナ』の感度低下"
        analysis = """
        相手の信号を受け取る力が全体的に弱まっています。特に深刻なのは、相手が発しているであろう「無言のサイン」や「小さなSOS」を見落としている可能性が高いことです。
        あなたの余裕のなさが、知らず知らずのうちに**「今は話しかけないでオーラ」**となって相手を威圧しているかもしれません。
        この状態が続くと、パートナーは「この人に何を言っても無駄だ」と学習性無力感に陥り、ある日突然、関係の終了を告げられるリスクがあります。
        """
        action = """
        「聞く」ことの定義を変えてみましょう。アドバイスや解決策を出す必要はありません。
        ただ相手の目を見て、相手が話し終わるまで沈黙を守る。そして「そうなんだね」と繰り返す。
        この「能動的な沈黙」こそが、今の二人に最も必要なコミュニケーションです。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析3: Doing(貢献) vs Being(共有) のバランス (Q7, Q8)
    # ---------------------------------------------------------
    diff_action = q7 - q8
    if diff_action >= 3: # 貢献ばかりして、ただ一緒にいるのが苦手
        title = "🏃‍♂️ 『ワーカホリック』な愛情表現"
        analysis = """
        あなたは「相手の役に立つこと」でしか、自分の存在価値を感じられなくなっているかもしれません。
        家事をする、稼ぐ、問題を解決する…そういった「機能」としての自分を提供し続けていないと、愛される自信がないのです。
        しかし、皮肉なことに、あなたが動けば動くほど、パートナーは「私は信頼されていない」「ただの同居人だ」と感じてしまうことがあります。
        """
        action = """
        最大の戦略は**「あえて、何もしない」**ことです。
        今週末は、生産的なことを一切禁止してみませんか？ 掃除も料理も手抜きにして、ただソファで二人でダラダラする。
        その「無駄な時間」に耐えられた時、あなたは「何もしなくても愛されている」という事実を知ることになります。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})
    
    elif diff_action <= -3: # 何もしないけど、一緒にいる（ヒモ・依存傾向？）
        title = "🛋️ 『依存的共生』の落とし穴"
        analysis = """
        一緒にいることの居心地は良いようですが、相手への能動的な貢献が不足しています。
        「言わなくてもわかってくれる」「やってくれるのが当たり前」という甘えが、相手の負担を限界まで高めている可能性があります。
        今の快適さは、パートナーの隠れた我慢の上に成り立っている砂上の楼閣かもしれません。
        """
        action = """
        相手が普段やっている「名もなき家事」や「気遣い」を数えてみてください。
        そして、頼まれる前に一つだけ、自分から動いてみる。「ゴミをまとめる」だけでもいいです。あなたの主体的な行動が、相手の孤独感を癒やします。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析4: スキンシップと親密性 (Q6 focus)
    # ---------------------------------------------------------
    if g_q6 in ["Danger", "Warning"] and g_q8 in ["Good", "Master"]:
        title = "🤝 『戦友』から『恋人』への回帰"
        analysis = """
        「一緒にいて楽」だし「信頼もしている」。しかし、そこに「肌の触れ合い」だけが欠落している、典型的な**「熟年夫婦的・ルームメイト化」**の現象です。
        精神的なつながりは強いですが、動物的な、本能的なつながりが希薄になっています。
        これは放置すると「セックスレス」の固定化を招き、心の距離まで少しずつ広げてしまう原因になります。
        """
        action = """
        いきなり濃厚な接触をする必要はありません。「情報のやり取り」ではないタッチを増やしましょう。
        出かける前のハイタッチ、テレビを見ている時に膝が触れ合う距離に座る、相手の肩を揉む。
        言葉を介さないコミュニケーションが、脳内のオキシトシン（愛情ホルモン）を分泌させ、理屈ではない安心感を生み出します。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析5: 理想的な状態へのネクストステップ (Overall Good)
    # ---------------------------------------------------------
    avg_score = (q1+q2+q3+q4+q5+q6+q7+q8) / 8
    if avg_score >= 7 and len(reports) == 0:
        title = "👑 『成熟した関係』の、その先へ"
        analysis = """
        おめでとうございます。あなたのパートナーシップは、非常に高いレベルでバランスが取れています。
        お互いが自立し、かつ健全に依存し合える、多くの人が羨む理想的な状態です。
        大きな問題がない今だからこそ、守りに入るのではなく、二人の未来を「創造」するフェーズに入っています。
        """
        action = """
        日常のメンテナンスは十分できています。次は「非日常」のビジョンを共有しましょう。
        「3年後、二人でどんな景色を見ていたいか？」「どんな人生なら最高か？」
        トラブル解決のためではなく、夢を語るためのミーティングをセットしてみてください。それが二人の絆を「最強」にします。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # レポートがない（平均的）場合のフォールバック
    if len(reports) == 0:
        title = "⚖️ 『凪（なぎ）』の状態・現状維持の罠"
        analysis = """
        極端に悪いところもなければ、飛び抜けて良いところもない。今の二人は、ある意味で「安定」しています。
        しかし、パートナーシップにおいて「現状維持」は「緩やかな後退」を意味することがあります。
        大きな不満がないからこそ、情熱や関心が薄れ、日々の業務連絡だけの関係になりやすい時期でもあります。
        """
        action = """
        「8つの項目」の中で、一番点数が低かった項目を一つだけピックアップしてください。
        今週は、その「たった一つの項目」だけを意識して10％改善してみるゲームをしましょう。
        全体を良くしようとする必要はありません。一点突破が、全体の空気を変えるトリガーになります。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    return reports

# --- 結果表示UI ---
if submitted:
    st.divider()
    
    # 1. レーダーチャート (前回と同じだが大きく表示)
    labels = ['発信:快', '発信:不快', '受信:快', '受信:不快', '空気感', 'スキンシップ', '貢献(Doing)', '共有(Being)']
    values = [q1, q2, q3, q4, q5, q6, q7, q8]
    values_radar = values + [values[0]]
    labels_radar = labels + [labels[0]]

    col_chart, col_score = st.columns([1, 1])

    with col_chart:
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values_radar, theta=labels_radar, fill='toself', name='Score',
            line_color='#FF4B4B', fillcolor='rgba(255, 75, 75, 0.2)'
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            margin=dict(t=20, b=20, l=40, r=40)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_score:
        st.markdown("### 📊 Overall Status")
        total_score = sum(values)
        st.metric("Total Score", f"{total_score} / 80")
        
        # 簡易フィードバック（強み）
        st.markdown("#### 💎 Relationship Assets")
        if q3 >= 8: st.markdown('<div class="asset-card">👂 卓越した「傾聴力」があります</div>', unsafe_allow_html=True)
        if q5 >= 8: st.markdown('<div class="asset-card">🏠 最高の「安全基地」を作れています</div>', unsafe_allow_html=True)
        if q2 >= 8: st.markdown('<div class="asset-card">🛡️ 健全な「境界線」を持っています</div>', unsafe_allow_html=True)
        if total_score <= 40: st.markdown('<div class="asset-card">🌱 これから「伸びていく」関係です</div>', unsafe_allow_html=True)

    # 2. 深層分析レポート (メインコンテンツ)
    st.header("📋 Deep Diagnostic Report")
    st.markdown("あなたの回答パターンから導き出された、現在の関係性の深層分析です。")
    
    reports = generate_deep_feedback(q1, q2, q3, q4, q5, q6, q7, q8)
    
    for report in reports:
        st.markdown(f"""
        <div class="report-card">
            <h3>{report['title']}</h3>
            <h4>🧐 現状の分析と心理的背景</h4>
            <p>{report['analysis']}</p>
            <h4>🚀 今すぐできる戦略的アクション</h4>
            <p>{report['action']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("※ この診断結果は、今の瞬間の「断面図」に過ぎません。定期的にチェックすることで、変化を感じ取ることができます。")