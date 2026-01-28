import streamlit as st
import plotly.graph_objects as go

# --- ページ設定 ---
st.set_page_config(
    page_title="Partnership Health Check",
    page_icon="❤️",
    layout="wide"
)

# --- スタイリング (Dark Mode Safe & Soft Design) ---
st.markdown("""
<style>
    /* 全体のフォント調整 */
    body {
        font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;
    }
    /* レポートボックスのデザイン */
    .report-card {
        background-color: #ffffff;
        color: #1e1e1e; /* 文字色を黒固定 */
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
    /* 強みボックスのデザイン */
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
st.title("❤️ Partnership Health Check")
st.markdown("""
あなたのパートナーシップの状態を**「8つの指標」**から多角的に分析します。  
**「今の二人の状態」** として、直感的に最も近い感覚を選んでください。
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


# --- ロジック関数 ---
def get_grade(score):
    if score <= 2: return "Danger"
    if score <= 4: return "Warning"
    if score <= 6: return "Average"
    if score <= 8: return "Good"
    return "Master"

def generate_deep_feedback(q1, q2, q3, q4, q5, q6, q7, q8):
    reports = []

    # グレード変換
    g_q1, g_q2 = get_grade(q1), get_grade(q2)
    g_q3, g_q4 = get_grade(q3), get_grade(q4)
    g_q5, g_q6 = get_grade(q5), get_grade(q6)
    g_q7, g_q8 = get_grade(q7), get_grade(q8)

    # ---------------------------------------------------------
    # 分析1: 「NOと言える力」の深度分析 (Q2 focus)
    # ---------------------------------------------------------
    if g_q2 in ["Danger", "Warning"]:
        # パターン1: 良い子ちゃんタイプ (NO言えないがYESは言える)
        if g_q1 in ["Good", "Master"]:
            title = "🛡️ 『境界線』の曖昧さと、優しさの代償"
            analysis = """
            あなたは「やりたいこと」を明るく提案できる、とてもポジティブなエネルギーを持っています。一方で、相手を気遣うあまり「嫌だ」という感情に少し蓋をしてしまう傾向が見られるかもしれません。
            これは**「関係を壊したくない」という優しさの裏返し**とも言えますが、無意識のうちに「NOと言ったら空気が悪くなるかも」という不安を抱えている可能性があります。
            今の平和な関係は、もしかすると、あなたの「見えない我慢」によって支えられている側面があるかもしれません。
            """
            action = """
            まずは「小さなNO」を伝えるリハビリから始めてみませんか？
            重要な決断ではなく、「今日はそのお店の気分じゃないな」「今は少し疲れているから、後で話そう」といった、些細な本音を小出しにしてみましょう。
            あなたが優しく断ることで、相手との信頼が崩れることはありません。その「安全確認」を少しずつ積み重ねていくことが、今のあなたを楽にする鍵です。
            """
            reports.append({"title": title, "analysis": analysis, "action": action})
        
        # パターン2: 完全受け身タイプ (YESもNOも言えない)
        else:
            title = "🍃 自分らしさの迷子と、高い順応力"
            analysis = """
            相手の意見を尊重し、柔軟に合わせることができる協調性の高さがうかがえます。ただ、その適応能力の高さゆえに、いつの間にか「自分自身の輪郭」が少しぼやけてしまっているかもしれません。
            「どうせ聞いてもらえない」という諦めが隠れているか、あるいは「相手に合わせたほうが楽だ」と、自分の欲求を後回しにする癖がついている可能性もあります。
            あなたが思っている以上に、あなたの本当の気持ちは、この関係にとって大切な羅針盤です。
            """
            action = """
            パートナーシップのことよりも、まずは「自分自身」と対話する時間を作ってみませんか？
            相手がいないひとりの時間に、自分が何を食べたいか、本当はどうしたいかを問いかけ、それを実行してみる。
            そんな「自分を取り戻す小さな冒険」が、結果として二人の関係に新しい風を吹き込むはずです。
            """
            reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析2: 「受信力」と「安全基地」 (Q3, Q4, Q5)
    # ---------------------------------------------------------
    receptivity_score = q3 + q4 + q5
    if receptivity_score <= 12: 
        title = "📡 『受信モード』の休息と再調整"
        analysis = """
        日々の忙しさや責任感から、少し心に余裕がなくなっている時期かもしれません。
        相手の信号を受け取るアンテナの感度が、一時的に弱まっている可能性があります。もしかすると、あなたの疲れが知らず知らずのうちに「今は話しかけないで」という雰囲気として伝わってしまっていることも考えられます。
        悪気はなくても、パートナーが「今は何を言っても届かないかも」と少し寂しさを感じているサインを見落としているかもしれません。
        """
        action = """
        「聞く」ことのハードルを少し下げてみませんか？ 解決策や立派なアドバイスは必要ありません。
        ただ相手の目を見て、相手が話し終わるまで静かに頷く。そして「そうだったんだね」と繰り返す。
        そんな「能動的な沈黙」の時間を数分作るだけで、相手の安心感は大きく変わるはずです。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析3: Doing(貢献) vs Being(共有) のバランス (Q7, Q8)
    # ---------------------------------------------------------
    diff_action = q7 - q8
    
    # パターン4: 尽くしすぎタイプ
    if diff_action >= 3:
        title = "🏃‍♂️ 『頑張り屋さん』の愛情表現"
        analysis = """
        あなたはとても誠実で、「相手の役に立ちたい」という思いが強い方のようです。
        ただ、もしかすると「何かをしてあげないと、愛される価値がない」という不安が、心のどこかにあるのかもしれません。家事や仕事で貢献することで、自分の居場所を確認しようとしている傾向が見受けられます。
        しかし、あなたが頑張れば頑張るほど、パートナーは逆に「自分は信頼されていないのかな」「ただの同居人みたいだ」と、役割のなさを感じてしまう皮肉なすれ違いが起きている可能性があります。
        """
        action = """
        今のあなたに最も必要な戦略は、勇気を出して**「何もしない」**ことかもしれません。
        今週末は、生産的な活動を少しお休みしてみませんか？ 家事も手抜きをして、ただソファで二人でダラダラする。
        そんな「無駄な時間」を共有しても大丈夫だと感じられた時、本当の意味での安心感が二人の間に生まれるはずです。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})
    
    # パターン5: 甘え/依存タイプ
    elif diff_action <= -3:
        title = "🛋️ 『安心感』と『頼りがい』のバランス"
        analysis = """
        パートナーと一緒にいる空間が、あなたにとって非常に居心地の良いものになっていることが分かります。相手を深く信頼している証拠です。
        ただ、その安心感に身を委ねるあまり、相手への能動的な働きかけが少し控えめになっているかもしれません。「言わなくても分かってくれるだろう」という甘えが、知らず知らずのうちに相手の負担感を強めている可能性もあります。
        今のこの快適さは、パートナーの静かな頑張りや配慮の上に成り立っているものかもしれません。
        """
        action = """
        相手が普段何気なくやってくれている「名もなき気遣い」を探してみませんか？
        そして、頼まれる前に一つだけ、自分から動いてみる。「ありがとう」とお茶を淹れるだけでも十分です。あなたの主体的な優しさが、相手の孤独感をふっと癒やす瞬間になるはずです。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析4: スキンシップと親密性 (Q6 focus)
    # ---------------------------------------------------------
    # パターン6: レス傾向・同居人化
    if g_q6 in ["Danger", "Warning"] and g_q8 in ["Good", "Master"]:
        title = "🤝 『信頼あるパートナー』から『恋人』へ"
        analysis = """
        「一緒にいて楽」だし「信頼もしている」。とても安定した関係が築けています。
        一方で、そこに「肌の触れ合い」や「ときめき」の要素が少し置き去りになっている傾向があるかもしれません。精神的なつながりは強いものの、男女としての本能的な距離が、少しずつ開いてしまっている可能性があります。
        これは仲の良いカップルにもよくあることですが、意識的にケアしないと、関係が少しドライになりすぎてしまうサインかもしれません。
        """
        action = """
        いきなり濃厚な接触を目指す必要はありません。「情報のやり取り」ではない、温かみのあるタッチを増やしてみませんか？
        出かける前のハイタッチや、隣に座った時に肩が触れ合う距離感など。
        言葉を介さないコミュニケーションが、理屈ではない「大切にされている感覚」を呼び覚ますきっかけになります。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # ---------------------------------------------------------
    # 分析5: 理想的な状態へのネクストステップ (Overall Good)
    # ---------------------------------------------------------
    avg_score = (q1+q2+q3+q4+q5+q6+q7+q8) / 8
    
    # パターン7: 成熟した関係
    if avg_score >= 7 and len(reports) == 0:
        title = "👑 『成熟した関係』の、その先へ"
        analysis = """
        おめでとうございます。あなたのパートナーシップは、お互いが自立しつつ、健全に頼り合えている、非常にバランスの良い状態にあるようです。
        多くの人が目指す理想的な関係性が築けています。大きな問題がない今だからこそ、守りに入るのではなく、二人の未来をさらに楽しく「創造」できるフェーズに入っていると言えます。
        """
        action = """
        日常のメンテナンスは十分できています。次は「非日常」のビジョンを共有してみませんか？
        「3年後、二人でどんな景色を見ていたいか？」「どんな人生なら最高か？」
        トラブル解決のためではなく、夢を語るための作戦会議をセットしてみてください。それが二人の絆を、より強固なものにします。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    # フォールバック (どのパターンにも当てはまらない場合)
    if len(reports) == 0:
        title = "⚖️ 『凪（なぎ）』の状態と、変化の予感"
        analysis = """
        極端に悪いところもなければ、飛び抜けて良いところもない。今の二人は、ある意味でとても「安定」しています。
        ただ、パートナーシップにおいて「現状維持」は、時として「関心の低下」につながることがあります。
        大きな不満がないからこそ、情熱が落ち着き、日々の会話が業務連絡中心になりやすい時期でもあります。これは、関係を次のステージに進めるためのサインかもしれません。
        """
        action = """
        「8つの項目」の中で、一番点数が低かった項目を一つだけピックアップしてみてください。
        今週は、その「たった一つの項目」だけを意識して、10％だけ工夫してみるゲームをしてみませんか？
        全体を変える必要はありません。一点突破の小さな変化が、二人の空気を新鮮にするきっかけになるはずです。
        """
        reports.append({"title": title, "analysis": analysis, "action": action})

    return reports

# --- 結果表示UI ---
if submitted:
    st.divider()
    
    # チャートとスコア
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
        
        st.markdown("#### 💎 Relationship Assets")
        if q3 >= 8: st.markdown('<div class="asset-card">👂 卓越した「傾聴力」があります</div>', unsafe_allow_html=True)
        if q5 >= 8: st.markdown('<div class="asset-card">🏠 最高の「安全基地」を作れています</div>', unsafe_allow_html=True)
        if q2 >= 8: st.markdown('<div class="asset-card">🛡️ 健全な「境界線」を持っています</div>', unsafe_allow_html=True)
        if total_score <= 40: st.markdown('<div class="asset-card">🌱 これから「伸びていく」関係です</div>', unsafe_allow_html=True)

    # 深層レポート
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