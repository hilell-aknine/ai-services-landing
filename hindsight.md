# Hindsight — לקחים שנלמדו

> כל באג, כל החלטה לא ברורה, כל "אה, הייתי צריך להבין מראש" — הולך לכאן.
> פורמט: תאריך · מה קרה · למה זה קרה · איך לא לחזור על זה.

## 2026-05-24

### `\b` ב-regex של JS לא עובד לעברית
- **מה קרה:** Demo bot לא נכנס למצב דמו על "דמו". ה-regex היה `/^\s*(דמו|demo)\b/i`.
- **למה:** ב-JavaScript regex, `\w` = `[A-Za-z0-9_]`. אותיות עבריות (י, ו, ת...) הן NOT word chars. `\b` בוחן מעבר בין word ל-non-word — כש"ו" היא non-word וגם end-of-string היא non-word → אין boundary → אין מאצ'.
- **לא לחזור:** במקום `\b` להשתמש ב-`(\s|$)` או lookahead אחר. תמיד לבדוק regex עם node לפני שמפרסים.

### Green API שולח webhook פעמיים לאותה הודעה
- **מה קרה:** הבוט שלח כל תשובה פעמיים.
- **למה:** Green API לפעמים מספק את אותו webhook כפול. אין דרך לכבות את זה.
- **לא לחזור:** dedup בזיכרון לפי `data.idMessage` עם TTL 30 שניות. כל handler ציבורי צריך את זה.

### Supabase db push חסום בגלל גרסת migration כפולה
- **מה קרה:** `npx supabase db push` נכשל על קונפליקט גרסה ישן (`20260520120000_referral_leaderboard_exclude_staff.sql`).
- **למה:** ב-beit-vmetaplim יש 2 מיגרציות עם אותו timestamp prefix. אחת הוחלה ברימוט, השנייה לא, וזה חוסם את כל ה-push.
- **לא לחזור:**
  - דרך A: לזמן הריצה — `mv` של הקובץ הבעייתי ל-`/tmp`, push, restore.
  - דרך B (אם זה לא עבד): להשתמש ב-Supabase Studio (SQL Editor) להריץ ידנית. 30 שניות.

### PIL לא מטפל ב-RTL — הטקסט יוצא הפוך
- **מה קרה:** OG image עם טקסט "העסק שלך" יצא "ךלש קסעה".
- **למה:** PIL רושם תווים בסדר לוגי (כסדר הקלדה), בלי bidi. עברית צריכה להיכתב מימין לשמאל בתצוגה.
- **לא לחזור:** תמיד `from bidi.algorithm import get_display` ואז `get_display(hebrew_str)` לפני `draw.text()`.

### `arialbd.ttf` כן תומך עברית, `ariblk.ttf` לא תמיד
- **מה קרה:** הכותרת של OG יצאה ריבועים ריקים כשהפונט היה Arial Black.
- **לא לחזור:** לפונט עברי ב-Windows להעדיף `arialbd.ttf` (Arial Bold), `arial.ttf`, `tahoma.ttf`, `david.ttf`. **לא** `ariblk.ttf` או `Heebo-Bold.ttf` אם לא מותקן.

### Vercel deploy מאחר ב-1-2 דקות אחרי push
- **מה קרה:** עליתי commit עם og.jpg + meta tags, אבל curl על ה-URL החזיר 404 + HTML ישן ל-2 דקות.
- **למה:** Vercel build pipeline לוקח זמן. גם ה-CDN cache לוקח רגע להתפזר.
- **לא לחזור:** לא להבהל. לחכות 2 דקות. אם אחרי 3 דקות עדיין לא — לבדוק Vercel dashboard לראות אם ה-build נכשל.

### .vercelignore לא חובה כאן (האתר סטטי) — אבל...
- **מה קרה:** הסקריפטים `*.py`, `qa/`, ו-`hero-dolly.mp4` נכנסו לריפו דרך הירושה הראשונית (לפני שעשיתי `.gitignore`).
- **לא לחזור:** ליצור `.gitignore` תקין **לפני** הוא commit הראשון, לא אחריו.

### בוט שעובד עם שיחה רב-תורית צריך multi-turn chat, לא askQuestion
- **מה קרה:** `groq.askQuestion(question)` הוא single-turn. הצורך לזכור היסטוריית שיחה דרש פונקציה חדשה.
- **לא לחזור:** מה-יום הראשון, כשבונים אינטגרציית AI לבוט, להגדיר שני exports: `askQuestion` (חד-פעמי) ו-`chat(messages, opts)` (רב-תורי).

### Handoff signal דורש פורמט ברור ב-prompt
- **מה קרה:** במקום `[HANDOFF]` בודד, Groq לפעמים כתב "אעביר להילל את הפרטים שלך כעת [HANDOFF]" באמצע משפט — מה שיוצר רעש בהודעה ששודרה.
- **לא לחזור:** ב-system prompt לציין במפורש: "הסימן [HANDOFF] תמיד בשורה נפרדת בסוף ההודעה". להוסיף דוגמה.
