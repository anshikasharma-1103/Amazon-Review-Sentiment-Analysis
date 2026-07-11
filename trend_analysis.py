import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

DATASET = "dataset/AMAZON_FASHION_5_part0.csv"

def show_trends():

    df = pd.read_csv(DATASET)

    # Remove empty reviews
    df = df.dropna(subset=["reviewText"])

    # Create Sentiment using star ratings
    sentiments = []

    for rating in df["overall"]:

        if rating >= 4:
            sentiments.append("Positive")

        elif rating == 3:
            sentiments.append("Neutral")

        else:
            sentiments.append("Negative")

    df["Sentiment"] = sentiments

    counts = df["Sentiment"].value_counts()

    total = len(df)

    print("\n========== AMAZON TREND ANALYSIS ==========\n")

    print("Total Reviews :", total)

    print()

    for sentiment, count in counts.items():

        percent = (count / total) * 100

        print(f"{sentiment} : {count} ({percent:.2f}%)")

    # -----------------------
    # TOP TRENDING WORDS
    # -----------------------

    text = " ".join(df["reviewText"].astype(str))

    words = re.findall(r"[A-Za-z]+", text.lower())

    stopwords = {
        "the","is","was","are","am","this","that","with",
        "have","has","had","you","your","they","them",
        "very","for","and","but","not","its","from","all",
        "can","will","would","could","there","their"
    }

    words = [w for w in words if w not in stopwords and len(w)>2]

    common = Counter(words).most_common(10)

    print("\nTop Trending Words\n")

    for word,count in common:

        print(word,"-",count)

    # -----------------------
    # BAR GRAPH + REPORT
    # -----------------------

    fig = plt.figure(figsize=(14,7))

    # Bar Graph
    ax1 = plt.subplot(1,2,1)

    colors = ["green","orange","red"]

    ax1.bar(
    counts.index,
    counts.values,
    color=colors
    )

    ax1.set_title("Amazon Review Sentiment Trend",fontsize=16,fontweight="bold")
    ax1.set_xlabel("Sentiment")
    ax1.set_ylabel("Number of Reviews")

    # -----------------------
    # REPORT PANEL
    # -----------------------

    ax2 = plt.subplot(1,2,2)

    ax2.axis("off")

    report = f"""

    📊 AMAZON TREND ANALYSIS

    ━━━━━━━━━━━━━━━━━━━━━━

    Total Reviews : {total}

    😊 Positive : {counts.get('Positive',0)}

    😐 Neutral : {counts.get('Neutral',0)}

    😞 Negative : {counts.get('Negative',0)}

     ━━━━━━━━━━━━━━━━━━━━━━

    Positive : {(counts.get('Positive',0)/total)*100:.2f}%

    Neutral : {(counts.get('Neutral',0)/total)*100:.2f}%

    Negative : {(counts.get('Negative',0)/total)*100:.2f}%

    ━━━━━━━━━━━━━━━━━━━━━━

    🔥 Top Trending Words

    """

    for word,count in common:

       report += f"\n• {word} : {count}"

    ax2.text(
    0,
    1,
    report,
    fontsize=12,
    va="top",
    family="monospace"
    )

    plt.tight_layout()

    plt.show()

if __name__=="__main__":

    show_trends()