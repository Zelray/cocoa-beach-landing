import base64, os

with open('hero_b64.txt') as f:
    hero_b64 = f.read().strip()
with open('headshot_b64.txt') as f:
    headshot_b64 = f.read().strip()
with open('logo_b64.txt') as f:
    logo_b64 = f.read().strip()

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mortgage Genius | Find Your Dream Home in Cocoa Beach</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --primary: #004A7F;
      --accent: #FDB813;
      --white: #FFFFFF;
      --light-bg: #F4F8FC;
      --text-dark: #1A1A2E;
      --text-mid: #3D5A80;
      --text-light: #6B7A99;
      --shadow: 0 8px 32px rgba(0,74,127,0.12);
      --radius: 16px;
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Poppins', sans-serif; color: var(--text-dark); background: var(--white); overflow-x: hidden; }

    /* NAVBAR */
    nav {
      position: fixed; top: 0; left: 0; width: 100%; z-index: 1000;
      background: rgba(0,74,127,0.97); backdrop-filter: blur(12px);
      padding: 14px 40px; display: flex; align-items: center; justify-content: space-between;
      box-shadow: 0 2px 20px rgba(0,0,0,0.18);
    }
    .nav-logo { height: 48px; width: auto; filter: brightness(0) invert(1); }
    .nav-cta {
      background: var(--accent); color: var(--primary); font-family: 'Poppins', sans-serif;
      font-weight: 700; font-size: 0.875rem; padding: 10px 26px; border: none;
      border-radius: 50px; cursor: pointer; text-decoration: none; letter-spacing: 0.03em;
      transition: all 0.25s ease; box-shadow: 0 4px 14px rgba(253,184,19,0.35);
    }
    .nav-cta:hover { background: #ffc93c; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(253,184,19,0.5); }

    /* HERO */
    .hero {
      min-height: 100vh;
      background-image: linear-gradient(to bottom, rgba(0,30,60,0.62) 0%, rgba(0,74,127,0.45) 60%, rgba(0,20,50,0.72) 100%), url("HERO_PLACEHOLDER");
      background-size: cover; background-position: center top; background-attachment: fixed;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      text-align: center; padding: 120px 24px 80px;
    }
    .hero-badge {
      display: inline-flex; align-items: center; gap: 8px;
      background: rgba(253,184,19,0.18); border: 1.5px solid rgba(253,184,19,0.55);
      color: var(--accent); font-size: 0.78rem; font-weight: 600; letter-spacing: 0.12em;
      text-transform: uppercase; padding: 6px 18px; border-radius: 50px; margin-bottom: 28px;
    }
    .hero-badge::before { content: ''; display: inline-block; width: 7px; height: 7px; background: var(--accent); border-radius: 50%; }
    .hero h1 {
      font-size: clamp(2.4rem, 6vw, 4.2rem); font-weight: 800; color: var(--white);
      line-height: 1.15; max-width: 820px; margin-bottom: 20px; text-shadow: 0 2px 20px rgba(0,0,0,0.3);
    }
    .hero h1 span { color: var(--accent); }
    .hero p {
      font-size: clamp(1rem, 2.2vw, 1.3rem); font-weight: 300; color: rgba(255,255,255,0.88);
      max-width: 540px; margin-bottom: 44px; letter-spacing: 0.01em;
    }
    .hero-buttons { display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; }
    .btn-primary {
      background: var(--accent); color: var(--primary); font-family: 'Poppins', sans-serif;
      font-weight: 700; font-size: 1rem; padding: 16px 40px; border: none; border-radius: 50px;
      cursor: pointer; text-decoration: none; letter-spacing: 0.02em; transition: all 0.28s ease;
      box-shadow: 0 6px 24px rgba(253,184,19,0.4);
    }
    .btn-primary:hover { background: #ffc93c; transform: translateY(-3px); box-shadow: 0 10px 30px rgba(253,184,19,0.55); }
    .btn-outline {
      background: transparent; color: var(--white); font-family: 'Poppins', sans-serif;
      font-weight: 600; font-size: 1rem; padding: 15px 38px; border: 2px solid rgba(255,255,255,0.65);
      border-radius: 50px; cursor: pointer; text-decoration: none; letter-spacing: 0.02em; transition: all 0.28s ease;
    }
    .btn-outline:hover { border-color: var(--white); background: rgba(255,255,255,0.1); transform: translateY(-3px); }
    .hero-scroll { margin-top: 60px; display: flex; flex-direction: column; align-items: center; gap: 8px; color: rgba(255,255,255,0.55); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; }
    .scroll-arrow { width: 28px; height: 28px; border-right: 2px solid rgba(255,255,255,0.45); border-bottom: 2px solid rgba(255,255,255,0.45); transform: rotate(45deg); animation: bounce 1.8s infinite; }
    @keyframes bounce { 0%, 100% { transform: rotate(45deg) translateY(0); } 50% { transform: rotate(45deg) translateY(6px); } }

    /* STATS */
    .stats-strip { background: var(--primary); padding: 36px 40px; display: flex; justify-content: center; gap: 0; flex-wrap: wrap; }
    .stat-item { text-align: center; padding: 12px 48px; border-right: 1px solid rgba(255,255,255,0.18); }
    .stat-item:last-child { border-right: none; }
    .stat-number { font-size: 2.2rem; font-weight: 800; color: var(--accent); line-height: 1; margin-bottom: 4px; }
    .stat-label { font-size: 0.8rem; font-weight: 400; color: rgba(255,255,255,0.72); letter-spacing: 0.05em; text-transform: uppercase; }

    /* SECTIONS */
    section { padding: 96px 24px; }
    .section-inner { max-width: 1100px; margin: 0 auto; }
    .section-tag { display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--accent); background: rgba(253,184,19,0.12); padding: 5px 14px; border-radius: 50px; margin-bottom: 14px; }
    .section-title { font-size: clamp(1.8rem, 3.5vw, 2.6rem); font-weight: 700; color: var(--primary); line-height: 1.25; margin-bottom: 16px; }
    .section-subtitle { font-size: 1.05rem; color: var(--text-light); font-weight: 400; max-width: 560px; line-height: 1.7; }

    /* ABOUT */
    .about { background: var(--light-bg); }
    .about-grid { display: grid; grid-template-columns: 1fr 1.5fr; gap: 72px; align-items: center; }
    .about-image-wrap { position: relative; }
    .about-image-wrap::before { content: ''; position: absolute; top: -18px; left: -18px; width: 100%; height: 100%; border: 3px solid var(--accent); border-radius: 24px; z-index: 0; }
    .about-image-wrap::after { content: ''; position: absolute; bottom: -18px; right: -18px; width: 65%; height: 65%; background: var(--primary); border-radius: 16px; z-index: 0; opacity: 0.12; }
    .about-photo { position: relative; z-index: 1; width: 100%; max-width: 360px; border-radius: 20px; object-fit: cover; aspect-ratio: 3/4; box-shadow: var(--shadow); display: block; }
    .about-badge { position: absolute; bottom: 24px; right: -24px; z-index: 2; background: var(--primary); color: var(--white); padding: 14px 20px; border-radius: 14px; text-align: center; box-shadow: 0 8px 28px rgba(0,74,127,0.3); }
    .about-badge strong { display: block; font-size: 1.6rem; font-weight: 800; color: var(--accent); line-height: 1; }
    .about-badge span { font-size: 0.72rem; font-weight: 500; opacity: 0.85; letter-spacing: 0.04em; }
    .about-content { display: flex; flex-direction: column; gap: 20px; }
    .about-content p { font-size: 1.02rem; color: var(--text-mid); line-height: 1.8; }
    .about-highlights { display: flex; flex-direction: column; gap: 14px; margin-top: 8px; }
    .highlight-item { display: flex; align-items: flex-start; gap: 14px; }
    .highlight-icon { flex-shrink: 0; width: 40px; height: 40px; background: var(--primary); border-radius: 10px; display: flex; align-items: center; justify-content: center; }
    .highlight-icon svg { width: 20px; height: 20px; fill: var(--accent); }
    .highlight-text strong { display: block; font-size: 0.9rem; font-weight: 600; color: var(--primary); }
    .highlight-text span { font-size: 0.82rem; color: var(--text-light); }

    /* SERVICES */
    .services { background: var(--white); }
    .services-header { text-align: center; margin-bottom: 56px; }
    .services-header .section-subtitle { margin: 0 auto; }
    .services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
    .service-card { background: var(--light-bg); border-radius: var(--radius); padding: 36px 28px; transition: all 0.3s ease; border: 1.5px solid transparent; position: relative; overflow: hidden; }
    .service-card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: var(--accent); transform: scaleY(0); transition: transform 0.3s ease; }
    .service-card:hover { border-color: rgba(0,74,127,0.12); box-shadow: var(--shadow); transform: translateY(-6px); background: var(--white); }
    .service-card:hover::before { transform: scaleY(1); }
    .service-icon { width: 56px; height: 56px; background: var(--primary); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin-bottom: 22px; }
    .service-icon svg { width: 28px; height: 28px; fill: var(--accent); }
    .service-card h3 { font-size: 1.1rem; font-weight: 700; color: var(--primary); margin-bottom: 10px; }
    .service-card p { font-size: 0.9rem; color: var(--text-light); line-height: 1.7; }

    /* TESTIMONIALS */
    .testimonials { background: var(--primary); padding: 96px 24px; }
    .testimonials .section-title { color: var(--white); }
    .testimonials-header { text-align: center; margin-bottom: 56px; }
    .testimonials-header .section-subtitle { color: rgba(255,255,255,0.65); margin: 0 auto; }
    .testimonials-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1100px; margin: 0 auto; }
    .testimonial-card { background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12); border-radius: var(--radius); padding: 32px 28px; transition: all 0.3s ease; }
    .testimonial-card:hover { background: rgba(255,255,255,0.12); transform: translateY(-4px); }
    .stars { color: var(--accent); font-size: 1rem; letter-spacing: 2px; margin-bottom: 16px; }
    .testimonial-card p { font-size: 0.92rem; color: rgba(255,255,255,0.82); line-height: 1.75; font-style: italic; margin-bottom: 20px; }
    .testimonial-author { display: flex; align-items: center; gap: 12px; }
    .author-avatar { width: 44px; height: 44px; border-radius: 50%; background: var(--accent); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; color: var(--primary); flex-shrink: 0; }
    .author-info strong { display: block; font-size: 0.9rem; font-weight: 600; color: var(--white); }
    .author-info span { font-size: 0.78rem; color: rgba(255,255,255,0.5); }

    /* CONTACT */
    .contact { background: var(--light-bg); }
    .contact-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 64px; align-items: start; }
    .contact-info { display: flex; flex-direction: column; gap: 28px; }
    .contact-detail { display: flex; align-items: center; gap: 16px; }
    .contact-detail-icon { width: 48px; height: 48px; background: var(--primary); border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .contact-detail-icon svg { width: 22px; height: 22px; fill: var(--accent); }
    .contact-detail-text strong { display: block; font-size: 0.85rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.06em; }
    .contact-detail-text span { font-size: 0.95rem; color: var(--text-mid); }
    .contact-form { background: var(--white); border-radius: 20px; padding: 44px 40px; box-shadow: var(--shadow); }
    .contact-form h3 { font-size: 1.4rem; font-weight: 700; color: var(--primary); margin-bottom: 28px; }
    .form-group { margin-bottom: 20px; }
    .form-group label { display: block; font-size: 0.82rem; font-weight: 600; color: var(--primary); margin-bottom: 7px; letter-spacing: 0.04em; text-transform: uppercase; }
    .form-group input, .form-group textarea, .form-group select { width: 100%; padding: 13px 16px; border: 1.5px solid #D8E4EF; border-radius: 10px; font-family: 'Poppins', sans-serif; font-size: 0.92rem; color: var(--text-dark); background: var(--light-bg); transition: border-color 0.2s ease, box-shadow 0.2s ease; outline: none; }
    .form-group input:focus, .form-group textarea:focus, .form-group select:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(0,74,127,0.1); background: var(--white); }
    .form-group textarea { resize: vertical; min-height: 110px; }
    .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .btn-submit { width: 100%; background: var(--primary); color: var(--white); font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 1rem; padding: 15px; border: none; border-radius: 10px; cursor: pointer; letter-spacing: 0.03em; transition: all 0.28s ease; margin-top: 8px; }
    .btn-submit:hover { background: #003a66; box-shadow: 0 8px 24px rgba(0,74,127,0.3); transform: translateY(-2px); }

    /* FOOTER */
    footer { background: #001f3f; padding: 48px 40px 32px; text-align: center; }
    .footer-logo { height: 44px; width: auto; filter: brightness(0) invert(1); margin-bottom: 20px; }
    .footer-tagline { font-size: 0.88rem; color: rgba(255,255,255,0.5); margin-bottom: 28px; }
    .footer-divider { border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 24px auto; max-width: 400px; }
    .footer-copy { font-size: 0.78rem; color: rgba(255,255,255,0.35); }

    /* RESPONSIVE */
    @media (max-width: 900px) {
      nav { padding: 12px 20px; }
      .about-grid { grid-template-columns: 1fr; gap: 48px; }
      .about-image-wrap { max-width: 320px; margin: 0 auto; }
      .about-badge { right: 0; }
      .services-grid { grid-template-columns: 1fr 1fr; }
      .testimonials-grid { grid-template-columns: 1fr 1fr; }
      .contact-grid { grid-template-columns: 1fr; gap: 40px; }
      .stat-item { padding: 12px 24px; }
    }
    @media (max-width: 600px) {
      section { padding: 64px 20px; }
      .services-grid { grid-template-columns: 1fr; }
      .testimonials-grid { grid-template-columns: 1fr; }
      .form-row { grid-template-columns: 1fr; }
      .stats-strip { flex-direction: column; align-items: center; }
      .stat-item { border-right: none; border-bottom: 1px solid rgba(255,255,255,0.18); width: 100%; max-width: 280px; }
      .stat-item:last-child { border-bottom: none; }
      .contact-form { padding: 28px 20px; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <nav>
    <img src="LOGO_PLACEHOLDER" alt="Mortgage Genius Logo" class="nav-logo" />
    <a href="#contact" class="nav-cta">Contact Me</a>
  </nav>

  <!-- HERO -->
  <section class="hero" id="home">
    <div class="hero-badge">Cocoa Beach, Florida</div>
    <h1>Find Your Dream Home in<br /><span>Cocoa Beach</span></h1>
    <p>Your expert guide to paradise. Let's find the perfect coastal home for you.</p>
    <div class="hero-buttons">
      <a href="#contact" class="btn-primary">Contact Me Today</a>
      <a href="#about" class="btn-outline">Learn More</a>
    </div>
    <div class="hero-scroll">
      <span>Scroll</span>
      <div class="scroll-arrow"></div>
    </div>
  </section>

  <!-- STATS -->
  <div class="stats-strip">
    <div class="stat-item"><div class="stat-number">15+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat-item"><div class="stat-number">300+</div><div class="stat-label">Homes Sold</div></div>
    <div class="stat-item"><div class="stat-number">98%</div><div class="stat-label">Client Satisfaction</div></div>
    <div class="stat-item"><div class="stat-number">#1</div><div class="stat-label">Local Agent</div></div>
  </div>

  <!-- ABOUT -->
  <section class="about" id="about">
    <div class="section-inner">
      <div class="about-grid">
        <div class="about-image-wrap">
          <img src="HEADSHOT_PLACEHOLDER" alt="Michael - Real Estate Agent" class="about-photo" />
          <div class="about-badge"><strong>15+</strong><span>Years in<br />Cocoa Beach</span></div>
        </div>
        <div class="about-content">
          <div>
            <div class="section-tag">About Me</div>
            <h2 class="section-title">A Dedicated Local Expert You Can Trust</h2>
          </div>
          <p>Hi, I'm Michael — a passionate real estate professional who has called Cocoa Beach home for over 15 years. I know every neighborhood, every street, and every hidden gem this stunning coastal community has to offer. My mission is simple: to help you find not just a house, but a place where your life's best moments will unfold.</p>
          <p>Whether you're a first-time buyer dreaming of ocean breezes, a growing family seeking the perfect neighborhood, or an investor looking for prime beachside property, I bring deep local knowledge, honest guidance, and relentless dedication to every transaction.</p>
          <div class="about-highlights">
            <div class="highlight-item">
              <div class="highlight-icon"><svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div>
              <div class="highlight-text"><strong>Deep Local Knowledge</strong><span>Born and raised in Brevard County — I know every block.</span></div>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon"><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm4.24 16L12 15.45 7.77 18l1.12-4.81-3.73-3.23 4.92-.42L12 5l1.92 4.53 4.92.42-3.73 3.23L16.23 18z"/></svg></div>
              <div class="highlight-text"><strong>Award-Winning Service</strong><span>Recognized as a top producer in Brevard County for 8 consecutive years.</span></div>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon"><svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg></div>
              <div class="highlight-text"><strong>Client-First Philosophy</strong><span>Your goals are my goals — I'm with you every step of the way.</span></div>
            </div>
          </div>
          <div style="margin-top: 12px;"><a href="#contact" class="btn-primary" style="display:inline-block;">Let's Talk</a></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="services" id="services">
    <div class="section-inner">
      <div class="services-header">
        <div class="section-tag">What I Offer</div>
        <h2 class="section-title">Comprehensive Real Estate Services</h2>
        <p class="section-subtitle">From your first showing to closing day, I provide full-service support tailored to your unique needs.</p>
      </div>
      <div class="services-grid">
        <div class="service-card">
          <div class="service-icon"><svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg></div>
          <h3>Home Buying</h3>
          <p>I guide first-time buyers and seasoned investors through every step — from pre-approval to keys in hand — with clarity and confidence.</p>
        </div>
        <div class="service-card">
          <div class="service-icon"><svg viewBox="0 0 24 24"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/></svg></div>
          <h3>Market Valuation</h3>
          <p>Get an accurate, data-driven valuation of any Cocoa Beach property. I leverage the latest market data to ensure you never overpay or undersell.</p>
        </div>
        <div class="service-card">
          <div class="service-icon"><svg viewBox="0 0 24 24"><path d="M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.06 15.94 0 13.36 0c-1.46 0-2.75.67-3.64 1.71L8 3.5 6.28 1.71C5.39.67 4.1 0 2.64 0 1.06 0 0 1.06 0 2.64c0 .48.11.92.18 1.36H0v14c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zM13.36 2c.9 0 1.64.74 1.64 1.64 0 .9-.74 1.64-1.64 1.64L10 5.27l1.09-1.27c.47-.55 1.14-.9 1.86-.9l.41-.1zM2.64 2c.72 0 1.39.35 1.86.9L5.59 4.28 2.36 5.28C1.46 5.28.72 4.54.72 3.64.72 2.74 1.46 2 2.36 2h.28zM18 18H2V8h16v10z"/></svg></div>
          <h3>Relocation Services</h3>
          <p>Moving to Cocoa Beach from out of state? I specialize in seamless relocations, helping you discover the best neighborhoods for your lifestyle.</p>
        </div>
        <div class="service-card">
          <div class="service-icon"><svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 3c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm7 13H5v-.23c0-.62.28-1.2.76-1.58C7.47 15.82 9.64 15 12 15s4.53.82 6.24 2.19c.48.38.76.97.76 1.58V19z"/></svg></div>
          <h3>Buyer Representation</h3>
          <p>I represent your interests exclusively — negotiating the best price, terms, and conditions so you walk away with the best possible deal.</p>
        </div>
        <div class="service-card">
          <div class="service-icon"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg></div>
          <h3>Investment Properties</h3>
          <p>Cocoa Beach is a prime vacation rental market. I help investors identify high-yield beachside properties with strong rental income potential.</p>
        </div>
        <div class="service-card">
          <div class="service-icon"><svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg></div>
          <h3>Free Consultation</h3>
          <p>Not sure where to start? Schedule a no-obligation consultation. I'll answer your questions and help you build a clear path to homeownership.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- TESTIMONIALS -->
  <section class="testimonials" id="testimonials">
    <div class="section-inner">
      <div class="testimonials-header">
        <div class="section-tag">Client Stories</div>
        <h2 class="section-title">What My Clients Say</h2>
        <p class="section-subtitle">Real stories from real people who found their dream home in Cocoa Beach.</p>
      </div>
      <div class="testimonials-grid">
        <div class="testimonial-card">
          <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p>"Michael made our dream of owning a beachfront home a reality. His knowledge of the Cocoa Beach market is unmatched, and he was with us every single step of the way."</p>
          <div class="testimonial-author">
            <div class="author-avatar">JR</div>
            <div class="author-info"><strong>James &amp; Rachel T.</strong><span>Bought in Cocoa Beach, 2024</span></div>
          </div>
        </div>
        <div class="testimonial-card">
          <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p>"As a first-time buyer relocating from Chicago, I was nervous. Michael's patience and expertise turned what could have been a stressful experience into an exciting adventure."</p>
          <div class="testimonial-author">
            <div class="author-avatar">SP</div>
            <div class="author-info"><strong>Sarah P.</strong><span>Relocated from Chicago, 2024</span></div>
          </div>
        </div>
        <div class="testimonial-card">
          <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p>"We were looking for an investment property and Michael found us a gem. The rental income has exceeded our projections. We couldn't be happier with our decision."</p>
          <div class="testimonial-author">
            <div class="author-avatar">DM</div>
            <div class="author-info"><strong>David M.</strong><span>Investment Property, 2023</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CONTACT -->
  <section class="contact" id="contact">
    <div class="section-inner">
      <div class="contact-grid">
        <div class="contact-info">
          <div>
            <div class="section-tag">Get In Touch</div>
            <h2 class="section-title">Ready to Find Your Dream Home?</h2>
            <p class="section-subtitle">Reach out today for a free, no-obligation consultation. I'd love to help you find your perfect place in paradise.</p>
          </div>
          <div class="contact-detail">
            <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></div>
            <div class="contact-detail-text"><strong>Phone</strong><span>(321) 555-0192</span></div>
          </div>
          <div class="contact-detail">
            <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
            <div class="contact-detail-text"><strong>Email</strong><span>michael@mortgagegenius.com</span></div>
          </div>
          <div class="contact-detail">
            <div class="contact-detail-icon"><svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div>
            <div class="contact-detail-text"><strong>Office</strong><span>400 N Atlantic Ave, Cocoa Beach, FL 32931</span></div>
          </div>
        </div>
        <div class="contact-form">
          <h3>Send Me a Message</h3>
          <div class="form-row">
            <div class="form-group"><label for="fname">First Name</label><input type="text" id="fname" placeholder="John" /></div>
            <div class="form-group"><label for="lname">Last Name</label><input type="text" id="lname" placeholder="Doe" /></div>
          </div>
          <div class="form-group"><label for="email">Email Address</label><input type="email" id="email" placeholder="john@example.com" /></div>
          <div class="form-group"><label for="phone">Phone Number</label><input type="tel" id="phone" placeholder="(321) 555-0000" /></div>
          <div class="form-group">
            <label for="interest">I'm Interested In</label>
            <select id="interest">
              <option value="">Select an option...</option>
              <option>Buying a Home</option>
              <option>Investment Property</option>
              <option>Relocation Services</option>
              <option>Free Consultation</option>
            </select>
          </div>
          <div class="form-group"><label for="message">Message</label><textarea id="message" placeholder="Tell me about your dream home..."></textarea></div>
          <button class="btn-submit" type="button">Send Message</button>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <img src="LOGO_PLACEHOLDER" alt="Mortgage Genius Logo" class="footer-logo" />
    <p class="footer-tagline">Your expert guide to paradise in Cocoa Beach, Florida.</p>
    <hr class="footer-divider" />
    <p class="footer-copy">&copy; 2026 Mortgage Genius. All rights reserved. | Cocoa Beach, FL 32931</p>
  </footer>

</body>
</html>"""

# Inject base64 images
html = html.replace('HERO_PLACEHOLDER', f'data:image/jpeg;base64,{hero_b64}')
html = html.replace('HEADSHOT_PLACEHOLDER', f'data:image/jpeg;base64,{headshot_b64}')
html = html.replace('LOGO_PLACEHOLDER', f'data:image/png;base64,{logo_b64}')

with open('index.html', 'w') as f:
    f.write(html)

size = os.path.getsize('index.html')
print(f"index.html written: {size:,} bytes ({size/1024/1024:.2f} MB)")
