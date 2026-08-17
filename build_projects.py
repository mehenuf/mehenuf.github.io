#!/usr/bin/env python3
"""Render the five project case-study pages from one shared shell."""
import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects")
os.makedirs(OUT, exist_ok=True)

MAILTO = ("mailto:mehenuf@gmail.com?subject=R%C3%A9sum%C3%A9%20request%20%E2%80%94%20portfolio"
          "&body=Hi%20Mehenuf%2C%0A%0AI%20came%20across%20your%20portfolio%20and%20would%20like%20a%20copy%20"
          "of%20your%20CV%2Fr%C3%A9sum%C3%A9.%0A%0AName%3A%0ACompany%2Forganisation%3A%0ARole%20or%20context%3A%0A%0AThanks%2C")

GH_ICON = ('<svg viewBox="0 0 24 24"><path fill="currentColor" d="M12 2C6.48 2 2 6.58 2 12.26c0 4.54 2.87 8.39 6.84 '
           '9.75.5.1.68-.22.68-.5 0-.24-.01-1.05-.01-1.9-2.78.62-3.37-1.19-3.37-1.19-.46-1.2-1.11-1.53-1.11-1.53-.91-.64.07-.63.07-.63 '
           '1 .07 1.53 1.05 1.53 1.05.89 1.56 2.34 1.11 2.91.85.09-.66.35-1.11.63-1.36-2.22-.26-4.56-1.14-4.56-5.06 '
           '0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.31.1-2.73 0 0 .84-.27 2.75 1.05a9.3 9.3 0 0 1 5 0c1.91-1.32 '
           '2.75-1.05 2.75-1.05.55 1.42.2 2.47.1 2.73.64.72 1.03 1.63 1.03 2.75 0 3.93-2.35 4.79-4.58 5.05.36.32.68.94.68 '
           '1.9 0 1.37-.01 2.47-.01 2.81 0 .28.18.61.69.5A10.03 10.03 0 0 0 22 12.26C22 6.58 17.52 2 12 2Z"/></svg>')
ARROW_R = ('<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" '
           'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW_L = ('<svg viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6" fill="none" stroke="currentColor" '
           'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
EXT = ('<svg viewBox="0 0 24 24"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" '
       'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
DL = ('<svg viewBox="0 0 24 24"><path d="M12 3v11m0 0-4-4m4 4 4-4M5 20h14" fill="none" stroke="currentColor" '
      'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Md. Mehenuf Hossain Bhuiyan</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F5F6F8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0C0E15" media="(prefers-color-scheme: dark)">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%2312141C'/%3E%3Ctext x='16' y='22' font-family='monospace' font-size='15' fill='%23fff' text-anchor='middle'%3EM%3C/text%3E%3C/svg%3E">
<script>
(function(){{
  var d=document.documentElement; d.classList.add('js');
  var s=null; try{{ s=localStorage.getItem('theme'); }}catch(e){{}}
  var p=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches;
  d.setAttribute('data-theme', s||(p?'dark':'light'));
}})();
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css?v=2">
</head>
<body>

<header class="nav">
  <div class="nav-inner">
    <a href="../index.html#top" class="brand"><span class="mark"><span>M</span></span> Mehenuf</a>
    <nav class="nav-links" aria-label="Main">
      <a href="../index.html#about">About</a>
      <a href="../index.html#timeline">Timeline</a>
      <a href="../index.html#research">Research</a>
      <a href="../index.html#skills">Skills</a>
      <a href="../index.html#work">Projects</a>
      <a href="../index.html#contact">Contact</a>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-ghost btn-sm" href="{mailto}">{dl}Request résumé</a>
      <button class="icon-btn theme-toggle" aria-label="Switch to dark theme">
        <svg class="i-sun" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <svg class="i-moon" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
      </button>
      <button class="icon-btn nav-toggle" aria-label="Toggle menu" aria-expanded="false">
        <svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</header>

<main>
  <section class="p-hero">
    <div class="wrap">
      <a class="p-back reveal" href="../index.html#work">{arrow_l}Back to projects</a>
      <div class="kicker reveal">{eyebrow}</div>
      <h1 class="reveal">{headline}</h1>
      <p class="sub reveal">{sub}</p>
      <div class="p-tags reveal">{tags}</div>
      <div class="p-cta-row reveal">
        {primary_cta}
        {extra_cta}
      </div>
      <div class="facts" data-stagger style="margin-top:44px;">{facts}</div>
    </div>
  </section>

{body}

  <section class="p-section">
    <div class="wrap">
      <div class="reveal">
        <div class="kicker">Built with</div>
        <div class="chip-row">{stack}</div>
      </div>
      <div class="p-nav">
        <a href="{prev_href}">{arrow_l}{prev_label}</a>
        <a href="../index.html#work">All projects</a>
        <a href="{next_href}">{next_label}{arrow_r}</a>
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="wrap footer-inner">
    <span class="foot-note">© <span data-year></span> Md. Mehenuf Hossain Bhuiyan</span>
    <div class="footer-links">
      <a href="https://github.com/mehenuf" target="_blank" rel="noopener">GitHub</a>
      <a href="https://www.linkedin.com/in/mehenuf" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://scholar.google.com/citations?user=QUsIy4QAAAAJ&hl=en" target="_blank" rel="noopener">Scholar</a>
      <a href="mailto:mehenuf@gmail.com">Email</a>
    </div>
  </div>
</footer>

<script src="../assets/js/main.js?v=2"></script>
</body>
</html>
"""


def github_cta(repo_url):
    return f'<a class="btn btn-primary" href="{repo_url}" target="_blank" rel="noopener">{GH_ICON}View source on GitHub</a>'


AUTOMATION_MAILTO = (
    "mailto:mehenuf@gmail.com?subject=Patient%20Care%20OS%20%E2%80%94%20full%20report%20request"
    "&body=Hi%20Mehenuf%2C%0A%0AI%27d%20like%20to%20see%20the%20full%20write-up%20for%20the%20"
    "Patient%20Care%20Operating%20System%20project%20%E2%80%94%20the%20ClickUp%20build%20guide%2C%20"
    "n8n%20automation%20guide%2C%20and%2For%20a%20walkthrough.%0A%0AThanks%2C"
)


def facts(rows):
    return "".join(
        f'<div class="fact"><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in rows
    )


def tags(items):
    return "".join(f"<span>{t}</span>" for t in items)


def chips(items):
    return "".join(f'<span class="chip">{t}</span>' for t in items)


def section(kicker, h2, lede="", inner=""):
    lede_html = f'<p class="p-lede">{lede}</p>' if lede else ""
    return f"""  <section class="p-section">
    <div class="wrap">
      <div class="reveal">
        <div class="kicker">{kicker}</div>
        <h2>{h2}</h2>
        {lede_html}
      </div>
{inner}
    </div>
  </section>
"""


def block(items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'      <div class="p-block reveal"><ul>{lis}</ul></div>\n'


def pipeline(steps):
    out = ['      <div class="pipeline" data-stagger>']
    for i, (h, p) in enumerate(steps, 1):
        out.append(f'        <div class="pipe-step"><span class="pn">{i:02d}</span><h4>{h}</h4><p>{p}</p></div>')
    out.append("      </div>\n")
    return "\n".join(out)


def findings(items):
    out = ['      <div class="finding-grid" data-stagger>']
    for tag, h, p in items:
        out.append(f'        <div class="finding"><span class="tag">{tag}</span><div><h3>{h}</h3><p>{p}</p></div></div>')
    out.append("      </div>\n")
    return "\n".join(out)


def table(headers, rows, caption=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        trs += f"<tr>{tds}</tr>"
    cap = f'      <p class="note">{caption}</p>\n' if caption else ""
    return (f'      <div class="table-scroll reveal"><table class="m-table">'
            f"<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>\n{cap}")


def _dims(src):
    """Intrinsic size, so lazy images reserve their space and never shift layout."""
    from PIL import Image
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), src.replace("../", ""))
    with Image.open(path) as im:
        return im.width, im.height


def gallery(shots, one=False):
    cls = "gallery one" if one else "gallery"
    out = [f'      <div class="{cls}">']
    for src, alt, title, cap in shots:
        w, h = _dims(src)
        out.append(
            f'        <figure class="shot reveal-img" tabindex="0" role="button" aria-label="Enlarge: {html.escape(title)}">'
            f'<img src="{src}" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async">'
            f"<figcaption><b>{title}</b>{cap}</figcaption></figure>"
        )
    out.append("      </div>\n")
    return "\n".join(out)


# =====================================================================
PAGES = {}

# ---------------------------------------------------------------- CIFAR
PAGES["cifar10-classifier.html"] = dict(
    title="CIFAR-10 with SE-ResNet, CutMix & Calibration",
    desc="A custom SE-ResNet trained from scratch on CIFAR-10: 95.48% top-1, CutMix, Focal Loss, and temperature-scaled calibration, deployed as a Gradio app.",
    eyebrow="Personal project · 2026",
    headline="I didn't chase a higher number. I found the four errors the model kept making, and fixed those.",
    sub="A custom SE-ResNet CNN trained from scratch on CIFAR-10 — no pretrained weights. Every change in V2 was aimed at a specific, measured failure in V1.",
    tags=tags(["PyTorch", "SE-ResNet", "CutMix", "Focal Loss", "Temperature Scaling", "Gradio"]),
    primary_cta=github_cta("https://github.com/mehenuf/cifar10-classifier"),
    repo="https://github.com/mehenuf/cifar10-classifier",
    extra_cta='<a class="btn btn-ghost" href="../index.html#contact">Ask me about this</a>',
    facts=facts([
        ("95.48<span class='u'>%</span>", "Top-1 accuracy on 10,000 held-out test images"),
        ("99.83<span class='u'>%</span>", "Top-5 accuracy — 9,983 of 10,000 correct in top five"),
        ("0.9498", "Matthews correlation coefficient / Cohen's kappa"),
        ("−17<span class='u'>%</span>", "Cat↔dog confusion errors, V1 → V2 (120 → 100)"),
    ]),
    stack=chips(["Python", "PyTorch", "torchvision", "NumPy", "scikit-learn", "Gradio", "CUDA"]),
    prev_href="flood-alert-system.html", prev_label="Flood Alert System",
    next_href="patient-care-operating-system.html", next_label="Patient Care Operating System",
    body=(
        section("The problem",
                "Pretrained backbones make CIFAR-10 easy. Training from scratch exposes what the architecture actually learned.",
                "V1 was an ordinary ResNet-style CNN that reached 94.81%. That number looks fine until you open the confusion matrix — 120 of the errors were the model mistaking cats for dogs and dogs for cats. Averaged accuracy was hiding a specific, structural weakness.",
                block([
                    "<b>The model weighted every feature channel equally.</b> Nothing let it amplify whisker-and-pointed-ear channels when it was looking at a cat and suppress them when it wasn't.",
                    "<b>It had only ever seen whole objects.</b> Standard augmentation never showed it a partial view, so an unusual angle or an occlusion pushed it off a cliff.",
                    "<b>Easy examples dominated the gradient.</b> Cross-entropy spent most of its signal confirming images the model already got right, instead of on the ambiguous cat/dog boundary.",
                    "<b>Confidence meant nothing.</b> Raw softmax scores were badly calibrated, so a '95% sure' prediction was not right 95% of the time.",
                ])) +
        section("The approach",
                "Four research-backed changes, each aimed at one of those four failures.",
                "",
                pipeline([
                    ("Squeeze-and-Excitation blocks", "An SE block inside every residual block learns to reweight feature channels per image — the fix for treating all channels equally."),
                    ("CutMix augmentation", "Cuts a patch from one training image into another and mixes labels by area, forcing recognition from partial views."),
                    ("Focal Loss (γ = 2.0)", "A (1−pt)^γ factor down-weights easy examples so capacity goes to the hard boundary cases."),
                    ("Temperature scaling", "One learned scalar recalibrates softmax confidence after training, without touching accuracy."),
                    ("Gradio deployment", "The whole pipeline — preprocessing through calibrated prediction — wrapped for real-time GPU inference."),
                ])) +
        section("Results",
                "Where the gains landed — and where they didn't.",
                "Headline accuracy moved +0.67%. The more interesting story is which classes moved.",
                table(["Metric", "V1 baseline", "V2 improved", "Change"],
                      [["Top-1 accuracy", "<span class='num'>94.81%</span>", "<span class='best'>95.48%</span>", "<span class='num'>+0.67</span>"],
                       ["Top-5 accuracy", "<span class='num'>99.57%</span>", "<span class='best'>99.83%</span>", "<span class='num'>+0.26</span>"],
                       ["Macro F1", "<span class='num'>0.9480</span>", "<span class='best'>0.9548</span>", "<span class='num'>+0.0068</span>"],
                       ["Matthews MCC", "<span class='num'>0.9423</span>", "<span class='best'>0.9498</span>", "<span class='num'>+0.0075</span>"],
                       ["Cat accuracy", "<span class='num'>86.9%</span>", "<span class='best'>89.8%</span>", "<span class='num'>+2.9</span>"],
                       ["Bird accuracy", "<span class='num'>92.3%</span>", "<span class='best'>94.7%</span>", "<span class='num'>+2.4</span>"],
                       ["Truck accuracy", "<span class='num'>97.1%</span>", "<span class='warn'>95.4%</span>", "<span class='num'>−1.7</span>"],
                       ["GPU throughput", "<span class='num'>13,671 img/s</span>", "<span class='num'>13,206 img/s</span>", "<span class='num'>−3% (SE cost)</span>"]],
                      "Truck regressed by design: Focal Loss made the model less willing to commit on genuinely ambiguous vehicle boundaries. The errors went up, the confidence behind them went down.") +
                findings([
                    ("TARGETED", "The biggest gains landed exactly where they were aimed",
                     "Cat +2.9% and bird +2.4% were the two weakest classes in V1. Cat↔dog confusion fell from 120 errors to 100 — a 17% reduction on the pair the whole intervention targeted."),
                    ("CALIBRATION", "Temperature scaling cut expected calibration error by ~38%",
                     "ECE fell from 0.163 to 0.101 on the held-out set. Still short of well-calibrated — the honest read is that it's better, not solved, and a proper validation-split temperature search is the next step."),
                    ("HONEST LIMITS", "Cat is still the weakest class at 89.8%",
                     "Every other class sits at or above 93%. The remaining gap is a genuine limit of 32×32 resolution rather than something another augmentation trick fixes."),
                ])) +
        section("From the repo",
                "Training curves, confusion analysis, and the deployed app.",
                "All generated by the evaluation notebook in the repository. Click any chart to enlarge.",
                gallery([
                    ("../assets/img/cifar/nb_dashboard.jpg", "Final results dashboard showing headline metrics and per-class accuracy",
                     "Results dashboard", "Headline metrics plus per-class accuracy. Cat is visibly the outlier."),
                    ("../assets/img/cifar/nb_training_curves.jpg", "V2 training and validation curves over 200 epochs",
                     "Training curves — V2", "200 epochs with Focal Loss. The jagged train loss is expected: the loss is actively re-weighting hard examples each batch."),
                    ("../assets/img/cifar/nb_confusion_matrix.jpg", "Confusion matrix for the ten CIFAR-10 classes",
                     "Confusion matrix", "The cat/dog block is where nearly all remaining error concentrates."),
                    ("../assets/img/cifar/nb_confusion_pairs.jpg", "Target confusion pairs before and after the V2 changes",
                     "Target confusion pairs", "Cat→dog and dog→cat errors, V1 versus V2. The pair total drops from 120 to 100."),
                    ("../assets/img/cifar/nb_cutmix_examples.jpg", "Examples of CutMix augmentation applied to training images",
                     "CutMix examples", "Original above, augmented below. Labels blend proportionally to patch area."),
                    ("../assets/img/cifar/nb_calibration_comparison.jpg", "Reliability diagram before and after temperature scaling",
                     "Calibration comparison", "Reliability before and after temperature scaling."),
                    ("../assets/img/cifar/nb_per_class_metrics.jpg", "Per-class precision, recall and F1 scores",
                     "Per-class metrics", "Precision, recall, and F1 across all ten classes."),
                    ("../assets/img/cifar/nb_ablation.jpg", "Ablation study isolating the contribution of each change",
                     "Ablation study", "Isolating what each of the four changes actually contributed."),
                ]) +
                gallery([
                    ("../assets/img/cifar/app_prediction.jpg", "The Gradio web app returning a calibrated prediction",
                     "Gradio app — prediction", "Real-time inference with calibrated class probabilities."),
                    ("../assets/img/cifar/app_empty.jpg", "The Gradio web app in its empty state",
                     "Gradio app — empty state", "The upload interface before a prediction is run."),
                ]))
    ),
)

# ------------------------------------------------------- PATIENT CARE OS
PAGES["patient-care-operating-system.html"] = dict(
    title="Patient Care Operating System — ClickUp + n8n Automation",
    desc="A ClickUp workspace and 7 self-hosted n8n workflows built for an Operations & AI Automation Specialist assessment — engineered around a 60-use field budget and a 5-automation ceiling.",
    eyebrow="Take-home technical assessment · Operations & AI Automation Specialist role",
    headline="Three numbers in the brief didn't add up. I found them before I built anything.",
    sub="A ClickUp workspace and seven self-hosted n8n workflows for a fictional 12-room assisted-living facility, engineered around a 60-use lifetime custom-field budget and a 5-automation ceiling on the free tier.",
    tags=tags(["ClickUp", "n8n", "Workflow Automation", "Process Design", "REST APIs"]),
    primary_cta=f'<a class="btn btn-primary" href="{AUTOMATION_MAILTO}">{DL}Request the full report</a>',
    extra_cta='<a class="btn btn-ghost" href="../index.html#contact">Ask me about this</a>',
    facts=facts([
        ("≈$99K<span class='u'>/yr</span>", "Forgone revenue found in a 3-bed staffing ceiling"),
        ("32<span class='u'>/60</span>", "Custom-field budget spent — everything else moved to free objects"),
        ("7", "Self-hosted n8n workflows, built and live-tested against the real workspace"),
        ("0", "Duplicate notifications across repeated runs — idempotent by design"),
    ]),
    stack=chips(["ClickUp API", "n8n", "JavaScript (Code nodes)", "REST APIs", "Google Sheets API", "Process Automation", "Technical Documentation"]),
    prev_href="cifar10-classifier.html", prev_label="CIFAR-10 Classifier",
    next_href="credit-scoring-blockchain.html", next_label="Credit Scoring Protocol",
    body=(
        section("The scenario",
                "A fictional facility. A very real set of constraints.",
                "The brief described a 12-room assisted-living facility running since 2018 — three caregivers, a 1:3 ratio policy, cash-only billing, and a free-tier ClickUp plan expected to hold all of it together.",
                table(["Fact", "Value"],
                      [["Licensed capacity", "12 rooms"],
                       ["Current census", "8 residents"],
                       ["Caregivers", "3, at a 1:3 ratio policy"],
                       ["Caregiver lunch break", "30 min, at noon, for each caregiver"],
                       ["Sales calls", "45/day, 8 min average, 22% stated conversion"],
                       ["Sales shift", "6 hours active"],
                       ["Billing", "$2,000–$3,500/month per bed, cash only"]],
                      "Two deliverables were required: a ClickUp workspace covering task management, medication tracking, a sales CRM, and a relatives directory (Part 1); and an n8n automation sending visit-day weather briefings to relatives (Part 2, the brief's one explicit automation requirement).")) +
        section("What I found",
                "Three problems hiding in the brief's own arithmetic.",
                "Not gaps the brief left open — numbers it stated that quietly contradicted each other.",
                findings([
                    ("STAFFING", "All three caregivers break at the same time",
                     "Noon lunch, taken simultaneously, for thirty minutes — for that window the facility runs 0 staff to 8 residents, a daily breach of its own 1:3 ratio policy."),
                    ("CAPACITY", "Three beds are structurally unsellable — and nobody had noticed",
                     "3 caregivers × 1:3 ratio caps safe census at 9. The facility is licensed for 12. Three beds sit empty for staffing reasons, not demand — about $99,000 a year in forgone revenue."),
                    ("SALES MATH", "The stated conversion rate breaks the business model",
                     "45 calls × 8 minutes is the entire 6-hour shift, leaving no time to log a call or follow up. And a flat 22% dial-to-admit rate would mean roughly 10 new admissions a day into a 12-bed home."),
                ])) +
        section("The build",
                "A 60-use field budget, for the life of the workspace.",
                "ClickUp's free plan doesn't cap custom fields — it caps uses: every value set on every task, counted once, forever. Eight residents on six ordinary fields would spend 80% of that budget on a single list. The design doctrine: a field earns its place only where a machine must read the value; everything else moves onto free, unlimited native objects.",
                pipeline([
                    ("Field-budget doctrine", "Custom fields treated as a non-renewable resource — statuses, tags, checklists, and relationships carry meaning for free instead."),
                    ("Four-Space workspace", "Care Operations, Growth, Family Relations, and Business Office — 12 lists total, built around the doctrine above."),
                    ("5 native automations, spent deliberately", "Each of ClickUp Free's five automation slots assigned to the single highest-value trigger on its list."),
                    ("Free-plan workarounds", "No chart cards, no map view, no webhooks, no automation conditions — each gap engineered around rather than accepted."),
                    ("n8n as the escape hatch", "Self-hosted, unlimited execution — everything conditional, cross-list, scheduled, or chart-based that the free plan structurally cannot do."),
                ])) +
        section("The automation suite",
                "Seven workflows, each covering a gap ClickUp Free cannot close natively.",
                "Every workflow below was built, debugged against real API responses, and executed live against the actual workspace — not simulated.",
                table(["Workflow", "Runs", "What ClickUp Free can't do"],
                      [["W1 — Visit-Day Weather Briefing", "<span class='num'>Daily 06:00</span>", "No task webhooks, no external API calls, no household grouping — the brief's one explicit Part 2 requirement"],
                       ["W2 — Medication Safety Net", "<span class='num'>Every 30 min</span>", "Can trigger on a status change, not evaluate a numeric threshold like '45 minutes late' or '3× in 7 days'"],
                       ["W3 — Sales Command Center", "<span class='num'>Daily 06:15</span>", "No chart cards on Free, and Dashboards cap at 60 lifetime views"],
                       ["W4 — Shift Handover Digest", "<span class='num'>06:45 &amp; 18:45</span>", "One automation is scoped to one List; this aggregates four Lists per caregiver"],
                       ["W5 — Cash &amp; Arrears Control", "<span class='num'>Daily 08:00</span>", "Can't total a column or compare consecutive receipt numbers for gaps"],
                       ["W6 — Capacity-Aware Lead Routing", "<span class='num'>Daily 08:30</span>", "Cross-list comparison — beds vs. leads — against a policy ratio, then branching"],
                       ["W7 — Retention Radar &amp; Hygiene", "<span class='num'>Weekly, Mon 07:30</span>", "No trigger exists for 'this relationship doesn't exist' across two lists"]],
                      "W1's idempotency was verified directly: run twice in immediate succession, the second run processed zero households — zero duplicate emails, proven rather than assumed.")) +
        section("Engineering reality",
                "The bugs are part of the work, not incidental noise.",
                "Real debugging that shaped the final build.",
                findings([
                    ("API", "A GET request disguised as a PUT",
                     "ClickUp's API silently defaulted the HTTP method, returning a 403 from CloudFront with no obvious cause. Fixed by explicitly setting the method on every write-back node — now a standing verification step."),
                    ("DATA FLOW", "One chain, two consumers, a silent overwrite",
                     "A linear node chain let a later step overwrite data an earlier step still needed downstream. Rewired into two parallel branches off the same source node so both consumers get their own copy."),
                    ("FIELD NAMES", "A `400 – Comment is required` error with a comment already in the payload",
                     "The code referenced `$json.commentText`, but the upstream node's real output field was named `comment` — `JSON.stringify` silently drops keys that resolve to `undefined`. Fixed by cross-checking the exact field name in the actual upstream output before writing any downstream expression."),
                    ("SCOPE HONESTY", "The video script ran over the assessment's 10-minute limit",
                     "Flagged plainly rather than hidden, with a prioritized, quantified cut plan — exactly what to shorten and how much time each cut recovers — so the final recording fits the constraint without losing the content that best demonstrates the reasoning."),
                ])) +
        section("Note on assets",
                "This one lives in ClickUp and n8n, not a code repo.",
                "",
                '      <p class="note reveal">The deliverables for this project are a ClickUp workspace, seven live n8n workflows, and a set of written guides rather than a public repository — so there\'s no "View source" link here. Get in touch and I\'m glad to walk through the live workspace, the workflow canvases, or the full written report.</p>\n')
    ),
)

# ------------------------------------------------------------ CREDIT
PAGES["credit-scoring-blockchain.html"] = dict(
    title="Decentralised Credit Scoring — Ensemble + Blockchain Oracle",
    desc="A stacking-ensemble credit risk engine for thin-file borrowers, with every decision committed to Ethereum and its evidence pinned to IPFS. Presented at ICIICE 2026.",
    eyebrow="Senior Design II capstone · Oct – Dec 2025",
    headline="A credit score is only worth something if someone else can check it.",
    sub="A risk engine for thin-file borrowers in emerging markets: alternative mobile-money data, a stacking ensemble, SHAP attributions for every decision, and a Node.js oracle that commits the result on-chain.",
    tags=tags(["XGBoost", "SMOTE", "Optuna", "SHAP", "Solidity", "Ethereum", "IPFS", "Node.js"]),
    primary_cta=github_cta("https://github.com/mehenuf/MFScreditScore-blockchain-oracle-ipfs"),
    repo="https://github.com/mehenuf/MFScreditScore-blockchain-oracle-ipfs",
    extra_cta=('<a class="btn btn-ghost" href="https://www.researchgate.net/publication/407327879_Blockchain_Meets_AI-Powered_Oracles_and_decentralized_storage_A_Secure_and_Scalable_Framework_for_Decentralized_Credit_Scoring" target="_blank" rel="noopener">Read the ICIICE 2026 paper' + EXT + "</a>"),
    facts=facts([
        ("0.984", "AUC — stacking ensemble on the held-out set"),
        ("0.948", "F1 score — ensemble, after SMOTE balancing"),
        ("&gt;99.9<span class='u'>%</span>", "IPFS retrieval rate via sequential gateway fallback"),
        ("ICIICE '26", "Presented and published on IEEE Xplore"),
    ]),
    stack=chips(["Python", "scikit-learn", "XGBoost", "Optuna", "SHAP", "pandas", "Node.js", "Express", "Solidity", "ethers.js", "IPFS", "Pinata"]),
    prev_href="patient-care-operating-system.html", prev_label="Patient Care Operating System",
    next_href="corn-leaf-xai.html", next_label="Corn Leaf XAI",
    body=(
        section("The problem",
                "Thin-file borrowers are invisible to conventional credit scoring — and invisible decisions can't be audited.",
                "Millions of people in emerging markets have years of mobile financial services history and no formal credit file. A model can read that alternative data. The harder question is what stops the lender changing the answer afterwards.",
                block([
                    "<b>Severe class imbalance.</b> Defaults are rare, so a naive model can score 95% accuracy by predicting 'no default' every time and be completely useless.",
                    "<b>Off-chain inference has no witness.</b> A prediction produced in a notebook is trivially editable after the fact — nothing records what the model actually said, or when.",
                    "<b>Regulators don't accept black boxes.</b> An automated decision that affects credit access has to come with a reason, per applicant, not just a global feature-importance chart.",
                    "<b>Blockchains are terrible databases.</b> Storing the applicant's data on-chain is both prohibitively expensive and a privacy violation.",
                ])) +
        section("The approach",
                "Score off-chain where compute is cheap. Commit the receipt on-chain where tampering is expensive.",
                "The architecture splits into four planes so PII never touches the chain and the chain never has to run a model.",
                pipeline([
                    ("SMOTE balancing", "Interpolates between minority-class samples to synthesise a balanced training distribution."),
                    ("Stacking ensemble", "Level-0: XGBoost (tuned with Optuna) and a 64/32 MLP. Level-1: logistic regression aggregates their probabilities."),
                    ("PDO score transform", "Converts probability of default into an industry-standard 300–850 score via points-to-double-the-odds."),
                    ("SHAP + IPFS", "Per-applicant Shapley attributions bundled into a JSON payload and pinned to IPFS, returning a content ID."),
                    ("Oracle → Ethereum", "A Node.js oracle polls the contract for requests, fetches from IPFS, and writes back the score and CID on-chain."),
                ])) +
        section("Results",
                "Model performance, and the engineering decision that came with it.",
                "",
                table(["Model", "AUC", "F1", "Precision", "Training time"],
                      [["Stacking ensemble", "<span class='best'>0.984</span>", "<span class='best'>0.948</span>", "<span class='num'>0.956</span>", "<span class='num'>49.2 s</span>"],
                       ["XGBoost (shipped)", "<span class='num'>0.983</span>", "<span class='num'>0.939</span>", "<span class='best'>0.961</span>", "<span class='best'>1.70 s</span>"],
                       ["Random Forest", "<span class='num'>0.918</span>", "<span class='num'>0.832</span>", "<span class='num'>0.840</span>", "<span class='num'>5.90 s</span>"]],
                      "The ensemble wins on AUC by 0.001 and costs 29× the training time. XGBoost went to production — the accuracy difference was not worth the latency for real-time inference.") +
                findings([
                    ("MODELLING", "A 0.001 AUC gain wasn't worth 29× the compute",
                     "The ensemble is the better model on paper. XGBoost shipped because it trains in 1.70s with a higher precision score, and precision is what matters when a false approval costs real money."),
                    ("EXPLAINABILITY", "Every score carries its own reasons",
                     "SHAP produces local and global attributions per applicant, so the system can state which variables raised or lowered a specific risk profile — not just which features matter on average."),
                    ("RELIABILITY", "The oracle assumes the network will fail",
                     "Sequential gateway fallback (ipfs.io → Cloudflare → Pinata) lifts an 88% first-attempt success rate to over 99.9% overall. Request IDs are deduplicated in memory so a retry never double-spends gas."),
                    ("COST", "The contract stores receipts, not data",
                     "Emitting optimised events instead of writing strings on-chain keeps a request at ~115,000 gas and a fulfilment at ~145,000 — the design constraint that made the whole thing viable."),
                ])) +
        section("From the repo",
                "Model evaluation, tracked in Weights & Biases.",
                "Charts logged during the training runs in the repository. Click to enlarge.",
                gallery([
                    ("../assets/img/credit/roc_pr.jpg", "ROC and precision-recall curves for the credit scoring models",
                     "ROC & precision–recall", "Both curves side by side — precision–recall is the honest one on imbalanced default data."),
                    ("../assets/img/credit/calibration.jpg", "Calibration plot for the credit scoring ensemble",
                     "Calibration plot", "How closely predicted default probability tracks observed default rate."),
                    ("../assets/img/credit/ks_plot.jpg", "Kolmogorov-Smirnov separation plot between good and bad borrowers",
                     "KS separation", "Kolmogorov–Smirnov distance between the good and bad borrower distributions."),
                    ("../assets/img/credit/score_dist.jpg", "Distribution of generated credit scores",
                     "Score distribution", "The 300–850 scores produced by the PDO transform across the population."),
                    ("../assets/img/credit/score_bands.jpg", "Default rate stacked by credit score band",
                     "Score bands", "Default rate by score band — the check that the score is monotonic in risk."),
                    ("../assets/img/credit/dashboard.jpg", "Portfolio-level risk dashboard",
                     "Portfolio dashboard", "Portfolio-level view: approval rates and expected loss across score cut-offs."),
                ]))
    ),
)

# ------------------------------------------------------------- CORN
PAGES["corn-leaf-xai.html"] = dict(
    title="XAI-Driven Multi-Teacher Knowledge Distillation",
    desc="A lesion-aware Inception teacher guided by U-Net masks, distilled into a quantized MobileNetV3 student running in 15.5 ms on CPU, with Grad-CAM verification.",
    eyebrow="Pattern Recognition & Neural Networks · Jun – Aug 2025",
    headline="A 97% model is useless on a phone in a field. So I taught a small one to think like it.",
    sub="A dual-branch, lesion-aware Inception teacher guided by U-Net mask proposals, distilled into a MobileNetV3 student and quantized to INT8 — with Grad-CAM used to confirm it looks at the disease, not the background.",
    tags=tags(["Grad-CAM", "Knowledge Distillation", "U-Net", "MobileNetV3", "DeiT", "QAT / INT8", "PyTorch"]),
    primary_cta=github_cta("https://github.com/mehenuf/corn-leaf-classification"),
    repo="https://github.com/mehenuf/corn-leaf-classification",
    extra_cta='<a class="btn btn-ghost" href="../index.html#contact">Ask me about this</a>',
    facts=facts([
        ("97.12<span class='u'>%</span>", "Teacher accuracy — lesion-aware Inception V3"),
        ("15.5<span class='u'>ms</span>", "Student inference on CPU, 299×299, after INT8 QAT"),
        ("0.966", "Student F1 — statistically level with the teacher's 0.970"),
        ("4 classes", "Common rust, leaf blight, gray spot, healthy"),
    ]),
    stack=chips(["Python", "PyTorch", "torchvision", "scikit-learn", "OpenCV", "ONNX", "Roboflow", "Grad-CAM", "Matplotlib", "Seaborn"]),
    prev_href="credit-scoring-blockchain.html", prev_label="Credit Scoring Protocol",
    next_href="perfume-store-rdbms.html", next_label="Perfume Store RDBMS",
    body=(
        section("The problem",
                "Three requirements that normally trade off against each other.",
                "Corn leaf disease has to be caught early to matter. That means diagnosis happens in a field, on a cheap device, offline — which rules out the models that are accurate enough to trust.",
                block([
                    "<b>Accuracy lives in models too heavy to deploy.</b> Inception V3 and the vision transformers score well and are far too slow for edge inference.",
                    "<b>Background noise is a real failure mode.</b> A model trained on whole photographs can learn soil and lighting instead of pathology, and nobody notices until it meets a new field.",
                    "<b>Compression usually costs the fine-grained cues.</b> Distilling into a mobile-sized student risks losing exactly the lesion detail that made the teacher accurate.",
                    "<b>A confident wrong diagnosis is worse than no diagnosis.</b> A model that can't decline to answer will always answer, including on images it has no business classifying.",
                ])) +
        section("The approach",
                "Force attention onto the lesion first. Compress second. Add an escape hatch last.",
                "",
                pipeline([
                    ("U-Net mask proposals", "A lightweight U-Net proposes lesion masks, supervised jointly with the classifier."),
                    ("Lesion-aware dual branch", "One branch sees the raw image, one sees the mask-attenuated image — forcing focus onto pathology, not background."),
                    ("Multi-teacher ensemble", "The LAIC Inception teacher plus DeiT-Small contribute complementary signal."),
                    ("Distillation into MobileNetV3", "Logit distillation, attention transfer, and GAP feature matching compress the teachers into one student."),
                    ("QAT to INT8 + abstention", "Quantization-aware training for edge latency, then temperature scaling and selective prediction validated with risk–coverage analysis."),
                ])) +
        section("Results",
                "The student kept the teacher's F1 and shed most of its cost.",
                "",
                table(["Model", "Accuracy", "F1", "Note"],
                      [["Inception V3 (LAIC teacher)", "<span class='best'>97.12%</span>", "<span class='best'>0.970</span>", "Baseline FP32, ~40.1 s/epoch"],
                       ["DeiT-Small", "<span class='num'>96.18%</span>", "<span class='num'>0.96</span>", "Best transformer evaluated"],
                       ["ResNet101", "<span class='num'>95.23%</span>", "<span class='num'>0.95</span>", "Conventional CNN reference"],
                       ["ViT", "<span class='num'>93.32%</span>", "<span class='num'>0.93</span>", "Underperforms at this dataset size"],
                       ["Student MobileNetV3 (FP32)", "<span class='best'>97.12%</span>", "<span class='num'>0.966</span>", "18.2 ms CPU"],
                       ["Student INT8 (dynamic QAT)", "<span class='num'>95.90%</span>", "<span class='num'>0.966</span>", "<span class='best'>15.5 ms CPU</span> — shipped"],
                       ["Multi-teacher KD (LAIC + DeiT)", "<span class='num'>96.16%</span>", "<span class='num'>0.951</span>", "Two teachers, more signal, slightly lower F1"]],
                      "The FP32 student matches the teacher's accuracy exactly at a fraction of the cost. Quantizing to INT8 trades 1.2 points of accuracy for another 15% latency cut — worth it for offline field use, and the honest tradeoff to state rather than hide.") +
                findings([
                    ("EXPLAINABILITY", "Grad-CAM confirms the model looks at diseased tissue",
                     "Peak activations align consistently with lesion regions rather than background — the check that separates a model that learned pathology from one that learned the photographer's habits."),
                    ("ROBUSTNESS", "Stress-tested against the conditions it will actually meet",
                     "Evaluated under busy backgrounds, additive Gaussian noise, severe blur, and random rectangular occlusion to measure behaviour under real distribution shift, not just clean test images."),
                    ("RELIABILITY", "The model is allowed to decline",
                     "Temperature scaling plus selective prediction lets it abstain on low-confidence cases, validated with risk–coverage curves and AURC — so ambiguous images route to a human instead of getting a guess."),
                ])) +
        section("Note on assets",
                "This one's charts live in the notebook.",
                "",
                '      <p class="note reveal">Unlike the other two ML projects, this repository ships as a single Jupyter notebook, so the Grad-CAM overlays, reliability diagrams, and risk–coverage curves are generated at run time rather than committed as image files. Export them from the notebook into <code>assets/img/corn/</code> and they can be dropped into this page in the same gallery format used on the other case studies.</p>\n')
    ),
)

# ------------------------------------------------------------ RDBMS
PAGES["perfume-store-rdbms.html"] = dict(
    title="Relational DBMS — E-Commerce Perfume Store",
    desc="A fully normalized (3NF) MySQL schema with PL/SQL triggers and ACID transactions behind a full-stack PHP storefront and admin dashboard.",
    eyebrow="Advanced Database Systems · Sep – Dec 2024",
    headline="The schema is the product. The storefront is just how you look at it.",
    sub="A fully normalized MySQL database with PL/SQL stored procedures, automated triggers, and ACID-compliant transactions — with a complete PHP storefront and admin dashboard built on top.",
    tags=tags(["MySQL", "PL/SQL", "3NF", "Triggers", "ACID", "PHP", "JavaScript"]),
    primary_cta=github_cta("https://github.com/mehenuf/cse311-perfume-store"),
    repo="https://github.com/mehenuf/cse311-perfume-store",
    extra_cta='<a class="btn btn-ghost" href="../index.html#contact">Ask me about this</a>',
    facts=facts([
        ("3NF", "Third normal form across every table"),
        ("Zero", "Redundant data between product, supplier and inventory"),
        ("ACID", "Transaction-safe concurrent stock control"),
        ("Full-stack", "Storefront, cart, checkout, and admin dashboard"),
    ]),
    stack=chips(["SQL", "MySQL", "PL/SQL", "PHP", "JavaScript", "jQuery", "Bootstrap", "HTML", "CSS"]),
    prev_href="corn-leaf-xai.html", prev_label="Corn Leaf XAI",
    next_href="flood-alert-system.html", next_label="Flood Alert System",
    body=(
        section("The problem",
                "An e-commerce backend has to survive concurrency, not just look correct on paper.",
                "Inventory, suppliers, and orders all change at once from multiple places. A schema that isn't properly normalized either duplicates data until it drifts out of sync, or falls apart under concurrent writes — and both failures reach the customer as a wrong stock count.",
                block([
                    "<b>Redundant data drifts.</b> Denormalized product and supplier records mean an update can silently miss a copy, and the storefront starts advertising things that aren't there.",
                    "<b>Two customers, one last unit.</b> Simultaneous checkout is a correctness problem that has to be solved at the transaction layer, not with application-level guesswork.",
                    "<b>Business rules leak.</b> If stock decrements live only in PHP, any new code path that forgets to call them corrupts the inventory.",
                ])) +
        section("The approach",
                "Model it properly, enforce it in the database, then build the store.",
                "",
                pipeline([
                    ("ERD design", "Entity-relationship modelling for products, brands, suppliers, orders, and customers before a single table existed."),
                    ("Normalize to 3NF", "No repeating groups, no partial dependencies, no transitive dependencies — redundancy designed out rather than patched."),
                    ("Triggers & stored procedures", "PL/SQL enforces stock decrements and integrity checks at the data layer, so no application path can skip them."),
                    ("Transactional checkout", "ACID transactions wrap order placement so concurrent checkouts can't oversell."),
                    ("Storefront & admin", "PHP storefront with brand filtering and cart management, plus a secure dashboard for orders and inventory."),
                ])) +
        section("Results",
                "What the design actually guarantees.",
                "",
                findings([
                    ("SCHEMA", "Redundancy designed out, not cleaned up later",
                     "Third normal form across products, brands, suppliers, and inventory means a fact is stored once and updated once — the drift problem stops being possible rather than being monitored for."),
                    ("INTEGRITY", "Rules the application layer can't bypass",
                     "Stock control and audit logging run as PL/SQL triggers and stored procedures, so they fire regardless of which code path placed the order."),
                    ("CONCURRENCY", "Checkout is transactional",
                     "ACID-compliant transactions wrap order placement, making simultaneous purchases of the last unit a resolved case rather than a race."),
                    ("PRODUCT", "A working store, not a diagram",
                     "Brand-filtered catalogue pages, cart and checkout flow, order history, and an admin dashboard covering active orders, inventory, and product management."),
                ])) +
        section("Note on assets",
                "Screenshots to add.",
                "",
                '      <p class="note reveal">This repository ships the application source rather than exported screenshots. Run it locally against MySQL and capture the storefront, cart, and admin dashboard into <code>assets/img/store/</code> — plus an export of the ERD — and they can be dropped into this page in the same gallery format used on the ML case studies.</p>\n')
    ),
)

# ------------------------------------------------------------- FLOOD
PAGES["flood-alert-system.html"] = dict(
    title="Flood Alert & Relief Coordination System",
    desc="A Firebase-backed disaster relief platform with live flood tracking, geolocation-based alert routing, and an admin dashboard for resource allocation and volunteer dispatch.",
    eyebrow="Junior Design course · May – Aug 2024",
    headline="During a flood the bottleneck usually isn't supplies. It's knowing who to send where.",
    sub="A real-time coordination platform for disaster relief: live flood tracking, forecast views, geolocation-based alert routing, and an admin dashboard tying reports of need to available volunteers and resources.",
    tags=tags(["Firebase", "JavaScript", "Geolocation", "Real-time DB", "HTML/CSS"]),
    primary_cta=github_cta("https://github.com/mehenuf/Flood-Alert-and-Relief-Coordination-System"),
    repo="https://github.com/mehenuf/Flood-Alert-and-Relief-Coordination-System",
    extra_cta='<a class="btn btn-ghost" href="../index.html#contact">Ask me about this</a>',
    facts=facts([
        ("Real-time", "Firebase-backed live flood tracking and alerts"),
        ("Geolocation", "Alerts routed by proximity, not manual triage"),
        ("Dashboard", "Single operational view of incidents and dispatch"),
        ("Forecast", "Forward-looking view alongside current conditions"),
    ]),
    stack=chips(["JavaScript", "Firebase", "Firestore", "HTML", "CSS", "Git"]),
    prev_href="perfume-store-rdbms.html", prev_label="Perfume Store RDBMS",
    next_href="cifar10-classifier.html", next_label="CIFAR-10 Classifier",
    body=(
        section("The problem",
                "Relief efforts rarely fail for lack of willingness. They fail on latency.",
                "Volunteers, supplies, and reports of need all exist during a flood — usually in three separate places, moving at the speed of phone calls. A report that waits an hour in an inbox is a household that waited an hour longer.",
                block([
                    "<b>Manual triage doesn't scale.</b> Once a disaster crosses more than a few neighbourhoods, a human reading incoming reports becomes the bottleneck.",
                    "<b>Knowing where the need is isn't enough.</b> Without a workflow matching need to available volunteers and supplies, a map of problems is just a map of problems.",
                    "<b>Nobody learns software mid-crisis.</b> Anything that needs explaining will be abandoned for a phone call the moment things get busy.",
                ])) +
        section("The approach",
                "From incoming report to dispatched volunteer, with no manual handoff.",
                "",
                pipeline([
                    ("Incident intake", "Reports of need enter through the web app with location attached."),
                    ("Live flood tracking", "A Firebase real-time layer keeps current conditions and affected areas in sync across every connected client."),
                    ("Geolocation routing", "Alerts route by proximity so the nearest available response is notified first, with no manual triage step."),
                    ("Resource allocation", "Available supplies are matched against reported need through a structured workflow."),
                    ("Dispatch & dashboard", "Volunteers are assigned to tasks and locations, with one admin view of active incidents and dispatch state."),
                ])) +
        section("Results",
                "What the platform does — and where it stands.",
                "",
                findings([
                    ("COORDINATION", "The triage step disappears",
                     "Geolocation-based routing removes the human bottleneck between a report arriving and the nearest responder hearing about it."),
                    ("REAL-TIME", "Everyone sees the same state",
                     "Firebase keeps flood conditions, incidents, and dispatch status synchronised live across every connected client — no refreshing, no conflicting copies."),
                    ("OPERATIONS", "Resource allocation as a data workflow",
                     "Supply matching and volunteer dispatch are structured pipelines rather than a contact form, which is what makes the coordination view meaningful."),
                    ("SCOPE", "A course project, honestly scoped",
                     "Built for the Junior Design course as a functional prototype. It demonstrates the routing and dispatch architecture end to end; it has not been operationally deployed with a relief organisation."),
                ])) +
        section("Note on assets",
                "Screenshots to add.",
                "",
                '      <p class="note reveal">The repository ships the application pages — <code>index.html</code>, <code>flood-tracking.html</code>, <code>forecast.html</code>, and <code>admin-dashboard.html</code> — rather than exported screenshots. Run it with your Firebase config and capture each view into <code>assets/img/flood/</code> to drop them into this page.</p>\n')
    ),
)

# =====================================================================
for fname, cfg in PAGES.items():
    out = SHELL.format(
        mailto=MAILTO, gh=GH_ICON, dl=DL, arrow_l=ARROW_L, arrow_r=ARROW_R,
        **cfg
    )
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"wrote projects/{fname}  ({len(out):,} bytes)")
