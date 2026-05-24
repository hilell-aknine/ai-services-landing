# CLAUDE.md — AI Services Landing (העסק האישי של הילל)

## Project Overview
- **Name:** AI Services Landing — דף נחיתה לשירותי AI של הילל
- **Stack:** HTML5 + Tailwind CDN + Motion (motion.dev) + Canvas scroll-frame hero
- **Assets:** FAL Flux/Kling-generated (hero, 3 cards, 80 frames)
- **Path:** `C:\Users\saraa\OneDrive\שולחן העבודה\לקוחות\דברים לעסק שלי`
- **Repo:** `hilell-aknine/ai-services-landing`
- **Live URLs:**
  - Vercel (primary): https://ai-services-landing.vercel.app/
  - GitHub Pages (mirror): https://hilell-aknine.github.io/ai-services-landing/
- **Purpose:** לגייס 2-3 לקוחות איכותיים לשירותי פיתוח AI של הילל

## Startup Protocol
> בתחילת כל סשן:
1. קרא `primer.md` למצב הנוכחי
2. רוץ `git log --oneline -10`
3. רוץ `git diff --stat`
4. קרא `hindsight.md` ללקחים מהעבר

## Architecture (קצר)
- **Hero**: section בגובה 180vh/260vh עם sticky canvas. גלילה = dolly-in דרך 80 פריימים (Kling 2.0 → ffmpeg, ~3.7MB).
- **3 כרטיסי שירות**: כל אחד עם תמונת FAL Flux + תוכן.
- **Recent Work**: 3 כרטיסי proof (מילואים / משפיע מקבלנים / סדנאות AI).
- **טופס**: שולח wa.me ל-Hillel (972549116092) עם הודעה פשוטה.
- **Demo bot CTA**: כפתורים שמובילים ל-wa.me ל-972512940781 (בית המטפלים) עם המילה "דמו" — מפעיל את demo handler ב-crm-bot.

## Connected systems
- **Bot:** `crm-bot/src/handlers/demo.js` (פרוס ב-Fly.io as `crm-bot-hillel`). מסלול דמו עוקף את ה-auth של ה-CRM.
- **Supabase:** טבלאות `demo_sessions` ו-`demo_handoffs` (פרוייקט `eimcudmlfjlyxjyrdcgc`, משותף עם בית המטפלים).
- **Groq:** LLaMA 3.3 70B מנהל את השיחה לפי כללי Gemini.

## Rules
- עדכן את `primer.md` אחרי כל משימה משמעותית
- כל באג / החלטה לא ברורה → הוסף ל-`hindsight.md`
- אל תיגע ב-CRM bot's production flow — רק במסלול הדמו (`src/handlers/demo.js`)
- כל push ל-main → אוטומטית מפרס ל-Vercel + GH Pages
- שמור את `assets/hero-dolly.mp4` מקומית (לא בריפו) — הפריימים מספיקים

## Common commands
```bash
# פיתוח מקומי (אין build step)
python -m http.server 8000   # אז http://localhost:8000

# פריסה
git push                      # אוטומטית ל-Vercel + GH Pages

# QA מובייל
python mobile_full_qa.py     # 4 מכשירים, overflow, touch targets, iOS zoom

# יצירת תמונות
python generate_images.py    # 4 תמונות FAL
python generate_video.py     # וידאו Kling דולי
python generate_og.py        # OG share image

# בוט (פרויקט נפרד)
cd ../../../crm-bot && fly.exe deploy
```

## Files NOT in repo (kept locally)
- `assets/hero-dolly.mp4` (9.5MB — המקור של הפריימים)
- `assets/manifest.json`
- `qa/` (~30 צילומי בדיקה)
- כל `generate_*.py` ו-`mobile_*.py` (סקריפטים פנימיים)
