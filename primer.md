# Primer — Current State (2026-05-24)

## ⚡ Quick status
- **חי באוויר**: https://ai-services-landing.vercel.app/ (Vercel ראשי) + https://hilell-aknine.github.io/ai-services-landing/ (GH Pages מראה)
- **בוט WhatsApp דמו**: פעיל ב-972512940781 — שלח "דמו" מכל מספר זר → זרימת qualification מנוהלת Groq
- **הליד הראשון**: עדיין לא הגיע. ממתין לבדיקה אמיתית של זרים.

## Recent changes (latest first)
| תאריך | מה נעשה | סטטוס |
|---|---|---|
| 2026-05-24 18:30 | OG image (1200×630) + meta tags + vercel.json עם cache headers | ✅ פרוס |
| 2026-05-24 17:00 | רפקטור demo bot לזרימת Gemini (שיחה חופשית עם handoff) | ✅ פרוס |
| 2026-05-24 16:30 | Supabase: עמודת `history` ל-`demo_sessions` + טבלת `demo_handoffs` | ✅ הוחל |
| 2026-05-24 15:00 | חיבור Vercel — domain ai-services-landing.vercel.app | ✅ |
| 2026-05-24 14:00 | כפתור "נסה את הבוט שלי" בכרטיס Personal AI | ✅ |
| 2026-05-24 13:30 | הודעת WhatsApp בטופס: מ-form dump לטון אישי "היי, זה X" | ✅ |
| 2026-05-24 13:00 | Demo bot v1: 3-option menu + CRM mock + Q&A | replaced by v2 |
| 2026-05-24 12:00 | רפקטור קופי — סולק כל הז'רגון (Supabase, CRM, RLS, Edge Functions) | ✅ |
| 2026-05-24 11:00 | Hero canvas scroll-frame (80 פריימים Kling 2.0) | ✅ |
| 2026-05-24 10:30 | תמונות FAL Flux: hero + 3 כרטיסי שירות | ✅ |
| 2026-05-24 10:00 | יצירה ראשונה של הדף — Hero + שירותים + Guarantee + Process + Form | ✅ |

## Known issues
- `mobile_check.py` עד `mobile_check3.py` — סקריפטים ישנים, אפשר למחוק אם רוצים ניקיון (לא ב-repo).
- Vercel deploy של ה-OG image עדיין ב-propagation (404 ב-15:22 UTC, אמור לעלות תוך 1-2 דקות).
- בית המטפלים = שם הפרופיל ב-WhatsApp של הבוט. מבקרים יראו את זה. אופציות: לשנות פרופיל / להוסיף הסבר בפתיח / קו נפרד.

## Open questions for next session
- האם להוסיף Google Analytics?
- האם לחבר דומיין מותאם אישית? (`hilell-aknine.io` או דומה?)
- האם להוסיף QR code לחיבור מהיר במחשב?
- האם לפרסם ב-LinkedIn / קהילות AI?

## Environment
- Node 20 (לא נדרש לאתר עצמו)
- Python 3.13 + Pillow + python-bidi + playwright + fal-client (לסקריפטים בלבד)
- ffmpeg 8.x (לחיתוך פריימים)
- gh CLI + fly CLI + supabase CLI (פרוסים)

## Secrets
- `FAL_KEY` ב-`C:\Users\saraa\.secrets\creative-board.env`
- `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` ב-`crm-bot/.env`
- Fly access token ב-`C:\Users\saraa\.fly\config.yml`
