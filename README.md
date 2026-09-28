# Suresh Shahi — Premium Django Portfolio

This revision follows the selected **Developer × Explorer** concept more closely and uses `static/images/travel/hero-mardi.jpg` as the hero image.

## Fresh setup

```bash
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py seed_portfolio
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and Admin at `http://127.0.0.1:8000/admin/`.

## If upgrading your existing portfolio

Copy the new files over your current project, then run:

```bash
python manage.py makemigrations portfolio
python manage.py migrate
python manage.py runserver
```

Do **not** run `seed_portfolio` on a site where you already entered custom content: it resets the starter portfolio records.

## Adventure + Instagram workflow

In **Admin → Adventures → Add/Change Adventure**:

1. Upload a cover photo.
2. Add the location, summary and your personal journey in **Story**.
3. Paste the URL of the *specific* Instagram post/reel for that trip into **Instagram post URL** (for example a `/p/.../` or `/reel/.../` URL).
4. Add extra photos using the **Adventure photos** inline at the bottom.
5. Save.

The homepage adventure card opens a dedicated travel detail page containing the story, photo gallery and Instagram embed. Instagram controls the embed itself, so a public/embeddable post is required. If a post cannot be embedded, the page still provides the Instagram fallback link.

## Hero image

The requested photo is included as:

`static/images/travel/hero-mardi.jpg`

Replace that file later if you want to change the hero while keeping the same design.

## Tech Stack

The Tech Stack is intentionally compact and sits directly between Featured Projects and My Journey. Skills remain editable from Django Admin.

## Design refresh (this revision)

The site had two real problems and one polish pass was done on top:

1. **Projects / Adventures / Posts pages were crashing.** All three list templates shared one line — `{{ item.get_category_display|default:item.location }}` — which throws for `Project` objects (no `location` field). Any visit to `/projects/`, `/adventures/` or `/posts/` triggered a server error. Each page has been rebuilt with its own correct template.
2. **The project card buttons/tags on the homepage could visually break out of the card** (the CivicEye card in the screenshot). Fixed by making tags and action buttons wrap as whole units (`white-space:nowrap` + `flex-wrap`) instead of squeezing/clipping, and by capping the visible tech tags to 3.
3. **Premium pass:** a navy + brass ("developer × explorer") token system, refined shadows/typography, a proper header band + detail layout for every inner page (previously plain, generic `<div class="simple-card">` grids), a scroll progress bar, active nav-link highlighting, a back-to-top button, a one-time orchestrated hero entrance animation, and restrained scroll/hover motion throughout (staggered card reveals, magnetic buttons, image zoom on hover). Motion respects `prefers-reduced-motion`.

Run `python manage.py makemigrations portfolio && python manage.py migrate && python manage.py seed_portfolio` on a fresh clone to see it with sample content.
