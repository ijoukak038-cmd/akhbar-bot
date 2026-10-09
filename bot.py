import feedparser
import random
from datetime import datetime

print("✅ البوت بدا خدام...")

# كيجيب الأخبار من هسبريس RSS
feed = feedparser.parse("https://www.hespress.com/feed")

if feed.entries:
    # ناخد 1 خبر عشوائي
    entry = random.choice(feed.entries[:10])
    title = entry.title
    link = entry.link
    summary = entry.summary if hasattr(entry, 'summary') else ""

    print(f"📰 لقينا خبر: {title}")
    print(f"🔗 {link}")
    
    # هنا غادي نزيد كود النشر لبلوجر من بعد
    # دابا غير كنجربو واش كيخدم

else:
    print("❌ ما لقيناش أخبار")

print(f"⏰ الوقت: {datetime.now()}")
