import feedparser
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# RSS feed for AI news (you can change sources here)
FEED_URLS = [
    "https://news.google.com/rss/search?q=artificial+intelligence&hl=en-IN&gl=IN&ceid=IN:en",
    "https://www.analyticsinsight.net/category/artificial-intelligence/feed/",
    "https://venturebeat.com/category/ai/feed/"
]

RECIPIENTS = ["siegerintern@gmail.com", "kavyaraj922@gmail.com"]
SENDER_EMAIL = "your_email@gmail.com"  # Use your Gmail
APP_PASSWORD = "your_app_password"     # Create this in Step 4

def get_news():
    items = []
    for url in FEED_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # top 3 articles per feed
            items.append(f"<b>{entry.title}</b><br><a href='{entry.link}'>{entry.link}</a><br><br>")
    return items

def send_email(news_html):
    msg = MIMEText(news_html, "html")
    msg['Subject'] = f"The AI Times – {datetime.now().strftime('%d %b %Y')}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECIPIENTS)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())

if __name__ == "__main__":
    news_list = get_news()
    if news_list:
        html_content = f"<h2>🧠 The AI Times – {datetime.now().strftime('%d %b %Y')}</h2><br>" + "".join(news_list)
        send_email(html_content)
